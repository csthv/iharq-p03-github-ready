"""Append-only threshold registry with durable records and deterministic index."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Mapping

from .identity import canonical_json
from .thresholds import register_threshold, resolve_threshold, supersede_threshold
from .writers import write_json


class ThresholdStore:
    def __init__(self, root: str | Path):
        self.root = Path(root)
        self.log_path = self.root / "threshold_registry.jsonl"
        self.index_path = self.root / "threshold_registry_index.json"
        self.root.mkdir(parents=True, exist_ok=True)

    def _append(self, payload: Mapping[str, Any]) -> None:
        line = (canonical_json(dict(payload)) + "\n").encode("utf-8")
        fd = os.open(self.log_path, os.O_CREAT | os.O_WRONLY | os.O_APPEND, 0o644)
        try:
            os.write(fd, line)
            os.fsync(fd)
        finally:
            os.close(fd)

    def events(self) -> list[dict[str, Any]]:
        if not self.log_path.exists():
            return []
        with self.log_path.open("r", encoding="utf-8") as handle:
            return [json.loads(line) for line in handle if line.strip()]

    def active_records(self) -> list[dict[str, Any]]:
        records: dict[str, dict[str, Any]] = {}
        for event in self.events():
            if event.get("event") == "REGISTER":
                record = dict(event["record"])
                records[record["threshold_id"]] = record
            elif event.get("event") == "SUPERSEDE" and event["threshold_id"] in records:
                records[event["threshold_id"]]["lifecycle_status"] = "SUPERSEDED"
                records[event["threshold_id"]]["effective_until"] = event["effective_until"]
                records[event["threshold_id"]]["supersession_reason"] = event["reason"]
                records[event["threshold_id"]]["successor_id"] = event["successor_id"]
        return sorted(records.values(), key=lambda item: item["threshold_id"])

    def register(self, candidate: Mapping[str, Any]) -> dict[str, Any]:
        record = register_threshold(candidate)
        if any(item["threshold_id"] == record["threshold_id"] for item in self.active_records()):
            return record
        self._append({"event": "REGISTER", "record": record})
        self.rebuild_index()
        return record

    def supersede(self, old_id: str, successor_id: str, reason: str, effective_until: str) -> dict[str, Any]:
        active = {item["threshold_id"]: item for item in self.active_records()}
        if old_id not in active or successor_id not in active:
            raise ValueError("Both old and successor thresholds must be registered")
        event = supersede_threshold(active[old_id], successor_id, reason, effective_until)
        self._append(event)
        self.rebuild_index()
        return event

    def resolve(self, query: Mapping[str, Any], consumer: str) -> dict[str, Any]:
        return resolve_threshold(self.active_records(), query, consumer)

    def rebuild_index(self) -> Path:
        records = self.active_records()
        return write_json(self.index_path, {"active_count": sum(r["lifecycle_status"] == "ACTIVE" for r in records), "records": records})

