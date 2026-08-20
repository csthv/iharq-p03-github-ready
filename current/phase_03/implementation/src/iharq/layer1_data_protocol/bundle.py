from __future__ import annotations
from pathlib import Path
from typing import Any
import shutil, zipfile, json, yaml
from iharq.manifests import build_file_manifest, file_digest
from .manifests import write_checksums

BUNDLE_PATHS=["implementation_snapshot","config_snapshot","source_access","inputs","records","raw_outputs","derived_outputs","reports/phase_01","negative_and_failed_results","figure_source_data","table_source_data","docs/cards","tests","manifests/phase_01","analysis_inputs","protocol_v1_handoff","layer0_handoff","evidence_map_handoff","layer10_source_bundle","phase2_handoff","handoffs","external_artifact_pointers"]
SNAPSHOT_PATHS=["src/iharq","schemas/phase_01","configs/phase_01","configs/datasets","configs/preprocessing","configs/splits","configs/budgets","configs/windows","configs/quality","configs/validation","configs/cards","configs/manifests","contracts/phase_01","catalogs/record_family_catalog.yaml","pyproject.toml","requirements-lock.txt","requirements/requirements-kaggle-r1.txt"]

def initialize(root:Path):
    root.mkdir(parents=True,exist_ok=True)
    for rel in BUNDLE_PATHS: (root/rel).mkdir(parents=True,exist_ok=True)

def snapshot_runtime(source_root:Path,bundle_root:Path)->list[str]:
    snapshot=bundle_root/"implementation_snapshot"; copied=[]
    for rel in SNAPSHOT_PATHS:
        src=source_root/rel; dst=snapshot/rel
        if src.is_dir(): shutil.copytree(src,dst,dirs_exist_ok=True); copied.extend(p.relative_to(snapshot).as_posix() for p in dst.rglob('*') if p.is_file())
        elif src.is_file(): dst.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(src,dst); copied.append(dst.relative_to(snapshot).as_posix())
    return sorted(copied)

def create_integration_patch_manifest(source_root:Path,bundle_root:Path)->dict[str,Any]:
    rows=[]
    allowed=("src/","schemas/phase_01/","configs/phase_01/","configs/datasets/","configs/preprocessing/","configs/splits/","configs/budgets/","configs/windows/","configs/quality/","configs/validation/","configs/cards/","configs/manifests/","contracts/phase_01/","catalogs/","requirements/")
    for r in build_file_manifest(source_root):
        path=r["path"]
        if path in {"pyproject.toml","requirements-lock.txt"} or path.startswith(allowed):
            rows.append({"runtime_path":path,"intended_project_path":path,"origin":"P01_L1_KAGGLE_RUNTIME_R6","sha256":r["sha256"],"action":"ADD_OR_REPLACE_AFTER_REVIEW","invalidation":"AFFECTED_P01_DESCENDANTS_ONLY","validation":"COMPILE_TEST_HASH"})
    obj={"manifest_id":"P01-L1-INTEGRATION-PATCH-R6","files":rows,"later_integration_may_finish_missing_logic":False}
    (bundle_root/"integration_patch_manifest.yaml").write_text(yaml.safe_dump(obj,sort_keys=False),encoding="utf-8")
    return obj

def finalize(root:Path,zip_path:Path)->dict[str,Any]:
    checksum_path=root/"checksums.sha256"
    if not checksum_path.is_file():
        rows=write_checksums(root,checksum_path)
    else:
        rows=[line for line in checksum_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    with zipfile.ZipFile(zip_path,"w",zipfile.ZIP_DEFLATED) as z:
        for p in sorted(root.rglob("*")):
            if p.is_file(): z.write(p,p.relative_to(root.parent).as_posix())
    digest=file_digest(zip_path); sidecar=Path(str(zip_path)+".sha256")
    sidecar.write_text(f"{digest}  {zip_path.name}\n",encoding="utf-8")
    return {"zip":str(zip_path),"sha256":digest,"sha256_file":str(sidecar),"file_count":len(rows)+1,"bytes":zip_path.stat().st_size}
