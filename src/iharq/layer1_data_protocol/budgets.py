from __future__ import annotations
from collections import defaultdict
from typing import Any
import hashlib

def allocate(event_rows:list[dict[str,Any]],profile:dict[str,Any])->tuple[list[dict[str,Any]],dict[str,Any]]:
    budgets=[int(x) for x in profile.get("budgets_per_class") or []]; seed=profile.get("seed"); source_role=str(profile.get("source_role") or "calibration")
    classes=[str(x) for x in profile.get("normalized_classes",["left_hand","right_hand"])]
    if not budgets or seed is None: raise ValueError("budget freeze incomplete")
    grouped=defaultdict(list)
    for row in event_rows:
        if row["role"]==source_role and row.get("normalized_label") in classes: grouped[(row["dataset_id"],row["normalized_label"])].append(row)
    allocations=[]; insufficient=[]
    for dataset in sorted({k[0] for k in grouped}):
        for budget in budgets:
            bid=f"{dataset}:budget-{budget}-seed-{seed}"; selected=[]
            for label in classes:
                rows=grouped.get((dataset,label),[])
                ordered=sorted(rows,key=lambda r:hashlib.sha256(f"{seed}|{dataset}|{r['subject_id']}|{r['session_id']}|{r['run_id']}|{r['event_id']}".encode()).hexdigest())
                if len(ordered)<budget: insufficient.append({"dataset_id":dataset,"budget_id":bid,"label":label,"available":len(ordered),"required":budget})
                selected.extend(r["event_id"] for r in ordered[:budget])
            allocations.append({"dataset_id":dataset,"budget_id":bid,"budget_per_class":budget,"source_role":source_role,"event_ids":sorted(selected),"nested_prefix":True})
    return allocations,{"status":"PASS" if not insufficient else "DIAGNOSTIC_ONLY","insufficient":insufficient,"allocation_count":len(allocations)}
