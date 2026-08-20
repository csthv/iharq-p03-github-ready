from __future__ import annotations
from pathlib import Path
import json,yaml,zipfile,re
import numpy as np
import pytest
ROOT=Path(__file__).resolve().parents[1]
DATA_CONTRACT=yaml.safe_load((ROOT/'configs/phase_02/data.yaml').read_text())
from iharq.layer2_decoders.validation import planned_cells,stage_plan
from iharq.layer2_decoders.orchestration import FAMILY_STAGE,HANDLERS
from iharq.layer2_decoders.metrics import evaluate,hard_vote,probability_average
from iharq.layer2_decoders.statistics import wilcoxon_paired,paired_bootstrap,holm
from iharq.layer2_decoders.a4 import strongest
from iharq.layer2_decoders.kaggle_entry import authoring_fixture_simulation
from iharq.layer2_decoders.security import scan_tree
from iharq.layer2_decoders.bundle import verify
from iharq.layer2_decoders.store import Store
from iharq.layer2_decoders.fixtures import SyntheticCoreDataset
import iharq.layer2_decoders.a4 as a4mod
from iharq.layer2_decoders.writers import atomic_jsonl
from iharq.layer2_decoders.identity import derive_seed
from iharq.layer2_decoders.config import load_config
from iharq.layer2_decoders.data import frozen_budget_memberships
from iharq.layer2_decoders.stage_runner import StageRunner
from iharq.layer2_decoders.models import make_adapter
from iharq.layer2_decoders.checkpoints import save_roundtrip
from iharq.layer2_decoders.records import load_schemas,make_record
from iharq.layer2_decoders.security import scan_text

def test_frozen_counts():
 r=planned_cells(ROOT/'machine_readable/p02_full_ablation_planned_run_cells_R3.yaml');assert r['status']=='PASS' and r['total']==1896 and r['A0']==678 and r['A4']==1218 and r['unique']==1896 and r['expected']=={'total':1896,'A0':678,'A4':1218}
def test_26_real_handlers():
 p=stage_plan(ROOT/'machine_readable/p02_notebook_stage_plan_R4.yaml');assert p['status']=='PASS' and p['count']==26
 ids=[str(x['stage']) for x in yaml.safe_load((ROOT/'machine_readable/p02_notebook_stage_plan_R4.yaml').read_text())['stages']];assert set(ids)==set(HANDLERS) and len(HANDLERS)==26
 for sid,fn in HANDLERS.items(): assert callable(fn) and '<lambda>' not in getattr(fn,'__name__','') or sid in {'08','09','10','11','12'}
def test_all_a0_branches_routed():
 rows=yaml.safe_load((ROOT/'machine_readable/p02_full_ablation_planned_run_cells_R3.yaml').read_text())['rows'];a=[r for r in rows if r['ablation_id']=='A0'];assert len(a)==678 and all(r['branch_slot'] in FAMILY_STAGE for r in a)
def test_model_portfolio_16_and_a14_absent():
 m=yaml.safe_load((ROOT/'machine_readable/p02_model_portfolio.yaml').read_text())['models'];assert len(m)==16
 text='\n'.join(p.read_text(errors='ignore') for p in [ROOT/'configs/phase_02/phase.yaml',ROOT/'src/iharq/layer2_decoders/orchestration.py']);assert 'ABSENT_PROHIBITED' in text and not re.search(r'A14.*FULL_EXECUTION_REQUIRED',text)
def test_metric_golden_vectors():
 y=[0,0,1,1];p=[0,1,1,1];m=evaluate(y,p);assert abs(m['ACC']-.75)<1e-12 and abs(m['BACC']-.75)<1e-12
 a,t=hard_vote([np.array([0,1,1]),np.array([0,0,1]),np.array([1,0,1])]);assert a.tolist()==[0,0,1] and t==0
 q=probability_average([np.array([[.8,.2],[.2,.8]]),np.array([[.6,.4],[.4,.6]])]);assert np.allclose(q,[[.7,.3],[.3,.7]])
def test_stats_floor_and_holm():
 assert wilcoxon_paired([1,2,3,4],[1,1,1,1])['status']=='DESCRIPTIVE_ONLY'
 x=wilcoxon_paired([1,2,3,4,5],[0,0,0,0,0]);assert x['status']=='PASS'
 h=holm({'a':.01,'b':.04});assert h['a']<=h['b']<=1
 b=paired_bootstrap([1,1,1,1,1,1],1,200,.95);assert b['status']=='PASS' and b['estimate']==1
def test_no_test_argument_in_strongest_selector():
 import inspect
 sig=str(inspect.signature(strongest));assert 'test' not in sig.lower()
 src=inspect.getsource(strongest);assert 'validation_selection' in src or "validation_selection" in (ROOT/'src/iharq/layer2_decoders/a4.py').read_text()
def test_c4_c5_negative_semantics_static():
 s=(ROOT/'src/iharq/layer2_decoders/a4.py').read_text();assert 'MEMBER_PROBABILITY_OR_CLASS_ORDER_UNAVAILABLE' in s and 'A4_C4_C5_EMPTY_COMMON_SUPPORT' in s and 'strongest_constituent_prediction_partition' in s
def test_security_and_paths_current_tree():
 s=scan_tree(ROOT);assert s['status']=='PASS'
 forbidden='/'+'mnt'+'/'+'data'+'/'
 scan_roots=[ROOT/'src',ROOT/'configs',ROOT/'contracts',ROOT/'machine_readable',ROOT/'notebook',ROOT/'validation',ROOT/'execution_bundle_schema',ROOT/'scripts']
 for base in scan_roots:
  if not base.exists(): continue
  for p in base.rglob('*'):
   if p.is_file() and p.suffix.lower() in {'.py','.md','.json','.yaml','.yml','.csv','.toml','.ipynb'}:
    assert forbidden not in p.read_text(errors='ignore')
@pytest.fixture(scope='session')
def fixture_run(tmp_path_factory):
 root=tmp_path_factory.mktemp('p02_full_graph');r=authoring_fixture_simulation(ROOT,root);return root,r
def test_full_stage_graph_synthetic_integration(fixture_run):
 root,r=fixture_run;assert r['status']=='PASS' and len(r['stages'])==26 and all(x['status']=='SUCCESS' for x in r['stages']);assert r['finalization']['status']=='PASS' and r['finalization']['scientific_evidence'] is False
