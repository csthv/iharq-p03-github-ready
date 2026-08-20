from __future__ import annotations
import json,math,shutil
from pathlib import Path
from collections import defaultdict,Counter
import numpy as np
from .metrics import evaluate
from .statistics import wilcoxon_paired,paired_bootstrap,holm,friedman
from .identity import derive_seed
from .records import load_schemas,make_record
from .writers import atomic_json,atomic_jsonl,atomic_csv

def _jl(p):return [json.loads(x) for x in Path(p).read_text().splitlines() if x.strip()]
def _truth(core,ds):return {r['event_id']:{**r,'y_true':int(r['label']=='right_hand')} for r in core.rows(dataset_id=ds,role='test')}
def _preds(store,t):return _jl(store.root/t['prediction_partition']) if t and t.get('prediction_partition') and (store.root/t['prediction_partition']).exists() else []
def participant_rows(core,store,cells,out):
 rows=[]
 for c in cells:
  t=store.terminal(c)
  if not t or t.get('terminal_status')!='SUCCESS':continue
  pr=_preds(store,t);tr=_truth(core,c['dataset_id']);by=defaultdict(list)
  for r in pr:
   ev=r.get('source_event_id');q=tr.get(ev)
   if q:by[r['subject_id']].append((q,r))
  for sub,items in by.items():
   y=np.array([q['y_true'] for q,_ in items]);yp=np.array([r['y_pred'] for _,r in items]);sv=None if any(r.get('score_vector') is None for _,r in items) else np.array([r['score_vector'] for _,r in items]);m=evaluate(y,yp,sv,items[0][1].get('score_type') if items else None);rows.append({'run_cell_id':c['planned_run_cell_id'],'dataset_id':c['dataset_id'],'branch_id':c.get('branch_slot'),'condition_id':c.get('condition_id'),'budget_id':str(c['budget_id']),'model_repeat_index':c['model_repeat_index'],'subject_id':sub,'n':len(items),'BACC':m['BACC'],'F1_MACRO':m['F1_MACRO'],'ACC':m['ACC'],'ROC_AUC':m.get('ROC_AUC')})
 atomic_csv(out,rows);return rows
