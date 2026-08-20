"""Historical P02→P03 regression checks retained after P03 closure.

Current lifecycle assertions live in ``test_p03_to_p04_handoff.py``. These
checks ensure the predecessor handoff and its access/provenance boundaries were
not lost during cumulative promotion.
"""
from pathlib import Path
import yaml
ROOT=Path(__file__).parents[1]

def test_historical_p02_to_p03_handoff_is_preserved():
 p=ROOT/'history/p03_merge_preimages_R1/phase_handoff.yaml'
 h=yaml.safe_load(p.read_text())['phase_handoff']
 assert h['producer_phase']=='P02' and h['consumer_phase']=='P03'
 assert h['blockers']==[]
 assert (ROOT/'artifacts/handoffs/phase_02_to_phase_03/downstream_readiness.yaml').is_file()

def test_historical_dual_credential_contract_is_preserved():
 t=(ROOT/'artifacts/handoffs/phase_02_to_phase_03/external_artifact_retrieval.yaml').read_text()
 assert 'IHARQ_HF_TOKEN_PRE_P02' in t and 'IHARQ_HF_TOKEN_P02' in t
 assert 'bc14961e14f2e48690e55df3577014275f9cbf30' in t
