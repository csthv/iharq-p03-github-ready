"""Canonical serialization, hashing, and deterministic identifiers."""

from __future__ import annotations

import dataclasses
import datetime as dt
import hashlib
import json
import math
from pathlib import Path
from typing import Any, Iterable


def _normalize(value: Any) -> Any:
    if dataclasses.is_dataclass(value):
        value = dataclasses.asdict(value)
    if isinstance(value, Path):
        return value.as_posix()
    if isinstance(value, dict):
        return {str(k): _normalize(v) for k, v in sorted(value.items(), key=lambda item: str(item[0]))}
    if isinstance(value, (list, tuple)):
        return [_normalize(v) for v in value]
    if isinstance(value, set):
        return sorted((_normalize(v) for v in value), key=lambda x: canonical_json(x))
    if isinstance(value, (dt.datetime, dt.date)):
        return value.isoformat().replace("+00:00", "Z")
    if hasattr(value, "item"):
        try:
            return _normalize(value.item())
        except (TypeError, ValueError):
            pass
    if isinstance(value, float):
        if not math.isfinite(value):
            raise ValueError("Canonical JSON prohibits NaN and infinity")
        if value == 0.0:
            return 0.0
    return value


def canonical_json(value: Any) -> str:
    """Return deterministic UTF-8-safe JSON used for all governed hashes."""
    return json.dumps(_normalize(value), ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_text(text: str) -> str:
    return sha256_bytes(text.encode("utf-8"))


def sha256_json(value: Any) -> str:
    return sha256_text(canonical_json(value))


def sha256_file(path: str | Path, chunk_bytes: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        while chunk := handle.read(chunk_bytes):
            digest.update(chunk)
    return digest.hexdigest()


def deterministic_id(prefix: str, payload: Any, length: int = 20) -> str:
    clean = "".join(c if c.isalnum() or c in "-_" else "-" for c in prefix).strip("-")
    return f"{clean}-{sha256_json(payload)[:length]}"


def combine_hashes(items: Iterable[str]) -> str:
    return sha256_json(sorted(str(item) for item in items))


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")

