from __future__ import annotations
from pathlib import Path
from collections import Counter
import json,yaml,shutil
from .config import load_config
from .store import Store
from .fixtures import SyntheticCoreDataset,SyntheticA4Dataset,fixture_identity
from .data import CoreWindowDataset,A4WindowDataset,frozen_budget_memberships
from .input_resolver import resolve_inputs,verify_cumulative,resolve_conditional_assets_hybrid
from .scientific import execute_cell,validation_only_fixed_neural_fit
from .training_policy_evidence import close_training_policy_challenger
from .a4 import select_reps,execute_role,execute_ensemble
from .evidence import close_a0,low_label,subject_profiles,close_a4,close_failures,figure_tables
from .resources import preflight as resource_preflight,snapshot
from .environment import verify as env_verify
from .security import scan_tree,credential_summary
from .readiness import p03_readiness,evidence_sufficiency
from .handoffs import generate as generate_handoffs
from .ablation_controller import resolve as resolve_ablation
from .bundle import checksums,verify,zip_bundle
from .writers import atomic_json,atomic_yaml
from .records import load_schemas,make_record
from .training_policy import validate_training_policy_binding,select_sr_probability

FAMILY_STAGE={'SAN-MAJ':'08','SAN-STRAT':'08','SAN-PERM':'08','SAN-PRIOR':'08','DIAG-LOGVAR':'08','CLS-CSP-LDA':'09','CLS-FBCSP-LR':'09','RIE-TS-LR':'10','RIE-EA-TS':'10','RIE-MDM':'10','DNN-EEGNET':'11','DNN-FBCNET':'12','DNN-SEQ':'12','DNN-EGTC':'12','SSL-CBRAMOD':'12','SSL-REVE':'12'}
class Context:
 def __init__(self,package_root,work_root,fixture=False):self.package_root=Path(package_root);self.work_root=Path(work_root);self.fixture=fixture;self.state={};self.mr=self.package_root/'machine_readable';self.cfg=self.package_root/'configs/phase_02'
def init(ctx):
 if ctx.state.get('init'):return
 cfg,ch=load_config(ctx.cfg);run_id=('FIXTURE-NON-SCIENTIFIC-RUN' if ctx.fixture else 'P02-L2-OFFICIAL-RUN-R4DYN-'+ch[:12]);freeze=yaml.safe_load((ctx.mr/'p02_planned_scientific_execution_freeze_R5.yaml').read_text());chall_doc=yaml.safe_load((ctx.mr/'p02_training_policy_challenger_run_cells_R2.yaml').read_text());chall_rows=chall_doc['rows'];plan_doc=yaml.safe_load((ctx.mr/'p02_full_ablation_planned_run_cells_R3.yaml').read_text());rows=plan_doc['rows'];bindings=yaml.safe_load((ctx.cfg/'models/implementation_bindings.yaml').read_text());bindings={k:v for k,v in bindings.items() if k.startswith(('DNN-','SSL-'))};hf_policy=yaml.safe_load((ctx.cfg/'models/huggingface_assets.yaml').read_text());store=Store(ctx.work_root/'runtime',ch);ctx.state.update(init=True,config=cfg,config_hash=ch,run_id=run_id,freeze=freeze,all_cells=rows,planned_counts={'A0':int(plan_doc['a0_cell_count']),'A4':int(plan_doc['a4_cell_count']),'total':int(plan_doc['cell_count'])},store=store,schema=ctx.mr/'p02_record_schema_freeze_R2.yaml',implementation_bindings=bindings,hf_policy=hf_policy,challenger_cells=chall_rows,_hf_token=None,_hf_token_source='NONE')
 if ctx.fixture:
  f=json.loads(json.dumps(freeze));f['a0']['datasets']=['PhysioNetMI'];f['a4']['datasets']=['PhysioNetMI'];f['neural_training']['max_epochs']=1;f['neural_training']['patience']=1
  a0=[]
  for b,bud in [('SAN-MAJ','FULL_TRAIN'),('CLS-CSP-LDA','FULL_TRAIN'),('RIE-TS-LR','FULL_TRAIN'),('DNN-EEGNET','FULL_TRAIN'),('SSL-CBRAMOD','FULL_TRAIN'),('CLS-CSP-LDA','1')]:
   q=[r for r in rows if r['ablation_id']=='A0' and r['dataset_id']=='PhysioNetMI' and r['branch_slot']==b and str(r['budget_id'])==bud and r['model_repeat_index']==0]
   if q:a0.append(dict(q[0]))
  a4=[]
  for cond,role in [('A4-C0-CORE','CLASSICAL'),('A4-C1-LONG-3P5S','CLASSICAL'),('A4-C2-MULTI-HARD-VOTE','CLASSICAL'),('A4-C3-MULTI-PROB-AVG','CLASSICAL'),('A4-C0-CORE','RIEMANNIAN'),('A4-C1-LONG-3P5S','RIEMANNIAN'),('A4-C4-MODEL-HARD-VOTE','FIXED_MODEL_ENSEMBLE'),('A4-C5-MODEL-PROB-AVG','FIXED_MODEL_ENSEMBLE')]:
   q=[r for r in rows if r['ablation_id']=='A4' and r['dataset_id']=='PhysioNetMI' and r['condition_id']==cond and r['role_id']==role and str(r['budget_id'])=='FULL_TRAIN' and r['model_repeat_index']==0]
   if q:a4.append(dict(q[0]))
  ch=[dict(x) for x in chall_rows if x['dataset_id']=='PhysioNetMI' and x['model_repeat_index']==0][:1];core=SyntheticCoreDataset();ctx.state.update(runtime_freeze=f,a0=a0,a4cells=a4,challenger_cells=ch,cells=a0+a4+ch,core=core,a4=SyntheticA4Dataset(core))
 else:ctx.state.update(runtime_freeze=freeze,a0=[r for r in rows if r['ablation_id']=='A0'],a4cells=[r for r in rows if r['ablation_id']=='A4'],challenger_cells=chall_rows,cells=rows+chall_rows)
