from __future__ import annotations
from collections import defaultdict
from typing import Any

def audit(recordings,assignment,split_keys,window_index,fit_source_ids,budget_rows)->dict[str,Any]:
    issues=[]; role_units=defaultdict(set)
    for r in recordings:
        unit="|".join(str(getattr(r,k)) for k in split_keys); role_units[assignment[unit]].add(unit)
    roles=sorted(role_units)
    for i,a in enumerate(roles):
        for b in roles[i+1:]:
            overlap=role_units[a]&role_units[b]
            if overlap: issues.append({"code":"P01_SPLIT_OVERLAP","left":a,"right":b,"units":sorted(overlap)})
    by_hash=defaultdict(list)
    for row in window_index: by_hash[row["sample_hash"]].append(row)
    for h,rows in by_hash.items():
        if len({r["role"] for r in rows})>1: issues.append({"code":"P01_DUPLICATE_SAMPLE","sample_hash":h,"records":[r["window_record_id"] for r in rows]})
    overlap_roles=defaultdict(set)
    for row in window_index: overlap_roles[row["event_id"]].add(row["role"])
    for group,rs in overlap_roles.items():
        if len(rs)>1: issues.append({"code":"P01_OVERLAP_GROUP_LEAKAGE","group":group,"roles":sorted(rs)})
    evaluation_units=set().union(*(role_units[r] for r in role_units if r in {"validation","test"}))
    if evaluation_units & set(fit_source_ids): issues.append({"code":"P01_PREPROCESSING_FIT_LEAKAGE","units":sorted(evaluation_units & set(fit_source_ids))})
    test_events={row["event_id"] for row in window_index if row["role"]=="test"}
    for b in budget_rows:
        overlap=test_events & set(b.get("event_ids",[]))
        if overlap: issues.append({"code":"P01_BUDGET_TEST_CONTAMINATION","budget_id":b["budget_id"],"event_ids":sorted(overlap)})
    return {"status":"PASS" if not issues else "FAIL","issues":issues,"checks":["GROUP_DISJOINTNESS","DUPLICATE_SAMPLE","OVERLAP_GROUP","FIT_SCOPE","BUDGET_TEST_CONTAMINATION"]}
