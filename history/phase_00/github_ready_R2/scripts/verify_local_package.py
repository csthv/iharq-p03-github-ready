from __future__ import annotations
import argparse,hashlib,json,tempfile,zipfile,shutil
from pathlib import Path,PurePosixPath
ap=argparse.ArgumentParser();ap.add_argument('--archive',required=True);args=ap.parse_args();archive=Path(args.archive)
problems=[]
with zipfile.ZipFile(archive) as z:
 bad=z.testzip()
 if bad:problems.append(f'corrupt entry {bad}')
 names=[n for n in z.namelist() if not n.endswith('/')]
 required={'README.md','pyproject.toml','requirements-lock.txt','src/iharq/cli.py','docs/index.md','manifests/publication_manifest.json'}
 missing=sorted(required-set(names))
 if missing:problems.append(f'missing root files: {missing}')
 if any(n.startswith('IHARQ_Phase_0_GitHub_Scholarship_Ready_R2/') for n in names):problems.append('extra wrapper directory present')
 for n in names:
  pp=PurePosixPath(n)
  if pp.is_absolute() or '..' in pp.parts:problems.append(f'unsafe path: {n}')
  if '__pycache__' in pp.parts or '.pytest_cache' in pp.parts or '.venv' in pp.parts or n.endswith(('.pyc','.pyo')):problems.append(f'transient file: {n}')
result={'archive':archive.name,'sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'entries':len(names),'root_layout':'DIRECT_REPOSITORY_ROOT','status':'PASS' if not problems else 'FAIL','problems':problems}
print(json.dumps(result,indent=2));raise SystemExit(0 if not problems else 1)