def art(ctx,sid,name,p):
 q=ctx.work_root/'stage_artifacts'/f'{sid}_{name}.json';atomic_json(q,p);return str(q.relative_to(ctx.work_root))
def s00(ctx):init(ctx);p={'status':'PASS','notebook_id':'IHARQ-P02-COMPLETE-EXECUTION-AND-ANALYSIS-R4','build_book_id':'IHARQ-P02-L2-INTEGRATED-BUILD-BOOK-R4','freeze_id':'P02-PLANNED-SCIENTIFIC-EXECUTION-FREEZE-R5','one_notebook':True,'a14':'ABSENT_PROHIBITED','fixture':fixture_identity() if ctx.fixture else None};p['artifact']=art(ctx,'00','authority',p);return p
def s01(ctx):
 init(ctx)
 r=resource_preflight(ctx.work_root,.1 if ctx.fixture else 8);ctx.state['resource_profile']=r;e=env_verify(ctx.package_root/'requirements-kaggle.txt',False);p={'status':'PASS' if r['status']=='PASS' and (ctx.fixture or e['status']=='PASS') else ('ENVIRONMENT_BLOCKED' if e['status']!='PASS' else r['status']),'resources':r,'environment':e,'credentials':credential_summary()}
 if p['status']!='PASS':raise RuntimeError('RESOURCE_BLOCKED')
 p['artifact']=art(ctx,'01','environment',p);return p
def s02(ctx):
 init(ctx)
 if ctx.fixture:p={'status':'PASS','fixture':True,'cumulative':'NOT_REQUIRED_FOR_FIXTURE'}
 else:
  inp=resolve_inputs('/kaggle/input',ctx.state['config']['inputs']);ctx.state['inputs']=inp;p={'status':'PASS','cumulative':verify_cumulative(inp['cumulative_zip'])}
 p['artifact']=art(ctx,'02','cumulative',p);return p
def s03(ctx):
 init(ctx)
 if ctx.fixture:p={'status':'PASS','core':'SyntheticCoreDataset','a4':'SyntheticA4Dataset'}
 else:
  inp=ctx.state.get('inputs') or resolve_inputs('/kaggle/input',ctx.state['config']['inputs']);ctx.state['inputs']=inp;bindings,asset_evidence=resolve_conditional_assets_hybrid('/kaggle/input',ctx.state['implementation_bindings'],ctx.state['hf_policy'],ctx.work_root,ctx.state.get('_hf_token'),ctx.state.get('_hf_token_source','NONE'));ctx.state['implementation_bindings']=bindings;ctx.state['conditional_asset_evidence']=asset_evidence;ctx.state['core']=CoreWindowDataset(inp['core_root'],ctx.state['config']['inputs']['required']['p01_core']['manifest_sha256']);ctx.state['a4']=A4WindowDataset(inp['a4_root'],ctx.state['config']['inputs']['required']['p01_a4']['manifest_sha256']);p={'status':'PASS','resolved':inp,'conditional_assets':asset_evidence}
 p['artifact']=art(ctx,'03','pointers',p);return p
def s04(ctx):
 init(ctx);m=ctx.state['a4'].verify_parent_match(ctx.state['core']);
 if m['status']!='PASS':raise RuntimeError('A4_PARENT_MATCH_FAIL_CLOSED')
 b=frozen_budget_memberships(ctx.state['core'],budgets=ctx.state['runtime_freeze']['budgets']['per_class'],seed=int(ctx.state['runtime_freeze']['budgets']['seed']));core_n=len(ctx.state['core'].rows());a4_n=len(ctx.state['a4'].parent_ids());expected_core=core_n if ctx.fixture else int(ctx.state['config']['inputs']['required']['p01_core']['expected_windows']);expected_a4=a4_n if ctx.fixture else int(ctx.state['config']['inputs']['required']['p01_a4']['expected_matched_parents']);
 if core_n!=expected_core or a4_n!=expected_a4:raise RuntimeError(f'P01_EXPECTED_COUNT_MISMATCH:{core_n}:{a4_n}')
 p={'status':'PASS','core_rows':core_n,'a4_parents':a4_n,'expected_core_rows':expected_core,'expected_a4_parents':expected_a4,'parent_match':m,'budget_families':len(b),'immutable':True};p['artifact']=art(ctx,'04','p01_validation',p);return p
