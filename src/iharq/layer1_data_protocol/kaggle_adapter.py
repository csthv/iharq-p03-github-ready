from __future__ import annotations
from pathlib import Path
import json, os, platform, sys, subprocess, shutil, yaml, hashlib, importlib.metadata as md
from .models import StageResult
from .pipeline import Layer1Pipeline

PROHIBITED={"TBD","TODO","UNKNOWN","UNRESOLVED","ACCESS_UNRESOLVED","OWNER_DECISION_REQUIRED","DEFERRED","PLACEHOLDER","TO_BE_DECIDED"}

def _zero_unresolved(config):
    findings=[]
    def walk(v,path="",active=True):
        if isinstance(v,dict):
            local_active=active and v.get("active_for_run",True) is not False
            for k,x in v.items(): walk(x,f"{path}.{k}" if path else k,local_active)
        elif isinstance(v,list):
            for i,x in enumerate(v): walk(x,f"{path}[{i}]",active)
        elif active:
            if v is None: findings.append({"path":path,"value":None})
            elif isinstance(v,str) and (v.strip() in PROHIBITED or any(t in v.upper() for t in ["ACCESS_UNRESOLVED","OWNER_DECISION_REQUIRED"])): findings.append({"path":path,"value":v})
    walk(config)
    return findings