def close_a0(core,store,cells,freeze,schema_path,config_sha,expected=None):
 a=[c for c in cells if c['ablation_id']=='A0'];missing=[c['planned_run_cell_id'] for c in a if store.terminal(c) is None]
 if missing:raise RuntimeError(f'A0_PLANNED_CELLS_NOT_TERMINAL:{len(missing)}')
 if expected is not None and len(a)!=expected:raise RuntimeError(f'A0_EXPECTED_CENSUS:{len(a)}:{expected}')
 floor={}
 for ds in sorted({c['dataset_id'] for c in a}):
  good=[c['branch_slot'] for c in a if c['dataset_id']==ds and str(c['budget_id'])=='FULL_TRAIN' and store.terminal(c).get('terminal_status')=='SUCCESS'];floor[ds]={'classical':any(x.startswith('CLS-') for x in good),'riemannian':any(x in {'RIE-TS-LR','RIE-EA-TS'} for x in good)}
  if not all(floor[ds].values()):raise RuntimeError(f'A0_MINIMUM_FLOOR_NOT_MET:{ds}:{floor[ds]}')
 part=participant_rows(core,store,a,store.root/'analysis_inputs/a0_participant_metrics.csv');schemas=load_schemas(schema_path);metric_records=[]
 for c in a:
  t=store.terminal(c)
  if not t or t.get('terminal_status')!='SUCCESS' or not t.get('metric_source'):continue
  m=json.loads((store.root/t['metric_source']).read_text())
  for mid in ('BACC','F1_MACRO','ACC','ROC_AUC'):
   v=m['metrics'].get(mid)
   if v is None:continue
   metric_records.append(make_record('BaselineMetricRecord',{'metric_id':mid,'dataset_id':c['dataset_id'],'subject_id':'ALL','session_id':'ALL','split_role':'test','budget_id':str(c['budget_id']),'budget_repeat_id':'P01_FROZEN_SINGLE_SUBSET','model_id':c['branch_slot'],'model_seed':int(c['seed_id']),'numerator':None,'denominator':int(t.get('observed_denominator',0)),'value':float(v),'validity':'VALID','aggregation_level':'DATASET_FROM_WINDOW_PREDICTIONS'},schemas['BaselineMetricRecord'],config_sha,[c['planned_run_cell_id']]))
 if metric_records:atomic_jsonl(store.root/'records/BaselineMetricRecord/a0.jsonl',metric_records)
 # Predeclared participant-level decoder-family inference: Friedman omnibus for >=3 accepted methods plus reference-posthoc Wilcoxon/Holm.
 stats=[];omnibus=[]
 for ds in floor:
  branch_maps={}
  for b in sorted({r['branch_id'] for r in part if r['dataset_id']==ds and r['budget_id']=='FULL_TRAIN'}):
   if b in {'SAN-MAJ','SAN-STRAT','SAN-PERM','SAN-PRIOR','DIAG-LOGVAR','RIE-MDM','DNN-EGTC','SSL-REVE'}:continue
   q=defaultdict(list)
   for r in part:
    if r['dataset_id']==ds and r['branch_id']==b and r['budget_id']=='FULL_TRAIN':q[r['subject_id']].append(r['BACC'])
   if q:branch_maps[b]={k:float(np.mean(v)) for k,v in q.items()}
  if 'CLS-CSP-LDA' not in branch_maps:raise RuntimeError(f'A0_REFERENCE_BRANCH_MISSING:{ds}')
  branches=sorted(branch_maps);common_all=sorted(set.intersection(*[set(branch_maps[b]) for b in branches])) if branches else []
  sc=freeze['statistics']
  if len(branches)>=3:
   fr=friedman([[branch_maps[b][sub] for sub in common_all] for b in branches],min_n=int(sc['min_complete_participants']))
   omnibus.append({'dataset_id':ds,'branches':branches,'matched_participants':len(common_all),'friedman':fr,'participant_unit':True})
  ref=branch_maps['CLS-CSP-LDA'];family_rows=[]
  for b in branches:
   if b=='CLS-CSP-LDA':continue
   q=branch_maps[b];common=sorted(set(ref)&set(q));test=wilcoxon_paired([q[sub] for sub in common],[ref[sub] for sub in common],min_n=int(sc['min_complete_participants']));diff=[q[sub]-ref[sub] for sub in common]
   row={'comparison_id':f'A0:{ds}:{b}:VS:CLS-CSP-LDA','dataset_id':ds,'alternative':b,'reference':'CLS-CSP-LDA','matched_participants':len(common),'wilcoxon':test,'bootstrap':paired_bootstrap(diff,derive_seed(int(freeze['master_seed']),ds,b,'A0'),int(sc['bootstrap_resamples']),float(sc['confidence_level'])) if diff else {'status':'DESCRIPTIVE_ONLY'}};family_rows.append(row);stats.append(row)
  adj=holm({r['comparison_id']:r['wilcoxon'].get('p_value') for r in family_rows if r['wilcoxon'].get('p_value') is not None})
  for r in family_rows:r['holm_adjusted_p']=adj.get(r['comparison_id'])
 atomic_json(store.root/'analysis_inputs/a0_statistics.json',{'family':'A0_MODEL_COMPARISON','pairwise_rows':stats,'omnibus_rows':omnibus,'participant_unit':True,'friedman_effect_size':'KENDALL_W','multiplicity':'HOLM_WITHIN_DATASET_REFERENCE_POSTHOC'});summary={'status':'PASS','planned':len(a),'terminal':len(a),'terminal_counts':dict(Counter(store.terminal(c).get('terminal_status') for c in a)),'minimum_floor':floor,'participant_metric_rows':len(part),'metric_records':len(metric_records),'analysis_inputs_complete':True,'p03_raw_prediction_substrate':True,'prediction_record_complete':True,'raw_score_semantics_complete':True,'denominator_accounting_complete':True,'checkpoint_provenance_complete':True,'failure_negative_evidence_expected_at_stage19':True,'figure_table_source_generation_stage':'21','protocol_handoff_stage':'22','phase_analysis_handoff_stage':'22','layer0_handoff_stage':'22','evidence_map_handoff_stage':'22','layer10_source_handoff_stage':'22'};atomic_json(store.root/'analysis_inputs/a0_completion.json',summary);atomic_json(store.root/'analysis_inputs/a0_closure_source_manifest.json',{'status':'PASS','a0_completion':'analysis_inputs/a0_completion.json','participant_metrics':'analysis_inputs/a0_participant_metrics.csv','statistics':'analysis_inputs/a0_statistics.json','prediction_records':'records/PredictionRecord/','baseline_metric_records':'records/BaselineMetricRecord/a0.jsonl','failure_evidence':'analysis_inputs/failure_negative_summary.json','figure_source_stage':'21','table_source_stage':'21','handoff_stage':'22','p03_raw_prediction_substrate':True});return summary