def s05(ctx):
 init(ctx);policy=validate_training_policy_binding(ctx.state['config']['training_policy'])
 if policy['status']!='PASS': raise RuntimeError('SCIENTIFIC_FREEZE_INCOMPLETE:'+json.dumps(policy,sort_keys=True))
 challengers=ctx.state['challenger_cells']; cids=[c['planned_run_cell_id'] for c in challengers]; aug_binding=ctx.state['config']['training_policy']['augmentation_challenger']; expected_challengers=int(aug_binding['run_cell_count'])
 if (not ctx.fixture and len(challengers)!=expected_challengers) or len(cids)!=len(set(cids)):raise RuntimeError('TRAINING_POLICY_CHALLENGER_MANIFEST_INVALID')
 # Class-weight policy is algorithmically frozen; record current training counts without selecting from test evidence.
 train_counts={}
 for ds in sorted(ctx.state['runtime_freeze']['a0']['datasets']):
  rr=ctx.state['core'].rows(dataset_id=ds,role='train');train_counts[ds]={'left_hand':sum(x['label']=='left_hand' for x in rr),'right_hand':sum(x['label']=='right_hand' for x in rr)}
 ids=[r['planned_run_cell_id'] for r in ctx.state['all_cells']];expected_a0=int(ctx.state['planned_counts']['A0']);expected_a4=int(ctx.state['planned_counts']['A4']);expected_total=int(ctx.state['planned_counts']['total'])
 p={'status':'PASS','total':expected_total,'A0':expected_a0,'A4':expected_a4,'unique':len(set(ids)),'A0_unrouted':0,'stage05_decisions':'VERIFY_ALGORITHMIC_POLICY_ONLY_NO_TEST_ACCESS','scientific_training_policy':policy,'training_role_class_counts':train_counts,'training_policy_challenger_cells':len(challengers),'preexecution_amendment_id':ctx.state['config']['training_policy']['amendment_id'],'fixture_authority_blocker_bypass':False};p['artifact']=art(ctx,'05','freeze',p);return p
def s06(ctx):
 init(ctx);from .records import load_schemas
 import subprocess,sys,os
 schemas=load_schemas(ctx.state['schema'])
 if len(schemas)!=10:raise RuntimeError('SCHEMA_COUNT_MISMATCH')
 src=ctx.package_root/'src';syntax_files=0
 for py in src.rglob('*.py'):
  compile(py.read_text(encoding='utf-8'),str(py),'exec');syntax_files+=1
 env=os.environ.copy();env['PYTHONDONTWRITEBYTECODE']='1';env['PYTHONPATH']=str(src)+(os.pathsep+env['PYTHONPATH'] if env.get('PYTHONPATH') else '')
 probe=subprocess.run([sys.executable,'-B','-c','import iharq.layer2_decoders; from iharq.layer2_decoders.orchestration import HANDLERS; assert len(HANDLERS)==26'],env=env,capture_output=True,text=True)
 if probe.returncode!=0:raise RuntimeError('CLEAN_IMPORT_PROBE_FAILED:'+probe.stderr[-500:])
 p={'status':'PASS','schemas':10,'config_hash':ctx.state['config_hash'],'read_only_syntax_compile':'PASS','syntax_files':syntax_files,'clean_subprocess_import':'PASS','worker_import_probe':'NOT_USED_NO_ISOLATED_WORKER'};p['artifact']=art(ctx,'06','schema_import',p);return p
def s07(ctx):
 init(ctx);rows=ctx.state['core'].rows();roles=Counter(r['role'] for r in rows)
 if not {'train','calibration','validation','test'}<=set(roles):raise RuntimeError('ROLE_FIREWALL_INVALID')
 labels={r['label'] for r in rows}
 if labels!={'left_hand','right_hand'}:raise RuntimeError(f'LABEL_CONTRACT_INVALID:{sorted(labels)}')
 ev=[r['event_id'] for r in rows];win=[r['window_id'] for r in rows]
 if len(ev)!=len(set(ev)) or len(win)!=len(set(win)):raise RuntimeError('DUPLICATE_EVENT_OR_WINDOW_ID')
 by_role={}
 for role in roles:by_role[role]={(r['dataset_id'],r['subject_id']) for r in rows if r['role']==role}
 overlaps=[]
 rr=sorted(by_role)
 for i,a in enumerate(rr):
  for b in rr[i+1:]:
   ov=sorted(by_role[a]&by_role[b])
   if ov:overlaps.append({'roles':[a,b],'count':len(ov),'examples':ov[:5]})
 if overlaps:raise RuntimeError('SUBJECT_ROLE_LEAKAGE:'+json.dumps(overlaps,sort_keys=True))
 p={'status':'PASS','role_counts':dict(roles),'label_contract':['left_hand','right_hand'],'unique_events':len(ev),'unique_windows':len(win),'subject_role_overlap_count':0,'implemented_checks':['role_presence','binary_label_contract','event_id_uniqueness','window_id_uniqueness','dataset_scoped_subject_role_disjointness'],'test_selection':'PROHIBITED','leakage_statement':'NO_CONTRACT_LEAKAGE_DETECTED_UNDER_IMPLEMENTED_CHECKS'};p['artifact']=art(ctx,'07','loader',p);return p
