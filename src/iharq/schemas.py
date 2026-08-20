from __future__ import annotations
from functools import lru_cache
from pathlib import Path
import json
from jsonschema import Draft202012Validator
from .errors import SchemaError

@lru_cache(maxsize=None)
def _load_schema_cached(record_type:str,root_str:str):
    p=Path(root_str)/(record_type+".schema.json")
    if not p.exists(): raise SchemaError(f"missing schema for {record_type}")
    s=json.loads(p.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(s)
    return s

def load_schema(record_type:str,root:str|Path="schemas/records"):
    return _load_schema_cached(record_type,str(Path(root).resolve()))

def errors(instance,schema):
    return sorted(Draft202012Validator(schema).iter_errors(instance),key=lambda e:list(e.path))