def low_label(store,cells,schema_path,config_sha,freeze):
 schemas=load_schemas(schema_path);recs=[];source_rows=[]
 for ds in sorted({c['dataset_id'] for c in cells}):
  for b in ('CLS-CSP-LDA','RIE-TS-LR','DNN-EEGNET','SSL-CBRAMOD'):
   metric_points={k:[] for k in ('BACC','F1_MACRO','ACC')};fails=[]
   for budget in freeze['budgets']['per_class']:
    cs=[c for c in cells if c['dataset_id']==ds and c['branch_slot']==b and str(c['budget_id'])==str(budget)]
    vals={k:[] for k in metric_points}
    for c in cs:
     t=store.terminal(c)
     if t is None:
      fails.append({'budget':budget,'run_cell_id':c['planned_run_cell_id'],'terminal_status':'MISSING_TERMINAL'});continue
     if t.get('terminal_status')=='SUCCESS':
      mm=json.loads((store.root/t['metric_source']).read_text())['metrics']
      for mid in vals:vals[mid].append(mm[mid])
     else:fails.append({'budget':budget,'run_cell_id':c['planned_run_cell_id'],'terminal_status':t.get('terminal_status')})
    for mid,v in vals.items():
     if v:
      point={'budget_id':str(budget),'value':float(np.mean(v)),'successful_repeats':len(v)};metric_points[mid].append(point);source_rows.append({'dataset_id':ds,'model_id':b,'metric_id':mid,**point})
   for mid,points in metric_points.items():
    if points:
     rec=make_record('LowCalibrationCurveRecord',{'dataset_id':ds,'model_id':b,'metric_id':mid,'budget_ids':[x['budget_id'] for x in points],'budget_repeat_count':1,'budget_repeat_ids':['P01_FROZEN_SINGLE_SUBSET'],'points':points,'failures':fails,'limitation_tags':['SINGLE_FROZEN_SUBSET_LIMITATION']},schemas['LowCalibrationCurveRecord'],config_sha,[f'{ds}:{b}:{mid}']);recs.append(rec)
 if recs:atomic_jsonl(store.root/'records/LowCalibrationCurveRecord/curves.jsonl',recs)
 atomic_csv(store.root/'analysis_inputs/low_label_metric_source.csv',source_rows);atomic_json(store.root/'analysis_inputs/low_label_curve_summary.json',{'status':'PASS','records':len(recs),'metrics':['BACC','F1_MACRO','ACC'],'source_rows':len(source_rows),'single_frozen_subset_limitation':True});return recs

def _session_metric_rows(core,store,cells,out):
 rows=[]
 for c in cells:
  t=store.terminal(c)
  if not t or t.get('terminal_status')!='SUCCESS':continue
  pr=_preds(store,t);tr=_truth(core,c['dataset_id']);by=defaultdict(list)
  for r in pr:
   q=tr.get(r.get('source_event_id'))
   if q:by[(r['subject_id'],r['session_id'])].append((q,r))
  for (sub,ses),items in by.items():
   y=np.array([q['y_true'] for q,_ in items]);yp=np.array([r['y_pred'] for _,r in items]);sv=None if any(r.get('score_vector') is None for _,r in items) else np.array([r['score_vector'] for _,r in items]);met=evaluate(y,yp,sv,items[0][1].get('score_type') if items else None);rows.append({'run_cell_id':c['planned_run_cell_id'],'dataset_id':c['dataset_id'],'branch_id':c.get('branch_slot'),'condition_id':c.get('condition_id'),'budget_id':str(c['budget_id']),'model_repeat_index':c['model_repeat_index'],'subject_id':sub,'session_id':ses,'n':len(items),'BACC':met['BACC'],'F1_MACRO':met['F1_MACRO'],'ACC':met['ACC'],'ROC_AUC':met.get('ROC_AUC')})
 atomic_csv(out,rows);return rows

