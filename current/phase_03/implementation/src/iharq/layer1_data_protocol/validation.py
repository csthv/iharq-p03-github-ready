from __future__ import annotations
from pathlib import Path
from typing import Any
import json
from jsonschema import Draft202012Validator
from iharq.ids import validate_id
from iharq.lineage import missing_sources
from .records import make_record

def validate_records(records:list[dict[str,Any]],schema_root:Path,config_id:str)->tuple[list[dict[str,Any]],dict[str,Any]]:
    errors=[]
    for record in records:
        path=schema_root/f"{record['record_type']}.schema.json"
        if not path.exists(): errors.append({"code":"P01_SCHEMA_MISSING","record_id":record["record_id"],"schema":str(path)}); continue
        schema=json.loads(path.read_text(encoding="utf-8")); Draft202012Validator.check_schema(schema)
        for e in Draft202012Validator(schema).iter_errors(record): errors.append({"code":"P01_SCHEMA_INVALID","record_id":record["record_id"],"path":"/".join(map(str,e.path)),"message":e.message})
        if not validate_id(record["record_id"]): errors.append({"code":"P01_RECORD_ID_INVALID","record_id":record["record_id"]})
    missing=missing_sources(records)
    for rid,values in missing.items(): errors.append({"code":"P01_LINEAGE_BROKEN","record_id":rid,"missing":values})
    payload={"validation_report_id":f"validation:{config_id[:16]}","target_ids":[r["record_id"] for r in records],"checks":[{"name":"schema_id_lineage","status":"PASS" if not errors else "FAIL","errors":errors}],"status":"PASS" if not errors else "FAIL"}
    report=make_record("ValidationReport",payload,config_id,[r["record_id"] for r in records],evidence_mode="VALIDATION",lifecycle_status="VALIDATED" if not errors else "BLOCKED",evidence_role="DERIVED")
    return errors,report
