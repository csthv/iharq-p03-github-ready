from __future__ import annotations
from datetime import date
from typing import Any
from iharq.ids import make_id
from iharq.canonical import semantic_hash

def hashable(value:Any)->Any:
    if isinstance(value,float):
        return format(value,'.17g')
    if hasattr(value,'item') and callable(getattr(value,'item')):
        try:
            return hashable(value.item())
        except Exception:
            return str(value)
    if isinstance(value,dict):
        return {str(k):hashable(v) for k,v in value.items()}
    if isinstance(value,(list,tuple,set)):
        return [hashable(v) for v in value]
    return value

def make_record(record_type:str,payload:dict[str,Any],config_id:str,source_ids:list[str],*,evidence_mode:str="IMPLEMENTATION",lifecycle_status:str="CREATED",limitation_tags:list[str]|None=None,evidence_role:str="PRIMARY",ablation_id:str|None=None,day:date|None=None)->dict[str,Any]:
    body={"record_type":record_type,"payload":payload,"config_id":config_id,"source_ids":sorted(set(source_ids)),"phase_id":"P01"}
    hash_body=hashable(body)
    return {
        "record_id":make_id(record_type.upper(),hash_body,day=day),
        "record_type":record_type,
        "schema_version":"1.0-p01",
        "authority_status":"REGISTRY_REFERENCED",
        "owner_layer":"L1",
        "phase_id":"P01",
        "config_id":config_id,
        "source_ids":sorted(set(source_ids)),
        "evidence_mode":evidence_mode,
        "limitation_tags":sorted(set(limitation_tags or ["PUBLIC_EEG_ONLY","NON_CLINICAL","NO_DEPLOYMENT_CLAIM"])),
        "lifecycle_status":lifecycle_status,
        "fixture":False,
        "fixture_tags":[],
        "evidence_role":evidence_role,
        "payload":payload,
        "ablation_id":ablation_id,
        "semantic_hash":semantic_hash(hash_body),
    }
