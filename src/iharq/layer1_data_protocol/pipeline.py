from __future__ import annotations
from pathlib import Path
from typing import Any
import json, yaml, csv, shutil
from iharq.canonical import semantic_hash
from iharq.manifests import build_file_manifest
from .adapters import ADAPTERS
from .dataset_registry import validate_source_profile, admission_decision, build_dataset_record, alias_index
from .metadata import normalize_metadata
from .labels import build_label_map
from .preprocessing import compile_operations, fit, transform_recording, build_preprocessing_record
from .quality import annotate
from .splits import construct, recording_role, validate_disjointness, validate_role_coverage
from .budgets import allocate
from .windows import generate
from .validation import validate_records
from .leakage import audit as leakage_audit
from .cards import dataset_card, protocol_card
from .readiness import generate as readiness_generate, prove_a14_absent
from .gates import evaluate as gate_evaluate
from .manifests import write_json, build_layer1_manifest, write_checksums, verify_execution_manifest, verify_checksums
from .bundle import initialize, create_integration_patch_manifest, snapshot_runtime, finalize
from .records import hashable

def safe(v:Any)->str:
    import re
    return re.sub(r'[^A-Za-z0-9._-]+','_',str(v)).strip('_') or 'unknown'

def write_csv(path:Path,rows:list[dict[str,Any]],fields:list[str]):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows([{k:r.get(k,'') for k in fields} for r in rows])

