from __future__ import annotations
import json,time,numpy as np
from collections import defaultdict
from .models import make_adapter
from .data import frozen_budget_memberships
from .metrics import evaluate,hard_vote,probability_average
from .checkpoints import save_roundtrip
from .records import load_schemas,make_record
from .scientific import branch_grid,_payload_prediction
from .writers import atomic_jsonl,atomic_json

ROLE_POOLS={'CLASSICAL':{'full':['CLS-CSP-LDA','CLS-FBCSP-LR'],'low':['CLS-CSP-LDA']},'RIEMANNIAN':{'full':['RIE-TS-LR','RIE-EA-TS'],'low':['RIE-TS-LR']},'NEURAL':{'full':['DNN-EEGNET','DNN-FBCNET','DNN-SEQ'],'low':['DNN-EEGNET']},'SSL':{'full':['SSL-CBRAMOD'],'low':['SSL-CBRAMOD']}}
def _j(p):return json.loads(p.read_text())
def _jl(p):return [json.loads(x) for x in p.read_text().splitlines() if x.strip()]
def a0_term(store,ds,b,budget,rep):
 ps=list((store.root/'run_cells').glob(f'P02-A0-{ds}-{b}-{budget}-MR{int(rep):02d}*.json')) or (list((store.root/'run_cells').glob(f'P02-A0-{ds}-{b}-{budget}-MR00*.json')) if rep else [])
 good=[_j(p) for p in ps if _j(p).get('terminal_status')=='SUCCESS'];return good[0] if good else None
def select_reps(store,ds,budget):
 low=str(budget)!='FULL_TRAIN';out={};prov={}
 for role,pool in ROLE_POOLS.items():
  cand=[]
  for b in pool['low' if low else 'full']:
   ms=[]
   for p in (store.root/'metrics').glob(f'P02-A0-{ds}-{b}-{budget}-*.json'):
    d=_j(p);v=d.get('validation_selection');
    if v and np.isfinite(v.get('BACC',np.nan)):ms.append(d)
   if ms:cand.append({'branch_id':b,'BACC':float(np.median([x['validation_selection']['BACC'] for x in ms])),'F1':float(np.median([x['validation_selection']['F1_MACRO'] for x in ms])),'burden':float(np.median([x.get('validation_burden_seconds',float('inf')) for x in ms]))})
  if cand:
   cand.sort(key=lambda x:(-x['BACC'],-x['F1'],x['burden'],x['branch_id']));out[role]=cand[0]['branch_id'];prov[role]=cand
 return out,prov
def strongest(store,ds,budget,branches):
 c=[]
 for b in sorted(set(branches)):
  ms=[]
  for p in (store.root/'metrics').glob(f'P02-A0-{ds}-{b}-{budget}-*.json'):
   d=_j(p);v=d.get('validation_selection');
   if v and np.isfinite(v.get('BACC',np.nan)):ms.append(d)
  if ms:c.append({'branch_id':b,'BACC':float(np.median([x['validation_selection']['BACC'] for x in ms])),'F1':float(np.median([x['validation_selection']['F1_MACRO'] for x in ms])),'burden':float(np.median([x.get('validation_burden_seconds',float('inf')) for x in ms]))})
 if not c:raise RuntimeError('A4_STRONGEST_CONSTITUENT_VALIDATION_EVIDENCE_MISSING')
 c.sort(key=lambda x:(-x['BACC'],-x['F1'],x['burden'],x['branch_id']));return {'selected_branch':c[0]['branch_id'],'candidate_summaries':c,'test_outcome_influence':'PROHIBITED'}
def _train(a4,core,ds,budget,freeze):
 if str(budget)=='FULL_TRAIN':return a4.rows(dataset_id=ds,role='train')
 seed=int(freeze['budgets']['seed']);ids=frozen_budget_memberships(core,budgets=freeze['budgets']['per_class'],seed=seed)[f'{ds}:budget-{int(budget)}-seed-{seed}'];return [r for r in a4.rows(dataset_id=ds,role='calibration') if r['event_id'] in ids]
def _params(store,ds,b,budget,rep):
 t=a0_term(store,ds,b,budget,rep);return {} if not t else _j(store.root/t['metric_source']).get('selected_params',{})
