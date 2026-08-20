from __future__ import annotations
from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field

class RecordEnvelope(BaseModel):
    model_config=ConfigDict(extra="forbid", strict=True)
    record_id: str
    record_type: str
    schema_version: str
    authority_status: str
    owner_layer: str
    phase_id: str
    config_id: str
    source_ids: list[str]
    evidence_mode: Literal["FOUNDATION","IMPLEMENTATION","CONFORMANCE","VALIDATION","REPRODUCIBILITY_READINESS"]
    limitation_tags: list[str]
    lifecycle_status: Literal["CREATED","VALIDATED","ACCEPTED","DIAGNOSTIC_ONLY","BLOCKED","SUPERSEDED","INVALIDATED"]
    fixture: bool
    fixture_tags: list[str]
    evidence_role: Literal["PRIMARY","DERIVED","GOVERNANCE","RENDERING","PACKAGING"]
    payload: dict[str,Any]
    ablation_id: str|None=None

class PhaseConfig(BaseModel):
    model_config=ConfigDict(extra="forbid", strict=True)
    phase_id: Literal["P00"]
    official_name: str
    protocol_timing_mode: Literal["C_ADMINISTRATIVE_FOUNDATION"]
    execution_mode: Literal["real","smoke","dry-run"]
    participating_layers: list[str]
    ablation_bindings: list[str]
    closure_profile: list[str]
    no_empirical_execution: Literal[True]
