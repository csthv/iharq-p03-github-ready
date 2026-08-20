from __future__ import annotations
from typing import Any
from .models import RawRecording
from .records import make_record

def build_label_map(dataset_id:str,recordings:list[RawRecording],profile:dict[str,Any],config_id:str,dataset_record_id:str|None=None)->tuple[dict[str,Any],dict[str,Any]]:
    mapping={str(k):str(v) for k,v in dict(profile.get("mapping",{})).items()}; excluded=set(str(x) for x in profile.get("excluded_labels",[]))
    observed=sorted({str(e.original_label) for r in recordings for e in r.events}); unknown=[x for x in observed if x not in mapping and x not in excluded]
    expected=set(str(x) for x in profile.get("expected_event_codes",[])); inventory_extra=sorted(set(observed)-expected) if expected else []
    if inventory_extra: unknown=sorted(set(unknown)|set(inventory_extra))
    payload={"label_map_id":f"{dataset_id}:label-map:{config_id[:12]}","dataset_id":dataset_id,"mapping":mapping,"mapping_metadata":profile.get("mapping_metadata",{}),
      "original_labels":observed,"normalized_labels":sorted(set(mapping.values())),"excluded_labels":sorted(excluded),"unknown_labels":unknown,
      "proxy_limitations":list(profile.get("proxy_limitations",["PROXY_INTENT_ONLY"])),"round_trip_required":bool(profile.get("round_trip_required",True)),
      "expected_event_codes":sorted(expected),"unknown_event_behavior":profile.get("unknown_event_behavior","BLOCK_SOURCE_EVENT_WITH_UNKNOWN_LABEL")}
    status="BLOCKED" if unknown else "VALIDATED"
    return make_record("LabelMapRecord",payload,config_id,[dataset_record_id] if dataset_record_id else [],lifecycle_status=status),{"unknown":unknown,"excluded":sorted(excluded),"observed":observed,"status":status}

def map_event_label(label:str,label_record:dict[str,Any])->str|None:
    p=label_record["payload"]; key=str(label)
    if key in set(p["excluded_labels"]): return None
    return p["mapping"].get(key)
