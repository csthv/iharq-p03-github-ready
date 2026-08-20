from pathlib import Path
import json, yaml, importlib
ROOT=Path(__file__).parents[1]

def test_current_state_is_p02_closed_p03_not_started():
 d=json.loads((ROOT/'CURRENT_PROJECT_STATUS.json').read_text())
 assert d['completed_phase_scopes']==['P00','P01','P02']
 assert d['p02_execution_complete'] is True and d['p03_execution_started'] is False
 assert d['scientific_blockers']==d['documentary_blockers']==d['major_issues']==0

def test_l1_l2_l3_import_boundaries_are_nonexecuting():
 for mod in ['iharq.layer1_data_protocol','iharq.layer2_decoders','iharq.layer3_calibration_uncertainty']:
  m=importlib.import_module(mod); assert m.SCIENTIFIC_EXECUTION is False

def test_p02_to_p03_readiness_is_explicit_and_unblocked():
 h=yaml.safe_load((ROOT/'phase_handoff.yaml').read_text())['phase_handoff']
 assert h['consumer_phase']=='P03' and h['blockers']==[]
 assert h['status']=='READY_WITH_EXPLICIT_NONBLOCKING_LIMITATIONS'
 assert (ROOT/'artifacts/handoffs/phase_02_to_phase_03/downstream_readiness.yaml').is_file()
 assert (ROOT/'contracts/phases/p03/input_contract.yaml').is_file()

def test_dual_credential_contract_is_preserved():
 t=(ROOT/'artifacts/handoffs/phase_02_to_phase_03/external_artifact_retrieval.yaml').read_text()
 assert 'IHARQ_HF_TOKEN_PRE_P02' in t and 'IHARQ_HF_TOKEN_P02' in t
 assert 'bc14961e14f2e48690e55df3577014275f9cbf30' in t

def test_final_lifecycle_authorities_are_available():
 for p in [
  'final_state/through_p02/authorities/protocol_v1/IHARQ_Protocol_v1_0_Final_Through_Phase_02_R1.md',
  'final_state/through_p02/analysis/IHARQ_Cumulative_Phase_Evidence_Results_and_Interpretation_Through_P02_Final_R1.md',
  'final_state/through_p02/layer0/Layer_0_Claim_Governance_Through_P02.md',
  'final_state/through_p02/evidence_map/IHARQ_Cumulative_Evidence_Map_Through_P02.md',
  'final_state/through_p02/layer10/Layer_10_Artifact_Package_Through_P02.md']:
  assert (ROOT/p).is_file(),p

def test_promoted_layer2_functional_files_match_preserved_source():
 d=json.loads((ROOT/'artifacts/cumulative_state/p02_final_merge_R2/root_layer2_promotion_manifest.json').read_text())
 assert d['scientific_logic_changed'] is False
 assert d['functional_module_files_byte_identical_except_init_compatibility_shim'] is True
