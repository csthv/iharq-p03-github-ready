"""Atomic stage execution, exact-fingerprint resume, attempt preservation, and progress."""

from __future__ import annotations

import json
import os
import shutil
import time
import traceback
from pathlib import Path
from typing import Any, Callable, Mapping

from .errors import GateBlocked, ResumeRejected
from .identity import sha256_json, utc_now
from .models import ExecutionContext, StageReceipt, StageStatus
from .resources import progress_payload
from .writers import build_manifest, write_json

STAGE_META: dict[str, dict[str, Any]] = {
    "00": {"title": "Authority/source preflight", "gate": "G03-00-AUTHORITY", "steps": ["1"]},
    "01": {"title": "Repository validation", "gate": "G03-01-REPOSITORY", "steps": ["1"]},
    "02": {"title": "Environment bootstrap and exact verification", "gate": "G03-02-ENVIRONMENT", "steps": ["1"]},
    "03": {"title": "External artifact retrieval", "gate": "G03-03-RETRIEVAL", "steps": ["1"]},
    "04": {"title": "P02 handoff verification", "gate": "G03-04-HANDOFF", "steps": ["1"]},
    "05": {"title": "P03 Protocol/config freeze verification", "gate": "G03-05-FREEZE", "steps": ["1"]},
    "06": {"title": "Schema/import/worker full component validation", "gate": "G03-06-COMPONENT", "steps": ["1", "2"]},
    "07": {"title": "Load/join/canonicalize", "gate": "G03-07-JOIN", "steps": ["2"]},
    "08": {"title": "Split/leakage firewall", "gate": "G03-08-LEAKAGE", "steps": ["3"]},
    "09": {"title": "Score/class-order/eligibility validation", "gate": "G03-09-ELIGIBILITY", "steps": ["4"]},
    "10": {"title": "Identity calibration baseline", "gate": "G03-10-IDENTITY", "steps": ["5"]},
    "11": {"title": "Accepted calibration challengers", "gate": "G03-11-CALIBRATION", "steps": ["5"]},
    "12": {"title": "Reliability and HCW audit", "gate": "G03-12-RELIABILITY", "steps": ["6"]},
    "13": {"title": "Mandatory and conditional uncertainty", "gate": "G03-13-UNCERTAINTY", "steps": ["7"]},
    "14": {"title": "A2 legal threshold selection", "gate": "G03-14-A2-SELECT", "steps": ["8"]},
    "15": {"title": "A2 frozen-rule application", "gate": "G03-15-A2-APPLY", "steps": ["8"]},
    "16": {"title": "A3 feature-specific selective curves", "gate": "G03-16-A3", "steps": ["8"]},
    "17": {"title": "Threshold registration", "gate": "G03-17-THRESHOLD", "steps": ["9"]},
    "18": {"title": "Matched A1/A2/A3 evidence", "gate": "G03-18-MATCHED", "steps": ["10"]},
    "19": {"title": "Group/budget audit", "gate": "G03-19-GROUP", "steps": ["6", "10"]},
    "20": {"title": "Negative/failure/diagnostic preservation", "gate": "G03-20-NEGATIVE", "steps": ["11"]},
    "21": {"title": "Layer10 source export", "gate": "G03-21-SOURCES", "steps": ["12"]},
    "22": {"title": "Layer0/EvidenceMap/P04 handoffs", "gate": "G03-22-HANDOFFS", "steps": ["13", "14"]},
    "23": {"title": "Evidence sufficiency and parity", "gate": "G03-23-SUFFICIENCY", "steps": ["14"]},
    "24": {"title": "Manifest/checksum/secret scan/export", "gate": "G03-24-EXPORT", "steps": ["14"]},
}