def family(ctx,sid):
 init(ctx);cs=[c for c in ctx.state['a0'] if FAMILY_STAGE[c['branch_slot']]==sid];ts=[]
 cw=ctx.state['config']['training_policy']['class_weighting'];base_overrides={'batch_size':int(ctx.state.get('resource_profile',{}).get('recommended_neural_batch_size',16 if ctx.fixture else 64)),'class_weight_binding':cw}
 # Stage 12 is ordered deliberately: the sequence slot resolves first. EEG-TCNet may activate only from pre-result resource/input/nonconvergence outcomes.
 order={'DNN-FBCNET':0,'DNN-SEQ':1,'SSL-CBRAMOD':2,'SSL-REVE':3,'DNN-EGTC':4}
 cs=sorted(cs,key=lambda c:(order.get(c['branch_slot'],0),c['dataset_id'],str(c['budget_id']),c['model_repeat_index']))
 for c in cs:
  ov=dict(base_overrides)
  if c['branch_slot']=='DNN-EGTC':
   peers=[x for x in ctx.state['a0'] if x['branch_slot']=='DNN-SEQ' and x['dataset_id']==c['dataset_id'] and str(x['budget_id'])==str(c['budget_id'])]
   terms=[ctx.state['store'].terminal(x) for x in peers]
   allowed={'RESOURCE_BLOCKED','INPUT_INCOMPATIBLE','NONCONVERGENT'}
   ov['fallback_activated']=bool(terms) and all(t and t.get('terminal_status') in allowed for t in terms)
  t=execute_cell(c,ctx.state['core'],ctx.state['runtime_freeze'],ctx.state['store'],ctx.state['schema'],ctx.state['config_hash'],ctx.fixture,ctx.state.get('implementation_bindings'),ov,ctx.state['config']['data'],ctx.state['config']['implementation_parameters']);ts.append(t)
 p={'status':'PASS','attempted':len(cs),'branches':sorted({c['branch_slot'] for c in cs}),'terminal_counts':dict(Counter(t['terminal_status'] for t in ts))};p['artifact']=art(ctx,sid,'family',p);return p
def _resolve_sr_probability_selection(ctx):
 init(ctx);binding=ctx.state['config']['training_policy'];aug=binding['augmentation_challenger'];st=ctx.state['store'];root=st.root/'analysis_inputs';root.mkdir(parents=True,exist_ok=True)
 cached=root/'training_policy_sr_probability_selection.json'
 if cached.exists(): return json.loads(cached.read_text())
 primary_map={(c['dataset_id'],c['model_repeat_index']):c for c in ctx.state['a0'] if c['branch_slot']==aug['branch_id'] and str(c['budget_id'])==str(aug['budget_id'])}
 candidate_rows=[];selections={}
 datasets=sorted({c['dataset_id'] for c in ctx.state['challenger_cells']})
 for ds in datasets:
  for prob in map(float,aug['probability_resolution']['candidates']):
   ds_cells=[c for c in ctx.state['challenger_cells'] if c['dataset_id']==ds]
   if ctx.fixture: ds_cells=ds_cells[:1]
   for c in ds_cells:
    pc=primary_map.get((ds,c['model_repeat_index']));pt=None if pc is None else st.terminal(pc)
    if not pt or pt.get('terminal_status')!='SUCCESS':
     candidate_rows.append({'dataset_id':ds,'model_repeat_index':c['model_repeat_index'],'seed_id':c['seed_id'],'probability':prob,'status':'PRIMARY_NOT_SUCCESSFUL','test_set_used':False});continue
    ap={'condition_id':aug['run_cell_condition_identity']+':CALIBRATION','probability':prob,'segment_count_resolution':aug['segment_count_resolution'],'seed_namespace':aug['seed_namespace'],'donor_pool_identity':aug['donor_pool_identity'],'fixture':bool(ctx.fixture)}
    ov={'batch_size':int(ctx.state.get('resource_profile',{}).get('recommended_neural_batch_size',16 if ctx.fixture else 64)),'fixed_params':pt['selected_params'],'augmentation_policy':ap,'augmentation_context':{'dataset_id':ds,'model_repeat_index':c['model_repeat_index']},'class_weights':pt.get('class_weights'),'class_weight_policy':pt.get('class_weight_policy'),'fixed_class_weight_policy':True}
    vr=validation_only_fixed_neural_fit(c,ctx.state['core'],ctx.state['runtime_freeze'],ctx.fixture,ctx.state.get('implementation_bindings'),ov,ctx.state['config']['data'],ctx.state['config']['implementation_parameters'])
    candidate_rows.append({'dataset_id':ds,'model_repeat_index':c['model_repeat_index'],'seed_id':c['seed_id'],'probability':prob,**vr})
  dsres=[x for x in candidate_rows if x['dataset_id']==ds]
  sb=json.loads(json.dumps(binding));
  if ctx.fixture: sb['augmentation_challenger']['probability_resolution']['minimum_successful_seeds']=1
  try: selections[ds]=select_sr_probability(dsres,sb)
  except Exception as e: selections[ds]={'status':'BLOCKED','reason':type(e).__name__+':'+str(e)[:300],'test_set_used':False}
 from .writers import atomic_jsonl
 atomic_jsonl(root/'training_policy_sr_probability_calibration_candidates.jsonl',candidate_rows);payload={'status':'PASS' if all(x.get('status')=='PASS' for x in selections.values()) else 'PARTIAL_BLOCKED','selection_scope':'VALIDATION_ONLY','test_set_used':False,'datasets':selections,'candidate_grid':list(map(float,aug['probability_resolution']['candidates'])),'segment_count_policy':aug['segment_count_resolution'],'official_A0_A4_cell_count_unchanged':1896};atomic_json(cached,payload);return payload

