from __future__ import annotations
from typing import Any, Iterable
from .models import SourceProfile
from .records import make_record
from .reason_codes import SOURCE_FACTS_UNRESOLVED, SOURCE_LICENSE_UNRESOLVED, SOURCE_REVISION_UNRESOLVED

REQUIRED_ACTIVE_FACTS=("exact_revision","citation","license","access_method","official_reference","checksum_policy","adapter")
INACTIVE_ADAPTERS={"NOT_APPLICABLE_TO_ACTIVE_RUN","NOT_ACTIVE_FOR_P01_OFFICIAL_RUN","SCREENED_SOURCE_ADAPTER_UNRESOLVED","ACCESS_UNRESOLVED",""}

def validate_source_profile(raw:dict[str,Any])->tuple[SourceProfile|None,list[dict[str,str]]]:
    blockers=[]; active=raw.get("active_for_run")
    if active not in {True,False}:
        blockers.append({"code":SOURCE_FACTS_UNRESOLVED,"field":"active_for_run","dataset_id":str(raw.get("dataset_id","<unknown>")),"owner":"BUILD_BOOK"})
        return None,blockers
    keys=REQUIRED_ACTIVE_FACTS if active else ("exact_revision","citation","license","official_reference")
    for key in keys:
        if key=="checksum_policy":
            value=str(raw.get("checksum_policy") or raw.get("expected_checksum") or "").strip()
            report_field="expected_checksum"
        else:
            value=str(raw.get(key) or "").strip(); report_field=key
        if not value:
            code=SOURCE_LICENSE_UNRESOLVED if key=="license" else SOURCE_REVISION_UNRESOLVED if key=="exact_revision" else SOURCE_FACTS_UNRESOLVED
            blockers.append({"code":code,"field":report_field,"dataset_id":str(raw.get("dataset_id","<unknown>")),"owner":"BUILD_BOOK"})
    adapter=str(raw.get("adapter") or "")
    if active and (not adapter or adapter in INACTIVE_ADAPTERS):
        blockers.append({"code":SOURCE_FACTS_UNRESOLVED,"field":"adapter","dataset_id":str(raw.get("dataset_id","<unknown>")),"owner":"BUILD_BOOK"})
    if blockers: return None,blockers
    return SourceProfile(
        dataset_id=str(raw["dataset_id"]),aliases=list(raw.get("aliases",[])),authority_status=str(raw["authority_status"]),scientific_role=str(raw["scientific_role"]),
        active_for_run=bool(active),exact_revision=str(raw["exact_revision"]),citation=str(raw["citation"]),license=str(raw["license"]),access_method=str(raw["access_method"]),
        official_reference=str(raw["official_reference"]),expected_checksum=str(raw.get("expected_checksum") or "COMPUTE_OR_VERIFY_PER_FROZEN_POLICY"),
        published_checksum=str(raw.get("published_checksum") or "NO_SINGLE_PROVIDER_WIDE_PUBLISHED_SHA256"),checksum_policy=str(raw.get("checksum_policy") or ""),
        adapter=adapter,cache_path=str(raw.get("cache_path") or ""),redistribution_allowed=str(raw.get("redistribution_allowed") or "NOT_APPLICABLE"),
        source_native_preprocessing=list(raw.get("source_native_preprocessing",[])),limitations=list(raw.get("limitations",[])),adapter_options=dict(raw.get("adapter_options",{}))) ,[]

def alias_index(profiles:Iterable[SourceProfile])->dict[str,str]:
    index={}
    for p in profiles:
        for value in [p.dataset_id,*p.aliases]:
            key=str(value).strip().casefold()
            if key in index and index[key]!=p.dataset_id: raise ValueError(f"dataset alias collision: {value}")
            index[key]=p.dataset_id
    return index

def resolve_alias(profiles:Iterable[SourceProfile],value:str)->str:
    key=str(value).strip().casefold(); index=alias_index(profiles)
    if key not in index: raise KeyError(f"unknown dataset alias: {value}")
    return index[key]

def admission_decision(profile:SourceProfile)->dict[str,Any]:
    selected=profile.authority_status in {"PRIMARY_SELECTED","PRIMARY_SELECTED_WITH_SOURCE_QUALIFICATIONS","SELECTED"}
    admitted=profile.active_for_run and selected
    return {"dataset_id":profile.dataset_id,"admitted":admitted,"authority_status":profile.authority_status,"reason":"ACTIVE_AND_AUTHORIZED" if admitted else "INACTIVE_SCREENED_OR_NOT_AUTHORIZED"}

def build_dataset_record(profile:SourceProfile,inventory:dict[str,Any],metadata_summary:dict[str,Any],config_id:str)->dict[str,Any]:
    payload={"dataset_id":profile.dataset_id,"aliases":profile.aliases,"authority_status":profile.authority_status,"scientific_role":profile.scientific_role,
      "source_revision":profile.exact_revision,"citation":profile.citation,"license":profile.license,"access_method":profile.access_method,"official_reference":profile.official_reference,
      "published_checksum":profile.published_checksum,"checksum_policy":profile.checksum_policy,"observed_aggregate_sha256":inventory.get("aggregate_sha256"),
      "redistribution_allowed":profile.redistribution_allowed,"subjects":metadata_summary.get("subjects",[]),"sessions":metadata_summary.get("sessions",[]),"runs":metadata_summary.get("runs",[]),
      "event_count":metadata_summary.get("event_count",0),"channel_sets":metadata_summary.get("channel_sets",[]),"sampling_hz":metadata_summary.get("sampling_hz",[]),
      "metadata_completeness":metadata_summary.get("completeness",{}),"source_inventory":inventory,"source_native_preprocessing":profile.source_native_preprocessing,
      "limitations":profile.limitations,"admission_status":"ADMITTED"}
    return make_record("DatasetRecord",payload,config_id,[],lifecycle_status="VALIDATED")
