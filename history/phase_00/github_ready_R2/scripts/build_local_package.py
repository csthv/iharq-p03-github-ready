from __future__ import annotations
import argparse,hashlib,json,zipfile
from pathlib import Path
ROOT=Path(__file__).parents[1]
TRANSIENT={'.git','.venv','venv','.pytest_cache','__pycache__','.mypy_cache','.ruff_cache','htmlcov','build','dist'}
def intended_files():
 for p in sorted(ROOT.rglob('*')):
  if not p.is_file() or any(x in TRANSIENT for x in p.parts) or p.suffix in {'.pyc','.pyo'}:continue
  yield p
ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args();out=Path(args.output).resolve();out.parent.mkdir(parents=True,exist_ok=True)
files=[p for p in intended_files() if p.resolve()!=out]
with zipfile.ZipFile(out,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for p in files:z.write(p,p.relative_to(ROOT).as_posix())
obj={'archive':out.name,'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'file_count':len(files),'root':'REPOSITORY_ROOT_NO_WRAPPER'}
print(json.dumps(obj,indent=2))
