from pathlib import Path
import hashlib,yaml
ROOT=Path(__file__).parents[1]
def test_required_final_document_set():
 m=yaml.safe_load((ROOT/'manifests/phase_00/final_document_set_manifest.yaml').read_text());assert m['required_count']==m['present_count']==18;assert len(m['documents'])==18
 for d in m['documents']:
  p=ROOT/d['path'];assert p.exists();assert hashlib.sha256(p.read_bytes()).hexdigest()==d['sha256']
def test_distribution_snapshot_bodies_match():
 import json
 a=json.loads((ROOT/'reports/phase_00_finalization/document_independence_and_selection_audit.json').read_text());assert a['snapshots_body_match'];assert a['independent_markdown_status']=='PASS'
