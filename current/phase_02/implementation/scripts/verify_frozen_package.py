#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,csv,yaml,nbformat,zipfile,re,sys
ROOT=Path(__file__).resolve().parents[1]
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
def main():
 fails=[]
 def c(name,cond,detail=''):
  if not cond:fails.append((name,detail))
 req=['checksums.sha256','P02_KAGGLE_PREEXECUTION_AUDIT_FINAL_CERTIFICATION_R5_HF.md','P02_HF_OPERATIONAL_RELEASE_MANIFEST_R5.json','validation/P02_HF_CONDITIONAL_ASSET_AUDIT_R1.json','validation/P02_HF_SECRET_SAFETY_AUDIT_R1.json','notebook/IHARQ_Phase_02_Complete_Execution_and_Analysis_R4_HF_R1.ipynb','configs/phase_02/models/huggingface_assets.yaml','docs/KAGGLE_RUN_GUIDE_R5_HF.md','P02_KAGGLE_PREEXECUTION_AUDIT_FINAL_CERTIFICATION_R4.md','validation/final_authoring_validation.json','validation/P02_FREEZE_CRITICAL_BLOCKER_REGISTER_R4.json','validation/P02_EXPANDED_FINAL_READINESS_R4.json','validation/P02_TRAINING_POLICY_SOURCE_EXHAUSTION_R2.json','validation/P02_TRAINING_POLICY_BLOCKER_RESOLUTION_REGISTER_R4.json','validation/P02_TRAINING_POLICY_CODE_OWNERSHIP_AUDIT_R2.json','validation/P02_OTHER_SAME_CLASS_FREEZE_GAP_AUDIT_R4.json','validation/P02_UPSTREAM_STATE_REVALIDATION_R4.json','validation/P02_AUDIT_SECTIONS_1_274_EXHAUSTION_R4.csv','validation/P02_PROMPT_275_323_TRACEABILITY.csv','validation/FIXTURE_NON_SCIENTIFIC_RUNTIME_BUNDLE.zip','contracts/P02_PREEXECUTION_TRAINING_POLICY_AMENDMENT_R2.yaml','configs/phase_02/training_policy_authority_bindings.yaml','machine_readable/p02_planned_scientific_execution_freeze_R5.yaml','machine_readable/p02_training_policy_challenger_run_cells_R2.yaml','machine_readable/p02_protocol_v1_handoff_template.yaml','docs/P02_FUTURE_PROTOCOL_BUILD_BOOK_SYNC_NOTE_R2.md','docs/P02_TRAINING_POLICY_EXTERNAL_EVIDENCE_NOTE_R2.md','notebook/IHARQ_Phase_02_Complete_Execution_and_Analysis_R4.ipynb']
 for r in req:c('exists:'+r,(ROOT/r).is_file())
 bad=[];n=0
 for line in (ROOT/'checksums.sha256').read_text().splitlines():
  if not line.strip():continue
  n+=1;m=re.match(r'^([0-9a-f]{64})  (.+)$',line)
  if not m:bad.append(('malformed',line));continue
  hh,rel=m.groups();p=ROOT/rel
  if not p.is_file():bad.append(('missing',rel))
  elif sha(p)!=hh:bad.append(('mismatch',rel))
 c('checksums',not bad,(n,bad[:5]))
 f=json.loads((ROOT/'validation/final_authoring_validation.json').read_text()); c('final_validation',f['status']=='PASS' and f['freeze_critical_blockers']==0 and f['ready_for_actual_kaggle_execution'] and not f['scientific_execution_started'])
 br=json.loads((ROOT/'validation/P02_FREEZE_CRITICAL_BLOCKER_REGISTER_R4.json').read_text());c('blockers',br['status']=='PASS' and br['freeze_critical_blocker_count']==0)
 rd=json.loads((ROOT/'validation/P02_EXPANDED_FINAL_READINESS_R4.json').read_text());c('readiness',rd['status']=='PASS' and rd['freeze_critical_blocker_count']==0 and all(v==0 for v in rd['zero_defect_invariants'].values()))
 se=json.loads((ROOT/'validation/P02_TRAINING_POLICY_SOURCE_EXHAUSTION_R2.json').read_text());c('source_exhaustion',se['status']=='PASS' and se['other_same_class_freeze_gaps_found']==0)
 sg=json.loads((ROOT/'validation/P02_OTHER_SAME_CLASS_FREEZE_GAP_AUDIT_R4.json').read_text());c('same_class',sg['status']=='PASS' and sg['other_same_class_freeze_gaps_found']==0)
 b=yaml.safe_load((ROOT/'configs/phase_02/training_policy_authority_bindings.yaml').read_text()); a=b['augmentation_challenger'];w=b['class_weighting'];c('dynamic_aug',a['probability_resolution']['test_set_access']=='PROHIBITED' and len(a['probability_resolution']['candidates'])==3 and a['segment_count_resolution']['requested_n_segments'] is None and a['run_cell_count']==15);c('dynamic_weight',w['policy']=='VALIDATION_SELECTED_UNIFORM_VS_BALANCED_WHEN_TRAIN_COUNTS_UNEQUAL' and w['balanced_formula']['type']=='SKLEARN_COMPUTE_CLASS_WEIGHT_BALANCED' and w['selection']['test_set_access']=='PROHIBITED')
 fr=yaml.safe_load((ROOT/'machine_readable/p02_planned_scientific_execution_freeze_R5.yaml').read_text());c('freeze_R5',fr['freeze_id']=='P02-PLANNED-SCIENTIFIC-EXECUTION-FREEZE-R5' and fr['preexecution_amendment_id']=='P02-PREEXEC-TRAINING-POLICY-AMENDMENT-R2' and fr.get('owner_decisions_remaining',0)==0 and fr['training_policy_resolution']['class_weighting']==w)
 ch=yaml.safe_load((ROOT/'machine_readable/p02_training_policy_challenger_run_cells_R2.yaml').read_text());c('challenger_15',ch['cell_count']==15 and len(ch['rows'])==15 and ch['official_A0_A4_total_remains']==1896)
 nb=nbformat.read(ROOT/'notebook/IHARQ_Phase_02_Complete_Execution_and_Analysis_R4.ipynb',as_version=4);nbformat.validate(nb);txt='\n'.join(x.source for x in nb.cells);tags=[t for x in nb.cells for t in x.metadata.get('tags',[]) if t.startswith('governed-stage-')];c('notebook',len(tags)==26 and nb.metadata['iharq']['scientific_freeze']=='P02-PLANNED-SCIENTIFIC-EXECUTION-FREEZE-R5' and nb.metadata['iharq']['preexecution_amendment']=='P02-PREEXEC-TRAINING-POLICY-AMENDMENT-R2' and all(x.get('execution_count') is None and not x.get('outputs',[]) for x in nb.cells if x.cell_type=='code'));c('notebook_note','FUTURE PROTOCOL / BUILD-BOOK SYNCHRONIZATION REQUIRED' in txt and 'P02_FREEZE_CRITICAL_BLOCKER_REGISTER_R4.json' in txt)
 with zipfile.ZipFile(ROOT/'validation/FIXTURE_NON_SCIENTIFIC_RUNTIME_BUNDLE.zip') as z:
  names=z.namelist(); c('fixture_crc',z.testzip() is None); c('fixture_safe',all(not Path(x).is_absolute() and '..' not in Path(x).parts for x in names)); reqz=['P02_PREEXECUTION_TRAINING_POLICY_AMENDMENT_R2.yaml','P02_FUTURE_PROTOCOL_BUILD_BOOK_SYNC_NOTE_R2.md','P02_TRAINING_POLICY_EXTERNAL_EVIDENCE_NOTE_R2.md','training_policy_sr_probability_selection.json'];c('fixture_dynamic_artifacts',all(any(n.endswith(x) for n in names) for x in reqz)); sel=[n for n in names if n.endswith('training_policy_sr_probability_selection.json')][0];sj=json.loads(z.read(sel));c('fixture_selector',sj['status']=='PASS' and not sj['test_set_used'])
 hf=yaml.safe_load((ROOT/'configs/phase_02/models/huggingface_assets.yaml').read_text());cb=hf['assets']['SSL-CBRAMOD'];rv=hf['assets']['SSL-REVE'];c('hf_policy',hf['policy_id']=='P02-HF-CONDITIONAL-ASSET-POLICY-R1' and cb['revision']=='584cdc415913739a05d84bf0c1cb3db397764507' and cb['checkpoint_sha256']=='a939ace9aa1e229f08391ad8bb2d197b507ae2c519a50addf087f0151b2df5c3' and rv['download_policy']=='DO_NOT_DOWNLOAD_CURRENT_P02')
 hnb=nbformat.read(ROOT/'notebook/IHARQ_Phase_02_Complete_Execution_and_Analysis_R4_HF_R1.ipynb',as_version=4);ht='\n'.join(x.source for x in hnb.cells);c('hf_notebook', 'getpass.getpass' in ht and 'UserSecretsClient' in ht and 'SESSION.clear_hf_token()' in ht and 'HF_TOKEN = None' in ht and all(x.get('execution_count') is None and not x.get('outputs',[]) for x in hnb.cells if x.cell_type=='code'))
 ha=json.loads((ROOT/'validation/P02_HF_CONDITIONAL_ASSET_AUDIT_R1.json').read_text());hs=json.loads((ROOT/'validation/P02_HF_SECRET_SAFETY_AUDIT_R1.json').read_text());c('hf_audits',ha['status']=='PASS' and hs['status']=='PASS')
 print(json.dumps({'status':'PASS' if not fails else 'FAIL','release_readiness':'READY_FOR_GOVERNED_KAGGLE_EXECUTION' if not fails else 'NOT_READY','checksums_rows':n,'failures':fails},indent=2)); return 0 if not fails else 1
if __name__=='__main__': raise SystemExit(main())