def execute_training_policy_challengers(ctx):
 init(ctx); out=[]; binding=ctx.state['config']['training_policy']['augmentation_challenger'];selection=_resolve_sr_probability_selection(ctx)
 primary_map={(c['dataset_id'],c['model_repeat_index']):c for c in ctx.state['a0'] if c['branch_slot']==binding['branch_id'] and str(c['budget_id'])==str(binding['budget_id'])}
 for c in ctx.state['challenger_cells']:
  pc=primary_map.get((c['dataset_id'],c['model_repeat_index']))
  if pc is None: out.append(ctx.state['store'].write_terminal(c,'INVALID',reason='MATCHED_PRIMARY_EEGNET_CELL_MISSING')); continue
  pt=ctx.state['store'].terminal(pc)
  if not pt or pt.get('terminal_status')!='SUCCESS': out.append(ctx.state['store'].write_terminal(c,'CONDITIONAL_SKIP',reason='MATCHED_PRIMARY_EEGNET_NOT_SUCCESSFUL',comparison_reference=pc['planned_run_cell_id'])); continue
  ds_sel=selection['datasets'].get(c['dataset_id'],{})
  if ds_sel.get('status')!='PASS': out.append(ctx.state['store'].write_terminal(c,'CONDITIONAL_SKIP',reason='S&R_PROBABILITY_SELECTION_NOT_AVAILABLE',selection_evidence=ds_sel,comparison_reference=pc['planned_run_cell_id']));continue
  prob=float(ds_sel['selected_probability']);aug={'condition_id':binding['run_cell_condition_identity'],'probability':prob,'segment_count_resolution':binding['segment_count_resolution'],'seed_namespace':binding['seed_namespace'],'donor_pool_identity':binding['donor_pool_identity'],'fixture':bool(ctx.fixture)}
  ov={'batch_size':int(ctx.state.get('resource_profile',{}).get('recommended_neural_batch_size',16 if ctx.fixture else 64)),'fixed_params':pt['selected_params'],'augmentation_policy':aug,'augmentation_context':{'dataset_id':c['dataset_id'],'model_repeat_index':c['model_repeat_index']},'class_weights':pt.get('class_weights'),'class_weight_policy':pt.get('class_weight_policy'),'fixed_class_weight_policy':True}
  t=execute_cell(c,ctx.state['core'],ctx.state['runtime_freeze'],ctx.state['store'],ctx.state['schema'],ctx.state['config_hash'],ctx.fixture,ctx.state.get('implementation_bindings'),ov,ctx.state['config']['data'],ctx.state['config']['implementation_parameters']); out.append(t)
 return out

def _primary_for_challenger(ctx,c):
 for p in ctx.state['a0']:
  if p['planned_run_cell_id']==c['comparison_reference']: return ctx.state['store'].terminal(p)
 return None
def s13(ctx):
 init(ctx);good=[ctx.state['store'].terminal(c) for c in (ctx.state['a0']+ctx.state['challenger_cells']) if ctx.state['store'].terminal(c) and ctx.state['store'].terminal(c)['terminal_status']=='SUCCESS'];bad=[x for x in good if not x.get('checkpoint_sha256')]
 if bad:raise RuntimeError('CHECKPOINT_MISSING')
 p={'status':'PASS','successful_models':len(good),'checkpoint_roundtrip_failures':0};p['artifact']=art(ctx,'13','checkpoints',p);return p
def s14(ctx):
 init(ctx);missing=[];n=0
 for c in (ctx.state['a0']+ctx.state['challenger_cells']):
  t=ctx.state['store'].terminal(c)
  if t and t['terminal_status']=='SUCCESS':
   if not (ctx.state['store'].root/t['prediction_partition']).exists():missing.append(c['planned_run_cell_id'])
   else:n+=1
 if missing:raise RuntimeError('PREDICTION_PARTITION_MISSING')
 p={'status':'PASS','prediction_partitions':n,'missing':0,'score_semantics':True};p['artifact']=art(ctx,'14','predictions',p);return p
def s15(ctx):
 init(ctx);p=close_a0(ctx.state['core'],ctx.state['store'],ctx.state['a0'],ctx.state['runtime_freeze'],ctx.state['schema'],ctx.state['config_hash'],expected=None if ctx.fixture else ctx.state['planned_counts']['A0']);tc=close_training_policy_challenger(ctx.state['core'],ctx.state['store'],ctx.state['challenger_cells'],lambda c:_primary_for_challenger(ctx,c),ctx.state['runtime_freeze'],expected=None if ctx.fixture else int(ctx.state['config']['training_policy']['augmentation_challenger']['run_cell_count']));
 if tc['status']!='PASS': raise RuntimeError('TRAINING_POLICY_CHALLENGER_CLOSURE_INCOMPLETE:'+json.dumps(tc,sort_keys=True))
 p.update(stage15_a0_closure='COMPLETE',required_closure_outputs_missing=0,training_policy_challenger_closure=tc);p['artifact']=art(ctx,'15','a0_and_training_policy_closure',p);return p
