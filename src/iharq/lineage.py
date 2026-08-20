from __future__ import annotations
from collections import defaultdict,deque

def missing_sources(records:list[dict])->dict[str,list[str]]:
    ids={r.get("record_id") for r in records}
    return {r["record_id"]:[x for x in r.get("source_ids",[]) if x not in ids] for r in records if any(x not in ids for x in r.get("source_ids",[]))}
def descendants(records:list[dict],roots:set[str])->set[str]:
    child=defaultdict(set)
    for r in records:
        for s in r.get("source_ids",[]): child[s].add(r["record_id"])
    q=deque(roots); seen=set(roots)
    while q:
        for c in child[q.popleft()]:
            if c not in seen: seen.add(c); q.append(c)
    return seen-roots