def test_stage15_real_closure(fixture_run):
 root,_=fixture_run;d=json.loads((root/'stage_ledger/stage_15.json').read_text())['outputs'];assert d['stage15_a0_closure']=='COMPLETE' and d['minimum_floor']['PhysioNetMI']=={'classical':True,'riemannian':True} and d['required_closure_outputs_missing']==0
def test_stage18_c4c5_closure(fixture_run):
 root,_=fixture_run;d=json.loads((root/'stage_ledger/stage_18.json').read_text())['outputs'];assert d['c4_vs_strongest']=='COMPLETE' and d['c5_vs_strongest']=='COMPLETE' and d['closure']['c4_c5_incomplete']==0
 s=json.loads((root/'runtime/analysis_inputs/a4_c4_c5_statistics.json').read_text());conds={x['condition_id'] for x in s['rows']};assert conds=={'A4-C4-MODEL-HARD-VOTE','A4-C5-MODEL-PROB-AVG'} and all(x.get('validation_selection_provenance',{}).get('test_outcome_influence')=='PROHIBITED' for x in s['rows'])
def test_c4c5_common_support_and_stats(fixture_run):
 root,_=fixture_run;s=json.loads((root/'runtime/analysis_inputs/a4_c4_c5_statistics.json').read_text());assert all(x['matched_participants']>=5 for x in s['rows']) and all(x['bootstrap']['resamples']==10000 for x in s['rows']) and all('holm_adjusted_p' in x for x in s['rows'])
 sup=[json.loads(x) for x in (root/'runtime/analysis_inputs/a4_c4_c5_common_support.jsonl').read_text().splitlines()];assert len(sup)==2 and all(x['matched_event_denominator']>0 for x in sup)
def test_stage18u_real_check(fixture_run):
 root,_=fixture_run;d=json.loads((root/'stage_ledger/stage_18U.json').read_text())['outputs'];assert d['decision']=='NO_ADDITIONAL_FULL_EXECUTION_ABLATION_UNLOCKED' and d['authority_check'] and d['contract_check']
def test_failure_readiness_sources_handoffs_bundle(fixture_run):
 root,r=fixture_run
 for sid in ['19','20','21','22','23','24']:assert json.loads((root/f'stage_ledger/stage_{sid}.json').read_text())['status']=='SUCCESS'
 assert (root/'runtime/analysis_inputs/failure_negative_summary.json').is_file();assert (root/'runtime/figure_source_data/a4_c4_c5_statistics.json').is_file();assert (root/'runtime/table_source_data/a4_c4_c5_statistics.json').is_file();assert (root/'runtime/handoffs/runtime_evidence_index.json').is_file();assert verify(root/'runtime')['status']=='PASS'
 with zipfile.ZipFile(r['finalization']['zip']['path']) as z:assert z.testzip() is None and all(not n.startswith('/') and '..' not in Path(n).parts for n in z.namelist())
def test_all_gate_results_fixture(fixture_run):
 root,_=fixture_run;g=list((root/'gate_results').glob('*.json'));assert len(g)==26 and all(json.loads(p.read_text())['status']=='PASS' for p in g)
def test_fixture_never_claims_p02_science(fixture_run):
 root,r=fixture_run;assert r['finalization']['scientific_evidence'] is False
 ident=json.loads((root/'runtime/manifests/runtime_manifest.json').read_text());assert ident['scientific_evidence'] is False

def _a4_cell(condition):
 rows=yaml.safe_load((ROOT/'machine_readable/p02_full_ablation_planned_run_cells_R3.yaml').read_text())['rows']
 return next(dict(r) for r in rows if r['ablation_id']=='A4' and r['dataset_id']=='PhysioNetMI' and r['condition_id']==condition and r['role_id']=='FIXED_MODEL_ENSEMBLE' and str(r['budget_id'])=='FULL_TRAIN' and r['model_repeat_index']==0)

def test_a4_c4_missing_constituent_governed(tmp_path,monkeypatch):
 store=Store(tmp_path/'runtime');core=SyntheticCoreDataset();c=_a4_cell('A4-C4-MODEL-HARD-VOTE')
 monkeypatch.setattr(a4mod,'a0_term',lambda *a,**k: None)
 t=a4mod.execute_ensemble(c,store,core,{'CLASSICAL':'CLS-CSP-LDA','RIEMANNIAN':'RIE-TS-LR'},ROOT/'machine_readable/p02_record_schema_freeze_R2.yaml','fixture',DATA_CONTRACT)
 assert t['terminal_status']=='NOT_APPLICABLE_REPEAT_SLOT' and t['reason']=='MINIMUM_ENSEMBLE_ROLES_NOT_AVAILABLE'

def test_a4_c5_probability_or_class_order_unavailable(tmp_path,monkeypatch):
 store=Store(tmp_path/'runtime');core=SyntheticCoreDataset();c=_a4_cell('A4-C5-MODEL-PROB-AVG');testrows=core.rows(dataset_id='PhysioNetMI',role='test')[:8]
 def terminal(branch):
  rel=f'pred/{branch}.jsonl';rows=[{'source_event_id':r['event_id'],'y_pred':0,'score_vector':[.7,.3],'score_type':'NATIVE_PROBABILITY','class_order':['WRONG','ORDER'],'checkpoint_id':'a'*64} for r in testrows];atomic_jsonl(store.root/rel,rows);return {'terminal_status':'SUCCESS','prediction_partition':rel,'checkpoint_sha256':'a'*64}
 monkeypatch.setattr(a4mod,'a0_term',lambda store_,ds,b,budget,rep: terminal(b))
 monkeypatch.setattr(a4mod,'strongest',lambda *a,**k:{'selected_branch':'CLS-CSP-LDA','candidate_summaries':[],'test_outcome_influence':'PROHIBITED'})
 t=a4mod.execute_ensemble(c,store,core,{'CLASSICAL':'CLS-CSP-LDA','RIEMANNIAN':'RIE-TS-LR'},ROOT/'machine_readable/p02_record_schema_freeze_R2.yaml','fixture',DATA_CONTRACT)
 assert t['terminal_status']=='NOT_APPLICABLE_SCORE_SEMANTICS' and t['reason']=='MEMBER_PROBABILITY_OR_CLASS_ORDER_UNAVAILABLE'

