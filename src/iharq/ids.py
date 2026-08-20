from __future__ import annotations
from datetime import date
import re
from typing import Any
from .canonical import semantic_hash
ID_RE=re.compile(r"^IHARQ-(?P<kind>[A-Z][A-Z0-9_]*)-(?P<day>\d{8})-(?P<digest>[0-9a-f]{16})$")
def make_id(kind:str,payload:Any,day:date|None=None)->str:
    k=kind.upper().replace("-","_")
    if not re.fullmatch(r"[A-Z][A-Z0-9_]*",k): raise ValueError("invalid kind")
    d=day or date.today()
    return f"IHARQ-{k}-{d:%Y%m%d}-{semantic_hash(payload)[:16]}"
def validate_id(value:str,kind:str|None=None)->bool:
    m=ID_RE.fullmatch(value)
    return bool(m and (kind is None or m.group('kind')==kind.upper().replace('-','_')))