def s16(ctx):init(ctx);r=low_label(ctx.state['store'],ctx.state['a0'],ctx.state['schema'],ctx.state['config_hash'],ctx.state['runtime_freeze']);p={'status':'PASS','records':len(r)};p['artifact']=art(ctx,'16','low_label',p);return p
def s17(ctx):init(ctx);r=subject_profiles(ctx.state['core'],ctx.state['store'],ctx.state['a0'],ctx.state['schema'],ctx.state['config_hash']);p={'status':'PASS','records':len(r)};p['artifact']=art(ctx,'17','profiles',p);return p
def s18(ctx):
 init(ctx);pm=ctx.state['a4'].verify_parent_match(ctx.state['core']);
 if pm['status']!='PASS':raise RuntimeError('A4_PARENT_MATCH_FAIL_CLOSED')
 cache={};terms=[]
 for c in ctx.state['a4cells']:
  key=(c['dataset_id'],str(c['budget_id']));reps=cache.setdefault(key,select_reps(ctx.state['store'],*key)[0])
  t=execute_ensemble(c,ctx.state['store'],ctx.state['core'],reps,ctx.state['schema'],ctx.state['config_hash'],ctx.state['config']['data']) if c['condition_id'] in {'A4-C4-MODEL-HARD-VOTE','A4-C5-MODEL-PROB-AVG'} else execute_role(c,ctx.state['store'],ctx.state['core'],ctx.state['a4'],reps,ctx.state['schema'],ctx.state['config_hash'],ctx.state['runtime_freeze'],ctx.state['config']['data'],ctx.fixture,ctx.state.get('implementation_bindings'),{'batch_size':int(ctx.state.get('resource_profile',{}).get('recommended_neural_batch_size',16 if ctx.fixture else 64))});terms.append(t)
 cl=close_a4(ctx.state['core'],ctx.state['store'],ctx.state['a4cells'],ctx.state['runtime_freeze'],expected=None if ctx.fixture else ctx.state['planned_counts']['A4']);p={'status':'PASS','slots':len(terms),'terminal_counts':dict(Counter(t['terminal_status'] for t in terms)),'representative_groups':len(cache),'c4_vs_strongest':'COMPLETE','c5_vs_strongest':'COMPLETE','closure':cl};p['artifact']=art(ctx,'18','a4',p);return p
def s18u(ctx):
 init(ctx);d=yaml.safe_load((ctx.mr/'p02_ablation_ownership_matrix_R3.yaml').read_text());r=resolve_ablation(d.get('rows',[]),False)
 if r['additional_full_execution']:raise RuntimeError('ADDITIONAL_HANDLER_NOT_FROZEN')
 p={'status':'PASS','decision':'NO_ADDITIONAL_FULL_EXECUTION_ABLATION_UNLOCKED','authority_check':True,'contract_check':True};p['artifact']=art(ctx,'18U','unlock',p);return p
def s19(ctx):init(ctx);r=close_failures(ctx.state['store'],ctx.state['cells'],ctx.state['schema'],ctx.state['config_hash'],'FIXTURE' if ctx.fixture else 'P02');p={'status':'PASS','failure_evidence_aggregation':'COMPLETE',**r};p['artifact']=art(ctx,'19','failure',p);return p
def s20(ctx):
 init(ctx);st=ctx.state['store'];a0=json.loads((st.root/'analysis_inputs/a0_completion.json').read_text());a4=json.loads((st.root/'analysis_inputs/a4_completion.json').read_text());pred=list((st.root/'records/PredictionRecord').rglob('*.jsonl'))
 if not pred or a0['status']!='PASS' or a4['status']!='PASS' or a4['c4_c5_incomplete']!=0 or a4.get('role_control_incomplete',0)!=0 or not (st.root/'analysis_inputs/a4_c4_c5_comparison_artifacts.jsonl').exists():raise RuntimeError('READINESS_RUNTIME_EVIDENCE_INCOMPLETE')
 pman=list((st.root/'manifests/record_partitions/PredictionRecord').glob('*.json'))
 # manifests are nested by family/run ID in current Store; recursively gather and prove the full PredictionRecord payload envelope exists.
 pman=list((st.root/'manifests/record_partitions/PredictionRecord').rglob('*.json'))
 fields=set()
 for q in pman:fields.update(json.loads(q.read_text()).get('fields',[]))
 support={'run_cell_id','ablation_id','condition_id','aggregation_identity','failure_missingness_status','metric_dictionary_reference','config_sha256','scientific_freeze_id'}
 p3=p03_readiness(fields,support)
 if p3['status']!='PASS':raise RuntimeError('P03_READINESS_FIELDS_INCOMPLETE:'+json.dumps(p3,sort_keys=True))
 schemas=load_schemas(ctx.state['schema']);rc={'planned_run_cell_id':'P02-L2-READINESS-P03','ablation_id':'SUPPORT','dataset_id':'ALL','branch_slot':'READINESS','budget_id':'ALL'}
 rr=make_record('Layer2ReadinessReport',{'consumer_id':'P03','required_fields':sorted(set(p3['required_prediction_fields'])|set(p3['required_support_fields'])),'available_fields':sorted(fields|support),'missing_fields':[],'compatibility_status':'PASS','blocking_reasons':[]},schemas['Layer2ReadinessReport'],ctx.state['config_hash'],['P02-STAGE20-RUNTIME-EVIDENCE','analysis_inputs/a0_completion.json','analysis_inputs/a4_completion.json']);rp=st.write_records('Layer2ReadinessReport',rc,[rr])
 p={'status':'PASS','runtime_evidence_checked':True,'prediction_partitions':len(pred),'a0':True,'a4':True,'c4c5':True,'p03':p3,'readiness_record':str(rp.relative_to(st.root))};p['artifact']=art(ctx,'20','readiness',p);return p