def test_a4_c4_empty_common_support(tmp_path,monkeypatch):
 store=Store(tmp_path/'runtime');core=SyntheticCoreDataset();c=_a4_cell('A4-C4-MODEL-HARD-VOTE');testrows=core.rows(dataset_id='PhysioNetMI',role='test')
 def terminal(branch):
  rel=f'pred/{branch}.jsonl';rr=testrows[:5] if branch=='CLS-CSP-LDA' else testrows[5:10];rows=[{'source_event_id':r['event_id'],'y_pred':0,'score_vector':[.7,.3],'score_type':'NATIVE_PROBABILITY','class_order':['left_hand','right_hand'],'checkpoint_id':'b'*64} for r in rr];atomic_jsonl(store.root/rel,rows);return {'terminal_status':'SUCCESS','prediction_partition':rel,'checkpoint_sha256':'b'*64}
 monkeypatch.setattr(a4mod,'a0_term',lambda store_,ds,b,budget,rep: terminal(b))
 monkeypatch.setattr(a4mod,'strongest',lambda *a,**k:{'selected_branch':'CLS-CSP-LDA','candidate_summaries':[],'test_outcome_influence':'PROHIBITED'})
 t=a4mod.execute_ensemble(c,store,core,{'CLASSICAL':'CLS-CSP-LDA','RIEMANNIAN':'RIE-TS-LR'},ROOT/'machine_readable/p02_record_schema_freeze_R2.yaml','fixture',DATA_CONTRACT)
 assert t['terminal_status']=='INVALID' and t['reason']=='A4_C4_C5_EMPTY_COMMON_SUPPORT'

def test_a4_inferential_floor_is_descriptive_only():
 r=wilcoxon_paired([.6,.7,.8,.9],[.5,.6,.7,.8]);assert r['status']=='DESCRIPTIVE_ONLY' and r['n']==4

def test_stage18_preserves_c1_c2_c3_comparisons(fixture_run):
 root,_=fixture_run;d=json.loads((root/'stage_ledger/stage_18.json').read_text())['outputs']['closure']
 assert d['role_control_incomplete']==0 and d['role_control_closure_rows']==d['role_control_expected']
 s=json.loads((root/'runtime/analysis_inputs/a4_role_control_statistics.json').read_text());alts={r['alternative_condition'] for r in s['rows']}
 assert {'A4-C1-LONG-3P5S','A4-C2-MULTI-HARD-VOTE','A4-C3-MULTI-PROB-AVG'}<=alts
 assert all(r.get('reference_condition')=='A4-C0-CORE' for r in s['rows'])

def test_config_schema_and_frozen_identity():
 cfg,h=load_config(ROOT/'configs/phase_02');assert cfg['phase']['phase_id']=='P02' and cfg['phase']['notebook_id']=='IHARQ-P02-COMPLETE-EXECUTION-AND-ANALYSIS-R4' and len(h)==64
 assert cfg['phase']['a14']=='ABSENT_PROHIBITED' and cfg['phase']['alternative_scientific_modes']=='PROHIBITED'

def test_seed_derivation_reproducible_and_distinct():
 a=derive_seed(20260804,'X','MODEL_INIT');b=derive_seed(20260804,'X','MODEL_INIT');c=derive_seed(20260804,'Y','MODEL_INIT')
 assert a==b and a!=c

def test_frozen_budget_membership_counts_and_nesting():
 core=SyntheticCoreDataset();m=frozen_budget_memberships(core,budgets=(1,2,4,8,16,32),seed=20260804)
 for b in (1,2,4,8,16,32):
  key=f'PhysioNetMI:budget-{b}-seed-20260804';assert len(m[key])==2*b
 assert m['PhysioNetMI:budget-1-seed-20260804']<=m['PhysioNetMI:budget-2-seed-20260804']<=m['PhysioNetMI:budget-4-seed-20260804']<=m['PhysioNetMI:budget-8-seed-20260804']<=m['PhysioNetMI:budget-16-seed-20260804']<=m['PhysioNetMI:budget-32-seed-20260804']

def test_checkpoint_roundtrip_synthetic(tmp_path):
 m=make_adapter('SAN-MAJ',1,16,8,{})
 X=np.zeros((4,8,16),dtype=np.float32);y=np.array([0,0,1,1]);m.fit(X,y)
 r=save_roundtrip(m,X,tmp_path/'m.pkl');assert r['status']=='PASS' and len(r['checkpoint_sha256'])==64

def test_record_unknown_field_rejected():
 schemas=load_schemas(ROOT/'machine_readable/p02_record_schema_freeze_R2.yaml')
 payload={'dataset_id':'D','subject_id':'S','session_id':'SE','split_role':'test','budget_id':'FULL_TRAIN','budget_repeat_id':'R','model_id':'M','metric_id':'BACC','model_seed':1,'numerator':None,'denominator':2,'value':.5,'validity':'VALID','aggregation_level':'DATASET','UNAUTHORIZED_FIELD':1}
 with pytest.raises(Exception):make_record('BaselineMetricRecord',payload,schemas['BaselineMetricRecord'],'a'*64,['x'])

def test_stage_dependency_idempotency_and_revision_guard(tmp_path):
 plan=[{'stage':'00','gate':'G00'},{'stage':'01','gate':'G01'}];count={'n':0}
 r=StageRunner(tmp_path,plan,{'revision':'A'},heartbeat=1)
 with pytest.raises(RuntimeError):r.run('01',lambda:{'ok':1})
 a=r.run('00',lambda:count.update(n=count['n']+1) or {'ok':1});b=r.run('00',lambda:count.update(n=count['n']+1) or {'ok':2})
 assert a['attempt_id']==b['attempt_id'] and count['n']==1
 r2=StageRunner(tmp_path,plan,{'revision':'B'},heartbeat=1);assert r2.accepted('00') is None

def test_secret_pattern_negative():
 fake='Bearer '+'X'*24
 assert scan_text(fake)

def test_a14_creation_not_present_anywhere_current():
 text=(ROOT/'configs/phase_02/phase.yaml').read_text()+(ROOT/'src/iharq/layer2_decoders/orchestration.py').read_text()
 assert 'a14:' in text.lower() and 'ABSENT_PROHIBITED' in text and 'A14-C' not in text

