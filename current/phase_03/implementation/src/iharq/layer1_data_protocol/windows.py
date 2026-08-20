from __future__ import annotations
from pathlib import Path
from typing import Any
import numpy as np
from iharq.canonical import semantic_hash
from .models import RawRecording
from .records import make_record
from .labels import map_event_label
from .splits import recording_role

def generate(recordings:list[RawRecording],assignment:dict[str,str],split_keys:list[str],label_record:dict[str,Any],preprocessing_record:dict[str,Any],profile:dict[str,Any],config_id:str,output_root:Path,split_record:dict[str,Any]|None=None,dataset_record_id:str|None=None)->tuple[list[dict[str,Any]],list[dict[str,Any]]]:
    official="start_offset_samples" in profile
    if official:
        offset=int(profile["start_offset_samples"]); dur=int(profile["duration_samples"]); stride=int(profile["stride_samples"])
        if dur!=480 or stride!=480 or offset!=80: raise ValueError("window parameters differ from official freeze")
    else:
        offset=0; dur=max(1,int(round(float(profile["duration_seconds"])*recordings[0].sampling_hz))); stride=max(1,int(round(float(profile["stride_seconds"])*recordings[0].sampling_hz)))
    split_id=(split_record or {}).get("record_id") or preprocessing_record.get("payload",{}).get("split_record_id")
    if not split_id: raise ValueError("window generation requires explicit SplitRecord lineage")
    output_root.mkdir(parents=True,exist_ok=True); records=[]; index=[]; invalid=[]
    for rec in recordings:
        if official and abs(float(rec.sampling_hz)-160.0)>1e-9: raise ValueError("windows require frozen 160 Hz signal")
        role=recording_role(rec,assignment,split_keys)
        for event in rec.events:
            normalized=map_event_label(event.original_label,label_record)
            if normalized is None: continue
            source_sample=event.metadata.get("original_source_event_sample",event.start_sample if not official else None)
            resampled_sample=event.metadata.get("resampled_event_sample",event.start_sample)
            if source_sample is None or resampled_sample is None:
                invalid.append({"event_id":event.event_id,"reason":"MISSING_PARENT_EVENT_SAMPLE_LINEAGE"}); continue
            start=int(resampled_sample)+offset; end=start+dur
            if start<0 or end>rec.signal.shape[1]:
                invalid.append({"event_id":event.event_id,"start":start,"end":end,"samples":rec.signal.shape[1],"reason":"WINDOW_OUT_OF_BOUNDS"}); continue
            identity={"dataset":rec.dataset_id,"subject":rec.subject_id,"session":rec.session_id,"run":rec.run_id,"event":event.event_id,"original_event_sample":source_sample,"resampled_event_sample":resampled_sample,"start":start,"stop":end,"split_record_id":split_id,"role":role,"config":config_id}
            digest=semantic_hash(identity); wid="window:"+digest[:20]; rel=Path("derived_outputs/windows")/rec.dataset_id/role/f"{digest[:24]}.npz"; path=output_root/rel; path.parent.mkdir(parents=True,exist_ok=True)
            signal=rec.signal[:,start:end]; np.savez_compressed(path,signal=signal,sampling_hz=np.asarray(rec.sampling_hz),channel_names=np.asarray(rec.channel_names))
            payload={"window_id":wid,"parent_event_id":event.event_id,"dataset_id":rec.dataset_id,"subject_id":rec.subject_id,"session_id":rec.session_id,"run_id":rec.run_id,
              "split_record_id":split_id,"preprocessing_record_id":preprocessing_record["record_id"],"label_map_record_id":label_record["record_id"],
              "original_source_event_sample":int(source_sample),"resampled_event_sample":int(resampled_sample),"start_offset_samples":offset,"start_sample":start,"stop_sample":end,
              "duration_samples":dur,"stride_samples":stride,"overlap_group_id":event.event_id,"normalized_label":normalized,"original_label":event.original_label,"role":role,
              "signal_pointer":rel.as_posix(),"channel_mask_id":None}
            source_ids=[x for x in [dataset_record_id,split_id,preprocessing_record["record_id"],label_record["record_id"]] if x]
            record=make_record("WindowRecord",payload,config_id,source_ids,lifecycle_status="VALIDATED"); records.append(record)
            index.append({"window_record_id":record["record_id"],"path":rel.as_posix(),"role":role,"label":normalized,"event_id":event.event_id,"split_record_id":split_id,
              "dataset_id":rec.dataset_id,"subject_id":rec.subject_id,"session_id":rec.session_id,"run_id":rec.run_id,"overlap_group_id":event.event_id,
              "sample_hash":semantic_hash({"shape":list(signal.shape),"head":[str(float(v)) for v in signal.reshape(-1)[:128]]})})
    if invalid:
        invalid_path=output_root/"negative_and_failed_results"/f"invalid_windows_{recordings[0].dataset_id if recordings else 'unknown'}.json"
        invalid_path.parent.mkdir(parents=True,exist_ok=True)
        invalid_path.write_text(__import__('json').dumps(invalid,indent=2),encoding='utf-8')
    return records,index
