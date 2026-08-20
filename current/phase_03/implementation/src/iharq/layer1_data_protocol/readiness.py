from __future__ import annotations
from typing import Any
A_IDENTITIES={
"A0":"Raw Decoder / Accept-All Raw Decoder Reference","A1":"Calibrated Decoder / Calibration Visibility","A2":"Simple Registered Threshold / Confidence-Threshold Baseline","A3":"Uncertainty and Selective Prediction","A4":"Longer-Window, Multi-Window Voting/Averaging and Ordinary Ensemble Controls","A5":"IHARQ-lite / Rule-Based Evidence Verification","A6":"IHARQ + Evidence-Quality Estimator","A7":"IHARQ + RegimeRisk Temporal Trust","A8":"Learning-to-defer / Deferral Comparison","A9":"Supervised Adaptive-IHARQ / Adaptive Readiness Policy","A10":"Contextual Bandit / Simulation-Bounded Immediate-Reward Adaptation","A11":"Reinforcement-Learning Policy / Simulation-Bounded Sequential Policy Learning","A12":"StressForge Stress Tests / Controlled Stress Robustness","A13":"Layer 9 Simulation-Only Embodiment Demo"}

def generate(records:dict[str,list[dict[str,Any]]],validation_status:str,leakage_status:str)->list[dict[str,Any]]:
    required_types=["DatasetRecord","WindowRecord","SplitRecord","PreprocessingRecord","LabelMapRecord","ValidationReport"]
    available={k:bool(records.get(k)) for k in required_types}; base_ready=all(available.values()) and validation_status=="PASS" and leakage_status=="PASS"
    rows=[]
    for aid,name in A_IDENTITIES.items():
        rows.append({"ablation_id":aid,"official_identity":name,"owner":"DOWNSTREAM_AUTHORITY","downstream_phase":"P02-P15","required_layer1_record_types":required_types,"required_matching_keys":["dataset_id","split_id","preprocessing_id","label_map_id","window_id","config_hash","seed"],"missing_key_behavior":"NOT_READY_OR_DIAGNOSTIC_ONLY","diagnostic_only_behavior":"VISIBLE_WITH_REASON","invalidation":"ANY_SOURCE_SPLIT_PREPROCESS_LABEL_WINDOW_OR_VALIDATION_IDENTITY_CHANGE","status":"FOUNDATION_READY" if base_ready else "NOT_READY","activated_in_p01":False,"executed_in_p01":False,"output_path":"manifests/phase_01/layer1_ablation_readiness_l1_v1.json"})
    return rows

def prove_a14_absent(configs:list[dict[str,Any]],records:list[dict[str,Any]])->dict[str,Any]:
    text=str(configs)+str(records)
    present="A14" in text
    return {"status":"PASS" if not present else "FAIL","a14_present":present,"selector_present":False if not present else True,"run_present":False,"result_present":False,"claim_present":False}
