from __future__ import annotations
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any
import hashlib, urllib.request, json, re
from ..models import RawRecording, SourceProfile

class SourceAccessError(RuntimeError):
    __slots__=()

def file_sha256(path:Path)->str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""): h.update(chunk)
    return h.hexdigest()

def aggregate_file_digest(rows:list[dict[str,Any]])->str:
    h=hashlib.sha256()
    for row in sorted(rows,key=lambda x:x["relative_path"]):
        h.update(str(row["relative_path"]).encode()); h.update(b"\0"); h.update(str(row["sha256"]).encode()); h.update(b"\0"); h.update(str(row["bytes"]).encode()); h.update(b"\n")
    return h.hexdigest()

def _safe_rel(path:Path,bases:list[tuple[str,Path]])->tuple[str,str]:
    for cls,base in bases:
        try: return path.relative_to(base).as_posix(),cls
        except ValueError: pass
    return path.name,"EXTERNAL_RESOLVED_FILE"

class BaseDatasetAdapter(ABC):
    def __init__(self,profile:SourceProfile,input_root:Path,cache_root:Path):
        self.profile=profile; self.input_root=Path(input_root); self.cache_root=Path(cache_root); self.cache_root.mkdir(parents=True,exist_ok=True)
    @abstractmethod
    def resolve_files(self)->list[Path]: raise SourceAccessError("source resolver unavailable")
    def verify_files(self,files:list[Path])->dict[str,Any]:
        if not files: raise SourceAccessError("empty source file inventory")
        bases=[("KAGGLE_INPUT",self.input_root),("WORKING_CACHE",self.cache_root)]
        rows=[]
        for p in sorted(set(Path(x).resolve() for x in files if Path(x).is_file())):
            rel,cls=_safe_rel(p,bases); rows.append({"relative_path":rel,"runtime_path_class":cls,"sha256":file_sha256(p),"bytes":p.stat().st_size})
        if not rows: raise SourceAccessError("no source bytes available for verification")
        aggregate=aggregate_file_digest(rows); policy=self.profile.checksum_policy
        provider_verified=0; provider_failed=[]
        if "PHYSIONET SHA256SUMS" in policy.upper():
            manifest_url=str(self.profile.adapter_options.get("provider_checksum_manifest_url") or "https://physionet.org/files/eegmmidb/1.0.0/SHA256SUMS.txt")
            target=self.cache_root/"SHA256SUMS.txt"
            if not target.exists(): urllib.request.urlretrieve(manifest_url,target)
            expected={}
            for line in target.read_text(encoding="utf-8",errors="replace").splitlines():
                m=re.match(r"^([0-9a-fA-F]{64})\s+\*?(.+?)\s*$",line)
                if m: expected[Path(m.group(2)).as_posix().lstrip('./')]=m.group(1).lower()
            for row in rows:
                candidates=[k for k in expected if k.endswith(row["relative_path"]) or k.endswith(Path(row["relative_path"]).name)]
                if not candidates: provider_failed.append({"path":row["relative_path"],"reason":"NOT_IN_PROVIDER_MANIFEST"}); continue
                ok=any(expected[k]==row["sha256"] for k in candidates)
                if ok: provider_verified+=1
                else: provider_failed.append({"path":row["relative_path"],"reason":"PROVIDER_SHA256_MISMATCH"})
            if provider_failed: raise SourceAccessError(f"provider checksum verification failed: {provider_failed[:3]}")
            checksum_status="PROVIDER_VERIFIED_AND_AGGREGATE_FROZEN"
        else:
            checksum_status="COMPUTED_AND_FROZEN_FOR_RUN"
        return {"files":rows,"count":len(rows),"aggregate_sha256":aggregate,"observed_checksum":aggregate,"published_checksum":self.profile.published_checksum,
                "checksum_policy":policy,"checksum_status":checksum_status,"provider_verified_files":provider_verified,"provider_failures":provider_failed}
    @abstractmethod
    def load(self,files:list[Path])->list[RawRecording]: raise SourceAccessError("adapter load implementation unavailable")
