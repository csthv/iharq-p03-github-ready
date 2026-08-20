from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any
import numpy as np

@dataclass(frozen=True)
class Event:
    event_id: str
    start_sample: int
    stop_sample: int
    original_label: str
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass
class RawRecording:
    dataset_id: str
    subject_id: str
    session_id: str
    run_id: str
    source_file: str
    sampling_hz: float
    channel_names: list[str]
    signal: np.ndarray
    events: list[Event]
    source_metadata: dict[str, Any] = field(default_factory=dict)

@dataclass(frozen=True)
class SourceProfile:
    dataset_id: str
    aliases: list[str]
    authority_status: str
    scientific_role: str
    active_for_run: bool
    exact_revision: str
    citation: str
    license: str
    access_method: str
    official_reference: str
    expected_checksum: str
    adapter: str
    cache_path: str
    redistribution_allowed: str
    adapter_options: dict[str, Any]
    published_checksum: str = "NO_SINGLE_PROVIDER_WIDE_PUBLISHED_SHA256"
    checksum_policy: str = "COMPUTE_AND_FREEZE_PER_RUN"
    source_native_preprocessing: list[str] = field(default_factory=list)
    limitations: list[str] = field(default_factory=list)

@dataclass
class StageResult:
    stage: str
    status: str
    outputs: list[str] = field(default_factory=list)
    observations: dict[str, Any] = field(default_factory=dict)
    blockers: list[dict[str, Any]] = field(default_factory=list)
