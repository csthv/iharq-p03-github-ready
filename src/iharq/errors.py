from __future__ import annotations
from dataclasses import dataclass, asdict

@dataclass(frozen=True)
class ValidationIssue:
    code: str
    message: str
    path: str = "<root>"
    owner: str = "BUILD_BOOK"
    gate: str = "P0-GATE-08"
    severity: str = "ERROR"
    def as_dict(self): return asdict(self)

class IHARQError(Exception):
    code = "IHARQ_ERROR"
class ConfigError(IHARQError): code = "CFG_ERROR"
class CanonicalizationError(IHARQError): code = "JCS_ERROR"
class SchemaError(IHARQError): code = "SCHEMA_ERROR"
class LineageError(IHARQError): code = "LINEAGE_ERROR"