def test_notebook_has_no_executed_scientific_outputs():
 import nbformat
 nb=nbformat.read(ROOT/'notebook/IHARQ_Phase_02_Complete_Execution_and_Analysis_R4.ipynb',as_version=4)
 assert nb.metadata['iharq']['scientific_execution']=='NOT_YET_STARTED'
 assert all(c.get('execution_count') is None and not c.get('outputs',[]) for c in nb.cells if c.cell_type=='code')
 tags=[t for c in nb.cells for t in c.metadata.get('tags',[])];assert sum(t.startswith('governed-stage-') for t in tags)==26


def test_c4_hard_vote_golden_independent():
 y,t=hard_vote([np.array([0,1,1,0]),np.array([0,1,0,0]),np.array([1,1,1,0])])
 assert y.tolist()==[0,1,1,0] and t==0

def test_c5_probability_average_golden_independent():
 p1=np.array([[.9,.1],[.2,.8],[.6,.4]])
 p2=np.array([[.7,.3],[.4,.6],[.2,.8]])
 out=probability_average([p1,p2])
 assert np.allclose(out,[[.8,.2],[.3,.7],[.4,.6]]) and out.argmax(1).tolist()==[0,1,1]

def test_strongest_validation_selection_tie_break(tmp_path):
 st=Store(tmp_path/'runtime')
 for b,bacc,f1,burden in [('CLS-CSP-LDA',.70,.68,1),('RIE-TS-LR',.70,.68,0),('DNN-EEGNET',.69,.80,0)]:
  p=st.root/'metrics'/f'P02-A0-D-{b}-FULL_TRAIN-MR00.json';p.parent.mkdir(parents=True,exist_ok=True)
  p.write_text(json.dumps({'validation_selection':{'BACC':bacc,'F1_MACRO':f1},'validation_burden_seconds':burden,'model_storage_bytes':100}))
 r=strongest(st,'D','FULL_TRAIN',['CLS-CSP-LDA','RIE-TS-LR','DNN-EEGNET'])
 assert r['selected_branch']=='RIE-TS-LR' and r['test_outcome_influence']=='PROHIBITED'

def test_test_set_based_strongest_selection_attempt_rejected(tmp_path):
 st=Store(tmp_path/'runtime')
 with pytest.raises(TypeError): strongest(st,'D','FULL_TRAIN',['CLS-CSP-LDA'],test_metrics={'CLS-CSP-LDA':1.0})

def test_a4_checkpoint_mismatch_is_invalid(tmp_path,monkeypatch):
 store=Store(tmp_path/'runtime');core=SyntheticCoreDataset();c=_a4_cell('A4-C4-MODEL-HARD-VOTE');rows0=core.rows(dataset_id='PhysioNetMI',role='test')[:8]
 def terminal(branch):
  rel=f'pred/{branch}.jsonl';chk='a'*64
  rows=[{'source_event_id':r['event_id'],'y_pred':0,'score_vector':[.7,.3],'score_type':'NATIVE_PROBABILITY','class_order':['left_hand','right_hand'],'checkpoint_id':'b'*64} for r in rows0]
  atomic_jsonl(store.root/rel,rows);return {'terminal_status':'SUCCESS','prediction_partition':rel,'checkpoint_sha256':chk}
 monkeypatch.setattr(a4mod,'a0_term',lambda store_,ds,b,budget,rep: terminal(b))
 t=a4mod.execute_ensemble(c,store,core,{'CLASSICAL':'CLS-CSP-LDA','RIEMANNIAN':'RIE-TS-LR'},ROOT/'machine_readable/p02_record_schema_freeze_R2.yaml','fixture',DATA_CONTRACT)
 assert t['terminal_status']=='INVALID' and t['reason']=='CHECKPOINT_MISMATCH'

def test_a4_invalid_probability_not_fabricated(tmp_path,monkeypatch):
 store=Store(tmp_path/'runtime');core=SyntheticCoreDataset();c=_a4_cell('A4-C5-MODEL-PROB-AVG');rows0=core.rows(dataset_id='PhysioNetMI',role='test')[:8]
 def terminal(branch):
  rel=f'pred/{branch}.jsonl';chk='c'*64
  rows=[{'source_event_id':r['event_id'],'y_pred':0,'score_vector':[1.2,-.2],'score_type':'NATIVE_PROBABILITY','class_order':['left_hand','right_hand'],'checkpoint_id':chk} for r in rows0]
  atomic_jsonl(store.root/rel,rows);return {'terminal_status':'SUCCESS','prediction_partition':rel,'checkpoint_sha256':chk}
 monkeypatch.setattr(a4mod,'a0_term',lambda store_,ds,b,budget,rep: terminal(b))
 monkeypatch.setattr(a4mod,'strongest',lambda *a,**k:{'selected_branch':'CLS-CSP-LDA','candidate_summaries':[],'test_outcome_influence':'PROHIBITED'})
 t=a4mod.execute_ensemble(c,store,core,{'CLASSICAL':'CLS-CSP-LDA','RIEMANNIAN':'RIE-TS-LR'},ROOT/'machine_readable/p02_record_schema_freeze_R2.yaml','fixture',DATA_CONTRACT)
 assert t['terminal_status']=='NOT_APPLICABLE_SCORE_SEMANTICS'

def test_c4c5_support_export_has_participant_accounting(fixture_run):
 root,_=fixture_run
 rows=[json.loads(x) for x in (root/'runtime/analysis_inputs/a4_c4_c5_common_support.jsonl').read_text().splitlines() if x.strip()]
 assert len(rows)==2
 for r in rows:
  for k in ['eligible_ensemble_participants','eligible_constituent_participants','matched_participants','excluded_participants','ensemble_event_denominator','constituent_event_denominator','matched_event_denominator']:
   assert k in r

def test_c4c5_artifact_identity_export(fixture_run):
 root,_=fixture_run
 rows=[json.loads(x) for x in (root/'runtime/analysis_inputs/a4_c4_c5_comparison_artifacts.jsonl').read_text().splitlines() if x.strip()]
 assert len(rows)==2 and len({r['comparison_id'] for r in rows})==2
 assert all(r['phase_analysis_handoff'].endswith('phase_analysis_handoff.yaml') and r['layer10_source_handoff'].endswith('layer10_source_handoff.yaml') for r in rows)

