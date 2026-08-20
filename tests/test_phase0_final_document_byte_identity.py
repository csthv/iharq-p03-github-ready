from pathlib import Path
import hashlib,json,yaml
ROOT=Path(__file__).parents[1]
def test_final_document_hashes_and_snapshot_bodies():
    m=yaml.safe_load((ROOT/'manifests/phase_00/final_document_set_manifest.yaml').read_text())
    assert len(m['documents'])==18
    for d in m['documents']:
        p=ROOT/d['path']; assert p.exists(); assert hashlib.sha256(p.read_bytes()).hexdigest()==d['sha256']
    a=json.loads((ROOT/'reports/phase_00_finalization/document_independence_and_selection_audit.json').read_text())
    assert a['snapshots_body_match'] and a['independent_markdown_status']=='PASS'
