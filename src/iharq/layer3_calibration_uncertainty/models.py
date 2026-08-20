"""Core value objects for execution, stage receipts, and immutable context."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import StrEnum
from pathlib import Path
from typing import Any


class StageStatus(StrEnum):
    NOT_STARTED = "NOT_STARTED"
    IN_PROGRESS = "IN_PROGRESS"
    PARTIAL = "PARTIAL"
    COMPLETE = "COMPLETE"
    FAILED = "FAILED"
    RETRY = "RETRY"
    RESUMED = "RESUMED"
    SUPERSEDED = "SUPERSEDED"
    INVALIDATED = "INVALIDATED"
    BLOCKED = "BLOCKED"


class TerminalStatus(StrEnum):
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    BLOCKED = "BLOCKED"
    INELIGIBLE = "INELIGIBLE"
    DIAGNOSTIC_ONLY = "DIAGNOSTIC_ONLY"
    SUPERSEDED = "SUPERSEDED"
    INVALIDATED = "INVALIDATED"


@dataclass(frozen=True)
class ExecutionContext:
    run_id: str
    run_root: Path
    repository_root: Path
    package_root: Path
    config_path: Path
    protocol_path: Path
    config_sha256: str
    protocol_snapshot_id: str
    protocol_sha256: str
    code_sha256: str
    environment_sha256: str
    source_manifest_sha256: str
    created_at_utc: str
    authoring_fixture: bool = False

    @property
    def immutable_fingerprint(self) -> dict[str, str]:
        return {
            "run_id": self.run_id,
            "config_sha256": self.config_sha256,
            "protocol_sha256": self.protocol_sha256,
            "code_sha256": self.code_sha256,
            "environment_sha256": self.environment_sha256,
            "source_manifest_sha256": self.source_manifest_sha256,
        }


@dataclass
class StageReceipt:
    stage_id: str
    gate_id: str
    playbook_steps: list[str]
    status: str
    start_time: str
    end_time: str | None
    config_sha: str
    protocol_sha: str
    code_sha: str
    environment_sha: str
    input_manifest_sha: str
    output_manifest_sha: str | None
    stage_fingerprint: str
    attempt: int
    supersedes: list[str] = field(default_factory=list)
    failure: dict[str, Any] | None = None
    checkpoint: dict[str, Any] = field(default_factory=dict)
    progress: dict[str, Any] = field(default_factory=dict)
    notes: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