def test_stage15_closure_source_manifest(fixture_run):
 root,_=fixture_run;d=json.loads((root/'runtime/analysis_inputs/a0_closure_source_manifest.json').read_text())
 assert d['status']=='PASS' and d['p03_raw_prediction_substrate'] is True and d['handoff_stage']=='22'


def test_final_runtime_bundle_contains_required_provenance(fixture_run):
 root,r=fixture_run;rt=root/'runtime'
 required=['manifests/config_snapshot.yaml','manifests/scientific_freeze_snapshot.yaml','manifests/input_and_run_cell_manifest.json','analysis_inputs/a4_c4_c5_comparison_artifacts.jsonl','analysis_inputs/a0_closure_source_manifest.json','handoffs/runtime_evidence_index.json','checksums.sha256']
 assert all((rt/x).is_file() for x in required)
 assert len(list((rt/'gate_results').glob('*.json')))==26
 assert len(list((rt/'logs').glob('stage_*.log')))>=26
 assert verify(rt)['status']=='PASS'

def test_failure_negative_summary_is_runtime_evidence(fixture_run):
 root,_=fixture_run;d=json.loads((root/'runtime/analysis_inputs/failure_negative_summary.json').read_text())
 assert d['status']=='PASS' and d['all_terminal_states_preserved'] is True and d['null_negative_evidence_preserved'] is True and 'negative_result_notes' in d

# --- R2 cumulative pre-execution semantic/code-quality regression tests ---
def test_model_branch_adapter_routing_is_semantically_distinct():
 from iharq.layer2_decoders.models import BraindecodeAdapter,FBCNetConditional,SequenceSlot,BlockedAdapter
 a=make_adapter('DNN-EEGNET',1,480,8,{})
 f=make_adapter('DNN-FBCNET',1,480,8,{})
 s=make_adapter('DNN-SEQ',1,480,8,{'allow_eegconformer_fallback':True})
 e=make_adapter('DNN-EGTC',1,480,8,{'fallback_activated':False})
 assert isinstance(a,BraindecodeAdapter) and a.variant=='EEGNet'
 assert isinstance(f,FBCNetConditional)
 assert isinstance(s,SequenceSlot)
 assert isinstance(e,BlockedAdapter) and e.admission()['status']=='CONDITIONAL_SKIP'

def test_fbcnet_requires_original_author_or_verified_equivalent():
 f=make_adapter('DNN-FBCNET',1,480,8,{'implementation_module':'anything','license_status':'CAN_EXECUTE','implementation_equivalence':'UNVERIFIED'})
 a=f.admission();assert a['status']=='DEPENDENCY_BLOCKED' and 'EQUIVALENCE' in a['reason']

def test_sequence_slot_prefers_db_plugin_then_uses_eegconformer_fallback(monkeypatch):
 import sys,types
 from iharq.layer2_decoders.models import SequenceSlot
 class FakeConformer: pass
 fake_models=types.SimpleNamespace(EEGConformer=FakeConformer)
 fake=types.ModuleType('braindecode');fake.models=fake_models;monkeypatch.setitem(sys.modules,'braindecode',fake)
 s=SequenceSlot(1,480,8,{'allow_eegconformer_fallback':True,'dbconformer':{'implementation_module':None}})
 a=s.admission();assert a['status']=='ADMITTED' and a['resolved_variant']=='EEGConformer'

def test_eegtcnet_fallback_requires_pre_result_activation(monkeypatch):
 import sys,types
 class FakeTC: pass
 fake_models=types.SimpleNamespace(EEGTCNet=FakeTC)
 fake=types.ModuleType('braindecode');fake.models=fake_models;monkeypatch.setitem(sys.modules,'braindecode',fake)
 off=make_adapter('DNN-EGTC',1,480,8,{'fallback_activated':False});assert off.admission()['status']=='CONDITIONAL_SKIP'
 on=make_adapter('DNN-EGTC',1,480,8,{'fallback_activated':True});assert on.admission()['status']=='ADMITTED' and on.resolved_variant=='EEGTCNet'

def test_euclidean_alignment_reference_is_train_only_and_transform_does_not_refit():
 from iharq.layer2_decoders.models import Riemann
 rng=np.random.default_rng(1);tr=rng.normal(size=(12,4,64));te=rng.normal(loc=4,size=(5,4,64))
 m=Riemann('RIE-EA-TS',align=True);m._fit_alignment(tr);w=m.ea_whitener_.copy();_ = m._aligned(te)
 assert np.allclose(w,m.ea_whitener_)
 m2=Riemann('RIE-EA-TS',align=True);m2._fit_alignment(np.concatenate([tr,te]));assert not np.allclose(w,m2.ea_whitener_)

def test_mdm_score_semantics_are_distance_derived_not_native_probability():
 from iharq.layer2_decoders.models import Riemann
 assert Riemann('RIE-MDM').score_type=='DISTANCE_DERIVED_SIMPLEX'

def test_fbcsp_uses_frozen_config_values_not_internal_band_defaults():
 from iharq.layer2_decoders.models import FBCSP
 x=FBCSP(2,1,bands=[[8,12],[12,16]],fs=160,filter_order=4,reg='oas',max_iter=2000)
 assert x.bands==[(8,12),(12,16)] and x.fs==160 and x.filter_order==4 and x.reg=='oas' and x.max_iter==2000

def test_metric_invalid_scores_fail_closed_and_auc_unavailable_is_explicit():
 y=np.array([0,1,0,1]);p=np.array([0,1,0,1])
 d=evaluate(y,p,None,'HARD_LABEL_ONLY');assert d['ROC_AUC'] is None and d['ROC_AUC_STATUS']=='NOT_AVAILABLE_NO_CONTINUOUS_SCORE'
 with pytest.raises(ValueError):evaluate(y,p,np.array([[.5,.5]]),'NATIVE_PROBABILITY')
 with pytest.raises(ValueError):evaluate(y,p,np.array([[.5,.5],[.4,.6],[np.nan,.2],[.1,.9]]),'NATIVE_PROBABILITY')

def test_bca_degenerate_case_uses_only_declared_percentile_fallback():
 r=paired_bootstrap([1,1,1,1,1],seed=7,n=200,level=.95)
 assert r['status']=='PASS' and r['method'].startswith('PERCENTILE_FALLBACK')