def _fit_member(c,store,core,a4,b,member,schema_path,config_sha,freeze,fixture=False,implementation_bindings=None,runtime_overrides=None):
 ds=c['dataset_id'];budget=c['budget_id'];rep=c['model_repeat_index'];key=f'{ds}__{budget}__{b}__{rep}__{member or "LONG"}';meta=store.root/'diagnostics'/f'A4MEM-{key}.json';rowsf=store.root/'diagnostics'/f'A4MEM-{key}.jsonl'
 if meta.exists() and rowsf.exists():
  old=_j(meta)
  if old.get('config_sha256')==config_sha:return {**old,'rows':_jl(rowsf)}
 tr=_train(a4,core,ds,budget,freeze);va=a4.rows(dataset_id=ds,role='validation');te=a4.rows(dataset_id=ds,role='test');X,y,_=a4.load_rows(tr,member);Xv,yv,_=a4.load_rows(va,member);Xt,yt,rows=a4.load_rows(te,member);p=_params(store,ds,b,budget,rep);pp={**dict((implementation_bindings or {}).get(b,{}) or {}),**p,**dict(runtime_overrides or {}),**({'fixture_non_scientific_adapter':True} if fixture and b.startswith('RIE-') else {})};m=make_adapter(b,int(c['seed_id']),X.shape[-1],X.shape[1],pp)
 if hasattr(m,'admission'):
  a=m.admission()
  if a['status']!='ADMITTED':return {'status':a['status'],'reason':a}
 try:
  if b.startswith('DNN-'):
   import torch
   m.fit(X,y,epochs=1 if fixture else int(freeze['neural_training']['max_epochs']),lr=float(p.get('lr',1e-3)),weight_decay=float(p.get('weight_decay',0.0)),batch_size=int((runtime_overrides or {}).get('batch_size',16 if fixture else freeze['neural_training']['effective_batch_target'])),effective_batch_target=int(freeze['neural_training']['effective_batch_target']),device='cuda' if torch.cuda.is_available() else 'cpu',X_val=Xv,y_val=yv,patience=1 if fixture else int(freeze['neural_training']['patience']),min_delta=float(freeze['neural_training']['min_delta']),restore_best=bool(freeze['neural_training']['restore_best']))
  else:m.fit(X,y)
 except (ImportError,ModuleNotFoundError) as e:return {'status':'DEPENDENCY_BLOCKED','reason':type(e).__name__}
 except ResourceWarning as e:return {'status':'RESOURCE_BLOCKED','reason':str(e)[:200]}
 except Exception as e:return {'status':'FAILED','reason':f'{type(e).__name__}:{str(e)[:200]}'}
 # Measured batch-1 inference burden; this is runtime/resource evidence, not model selection.
 times=[]
 for _ in range(5):
  t0=time.perf_counter();_p=m.predict(Xt[:1]);_s=m.scores(Xt[:1]);times.append(time.perf_counter()-t0)
 pred=m.predict(Xt);scores=m.scores(Xt);chk=save_roundtrip(m,Xt[:4],store.root/'checkpoints'/f'A4MEM-{key}.pkl')
 if chk['status']!='PASS':return {'status':'INVALID','reason':'CHECKPOINT_RELOAD_FAILURE'}
 src=[]
 for i,(r,yp) in enumerate(zip(rows,pred)):src.append({'dataset_id':ds,'event_id':r['event_id'],'window_id':r['window_id'],'window_record_id':r['window_record_id'],'subject_id':r['subject_id'],'session_id':r['session_id'],'split_record_id':r['split_record_id'],'role':r['role'],'y_true':int(yt[i]),'y_pred':int(yp),'score_vector':None if scores is None else np.asarray(scores[i]).tolist(),'score_type':m.score_type})
 atomic_jsonl(rowsf,src);out={'status':'SUCCESS','config_sha256':config_sha,'branch':b,'checkpoint_sha256':chk['checkpoint_sha256'],'model_id':f'{b}:A4:{key}','score_type':m.score_type,'latency_summary':{'batch1_latency_median_s':float(np.median(times)),'batch1_latency_p95_s':float(np.quantile(times,.95)),'repeats':len(times)}};atomic_json(meta,out);return {**out,'rows':src}