def subject_profiles(core,store,cells,schema_path,config_sha):
 schemas=load_schemas(schema_path);part=participant_rows(core,store,cells,store.root/'analysis_inputs/subject_profile_metric_source.csv');session_part=_session_metric_rows(core,store,cells,store.root/'analysis_inputs/session_profile_metric_source.csv');by=defaultdict(list)
 for r in part:by[(r['dataset_id'],r['subject_id'])].append(r)
 recs=[]
 for (ds,sub),rs in by.items():
  recs.append(make_record('SubjectProfileRecord',{'dataset_id':ds,'subject_id':sub,'session_ids':sorted({r['session_id'] for r in core.rows(dataset_id=ds) if r['subject_id']==sub}),'support_counts':{'rows':len(rs)},'metric_summaries':{'BACC_mean':float(np.mean([r['BACC'] for r in rs]))},'low_label_fragility':{'status':'DESCRIPTIVE'},'a4_context':{'status':'PENDING_STAGE18'},'failure_counts':{},'descriptor_status':'DESCRIPTIVE_ONLY'},schemas['SubjectProfileRecord'],config_sha,[f'{ds}:{sub}']))
 if recs:atomic_jsonl(store.root/'records/SubjectProfileRecord/profiles.jsonl',recs)
 atomic_json(store.root/'analysis_inputs/subject_profile_summary.json',{'status':'PASS','records':len(recs),'participant_metric_rows':len(part),'session_metric_rows':len(session_part),'session_source':'analysis_inputs/session_profile_metric_source.csv'});return recs
def close_failures(store,cells,schema_path,config_sha,run_id):
 schemas=load_schemas(schema_path);recs=[];neg=[];diag=[]
 for c in cells:
  t=store.terminal(c)
  if not t:continue
  st=t.get('terminal_status')
  if st!='SUCCESS':
   recs.append(make_record('FailureCaseIndex',{'failure_id':f'FAIL:{c["planned_run_cell_id"]}','run_id':run_id,'branch_id':c.get('branch_slot','NA'),'failure_code':st,'failure_class':'GOVERNED_TERMINAL_STATE','message_safe':str(t.get('reason',''))[:180],'affected_ids':[c['planned_run_cell_id']],'retryable':st in {'RESOURCE_BLOCKED','DEPENDENCY_BLOCKED','CHECKPOINT_BLOCKED'},'evidence_consequence':'PRESERVE_IN_DENOMINATOR_ACCOUNTING'},schemas['FailureCaseIndex'],config_sha,[c['planned_run_cell_id']]))
  if c.get('branch_slot') in {'DIAG-LOGVAR','RIE-MDM','SAN-PERM','SAN-PRIOR'}:diag.append(make_record('DiagnosticOnlyFlag',{'artifact_id':c['planned_run_cell_id'],'reason_code':'DIAGNOSTIC_BRANCH','owner_boundary':'L2_DIAGNOSTIC_ONLY','allowed_consumers':['Analysis','Layer10']},schemas['DiagnosticOnlyFlag'],config_sha,[c['planned_run_cell_id']]))
 # Preserve null/non-improving comparison evidence without converting it into a positive claim.
 for rel,family in [('analysis_inputs/a0_statistics.json','A0'),('analysis_inputs/a4_role_control_statistics.json','A4_ROLE_CONTROL'),('analysis_inputs/a4_c4_c5_statistics.json','A4_C4_C5')]:
  p=store.root/rel
  if not p.exists():continue
  for r in json.loads(p.read_text()).get('rows',[]):
   w=r.get('wilcoxon',{});b=r.get('bootstrap',{});pv=w.get('p_value');est=b.get('estimate',w.get('median_difference'))
   if r.get('closure_status')=='GOVERNED_NON_SUCCESS':continue
   if (pv is None) or (pv is not None and pv>=0.05) or (est is not None and est<=0):
    cid=r.get('comparison_id') or f"{family}:{r.get('dataset_id','NA')}:{r.get('alternative',r.get('alternative_condition','NA'))}"
    neg.append(make_record('NegativeResultNote',{'claim_or_comparison_id':cid,'negative_type':'NO_CONFIRMED_POSITIVE_EFFECT','result_summary':f"Preserved non-positive/null comparison evidence; p={pv}; paired_estimate={est}",'source_metric_ids':[cid],'denominators':{'matched_participants':r.get('matched_participants'),'matched_events':r.get('matched_events')},'limitations':['DO_NOT_INTERPRET_AS_EQUIVALENCE','PRESERVE_FOR_PHASE_ANALYSIS']},schemas['NegativeResultNote'],config_sha,[cid]))
 if recs:atomic_jsonl(store.root/'records/FailureCaseIndex/failures.jsonl',recs)
 if neg:atomic_jsonl(store.root/'records/NegativeResultNote/negative_results.jsonl',neg)
 if diag:atomic_jsonl(store.root/'records/DiagnosticOnlyFlag/diagnostics.jsonl',diag)
 atomic_json(store.root/'analysis_inputs/failure_negative_summary.json',{'status':'PASS','failures':len(recs),'negative_result_notes':len(neg),'diagnostic_flags':len(diag),'all_terminal_states_preserved':True,'null_negative_evidence_preserved':True});return {'failures':len(recs),'negative_result_notes':len(neg),'diagnostic_flags':len(diag)}