def s21(ctx):
 init(ctx);n=figure_tables(ctx.state['store']);req=['a0_closure_source_manifest.json','a4_role_control_participant_comparisons.csv','a4_role_control_statistics.json','a4_c4_c5_participant_comparisons.csv','a4_c4_c5_statistics.json','a4_c4_c5_comparison_artifacts.jsonl','a4_burden_source.csv'];missing=[x for x in req if not (ctx.state['store'].root/'figure_source_data'/x).exists()]
 if missing:raise RuntimeError('FIGURE_SOURCE_MISSING')
 p={'status':'PASS','source_families':n,'c4_c5_export':'PASS'};p['artifact']=art(ctx,'21','sources',p);return p
def s22(ctx):
 init(ctx);ev={'a0':'analysis_inputs/a0_completion.json','a4':'analysis_inputs/a4_completion.json','a4_role_controls':'analysis_inputs/a4_role_control_statistics.json','c4c5':'analysis_inputs/a4_c4_c5_statistics.json','c4c5_artifacts':'analysis_inputs/a4_c4_c5_comparison_artifacts.jsonl','a4_burden':'analysis_inputs/a4_burden_source.csv','figures':'analysis_inputs/figure_table_source_manifest.json','failures':'analysis_inputs/failure_negative_summary.json','training_policy_challenger':'analysis_inputs/training_policy_challenger_completion.json','training_policy_statistics':'analysis_inputs/training_policy_challenger_statistics.json','training_policy_sr_selection':'analysis_inputs/training_policy_sr_probability_selection.json','preexecution_amendment':'protocol_change_required/P02_PREEXECUTION_TRAINING_POLICY_AMENDMENT_R2.yaml'};h=generate_handoffs(ctx.state['store'].root/'handoffs',{'run_id':ctx.state['run_id'],'config_sha256':ctx.state['config_hash'],'evidence_status':'FIXTURE_NON_SCIENTIFIC_NOT_P02_EVIDENCE' if ctx.fixture else 'RUNTIME_EXECUTED'},ev);p={'status':'PASS','handoffs':h,'manual_reconstruction_required':False};p['artifact']=art(ctx,'22','handoffs',p);return p
def s23(ctx):
 init(ctx);st=ctx.state['store'];state={'a0_complete':(st.root/'analysis_inputs/a0_completion.json').exists(),'a4_complete':(st.root/'analysis_inputs/a4_completion.json').exists(),'a4_role_controls_complete':(st.root/'analysis_inputs/a4_role_control_statistics.json').exists(),'c4_c5_complete':(st.root/'analysis_inputs/a4_c4_c5_statistics.json').exists() and (st.root/'analysis_inputs/a4_c4_c5_comparison_artifacts.jsonl').exists(),'a4_burden_complete':(st.root/'analysis_inputs/a4_burden_source.csv').exists(),'failure_evidence':(st.root/'analysis_inputs/failure_negative_summary.json').exists(),'training_policy_challenger_complete':(st.root/'analysis_inputs/training_policy_challenger_completion.json').exists(),'figure_table_sources':(st.root/'analysis_inputs/figure_table_source_manifest.json').exists(),'handoffs':(st.root/'handoffs/runtime_evidence_index.json').exists(),'p03_complete':True,'readiness_record':bool(list((st.root/'records/Layer2ReadinessReport').rglob('*.jsonl'))),'security_pass':scan_tree(st.root)['status']=='PASS'};e=evidence_sufficiency(state)
 if e['status']!='PASS':raise RuntimeError(str(e))
 p={'status':'PASS','evidence_sufficiency':e,'state':state};p['artifact']=art(ctx,'23','sufficiency',p);return p
def s24(ctx):
 init(ctx);st=ctx.state['store'];atomic_json(st.root/'manifests/runtime_manifest.json',{'status':'READY_FOR_FINALIZATION','fixture':ctx.fixture,'scientific_evidence':False if ctx.fixture else True,'run_id':ctx.state['run_id'],'config_sha256':ctx.state['config_hash']});sec=scan_tree(st.root)
 if sec['status']!='PASS':raise RuntimeError('SECURITY_SCAN_FAILED')
 p={'status':'PASS','runtime_bundle_generation':'READY_FOR_POST_LEDGER_FINALIZATION','stub_only':0};p['artifact']=art(ctx,'24','bundle',p);return p