class StageRunner:
    def __init__(self,package_root:Path,work_root:Path,input_root:Path,config_path:Path):
        self.package_root=Path(package_root); self.work_root=Path(work_root); self.input_root=Path(input_root); self.config_path=Path(config_path); self.work_root.mkdir(parents=True,exist_ok=True)
        self.config=yaml.safe_load(self.config_path.read_text(encoding="utf-8")); self.pipeline=Layer1Pipeline(self.package_root,self.work_root,self.config); self.results=[]
    def _record(self,stage,status,outputs=None,observations=None,blockers=None):
        effective=list(blockers or [])
        if status in {"FAIL","BLOCKED"} and not effective:
            effective=[{"code":f"P01_STAGE_{stage}_{status}","owner":"BUILD_BOOK_OR_EXTERNAL_RUNTIME","stage":stage}]
        for blocker in effective:
            if blocker not in self.pipeline.blockers: self.pipeline.blockers.append(blocker)
        result=StageResult(stage,status,outputs or [],observations or {},effective); self.results.append(result)
        self.pipeline.state.setdefault("stage_results",[]).append(result.__dict__)
        path=self.work_root/"stage_status"/f"{stage}.json"; path.parent.mkdir(parents=True,exist_ok=True); path.write_text(json.dumps(result.__dict__,indent=2),encoding="utf-8"); return result
    def run_stage(self,stage:str): return getattr(self,f"stage_{stage}")()
    def stage_00(self):
        control={"phase":"P01","layer":"L1","package_root_class":"KAGGLE_INPUT_BUNDLE_R6","config_path":"configs/phase_01/phase01_layer1_resolved_R6.yaml","notebook_revision":"R6","build_book":"IHARQ-IBB-R10-P01-L1-INDEPENDENT-AUDIT-REPAIRED","annex":"IHARQ-IBB-P01-L1-ANNEX-R4","freeze":"P01-L1-OFFICIAL-RUN-FREEZE-R2"}
        (self.pipeline.bundle_root/"authority_manifest.json").write_text(json.dumps(control,indent=2),encoding='utf-8'); return self._record("00","PASS",["authority_manifest.json"],control)
    def stage_01(self):
        disk=shutil.disk_usage(self.work_root)
        try:
            import psutil; ram_bytes=psutil.virtual_memory().total
        except Exception: ram_bytes=None
        pins=self.config["environment"]["packages"]; installed={}
        for package,expected in pins.items():
            try: installed[package]=md.version(package.replace('_','-'))
            except Exception: installed[package]="MISSING"
        mismatches={k:{"expected":str(v),"observed":installed[k]} for k,v in pins.items() if installed[k]!=str(v)}
        official_kaggle=Path('/kaggle/working').exists(); resource_fail=[]
        if official_kaggle and disk.free < int(self.config['environment']['resources']['minimum_free_disk_gb'])*1024**3: resource_fail.append("FREE_DISK_BELOW_60_GB")
        env={"python":sys.version,"platform":platform.platform(),"cpu_count":os.cpu_count(),"ram_bytes":ram_bytes,"disk_total_bytes":disk.total,"disk_free_bytes":disk.free,"official_kaggle":official_kaggle,"installed_packages":installed,"pin_mismatches":mismatches,"resource_failures":resource_fail,"deterministic_environment":self.config['environment']['deterministic_environment']}
        (self.pipeline.bundle_root/"environment_manifest.json").write_text(json.dumps(env,indent=2),encoding="utf-8")
        python_expected=str(self.config["environment"]["python"]["required_major_minor"]); python_observed=f"{sys.version_info.major}.{sys.version_info.minor}"
        required_imports=["moabb","mne","pymatreader","mne_bids","pyriemann","edfio","filelock","pooch"]
        import_failures=[]
        for name in required_imports:
            try: __import__(name)
            except Exception as exc: import_failures.append({"module":name,"error":str(exc)})
        blockers=[{"code":"P01_ENVIRONMENT_PIN_MISMATCH","details":mismatches,"owner":"KAGGLE_ENVIRONMENT"}] if mismatches else []
        if python_observed!=python_expected: blockers.append({"code":"P01_PYTHON_VERSION_MISMATCH","expected":python_expected,"observed":python_observed,"owner":"KAGGLE_ENVIRONMENT"})
        if import_failures: blockers.append({"code":"P01_MOABB_DEPENDENCY_GRAPH_INCOMPLETE","details":import_failures,"owner":"KAGGLE_ENVIRONMENT"})
        env["python_required_major_minor"]=python_expected; env["python_observed_major_minor"]=python_observed; env["required_import_failures"]=import_failures
        blockers += [{"code":x,"owner":"KAGGLE_RUNTIME"} for x in resource_fail]
        self.pipeline.blockers.extend(blockers); return self._record("01","PASS" if not blockers else "BLOCKED",["environment_manifest.json"],env,blockers)
    def stage_02(self):
        required=["src/iharq","schemas","configs/phase_01/phase01_layer1_resolved_R6.yaml","contracts","implementation_authority/current_r10_r4","manifests/authority_manifest.yaml","tests"]
        missing=[x for x in required if not (self.package_root/x).exists()]; blockers=[{"code":"P01_INPUT_BUNDLE_INCOMPLETE","path":x,"owner":"BUILD_BOOK"} for x in missing]
        self.pipeline.blockers.extend(blockers); return self._record("02","PASS" if not missing else "FAIL",observations={"missing":missing},blockers=blockers)
    def stage_03(self):
        unresolved=_zero_unresolved(self.config); active=[x['dataset_id'] for x in self.config['datasets'] if x['active_for_run']]
        expected=["PhysioNetMI","BNCI2014_001","Lee2019_MI"]; blockers=[]
        if unresolved: blockers.append({"code":"P01_CONFIG_UNRESOLVED","fields":unresolved,"owner":"BUILD_BOOK"})
        if active!=expected: blockers.append({"code":"P01_ACTIVE_SOURCE_FREEZE_DRIFT","observed":active,"expected":expected,"owner":"BUILD_BOOK"})
        self.pipeline.blockers.extend(blockers); manifest={"config_id":self.pipeline.config_id,"freeze_id":self.config['freeze_id'],"active_sources":active,"unresolved":unresolved}
        p=self.pipeline.bundle_root/"config_snapshot"/"official_run_freeze_manifest.json"; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(manifest,indent=2),encoding='utf-8')
        return self._record("03","PASS" if not blockers else "FAIL",[str(p.relative_to(self.pipeline.bundle_root))],manifest,blockers)
    def stage_04(self):
        report_path=self.pipeline.bundle_root/"reports/phase_01/tests/phase0_and_runtime_regression.json"; report_path.parent.mkdir(parents=True,exist_ok=True)
        env=dict(os.environ); env["PYTHONPATH"]=str(self.package_root/"src")+(os.pathsep+env["PYTHONPATH"] if env.get("PYTHONPATH") else "")
        proc=subprocess.run([sys.executable,"-m","pytest","-q","tests"],cwd=self.package_root,env=env,text=True,capture_output=True)
        a14="A14" not in json.dumps(self.config); status="PASS" if proc.returncode==0 and a14 else "FAIL"; report={"status":status,"returncode":proc.returncode,"stdout":proc.stdout,"stderr":proc.stderr,"a14_absent":a14}
        report_path.write_text(json.dumps(report,indent=2),encoding='utf-8'); self.pipeline.state["phase0_regression_status"]=status; self.pipeline.state["phase0_regression_report"]=report
        blockers=[] if status=="PASS" else [{"code":"P01_PHASE0_REGRESSION_FAILED","owner":"BUILD_BOOK","returncode":proc.returncode}]; self.pipeline.blockers.extend(blockers)
        return self._record("04",status,[str(report_path.relative_to(self.pipeline.bundle_root))],{"a14_absent":a14,"pytest_returncode":proc.returncode,"summary":proc.stdout.splitlines()[-1:]},blockers)
    def stage_05(self):
        profiles=self.pipeline.resolve_sources(); blockers=[b for b in self.pipeline.blockers if b['code'].startswith('P01_SOURCE') or b['code'].startswith('P01_ADAPTER')]
        return self._record("05","PASS" if len(profiles)==3 and not blockers else "BLOCKED",observations={"resolved_active_sources":[p.dataset_id for p in profiles],"adapters":{p.dataset_id:p.adapter for p in profiles}},blockers=blockers)
    def stage_06(self): return self._record("06","PASS" if len(self.pipeline.state.get("profiles",[]))==3 else "BLOCKED",observations={"admission_decisions":self.pipeline.state.get("source_decisions",[])},blockers=self.pipeline.blockers)
    def stage_07(self):
        if not self.pipeline.state.get("profiles"): return self._record("07","BLOCKED",blockers=self.pipeline.blockers)
        recs=self.pipeline.load_sources(self.input_root); expected={"PhysioNetMI","BNCI2014_001","Lee2019_MI"}; observed={r.dataset_id for r in recs}
        status="PASS" if expected==observed and all(self.pipeline.state.get('inventories',{}).get(x,{}).get('checksum_status') in {'PROVIDER_VERIFIED_AND_AGGREGATE_FROZEN','COMPUTED_AND_FROZEN_FOR_RUN'} for x in expected) else "BLOCKED"
        return self._record("07",status,observations={"recordings":len(recs),"datasets":sorted(observed),"inventories":self.pipeline.state.get("inventories",{})},blockers=self.pipeline.blockers)
    def stage_08(self):
        if not self.pipeline.state.get("recordings"): return self._record("08","BLOCKED",blockers=self.pipeline.blockers)
        self.pipeline.normalize_and_register(); return self._record("08","PASS",observations={"dataset_records":len(self.pipeline.state["dataset_records"]),"summaries":self.pipeline.state.get("metadata_summaries",{})})
    def stage_09(self):
        if not self.pipeline.state.get("dataset_records"): return self._record("09","BLOCKED",blockers=self.pipeline.blockers)
        self.pipeline.labels(); failed=any(b["code"]=="P01_LABEL_COVERAGE_FAILED" for b in self.pipeline.blockers); return self._record("09","FAIL" if failed else "PASS",observations={"label_records":len(self.pipeline.state["label_records"]),"reports":self.pipeline.state.get("label_reports",{})},blockers=self.pipeline.blockers)
    def stage_10(self):
        try:
            from .preprocessing import compile_operations; ops=compile_operations(self.config["preprocessing"]); return self._record("10","PASS",observations={"operations":ops,"freeze":self.config['preprocessing']['profile_id']})
        except Exception as exc:
            blocker={"code":"P01_PREPROCESSING_FREEZE_INVALID","message":str(exc),"owner":"BUILD_BOOK"}
            return self._record("10","FAIL",blockers=[blocker])
    def stage_11(self):
        if not self.pipeline.state.get("recordings"): return self._record("11","BLOCKED",blockers=self.pipeline.blockers)
        try:
            self.pipeline.split_budget_preprocess(); ok=self.pipeline.state["split_disjointness"]["status"]=="PASS" and self.pipeline.state["split_role_coverage"]["status"]=="PASS"; return self._record("11","PASS" if ok else "FAIL",observations={"split_record":self.pipeline.state["split_record"]["record_id"],"disjointness":self.pipeline.state["split_disjointness"],"role_coverage":self.pipeline.state["split_role_coverage"]})
        except Exception as exc:
            b={"code":"P01_SPLIT_OR_PREPROCESS_FAILED","message":str(exc),"owner":"BUILD_BOOK_OR_EXTERNAL_BYTES"}; self.pipeline.blockers.append(b); return self._record("11","BLOCKED",blockers=self.pipeline.blockers)
    def stage_12(self): return self._record("12","PASS" if self.pipeline.state.get("budget_report",{}).get("status") in {"PASS","DIAGNOSTIC_ONLY"} else "BLOCKED",observations=self.pipeline.state.get("budget_report",{}),blockers=self.pipeline.blockers)
    def stage_13(self): return self._record("13","PASS" if self.pipeline.state.get("preprocessing_record") else "BLOCKED",observations={"preprocessing_record":self.pipeline.state.get("preprocessing_record",{}).get("record_id")})
    def stage_14(self):
        if not self.pipeline.state.get("preprocessing_record"): return self._record("14","BLOCKED",blockers=self.pipeline.blockers)
        self.pipeline.quality(); hard=sum(x.get('hard_invalid',0) for x in self.pipeline.state.get('quality_summaries',[]))
        blockers=[] if hard==0 else [{"code":"P01_QUALITY_HARD_INVALID","hard_invalid":hard,"owner":"L1_QUALITY_OR_SOURCE_BYTES"}]
        return self._record("14","PASS" if hard==0 else "FAIL",observations={"quality_records":len(self.pipeline.state["quality_records"]),"hard_invalid":hard,"coverage":self.pipeline.state.get("quality_summaries",[])},blockers=blockers)
    def stage_15(self):
        if not self.pipeline.state.get("preprocessing_record"): return self._record("15","BLOCKED",blockers=self.pipeline.blockers)
        try:
            self.pipeline.windows(); invalid=int(self.pipeline.state.get("window_report",{}).get("invalid_window_count",0))
            blockers=[] if self.pipeline.state["window_records"] and invalid==0 else [{"code":"P01_WINDOW_INVALID_OR_MISSING","invalid_window_count":invalid,"owner":"L1_WINDOWS_OR_SOURCE_BYTES"}]
            return self._record("15","PASS" if not blockers else "FAIL",observations=self.pipeline.state.get("window_report",{}),blockers=blockers)
        except Exception as exc: b={"code":"P01_WINDOW_GENERATION_FAILED","message":str(exc),"owner":"BUILD_BOOK_OR_SOURCE_BYTES"}; self.pipeline.blockers.append(b); return self._record("15","BLOCKED",blockers=self.pipeline.blockers)
    def stage_16(self):
        if not self.pipeline.state.get("window_records"): return self._record("16","BLOCKED",blockers=self.pipeline.blockers)
        self.pipeline.validation_and_leakage(); return self._record("16","PASS" if not self.pipeline.state["validation_errors"] else "FAIL",observations={"errors":len(self.pipeline.state["validation_errors"])})
    def stage_17(self): return self._record("17",self.pipeline.state.get("leakage",{}).get("status","BLOCKED"),observations=self.pipeline.state.get("leakage",{}),blockers=self.pipeline.blockers)
    def stage_18(self):
        if "leakage" not in self.pipeline.state: return self._record("18","BLOCKED",blockers=self.pipeline.blockers)
        self.pipeline.readiness_cards_manifests(); ok=len(self.pipeline.state["readiness"])==14 and self.pipeline.state["a14"]["status"]=="PASS"; return self._record("18","PASS" if ok else "FAIL",observations={"rows":len(self.pipeline.state["readiness"]),"a14":self.pipeline.state["a14"]})
    def stage_19(self): return self._record("19","PASS" if list((self.pipeline.bundle_root/"docs/cards").rglob("*.md")) else "BLOCKED")
    def stage_20(self): return self._record("20","PASS" if (self.pipeline.bundle_root/"manifests/phase_01/layer1_ablation_readiness_l1_v1.json").exists() else "BLOCKED")
    def stage_21(self):
        path=self.pipeline.bundle_root/"negative_and_failed_results/run_failures_and_blockers.json"; path.parent.mkdir(parents=True,exist_ok=True)
        snapshot={"register_status":"INTERIM_BEFORE_FINAL_EXPORT","blockers":self.pipeline.blockers,"stages":[r.__dict__ for r in self.results]}
        path.write_text(json.dumps(snapshot,indent=2),encoding="utf-8")
        return self._record("21","PASS",[str(path.relative_to(self.pipeline.bundle_root))],{"register_status":"INTERIM; FINALIZED_AFTER_STAGE_26"})
    def stage_22(self):
        required=["DatasetRecord","WindowRecord","SplitRecord","PreprocessingRecord","LabelMapRecord","ValidationReport"]; available={t:any(r.get("record_type")==t for r in self.pipeline.state.get("records",[])) for t in required}
        return self._record("22","PASS" if all(available.values()) else "BLOCKED",observations={"required_consumer_artifacts":available,"later_layers":["L2","L3","L4","L5","L6","L7","L8","L9"]},blockers=self.pipeline.blockers)
    def stage_23(self):
        decision=self.pipeline.evaluate_evidence_sufficiency(); return self._record("23","PASS" if decision["status"]=="ACCEPTED" else "BLOCKED",["reports/phase_01/preliminary_gate_evaluation.json"],{"pre_export_decision":decision},self.pipeline.blockers)
    def stage_24(self):
        repair={"failed_bundle_preserved":True,"defect_owners":sorted({b.get("owner","BUILD_BOOK") for b in self.pipeline.blockers}),"minimum_repair":"Repair only the external failure or affected governed runtime surface","identity_rule":"Any material source/config/code repair creates a new run identity","invalidation":"Affected descendants only"}; p=self.pipeline.bundle_root/"reports/phase_01/repair_reentry.json"; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(repair,indent=2),encoding="utf-8"); return self._record("24","PASS",[str(p.relative_to(self.pipeline.bundle_root))],repair)
    def stage_25(self):
        checks=self.pipeline.expected_artifact_status()
        excluded={"manifests/phase_01/execution_bundle_manifest.json","manifests/phase_01/gate_decision.json","Layer1Manifest"}
        missing=sorted(k for k,v in checks.items() if k not in excluded and not v)
        blockers=[] if not missing else [{"code":"P01_PRE_EXPORT_ARTIFACT_CLOSURE_FAILED","missing":missing,"owner":"L1_PACKAGING"}]
        return self._record("25","PASS" if not blockers else "BLOCKED",observations={"export_preparation":"COMPLETE" if not blockers else "BLOCKED","missing":missing},blockers=blockers)
    def stage_26(self):
        expected_zip=self.work_root/f"{self.pipeline.bundle_root.name}.zip"
        expected_sha=Path(str(expected_zip)+".sha256")
        pre={"phase":"P01","layer":"L1","notebook_revision":"R6","config_id":self.pipeline.config_id,"pre_package_decision":self.pipeline.state.get("preliminary_decision",{}).get("status","BLOCKED"),"blockers":self.pipeline.blockers,"bundle_target":str(expected_zip),"detached_checksum_target":str(expected_sha),"next_step":"Create Protocol v1.0 P01 annex" if self.pipeline.state.get("preliminary_decision",{}).get("status")=="ACCEPTED" else "Preserve failed bundle; repair the exact external/runtime defect and rerun"}
        result=self._record("26","PASS",[str(expected_zip),str(expected_sha)],pre)
        package=self.pipeline.package_bundle()
        result.observations["external_package_verification"]=package
        self.pipeline.state["package"]=package
        status_path=self.work_root/"stage_status"/"26.json"
        status_path.write_text(json.dumps(result.__dict__,indent=2),encoding="utf-8")
        external=self.work_root/"final_external_package_verification.json"
        external.write_text(json.dumps({"stage":"26","package":package,"bundle_internal_stage_evidence":"reports/phase_01/tests/stage_results.json","self_hash_boundary":"ZIP SHA-256 IS DETACHED AND CANNOT BE EMBEDDED INSIDE THE SAME ZIP"},indent=2),encoding="utf-8")
        print(json.dumps({**pre,"package":package},indent=2))
        return result
