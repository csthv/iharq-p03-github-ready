#!/usr/bin/env python3
from pathlib import Path
import json, yaml, hashlib, sys, re, tomllib

ROOT=Path(__file__).resolve().parents[1]
fail=[]; passed=[]

def check(name, cond, detail=""):
    (passed if cond else fail).append((name,detail))

# Current handoff
hp=ROOT/"artifacts/phase_closure/IHARQ_Phase_01_Final_Handoff_and_Phase2_Readiness_R1.yaml"
check("current_handoff_exists", hp.exists())
if hp.exists():
    h=yaml.safe_load(hp.read_text())["phase_handoff"]
    check("phase_status", h["phase_status"]=="PHASE_01_SCOPE_FINALIZED_READY_FOR_P02_TRANSITION", h["phase_status"])
    check("p02_readiness", h["next_phase_readiness"].startswith("PASS_"), h["next_phase_readiness"])
    check("no_open_blockers", h["open_blockers"]==[], str(h["open_blockers"]))
    check("a4_not_effectiveness", h["p02_contract"]["a4_effectiveness_executed_in_p01"] is False)
    check("a14_prohibited", h["p02_contract"]["a14"]=="ABSENT_PROHIBITED")
    check("core_windows_12910", h["p02_contract"]["core_window_count"]==12910)
    check("p01_g15_pass", h["p02_contract"]["p01_gate_15"]=="PASS")

# Canonical docs
required=[
"docs/phase_01/implementation/IHARQ_Master_Implementation_Build_Book_Current_with_P01_L1_Annex_R4.md",
"docs/phase_01/implementation/IHARQ_Phase_1_Layer_1_Integrated_Implementation_and_Execution_Annex_R4.md",
"docs/phase_01/protocol/IHARQ_Experiment_Ablation_Evaluation_Protocol_v1_0_Current.md",
"docs/phase_01/analysis/IHARQ_Cumulative_Phase_Evidence_Results_and_Interpretation_Report_Through_P01_Current.md",
"docs/phase_01/layer0/IHARQ_Phase_01_Layer_0_Claim_Review_and_Disposition_Derivative.md",
"docs/phase_01/evidence_map/IHARQ_Cumulative_Paper_and_Thesis_Evidence_Map_Through_P01_Current.md",
"docs/phase_01/layer10/IHARQ_Cumulative_Layer10_Through_P01_Current.md",
"docs/phase_01/closure/IHARQ_Phase_01_Final_Whole_Stack_Synchronization_and_Phase2_Readiness_Report_R1.md",
"notebooks/IHARQ_Phase_01_Layer_01_R54_Matched_A4_R2_Secret_Safe_Final.ipynb",
]
for r in required: check("required:"+r, (ROOT/r).is_file())

# Operational Python metadata
with open(ROOT/"pyproject.toml","rb") as f: py=tomllib.load(f)
check("python_requires_3_12", py["project"]["requires-python"]==">=3.12,<3.13", py["project"]["requires-python"])
check("primary_python_3_12", py["tool"]["iharq"]["primary_python"]=="3.12", py["tool"]["iharq"]["primary_python"])

# Historical execution handoff stays historical
old=yaml.safe_load((ROOT/"artifacts/phase_execution_handoff.yaml").read_text())
check("historical_handoff_preserved", old.get("protocol_v1_created") is False and old.get("layer10_applied") is False)

# P02 compatibility gate
g15=json.load(open(ROOT/"artifacts/manifests/phase_01/gates/P01-G15.json"))
check("P01-G15", g15.get("status")=="PASS", g15.get("status",""))

# Current manifest
mp=ROOT/"CURRENT_GITHUB_READY_REPOSITORY_MANIFEST.json"
check("current_repo_manifest_exists",mp.exists())
if mp.exists():
    m=json.load(open(mp))
    missing=[]; mismatch=[]
    for row in m["files"]:
        p=ROOT/row["path"]
        if not p.exists(): missing.append(row["path"]); continue
        hh=hashlib.sha256(p.read_bytes()).hexdigest()
        if hh!=row["sha256"] or p.stat().st_size!=row["bytes"]: mismatch.append(row["path"])
    check("current_repo_manifest_files",not missing and not mismatch, f"missing={len(missing)} mismatch={len(mismatch)}")

# No active A14 state in current handoff/status surfaces
current_text=(ROOT/"README.md").read_text()+"\n"+hp.read_text()
check("a14_current_boundary", "ABSENT_PROHIBITED" in current_text and not re.search(r'\bA14\b.{0,40}\bACTIVE\b', current_text, re.I|re.S))

print(f"PASS={len(passed)} FAIL={len(fail)}")
for n,d in fail: print("FAIL",n,d)
if fail: sys.exit(1)