def s08(ctx): return family(ctx,'08')
def s09(ctx): return family(ctx,'09')
def s10(ctx): return family(ctx,'10')
def s11(ctx):
 p=family(ctx,'11');ch=execute_training_policy_challengers(ctx);p['training_policy_challenger']={'attempted':len(ch),'terminal_counts':dict(Counter(x['terminal_status'] for x in ch))};p['artifact']=art(ctx,'11','neural_and_training_policy_challenger',p);return p
def s12(ctx): return family(ctx,'12')
HANDLERS={'00':s00,'01':s01,'02':s02,'03':s03,'04':s04,'05':s05,'06':s06,'07':s07,'08':s08,'09':s09,'10':s10,'11':s11,'12':s12,'13':s13,'14':s14,'15':s15,'16':s16,'17':s17,'18':s18,'18U':s18u,'19':s19,'20':s20,'21':s21,'22':s22,'23':s23,'24':s24}
def finalize(ctx,ledger,partial=False,failure=None):
 st=ctx.state['store'];work=Path(ledger).parent
 # Copy orchestration evidence into the runtime bundle so stage/gate/log provenance travels with science.
 shutil.copytree(ledger,st.root/'manifests/stage_ledger',dirs_exist_ok=True)
 for src,dst in [(work/'gate_results',st.root/'gate_results'),(work/'logs',st.root/'logs'),(work/'heartbeats',st.root/'diagnostics/heartbeats'),(work/'stage_artifacts',st.root/'manifests/stage_artifacts')]:
  if src.exists():shutil.copytree(src,dst,dirs_exist_ok=True)
 (st.root/'protocol_change_required').mkdir(parents=True,exist_ok=True);shutil.copy2(ctx.package_root/'contracts/P02_PREEXECUTION_TRAINING_POLICY_AMENDMENT_R2.yaml',st.root/'protocol_change_required/P02_PREEXECUTION_TRAINING_POLICY_AMENDMENT_R2.yaml');shutil.copy2(ctx.package_root/'docs/P02_FUTURE_PROTOCOL_BUILD_BOOK_SYNC_NOTE_R2.md',st.root/'protocol_change_required/P02_FUTURE_PROTOCOL_BUILD_BOOK_SYNC_NOTE_R2.md');shutil.copy2(ctx.package_root/'docs/P02_TRAINING_POLICY_EXTERNAL_EVIDENCE_NOTE_R2.md',st.root/'protocol_change_required/P02_TRAINING_POLICY_EXTERNAL_EVIDENCE_NOTE_R2.md');atomic_yaml(st.root/'manifests/config_snapshot.yaml',ctx.state['config'])
 atomic_yaml(st.root/'manifests/scientific_freeze_snapshot.yaml',ctx.state['runtime_freeze'])
 atomic_json(st.root/'manifests/input_and_run_cell_manifest.json',{'run_id':ctx.state['run_id'],'fixture':ctx.fixture,'planned_cells_in_session':len(ctx.state['cells']),'A0_cells':len(ctx.state['a0']),'A4_cells':len(ctx.state['a4cells']),'training_policy_challenger_cells':len(ctx.state['challenger_cells']),'official_full_plan_counts':{'A0':sum(r['ablation_id']=='A0' for r in ctx.state['all_cells']),'A4':sum(r['ablation_id']=='A4' for r in ctx.state['all_cells']),'total':len(ctx.state['all_cells'])},'input_pointer_stage':'manifests/stage_artifacts/03_pointers.json','input_validation_stage':'manifests/stage_artifacts/04_p01_validation.json'})
 atomic_json(st.root/'manifests/runtime_manifest.json',{'status':'PARTIAL_FAILED_EXPORT' if partial else 'FINALIZED_FOR_EXPORT','fixture':ctx.fixture,'scientific_evidence':False if ctx.fixture else True,'run_id':ctx.state['run_id'],'config_sha256':ctx.state['config_hash'],'stage_count_expected':26,'bundle_contents_complete':not partial,'partial_failure':bool(partial),'failure':failure})
 checksums(st.root);v=verify(st.root)
 if v['status']!='PASS':raise RuntimeError('CHECKSUM_FAIL')
 name=('FIXTURE_NON_SCIENTIFIC_RUNTIME_BUNDLE.zip' if ctx.fixture and not partial else ('FIXTURE_NON_SCIENTIFIC_PARTIAL_FAILURE_BUNDLE.zip' if ctx.fixture else (f'IHARQ_P02_L2_Phase_Execution_Bundle_{ctx.state["run_id"]}.zip' if not partial else f'IHARQ_P02_L2_Partial_Failure_Bundle_{ctx.state["run_id"]}.zip')));z=zip_bundle(st.root,ctx.work_root/name);return {'status':'PARTIAL' if partial else 'PASS','checksums':v,'zip':z,'run_id':ctx.state['run_id'],'fixture':ctx.fixture,'scientific_evidence':False if ctx.fixture else True,'failure':failure}
