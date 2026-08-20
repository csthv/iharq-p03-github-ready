#!/usr/bin/env python3
from pathlib import Path
import json,yaml,csv,re,zipfile,nbformat,sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from iharq.layer2_decoders.training_policy import validate_training_policy_binding
from iharq.layer2_decoders.orchestration import HANDLERS,FAMILY_STAGE
from iharq.layer2_decoders.security import scan_tree

def main():
 rows=[]
 def ck(name,cond,detail=''): rows.append({'check':name,'status':'PASS' if cond else 'FAIL','detail':detail})
 required=['README.md','requirements-kaggle.txt','notebook/IHARQ_Phase_02_Complete_Execution_and_Analysis_R4_HF_R1.ipynb','src/iharq/layer2_decoders/hf_assets.py','src/iharq/layer2_decoders/hf_cbramod_adapter.py','configs/phase_02/models/huggingface_assets.yaml','docs/HUGGINGFACE_CONDITIONAL_ASSET_POLICY_R1.md','docs/KAGGLE_RUN_GUIDE_R5_HF.md','P02_HF_OPERATIONAL_RELEASE_MANIFEST_R5.json','P02_KAGGLE_PREEXECUTION_AUDIT_FINAL_CERTIFICATION_R4.md','notebook/IHARQ_Phase_02_Complete_Execution_and_Analysis_R4.ipynb','src/iharq/layer2_decoders/orchestration.py','src/iharq/layer2_decoders/training_policy.py','src/iharq/layer2_decoders/scientific.py','configs/phase_02/phase.yaml','configs/phase_02/training_policy_authority_bindings.yaml','contracts/P02_PREEXECUTION_TRAINING_POLICY_AMENDMENT_R2.yaml','docs/P02_FUTURE_PROTOCOL_BUILD_BOOK_SYNC_NOTE_R2.md','docs/P02_TRAINING_POLICY_EXTERNAL_EVIDENCE_NOTE_R2.md','machine_readable/p02_planned_scientific_execution_freeze_R5.yaml','machine_readable/p02_training_policy_challenger_run_cells_R2.yaml','machine_readable/p02_full_ablation_planned_run_cells_R3.yaml','machine_readable/p02_notebook_stage_plan_R4.yaml','validation/P02_FREEZE_CRITICAL_BLOCKER_REGISTER_R4.json','validation/P02_TRAINING_POLICY_BLOCKER_RESOLUTION_REGISTER_R4.json','validation/P02_TRAINING_POLICY_SOURCE_EXHAUSTION_R2.json','validation/P02_OTHER_SAME_CLASS_FREEZE_GAP_AUDIT_R4.json','validation/P02_TRAINING_POLICY_CODE_OWNERSHIP_AUDIT_R2.json','validation/P02_EXPANDED_FINAL_READINESS_R4.json','validation/P02_UPSTREAM_STATE_REVALIDATION_R4.json','validation/P02_AUDIT_SECTIONS_1_274_EXHAUSTION_R4.csv','validation/P02_AUDIT_SECTIONS_1_274_EVIDENCE_LEDGER_R4.csv','validation/P02_PROMPT_275_323_TRACEABILITY.csv','validation/P02_STAGE_RUNTIME_IMPLEMENTATION_TRACEABILITY.csv','validation/P02_A4_COMPARISON_TRACEABILITY.csv','validation/P02_STAGE_TO_BUNDLE_TRACEABILITY.csv','validation/full_stage_graph_synthetic_integration.json','validation/FIXTURE_NON_SCIENTIFIC_RUNTIME_BUNDLE.zip','validation/synthetic_test_results.txt','execution_bundle_schema/README.md']
 for r in required: ck('exists:'+r,(ROOT/r).is_file())
 # Authority binding and scientific freeze
 b=yaml.safe_load((ROOT/'configs/phase_02/training_policy_authority_bindings.yaml').read_text()); vr=validate_training_policy_binding(b); ck('training_policy_binding',vr['status']=='PASS' and not vr['missing'] and not vr['blockers'],vr)
 a=b['augmentation_challenger']; cw=b['class_weighting']; pr=a['probability_resolution']
 ck('sr_primary_unaugmented',a['primary_reference_augmentation']=='NONE')
 ck('sr_grid_frozen',pr['type']=='VALIDATION_ONLY_DATASET_LEVEL_GRID_SEARCH' and [float(x) for x in pr['candidates']]==[.25,.5,.75] and pr['test_set_access']=='PROHIBITED' and pr['selection_frozen_before_test'] is True)
 ck('sr_segments_auto',a['segment_count_resolution']['requested_n_segments'] is None and a['segment_count_resolution']['type']=='BRAINCDECODE_PUBLIC_API_AUTO_N_SEGMENTS' and a['segment_count_resolution']['test_set_access']=='NONE')
 ck('sr_final_cells_policy',a['run_cell_count']==15 and a['diagnostic_only'] and not a['a4_eligible'] and not a['p03_primary_eligible'] and a['augmentation_specific_model_hyperparameter_retuning'] is False)
 ck('class_weight_algorithm',cw['policy']=='VALIDATION_SELECTED_UNIFORM_VS_BALANCED_WHEN_TRAIN_COUNTS_UNEQUAL' and cw['trigger']['type']=='EXACT_TRAIN_COUNT_EQUALITY_THEN_VALIDATION_POLICY_COMPARISON' and cw['balanced_formula']['type']=='SKLEARN_COMPUTE_CLASS_WEIGHT_BALANCED' and cw['selection']['test_set_access']=='PROHIBITED' and cw['selection']['tie_break']=='UNIFORM_NO_WEIGHT')
 ck('class_weight_scope_no_retrofit',cw['eligible_branch_rule']=='ANY_SELECTED_BRANCH_WITH_NATIVE_OR_VERIFIED_CLASS_WEIGHT_SUPPORT' and 'CLS-CSP-LDA' not in cw['native_supported_branches'] and 'RIE-MDM' not in cw['native_supported_branches'])
 freeze=yaml.safe_load((ROOT/'machine_readable/p02_planned_scientific_execution_freeze_R5.yaml').read_text()); ck('scientific_freeze_R5',freeze['freeze_id']=='P02-PLANNED-SCIENTIFIC-EXECUTION-FREEZE-R5' and freeze['preexecution_amendment_id']=='P02-PREEXEC-TRAINING-POLICY-AMENDMENT-R2' and freeze.get('owner_decisions_remaining',0)==0)
 ck('freeze_binding_sync',freeze['training_policy_resolution']['augmentation_challenger']==a and freeze['training_policy_resolution']['class_weighting']==cw)
 # cell plans
 full=yaml.safe_load((ROOT/'machine_readable/p02_full_ablation_planned_run_cells_R3.yaml').read_text())['rows']; ck('full_ablation_1896',len(full)==1896 and sum(x['ablation_id']=='A0' for x in full)==678 and sum(x['ablation_id']=='A4' for x in full)==1218 and len({x['planned_run_cell_id'] for x in full})==1896)
 ch=yaml.safe_load((ROOT/'machine_readable/p02_training_policy_challenger_run_cells_R2.yaml').read_text()); cr=ch['rows']; ck('diagnostic_cells_15',ch['cell_count']==15 and len(cr)==15 and len({x['planned_run_cell_id'] for x in cr})==15 and ch['official_A0_A4_total_remains']==1896 and all(x['diagnostic_only'] and not x['a4_eligible'] and not x['p03_primary_eligible'] and x['probability']=='DATASET_LEVEL_VALIDATION_SELECTED_FROM_FROZEN_GRID' and x['segment_count']=='BRAINCDECODE_AUTO_N_SEGMENTS' for x in cr))
 # runtime stage/branch routing
 ck('production_handlers_26',len(HANDLERS)==26 and all(callable(x) for x in HANDLERS.values()),sorted(HANDLERS))
 ck('branch_routing_16',len(FAMILY_STAGE)==16 and all(v in HANDLERS for v in FAMILY_STAGE.values()),FAMILY_STAGE)
 plan=yaml.safe_load((ROOT/'machine_readable/p02_notebook_stage_plan_R4.yaml').read_text()); ids=[str(x['stage']) for x in plan['stages']]; expected=['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','18U','19','20','21','22','23','24']; ck('stage_plan_26',ids==expected,ids); ck('stage_plan_R5',plan.get('scientific_execution_freeze')=='P02-PLANNED-SCIENTIFIC-EXECUTION-FREEZE-R5')
 # blocker/readiness/source audit
 br=json.loads((ROOT/'validation/P02_FREEZE_CRITICAL_BLOCKER_REGISTER_R4.json').read_text()); ck('blockers_zero',br['status']=='PASS' and br['freeze_critical_blocker_count']==0 and not br['freeze_critical_blockers'])
 rr=json.loads((ROOT/'validation/P02_TRAINING_POLICY_BLOCKER_RESOLUTION_REGISTER_R4.json').read_text()); ck('blocker_resolution_R4',rr['status']=='PASS' and rr['unresolved_after_repair']==0)
 se=json.loads((ROOT/'validation/P02_TRAINING_POLICY_SOURCE_EXHAUSTION_R2.json').read_text()); ck('source_exhaustion',se['status']=='PASS' and se['post_amendment_reaudit']=='PASS' and se['other_same_class_freeze_gaps_found']==0)
 sg=json.loads((ROOT/'validation/P02_OTHER_SAME_CLASS_FREEZE_GAP_AUDIT_R4.json').read_text()); ck('same_class_gap_scan',sg['status']=='PASS' and sg['other_same_class_freeze_gaps_found']==0)
 co=json.loads((ROOT/'validation/P02_TRAINING_POLICY_CODE_OWNERSHIP_AUDIT_R2.json').read_text()); ck('code_ownership',co['status']=='PASS' and co['unresolved_code_owned_scientific_bindings']==0 and co['test_set_used_for_resolution'] is False)
 rd=json.loads((ROOT/'validation/P02_EXPANDED_FINAL_READINESS_R4.json').read_text()); ck('readiness',rd['status']=='PASS' and rd['freeze_critical_blocker_count']==0 and all(v==0 for v in rd['zero_defect_invariants'].values()) and all(v=='YES' for v in rd['pre_pass_questions'].values()))
 up=json.loads((ROOT/'validation/P02_UPSTREAM_STATE_REVALIDATION_R4.json').read_text()); ck('upstream',up['status']=='PASS' and up['cumulative_verifier']=='40/40 PASS' and up['p01_verifier']=='24/24 PASS')
 # prompt coverage
 ex=list(csv.DictReader((ROOT/'validation/P02_AUDIT_SECTIONS_1_274_EXHAUSTION_R4.csv').open())); ck('sections_1_274',len(ex)==274 and all(x['audit_executed']=='YES' and 'BLOCKED' not in x['result'] and not x['blockers'] for x in ex),len(ex))
 e2=list(csv.DictReader((ROOT/'validation/P02_AUDIT_SECTIONS_1_274_EVIDENCE_LEDGER_R4.csv').open())); ck('evidence_1_274',len(e2)==274 and all(x['audit_executed']=='YES' for x in e2),len(e2))
 p323=list(csv.DictReader((ROOT/'validation/P02_PROMPT_275_323_TRACEABILITY.csv').open())); ck('sections_275_323',len(p323)==49 and {int(x['section']) for x in p323}==set(range(275,324)) and all(x['status']=='MAPPED_AND_REAUDITED' for x in p323),len(p323))
 # tests result
 txt=(ROOT/'validation/synthetic_test_results.txt').read_text(); ck('pytest_82','82 passed' in txt,txt[-200:])
 # fixture proves successful dynamic selector path and protocol-change artifacts
 fx=json.loads((ROOT/'validation/full_stage_graph_synthetic_integration.json').read_text()); ck('fixture_26',fx['status']=='PASS' and fx['stages']==26 and fx['runtime_checksums']['status']=='PASS' and fx['runtime_zip']['crc']=='PASS',fx)
 with zipfile.ZipFile(ROOT/'validation/FIXTURE_NON_SCIENTIFIC_RUNTIME_BUNDLE.zip') as z:
  names=z.namelist(); ck('fixture_zip_crc',z.testzip() is None); ck('fixture_zip_paths',all(not Path(n).is_absolute() and '..' not in Path(n).parts for n in names))
  reqz=['protocol_change_required/P02_PREEXECUTION_TRAINING_POLICY_AMENDMENT_R2.yaml','protocol_change_required/P02_FUTURE_PROTOCOL_BUILD_BOOK_SYNC_NOTE_R2.md','protocol_change_required/P02_TRAINING_POLICY_EXTERNAL_EVIDENCE_NOTE_R2.md','analysis_inputs/training_policy_sr_probability_selection.json','analysis_inputs/training_policy_sr_probability_calibration_candidates.jsonl','analysis_inputs/training_policy_challenger_completion.json']
  ck('fixture_dynamic_artifacts',all(any(n.endswith(x) for n in names) for x in reqz),reqz)
  sel=[n for n in names if n.endswith('analysis_inputs/training_policy_sr_probability_selection.json')][0]; sj=json.loads(z.read(sel)); ck('fixture_sr_selector_success',sj['status']=='PASS' and not sj['test_set_used'] and all(v.get('status')=='PASS' and not v.get('test_set_used') for v in sj['datasets'].values()),sj)
 # Hugging Face operational policy
 hf=yaml.safe_load((ROOT/'configs/phase_02/models/huggingface_assets.yaml').read_text()); cb=hf['assets']['SSL-CBRAMOD']; rv=hf['assets']['SSL-REVE']
 ck('huggingface_policy_id',hf['policy_id']=='P02-HF-CONDITIONAL-ASSET-POLICY-R1' and hf['token']['persistence']=='MEMORY_ONLY' and hf['token']['bundle_inclusion']=='PROHIBITED' and hf['token']['login_persistence']=='PROHIBITED_PASS_TOKEN_DIRECTLY_TO_HUB_CALLS')
 ck('huggingface_cbramod_governed',cb['eligibility']=='ELIGIBLE_CURRENT_P02' and cb['repo_id']=='braindecode/cbramod-pretrained' and cb['revision']=='584cdc415913739a05d84bf0c1cb3db397764507' and cb['checkpoint_sha256']=='a939ace9aa1e229f08391ad8bb2d197b507ae2c519a50addf087f0151b2df5c3')
 ck('huggingface_reve_science_gate_beats_auth',rv['eligibility'].startswith('BLOCKED_') and rv['gated'] is True and rv['download_policy']=='DO_NOT_DOWNLOAD_CURRENT_P02')
 hfsrc=(ROOT/'src/iharq/layer2_decoders/hf_assets.py').read_text(); ck('huggingface_direct_token_no_login','hf_hub_download' in hfsrc and 'token=token' in hfsrc and 'login(' not in hfsrc)
 hfn=nbformat.read(ROOT/'notebook/IHARQ_Phase_02_Complete_Execution_and_Analysis_R4_HF_R1.ipynb',as_version=4); hft='\n'.join(c.source for c in hfn.cells)
 ck('huggingface_notebook_hidden_secret','UserSecretsClient' in hft and 'getpass.getpass' in hft and 'HF_TOKEN' in hft and 'SESSION.clear_hf_token()' in hft and 'HF_TOKEN = None' in hft)
 ck('huggingface_notebook_unexecuted',all(c.get('execution_count') is None and not c.get('outputs',[]) for c in hfn.cells if c.cell_type=='code'))
 # notebook
 nb=nbformat.read(ROOT/'notebook/IHARQ_Phase_02_Complete_Execution_and_Analysis_R4.ipynb',as_version=4); nbformat.validate(nb); tags=[t for c in nb.cells for t in c.metadata.get('tags',[]) if t.startswith('governed-stage-')]; nbt='\n'.join(c.source for c in nb.cells)
 ck('notebook_stage_cells_26',len(tags)==26,len(tags)); ck('notebook_unexecuted',all(c.get('execution_count') is None and not c.get('outputs',[]) for c in nb.cells if c.cell_type=='code')); ck('notebook_unique_ids',all(c.get('id') for c in nb.cells) and len({c.id for c in nb.cells})==len(nb.cells)); ck('notebook_R5_R2',nb.metadata.get('iharq',{}).get('scientific_freeze')=='P02-PLANNED-SCIENTIFIC-EXECUTION-FREEZE-R5' and nb.metadata['iharq'].get('preexecution_amendment')=='P02-PREEXEC-TRAINING-POLICY-AMENDMENT-R2')
 ck('notebook_governance_dynamic','FUTURE PROTOCOL / BUILD-BOOK SYNCHRONIZATION REQUIRED' in nbt and 'P02-PREEXEC-TRAINING-POLICY-AMENDMENT-R2' in nbt and 'Test labels/scores may never choose' in nbt and 'validation evidence' in nbt.lower())
 ck('notebook_governance_ids','P02-PREEXEC-TRAINING-POLICY-AMENDMENT-R2' in nbt and 'P02-PLANNED-SCIENTIFIC-EXECUTION-FREEZE-R5' in nbt)
 ck('notebook_blocker_register_R4','P02_FREEZE_CRITICAL_BLOCKER_REGISTER_R4.json' in nbt and 'P02_FREEZE_CRITICAL_BLOCKER_REGISTER_R3.json' not in nbt)
 # protocol handoff dynamic
 ph=yaml.safe_load((ROOT/'machine_readable/p02_protocol_v1_handoff_template.yaml').read_text()); ck('protocol_sync_dynamic',ph['status']=='PREEXECUTION_RESOLUTION_ALGORITHMS_FROZEN_FUTURE_DOCUMENT_SYNC_REQUIRED' and ph['preexecution_amendment']['amendment_id']=='P02-PREEXEC-TRAINING-POLICY-AMENDMENT-R2' and 'NO_TEST_DRIVEN_RESELECTION_OR_RETUNING' in ph['preexecution_amendment']['rule'])
 # structured parse current package excluding history (history is archival and tested separately by checksum only)
 parse_fail=[]; counts={'json':0,'yaml':0,'csv':0}
 for p in ROOT.rglob('*'):
  if not p.is_file() or 'history' in p.parts: continue
  try:
   if p.suffix=='.json': json.loads(p.read_text());counts['json']+=1
   elif p.suffix in {'.yaml','.yml'}: yaml.safe_load(p.read_text());counts['yaml']+=1
   elif p.suffix=='.csv': list(csv.reader(p.open()));counts['csv']+=1
  except Exception as e: parse_fail.append((str(p.relative_to(ROOT)),repr(e)))
 ck('structured_parse',not parse_fail,parse_fail[:4])
 # security/current path/placeholder/stale policy scans
 ck('security_scan',scan_tree(ROOT)['status']=='PASS')
 allowed_suffix={'.py','.md','.json','.yaml','.yml','.csv','.toml','.ipynb'}; pathhits=[]; placeholders=[]; stale=[]; forbidden='/'+'mnt'+'/'+'data'+'/'
 for p in ROOT.rglob('*'):
  if not p.is_file() or p.suffix.lower() not in allowed_suffix or 'history' in p.parts or ('docs' in p.parts and 'audit_prompts' in p.parts): continue
  if p.name in {'validate_authoring_package.py','verify_frozen_package.py'}: continue
  t=p.read_text(errors='ignore')
  if forbidden in t:pathhits.append(str(p.relative_to(ROOT)))
  if re.search(r'(?mi)^\s*(?:#\s*)?(?:TODO|TBD|FIXME)\b|\{\{[^}]+\}\}',t):placeholders.append(str(p.relative_to(ROOT)))
  if 'tests' not in p.parts and any(x in t for x in ['NEVER_WEIGHT_P02_CURRENT_FROZEN_INPUTS','P02_FREEZE_CRITICAL_BLOCKER_REGISTER_R3.json','P02_PREEXECUTION_TRAINING_POLICY_AMENDMENT_R1.yaml']):stale.append(str(p.relative_to(ROOT)))
 ck('current_transient_paths_zero',not pathhits,pathhits[:5]); ck('current_placeholders_zero',not placeholders,placeholders[:5]); ck('current_fixed_policy_stale_refs_zero',not stale,stale[:5])
 trans=[str(p.relative_to(ROOT)) for p in ROOT.rglob('*') if p.is_file() and ('__pycache__' in p.parts or '.pytest_cache' in p.parts or p.suffix=='.pyc')]; ck('transient_files_zero',not trans,trans[:5])
 status='PASS' if all(x['status']=='PASS' for x in rows) else 'FAIL'; rep={'validation_id':'P02-AUTHORING-STATIC-VALIDATION-R5-HF-CONDITIONAL-ASSETS','status':status,'checks_total':len(rows),'checks_pass':sum(x['status']=='PASS' for x in rows),'checks_fail':sum(x['status']=='FAIL' for x in rows),'structured_counts':counts,'rows':rows,'freeze_critical_blockers':sum(x['status']=='FAIL' for x in rows)}; (ROOT/'validation/static_authoring_validation.json').write_text(json.dumps(rep,indent=2)+'\n'); print(json.dumps({'status':status,'pass':rep['checks_pass'],'fail':rep['checks_fail'],'total':rep['checks_total']},indent=2)); return 0 if status=='PASS' else 1
if __name__=='__main__': raise SystemExit(main())
