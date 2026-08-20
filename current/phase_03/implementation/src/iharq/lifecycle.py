from __future__ import annotations
ALLOWED={
 "CREATED":{"VALIDATED","BLOCKED","INVALIDATED"},"VALIDATED":{"ACCEPTED","DIAGNOSTIC_ONLY","BLOCKED","INVALIDATED"},
 "ACCEPTED":{"SUPERSEDED","INVALIDATED"},"DIAGNOSTIC_ONLY":{"SUPERSEDED","INVALIDATED"},"BLOCKED":{"VALIDATED","INVALIDATED"},
 "SUPERSEDED":set(),"INVALIDATED":set(),
}
def transition_allowed(old:str,new:str)->bool: return new in ALLOWED.get(old,set())
def reusable_for_acceptance(status:str)->bool: return status in {"VALIDATED","ACCEPTED"}
