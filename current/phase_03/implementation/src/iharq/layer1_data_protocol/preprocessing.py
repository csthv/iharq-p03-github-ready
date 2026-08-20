from __future__ import annotations
from dataclasses import dataclass
from typing import Any
import math, numpy as np
from scipy import signal as sps
from iharq.canonical import semantic_hash
from .models import RawRecording, Event
from .records import make_record

@dataclass
class FitState:
    mean: np.ndarray|None
    std: np.ndarray|None
    source_ids: list[str]
    state_hash: str

def compile_operations(profile:dict[str,Any])->list[dict[str,Any]]:
    ops=profile.get("operations")
    if not isinstance(ops,list) or not ops: raise ValueError("official preprocessing operations missing")
    ordered=sorted((dict(x) for x in ops),key=lambda x:int(x.get("order",0)))
    required=["validate_units","capture_events","select_eeg","demean","rereference_average","resample_polyphase_with_events","bandpass_sos_zero_phase","cast"]
    names=[x.get("name") for x in ordered]
    if names==required: return ordered
    legacy_allowed={"demean","rereference_average","bandpass","notch","resample","standardize_train_fit"}
    if names and set(names).issubset(legacy_allowed): return ordered
    raise ValueError(f"preprocessing graph differs from freeze: {names}")

def fit(recordings:list[RawRecording],legal_source_ids:set[str],operations:list[dict[str,Any]])->FitState:
    if not legal_source_ids: raise ValueError("legal fit population is empty")
    if any(op.get("name")=="standardize_train_fit" for op in operations):
        selected=[r for r in recordings if f"{r.dataset_id}:{r.subject_id}:{r.session_id}:{r.run_id}" in legal_source_ids]
        if not selected: raise ValueError("legal fit population is empty")
        cat=np.concatenate([r.signal for r in selected],axis=1); mean=cat.mean(axis=1,keepdims=True); std=cat.std(axis=1,keepdims=True); std=np.where(std<1e-12,1.0,std)
        return FitState(mean,std,sorted(legal_source_ids),semantic_hash({"mean":[str(float(x)) for x in mean[:,0]],"std":[str(float(x)) for x in std[:,0]],"sources":sorted(legal_source_ids)}))
    return FitState(None,None,sorted(legal_source_ids),semantic_hash({"fit":"not-required","sources":sorted(legal_source_ids)}))

def _mne_raw_for_recording(rec:RawRecording):
    raw=rec.source_metadata.get("_mne_raw")
    if raw is not None: return raw.copy().load_data()
    import mne
    ch_types=rec.source_metadata.get("channel_types") or ["eeg"]*len(rec.channel_names)
    info=mne.create_info(rec.channel_names,float(rec.sampling_hz),ch_types=ch_types)
    return mne.io.RawArray(np.asarray(rec.signal,dtype=np.float64),info,verbose="ERROR")