def _write_agg(c,store,src,member_models,member_chks,agg,schema_path,config_sha,burden):
 schemas=load_schemas(schema_path);mid=f'A4-AGG:{c["planned_run_cell_id"]}';chk='AGG:'+__import__('hashlib').sha256('|'.join(member_chks).encode()).hexdigest();prs=[]
 for r in src:prs.append(make_record('PredictionRecord',_payload_prediction({'dataset_id':r['dataset_id'],'subject_id':r['subject_id'],'session_id':r['session_id'],'event_id':r['event_id'],'window_id':r['window_id'],'split_record_id':r['split_record_id'],'role':r['role']},mid,agg,chk,int(c['seed_id']),r['y_pred'],r.get('score_type',agg),r.get('score_vector'),c['budget_id']),schemas['PredictionRecord'],config_sha,[c['planned_run_cell_id'],r['window_record_id']]))
 pp=store.write_records('PredictionRecord',c,prs);er=make_record('EnsembleControlRecord',{'control_id':c['condition_id'],'a4_profile':'P01-L1-A4-WINDOW-FAMILY-FREEZE-R2','member_model_ids':member_models,'member_checkpoint_ids':member_chks,'aggregation_rule':agg,'matched_parent_ids':[r['event_id'] for r in src],'tie_count':0,'unresolved_tie_count':0,'missing_member_count':0,'evidence_duration_s':float(burden['evidence_duration_s']),'latency_summary':{'batch1_latency_median_s':burden.get('batch1_latency_median_s'),'batch1_latency_p95_s':burden.get('batch1_latency_p95_s'),'aggregation_latency_s':burden.get('aggregation_latency_s')}},schemas['EnsembleControlRecord'],config_sha,[c['planned_run_cell_id']]);store.write_records('EnsembleControlRecord',c,[er]);return str(pp.relative_to(store.root))
def execute_role(c,store,core,a4,reps,schema_path,config_sha,freeze,data_contract,fixture=False,implementation_bindings=None,runtime_overrides=None):
 old=store.terminal(c)
 if old:return old
 b=reps.get(c['role_id']);
 if not b:return store.write_terminal(c,'NOT_APPLICABLE_REPEAT_SLOT',reason='NO_VALIDATION_SELECTED_REPRESENTATIVE')
 cond=c['condition_id']
 if cond=='A4-C0-CORE':
  t=a0_term(store,c['dataset_id'],b,c['budget_id'],c['model_repeat_index']);
  if not t:return store.write_terminal(c,'NOT_APPLICABLE_REPEAT_SLOT',reason='A0_REPEAT_UNAVAILABLE')
  ib=t.get('inference_burden',{}) or {};burden={'evidence_duration_s':float(data_contract['core_window']['duration_s']),'observation_horizon_s':float(data_contract['core_window']['duration_s']),'model_or_view_evaluations':1,'member_count':1,'aggregation_operation':'DIRECT_CORE','batch1_latency_median_s':ib.get('batch1_latency_median_s'),'batch1_latency_p95_s':ib.get('batch1_latency_p95_s'),'aggregation_latency_s':0.0};return store.write_terminal(c,'SUCCESS',resolved_branch=b,prediction_partition=t['prediction_partition'],metric_source=t['metric_source'],checkpoint_sha256=t['checkpoint_sha256'],observed_denominator=t.get('observed_denominator'),burden=burden)
 if cond=='A4-C1-LONG-3P5S':parts=[_fit_member(c,store,core,a4,b,None,schema_path,config_sha,freeze,fixture,implementation_bindings,runtime_overrides)]
 elif cond in {'A4-C2-MULTI-HARD-VOTE','A4-C3-MULTI-PROB-AVG'}:parts=[_fit_member(c,store,core,a4,b,i,schema_path,config_sha,freeze,fixture,implementation_bindings,runtime_overrides) for i in (1,2,3)]
 else:raise RuntimeError('A4_ROLE_CONDITION_INVALID')
 if any(x['status']!='SUCCESS' for x in parts):return store.write_terminal(c,parts[0]['status'] if parts else 'FAILED',reason='A4_MEMBER_UNAVAILABLE',member_states=parts)
 maps=[{r['event_id']:r for r in p['rows']} for p in parts];common=sorted(set.intersection(*[set(m) for m in maps]));truth={r['event_id']:r for r in core.rows(dataset_id=c['dataset_id'],role='test')};common=[x for x in common if x in truth]
 if not common:return store.write_terminal(c,'INVALID',reason='EMPTY_COMMON_SUPPORT')
 if len(parts)==1:src=[maps[0][ev] for ev in common];agg='DIRECT_LONG';agg_time=0.0
 else:
  preds=[np.array([m[e]['y_pred'] for e in common]) for m in maps]
  t0=time.perf_counter()
  if cond.endswith('HARD-VOTE'):yp,t=hard_vote(preds);scores=None;agg='HARD_VOTE'
  else:
   if any(any(m[e].get('score_vector') is None for e in common) for m in maps):return store.write_terminal(c,'NOT_APPLICABLE_SCORE_SEMANTICS',reason='MISSING_NATIVE_PROBABILITY')
   if any(any(m[e].get('score_type') not in {'NATIVE_PROBABILITY','SOFTMAX_PROBABILITY','PROBABILITY'} for e in common) for m in maps):return store.write_terminal(c,'NOT_APPLICABLE_SCORE_SEMANTICS',reason='NON_GOVERNED_MEMBER_PROBABILITY')
   scores=probability_average([np.array([m[e]['score_vector'] for e in common],float) for m in maps]);yp=scores.argmax(1);agg='PROBABILITY_AVERAGE'
  agg_time=time.perf_counter()-t0
  src=[]
  for i,e in enumerate(common):
   r=maps[0][e];src.append({**r,'y_pred':int(yp[i]),'score_vector':None if scores is None else scores[i].tolist(),'score_type':agg})
 lat=[p.get('latency_summary',{}).get('batch1_latency_median_s') for p in parts if p.get('latency_summary',{}).get('batch1_latency_median_s') is not None];lat95=[p.get('latency_summary',{}).get('batch1_latency_p95_s') for p in parts if p.get('latency_summary',{}).get('batch1_latency_p95_s') is not None]
 if cond in {'A4-C2-MULTI-HARD-VOTE','A4-C3-MULTI-PROB-AVG'}: evidence_duration=float(data_contract['a4_multi']['member_duration_s']); horizon=float(data_contract['a4_multi']['observation_horizon_s'])
 else: evidence_duration=float(data_contract['a4_long']['duration_s']); horizon=evidence_duration
 burden={'evidence_duration_s':evidence_duration,'observation_horizon_s':horizon,'model_or_view_evaluations':len(parts),'member_count':len(parts),'aggregation_operation':agg,'batch1_latency_median_s':float(np.sum(lat)) if lat else None,'batch1_latency_p95_s':float(np.sum(lat95)) if lat95 else None,'aggregation_latency_s':float(agg_time)};pp=_write_agg(c,store,src,[p['model_id'] for p in parts],[p['checkpoint_sha256'] for p in parts],agg,schema_path,config_sha,burden);met=evaluate([r['y_true'] for r in src],[r['y_pred'] for r in src],None if any(r.get('score_vector') is None for r in src) else [r['score_vector'] for r in src],src[0].get('score_type') if src else None);mp=store.metric(c,{'metrics':met,'validation_selected_branch':b,'observed_denominator':len(src),'condition_id':cond,'burden':burden});raw=store.root/'raw_outputs'/f"{c['planned_run_cell_id']}.jsonl";atomic_jsonl(raw,src);return store.write_terminal(c,'SUCCESS',resolved_branch=b,prediction_partition=pp,metric_source=str(mp.relative_to(store.root)),source_rows=str(raw.relative_to(store.root)),observed_denominator=len(src),burden=burden)
