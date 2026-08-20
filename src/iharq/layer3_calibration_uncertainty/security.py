"""Credential-symbol, path, output, and export safety checks."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Iterable

from .errors import GateBlocked, SecurityViolation
from .writers import scan_for_secrets


ALLOWED_CREDENTIAL_SYMBOLS = frozenset({"IHARQ_HF_TOKEN_P02", "IHARQ_HF_TOKEN_P03"})


def require_credential_symbol(symbol: str, *, gate_id: str) -> str:
    if symbol not in ALLOWED_CREDENTIAL_SYMBOLS:
        raise SecurityViolation(f"Unapproved credential symbol: {symbol}")
    value = os.environ.get(symbol)
    if not value:
        raise GateBlocked(gate_id, "SYMBOLIC_CREDENTIAL_MISSING", symbol)
    return value


def assert_clean_export(root: str | Path) -> dict[str, object]:
    findings = scan_for_secrets(root)
    if findings:
        raise SecurityViolation(f"Secret scan found {len(findings)} item(s)")
    return {"status": "PASS", "literal_secrets": 0, "scanned_root": Path(root).as_posix()}


def sanitize_environment(keys: Iterable[str]) -> dict[str, str]:
    result = {}
    for key in keys:
        result[key] = "PRESENT_REDACTED" if os.environ.get(key) else "ABSENT"
    return result