class Layer1Pipeline:
    def __init__(self,package_root:Path,work_root:Path,config:dict[str,Any]):
        self.package_root=Path(package_root); self.work_root=Path(work_root); self.config=config; self.config_id=semantic_hash(hashable(config)); self.bundle_root=self.work_root/f"IHARQ_P01_L1_Phase_Execution_Bundle_{self.config_id[:12]}"; initialize(self.bundle_root)
        self.blockers=[]; self.state={"records":[],"recordings":[],"dataset_records":[],"label_records":[],"quality_records":[],"window_records":[],"stage_outputs":{},"stage_results":[],"phase0_regression_status":"NOT_RUN"}
    def resolve_sources(self):
        profiles=[]; decisions=[]
        for raw in self.config.get("datasets",[]):
            profile,blockers=validate_source_profile(raw); self.blockers.extend(blockers)
            if profile is not None:
                decisions.append(admission_decision(profile))
                if profile.active_for_run: profiles.append(profile)
        if profiles: alias_index(profiles)
        if not profiles: self.blockers.append({"code":"P01_NO_ACTIVE_RESOLVED_SOURCE","owner":"OWNER","effect":"OFFICIAL_EXECUTION_BLOCKED"})
        self.state["profiles"]=profiles; self.state["source_decisions"]=decisions; return profiles
    def load_sources(self,input_root:Path):
        recordings=[]; inventories={}
        for profile in self.state.get("profiles",[]):
            cls=ADAPTERS.get(profile.adapter)
            if cls is None: self.blockers.append({"code":"P01_ADAPTER_UNKNOWN","dataset_id":profile.dataset_id,"adapter":profile.adapter,"owner":"BUILD_BOOK"}); continue
            adapter=cls(profile,input_root,self.work_root/"source_cache"/profile.dataset_id)
            try:
                files=adapter.resolve_files(); inventories[profile.dataset_id]=adapter.verify_files(files); recordings.extend(adapter.load(files))
            except Exception as exc: self.blockers.append({"code":"P01_SOURCE_LOAD_FAILED","dataset_id":profile.dataset_id,"message":str(exc),"owner":"OWNER_OR_ADAPTER"})
        self.state["recordings"]=recordings; self.state["inventories"]=inventories; return recordings
    def normalize_and_register(self):
        by_dataset={}; summaries={}
        for r in self.state["recordings"]: by_dataset.setdefault(r.dataset_id,[]).append(r)
        for profile in self.state.get("profiles",[]):
            recs=by_dataset.get(profile.dataset_id,[])
            if not recs: continue
            recs,summary=normalize_metadata(recs); summaries[profile.dataset_id]=summary; record=build_dataset_record(profile,self.state["inventories"][profile.dataset_id],summary,self.config_id); self.state["dataset_records"].append(record)
        self.state["metadata_summaries"]=summaries; self.state["records"].extend(self.state["dataset_records"])
    def labels(self):
        by_dataset={}; reports={}
        for r in self.state["recordings"]: by_dataset.setdefault(r.dataset_id,[]).append(r)
        label_profiles={p["dataset_id"]:p for p in self.config.get("labels",[])}
        for dataset,recs in by_dataset.items():
            if dataset not in label_profiles: self.blockers.append({"code":"P01_LABEL_PROFILE_MISSING","dataset_id":dataset,"owner":"OWNER"}); continue
            dataset_record_id=next((x["record_id"] for x in self.state["dataset_records"] if x["payload"]["dataset_id"]==dataset),None); record,report=build_label_map(dataset,recs,label_profiles[dataset],self.config_id,dataset_record_id); self.state["label_records"].append(record); reports[dataset]=report
            if report["status"]!="VALIDATED": self.blockers.append({"code":"P01_LABEL_COVERAGE_FAILED","dataset_id":dataset,"unknown":report["unknown"],"owner":"OWNER"})
        self.state["label_reports"]=reports; self.state["records"].extend(self.state["label_records"])
    def split_budget_preprocess(self):
        split_profile=self.config.get("split",{}); assignment,split_record=construct(self.state["recordings"],split_profile,self.config_id,[r["record_id"] for r in self.state["dataset_records"]]); self.state["assignment"]=assignment; self.state["split_record"]=split_record; self.state["records"].append(split_record)
        self.state["split_disjointness"]=validate_disjointness(self.state["recordings"],assignment,list(split_profile["group_keys"])); self.state["split_role_coverage"]=validate_role_coverage(assignment,list(split_profile["roles"]))
        event_rows=[]; label_by_dataset={r["payload"]["dataset_id"]:r for r in self.state["label_records"]}
        for rec in self.state["recordings"]:
            role=recording_role(rec,assignment,list(split_profile["group_keys"])); lr=label_by_dataset[rec.dataset_id]
            from .labels import map_event_label
            for e in rec.events: event_rows.append({"event_id":e.event_id,"dataset_id":rec.dataset_id,"subject_id":rec.subject_id,"session_id":rec.session_id,"run_id":rec.run_id,"role":role,"normalized_label":map_event_label(e.original_label,lr),"source_unit":f"{rec.dataset_id}:{rec.subject_id}:{rec.session_id}:{rec.run_id}"})
        self.state["event_rows"]=event_rows; budgets,budget_report=allocate(event_rows,self.config.get("budgets",{})); self.state["budgets"]=budgets; self.state["budget_report"]=budget_report
        split_record["payload"]["budget_ids"]=[b["budget_id"] for b in budgets]; split_record["payload"]["source_event_ids"]=sorted(r["event_id"] for r in event_rows)
        operations=compile_operations(self.config.get("preprocessing",{})); fit_roles=set(self.config["preprocessing"].get("fit_roles",["train"])); legal={row["source_unit"] for row in event_rows if row["role"] in fit_roles}; state=fit(self.state["recordings"],legal,operations)
        transformed=[]
        for rec in self.state["recordings"]:
            transformed.append(transform_recording(rec,operations,state))
        self.state["recordings"]=transformed; self.state["operations"]=operations
        preproc=build_preprocessing_record(self.config["preprocessing"],operations,state,[r["record_id"] for r in self.state["dataset_records"]]+[split_record["record_id"]],self.config_id,"derived_outputs/preprocessed/"); preproc["payload"]["split_record_id"]=split_record["record_id"]
        self.state["preprocessing_record"]=preproc; self.state["records"].append(preproc); self.state["fit_source_ids"]=state.source_ids
    def quality(self):
        summaries=[]
        for rec in self.state["recordings"]:
            dataset_record_id=next((x["record_id"] for x in self.state["dataset_records"] if x["payload"]["dataset_id"]==rec.dataset_id),None); rows,summary=annotate(rec,self.config.get("quality",{}),self.config_id,dataset_record_id); self.state["quality_records"].extend(rows); summaries.append(summary)
        self.state["quality_summaries"]=summaries; self.state["records"].extend(self.state["quality_records"])
    def windows(self):
        label_by_dataset={r["payload"]["dataset_id"]:r for r in self.state["label_records"]}; all_records=[]; all_index=[]
        for dataset in sorted(label_by_dataset):
            recs=[r for r in self.state["recordings"] if r.dataset_id==dataset]; dataset_record_id=next((x["record_id"] for x in self.state["dataset_records"] if x["payload"]["dataset_id"]==dataset),None); records,index=generate(recs,self.state["assignment"],list(self.config["split"]["group_keys"]),label_by_dataset[dataset],self.state["preprocessing_record"],self.config.get("windows",{}),self.config_id,self.bundle_root,self.state["split_record"],dataset_record_id); all_records.extend(records); all_index.extend(index)
        self.state["window_records"]=all_records; self.state["window_index"]=all_index; self.state["records"].extend(all_records)
        invalid=[]
        for path in sorted((self.bundle_root/"negative_and_failed_results").glob("invalid_windows_*.json")):
            invalid.extend(json.loads(path.read_text(encoding="utf-8")))
        self.state["invalid_windows"]=invalid
        self.state["window_report"]={"window_count":len(all_records),"event_count":len({r["event_id"] for r in all_index}),"invalid_window_count":len(invalid),"invalid_windows":invalid,"roles":sorted({r["role"] for r in all_index}),"duration_seconds":self.config.get("windows",{}).get("duration_seconds"),"stride_seconds":self.config.get("windows",{}).get("stride_seconds"),"overlap_group":"PARENT_EVENT"}
    def validation_and_leakage(self):
        schema_root=self.package_root/"schemas/phase_01/records"; errors,report=validate_records(self.state["records"],schema_root,self.config_id); self.state["validation_errors"]=errors; self.state["validation_report"]=report; self.state["records"].append(report)
        self.state["leakage"]=leakage_audit(self.state["recordings"],self.state["assignment"],list(self.config["split"]["group_keys"]),self.state["window_index"],self.state["fit_source_ids"],self.state["budgets"])
    def readiness_cards_manifests(self):
        by_type={}
        for r in self.state["records"]: by_type.setdefault(r["record_type"],[]).append(r)
        readiness=readiness_generate(by_type,"PASS" if not self.state["validation_errors"] else "FAIL",self.state["leakage"]["status"]); a14=prove_a14_absent([self.config],self.state["records"]); self.state["readiness"]=readiness; self.state["a14"]=a14
        write_json(self.bundle_root/"manifests/phase_01/layer1_ablation_readiness_l1_v1.json",{"rows":readiness,"a14_absence":a14})
        cards_root=self.bundle_root/"docs/cards"; cards_root.mkdir(parents=True,exist_ok=True)
        for dr in self.state["dataset_records"]:
            w=cards_root/"datasets"/f"{safe(dr['payload']['dataset_id'])}.md"; w.parent.mkdir(parents=True,exist_ok=True); w.write_text(dataset_card(dr,{"status":"PASS" if not self.state["validation_errors"] else "FAIL"}),encoding="utf-8")
        pc=cards_root/"protocols"/f"{safe(self.config['split']['protocol_id'])}.md"; pc.parent.mkdir(parents=True,exist_ok=True); pc.write_text(protocol_card(self.config['split']['protocol_id'],self.state['split_record'],self.state['preprocessing_record'],self.config['windows'],self.state['leakage']),encoding="utf-8")
        required_keys=["dataset_id","split_id","preprocessing_id","label_map_id","window_id","config_hash","seed"]
        self.state["matched_key_rows"]=[{"ablation_id":r["ablation_id"],"required_keys":"|".join(required_keys),"keys_complete":r["status"]=="FOUNDATION_READY","status":r["status"]} for r in readiness]
    def _gate_context(self):
        active=self.state.get("profiles",[]); quality=self.state.get("quality_summaries",[]); cards=list((self.bundle_root/"docs/cards").rglob("*.md"))
        return {
          "authority_phase0_intake":self.state.get("phase0_regression_status")=="PASS",
          "source_provenance_license":bool(active) and not any(b["code"].startswith("P01_SOURCE") for b in self.blockers) and all(self.state.get("inventories",{}).get(p.dataset_id,{}).get("count",0)>0 and self.state.get("inventories",{}).get(p.dataset_id,{}).get("checksum_status") in {"PROVIDER_VERIFIED_AND_AGGREGATE_FROZEN","COMPUTED_AND_FROZEN_FOR_RUN"} and bool(p.exact_revision and p.license and p.citation and p.official_reference and p.checksum_policy) for p in active),
          "schema_canonical_object":not self.state.get("validation_errors"),
          "metadata_completeness":bool(self.state.get("dataset_records")) and all(not r["payload"]["metadata_completeness"]["missing_count"] for r in self.state.get("dataset_records",[])),
          "label_mapping":bool(self.state.get("label_records")) and all(not r["payload"].get("unknown_labels") for r in self.state.get("label_records",[])),
          "preprocessing_fit_scope":bool(self.state.get("preprocessing_record")) and not any(i.get("code")=="P01_PREPROCESSING_FIT_LEAKAGE" for i in self.state.get("leakage",{}).get("issues",[])),
          "split_disjointness":self.state.get("split_disjointness",{}).get("status")=="PASS" and self.state.get("split_role_coverage",{}).get("status")=="PASS",
          "leakage_chronology":self.state.get("leakage",{}).get("status")=="PASS",
          "low_calibration_budgets":self.state.get("budget_report",{}).get("status")=="PASS",
          "window_identity":bool(self.state.get("window_records")) and self.state.get("window_report",{}).get("window_count",0)>0 and self.state.get("window_report",{}).get("invalid_window_count",0)==0,
          "quality_coverage":bool(quality) and len(quality)==len(self.state.get("recordings",[])) and all("quality_available" in x for x in quality) and sum(int(x.get("hard_invalid",0)) for x in quality)==0,
          "matched_keys_ablation_readiness":len(self.state.get("readiness",[]))==14 and self.state.get("a14",{}).get("status")=="PASS" and all(r["keys_complete"] for r in self.state.get("matched_key_rows",[])),
          "cards_limitations":len(cards)>=len(active)+1 and all(all(term in p.read_text(encoding="utf-8").lower() for term in ["public eeg","clinical","deployment"]) for p in cards),
          "manifest_path_hash_closure":self.state.get("manifest_closure_status"),
          "phase2_compatibility":self.state.get("p02_ready"),
          "complete_artifact_closure":self.state.get("artifact_closure_status"),
        }
    def gates(self):
        self.state["gate_context"]=self._gate_context(); self.state["gates"]=gate_evaluate(self.state["gate_context"]); return self.state["gates"]
    def persist_records(self):
        for r in self.state.get("records",[]):
            rt=r["record_type"]; rid=safe(r["record_id"])
            p=r.get("payload",{})
            if rt=="DatasetRecord": path=self.bundle_root/"records/datasets"/safe(p.get("dataset_id"))/f"{rid}.json"
            elif rt=="WindowRecord": path=self.bundle_root/"records/windows"/safe(p.get("dataset_id"))/safe(p.get("split_record_id"))/f"{rid}.json"
            elif rt=="SplitRecord": path=self.bundle_root/"records/splits"/safe(p.get("protocol_id"))/f"{rid}.json"
            elif rt=="PreprocessingRecord": path=self.bundle_root/"records/preprocessing"/safe(p.get("profile_id"))/f"{rid}.json"
            elif rt=="LabelMapRecord": path=self.bundle_root/"records/labels"/safe(p.get("dataset_id"))/f"{rid}.json"
            elif rt=="ArtifactFlagRecord": path=self.bundle_root/"records/quality"/safe(p.get("dataset_id",p.get("target_id","unknown").split(':')[0]))/f"{rid}.json"
            elif rt=="ValidationReport": path=self.bundle_root/"reports/phase_01/validation"/f"{rid}.json"
            else: path=self.bundle_root/"records/other"/f"{rid}.json"
            write_json(path,r)
    def persist_supporting_outputs(self):
        profiles={p.dataset_id:p for p in self.state.get("profiles",[])}
        source_rows=[]
        for raw in self.config.get("datasets",[]):
            p=profiles.get(raw.get("dataset_id")); inv=self.state.get("inventories",{}).get(raw.get("dataset_id"),{})
            source_rows.append({"dataset_id":raw.get("dataset_id"),"authority_status":raw.get("authority_status"),"active_for_run":raw.get("active_for_run"),"exact_revision":raw.get("exact_revision"),"citation":raw.get("citation"),"license":raw.get("license"),"access_method":raw.get("access_method"),"official_reference":raw.get("official_reference"),"published_checksum":raw.get("published_checksum"),"checksum_policy":raw.get("checksum_policy"),"observed_aggregate_sha256":inv.get("aggregate_sha256"),"checksum_status":inv.get("checksum_status","NOT_EXECUTED"),"redistribution_allowed":raw.get("redistribution_allowed")})
        write_json(self.bundle_root/"reports/phase_01/sources/source_version_license_report.json",{"sources":source_rows})
        decisions={x["dataset_id"]:x for x in self.state.get("source_decisions",[])}
        include_rows=[]
        for raw in self.config.get("datasets",[]):
            d=decisions.get(raw.get("dataset_id"),{}); include_rows.append({"dataset_id":raw.get("dataset_id"),"authority_status":raw.get("authority_status"),"active_for_run":raw.get("active_for_run"),"admitted":d.get("admitted",False),"reason":d.get("reason","UNRESOLVED_OR_INACTIVE")})
        write_csv(self.bundle_root/"reports/phase_01/sources/dataset_inclusion_exclusion.csv",include_rows,["dataset_id","authority_status","active_for_run","admitted","reason"])
        write_json(self.bundle_root/"reports/phase_01/metadata/metadata_completeness.json",self.state.get("metadata_summaries",{}))
        write_json(self.bundle_root/"reports/phase_01/labels/label_map_validation.json",self.state.get("label_reports",{}))
        write_json(self.bundle_root/"reports/phase_01/preprocessing/fit_scope.json",{"fit_scope":self.config.get("preprocessing",{}).get("fit_scope"),"fit_roles":self.config.get("preprocessing",{}).get("fit_roles"),"fit_source_ids":self.state.get("fit_source_ids",[]),"operations":self.state.get("operations",[])})
        write_json(self.bundle_root/"reports/phase_01/splits/disjointness.json",{"disjointness":self.state.get("split_disjointness",{}),"role_coverage":self.state.get("split_role_coverage",{})})
        write_json(self.bundle_root/"reports/phase_01/leakage/leakage_contamination.json",self.state.get("leakage",{}))
        budget_rows=[]
        for b in self.state.get("budgets",[]): budget_rows.append({"budget_id":b["budget_id"],"budget_per_class":b["budget_per_class"],"source_role":b["source_role"],"event_count":len(b["event_ids"]),"status":self.state.get("budget_report",{}).get("status")})
        write_csv(self.bundle_root/"reports/phase_01/splits/low_calibration_budgets.csv",budget_rows,["budget_id","budget_per_class","source_role","event_count","status"])
        write_json(self.bundle_root/"reports/phase_01/windows/window_timing_overlap.json",self.state.get("window_report",{}))
        write_json(self.bundle_root/"reports/phase_01/quality/quality_coverage.json",{"rows":self.state.get("quality_summaries",[]),"record_count":len(self.state.get("quality_records",[]))})
        write_csv(self.bundle_root/"reports/phase_01/readiness/matched_key_completeness.csv",self.state.get("matched_key_rows",[]),["ablation_id","required_keys","keys_complete","status"])
        neg=self.bundle_root/"reports/phase_01/negative/negative_and_diagnostic.jsonl"; neg.parent.mkdir(parents=True,exist_ok=True)
        rows=[]
        rows.extend({"type":"BLOCKER",**b} for b in self.blockers); rows.extend({"type":"VALIDATION_ERROR",**e} for e in self.state.get("validation_errors",[])); rows.extend({"type":"BUDGET_INSUFFICIENCY",**e} for e in self.state.get("budget_report",{}).get("insufficient",[]))
        neg.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rows),encoding='utf-8')
        test_report=self.state.get("phase0_regression_report",{"status":"NOT_RUN"}); write_json(self.bundle_root/"manifests/phase_01/test_manifest.json",test_report)
        write_json(self.bundle_root/"reports/phase_01/negative_and_failed_register.json",{"blockers":self.blockers,"validation_errors":self.state.get("validation_errors",[])})
        write_json(self.bundle_root/"reports/phase_01/runtime/resource_and_persistence_plan.json",{"resource_policy_id":"P01-L1-KAGGLE-ENV-FREEZE-R2","minimum_free_disk_gb":60,"recommended_free_disk_gb":90,"minimum_ram_gb":16,"recommended_ram_gb":30,"expected_wall_time_hours_upper_bound":9,"platform_guarantee":"NONE; IHARQ PREFLIGHT THRESHOLDS ONLY","cache_root":"source_cache/<dataset_id>","processing_order":["PhysioNetMI","BNCI2014_001","Lee2019_MI"],"checkpoint_policy":"CHECKPOINT_AFTER_EACH_DATASET_WITH_CONFIG_AND_SOURCE_HASHES","cache_eviction":"EVICT_ONLY_VERIFIED_PROVIDER_CACHE_COPIES_UNDER_DISK_PRESSURE","restartability":"RESUME_DATASET_LEVEL_ONLY_WHEN_CONFIG_AND_SOURCE_HASHES_MATCH","failed_run_preservation":"negative_and_failed_results/","session_loss_prevention":["PACKAGE_BUNDLE_BEFORE_SESSION_END","WRITE_CHECKSUMS","SAVE_EXECUTED_NOTEBOOK_AND_VERSION"]})
    def _artifact_references(self, record_types:list[str])->dict[str,list[dict[str,Any]]]:
        refs={t:[] for t in record_types}
        for r in self.state.get("records",[]):
            rt=r.get("record_type")
            if rt not in refs: continue
            rid=safe(r["record_id"]); payload=r.get("payload",{})
            candidates=list(self.bundle_root.rglob(f"{rid}.json"))
            path=candidates[0].relative_to(self.bundle_root).as_posix() if candidates else None
            refs[rt].append({"record_id":r["record_id"],"path":path,"semantic_hash":r.get("semantic_hash"),"lifecycle_status":r.get("lifecycle_status"),"source_ids":r.get("source_ids",[])})
        return refs

    def p02_handoff(self):
        required=["DatasetRecord","WindowRecord","SplitRecord","PreprocessingRecord","LabelMapRecord","ValidationReport"]
        refs=self._artifact_references(required); complete=all(refs[t] for t in required) and self.state.get("leakage",{}).get("status")=="PASS" and self.state.get("split_role_coverage",{}).get("status")=="PASS"
        readiness_path="manifests/phase_01/layer1_ablation_readiness_l1_v1.json"
        handoff={"handoff_id":f"P01-TO-P02-{self.config_id[:12]}","status":"READY" if complete else "BLOCKED","artifact_references":refs,"quality_record_references":self._artifact_references(["ArtifactFlagRecord"])["ArtifactFlagRecord"],"dataset_cards":[p.relative_to(self.bundle_root).as_posix() for p in (self.bundle_root/"docs/cards/datasets").glob("*.md")],"protocol_cards":[p.relative_to(self.bundle_root).as_posix() for p in (self.bundle_root/"docs/cards/protocols").glob("*.md")],"readiness_artifact":readiness_path,"environment_manifest":"environment_manifest.json","notebook_manifest":"notebook_manifest.json","config_snapshot":"config_snapshot/","gate_decision":"manifests/phase_01/gate_decision.json","source_and_config_ids":{"config_id":self.config_id,"dataset_record_ids":[r["record_id"] for r in self.state.get("dataset_records",[])],"split_record_id":self.state.get("split_record",{}).get("record_id"),"preprocessing_record_id":self.state.get("preprocessing_record",{}).get("record_id"),"label_map_record_ids":[r["record_id"] for r in self.state.get("label_records",[])]},"matching_keys":["dataset_id","split_record_id","preprocessing_record_id","label_map_record_id","window_id","config_id","seed"],"validation_summary":{"schema_errors":len(self.state.get("validation_errors",[])),"leakage_status":self.state.get("leakage",{}).get("status"),"role_coverage":self.state.get("split_role_coverage",{}).get("status")},"limitations":["PUBLIC_EEG_ONLY","NON_CLINICAL","NO_DEPLOYMENT_CLAIM"],"unresolved_exclusions":[b for b in self.blockers],"invalidation_triggers":["DATASET_REVISION_CHANGE","SOURCE_CHECKSUM_CHANGE","SPLIT_ID_CHANGE","PREPROCESSING_ID_CHANGE","LABEL_MAP_CHANGE","WINDOW_PROFILE_CHANGE","VALIDATION_FAILURE","LEAKAGE_FAILURE"],"consumer_validation":["VERIFY_ALL_REFERENCED_PATHS_AND_HASHES","REQUIRE_ALL_P01_GATES_PASS","REJECT_CHANGED_IDENTITY_WITHOUT_INVALIDATION"]}
        data=yaml.safe_dump(handoff,sort_keys=False); path=self.bundle_root/"handoffs/phase_01_to_phase_02.yaml"; path.parent.mkdir(parents=True,exist_ok=True); path.write_text(data,encoding="utf-8"); (self.bundle_root/"phase2_handoff/phase_01_to_phase_02.yaml").write_text(data,encoding="utf-8"); self.state["p02_handoff"]=handoff; self.state["p02_ready"]=complete; return complete
    def write_downstream_handoffs(self):
        record_refs=self._artifact_references(["DatasetRecord","WindowRecord","SplitRecord","PreprocessingRecord","LabelMapRecord","ArtifactFlagRecord","ValidationReport"])
        base={"phase_id":"P01","config_id":self.config_id,"official_execution_status":"ACCEPTED" if self.state.get("p02_ready") else "BLOCKED","gate_decision":"manifests/phase_01/gate_decision.json","record_references":record_refs,"readiness_artifact":"manifests/phase_01/layer1_ablation_readiness_l1_v1.json","negative_register":"reports/phase_01/negative/negative_and_diagnostic.jsonl","limitations":["PUBLIC_EEG_ONLY","NON_CLINICAL","NO_DEPLOYMENT_CLAIM"]}
        later={
          "L2":{"required":["DatasetRecord","SplitRecord","PreprocessingRecord","LabelMapRecord","WindowRecord","ValidationReport"],"keys":["dataset_id","split_record_id","preprocessing_record_id","label_map_record_id","window_id"]},
          "L3":{"required":["SplitRecord","PreprocessingRecord","WindowRecord","ValidationReport"],"keys":["split_record_id","preprocessing_record_id","window_id"]},
          "L4":{"required":["WindowRecord","ValidationReport","AblationReadiness"],"keys":["window_id","config_id"]},
          "L5":{"required":["WindowRecord","SplitRecord","ValidationReport"],"keys":["window_id","split_record_id"]},
          "L6":{"required":["AblationReadiness","ValidationReport"],"keys":["config_id","seed"]},
          "L7":{"required":["AblationReadiness","ValidationReport"],"keys":["config_id","seed"]},
          "L8":{"required":["DatasetRecord","WindowRecord","ArtifactFlagRecord","ValidationReport"],"keys":["dataset_id","window_id"]},
          "L9":{"required":["AblationReadiness","ValidationReport"],"keys":["config_id"]}}
        files={
          "protocol_v1_handoff/p01_protocol_v1_inputs.yaml":{**base,"protocol_v1_created":False,"executed_notebook":"notebook_manifest.json","environment":"environment_manifest.json","source_inventory":"inputs/source_inventory.json","config_snapshot":"config_snapshot/","gate_statuses":"manifests/phase_01/gate_decision.json","failed_attempts":"negative_and_failed_results/"},
          "analysis_inputs/p01_analysis_input_manifest.yaml":{**base,"phase_analysis_created":False,"analysis_release_inputs":["records/","reports/phase_01/","manifests/phase_01/","negative_and_failed_results/","table_source_data/","figure_source_data/"]},
          "layer0_handoff/p01_layer0_candidate_claim_handoff.yaml":{**base,"layer0_applied":False,"candidate_claims":[],"evidence_sufficiency_field":"gate_decision.status","warning_candidates":["PUBLIC_EEG_ONLY","NON_CLINICAL","NO_DEPLOYMENT_CLAIM"],"source_links":["manifests/phase_01/layer1_manifest.json","checksums.sha256"],"claim_boundary":"NO_CLAIM_APPROVAL_IN_P01_RUNTIME"},
          "evidence_map_handoff/p01_evidence_map_source_handoff.yaml":{**base,"evidence_map_updated":False,"source_identifiers":{"bundle_id":self.bundle_root.name,"config_id":self.config_id,"record_ids":[r["record_id"] for r in self.state.get("records",[])],"gate_ids":[g["gate_id"] for g in self.state.get("gates",[])]},"evidence_paths":["records/","reports/phase_01/","manifests/phase_01/","checksums.sha256"]},
          "layer10_source_bundle/p01_layer10_source_manifest.yaml":{**base,"layer10_applied":False,"read_only":True,"cards":[p.relative_to(self.bundle_root).as_posix() for p in (self.bundle_root/"docs/cards").rglob("*.md")],"source_surfaces":["docs/cards/","reports/phase_01/","manifests/phase_01/","checksums.sha256"],"recomputation_allowed":False},
          "handoffs/p01_later_layer_dependency_map.yaml":{**base,"later_layer_dependencies":later}}
        for rel,obj in files.items(): p=self.bundle_root/rel; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(yaml.safe_dump(obj,sort_keys=False),encoding='utf-8')

    def expected_artifact_status(self):
        checks={
          "DatasetRecord":bool(list((self.bundle_root/"records/datasets").rglob("*.json"))),"WindowRecord":bool(list((self.bundle_root/"records/windows").rglob("*.json"))),"SplitRecord":bool(list((self.bundle_root/"records/splits").rglob("*.json"))),"PreprocessingRecord":bool(list((self.bundle_root/"records/preprocessing").rglob("*.json"))),"LabelMapRecord":bool(list((self.bundle_root/"records/labels").rglob("*.json"))),"ValidationReport":bool(list((self.bundle_root/"reports/phase_01/validation").rglob("*.json"))),
          "Layer1Manifest":True,"DatasetCard":bool(list((self.bundle_root/"docs/cards/datasets").glob("*.md"))),"ProtocolCard":bool(list((self.bundle_root/"docs/cards/protocols").glob("*.md"))),"AblationReadiness":(self.bundle_root/"manifests/phase_01/layer1_ablation_readiness_l1_v1.json").exists(),
        }
        supporting=["reports/phase_01/sources/source_version_license_report.json","reports/phase_01/sources/dataset_inclusion_exclusion.csv","reports/phase_01/metadata/metadata_completeness.json","reports/phase_01/labels/label_map_validation.json","reports/phase_01/preprocessing/fit_scope.json","reports/phase_01/splits/disjointness.json","reports/phase_01/leakage/leakage_contamination.json","reports/phase_01/splits/low_calibration_budgets.csv","reports/phase_01/windows/window_timing_overlap.json","reports/phase_01/quality/quality_coverage.json","reports/phase_01/readiness/matched_key_completeness.csv","reports/phase_01/negative/negative_and_diagnostic.jsonl","manifests/phase_01/test_manifest.json","manifests/phase_01/gate_decision.json","handoffs/phase_01_to_phase_02.yaml","manifests/phase_01/execution_bundle_manifest.json","reports/phase_01/runtime/resource_and_persistence_plan.json","handoffs/p01_later_layer_dependency_map.yaml"]
        for rel in supporting: checks[rel]=(self.bundle_root/rel).exists()
        # ArtifactFlagRecord is conditional; explicit quality coverage is mandatory instead.
        checks["ArtifactFlagRecord_where_supported"]=True
        return checks
    def _prior_stage_failures(self):
        # Section 23 is preliminary and may mirror already-governed blockers. Sections 24-26 are finalization obligations and must pass.
        return [r for r in self.state.get("stage_results",[]) if r.get("stage") != "23" and r.get("status")!="PASS"]

    def _write_gate_surfaces(self,decision):
        write_json(self.bundle_root/"gate_decision.json",decision)
        write_json(self.bundle_root/"manifests/phase_01/gate_decision.json",decision)
        for gate in decision["gates"]: write_json(self.bundle_root/f"manifests/phase_01/gates/{gate['gate_id']}.json",gate)
        handoff={"phase_id":"P01","execution_status":decision["status"],"bundle_id":self.bundle_root.name,"config_id":self.config_id,"record_count":len(self.state.get("records",[])),"gate_decision":"manifests/phase_01/gate_decision.json","protocol_v1_created":False,"phase_analysis_created":False,"layer0_applied":False,"evidence_map_updated":False,"layer10_applied":False,"exact_next_step":"Resolve blockers and rerun" if decision["status"]!="ACCEPTED" else "Create Protocol v1.0 Phase 1 annex"}
        (self.bundle_root/"phase_execution_handoff.yaml").write_text(yaml.safe_dump(handoff,sort_keys=False),encoding="utf-8")

    def evaluate_evidence_sufficiency(self):
        self.persist_records(); self.persist_supporting_outputs(); self.p02_handoff(); snapshot_runtime(self.package_root,self.bundle_root); create_integration_patch_manifest(self.package_root,self.bundle_root); self.write_downstream_handoffs()
        self.state["artifact_closure_status"]=all(v for k,v in self.expected_artifact_status().items() if k not in {"manifests/phase_01/execution_bundle_manifest.json","manifests/phase_01/gate_decision.json","Layer1Manifest"})
        self.state["manifest_closure_status"]=self.state["artifact_closure_status"]
        gates=gate_evaluate(self._gate_context()); stage_failures=self._prior_stage_failures()
        accepted=all(g["status"]=="PASS" for g in gates) and not self.blockers and not stage_failures
        decision={"phase_id":"P01","status":"ACCEPTED" if accepted else "BLOCKED","gates":gates,"blockers":self.blockers,"stage_failures":stage_failures,"limitations":["PUBLIC_EEG_ONLY","NON_CLINICAL","NO_DEPLOYMENT_CLAIM"],"evaluation":"PRE_EXPORT_EVIDENCE_SUFFICIENCY"}
        self.state["gates"]=gates; self.state["preliminary_decision"]=decision
        write_json(self.bundle_root/"reports/phase_01/preliminary_gate_evaluation.json",decision)
        return decision

    def prepare_final_artifacts(self):
        # All 27 section outcomes already exist when this method is called from Section 26. Freeze bytes only after full-stage evidence is materialized.
        self.persist_records(); self.persist_supporting_outputs(); self.p02_handoff(); snapshot_runtime(self.package_root,self.bundle_root); create_integration_patch_manifest(self.package_root,self.bundle_root); self.write_downstream_handoffs()
        stages=self.state.get("stage_results",[])
        write_json(self.bundle_root/"reports/phase_01/tests/stage_results.json",{"stage_count":len(stages),"expected_stages":[f"{i:02d}" for i in range(27)],"stages":stages})
        self.state["artifact_closure_status"]=all(v for k,v in self.expected_artifact_status().items() if k not in {"manifests/phase_01/execution_bundle_manifest.json","manifests/phase_01/gate_decision.json","Layer1Manifest"})
        self.state["manifest_closure_status"]=self.state["artifact_closure_status"]
        gates=gate_evaluate(self._gate_context()); stage_failures=self._prior_stage_failures()
        complete_stage_identity=[r.get("stage") for r in stages]==[f"{i:02d}" for i in range(27)]
        if not complete_stage_identity:
            self.blockers.append({"code":"P01_STAGE_IDENTITY_INCOMPLETE","observed":[r.get("stage") for r in stages],"owner":"L1_PACKAGING"})
        accepted=all(g["status"]=="PASS" for g in gates) and not self.blockers and not stage_failures and complete_stage_identity
        decision={"phase_id":"P01","status":"ACCEPTED" if accepted else "BLOCKED","gates":gates,"blockers":self.blockers,"stage_failures":stage_failures,"complete_stage_identity":complete_stage_identity,"limitations":["PUBLIC_EEG_ONLY","NON_CLINICAL","NO_DEPLOYMENT_CLAIM"],"evaluation":"FINAL_AFTER_ALL_27_SECTIONS_BEFORE_EXTERNAL_ZIP"}
        self.state["gates"]=gates; self._write_gate_surfaces(decision)
        final_register={"register_status":"FINAL","phase_id":"P01","run_id":self.bundle_root.name,"decision":decision["status"],"blockers":self.blockers,"stage_failures":stage_failures,"stages":stages}
        write_json(self.bundle_root/"negative_and_failed_results/run_failures_and_blockers.json",final_register)
        write_json(self.bundle_root/"reports/phase_01/final_run_summary.json",{"phase":"P01","layer":"L1","notebook_revision":"R6","config_id":self.config_id,"decision":decision["status"],"stage_count":len(stages),"gate_count":len(gates),"blocker_count":len(self.blockers),"external_zip_hash_boundary":"The execution ZIP SHA-256 is emitted as a detached sidecar after ZIP creation."})
        layer1=build_layer1_manifest(self.bundle_root,self.state.get("records",[]),gates,"manifests/phase_01/layer1_ablation_readiness_l1_v1.json","handoffs/phase_01_to_phase_02.yaml",self.config_id)
        write_json(self.bundle_root/"manifests/phase_01/layer1_manifest.json",layer1)
        entries=build_file_manifest(self.bundle_root,exclude={"checksums.sha256","manifests/phase_01/execution_bundle_manifest.json"})
        execution_manifest={"manifest_id":f"P01-EXECUTION-BUNDLE-R6-{self.config_id[:12]}","entries":entries,"file_count":len(entries),"gate_status":decision["status"],"stage_count":len(stages),"excluded_self":"manifests/phase_01/execution_bundle_manifest.json","checksum_surface":"checksums.sha256"}
        write_json(self.bundle_root/"manifests/phase_01/execution_bundle_manifest.json",execution_manifest)
        write_checksums(self.bundle_root,self.bundle_root/"checksums.sha256")
        manifest_check=verify_execution_manifest(self.bundle_root,self.bundle_root/"manifests/phase_01/execution_bundle_manifest.json")
        checksum_check=verify_checksums(self.bundle_root,self.bundle_root/"checksums.sha256")
        closure={"execution_manifest":manifest_check,"checksums":checksum_check,"stage_count":len(stages),"status":"PASS" if manifest_check["status"]==checksum_check["status"]=="PASS" and len(stages)==27 else "FAIL"}
        write_json(self.work_root/"final_manifest_closure_verification.json",closure)
        if closure["status"]!="PASS": raise RuntimeError(f"final manifest/hash closure failed: {closure}")
        self.state["decision"]=decision; self.state["prepared"]=True; self.state["final_manifest_closure"]=closure
        return decision

    def package_bundle(self):
        if not self.state.get("prepared"): self.prepare_final_artifacts()
        zip_path=self.work_root/f"{self.bundle_root.name}.zip"; package=finalize(self.bundle_root,zip_path); self.state["package"]=package; return package
