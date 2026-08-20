from pathlib import Path
import yaml
ROOT=Path(__file__).parents[1]
def test_all_sources_manifested():
 s=yaml.safe_load((ROOT/'manifests/authority_manifest.yaml').read_text())['sources'];assert len(s)>=12;assert all(x['sha256'] for x in s)
def test_llm_decisions():
 d=yaml.safe_load((ROOT/'docs/decisions/phase0_llm_decisions_R1.yaml').read_text())['decisions'];assert {x['id'] for x in d}=={'OD-001','OD-002','OD-004','OD-016','OD-018','OD-019','OD-022'};assert all(x['status'].startswith('LLM_DECISION_ACCEPTED') for x in d)
