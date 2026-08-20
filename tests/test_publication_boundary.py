from pathlib import Path
from iharq.gates import evaluate
ROOT=Path(__file__).parents[1]
def test_no_github_ci_workflow_or_gate():
    assert not (ROOT/'.github/workflows').exists()
    rows=evaluate({k:True for k in ['authority_baseline','paths','schemas','configs','identity_hash_seed','valid_fixtures','invalid_fixtures','validators','ablations','cross_layer_traceability','policy_update','frozen_evaluation','layer0_foundation','layer10_foundation','manifests','implementation_readiness','local_reproduction']})
    assert rows[16]['topic']=='local_reproduction' and rows[16]['status']=='PASS'
    assert rows[17]['topic']=='governed_publication_and_closure' and rows[17]['status'].startswith('READY_TO_PASS')
def test_uv_lock_omitted_and_exact_lock_present():
    assert not (ROOT/'uv.lock').exists(); assert (ROOT/'requirements-lock.txt').is_file(); assert (ROOT/'requirements-lock.sha256').is_file()
def test_public_docs_present():
    for p in ['README.md','docs/index.md','docs/phase_00/overview.md','provenance/ROLLBACK.md','publication/file_selection_manifest.csv']:
        assert (ROOT/p).is_file(),p
