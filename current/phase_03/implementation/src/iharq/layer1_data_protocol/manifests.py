from __future__ import annotations
from pathlib import Path
from typing import Any
import json
from iharq.manifests import build_file_manifest
from .records import make_record

def write_json(path:Path,obj:Any):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(obj,indent=2,ensure_ascii=False),encoding="utf-8")

def build_layer1_manifest(root:Path,records:list[dict[str,Any]],gates:list[dict[str,Any]],readiness_path:str,p02_handoff_path:str,config_id:str)->dict[str,Any]:
    entries=build_file_manifest(root,exclude={"checksums.sha256","manifests/phase_01/layer1_manifest.json","manifests/phase_01/execution_bundle_manifest.json"})
    payload={"manifest_id":f"layer1:{config_id[:16]}","record_ids":[r["record_id"] for r in records],"artifact_entries":entries,"gate_decisions":gates,"readiness_artifact":readiness_path,"p02_handoff":p02_handoff_path,"limitations":["PUBLIC_EEG_ONLY","NON_CLINICAL","NO_DEPLOYMENT_CLAIM"]}
    return make_record("Layer1Manifest",payload,config_id,[r["record_id"] for r in records],evidence_mode="REPRODUCIBILITY_READINESS",lifecycle_status="VALIDATED" if all(g["status"]=="PASS" for g in gates) else "BLOCKED",evidence_role="PACKAGING")

def write_checksums(root:Path,path:Path):
    rows=build_file_manifest(root,exclude={path.relative_to(root).as_posix()})
    path.parent.mkdir(parents=True,exist_ok=True)
    content="".join(f"{r['sha256']}  {r['path']}\n" for r in rows)
    path.write_text(content,encoding="utf-8")
    return rows


def verify_execution_manifest(root:Path, manifest_path:Path)->dict[str,Any]:
    data=json.loads(manifest_path.read_text(encoding="utf-8"))
    errors=[]
    for row in data.get("entries",[]):
        target=root/row["path"]
        if not target.is_file(): errors.append({"path":row["path"],"reason":"MISSING"}); continue
        from iharq.manifests import file_digest
        observed=file_digest(target)
        if observed!=row["sha256"]: errors.append({"path":row["path"],"reason":"SHA256_MISMATCH","expected":row["sha256"],"observed":observed})
    return {"status":"PASS" if not errors else "FAIL","checked":len(data.get("entries",[])),"errors":errors}

def verify_checksums(root:Path, path:Path)->dict[str,Any]:
    from iharq.manifests import file_digest
    errors=[]; checked=0
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip(): continue
        digest,rel=line.split(None,1); rel=rel.strip(); target=root/rel; checked+=1
        if not target.is_file(): errors.append({"path":rel,"reason":"MISSING"}); continue
        observed=file_digest(target)
        if observed!=digest: errors.append({"path":rel,"reason":"SHA256_MISMATCH","expected":digest,"observed":observed})
    return {"status":"PASS" if not errors else "FAIL","checked":checked,"errors":errors}