def transform_recording(rec:RawRecording,operations:list[dict[str,Any]],state:FitState)->RawRecording:
    raw=_mne_raw_for_recording(rec); source_sf=float(raw.info['sfreq'])
    if not math.isfinite(source_sf) or source_sf<=0: raise ValueError("invalid source sampling rate")
    events_arr=np.array([[int(e.start_sample),0,i+1] for i,e in enumerate(rec.events)],dtype=int) if rec.events else np.zeros((0,3),dtype=int)
    event_meta=[dict(e.metadata,original_source_event_sample=int(e.start_sample),original_stop_sample=int(e.stop_sample),original_onset_seconds=float(e.start_sample/source_sf)) for e in rec.events]
    # Select EEG only after event capture.
    picks=[i for i,t in enumerate(raw.get_channel_types()) if t=="eeg"]
    if not picks: raise ValueError("no EEG channels available")
    raw.pick(picks); data=raw.get_data().astype(np.float64,copy=True)
    if not np.isfinite(data).all(): raise ValueError("nonfinite source signal")
    data-=data.mean(axis=1,keepdims=True); data-=data.mean(axis=0,keepdims=True); raw._data=data
    target=160.0
    if events_arr.size:
        raw,events_resampled=raw.resample(target,method="polyphase",window=("kaiser",5.0),pad="reflect",events=events_arr,n_jobs=1,verbose="ERROR")
    else:
        raw.resample(target,method="polyphase",window=("kaiser",5.0),pad="reflect",n_jobs=1,verbose="ERROR"); events_resampled=events_arr
    y=raw.get_data().astype(np.float64,copy=False)
    sos=sps.butter(4,[8.0,32.0],btype="bandpass",fs=target,output="sos")
    if y.shape[1] <= 27: raise ValueError("continuous run shorter than frozen SOS pad length")
    y=sps.sosfiltfilt(sos,y,axis=1,padtype="odd",padlen=27).astype(np.float32)
    new_events=[]
    for i,e in enumerate(rec.events):
        new_start=int(events_resampled[i,0]); duration_sec=max(1/source_sf,(e.stop_sample-e.start_sample)/source_sf); new_stop=new_start+max(1,int(round(duration_sec*target)))
        meta=dict(event_meta[i],resampled_event_sample=new_start,resampled_stop_sample=new_stop,resampled_sampling_hz=target,event_resampling_method="MNE_POLYPHASE_JOINT_EVENTS")
        new_events.append(Event(e.event_id,new_start,new_stop,e.original_label,meta))
    return RawRecording(rec.dataset_id,rec.subject_id,rec.session_id,rec.run_id,rec.source_file,target,list(raw.ch_names),y,new_events,
        {k:v for k,v in rec.source_metadata.items() if k!="_mne_raw"}|{"preprocessing_history":[x["name"] for x in operations],"source_sampling_hz":source_sf,"output_dtype":"float32"})

def transform_signal(x:np.ndarray,sampling_hz:float,operations:list[dict[str,Any]],state:FitState)->tuple[np.ndarray,float]:
    names=[op.get("name") for op in operations]
    if names==["validate_units","capture_events","select_eeg","demean","rereference_average","resample_polyphase_with_events","bandpass_sos_zero_phase","cast"]:
        rec=RawRecording("compat","0","0","0","compat",sampling_hz,[f"EEG{i}" for i in range(x.shape[0])],x,[],{"channel_types":["eeg"]*x.shape[0]})
        out=transform_recording(rec,operations,state); return out.signal,out.sampling_hz
    y=np.asarray(x,dtype=np.float64).copy(); sf=float(sampling_hz)
    for op in operations:
        name=op["name"]
        if name=="demean": y=y-y.mean(axis=1,keepdims=True)
        elif name=="rereference_average": y=y-y.mean(axis=0,keepdims=True)
        elif name=="bandpass":
            sos=sps.butter(int(op.get("order",4)),[float(op["low_hz"]),float(op["high_hz"])],btype="bandpass",fs=sf,output="sos"); y=sps.sosfiltfilt(sos,y,axis=1)
        elif name=="notch":
            b,a=sps.iirnotch(float(op["frequency_hz"]),float(op.get("q",30)),fs=sf); y=sps.filtfilt(b,a,y,axis=1)
        elif name=="resample":
            target=float(op["target_hz"]); n=max(1,int(round(y.shape[1]*target/sf))); y=sps.resample(y,n,axis=1); sf=target
        elif name=="standardize_train_fit":
            if state.mean is None or state.std is None: raise ValueError("standardization requires fit state")
            y=(y-state.mean)/state.std
    return y,sf

def build_preprocessing_record(profile:dict[str,Any],operations:list[dict[str,Any]],state:FitState,source_ids:list[str],config_id:str,output_pointer:str)->dict[str,Any]:
    payload={"preprocessing_id":f"preprocessing:{config_id[:16]}","profile_id":str(profile["profile_id"]),"operations":operations,"fit_scope":str(profile["fit_scope"]),
      "fit_source_ids":state.source_ids,"fit_state_hash":state.state_hash,"input_ids":source_ids,"output_pointer":output_pointer,"joint_event_resampling":True,
      "target_sampling_hz":160,"filter_sos_padlen":27,"output_dtype":"float32"}
    return make_record("PreprocessingRecord",payload,config_id,source_ids,lifecycle_status="VALIDATED")
