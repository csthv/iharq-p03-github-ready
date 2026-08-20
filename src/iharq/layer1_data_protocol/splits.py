from __future__ import annotations
from typing import Any
from collections import defaultdict
import hashlib, math
from .models import RawRecording
from .records import make_record

def unit_key(r:RawRecording,keys:list[str])->str: return "|".join(str(getattr(r,key)) for key in keys)

def _largest_remainder_counts(n:int,roles:list[str],ratios:dict[str,float],tie_order:list[str])->dict[str,int]:
    quotas={r:n*float(ratios[r]) for r in roles}; counts={r:int(math.floor(quotas[r])) for r in roles}; remaining=n-sum(counts.values())
    rank={r:i for i,r in enumerate(tie_order)}
    order=sorted(roles,key=lambda r:(-(quotas[r]-counts[r]),rank.get(r,len(rank)),r))
    for r in order[:remaining]: counts[r]+=1
    if n>=len(roles):
        for empty in [r for r in roles if counts[r]==0]:
            donor=max((r for r in roles if counts[r]>1),key=lambda r:(counts[r],-rank.get(r,999)),default=None)
            if donor is None: raise ValueError("cannot guarantee one group per role")
            counts[donor]-=1; counts[empty]+=1
    return counts

def construct(recordings:list[RawRecording],profile:dict[str,Any],config_id:str,source_ids:list[str]|None=None)->tuple[dict[str,str],dict[str,Any]]:
    roles=list(profile.get("roles",[])); ratios={k:float(v) for k,v in dict(profile.get("ratios") or {}).items()}; keys=list(profile.get("group_keys",[])); seed=profile.get("seed")
    if not roles or set(roles)!=set(ratios) or not keys or seed is None: raise ValueError("split freeze incomplete")
    if abs(sum(ratios.values())-1.0)>1e-12: raise ValueError("split ratios must sum to one")
    tie=list(profile.get("tie_break_order",["test","validation","calibration","train"])); by_dataset=defaultdict(set)
    for r in recordings: by_dataset[r.dataset_id].add(unit_key(r,keys))
    assignment={}; observed_counts={}
    for dataset,units_set in sorted(by_dataset.items()):
        units=sorted(units_set,key=lambda u:hashlib.sha256(f"{seed}|{dataset}|{u}".encode()).hexdigest())
        counts=_largest_remainder_counts(len(units),roles,ratios,tie); observed_counts[dataset]=counts
        pos=0
        for role in roles:
            for u in units[pos:pos+counts[role]]: assignment[u]=role
            pos+=counts[role]
        expected=(profile.get("expected_group_counts") or {}).get(dataset)
        if expected and {k:int(v) for k,v in expected.items()}!=counts: raise ValueError(f"split counts differ from freeze for {dataset}: {counts}")
    payload={"split_id":f"split:{config_id[:16]}","protocol_id":str(profile["protocol_id"]),"seed":int(seed),"grouping_keys":keys,"roles":assignment,
      "role_counts_by_dataset":observed_counts,"allocation_algorithm":profile.get("allocation_algorithm"),"source_event_ids":[],"budget_ids":[]}
    return assignment,make_record("SplitRecord",payload,config_id,list(source_ids or []),lifecycle_status="VALIDATED")

def recording_role(recording:RawRecording,assignment:dict[str,str],keys:list[str])->str: return assignment[unit_key(recording,keys)]

def validate_disjointness(recordings:list[RawRecording],assignment:dict[str,str],keys:list[str])->dict[str,Any]:
    by_role=defaultdict(set)
    for r in recordings: by_role[recording_role(r,assignment,keys)].add(unit_key(r,keys))
    intersections=[]; roles=sorted(by_role)
    for i,a in enumerate(roles):
        for b in roles[i+1:]:
            overlap=sorted(by_role[a]&by_role[b])
            if overlap: intersections.append({"left":a,"right":b,"units":overlap})
    return {"status":"PASS" if not intersections else "FAIL","intersections":intersections,"counts":{k:len(v) for k,v in by_role.items()}}

def validate_role_coverage(assignment:dict[str,str],required_roles:list[str])->dict[str,Any]:
    counts={role:sum(1 for value in assignment.values() if value==role) for role in required_roles}; missing=[r for r,c in counts.items() if c==0]
    return {"status":"PASS" if not missing else "FAIL","counts":counts,"missing_roles":missing}
