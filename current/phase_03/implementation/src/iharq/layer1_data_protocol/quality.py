from __future__ import annotations
from typing import Any
import numpy as np
from .models import RawRecording
from .records import make_record

def _max_identical_run(x:np.ndarray)->int:
    if x.size<2: return int(x.size)
    changes=np.flatnonzero(np.diff(x)!=0)+1; bounds=np.r_[0,changes,x.size]; return int(np.max(np.diff(bounds)))

def annotate(recording:RawRecording,profile:dict[str,Any],config_id:str,dataset_record_id:str|None=None)->tuple[list[dict[str,Any]],dict[str,Any]]:
    thresholds=profile.get("thresholds") or {}
    flat=float(thresholds.get("flat_channel_std_max_v",profile.get("flat_std_threshold",0.0)))
    amp=float(thresholds.get("absolute_amplitude_max_v",profile.get("absolute_amplitude_threshold",float("inf"))))
    nonfinite_max=int(thresholds.get("nonfinite_count_max",0)); repeat_max=int(thresholds.get("repeated_identical_samples_max",10**9)); minimum=int(thresholds.get("minimum_window_samples",1))
    x=np.asarray(recording.signal); flags=[]; hard_invalid=[]
    if x.ndim!=2: hard_invalid.append((None,"WRONG_TENSOR_RANK","ERROR"))
    if x.ndim==2 and x.shape[1]<minimum: hard_invalid.append((None,"RUN_SHORTER_THAN_WINDOW","ERROR"))
    for i,ch in enumerate(recording.channel_names if x.ndim==2 else []):
        nonfinite=int(np.size(x[i])-np.isfinite(x[i]).sum()); std=float(np.nanstd(x[i])); mx=float(np.nanmax(np.abs(x[i]))) if np.isfinite(x[i]).any() else float('inf'); repeat=_max_identical_run(x[i])
        if nonfinite>nonfinite_max: hard_invalid.append((ch,"NONFINITE_VALUES","ERROR"))
        if std<=flat: flags.append((ch,"FLAT_CHANNEL","WARNING"))
        if mx>amp: flags.append((ch,"AMPLITUDE_EXCEEDS_SOFT_THRESHOLD","WARNING"))
        if repeat>repeat_max: flags.append((ch,"REPEATED_IDENTICAL_SAMPLES","WARNING"))
    provider=recording.source_metadata.get("provider_quality_flags",[])
    for row in provider: flags.append((row.get("channel"),str(row.get("code","SOURCE_DECLARED_QUALITY_FLAG")),str(row.get("severity","WARNING"))))
    rows=[]
    for ch,code,severity in [*hard_invalid,*flags]:
        payload={"artifact_flag_id":f"{recording.dataset_id}:{recording.run_id}:{ch or 'RUN'}:{code}","dataset_id":recording.dataset_id,
          "target_id":f"{recording.dataset_id}:{recording.subject_id}:{recording.session_id}:{recording.run_id}","flag_code":code,"channel_name":ch,
          "severity":severity,"source_supported":code.startswith("SOURCE_") or code=="PROVIDER_REJECTED_TRIAL","action":"BLOCK_AFFECTED_RECORD" if severity=="ERROR" else "ANNOTATE_ONLY",
          "units":"VOLTS","threshold_profile_id":profile.get("profile_id")}
        rows.append(make_record("ArtifactFlagRecord",payload,config_id,[dataset_record_id] if dataset_record_id else [],lifecycle_status="VALIDATED",evidence_role="DERIVED"))
    return rows,{"dataset_id":recording.dataset_id,"source_file":recording.source_file,"flags":len(rows),"hard_invalid":len(hard_invalid),"quality_available":True,"policy":"ANNOTATE_NOT_REPAIR","units":"VOLTS"}