class StageRunner:
    def __init__(self, context: ExecutionContext):
        self.context = context
        self.stage_root = context.run_root / "stage_artifacts"
        self.checkpoint_root = context.run_root / "checkpoints"
        self.attempt_root = context.run_root / "attempts"
        self.failure_root = context.run_root / "artifacts" / "negative_and_failed_results" / "phase_03" / "stage_failures"
        for path in (self.stage_root, self.checkpoint_root, self.attempt_root, self.failure_root):
            path.mkdir(parents=True, exist_ok=True)

    def receipt_path(self, stage_id: str) -> Path:
        return self.checkpoint_root / f"stage_{stage_id}" / "receipt.json"

    def prior_outputs(self, stage_id: str) -> list[str]:
        index = int(stage_id)
        hashes = []
        for prior in range(index):
            path = self.receipt_path(f"{prior:02d}")
            if path.is_file():
                receipt = json.loads(path.read_text(encoding="utf-8"))
                if receipt.get("status") == StageStatus.COMPLETE:
                    hashes.append(str(receipt.get("output_manifest_sha")))
        return hashes

    def fingerprint(self, stage_id: str) -> str:
        return sha256_json({"stage_id": stage_id, "immutable_context": self.context.immutable_fingerprint, "prior_output_hashes": self.prior_outputs(stage_id)})

    def _load_existing(self, stage_id: str) -> dict[str, Any] | None:
        path = self.receipt_path(stage_id)
        return json.loads(path.read_text(encoding="utf-8")) if path.is_file() else None

    def run(self, stage_id: str, handler: Callable[[ExecutionContext, Path, Callable[..., None]], Mapping[str, Any]]) -> dict[str, Any]:
        if stage_id not in STAGE_META:
            raise KeyError(f"Unknown official P03 stage: {stage_id}")
        meta = STAGE_META[stage_id]
        fingerprint = self.fingerprint(stage_id)
        existing = self._load_existing(stage_id)
        if existing and existing.get("status") == StageStatus.COMPLETE:
            if existing.get("stage_fingerprint") != fingerprint:
                raise ResumeRejected(f"Stage {stage_id} checkpoint fingerprint drift; explicit invalidation/amendment required")
            return {"resume_action": "REUSED_EXACT_CHECKPOINT", "receipt": existing, "result": self.load_stage_result(stage_id)}

        attempts = sorted((self.attempt_root / f"stage_{stage_id}").glob("attempt_*"))
        attempt = len(attempts) + 1
        attempt_dir = self.attempt_root / f"stage_{stage_id}" / f"attempt_{attempt:03d}"
        staging = attempt_dir / "staging"
        staging.mkdir(parents=True, exist_ok=False)
        start_iso = utc_now()
        start_mono = time.monotonic()
        receipt = StageReceipt(
            stage_id=stage_id,
            gate_id=meta["gate"],
            playbook_steps=meta["steps"],
            status=StageStatus.IN_PROGRESS,
            start_time=start_iso,
            end_time=None,
            config_sha=self.context.config_sha256,
            protocol_sha=self.context.protocol_sha256,
            code_sha=self.context.code_sha256,
            environment_sha=self.context.environment_sha256,
            input_manifest_sha=self.context.source_manifest_sha256,
            output_manifest_sha=None,
            stage_fingerprint=fingerprint,
            attempt=attempt,
            checkpoint={"state": "IN_PROGRESS", "attempt_dir": attempt_dir.as_posix()},
            progress=progress_payload(0, 1, start_mono, last_completed=None, error_count=0, checkpoint_state="IN_PROGRESS"),
            notes=[meta["title"]],
        )
        write_json(attempt_dir / "receipt.json", receipt.to_dict())

        def progress(completed: int, total: int, last_completed: str | None = None, error_count: int = 0, checkpoint_state: str = "IN_PROGRESS") -> None:
            receipt.progress = progress_payload(completed, total, start_mono, last_completed=last_completed, error_count=error_count, checkpoint_state=checkpoint_state)
            write_json(attempt_dir / "progress.json", receipt.progress)

        try:
            result = dict(handler(self.context, staging, progress))
            result.setdefault("stage_id", stage_id)
            result.setdefault("gate_id", meta["gate"])
            result.setdefault("status", "PASS")
            write_json(staging / "stage_result.json", result)
            manifest = build_manifest(staging)
            write_json(staging / "stage_manifest.json", manifest)
            output_sha = sha256_json(manifest)
            destination = self.stage_root / f"stage_{stage_id}"
            if destination.exists():
                raise ResumeRejected(f"Refusing to overwrite existing promoted stage directory: {destination}")
            destination.parent.mkdir(parents=True, exist_ok=True)
            os.replace(staging, destination)
            receipt.status = StageStatus.COMPLETE
            receipt.end_time = utc_now()
            receipt.output_manifest_sha = output_sha
            receipt.checkpoint = {"state": "COMPLETE", "promoted_path": destination.as_posix(), "manifest_sha256": output_sha}
            receipt.progress = progress_payload(1, 1, start_mono, last_completed="stage_result.json", error_count=0, checkpoint_state="COMPLETE")
            checkpoint_path = self.receipt_path(stage_id)
            write_json(checkpoint_path, receipt.to_dict())
            write_json(attempt_dir / "receipt.json", receipt.to_dict())
            return {"resume_action": "EXECUTED", "receipt": receipt.to_dict(), "result": result}
        except Exception as exc:
            receipt.status = StageStatus.BLOCKED if isinstance(exc, GateBlocked) else StageStatus.FAILED
            receipt.end_time = utc_now()
            receipt.failure = {
                "exception_type": type(exc).__name__,
                "message": str(exc),
                "gate_id": getattr(exc, "gate_id", meta["gate"]),
                "reason_code": getattr(exc, "reason_code", "UNCLASSIFIED_STAGE_FAILURE"),
                "traceback": traceback.format_exc(),
            }
            receipt.checkpoint = {"state": str(receipt.status), "attempt_dir": attempt_dir.as_posix(), "staging_preserved": staging.exists()}
            receipt.progress = progress_payload(0, 1, start_mono, last_completed=None, error_count=1, checkpoint_state=str(receipt.status))
            write_json(attempt_dir / "receipt.json", receipt.to_dict())
            write_json(self.failure_root / f"stage_{stage_id}_attempt_{attempt:03d}.json", receipt.to_dict())
            write_json(self.receipt_path(stage_id), receipt.to_dict())
            raise

    def load_stage_result(self, stage_id: str) -> dict[str, Any]:
        path = self.stage_root / f"stage_{stage_id}" / "stage_result.json"
        if not path.is_file():
            raise FileNotFoundError(path)
        return json.loads(path.read_text(encoding="utf-8"))

    def ledger(self) -> dict[str, Any]:
        rows = []
        for stage_id in STAGE_META:
            receipt = self._load_existing(stage_id)
            rows.append(receipt or {"stage_id": stage_id, "gate_id": STAGE_META[stage_id]["gate"], "status": StageStatus.NOT_STARTED})
        return {"run_id": self.context.run_id, "stage_count": len(rows), "stages": rows}