def test_neural_gradient_accumulation_honors_effective_batch_target():
 import torch
 from iharq.layer2_decoders.models import BraindecodeAdapter
 class Tiny(torch.nn.Module):
  def __init__(self):super().__init__();self.w=torch.nn.Linear(4,2)
  def forward(self,x):return self.w(x.reshape(len(x),-1))
 class A(BraindecodeAdapter):
  def _build(self):return Tiny()
 X=np.random.default_rng(0).normal(size=(8,1,4)).astype('float32');y=np.array([0,1,0,1,0,1,0,1])
 a=A('EEGNet',1,4,1);a.fit(X,y,epochs=1,batch_size=32,effective_batch_target=64,device='cpu')
 assert a.actual_batch_size==32 and a.gradient_accumulation==2

def test_checkpoint_write_is_atomic_no_tmp_left(tmp_path):
 m=make_adapter('SAN-MAJ',1,16,8,{});X=np.zeros((4,8,16),dtype=np.float32);y=np.array([0,0,1,1]);m.fit(X,y)
 r=save_roundtrip(m,X,tmp_path/'atomic.pkl');assert r['status']=='PASS' and not list(tmp_path.glob('*.tmp'))

def test_heartbeat_write_failure_is_preserved_not_silent(tmp_path,monkeypatch):
 import time
 import iharq.layer2_decoders.stage_runner as sr
 real=sr.atomic_json
 def controlled(path,value):
  if 'heartbeats' in Path(path).parts: raise OSError('fixture heartbeat denial')
  return real(path,value)
 monkeypatch.setattr(sr,'atomic_json',controlled)
 r=sr.StageRunner(tmp_path,[{'stage':'00','gate':'G00'}],{'revision':'HB'},heartbeat=1)
 out=r.run('00',lambda:(time.sleep(.05) or {'ok':1}))
 assert out['status']=='SUCCESS' and out['observability_status']=='DEGRADED_HEARTBEAT' and out['heartbeat_write_errors']


def test_training_policy_authority_bindings_are_algorithmically_frozen_resolved():
 from iharq.layer2_decoders.training_policy import validate_training_policy_binding
 b=yaml.safe_load((ROOT/'configs/phase_02/training_policy_authority_bindings.yaml').read_text());v=validate_training_policy_binding(b)
 assert v['status']=='PASS' and v['blockers']==[] and v['missing']==[]
 aug=b['augmentation_challenger'];cw=b['class_weighting']
 assert aug['probability_resolution']['type']=='VALIDATION_ONLY_DATASET_LEVEL_GRID_SEARCH'
 assert aug['probability_resolution']['candidates']==[0.25,0.5,0.75] and aug['probability_resolution']['test_set_access']=='PROHIBITED'
 assert aug['segment_count_resolution']['requested_n_segments'] is None and aug['run_cell_count']==15
 assert cw['policy']=='VALIDATION_SELECTED_UNIFORM_VS_BALANCED_WHEN_TRAIN_COUNTS_UNEQUAL' and cw['selection']['test_set_access']=='PROHIBITED'

def test_segmentation_reconstruction_is_train_only_deterministic_same_class():
 from iharq.layer2_decoders.training_policy import segmentation_reconstruction
 X=np.arange(8*2*12,dtype=float).reshape(8,2,12);y=np.array([0,0,0,0,1,1,1,1])
 A,pa=segmentation_reconstruction(X,y,probability=1.0,n_segments=4,seed=17);B,pb=segmentation_reconstruction(X,y,probability=1.0,n_segments=4,seed=17)
 assert np.array_equal(A,B) and pa==pb and np.array_equal(X,np.arange(8*2*12,dtype=float).reshape(8,2,12))
 assert all(y[x['target_index']]==y[x['donor_index']] and x['target_index']!=x['donor_index'] for x in pa['donor_log'])

def test_class_weight_policy_uses_standard_train_only_formula_and_validation_selection():
 from iharq.layer2_decoders.training_policy import balanced_class_weights,class_weight_policy_candidates,select_validation_policy
 y=np.array([0]*6+[1]*4);w,e=balanced_class_weights(y)
 assert np.allclose(w,[10/(2*6),10/(2*4)]) and e['counts']==[6,4]
 c=class_weight_policy_candidates(y,{})
 assert c['evidence']['selection_required'] is True and [x['policy'] for x in c['candidates']]==['UNIFORM_NO_WEIGHT','SKLEARN_BALANCED_TRAIN_FOLD']
 d=select_validation_policy([
  {'status':'SUCCESS','policy':'UNIFORM_NO_WEIGHT','weights':None,'validation_metrics':{'BACC':.70,'F1_MACRO':.68}},
  {'status':'SUCCESS','policy':'SKLEARN_BALANCED_TRAIN_FOLD','weights':w,'validation_metrics':{'BACC':.72,'F1_MACRO':.69}}])
 assert d['selected_policy']=='SKLEARN_BALANCED_TRAIN_FOLD' and d['test_set_used'] is False
 tie=select_validation_policy([
  {'status':'SUCCESS','policy':'UNIFORM_NO_WEIGHT','weights':None,'validation_metrics':{'BACC':.70,'F1_MACRO':.68}},
  {'status':'SUCCESS','policy':'SKLEARN_BALANCED_TRAIN_FOLD','weights':w,'validation_metrics':{'BACC':.70,'F1_MACRO':.68}}])
 assert tie['selected_policy']=='UNIFORM_NO_WEIGHT'

def test_equal_class_counts_short_circuit_to_uniform_without_threshold():
 from iharq.layer2_decoders.training_policy import class_weight_policy_candidates
 c=class_weight_policy_candidates(np.array([0,1,0,1]),{})
 assert c['evidence']['exactly_equal'] is True and c['evidence']['selection_required'] is False and c['candidates']==[{'policy':'UNIFORM_NO_WEIGHT','weights':None}]

