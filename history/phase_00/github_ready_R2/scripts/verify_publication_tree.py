from pathlib import Path
import hashlib, json, yaml, sys
ROOT=Path(__file__).parents[1]
problems=[]
# core directories
for d in ['src/iharq','schemas','configs','contracts','fixtures/valid','fixtures/invalid','docs/phase_00/final_documents','docs/authorities/current']:
    if not (ROOT/d).exists(): problems.append('missing:'+d)
# final docs and hashes
m=yaml.safe_load((ROOT/'manifests/phase_00/final_document_set_manifest.yaml').read_text())
if len(m.get('documents',[]))!=18: problems.append('final-document-count')
for row in m.get('documents',[]):
    p=ROOT/row['path']
    if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=row['sha256']: problems.append('final-document:'+row['path'])
# no GitHub workflow / no uv lock
if (ROOT/'.github/workflows').exists(): problems.append('github-workflow-present')
if (ROOT/'uv.lock').exists(): problems.append('uv-lock-present')
# publication manifest exactness (self-excluding)
pm=ROOT/'manifests/publication_manifest.json'
if pm.is_file():
    data=json.loads(pm.read_text()); listed={x['path']:x for x in data['files']}
    excluded=set(data.get('excluded_paths',[])); actual={p.relative_to(ROOT).as_posix():p for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts and '__pycache__' not in p.parts and '.pytest_cache' not in p.parts and p.suffix!='.pyc' and p.relative_to(ROOT).as_posix() not in excluded}
    if set(listed)!=set(actual): problems.append('publication-manifest-path-set')
    for rel,p in actual.items():
        if listed[rel]['sha256']!=hashlib.sha256(p.read_bytes()).hexdigest() or listed[rel]['bytes']!=p.stat().st_size: problems.append('publication-manifest-hash:'+rel)
print(json.dumps({'status':'PASS' if not problems else 'FAIL','problems':problems},indent=2));sys.exit(0 if not problems else 1)
