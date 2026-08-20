from __future__ import annotations
import hashlib, json, math
from typing import Any
from .errors import CanonicalizationError
SAFE_INT_MAX = 9007199254740991

def _utf16_key(s: str) -> bytes:
    try: return s.encode("utf-16-be", "strict")
    except UnicodeEncodeError as exc: raise CanonicalizationError("invalid Unicode surrogate") from exc

def _validate(v: Any) -> None:
    if v is None or isinstance(v,(str,bool)): return
    if isinstance(v,int) and not isinstance(v,bool):
        if abs(v)>SAFE_INT_MAX: raise CanonicalizationError("integer outside I-JSON safe range; encode as governed string")
        return
    if isinstance(v,float):
        if not math.isfinite(v): raise CanonicalizationError("NaN/Infinity forbidden")
        if v == 0.0 and math.copysign(1.0,v)<0: raise CanonicalizationError("negative zero forbidden")
        raise CanonicalizationError("floating values forbidden in hash-bearing profile; use governed decimal string")
    if isinstance(v,list):
        for x in v: _validate(x)
        return
    if isinstance(v,dict):
        for k,x in v.items():
            if not isinstance(k,str): raise CanonicalizationError("object keys must be strings")
            _utf16_key(k); _validate(x)
        return
    raise CanonicalizationError(f"unsupported type {type(v).__name__}")

def _string(s: str) -> str:
    _utf16_key(s)
    return json.dumps(s, ensure_ascii=False, separators=(",",":"))

def _emit(v: Any) -> str:
    if v is None: return "null"
    if v is True: return "true"
    if v is False: return "false"
    if isinstance(v,str): return _string(v)
    if isinstance(v,int): return str(v)
    if isinstance(v,list): return "["+",".join(_emit(x) for x in v)+"]"
    if isinstance(v,dict):
        return "{"+",".join(_string(k)+":"+_emit(v[k]) for k in sorted(v,key=_utf16_key))+"}"
    raise CanonicalizationError("unvalidated value")

def canonical_bytes(v: Any) -> bytes:
    _validate(v)
    return _emit(v).encode("utf-8")

def semantic_hash(v: Any) -> str:
    return hashlib.sha256(canonical_bytes(v)).hexdigest()