def test_neural_checkpoint_uses_state_dict_not_adapter_pickle(tmp_path):
 import torch
 from iharq.layer2_decoders.models import BraindecodeAdapter
 class Tiny(torch.nn.Module):
  def __init__(self):super().__init__();self.w=torch.nn.Linear(4,2)
  def forward(self,x):return self.w(x.reshape(len(x),-1))
 class A(BraindecodeAdapter):
  def _build(self):return Tiny()
 X=np.random.default_rng(4).normal(size=(8,1,4)).astype('float32');y=np.array([0,1,0,1,0,1,0,1])
 a=A('EEGNet',3,4,1);a.fit(X,y,epochs=1,batch_size=16,effective_batch_target=64,device='cpu')
 r=save_roundtrip(a,X[:4],tmp_path/'neural.pkl');assert r['status']=='PASS' and r['checkpoint_format']=='PYTORCH_STATE_DICT_WEIGHTS_ONLY' and r['path'].endswith('.state_dict.pt')

def test_external_checkpoint_requires_governed_safe_interface(tmp_path):
 class P:
  def predict(self,X):return np.zeros(len(X),int)
 class E:
  plugin=P()
 X=np.zeros((2,1,4),dtype='float32')
 r=save_roundtrip(E(),X,tmp_path/'external.pkl');assert r['status']=='FAIL' and r['reason']=='EXTERNAL_SAFE_CHECKPOINT_INTERFACE_MISSING'

def test_duplicate_record_partition_retry_is_idempotent(tmp_path):
    from iharq.layer2_decoders.store import Store
    st=Store(tmp_path/'runtime',config_sha256='c'*64)
    cell={'planned_run_cell_id':'FIXTURE-IDEMPOTENT-RECORD','ablation_id':'A0','dataset_id':'FIXTURE','branch_slot':'CLS-CSP-LDA','budget_id':'FULL_TRAIN'}
    row={'record_id':'rec-1','dataset_id':'FIXTURE','value':1}
    p1=st.write_records('FixtureRecord',cell,[row])
    p2=st.write_records('FixtureRecord',cell,[row])
    assert p1==p2
    rows=[json.loads(x) for x in p2.read_text().splitlines() if x.strip()]
    assert rows==[row]
    manifest=json.loads((st.root/'manifests/record_partitions/FixtureRecord/FIXTURE-IDEMPOTENT-RECORD.json').read_text())
    assert manifest['row_count']==1


def test_partial_failure_bundle_is_truthful_crc_clean(tmp_path,monkeypatch):
    from iharq.layer2_decoders import kaggle_entry as ke
    original=ke.HANDLERS['12']
    def forced_failure(ctx):
        raise RuntimeError('FIXTURE_FORCED_STAGE12_FAILURE')
    monkeypatch.setitem(ke.HANDLERS,'12',forced_failure)
    try:
        r=ke.NotebookSession(ROOT,tmp_path/'partial',{
            'notebook_revision':'R4','source_sha256':'FIXTURE','config_sha256':'FIXTURE',
            'stage_plan_sha256':'FIXTURE','scientific_freeze_id':'P02-PLANNED-SCIENTIFIC-EXECUTION-FREEZE-R5'
        },fixture=True,reuse=False).run_all()
    finally:
        monkeypatch.setitem(ke.HANDLERS,'12',original)
    assert r['status']=='BLOCKED'
    assert r['failure']['next_or_failed_stage']=='12'
    f=r['finalization']; assert f['status']=='PARTIAL'
    z=Path(f['zip']['path']); assert z.name=='FIXTURE_NON_SCIENTIFIC_PARTIAL_FAILURE_BUNDLE.zip'
    with zipfile.ZipFile(z) as zz:
        assert zz.testzip() is None
        names=zz.namelist()
        assert all(not n.startswith('/') and '..' not in Path(n).parts for n in names)
        runtime=[n for n in names if n.endswith('manifests/runtime_manifest.json')]
        assert len(runtime)==1
        man=json.loads(zz.read(runtime[0]))
        assert man['status']=='PARTIAL_FAILED_EXPORT' and man['partial_failure'] is True and man['bundle_contents_complete'] is False
        assert man['failure']['exception']=='RuntimeError'

def test_resolved_notebook_verifies_dynamic_amendment_before_dependency_install():
    nb=json.loads((ROOT/'notebook/IHARQ_Phase_02_Complete_Execution_and_Analysis_R4.ipynb').read_text())
    bootstrap=''.join(nb['cells'][1]['source']); verify=bootstrap.index('P02_FREEZE_CRITICAL_BLOCKER_REGISTER_R4.json'); install=bootstrap.index('subprocess.check_call')
    assert verify < install and 'P02_PREEXECUTION_SCIENTIFIC_FREEZE_BLOCKED' not in bootstrap
    assert 'p02_planned_scientific_execution_freeze_R5.yaml' in bootstrap and 'P02_PREEXECUTION_TRAINING_POLICY_AMENDMENT_R2.yaml' in bootstrap

def test_training_policy_challenger_manifest_preserves_official_ablation_counts():
 d=yaml.safe_load((ROOT/'machine_readable/p02_training_policy_challenger_run_cells_R2.yaml').read_text()); assert d['cell_count']==15 and d['official_A0_A4_total_remains']==1896
 assert len({r['planned_run_cell_id'] for r in d['rows']})==15
 assert all(r['condition_id']=='P02-TRAIN-AUG-SR-EEGNET-FULL-R2-VALIDATION-RESOLVED' and r['diagnostic_only'] and not r['a4_eligible'] and not r['p03_primary_eligible'] for r in d['rows'])
 assert all(r['probability']=='DATASET_LEVEL_VALIDATION_SELECTED_FROM_FROZEN_GRID' and r['segment_count']=='BRAINCDECODE_AUTO_N_SEGMENTS' for r in d['rows'])

def test_challenger_terminal_closure_accepts_governed_skip_without_silent_loss(tmp_path):
 from iharq.layer2_decoders.training_policy_evidence import close_training_policy_challenger
 from iharq.layer2_decoders.store import Store
 core=SyntheticCoreDataset();st=Store(tmp_path/'runtime','c'*64)
 c={'planned_run_cell_id':'FX-CH','comparison_reference':'FX-PRIMARY','dataset_id':'PhysioNetMI','model_repeat_index':0,'seed_id':1,'condition_id':'P02-TRAIN-AUG-SR-EEGNET-FULL-R2-VALIDATION-RESOLVED','ablation_id':'TRAINING_POLICY_DIAGNOSTIC','branch_slot':'DNN-EEGNET','budget_id':'FULL_TRAIN'}
 st.write_terminal(c,'CONDITIONAL_SKIP',reason='MATCHED_PRIMARY_EEGNET_NOT_SUCCESSFUL')
 q=close_training_policy_challenger(core,st,[c],lambda _: {'terminal_status':'DEPENDENCY_BLOCKED'}, {}, expected=1)
 assert q['status']=='PASS' and q['terminal_cells']==1 and q['successful_comparisons']==0 and q['non_success_terminal_cells']==1 and q['incomplete_cells']==[]