def _valid_probability_record(r):
 if r.get('score_vector') is None or r.get('class_order')!=['left_hand','right_hand']:
  return False
 if r.get('score_type') not in {'NATIVE_PROBABILITY','SOFTMAX_PROBABILITY','PROBABILITY','PROBABILITY_AVERAGE'}:
  return False
 try:p=np.asarray(r['score_vector'],float)
 except (TypeError,ValueError):return False
 return p.shape==(2,) and np.all(np.isfinite(p)) and np.all(p>=0) and np.all(p<=1) and abs(float(p.sum())-1.0)<=1e-5
def _member_partition_valid(t,rows):
 chk=t.get('checkpoint_sha256')
 if not chk:return False,'CHECKPOINT_MISSING'
 if any(r.get('checkpoint_id')!=chk for r in rows):return False,'CHECKPOINT_MISMATCH'
 if any(r.get('class_order')!=['left_hand','right_hand'] for r in rows):return False,'CLASS_ORDER_MISMATCH'
 return True,None
def execute_ensemble(c,store,core,reps,schema_path,config_sha,data_contract):
 old=store.terminal(c)
 if old:return old
 members=[]
 for role in ('CLASSICAL','RIEMANNIAN','NEURAL','SSL'):
  b=reps.get(role)
  if not b:continue
  t=a0_term(store,c['dataset_id'],b,c['budget_id'],c['model_repeat_index'])
  if t and t.get('prediction_partition'):
   rows=_jl(store.root/t['prediction_partition']);ok,reason=_member_partition_valid(t,rows)
   if not ok:return store.write_terminal(c,'NOT_APPLICABLE_SCORE_SEMANTICS' if reason=='CLASS_ORDER_MISMATCH' else 'INVALID',reason=('MEMBER_PROBABILITY_OR_CLASS_ORDER_UNAVAILABLE' if reason=='CLASS_ORDER_MISMATCH' else reason),affected_branch=b)
   members.append((role,b,t,rows))
 if not {'CLASSICAL','RIEMANNIAN'} <= {x[0] for x in members}:return store.write_terminal(c,'NOT_APPLICABLE_REPEAT_SLOT',reason='MINIMUM_ENSEMBLE_ROLES_NOT_AVAILABLE')
 sel=strongest(store,c['dataset_id'],c['budget_id'],[x[1] for x in members]);strong=sel['selected_branch'];maps={b:{r['source_event_id']:r for r in rs} for _,b,_,rs in members};common=sorted(set.intersection(*[set(m) for m in maps.values()]));truth={r['event_id']:r for r in core.rows(dataset_id=c['dataset_id'],role='test')};common=[e for e in common if e in truth]
 if not common:return store.write_terminal(c,'INVALID',reason='A4_C4_C5_EMPTY_COMMON_SUPPORT')
 if c['condition_id']=='A4-C4-MODEL-HARD-VOTE':
  t0=time.perf_counter();yp,ties=hard_vote([np.array([m[e]['y_pred'] for e in common]) for m in maps.values()]);agg_time=time.perf_counter()-t0;scores=None;agg='HARD_VOTE'
 else:
  probs=[]
  for b,m in maps.items():
   rs=[m[e] for e in common]
   if any(not _valid_probability_record(r) for r in rs):return store.write_terminal(c,'NOT_APPLICABLE_SCORE_SEMANTICS',reason='MEMBER_PROBABILITY_OR_CLASS_ORDER_UNAVAILABLE',affected_branch=b)
   probs.append(np.array([r['score_vector'] for r in rs],float))
  t0=time.perf_counter();scores=probability_average(probs);yp=scores.argmax(1);agg_time=time.perf_counter()-t0;agg='PROBABILITY_AVERAGE';ties=0
 src=[]
 for i,e in enumerate(common):
  q=truth[e];src.append({'dataset_id':c['dataset_id'],'event_id':e,'window_id':q['window_id'],'window_record_id':q['window_record_id'],'subject_id':q['subject_id'],'session_id':q['session_id'],'split_record_id':q['split_record_id'],'role':q['role'],'y_true':int(q['label']=='right_hand'),'y_pred':int(yp[i]),'score_vector':None if scores is None else scores[i].tolist(),'score_type':agg})
 chks=[x[2]['checkpoint_sha256'] for x in members];dur=float(data_contract['core_window']['duration_s']);member_lat=[x[2].get('inference_burden',{}).get('batch1_latency_median_s') for x in members if x[2].get('inference_burden',{}).get('batch1_latency_median_s') is not None];member_p95=[x[2].get('inference_burden',{}).get('batch1_latency_p95_s') for x in members if x[2].get('inference_burden',{}).get('batch1_latency_p95_s') is not None];burden={'evidence_duration_s':dur,'observation_horizon_s':dur,'model_or_view_evaluations':len(members),'member_count':len(members),'aggregation_operation':agg,'batch1_latency_median_s':float(np.sum(member_lat)) if member_lat else None,'batch1_latency_p95_s':float(np.sum(member_p95)) if member_p95 else None,'aggregation_latency_s':float(agg_time)};pp=_write_agg(c,store,src,[x[1] for x in members],chks,agg,schema_path,config_sha,burden);strongt=next(x[2] for x in members if x[1]==strong);raw=store.root/'raw_outputs'/f"{c['planned_run_cell_id']}.jsonl";atomic_jsonl(raw,src);mp=store.metric(c,{'metrics':evaluate([r['y_true'] for r in src],[r['y_pred'] for r in src],scores,agg),'strongest_constituent_branch':strong,'strongest_constituent_prediction_partition':strongt['prediction_partition'],'validation_selection_provenance':sel,'matched_denominator':len(common),'ensemble_member_branches':[x[1] for x in members],'ensemble_member_checkpoint_ids':chks,'burden':burden});return store.write_terminal(c,'SUCCESS',prediction_partition=pp,source_rows=str(raw.relative_to(store.root)),metric_source=str(mp.relative_to(store.root)),strongest_constituent_branch=strong,strongest_constituent_prediction_partition=strongt['prediction_partition'],strongest_constituent_checkpoint_sha256=strongt['checkpoint_sha256'],validation_selection_provenance=sel,ensemble_member_branches=[x[1] for x in members],ensemble_member_checkpoint_ids=chks,observed_denominator=len(common),burden=burden)
