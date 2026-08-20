"""Atomic, path-safe, canonical writers, manifests, checksums, and secret scanning."""

from __future__ import annotations

import csv
import json
import os
import re
import tempfile
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from .errors import SecurityViolation
from .identity import canonical_json, sha256_file, utc_now

SECRET_PATTERNS = {
    "generic_bearer": re.compile(r"(?i)\bbearer\s+[A-Za-z0-9._~+/=-]{16,}"),
    "hf_token": re.compile(r"\bhf_[A-Za-z0-9]{20,}\b"),
    "aws_access": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "private_key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "generic_secret_assignment": re.compile(r"(?i)(?:api[_-]?key|token|password|secret)\s*[:=]\s*['\"][^'\"]{12,}['\"]"),
}


def safe_child(root: str | Path, relative: str | Path) -> Path:
    root = Path(root).resolve()
    candidate = (root / relative).resolve()
    if candidate != root and root not in candidate.parents:
        raise SecurityViolation(f"Path escapes governed root: {relative}")
    return candidate


def _atomic_bytes(path: Path, payload: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_name, path)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)


def write_json(path: str | Path, payload: Any) -> Path:
    path = Path(path)
    _atomic_bytes(path, (canonical_json(payload) + "\n").encode("utf-8"))
    return path


def write_jsonl(path: str | Path, rows: Iterable[Mapping[str, Any]]) -> Path:
    data = "".join(canonical_json(dict(row)) + "\n" for row in rows)
    path = Path(path)
    _atomic_bytes(path, data.encode("utf-8"))
    return path


def write_csv(path: str | Path, rows: Sequence[Mapping[str, Any]], fieldnames: Sequence[str] | None = None) -> Path:
    path = Path(path)
    if fieldnames is None:
        fieldnames = list(rows[0]) if rows else []
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent, text=True)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="raise")
            writer.writeheader()
            writer.writerows(rows)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_name, path)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)
    return path


class AtomicJsonlCsvStream:
    """Bounded-memory dual JSONL/CSV writer with atomic success promotion.

    On failure, the closed temporary files remain inside the governed stage attempt
    directory so partial work is inspectable; they are never promoted as complete.
    """

    def __init__(self, jsonl_path: str | Path, csv_path: str | Path, fieldnames: Sequence[str]):
        self.jsonl_path, self.csv_path = Path(jsonl_path), Path(csv_path)
        self.fieldnames = list(fieldnames)
        self.jsonl_path.parent.mkdir(parents=True, exist_ok=True)
        self.csv_path.parent.mkdir(parents=True, exist_ok=True)
        json_fd, json_name = tempfile.mkstemp(prefix=f".{self.jsonl_path.name}.", suffix=".partial", dir=self.jsonl_path.parent)
        csv_fd, csv_name = tempfile.mkstemp(prefix=f".{self.csv_path.name}.", suffix=".partial", dir=self.csv_path.parent)
        self.json_temp, self.csv_temp = Path(json_name), Path(csv_name)
        self.json_handle = os.fdopen(json_fd, "w", encoding="utf-8", newline="")
        self.csv_handle = os.fdopen(csv_fd, "w", encoding="utf-8", newline="")
        self.csv_writer = csv.DictWriter(self.csv_handle, fieldnames=self.fieldnames, extrasaction="raise")
        self.csv_writer.writeheader()
        self.row_count = 0
        self.closed = False

    def write(self, row: Mapping[str, Any]) -> None:
        if self.closed:
            raise RuntimeError("stream already closed")
        payload = dict(row)
        self.json_handle.write(canonical_json(payload) + "\n")
        self.csv_writer.writerow(payload)
        self.row_count += 1

    def _close(self) -> None:
        if self.closed:
            return
        for handle in (self.json_handle, self.csv_handle):
            handle.flush()
            os.fsync(handle.fileno())
            handle.close()
        self.closed = True

    def commit(self) -> None:
        self._close()
        os.replace(self.json_temp, self.jsonl_path)
        os.replace(self.csv_temp, self.csv_path)

    def preserve_partial(self) -> None:
        self._close()


def build_manifest(root: str | Path, *, exclude_names: set[str] | None = None) -> dict[str, Any]:
    root = Path(root).resolve()
    excluded = exclude_names or {"checksums.sha256", "package_manifest.json"}
    files = []
    for path in sorted(p for p in root.rglob("*") if p.is_file() and p.name not in excluded):
        files.append({"path": path.relative_to(root).as_posix(), "bytes": path.stat().st_size, "sha256": sha256_file(path)})
    return {"manifest_version": "1.0", "created_at_utc": utc_now(), "root": ".", "file_count": len(files), "files": files}


def write_checksum_manifest(root: str | Path, path: str | Path | None = None) -> Path:
    root = Path(root).resolve()
    path = Path(path) if path else root / "checksums.sha256"
    lines = []
    for item in build_manifest(root)["files"]:
        lines.append(f"{item['sha256']}  {item['path']}")
    _atomic_bytes(path, ("\n".join(lines) + "\n").encode("utf-8"))
    return path


def verify_checksum_manifest(root: str | Path, path: str | Path | None = None) -> list[str]:
    root = Path(root).resolve()
    path = Path(path) if path else root / "checksums.sha256"
    failures: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        expected, relative = line.split("  ", 1)
        target = safe_child(root, relative)
        if not target.is_file() or sha256_file(target) != expected:
            failures.append(relative)
    return failures


def scan_for_secrets(root: str | Path, *, max_bytes: int = 5_000_000) -> list[dict[str, Any]]:
    root = Path(root)
    findings: list[dict[str, Any]] = []
    text_suffixes = {".py", ".json", ".jsonl", ".yaml", ".yml", ".md", ".txt", ".csv", ".toml", ".ipynb"}
    for path in sorted(p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in text_suffixes):
        if path.stat().st_size > max_bytes:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for name, pattern in SECRET_PATTERNS.items():
            for match in pattern.finditer(text):
                findings.append({
                    "path": path.relative_to(root).as_posix(),
                    "pattern": name,
                    "line": text.count("\n", 0, match.start()) + 1,
                    "redacted": "[REDACTED]",
                })
    return findings