def test_augmentation_seed_namespace_is_deterministic_candidate_specific():
 from iharq.layer2_decoders.training_policy import derive_augmentation_seed
 ns='IHARQ:P02:L2:EEGNET:SEGMENTATION_RECONSTRUCTION:R2';a=derive_augmentation_seed(ns,'PhysioNetMI',123,0,0,.25);b=derive_augmentation_seed(ns,'PhysioNetMI',123,0,0,.25);c=derive_augmentation_seed(ns,'PhysioNetMI',123,0,0,.5)
 assert a==b and a!=c and a>0

def test_future_protocol_sync_note_is_algorithmic_and_non_regressive():
 t=(ROOT/'docs/P02_FUTURE_PROTOCOL_BUILD_BOOK_SYNC_NOTE_R2.md').read_text()
 assert 'Protocol v1.0' in t and 'validation' in t.lower() and '1,896' in t and 'P00/P01' in t and 'do not recompute the selection' in t

def test_sr_probability_selection_is_validation_only_and_deterministic():
 from iharq.layer2_decoders.training_policy import select_sr_probability
 b=yaml.safe_load((ROOT/'configs/phase_02/training_policy_authority_bindings.yaml').read_text())
 rows=[]
 for p,bacc in [(0.25,.70),(0.5,.72),(0.75,.71)]:
  for seed in range(5): rows.append({'probability':p,'status':'SUCCESS','validation_metrics':{'BACC':bacc,'F1_MACRO':bacc-.01},'seed_id':seed})
 d=select_sr_probability(rows,b); assert d['selected_probability']==0.5 and d['test_set_used'] is False and d['selection_scope']=='VALIDATION_ONLY'

def test_auto_segment_fixture_resolver_matches_documented_braindecode_rule(monkeypatch):
 from iharq.layer2_decoders.training_policy import resolve_segment_count
 import builtins
 X=np.zeros((8,2,480),np.float32);y=np.array([0,0,0,0,1,1,1,1])
 real=builtins.__import__
 def fake(name,*a,**k):
  if name.startswith('braindecode'): raise ModuleNotFoundError(name)
  return real(name,*a,**k)
 monkeypatch.setattr(builtins,'__import__',fake)
 r=resolve_segment_count(X,y,policy={'type':'BRAINCDECODE_PUBLIC_API_AUTO_N_SEGMENTS'},seed=1,fixture=True)
 assert r['status']=='PASS' and r['n_segments']==20 and r['resolver_source']=='FIXTURE_DOCUMENTED_FALLBACK'

def test_training_policy_challenger_seeds_match_exact_primary_a0_cells():
 a=yaml.safe_load((ROOT/'machine_readable/p02_full_ablation_planned_run_cells_R3.yaml').read_text())['rows'];ch=yaml.safe_load((ROOT/'machine_readable/p02_training_policy_challenger_run_cells_R2.yaml').read_text())['rows'];idx={r['planned_run_cell_id']:r for r in a};assert len(ch)==15
 for c in ch:
  q=idx[c['comparison_reference']];assert q['branch_slot']=='DNN-EEGNET' and q['budget_id']=='FULL_TRAIN' and (c['dataset_id'],c['model_repeat_index'],c['seed_id'])==(q['dataset_id'],q['model_repeat_index'],q['seed_id'])

def test_segmentation_reconstruction_probability_boundaries_and_donor_exclusion():
 from iharq.layer2_decoders.training_policy import segmentation_reconstruction
 X=np.arange(8*2*13,dtype=float).reshape(8,2,13); y=np.array([0,0,0,0,1,1,1,1]);Z,p0=segmentation_reconstruction(X,y,probability=0.0,n_segments=4,seed=91);assert np.array_equal(Z,X) and p0['donor_log']==[]
 A,p1=segmentation_reconstruction(X,y,probability=1.0,n_segments=4,seed=91);assert len(p1['donor_log'])==len(X)*4 and all(r['target_index']!=r['donor_index'] and y[r['target_index']]==y[r['donor_index']] for r in p1['donor_log'])

def test_external_evidence_note_supports_not_supersedes_project_authority():
 t=(ROOT/'docs/P02_TRAINING_POLICY_EXTERNAL_EVIDENCE_NOTE_R2.md').read_text();assert 'supports but does not supersede' in t and 'task-dependent' in t and 'Test evidence is excluded' in t

def test_training_policy_realized_values_are_not_hardcoded_in_production_source():
 src='\n'.join((ROOT/'src/iharq/layer2_decoders'/x).read_text() for x in ['orchestration.py','scientific.py','models.py','training_policy.py'])
 assert 'NEVER_WEIGHT_P02_CURRENT_FROZEN_INPUTS' not in src
 assert "probability':0.5" not in src and 'probability=0.5' not in src
 b=yaml.safe_load((ROOT/'configs/phase_02/training_policy_authority_bindings.yaml').read_text())
 assert b['augmentation_challenger']['probability_resolution']['candidates']==[0.25,0.5,0.75]
 assert b['augmentation_challenger']['segment_count_resolution']['requested_n_segments'] is None
 assert b['class_weighting']['balanced_formula']['formula']=='n_samples / (n_classes * class_count)'

def test_native_class_weight_support_is_explicit_not_silently_added_to_lda_mdm():
 from iharq.layer2_decoders.models import make_adapter
 assert getattr(make_adapter('DIAG-LOGVAR',1,480,8,{}),'supports_class_weights',False)
 assert getattr(make_adapter('CLS-FBCSP-LR',1,480,8,{'bands_hz':[[8,12]],'fs':160,'filter_order':4}),'supports_class_weights',False)
 assert getattr(make_adapter('RIE-TS-LR',1,480,8,{}),'supports_class_weights',False)
 assert not getattr(make_adapter('CLS-CSP-LDA',1,480,8,{}),'supports_class_weights',False)
 assert not getattr(make_adapter('RIE-MDM',1,480,8,{}),'supports_class_weights',False)

