from __future__ import annotations
from pathlib import Path
from copy import deepcopy
from typing import Any
import yaml
from .models import PhaseConfig
from .canonical import semantic_hash
from .errors import ConfigError

def load_yaml(path:str|Path)->dict[str,Any]:
    data=yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data,dict): raise ConfigError("configuration root must be object")
    return data

def deep_merge(a:dict,b:dict)->dict:
    out=deepcopy(a)
    for k,v in b.items(): out[k]=deep_merge(out[k],v) if isinstance(v,dict) and isinstance(out.get(k),dict) else deepcopy(v)
    return out

def validate_phase_config(path:str|Path)->PhaseConfig:
    return PhaseConfig.model_validate(load_yaml(path))

def resolved_snapshot(paths:list[str|Path])->tuple[dict,str]:
    result={}
    for p in paths: result=deep_merge(result,load_yaml(p))
    return result,semantic_hash(result)