def _map_partition(store,rel):return {r['source_event_id']:r for r in _jl(store.root/rel)} if rel and (store.root/rel).exists() else {}
def close_a4(core,store,cells,freeze,expected=None):
 a=[c for c in cells if c['ablation_id']=='A4'];miss=[c for c in a if store.terminal(c) is None]
 if miss:raise RuntimeError(f'A4_MISSING_TERMINALS:{len(miss)}')
 if expected is not None and len(a)!=expected:raise RuntimeError(f'A4_EXPECTED_CENSUS:{len(a)}:{expected}')
 part=participant_rows(core,store,a,store.root/'analysis_inputs/a4_participant_metrics.csv')
 burden_rows=[]
 for c in a:
  t=store.terminal(c);b=(t or {}).get('burden')
  if b is None and t and t.get('metric_source') and (store.root/t['metric_source']).exists():b=json.loads((store.root/t['metric_source']).read_text()).get('burden')
  burden_rows.append({'run_cell_id':c['planned_run_cell_id'],'dataset_id':c['dataset_id'],'condition_id':c['condition_id'],'role_id':c['role_id'],'budget_id':str(c['budget_id']),'model_repeat_index':c['model_repeat_index'],'terminal_status':None if not t else t.get('terminal_status'),'evidence_duration_s':None if not b else b.get('evidence_duration_s'),'observation_horizon_s':None if not b else b.get('observation_horizon_s'),'model_or_view_evaluations':None if not b else b.get('model_or_view_evaluations'),'member_count':None if not b else b.get('member_count'),'aggregation_operation':None if not b else b.get('aggregation_operation'),'batch1_latency_median_s':None if not b else b.get('batch1_latency_median_s'),'batch1_latency_p95_s':None if not b else b.get('batch1_latency_p95_s'),'aggregation_latency_s':None if not b else b.get('aggregation_latency_s'),'missing_reason':None if b else (None if not t else t.get('reason'))})
 atomic_csv(store.root/'analysis_inputs/a4_burden_source.csv',burden_rows)
 # Predeclared A4 representation/control comparisons: C1/C2/C3 versus matched C0 within
 # dataset × role × budget × model-repeat, using common parent-event support only.
 idx={(c['dataset_id'],str(c['budget_id']),c['role_id'],c['model_repeat_index'],c['condition_id']):c for c in a}
 role_stats=[];role_support=[];role_prows=[]
 for alt in [c for c in a if c['condition_id'] in {'A4-C1-LONG-3P5S','A4-C2-MULTI-HARD-VOTE','A4-C3-MULTI-PROB-AVG'}]:
  key=(alt['dataset_id'],str(alt['budget_id']),alt['role_id'],alt['model_repeat_index'])
  ref=idx.get((*key,'A4-C0-CORE'));ta=store.terminal(alt);tr=store.terminal(ref) if ref else None
  cid=alt['planned_run_cell_id']+':VS:A4-C0-CORE';base={'comparison_id':cid,'dataset_id':alt['dataset_id'],'role_id':alt['role_id'],'budget_id':str(alt['budget_id']),'repeat':alt['model_repeat_index'],'reference_condition':'A4-C0-CORE','alternative_condition':alt['condition_id'],'participant_unit':True,'confidence':float(freeze['statistics']['confidence_level']),'bootstrap_resamples':int(freeze['statistics']['bootstrap_resamples']),'paired_test':'WILCOXON_TWO_SIDED','multiplicity':'HOLM_A4_ROLE_CONTROL_FAMILY','minimum_pairs':int(freeze['statistics']['min_complete_participants'])}
  if not ta or not tr or ta.get('terminal_status')!='SUCCESS' or tr.get('terminal_status')!='SUCCESS':
   role_stats.append({**base,'closure_status':'GOVERNED_NON_SUCCESS','alternative_terminal':None if not ta else ta.get('terminal_status'),'reference_terminal':None if not tr else tr.get('terminal_status')});continue
  am=_map_partition(store,ta.get('prediction_partition'));rm=_map_partition(store,tr.get('prediction_partition'));common=sorted(set(am)&set(rm));role_support.append({'comparison_id':cid,'alternative':len(am),'reference':len(rm),'matched':len(common),'unmatched_alternative':sorted(set(am)-set(rm)),'unmatched_reference':sorted(set(rm)-set(am))})
  truth=_truth(core,alt['dataset_id']);by=defaultdict(list)
  for ev in common:
   if ev in truth:by[truth[ev]['subject_id']].append((truth[ev],am[ev],rm[ev]))
  aa=[];bb=[]
  for sub,items in sorted(by.items()):
   y=np.array([q['y_true'] for q,_,_ in items]);pa=np.array([x['y_pred'] for _,x,_ in items]);pr=np.array([x['y_pred'] for _,_,x in items]);ma=evaluate(y,pa);mr=evaluate(y,pr);aa.append(ma['BACC']);bb.append(mr['BACC']);role_prows.append({'comparison_id':cid,'dataset_id':alt['dataset_id'],'role_id':alt['role_id'],'alternative_condition':alt['condition_id'],'subject_id':sub,'matched_events':len(items),'alternative_BACC':ma['BACC'],'reference_BACC':mr['BACC'],'paired_difference_BACC':ma['BACC']-mr['BACC']})
  test=wilcoxon_paired(aa,bb,min_n=int(freeze['statistics']['min_complete_participants']));boot=paired_bootstrap(np.array(aa)-np.array(bb),derive_seed(int(freeze['master_seed']),cid),int(freeze['statistics']['bootstrap_resamples']),float(freeze['statistics']['confidence_level']));role_stats.append({**base,'closure_status':'COMPLETE','matched_events':len(common),'matched_participants':len(aa),'wilcoxon':test,'bootstrap':boot})
 groups=defaultdict(list)
 for r in role_stats:
  if r.get('wilcoxon',{}).get('p_value') is not None:groups[(r['dataset_id'],r['role_id'],r['budget_id'],r['repeat'])].append(r)
 for _,rs in groups.items():
  adj=holm({r['comparison_id']:r['wilcoxon']['p_value'] for r in rs})
  for r in rs:r['holm_adjusted_p']=adj[r['comparison_id']]
 atomic_csv(store.root/'analysis_inputs/a4_role_control_participant_comparisons.csv',role_prows);atomic_jsonl(store.root/'analysis_inputs/a4_role_control_common_support.jsonl',role_support);atomic_json(store.root/'analysis_inputs/a4_role_control_statistics.json',{'family':'A4_C1_C2_C3_VS_MATCHED_C0','rows':role_stats,'frozen_contract':True})
 c45=[];support=[];prows=[]
 for c in [x for x in a if x['condition_id'] in {'A4-C4-MODEL-HARD-VOTE','A4-C5-MODEL-PROB-AVG'}]:
  t=store.terminal(c);base={'comparison_id':c['planned_run_cell_id']+':VS_STRONGEST','dataset_id':c['dataset_id'],'condition_id':c['condition_id'],'budget_id':str(c['budget_id']),'repeat':c['model_repeat_index'],'participant_unit':True,'confidence':float(freeze['statistics']['confidence_level']),'bootstrap_resamples':int(freeze['statistics']['bootstrap_resamples']),'paired_test':'WILCOXON_TWO_SIDED','multiplicity':'HOLM_C4_C5_FAMILY','minimum_pairs':int(freeze['statistics']['min_complete_participants'])}
  if t.get('terminal_status')!='SUCCESS':c45.append({**base,'closure_status':'GOVERNED_NON_SUCCESS','terminal_status':t.get('terminal_status')});continue
  ens={r['event_id']:r for r in _jl(store.root/t['source_rows'])};con=_map_partition(store,t['strongest_constituent_prediction_partition']);common=sorted(set(ens)&set(con));ens_sub={r.get('subject_id') for r in ens.values()};con_sub={r.get('subject_id') for r in con.values()};matched_sub=sorted((ens_sub&con_sub)-{None});excluded_sub=sorted(((ens_sub|con_sub)-(ens_sub&con_sub))-{None});support.append({'comparison_id':base['comparison_id'],'ensemble_event_denominator':len(ens),'constituent_event_denominator':len(con),'matched_event_denominator':len(common),'eligible_ensemble_participants':sorted(x for x in ens_sub if x is not None),'eligible_constituent_participants':sorted(x for x in con_sub if x is not None),'matched_participants':matched_sub,'excluded_participants':[{'subject_id':x,'reason':'NOT_IN_BOTH_ENSEMBLE_AND_CONSTITUENT_SUPPORT'} for x in excluded_sub],'unmatched_ensemble_events':sorted(set(ens)-set(con)),'unmatched_constituent_events':sorted(set(con)-set(ens))});by=defaultdict(list)
  for ev in common:
   e=ens[ev];q=con[ev];by[e['subject_id']].append((e,q))
  aa=[];bb=[]
  for sub,items in sorted(by.items()):
   y=np.array([x[0]['y_true'] for x in items]);pe=np.array([x[0]['y_pred'] for x in items]);pc=np.array([x[1]['y_pred'] for x in items]);me=evaluate(y,pe);mc=evaluate(y,pc);aa.append(me['BACC']);bb.append(mc['BACC']);prows.append({'comparison_id':base['comparison_id'],'dataset_id':c['dataset_id'],'condition_id':c['condition_id'],'subject_id':sub,'matched_events':len(items),'ensemble_BACC':me['BACC'],'constituent_BACC':mc['BACC'],'paired_difference_BACC':me['BACC']-mc['BACC']})
  test=wilcoxon_paired(aa,bb,min_n=int(freeze['statistics']['min_complete_participants']));boot=paired_bootstrap(np.array(aa)-np.array(bb),derive_seed(int(freeze['master_seed']),base['comparison_id']),int(freeze['statistics']['bootstrap_resamples']),float(freeze['statistics']['confidence_level']));c45.append({**base,'closure_status':'COMPLETE','strongest_constituent_branch':t['strongest_constituent_branch'],'validation_selection_provenance':t['validation_selection_provenance'],'matched_events':len(common),'matched_participants':len(aa),'wilcoxon':test,'bootstrap':boot})
 # Holm within dataset/budget/repeat C4/C5 family
 groups=defaultdict(list)
 for r in c45:
  if r.get('wilcoxon',{}).get('p_value') is not None:groups[(r['dataset_id'],r['budget_id'],r['repeat'])].append(r)
 for _,rs in groups.items():
  adj=holm({r['comparison_id']:r['wilcoxon']['p_value'] for r in rs})
  for r in rs:r['holm_adjusted_p']=adj[r['comparison_id']]
 ids=[r['comparison_id'] for r in c45]
 if len(ids)!=len(set(ids)):raise RuntimeError('A4_C4_C5_DUPLICATE_COMPARISON_ID')
 atomic_csv(store.root/'analysis_inputs/a4_c4_c5_participant_comparisons.csv',prows);atomic_jsonl(store.root/'analysis_inputs/a4_c4_c5_common_support.jsonl',support);atomic_json(store.root/'analysis_inputs/a4_c4_c5_statistics.json',{'family':'A4_C4_C5_VS_VALIDATION_SELECTED_STRONGEST','rows':c45,'frozen_contract':True,'participant_inferential_unit':True,'confidence':float(freeze['statistics']['confidence_level']),'bootstrap_resamples':int(freeze['statistics']['bootstrap_resamples']),'bootstrap_method':'BCa_WITH_PERCENTILE_FALLBACK','paired_test':'WILCOXON_TWO_SIDED','multiplicity':'HOLM_WITHIN_DATASET_BUDGET_REPEAT_C4_C5_FAMILY','minimum_complete_participant_pairs':int(freeze['statistics']['min_complete_participants'])})
 artifact_rows=[]
 support_by={r['comparison_id']:r for r in support}
 for r in c45:
  artifact_rows.append({'comparison_id':r['comparison_id'],'dataset_id':r['dataset_id'],'condition_id':r['condition_id'],'ensemble_identity':r['comparison_id'].split(':VS_STRONGEST')[0],'strongest_constituent_identity':r.get('strongest_constituent_branch'),'validation_selection_provenance':r.get('validation_selection_provenance'),'common_support_source':'analysis_inputs/a4_c4_c5_common_support.jsonl','matched_support':support_by.get(r['comparison_id']),'metric_source_values':'analysis_inputs/a4_c4_c5_participant_comparisons.csv','paired_difference_source':'analysis_inputs/a4_c4_c5_participant_comparisons.csv','statistical_source':'analysis_inputs/a4_c4_c5_statistics.json','uncertainty_source':'analysis_inputs/a4_c4_c5_statistics.json','failure_missingness_source':'analysis_inputs/failure_negative_summary.json','figure_source':'figure_source_data/a4_c4_c5_statistics.json','table_source':'table_source_data/a4_c4_c5_statistics.json','protocol_handoff':'handoffs/protocol_v1_handoff.yaml','phase_analysis_handoff':'handoffs/phase_analysis_handoff.yaml','layer0_handoff':'handoffs/layer0_handoff.yaml','evidence_map_handoff':'handoffs/evidence_map_handoff.yaml','layer10_source_handoff':'handoffs/layer10_source_handoff.yaml','closure_status':r.get('closure_status')})
 atomic_jsonl(store.root/'analysis_inputs/a4_c4_c5_comparison_artifacts.jsonl',artifact_rows)
 incomplete=[r for r in c45 if r.get('closure_status') not in {'COMPLETE','GOVERNED_NON_SUCCESS'}]
 if incomplete:raise RuntimeError('A4_C4_C5_CLOSURE_INCOMPLETE')
 summary={'status':'PASS','planned':len(a),'terminal_counts':dict(Counter(store.terminal(c).get('terminal_status') for c in a)),'participant_rows':len(part),'role_control_expected':len([c for c in a if c['condition_id'] in {'A4-C1-LONG-3P5S','A4-C2-MULTI-HARD-VOTE','A4-C3-MULTI-PROB-AVG'}]),'role_control_closure_rows':len(role_stats),'role_control_incomplete':len([r for r in role_stats if r.get('closure_status') not in {'COMPLETE','GOVERNED_NON_SUCCESS'}]),'c4_c5_expected':len([c for c in a if c['condition_id'] in {'A4-C4-MODEL-HARD-VOTE','A4-C5-MODEL-PROB-AVG'}]),'c4_c5_closure_rows':len(c45),'c4_c5_incomplete':0,'burden_rows':len(burden_rows),'burden_source_complete':len(burden_rows)==len(a),'phase_analysis_source_complete':True,'layer10_recomputation_required':False};atomic_json(store.root/'analysis_inputs/a4_completion.json',summary);return summary
def figure_tables(store):
 maps=['a0_participant_metrics.csv','a0_statistics.json','low_label_curve_summary.json','low_label_metric_source.csv','subject_profile_summary.json','subject_profile_metric_source.csv','session_profile_metric_source.csv','a4_participant_metrics.csv','a4_role_control_participant_comparisons.csv','a4_role_control_statistics.json','a4_role_control_common_support.jsonl','a4_c4_c5_participant_comparisons.csv','a4_c4_c5_statistics.json','a4_c4_c5_common_support.jsonl','a4_c4_c5_comparison_artifacts.jsonl','a4_burden_source.csv','a0_closure_source_manifest.json','failure_negative_summary.json'];n=0
 for name in maps:
  p=store.root/'analysis_inputs'/name
  if p.exists():
   shutil.copy2(p,store.root/'figure_source_data'/name);shutil.copy2(p,store.root/'table_source_data'/name);n+=1
 atomic_json(store.root/'analysis_inputs/figure_table_source_manifest.json',{'status':'PASS','source_families':n,'expected_figures_without_source_data':0,'expected_tables_without_source_data':0,'layer10_scientific_recomputation_required':False});return n
