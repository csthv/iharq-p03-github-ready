from __future__ import annotations
from pathlib import Path
import hashlib
TRANSIENT_PARTS={'.git','.venv','.pytest_cache','__pycache__','.mypy_cache','.ruff_cache','htmlcov','build','dist'}
TRANSIENT_SUFFIXES={'.pyc','.pyo','.coverage'}
def file_digest(path:str|Path)->str:
    h=hashlib.sha256();p=Path(path)
    with p.open('rb') as f:
        for c in iter(lambda:f.read(1024*1024),b''):h.update(c)
    return h.hexdigest()
def is_transient_path(rel:str)->bool:
    p=Path(rel)
    if any(part in TRANSIENT_PARTS for part in p.parts):return True
    if rel.endswith(tuple(TRANSIENT_SUFFIXES)):return True
    return False
def build_file_manifest(root:str|Path,exclude:set[str]|None=None,exclude_prefixes:tuple[str,...]=()):
    root=Path(root);exclude=exclude or set();rows=[]
    for p in sorted(root.rglob('*')):
        if not p.is_file():continue
        rel=p.relative_to(root).as_posix()
        if rel in exclude or is_transient_path(rel) or any(rel.startswith(prefix) for prefix in exclude_prefixes):continue
        rows.append({'path':rel,'sha256':file_digest(p),'bytes':p.stat().st_size})
    return rows
