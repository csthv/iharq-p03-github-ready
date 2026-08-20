# IHARQ Master Implementation Build Book - Current with P02/L2 Integrated Plan R4

**Canonical document ID:** `IHARQ-P02-L2-INTEGRATED-BUILD-BOOK-R4`  

**Target phase:** `P02 - Baseline decoders`  

**Primary layer:** `L2 - Decoder and Baseline Measurement Spine`  

**Parent cumulative state:** `IHARQ-CUMULATIVE-P00-P01-P02-INPUT-R1`  

**Governance:** `V6.1 SINGLE-TRACK / ZIP-FIRST / KAGGLE-CENTERED / ONE-NOTEBOOK-DEFAULT / FULL-ABLATION-AND-LAYER-COVERAGE`  

**Build Book status:** `PASS - STRETCH-COMPLETE / AUTHORITY-EXHAUSTED / DOUBLE-CHECKED / TRIPLE-CHECKED / EVALUATION-COMPLETE / ABLATION-COMPLETE / FINALIZED / FROZEN / READY FOR KAGGLE NOTEBOOK AUTHORING`  

**P02 scientific execution:** `NOT STARTED`  

**Official-run condition:** Stage 05 must formally materialize and verify the already-frozen R3 Protocol/environment/configuration bindings before scientific result stages; Stage 05 is verification-only and may not invent, retune, or replace scientific constants.  

**Execution organization:** exactly one comprehensive Kaggle notebook; no alternate execution modes.  

**Ablation amendment:** every P02-owned ablation/control that is fully unlocked under valid authority before its execution stage MUST run in that same notebook and produce analysis-ready evidence; technical computability alone does not change layer ownership.  

## Document Control

| Field | Value |
| --- | --- |
| Revision | R4 |
| Generated | 2026-08-08 |
| Target Phase | P02 |
| Official Phase Name | Baseline decoders |
| Primary Layer | L2 |
| Official Layer Name | Decoder and Baseline Measurement Spine |
| Parent Project State | IHARQ-CUMULATIVE-P00-P01-P02-INPUT-R1 |
| Intended Compute | Kaggle |
| Notebook Count | 1 |
| Execution Started | NO |
| A14 | ABSENT_PROHIBITED |
| Mandatory Ablation Full-Execution Amendment | SHA-256 `0a9b8765c8cdb05bd5c1df8898c284fd0b83bd95af638652c98d98b08d61e6db` |


## Executive Implementation Summary

Phase 02 converts the frozen P01 public-data/split/preprocessing/window foundation into the project's first governed decoder measurement spine. It must train and qualify a plural decoder portfolio, emit native prediction evidence, produce A0 raw-decoder baselines, construct low-label and participant/session evidence, execute A4 ordinary longer/multi-window/ensemble controls, preserve failed/skipped branches, and produce a consumer-specific P03 handoff. The design deliberately stops before Layer 3 calibration, thresholding, abstention, uncertainty or selective-prediction ownership.

The implementation principle is reuse-first: P01 data truth is immutable input. P02 may validate it, resolve pointers and consume it, but it may not relabel, resplit, rewindow, repair, or silently regenerate it. Model-local transforms are legal only when train-fitted and lineage-bound.

```text
completed_phases: [P00, P01]
target_phase: P02
entry_readiness: PASS
p02_execution_started: false
upstream_blockers: []
implementation_build_book_status: FINALIZED
kaggle_notebook_authoring_ready: true
official_run_ready_now: false
official_run_block: FORMALLY_MATERIALIZE_AND_VERIFY_R3_PLANNED_SCIENTIFIC_EXECUTION_FREEZE_ADOPTED_BY_R4_AT_STAGE_05
official_run_block_interpretation: VERIFICATION_ONLY_NO_NEW_SCIENTIFIC_CONSTANTS_OR_OWNER_CHOICES
notebook_count: 1
alternative_execution_modes: PROHIBITED
```

# PART I - AUTHORITY AND PRIOR-STATE INTAKE

## 1. Phase identity and objective

**Scientific purpose.** Establish reproducible public-EEG baseline decoder evidence and a measurement spine strong enough that later reliability layers can demonstrate added value against honest raw-decoder and ordinary-control references.

**Engineering purpose.** Turn the accepted P01 data contract into typed model/checkpoint/prediction/metric/control/readiness artifacts with complete provenance and failure visibility.

**Explicit non-goals.** P02 does not own calibration, confidence-threshold optimization, abstention/selective prediction, learned evidence-quality policy, RegimeRisk, adaptive policy, stress robustness, embodiment, clinical efficacy, deployment safety, or A14.

## 2. Authority manifest and precedence

| Authority | P02 role | Status |
| --- | --- | --- |
| Governance V6.1 | workflow, one-notebook full-scope, loopback, cumulative project state | USED_AS_AUTHORITY |
| Architecture | P02 identity, exact 8 L2 modules, ownership and layer boundaries | USED_AS_AUTHORITY |
| Canonical Registry | record/artifact identities, producer/consumer/lifecycle/status semantics | USED_AS_AUTHORITY |
| Execution and Evidence Plan | phase evidence products/gates/negative-result/reproduction obligations | USED_AS_AUTHORITY |
| Experiment/Ablation/Evaluation Protocol v0.1 | A0-A13 identities, comparison/metric/statistical ownership and claim boundaries | USED_AS_AUTHORITY |
| Phase Execution Playbook | 14-step P02 execution order and failure/handoff behavior | USED_AS_AUTHORITY |
| Method Selection Register | selected/conditional/diagnostic model portfolio, fallback, seed/budget/tuning policies | USED_AS_AUTHORITY |
| Nuts-and-Bolts | internal L2 algorithms/contracts/validators and Protocol sync boundaries | USED_AS_AUTHORITY |
| Current cumulative P00+P01 repo | actual project state, P01 records, pointers, code/schema/config gaps, verifiers | USED_AS_UPSTREAM_ARTIFACT |
| P01 Protocol/Analysis/Layer0/EvidenceMap/Layer10 | frozen upstream evidence and limitation inheritance | USED_AS_UPSTREAM_ARTIFACT |
| P02 master Build Book prompt | required Build Book completeness and output contract | USED_AS_TASK_SPEC |
| P02 Build Book template | document structure and self-audit checklist | USED_AS_STRUCTURAL_PRECEDENT |


Conflict routing follows proposition ownership. Architecture owns module identity; Registry owns canonical record semantics; Protocol owns ablation/metric/statistical scientific rules; Playbook owns execution order; Method Selection owns portfolio; Nuts-and-Bolts owns implementation-neutral internals; this Build Book owns concrete code/config/path/interface/orchestration realization. Historical P00/P01 artifacts are not silently rewritten.

## 3. Source-utilization audit

All supplied governing sources and the merged cumulative repository were inspected. Source hashes are pinned below; machine-readable source-use audit is included in validation.

| Source | SHA-256 |
| --- | --- |
| Governance V6.1 | c811373c19a7c2c3f6d72cf2aed984e02ffcb07bb448cfc3bdbdf26a35a4f1d9 |
| Seven-authority ZIP | beb00f47e4a790242d62405dcca799647d849c8dc2ff043c5196cee372607128 |
| Cumulative P00+P01 ZIP | dc2708ab70e7746499ae09760456825b54efcf587cae3db3410e6f72b0024542 |
| P02 master prompt | 1c97ebd71b2eb96fbc1a628895fcf8932438570d3afb5aeab7108a135cf1e830 |
| P02 template | 77758e9f55d901274102cb99a8111f1319c91f2e4653629622980d338286788c |
| P02 mandatory full-ablation amendment | 0a9b8765c8cdb05bd5c1df8898c284fd0b83bd95af638652c98d98b08d61e6db |
| 02_Canonical_Artifact_Record_and_Interface_Registry_FINAL_R44.md | bdb309f76b9b525ea89cfa56c79a9b7989348e3509febac9ae9fffe7858d1f87 |
| 04_Experiment_Ablation_and_Evaluation_Protocol_FINAL_R42.md | 8b7a393b860bd49a34a794db5c2b80af7f127bc318a112bc7ed3c375ce704813 |
| 01_Master_Architecture_Specification_FINAL_T29_LAYOUT_CORRECTED_R1.pdf | ae374c9de061bc5179c9223e7d646c70cf0d98c414007ab6baf95cd68c814f9b |
| 05_Complete_Phase_Execution_Playbook_FINAL_R41.md | 176f46950b86db8cd5c23789893955336c818a6fcd10ed36d6c66e096faccc87 |
| 07_Integrated_Layers0_to_10_Detailed_Design_and_Nuts_and_Bolts_Specification_FINAL_R2.md | 4f47c6f511e646b2127cc79f14a5f632b00f5112582a049b46c735e78ded638c |
| 03_Execution_and_Evidence_Plan_FINAL_R41.md | f31de3453b331d909a8cccbf951a2df61ef7ca38b71df4bde8be95040095da82 |
| 06_Integrated_Layers0_to_10_Method_Selection_and_Design_Rationale_Register_FINAL_R2.md | b036b02ac65b3bc2595513f4ca8a8137a6273f914e46e1cf6180515e57726749 |


## 4. Cumulative P00/P01 intake

| Property | Frozen value |
| --- | --- |
| Current state | P00_P01_MERGED_VALIDATED_READY_FOR_P02_ENTRY |
| P02 entry | PASS / green light YES |
| Datasets | PhysioNetMI, BNCI2014_001, Lee2019_MI |
| Task | binary left-hand vs right-hand motor imagery |
| Core windows | 12,910 valid; 0 invalid; +0.5..+3.5 s; 480 @160 Hz |
| Split | subject-grouped 102/35/17/18 train/cal/val/test; seed 20260804 |
| Low-label budgets | 1,2,4,8,16,32 per class; nested calibration-role subsets; seed 20260804 |
| A4 R2 | 0.0..3.5 s; 560 @160 Hz; slices 0:320/120:440/240:560; 12910/12910 parents |
| A14 | ABSENT_PROHIBITED |


External P01 numerical bytes remain pointer-governed. Core provider version 2/logical revision 1 and A4 provider version 1/logical revision 2 must be verified by manifest SHA before use.

## 4A. Mandatory cross-document synchronization through P01

The P02 freeze is not derived from the seven authorities in isolation. Before any P02 implementation is accepted, the following already-finalized downstream/current-state surfaces are cross-checked as mandatory constraints:

| Current source | Binding P02 consequence |
| --- | --- |
| Previous P01 Implementation Build Book | Preserve the accepted P01 Dataset/Label/Preprocessing/Split/Budget/Window identities, external-artifact handling, no-mutation rule, and execution-evidence conventions; do not revive P01 pre-run unresolved placeholders that were later resolved by execution. |
| Frozen cumulative Protocol v1.0 through P01 | Preserve role visibility, test-label firewall, run-cell identity requirements, A0-A13 identities, A14 prohibition, post-execution Protocol-update chronology, and the exact accepted P01 scientific freeze. |
| Cumulative Phase Analysis + embedded Layer 0 | Treat P01 results/limitations as current evidence: 12,910/12,910 core closure, A4 substrate readiness only, low-label identities ready but benefit not measured, and no clinical/deployment effectiveness. |
| Cumulative Evidence Map through P01 | Preserve reviewed claim wording/limitation routes and use exact evidence identities; P02 may create new evidence but may not rewrite prior evidence relationships. |
| Cumulative Layer 10 through P01 | Preserve rendering/reproduction boundaries, external artifact version namespaces, negative-evidence visibility, and the distinction READY != EFFECTIVE. |
| Cumulative P00+P01 repository / P02 handoff | Consume the clean merged repository state, five required P02-entry manifest families, P01-G15 PASS, concrete record counts, and phase-specific environment separation. |

**Conflict rule.** When historical Build-Book intent differs from later accepted execution/Protocol/Analysis/Evidence-Map/Layer-10 state, the later accepted governed state controls. No historical pre-run placeholder may be treated as an unresolved P02 input if P01 subsequently resolved it. Conversely, no later document may be used to manufacture a P02 result that has not yet been executed.

**Cross-document freeze result:** `P00_P01_CURRENT_STATE_RECONCILED_FOR_P02 = PASS`.

# PART II - REUSE, GAP, DEPENDENCY, AND INVALIDATION ANALYSIS

## 5. Reuse-first matrix

| item | decision | reason |
| --- | --- | --- |
| P01 core data/split/preprocessing/window records | REUSE_EXISTING_IMPLEMENTATION_AND_ARTIFACT | immutable accepted P01 input |
| P01 A4 R2 substrate | REUSE_EXISTING_IMPLEMENTATION_AND_ARTIFACT | exact matched substrate; P02 evaluates ordinary controls |
| P00/P01 manifest/checksum/ID utilities | REUSE_IMPLEMENTATION_WITH_NEW_PHASE_CONFIG | infrastructure reusable |
| Layer2 package stub | EXTEND_EXISTING_IMPLEMENTATION | currently scientific execution disabled |
| PhaseConfig model | EXTEND_EXISTING_IMPLEMENTATION | currently Literal[P00] and no_empirical_execution=True |
| P02 config | EXTEND_EXISTING_IMPLEMENTATION | template-ready; stale P00 result_values text and empty artifact IDs |
| P02 record schemas | CREATE/EXTEND SUCCESSOR PROFILES | current physical schemas P00-locked; LowCalibration/SubjectProfile absent physically |


## 6. Dependency graph

```text
P00 schema/config/test/provenance foundation
  -> P01 immutable data/split/preprocessing/window + A4 R2 substrate
    -> P02 L2 training/prediction/A0/low-label/profiles/A4/failure/readiness
      -> P03 L3 calibration/uncertainty/selective-prediction consumers
        -> later reliability/policy/stress/embodiment layers
```

**Invalidation roots.** Any accepted correction to P01 dataset/label/split/preprocessing/window identity invalidates dependent P02 model/config/prediction/metric/control/readiness descendants. P02 never patches P01 in place. Model/checkpoint/config corrections create P02 successors and invalidate only their downstream P02/P03 descendants.

## 7. Gap register — resolved pre-Kaggle implementation actions

The repository is a valid cumulative P02 input state, but its current Layer-2 code is a template/foundation surface. The predecessor closure converted every previously observed gap into an exact implementation action or a deterministic conditional terminal state. None remains an owner decision for Kaggle execution.

| gap | R2 resolution | when implemented | blocking state after R2 |
| --- | --- | --- | --- |
| `SCIENTIFIC_EXECUTION=False` in current L2 stub | Replace with versioned P02 execution package under `src/iharq/layer2_decoders/`; historical stub remains unchanged in history. Scientific stages are enabled only after G00-G07. | WP-P02-02/11 | NONE |
| Generic `PhaseConfig` is P00-only | Add `P02PhaseConfigV1` and common phase discriminator; preserve P00 parser behavior; schema round-trip and backwards-compatibility tests required. | WP-P02-02 | NONE |
| Several physical record schemas are P00-local / missing | Create the exact P02 successor schema IDs and required fields frozen in `p02_record_schema_freeze_R2.yaml`; never mutate predecessor schemas. | WP-P02-02 | NONE |
| Three inherited tests assume old P00 publication paths | Apply the exact cumulative-aware reconciliation in `p02_cumulative_test_reconciliation_R3.patch`; preserve original tests under predecessor history. Verified standard-patch result: **26/26 PASS (9.40 s)**; post-test cleanup/verifiers PASS. | WP-P02-12 before notebook scientific run | NONE |
| Seed/repeat cardinalities previously Protocol-bound but unset | Frozen by `P02-PLANNED-SCIENTIFIC-EXECUTION-FREEZE-R3`: master seed 20260804; deterministic branch-specific repeat counts and SHA-256 sub-seed derivation. | Build Book R3 / Stage05 verification only | NONE |
| Hyperparameter grids/caps previously unset | Exact compact grids, candidate caps, attempted-fit caps, early-stopping rules and family resource caps are carried forward and re-frozen by R3. | Build Book R3 / Stage05 verification only | NONE |
| Statistical operating numbers previously unset | 95% participant-cluster intervals; 10,000 bootstrap resamples; BCa with percentile fallback; paired Wilcoxon, Friedman/post-hoc and Holm policy are re-frozen by R3. | Build Book R3 / Stage05 verification only | NONE |
| P01 low-label method preferred 20 independently drawn subset repeats but P01 emitted only one frozen membership per budget | **Do not fabricate/reopen P01.** P02 consumes the one exact inherited subset (`budget_repeat_count=1`) at each 1/2/4/8/16/32-per-class budget. Model-seed replication remains separate. Low-label inference is explicitly `SINGLE_FROZEN_SUBSET_LIMITATION`; budget-sampling variability is not claimed. | R3 run/metric freeze | NONE |
| Conditional external model implementation/checkpoint/license availability | Exact preflight gates decide `ADMITTED` or `DEPENDENCY_BLOCKED/LICENSE_BLOCKED/CHECKPOINT_BLOCKED/INCOMPATIBLE`; primary A0 floor does not depend on these branches. No live scientific-stage download or human choice. | Stage01-05 | NONE |
| CBraMod 160→200 Hz adapter versus A4 3.5-s length | Core 480@160→600@200 valid; A4 virtual 2-s views 320@160→400@200 valid; A4 long 560@160→700@200 is **not admitted** unless the verified model implementation explicitly accepts 700 samples without pad/crop. Current freeze sets `CBRAMOD_A4_LONG=INCOMPATIBLE_FAIL_CLOSED`; no padding/cropping. | R3 model compatibility | NONE |

`UNRESOLVED_IMPLEMENTATION_DECISIONS = 0` and `UNRESOLVED_OFFICIAL_EXECUTION_OWNER_BINDINGS = 0`.

# PART III - P02 SCIENTIFIC AND IMPLEMENTATION CONTRACT

## 8. Immutable P01 input contract

Dataset, label, split, preprocessing, window, quality, budget, and external-artifact identities are read-only. P02 may create model-local train-fitted transforms and deterministic input adapters, but may not overwrite `PreprocessingRecord` or change the official core/A4 windows.

| Input | Count/identity | Rule |
| --- | --- | --- |
| DatasetRecord | 3 | read-only P01 authority |
| WindowRecord | 12,910 core | read-only; exact parent/source lineage |
| SplitRecord | 1 / P01-L1-SPLIT-OFFICIAL-R2 | subject-group roles immutable |
| PreprocessingRecord | 1 | never mutated by model transforms |
| LabelMapRecord | 3 | class order must be explicit |
| ValidationReport | 1 | entry readiness source |
| Core HDF5 | 172 subject shards | manifest/checksum/pointer validation |
| A4 R2 | 12910/12910 parents | exact profile; no padding/clipping/fabrication/drop |


## 9. A4 R2 input contract

| Property | Frozen value |
| --- | --- |
| Family | P01-L1-A4-WINDOW-FAMILY-FREEZE-R2 |
| Long profile | A4_LONG_MATCHED_3P5S_R2 |
| Window | +0.0 -> +3.5 s |
| Samples | 560 @ 160 Hz |
| Multi members | 0:320; 120:440; 240:560 |
| Matched parents | 12910/12910 |
| Manifest SHA | 29124d59907610b1545e0a2b5d1811a4d4a2bf1df64cad49aa880f4721c47305 |


P01 established only the substrate. P02 may now generate ordinary A4 decoder/control evidence. No P01 effectiveness claim is retrospectively created.

## 10. P02 claim ceiling

Permitted eventual evidence domains: baseline decoding, measurement, comparative baseline evidence, low-label behavior, participant/session heterogeneity, ordinary A4 control evidence, reproducibility and technical downstream consumability. P02 alone cannot establish clinical efficacy, deployment safety, calibrated uncertainty, selective-risk control, policy effectiveness, stress robustness or embodiment performance.

# PART IV - LAYER 2 ARCHITECTURE

## 11. Official module lock

| # | Official Layer 2 module | P02 role |
| --- | --- | --- |
| 1 | Baseline trainer | Train/run sanity, classical, Riemannian, compact neural, conditional deep/SSL, and the model sources needed by A0/A4 under frozen L1 inputs. |
| 2 | Prediction logger | Emit immutable prediction-level evidence with native score/logit/probability semantics and class order. |
| 3 | Low-calibration curve builder | Construct budget-aware performance curves using inherited legal P01 budget membership; retain failed/ineligible points. |
| 4 | Subject difficulty profiler | Describe participant/session heterogeneity without diagnosis, routing, or decision-time hard-subject labels. |
| 5 | Model-family registry | Bind family, branch, implementation, config, transform, checkpoint, class-order, score semantics, environment, status, and provenance. |
| 6 | Ensemble comparison builder | Build ordinary longer-window, multi-window vote/average, and fixed ordinary ensemble controls without IHARQ/policy logic. |
| 7 | Compact SSL adapter | Qualify and wrap compact pretrained/foundation branches under the same input/output/provenance contract; fail closed on license/checkpoint/overlap incompatibility. |
| 8 | Downstream readiness validator | Produce per-branch/per-consumer compatibility and missing-field status for P03 and later layers. |


`OFFICIAL_LAYER2_MODULE_COUNT = 8`. Cross-cutting metrics, failure indexing, gates, record builders and notebook orchestration are implementation capabilities, not ninth/tenth modules.

## 12. Prior implementation-capability crosswalk

| Existing capability | Official module | Reuse | P02 change |
| --- | --- | --- | --- |
| manifest/checksum/ID helpers | all/support | reuse with P02 phase config | P02 identities and output sets |
| Layer2 package stub | M01-M08 | extend in place | real scientific execution path |
| P00 record schemas | M02-M08 | semantic precedent only where phase-locked | successor physical profiles |
| P01 HDF5/pointer loader patterns | M01/M08 | reuse/extend | model-input and A4 consumers |
| release verifier/checksum framework | support | reuse with new required-output inventory | P02 phase bundle gates |


## 13. Concern-group crosswalk

| Concern | Modules | Main decisions |
| --- | --- | --- |
| C1 Training/foundation | Baseline trainer; Model-family registry; Compact SSL adapter | portfolio, transforms, training, tuning, seed, resource, checkpoint |
| C2 Prediction/measurement | Prediction logger; Low-calibration curve builder; Subject difficulty profiler; Ensemble comparison builder | score/class order, A0, low-label, profiles, A4, metrics |
| C3 Validation/readiness/handoff | Downstream readiness validator + cross-cutting failure/card/handoff support | failure visibility, readiness, claims, handoff, reproducibility |


# PART V - MODULE IMPLEMENTATION DOSSIERS

## MODULE 1 - Baseline trainer

### A. Identity and authority

`L2-M01`; official Architecture Layer-2 module; owner `L2/P02`.

### B. P02 responsibility

Train/run sanity, classical, Riemannian, compact neural, conditional deep/SSL, and the model sources needed by A0/A4 under frozen L1 inputs.

### C. Existing reusable implementation

Reuse common ID/hash/config/logging/checksum utilities and P01 loader/pointer conventions. Current L2 package is only a P00 foundation stub and cannot be treated as implemented scientific execution.

### D. Required implementation/extension

Implement inside `src/iharq/layer2_decoders/` using cohesive subpackages for config, data adapters, models/training, prediction, metrics, controls, records, validation, handoff and CLI. Do not create a parallel Layer-2 codebase.

### E. Canonical inputs

Layer1 records; model configs; budget configs; seed policy; environment/resource gates

### F. Canonical outputs

checkpoints; training logs; model-registry inputs; branch terminal ledger

### G. Internal components

pure validators; deterministic identity/seed helpers; fit/predict adapters; record builders; partitioned writers; status ledger; source-table builders as applicable.

### H. Public API

Expose stable project-level calls only after reconciling current CLI/API conventions; implementation examples include `load_layer1_inputs`, `validate_layer1_contract`, `build_model`, `fit_model`, `save_checkpoint`, `emit_prediction_records`, `compute_baseline_metrics`, `build_a4_controls`, `validate_layer2_readiness`, `export_phase2_bundle`.

### I. Algorithmic behavior

Fail closed on invalid input/identity. Preserve complete attempted-cell ledger. Deterministic operations are idempotent. Scientific selection is validation-based and fixed before final test.

### J. Fit/evaluation scope

All fitted state uses only the R2-frozen legal fit roles: `train` for FULL_TRAIN and the exact inherited `calibration` budget subset for LOW_LABEL. Validation is selection/checking only and test is evaluation only; test labels never influence fit, branch admission, checkpoint choice, ablation unlock or ensemble construction.

### K. Configuration

Every operation receives immutable config IDs/hashes, branch identity, split/window/budget/seed and environment identity. No hidden notebook constants for scientific settings.

### L. Invariants

P01 truth read-only; class order explicit; score semantics typed; no final-test selection; failures retained; A14 impossible; no downstream layer ownership creep.

### M. Validators

schema/version/lineage, split visibility, class order, score validity, finite values, cardinality, checkpoint/config hash, matched-key integrity, limitation and lifecycle status.

### N. Failure modes

invalid input; missing provenance; nonconvergence; missing native score; resource/license/checkpoint incompatibility; unmatched comparison; serialization/reload failure.

### O. Terminal statuses

SUCCESS, FAILED, NONCONVERGENT, RESOURCE_BLOCKED, LICENSE_BLOCKED, INCOMPATIBLE, SKIPPED_BY_CONDITIONAL_GATE, INVALID, DIAGNOSTIC_ONLY as applicable; preserve Registry vocabulary where more specific.

### P. Logs/observability

start/end/event logs, elapsed time, CPU/RAM/GPU/VRAM where measurable, input/output IDs, branch status, seed/config/checkpoint, failure reason, denominator/attrition.

### Q. Tests

unit + schema + integration + leakage + negative + reproduction tests from `p02_test_catalog.yaml`; module-specific output cardinality/semantic tests.

### R. Resource profile

Measure before setting ceilings. Stream HDF5 and partition outputs. Optional branches use deterministic admission gates; resource block never silently disappears.

### S. Security/licensing

No credentials in outputs. Store only pointer/checksum/license provenance for private/externally restricted artifacts. Pretrained checkpoints require license/corpus-overlap audit.

### T. A0/A4/downstream relationship

A0/A4; downstream fields are produced without implementing downstream methods.

### U. Limitations

Public EEG/offline evidence; model-family/branch/data/budget/seed/config bounded; no clinical/deployment claim.

### V. Definition of Done

Inputs validate; required outputs and failure rows emit; tests pass; source/consumer links resolve; branch/readiness status explicit; bundle/handoff inventory complete.

## MODULE 2 - Prediction logger

### A. Identity and authority

`L2-M02`; official Architecture Layer-2 module; owner `L2/P02`.

### B. P02 responsibility

Emit immutable prediction-level evidence with native score/logit/probability semantics and class order.

### C. Existing reusable implementation

Reuse common ID/hash/config/logging/checksum utilities and P01 loader/pointer conventions. Current L2 package is only a P00 foundation stub and cannot be treated as implemented scientific execution.

### D. Required implementation/extension

Implement inside `src/iharq/layer2_decoders/` using cohesive subpackages for config, data adapters, models/training, prediction, metrics, controls, records, validation, handoff and CLI. Do not create a parallel Layer-2 codebase.

### E. Canonical inputs

accepted models/checkpoints; WindowRecord; SplitRecord; LabelMapRecord

### F. Canonical outputs

PredictionRecord; inference logs; score-availability ledger

### G. Internal components

pure validators; deterministic identity/seed helpers; fit/predict adapters; record builders; partitioned writers; status ledger; source-table builders as applicable.

### H. Public API

Expose stable project-level calls only after reconciling current CLI/API conventions; implementation examples include `load_layer1_inputs`, `validate_layer1_contract`, `build_model`, `fit_model`, `save_checkpoint`, `emit_prediction_records`, `compute_baseline_metrics`, `build_a4_controls`, `validate_layer2_readiness`, `export_phase2_bundle`.

### I. Algorithmic behavior

Fail closed on invalid input/identity. Preserve complete attempted-cell ledger. Deterministic operations are idempotent. Scientific selection is validation-based and fixed before final test.

### J. Fit/evaluation scope

All fitted state uses only the R2-frozen legal fit roles: `train` for FULL_TRAIN and the exact inherited `calibration` budget subset for LOW_LABEL. Validation is selection/checking only and test is evaluation only; test labels never influence fit, branch admission, checkpoint choice, ablation unlock or ensemble construction.

### K. Configuration

Every operation receives immutable config IDs/hashes, branch identity, split/window/budget/seed and environment identity. No hidden notebook constants for scientific settings.

### L. Invariants

P01 truth read-only; class order explicit; score semantics typed; no final-test selection; failures retained; A14 impossible; no downstream layer ownership creep.

### M. Validators

schema/version/lineage, split visibility, class order, score validity, finite values, cardinality, checkpoint/config hash, matched-key integrity, limitation and lifecycle status.

### N. Failure modes

invalid input; missing provenance; nonconvergence; missing native score; resource/license/checkpoint incompatibility; unmatched comparison; serialization/reload failure.

### O. Terminal statuses

SUCCESS, FAILED, NONCONVERGENT, RESOURCE_BLOCKED, LICENSE_BLOCKED, INCOMPATIBLE, SKIPPED_BY_CONDITIONAL_GATE, INVALID, DIAGNOSTIC_ONLY as applicable; preserve Registry vocabulary where more specific.

### P. Logs/observability

start/end/event logs, elapsed time, CPU/RAM/GPU/VRAM where measurable, input/output IDs, branch status, seed/config/checkpoint, failure reason, denominator/attrition.

### Q. Tests

unit + schema + integration + leakage + negative + reproduction tests from `p02_test_catalog.yaml`; module-specific output cardinality/semantic tests.

### R. Resource profile

Measure before setting ceilings. Stream HDF5 and partition outputs. Optional branches use deterministic admission gates; resource block never silently disappears.

### S. Security/licensing

No credentials in outputs. Store only pointer/checksum/license provenance for private/externally restricted artifacts. Pretrained checkpoints require license/corpus-overlap audit.

### T. A0/A4/downstream relationship

A0 source; A1-A13 downstream source; downstream fields are produced without implementing downstream methods.

### U. Limitations

Public EEG/offline evidence; model-family/branch/data/budget/seed/config bounded; no clinical/deployment claim.

### V. Definition of Done

Inputs validate; required outputs and failure rows emit; tests pass; source/consumer links resolve; branch/readiness status explicit; bundle/handoff inventory complete.

## MODULE 3 - Low-calibration curve builder

### A. Identity and authority

`L2-M03`; official Architecture Layer-2 module; owner `L2/P02`.

### B. P02 responsibility

Construct budget-aware performance curves using inherited legal P01 budget membership; retain failed/ineligible points.

### C. Existing reusable implementation

Reuse common ID/hash/config/logging/checksum utilities and P01 loader/pointer conventions. Current L2 package is only a P00 foundation stub and cannot be treated as implemented scientific execution.

### D. Required implementation/extension

Implement inside `src/iharq/layer2_decoders/` using cohesive subpackages for config, data adapters, models/training, prediction, metrics, controls, records, validation, handoff and CLI. Do not create a parallel Layer-2 codebase.

### E. Canonical inputs

PredictionRecord; budget profile; metric dictionary

### F. Canonical outputs

LowCalibrationCurveRecord; curve source tables

### G. Internal components

pure validators; deterministic identity/seed helpers; fit/predict adapters; record builders; partitioned writers; status ledger; source-table builders as applicable.

### H. Public API

Expose stable project-level calls only after reconciling current CLI/API conventions; implementation examples include `load_layer1_inputs`, `validate_layer1_contract`, `build_model`, `fit_model`, `save_checkpoint`, `emit_prediction_records`, `compute_baseline_metrics`, `build_a4_controls`, `validate_layer2_readiness`, `export_phase2_bundle`.

### I. Algorithmic behavior

Fail closed on invalid input/identity. Preserve complete attempted-cell ledger. Deterministic operations are idempotent. Scientific selection is validation-based and fixed before final test.

### J. Fit/evaluation scope

All fitted state uses only the R2-frozen legal fit roles: `train` for FULL_TRAIN and the exact inherited `calibration` budget subset for LOW_LABEL. Validation is selection/checking only and test is evaluation only; test labels never influence fit, branch admission, checkpoint choice, ablation unlock or ensemble construction.

### K. Configuration

Every operation receives immutable config IDs/hashes, branch identity, split/window/budget/seed and environment identity. No hidden notebook constants for scientific settings.

### L. Invariants

P01 truth read-only; class order explicit; score semantics typed; no final-test selection; failures retained; A14 impossible; no downstream layer ownership creep.

### M. Validators

schema/version/lineage, split visibility, class order, score validity, finite values, cardinality, checkpoint/config hash, matched-key integrity, limitation and lifecycle status.

### N. Failure modes

invalid input; missing provenance; nonconvergence; missing native score; resource/license/checkpoint incompatibility; unmatched comparison; serialization/reload failure.

### O. Terminal statuses

SUCCESS, FAILED, NONCONVERGENT, RESOURCE_BLOCKED, LICENSE_BLOCKED, INCOMPATIBLE, SKIPPED_BY_CONDITIONAL_GATE, INVALID, DIAGNOSTIC_ONLY as applicable; preserve Registry vocabulary where more specific.

### P. Logs/observability

start/end/event logs, elapsed time, CPU/RAM/GPU/VRAM where measurable, input/output IDs, branch status, seed/config/checkpoint, failure reason, denominator/attrition.

### Q. Tests

unit + schema + integration + leakage + negative + reproduction tests from `p02_test_catalog.yaml`; module-specific output cardinality/semantic tests.

### R. Resource profile

Measure before setting ceilings. Stream HDF5 and partition outputs. Optional branches use deterministic admission gates; resource block never silently disappears.

### S. Security/licensing

No credentials in outputs. Store only pointer/checksum/license provenance for private/externally restricted artifacts. Pretrained checkpoints require license/corpus-overlap audit.

### T. A0/A4/downstream relationship

A0/A4 context; downstream fields are produced without implementing downstream methods.

### U. Limitations

Public EEG/offline evidence; model-family/branch/data/budget/seed/config bounded; no clinical/deployment claim.

### V. Definition of Done

Inputs validate; required outputs and failure rows emit; tests pass; source/consumer links resolve; branch/readiness status explicit; bundle/handoff inventory complete.

## MODULE 4 - Subject difficulty profiler

### A. Identity and authority

`L2-M04`; official Architecture Layer-2 module; owner `L2/P02`.

### B. P02 responsibility

Describe participant/session heterogeneity without diagnosis, routing, or decision-time hard-subject labels.

### C. Existing reusable implementation

Reuse common ID/hash/config/logging/checksum utilities and P01 loader/pointer conventions. Current L2 package is only a P00 foundation stub and cannot be treated as implemented scientific execution.

### D. Required implementation/extension

Implement inside `src/iharq/layer2_decoders/` using cohesive subpackages for config, data adapters, models/training, prediction, metrics, controls, records, validation, handoff and CLI. Do not create a parallel Layer-2 codebase.

### E. Canonical inputs

PredictionRecord; BaselineMetricRecord; subject/session metadata

### F. Canonical outputs

SubjectProfileRecord; descriptive source tables

### G. Internal components

pure validators; deterministic identity/seed helpers; fit/predict adapters; record builders; partitioned writers; status ledger; source-table builders as applicable.

### H. Public API

Expose stable project-level calls only after reconciling current CLI/API conventions; implementation examples include `load_layer1_inputs`, `validate_layer1_contract`, `build_model`, `fit_model`, `save_checkpoint`, `emit_prediction_records`, `compute_baseline_metrics`, `build_a4_controls`, `validate_layer2_readiness`, `export_phase2_bundle`.

### I. Algorithmic behavior

Fail closed on invalid input/identity. Preserve complete attempted-cell ledger. Deterministic operations are idempotent. Scientific selection is validation-based and fixed before final test.

### J. Fit/evaluation scope

All fitted state uses only the R2-frozen legal fit roles: `train` for FULL_TRAIN and the exact inherited `calibration` budget subset for LOW_LABEL. Validation is selection/checking only and test is evaluation only; test labels never influence fit, branch admission, checkpoint choice, ablation unlock or ensemble construction.

### K. Configuration

Every operation receives immutable config IDs/hashes, branch identity, split/window/budget/seed and environment identity. No hidden notebook constants for scientific settings.

### L. Invariants

P01 truth read-only; class order explicit; score semantics typed; no final-test selection; failures retained; A14 impossible; no downstream layer ownership creep.

### M. Validators

schema/version/lineage, split visibility, class order, score validity, finite values, cardinality, checkpoint/config hash, matched-key integrity, limitation and lifecycle status.

### N. Failure modes

invalid input; missing provenance; nonconvergence; missing native score; resource/license/checkpoint incompatibility; unmatched comparison; serialization/reload failure.

### O. Terminal statuses

SUCCESS, FAILED, NONCONVERGENT, RESOURCE_BLOCKED, LICENSE_BLOCKED, INCOMPATIBLE, SKIPPED_BY_CONDITIONAL_GATE, INVALID, DIAGNOSTIC_ONLY as applicable; preserve Registry vocabulary where more specific.

### P. Logs/observability

start/end/event logs, elapsed time, CPU/RAM/GPU/VRAM where measurable, input/output IDs, branch status, seed/config/checkpoint, failure reason, denominator/attrition.

### Q. Tests

unit + schema + integration + leakage + negative + reproduction tests from `p02_test_catalog.yaml`; module-specific output cardinality/semantic tests.

### R. Resource profile

Measure before setting ceilings. Stream HDF5 and partition outputs. Optional branches use deterministic admission gates; resource block never silently disappears.

### S. Security/licensing

No credentials in outputs. Store only pointer/checksum/license provenance for private/externally restricted artifacts. Pretrained checkpoints require license/corpus-overlap audit.

### T. A0/A4/downstream relationship

A0/A4 context; downstream fields are produced without implementing downstream methods.

### U. Limitations

Public EEG/offline evidence; model-family/branch/data/budget/seed/config bounded; no clinical/deployment claim.

### V. Definition of Done

Inputs validate; required outputs and failure rows emit; tests pass; source/consumer links resolve; branch/readiness status explicit; bundle/handoff inventory complete.

## MODULE 5 - Model-family registry

### A. Identity and authority

`L2-M05`; official Architecture Layer-2 module; owner `L2/P02`.

### B. P02 responsibility

Bind family, branch, implementation, config, transform, checkpoint, class-order, score semantics, environment, status, and provenance.

### C. Existing reusable implementation

Reuse common ID/hash/config/logging/checksum utilities and P01 loader/pointer conventions. Current L2 package is only a P00 foundation stub and cannot be treated as implemented scientific execution.

### D. Required implementation/extension

Implement inside `src/iharq/layer2_decoders/` using cohesive subpackages for config, data adapters, models/training, prediction, metrics, controls, records, validation, handoff and CLI. Do not create a parallel Layer-2 codebase.

### E. Canonical inputs

configs; trained artifacts; logs; failures

### F. Canonical outputs

ModelRegistryRecord; checkpoint registry; model-card source bundle

### G. Internal components

pure validators; deterministic identity/seed helpers; fit/predict adapters; record builders; partitioned writers; status ledger; source-table builders as applicable.

### H. Public API

Expose stable project-level calls only after reconciling current CLI/API conventions; implementation examples include `load_layer1_inputs`, `validate_layer1_contract`, `build_model`, `fit_model`, `save_checkpoint`, `emit_prediction_records`, `compute_baseline_metrics`, `build_a4_controls`, `validate_layer2_readiness`, `export_phase2_bundle`.

### I. Algorithmic behavior

Fail closed on invalid input/identity. Preserve complete attempted-cell ledger. Deterministic operations are idempotent. Scientific selection is validation-based and fixed before final test.

### J. Fit/evaluation scope

All fitted state uses only the R2-frozen legal fit roles: `train` for FULL_TRAIN and the exact inherited `calibration` budget subset for LOW_LABEL. Validation is selection/checking only and test is evaluation only; test labels never influence fit, branch admission, checkpoint choice, ablation unlock or ensemble construction.

### K. Configuration

Every operation receives immutable config IDs/hashes, branch identity, split/window/budget/seed and environment identity. No hidden notebook constants for scientific settings.

### L. Invariants

P01 truth read-only; class order explicit; score semantics typed; no final-test selection; failures retained; A14 impossible; no downstream layer ownership creep.

### M. Validators

schema/version/lineage, split visibility, class order, score validity, finite values, cardinality, checkpoint/config hash, matched-key integrity, limitation and lifecycle status.

### N. Failure modes

invalid input; missing provenance; nonconvergence; missing native score; resource/license/checkpoint incompatibility; unmatched comparison; serialization/reload failure.

### O. Terminal statuses

SUCCESS, FAILED, NONCONVERGENT, RESOURCE_BLOCKED, LICENSE_BLOCKED, INCOMPATIBLE, SKIPPED_BY_CONDITIONAL_GATE, INVALID, DIAGNOSTIC_ONLY as applicable; preserve Registry vocabulary where more specific.

### P. Logs/observability

start/end/event logs, elapsed time, CPU/RAM/GPU/VRAM where measurable, input/output IDs, branch status, seed/config/checkpoint, failure reason, denominator/attrition.

### Q. Tests

unit + schema + integration + leakage + negative + reproduction tests from `p02_test_catalog.yaml`; module-specific output cardinality/semantic tests.

### R. Resource profile

Measure before setting ceilings. Stream HDF5 and partition outputs. Optional branches use deterministic admission gates; resource block never silently disappears.

### S. Security/licensing

No credentials in outputs. Store only pointer/checksum/license provenance for private/externally restricted artifacts. Pretrained checkpoints require license/corpus-overlap audit.

### T. A0/A4/downstream relationship

A0/A4 provenance; downstream fields are produced without implementing downstream methods.

### U. Limitations

Public EEG/offline evidence; model-family/branch/data/budget/seed/config bounded; no clinical/deployment claim.

### V. Definition of Done

Inputs validate; required outputs and failure rows emit; tests pass; source/consumer links resolve; branch/readiness status explicit; bundle/handoff inventory complete.

## MODULE 6 - Ensemble comparison builder

### A. Identity and authority

`L2-M06`; official Architecture Layer-2 module; owner `L2/P02`.

### B. P02 responsibility

Build ordinary longer-window, multi-window vote/average, and fixed ordinary ensemble controls without IHARQ/policy logic.

### C. Existing reusable implementation

Reuse common ID/hash/config/logging/checksum utilities and P01 loader/pointer conventions. Current L2 package is only a P00 foundation stub and cannot be treated as implemented scientific execution.

### D. Required implementation/extension

Implement inside `src/iharq/layer2_decoders/` using cohesive subpackages for config, data adapters, models/training, prediction, metrics, controls, records, validation, handoff and CLI. Do not create a parallel Layer-2 codebase.

### E. Canonical inputs

matched PredictionRecord families; A4 R2 windows; model registry; control config

### F. Canonical outputs

EnsembleControlRecord; disagreement tables; A4 metrics; burden notes

### G. Internal components

pure validators; deterministic identity/seed helpers; fit/predict adapters; record builders; partitioned writers; status ledger; source-table builders as applicable.

### H. Public API

Expose stable project-level calls only after reconciling current CLI/API conventions; implementation examples include `load_layer1_inputs`, `validate_layer1_contract`, `build_model`, `fit_model`, `save_checkpoint`, `emit_prediction_records`, `compute_baseline_metrics`, `build_a4_controls`, `validate_layer2_readiness`, `export_phase2_bundle`.

### I. Algorithmic behavior

Fail closed on invalid input/identity. Preserve complete attempted-cell ledger. Deterministic operations are idempotent. Scientific selection is validation-based and fixed before final test.

### J. Fit/evaluation scope

All fitted state uses only the R2-frozen legal fit roles: `train` for FULL_TRAIN and the exact inherited `calibration` budget subset for LOW_LABEL. Validation is selection/checking only and test is evaluation only; test labels never influence fit, branch admission, checkpoint choice, ablation unlock or ensemble construction.

### K. Configuration

Every operation receives immutable config IDs/hashes, branch identity, split/window/budget/seed and environment identity. No hidden notebook constants for scientific settings.

### L. Invariants

P01 truth read-only; class order explicit; score semantics typed; no final-test selection; failures retained; A14 impossible; no downstream layer ownership creep.

### M. Validators

schema/version/lineage, split visibility, class order, score validity, finite values, cardinality, checkpoint/config hash, matched-key integrity, limitation and lifecycle status.

### N. Failure modes

invalid input; missing provenance; nonconvergence; missing native score; resource/license/checkpoint incompatibility; unmatched comparison; serialization/reload failure.

### O. Terminal statuses

SUCCESS, FAILED, NONCONVERGENT, RESOURCE_BLOCKED, LICENSE_BLOCKED, INCOMPATIBLE, SKIPPED_BY_CONDITIONAL_GATE, INVALID, DIAGNOSTIC_ONLY as applicable; preserve Registry vocabulary where more specific.

### P. Logs/observability

start/end/event logs, elapsed time, CPU/RAM/GPU/VRAM where measurable, input/output IDs, branch status, seed/config/checkpoint, failure reason, denominator/attrition.

### Q. Tests

unit + schema + integration + leakage + negative + reproduction tests from `p02_test_catalog.yaml`; module-specific output cardinality/semantic tests.

### R. Resource profile

Measure before setting ceilings. Stream HDF5 and partition outputs. Optional branches use deterministic admission gates; resource block never silently disappears.

### S. Security/licensing

No credentials in outputs. Store only pointer/checksum/license provenance for private/externally restricted artifacts. Pretrained checkpoints require license/corpus-overlap audit.

### T. A0/A4/downstream relationship

A4 direct; downstream fields are produced without implementing downstream methods.

### U. Limitations

Public EEG/offline evidence; model-family/branch/data/budget/seed/config bounded; no clinical/deployment claim.

### V. Definition of Done

Inputs validate; required outputs and failure rows emit; tests pass; source/consumer links resolve; branch/readiness status explicit; bundle/handoff inventory complete.

## MODULE 7 - Compact SSL adapter

### A. Identity and authority

`L2-M07`; official Architecture Layer-2 module; owner `L2/P02`.

### B. P02 responsibility

Qualify and wrap compact pretrained/foundation branches under the same input/output/provenance contract; fail closed on license/checkpoint/overlap incompatibility.

### C. Existing reusable implementation

Reuse common ID/hash/config/logging/checksum utilities and P01 loader/pointer conventions. Current L2 package is only a P00 foundation stub and cannot be treated as implemented scientific execution.

### D. Required implementation/extension

Implement inside `src/iharq/layer2_decoders/` using cohesive subpackages for config, data adapters, models/training, prediction, metrics, controls, records, validation, handoff and CLI. Do not create a parallel Layer-2 codebase.

### E. Canonical inputs

P01 windows; pretrained checkpoint; adapter config; provenance/license data

### F. Canonical outputs

PredictionRecord; ModelRegistryRecord; admission/failure evidence

### G. Internal components

pure validators; deterministic identity/seed helpers; fit/predict adapters; record builders; partitioned writers; status ledger; source-table builders as applicable.

### H. Public API

Expose stable project-level calls only after reconciling current CLI/API conventions; implementation examples include `load_layer1_inputs`, `validate_layer1_contract`, `build_model`, `fit_model`, `save_checkpoint`, `emit_prediction_records`, `compute_baseline_metrics`, `build_a4_controls`, `validate_layer2_readiness`, `export_phase2_bundle`.

### I. Algorithmic behavior

Fail closed on invalid input/identity. Preserve complete attempted-cell ledger. Deterministic operations are idempotent. Scientific selection is validation-based and fixed before final test.

### J. Fit/evaluation scope

All fitted state uses only the R2-frozen legal fit roles: `train` for FULL_TRAIN and the exact inherited `calibration` budget subset for LOW_LABEL. Validation is selection/checking only and test is evaluation only; test labels never influence fit, branch admission, checkpoint choice, ablation unlock or ensemble construction.

### K. Configuration

Every operation receives immutable config IDs/hashes, branch identity, split/window/budget/seed and environment identity. No hidden notebook constants for scientific settings.

### L. Invariants

P01 truth read-only; class order explicit; score semantics typed; no final-test selection; failures retained; A14 impossible; no downstream layer ownership creep.

### M. Validators

schema/version/lineage, split visibility, class order, score validity, finite values, cardinality, checkpoint/config hash, matched-key integrity, limitation and lifecycle status.

### N. Failure modes

invalid input; missing provenance; nonconvergence; missing native score; resource/license/checkpoint incompatibility; unmatched comparison; serialization/reload failure.

### O. Terminal statuses

SUCCESS, FAILED, NONCONVERGENT, RESOURCE_BLOCKED, LICENSE_BLOCKED, INCOMPATIBLE, SKIPPED_BY_CONDITIONAL_GATE, INVALID, DIAGNOSTIC_ONLY as applicable; preserve Registry vocabulary where more specific.

### P. Logs/observability

start/end/event logs, elapsed time, CPU/RAM/GPU/VRAM where measurable, input/output IDs, branch status, seed/config/checkpoint, failure reason, denominator/attrition.

### Q. Tests

unit + schema + integration + leakage + negative + reproduction tests from `p02_test_catalog.yaml`; module-specific output cardinality/semantic tests.

### R. Resource profile

Measure before setting ceilings. Stream HDF5 and partition outputs. Optional branches use deterministic admission gates; resource block never silently disappears.

### S. Security/licensing

No credentials in outputs. Store only pointer/checksum/license provenance for private/externally restricted artifacts. Pretrained checkpoints require license/corpus-overlap audit.

### T. A0/A4/downstream relationship

A0/A4 variant when admitted; downstream fields are produced without implementing downstream methods.

### U. Limitations

Public EEG/offline evidence; model-family/branch/data/budget/seed/config bounded; no clinical/deployment claim.

### V. Definition of Done

Inputs validate; required outputs and failure rows emit; tests pass; source/consumer links resolve; branch/readiness status explicit; bundle/handoff inventory complete.

## MODULE 8 - Downstream readiness validator

### A. Identity and authority

`L2-M08`; official Architecture Layer-2 module; owner `L2/P02`.

### B. P02 responsibility

Produce per-branch/per-consumer compatibility and missing-field status for P03 and later layers.

### C. Existing reusable implementation

Reuse common ID/hash/config/logging/checksum utilities and P01 loader/pointer conventions. Current L2 package is only a P00 foundation stub and cannot be treated as implemented scientific execution.

### D. Required implementation/extension

Implement inside `src/iharq/layer2_decoders/` using cohesive subpackages for config, data adapters, models/training, prediction, metrics, controls, records, validation, handoff and CLI. Do not create a parallel Layer-2 codebase.

### E. Canonical inputs

all P02 records, registry, warnings, score/class-order coverage

### F. Canonical outputs

Layer2ReadinessReport; compatibility matrix; handoff

### G. Internal components

pure validators; deterministic identity/seed helpers; fit/predict adapters; record builders; partitioned writers; status ledger; source-table builders as applicable.

### H. Public API

Expose stable project-level calls only after reconciling current CLI/API conventions; implementation examples include `load_layer1_inputs`, `validate_layer1_contract`, `build_model`, `fit_model`, `save_checkpoint`, `emit_prediction_records`, `compute_baseline_metrics`, `build_a4_controls`, `validate_layer2_readiness`, `export_phase2_bundle`.

### I. Algorithmic behavior

Fail closed on invalid input/identity. Preserve complete attempted-cell ledger. Deterministic operations are idempotent. Scientific selection is validation-based and fixed before final test.

### J. Fit/evaluation scope

All fitted state uses only the R2-frozen legal fit roles: `train` for FULL_TRAIN and the exact inherited `calibration` budget subset for LOW_LABEL. Validation is selection/checking only and test is evaluation only; test labels never influence fit, branch admission, checkpoint choice, ablation unlock or ensemble construction.

### K. Configuration

Every operation receives immutable config IDs/hashes, branch identity, split/window/budget/seed and environment identity. No hidden notebook constants for scientific settings.

### L. Invariants

P01 truth read-only; class order explicit; score semantics typed; no final-test selection; failures retained; A14 impossible; no downstream layer ownership creep.

### M. Validators

schema/version/lineage, split visibility, class order, score validity, finite values, cardinality, checkpoint/config hash, matched-key integrity, limitation and lifecycle status.

### N. Failure modes

invalid input; missing provenance; nonconvergence; missing native score; resource/license/checkpoint incompatibility; unmatched comparison; serialization/reload failure.

### O. Terminal statuses

SUCCESS, FAILED, NONCONVERGENT, RESOURCE_BLOCKED, LICENSE_BLOCKED, INCOMPATIBLE, SKIPPED_BY_CONDITIONAL_GATE, INVALID, DIAGNOSTIC_ONLY as applicable; preserve Registry vocabulary where more specific.

### P. Logs/observability

start/end/event logs, elapsed time, CPU/RAM/GPU/VRAM where measurable, input/output IDs, branch status, seed/config/checkpoint, failure reason, denominator/attrition.

### Q. Tests

unit + schema + integration + leakage + negative + reproduction tests from `p02_test_catalog.yaml`; module-specific output cardinality/semantic tests.

### R. Resource profile

Measure before setting ceilings. Stream HDF5 and partition outputs. Optional branches use deterministic admission gates; resource block never silently disappears.

### S. Security/licensing

No credentials in outputs. Store only pointer/checksum/license provenance for private/externally restricted artifacts. Pretrained checkpoints require license/corpus-overlap audit.

### T. A0/A4/downstream relationship

A0-A13 consumption readiness; downstream fields are produced without implementing downstream methods.

### U. Limitations

Public EEG/offline evidence; model-family/branch/data/budget/seed/config bounded; no clinical/deployment claim.

### V. Definition of Done

Inputs validate; required outputs and failure rows emit; tests pass; source/consumer links resolve; branch/readiness status explicit; bundle/handoff inventory complete.

# PART VI - MODEL PORTFOLIO

## 14. Portfolio authority and non-zoo rule

The portfolio is plural but bounded. Selected anchors remain fixed unless a formal method-selection reopen is triggered by material incompatibility. Conditional and diagnostic branches are visible; expensive branches do not disappear merely to shorten the notebook.

| branch_id | family | category | status | role | admission | scores | claim |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SAN-MAJ | majority/frequency | sanity | REQUIRED | deterministic hard-label lower bound | always if training labels legal | hard label; prior vector separately diagnostic | A0 lower-bound context |
| SAN-STRAT | seeded stratified random | sanity | REQUIRED | stochastic chance reference | training-role frequency vector + registered seed | probability/prior-based stochastic output where implementation supports | A0 chance context |
| SAN-PERM | grouped full-pipeline source-event label permutation | sanity | REQUIRED_DIAGNOSTIC | pipeline/leakage negative control | training role only; group/source-event atomicity | native selected simple pipeline output | diagnostic only |
| SAN-PRIOR | training-prior vector | sanity | DIAGNOSTIC_ONLY | score diagnostic; not duplicate hard-label baseline | training-role class frequencies | prior vector | diagnostic only |
| DIAG-LOGVAR | log-bandpower/log-variance + L2 logistic | diagnostic | DIAGNOSTIC_ONLY | spatial-attribution diagnostic | legal train fit and score semantics | logistic native | diagnostic only |
| CLS-CSP-LDA | CSP + shrinkage LDA | classical | SELECTED_MAXIMUM_SCOPE | claim-bearing classical anchor | P01 compatibility + valid train fit | labels + native posterior/decision semantics recorded | A0/A4 eligible |
| CLS-FBCSP-LR | FBCSP + L2 logistic | classical | SELECTED_MAXIMUM_SCOPE | frequency-sensitive classical anchor | filter-bank provenance + legal train fit | logistic scores/probabilities | A0/A4 eligible |
| RIE-TS-LR | shrinkage covariance -> tangent space -> L2 logistic | riemannian | SELECTED_MAXIMUM_SCOPE | geometry-aware score-producing anchor | legal covariance/tangent reference train fit | logistic scores/probabilities | A0/A4 eligible |
| RIE-EA-TS | train-safe Euclidean Alignment + tangent/logistic | riemannian | CONDITIONALLY_SELECTED | matched aligned challenger | fit only legal train/adaptation role; matched aligned/unaligned comparison | native terminal classifier output | qualified A0/A4 if admitted |
| RIE-MDM | MDM/FgMDM | riemannian | DIAGNOSTIC_ONLY | geometric mechanism sanity check | score semantics explicitly distance-derived; not calibrated probability | distance-derived simplex/labels | diagnostic only |
| DNN-EEGNET | EEGNet | compact_neural | SELECTED_MAXIMUM_SCOPE | permanent compact specialist anchor | input/output/resource compatibility | native logits/probabilities with exact semantics | A0/A4 eligible |
| DNN-FBCNET | FBCNet | conditional_neural | CONDITIONALLY_SELECTED | frequency-aware neural challenger | original-author implementation or demonstrated equivalence; resource/input gates | native logits | qualified if admitted |
| DNN-SEQ | DBConformer preferred; EEG Conformer direct fallback/matched comparator | conditional_sequence | CONDITIONALLY_SELECTED_ONE_FINAL_SLOT | one modern sequence slot | DBConformer first; if any admission gate fails use EEG Conformer; no final-test selection | native logits/probabilities semantics verified | one claim-bearing sequence slot if admitted |
| DNN-EGTC | EEG-TCNet | fallback | SCREENED_LOW_RESOURCE_FALLBACK | controlled low-resource sequence fallback | only governed reopen if DBConformer + EEG Conformer exceed resource/stability ceiling | native logits | not active by default |
| SSL-CBRAMOD | CBraMod | compact_ssl | CONDITIONALLY_SELECTED | audited compact pretrained branch | checkpoint hash + corpus-overlap + license + channel/montage + 200-Hz model-local adapter + resource + output + reload gates | native logits | qualified A0/A4 variant if admitted |
| SSL-REVE | REVE | compact_ssl | DIAGNOSTIC_ONLY | resource/flexible-montage reference | documentary/bounded diagnostic only under current authority | as declared by implementation | diagnostic only |


## 15-21. Category summary and minimum lawful fallback

Sanity controls: majority/frequency, seeded stratified random, grouped full-pipeline permutation, prior-vector diagnostic; log-bandpower/log-variance logistic is diagnostic attribution. Classical anchors: CSP-shrinkage-LDA and FBCSP-L2-logistic. Geometry anchor: unaligned shrinkage-covariance/tangent-space/L2-logistic; MDM/FgMDM diagnostic; train-safe Euclidean Alignment conditional. Compact neural anchor: EEGNet. FBCNet is fidelity-gated. Modern sequence slot: DBConformer preferred conditional; EEG Conformer direct fallback/matched comparator; only one final claim-bearing sequence slot. CBraMod is conditional SSL; REVE diagnostic-only.

**Minimum lawful floor.** Required sanity controls + at least one classical anchor + at least one Riemannian/robust-classical comparator + EEGNet where measured resources permit. If EEGNet is genuinely resource-infeasible, preserve `RESOURCE_BLOCKED` and narrow the evidence ceiling rather than pretending the neural floor ran. Conditional deep/SSL failure does not invalidate the classical measurement spine.

## 22. Conditional admission matrix

| Branch | Compatibility | License/checkpoint | Resource | Nonredundancy | Final status |
| --- | --- | --- | --- | --- | --- |
| RIE-EA-TS | required | required where external | measured gate | predeclared role | CONDITIONALLY_SELECTED |
| DNN-FBCNET | required | required where external | measured gate | predeclared role | CONDITIONALLY_SELECTED |
| DNN-SEQ | required | required where external | measured gate | predeclared role | CONDITIONALLY_SELECTED_ONE_FINAL_SLOT |
| DNN-EGTC | required | required where external | measured gate | predeclared role | SCREENED_LOW_RESOURCE_FALLBACK |
| SSL-CBRAMOD | required | required where external | measured gate | predeclared role | CONDITIONALLY_SELECTED |
| SSL-REVE | required | required where external | measured gate | predeclared role | DIAGNOSTIC_ONLY |


# PART VII - ABLATIONS AND CONTROLS — PHASE-OWNED FULL-EXECUTION FREEZE

## 23. Mandatory distinction: readiness is not completion

The P02 implementation contract treats **ablation ownership as an execution obligation**. An ablation that P02 owns to completion cannot exit P02 as merely `FOUNDATION_READY`, `READY_FOR_EXECUTION`, `IMPLEMENTATION_AVAILABLE`, or `SUBSTRATE_AVAILABLE`. The Build Book must make the experiment executable; the one Kaggle notebook must run it; Kaggle must export the result, negative result, failure, or lawful unsupported state; and later Phase Analysis must only interpret already-generated evidence.

The controlling chain is:

```text
P02 OWNS FULL ABLATION
→ BUILD BOOK FULLY SPECIFIES IT
→ SINGLE P02 KAGGLE NOTEBOOK FULLY EXECUTES/EVALUATES IT
→ KAGGLE EXPORTS COMPLETE EVIDENCE
→ PROTOCOL RECORDS WHAT OCCURRED
→ PHASE ANALYSIS INTERPRETS EXISTING EVIDENCE
→ LAYER 0 / EVIDENCE MAP / LAYER 10 CONSUME GOVERNED RESULTS
```

It is explicitly invalid to leave a P02-owned ablation partly prepared and expect Phase Analysis to invent the comparison, matching, metrics, statistics, or missing execution later.

**Phase Analysis does not complete missing P02 science.** It interprets Kaggle-generated evidence only; any missing P02-owned comparison, metric, statistical source, matching result, failure row or execution evidence is an execution-sufficiency failure that must return to the governed repair/rerun loop.

## 24. Independent A0–A13 phase-ownership resolution

The seven authorities, current Protocol v1.0 through P01, finalized P01 Analysis/Layer 0/Evidence Map/Layer 10, and the P01→P02 handoff were independently reconciled. `Phase 2 — Baseline decoders` and `Layer 2 — Decoder and Baseline Measurement Spine` own the **scientific production of A0 and A4 evidence**. A1–A3 are Layer 3 / Phase 3 work; A5–A13 are downstream-layer/phase science. P01 supplied frozen substrate, not A0/A4 effectiveness.

| Ablation | Official identity | Source owner / downstream owner | Exact P02 state | Required P02 end state |
|---|---|---|---|---|
| A0 | Raw Decoder / Accept-All Raw Decoder Reference | Layer 2 / Phase 2 | `FULL_EXECUTION_REQUIRED_IN_P02` | actual raw-decoder evidence + metrics + denominators + terminal/failure rows + analysis source outputs |
| A1 | Calibrated Decoder / Calibration Visibility | Layer 3 / Phase 3 | `DOWNSTREAM_PHASE_RESPONSIBILITY` | native score/logit/probability lineage preserved; no calibration execution |
| A2 | Simple Registered Threshold / Confidence-Threshold Baseline | Layer 3 / Phase 3 | `DOWNSTREAM_PHASE_RESPONSIBILITY` | threshold-compatible raw score lineage preserved; no threshold selection/execution |
| A3 | Uncertainty and Selective Prediction | Layer 3 / Phase 3 | `DOWNSTREAM_PHASE_RESPONSIBILITY` | uncertainty-consumable raw score lineage preserved; no selective-prediction execution |
| A4 | Longer-Window, Multi-Window Voting/Averaging and Ordinary Ensemble Controls | Layer 2 / Phase 2 | `FULL_EXECUTION_REQUIRED_IN_P02` | actual matched ordinary-control comparisons + burden + failures + analysis source outputs |
| A5 | IHARQ-lite / Rule-Based Evidence Verification | Layer 4 / downstream phase | `DOWNSTREAM_PHASE_RESPONSIBILITY` | model/prediction/provenance foreign keys only |
| A6 | IHARQ + Evidence-Quality Estimator | Layer 6 / downstream phase | `DOWNSTREAM_PHASE_RESPONSIBILITY` | model/prediction/provenance foreign keys only |
| A7 | IHARQ + RegimeRisk Temporal Trust | Layer 5 / downstream phase | `DOWNSTREAM_PHASE_RESPONSIBILITY` | time-ordered raw decoder lineage only |
| A8 | Learning-to-Defer / Deferral Comparison | downstream Layer 6/7 | `DOWNSTREAM_PHASE_RESPONSIBILITY` | compatible raw evidence and lineage only |
| A9 | Supervised Adaptive-IHARQ / Adaptive Readiness Policy | downstream adaptive-policy owner | `DOWNSTREAM_PHASE_RESPONSIBILITY` | compatible raw evidence and lineage only |
| A10 | Contextual Bandit / Simulation-Bounded Immediate-Reward Adaptation | downstream simulation/policy owner | `DOWNSTREAM_PHASE_RESPONSIBILITY` | stable decoder/context lineage only |
| A11 | Reinforcement-Learning Policy / Simulation-Bounded Sequential Policy Learning | downstream simulation/policy owner | `DOWNSTREAM_PHASE_RESPONSIBILITY` | stable decoder/context lineage only |
| A12 | StressForge Stress Tests / Controlled Stress Robustness | Layer 8 / downstream phase | `DOWNSTREAM_PHASE_RESPONSIBILITY` | clean decoder source lineage only; no stress execution |
| A13 | Layer 9 Simulation-Only Embodiment Demo | Layer 9 / downstream phase | `DOWNSTREAM_PHASE_RESPONSIBILITY` | raw decoder source lineage only; no embodiment execution |
| A14 | ABSENT / PROHIBITED | NONE | `ABSENT_PROHIBITED` | positive implementation/run/result count = 0 |

**Ownership conclusion:** `FULL_EXECUTION_REQUIRED_IN_P02 = [A0, A4]`. There are no partial-execution P02-owned global ablations in the current authority state.

## 25. A0 full-execution contract — raw decoder / accept-all reference

### 25.1 Scientific question and estimand

**Question:** Under the frozen P01 public-EEG data/split/preprocessing/window contract, what raw accept-all decoder performance and evidence are produced by the predeclared P02 baseline portfolio, without calibration, rejection, abstention, threshold gating, or downstream reliability logic?

**Primary estimand:** participant-weighted decoder performance within each dataset and governed run cell, with dataset-specific reporting primary. Cross-dataset pooling is descriptive only unless a later Protocol successor registers a valid confirmatory estimand.

### 25.2 Conditions

| Field | Frozen A0 rule |
|---|---|
| Reference/control identity | `A0-RAW-ACCEPT-ALL` |
| Input profile | P01 official CORE `+0.5..+3.5 s`, 480 samples @160 Hz |
| Datasets | PhysioNetMI, BNCI2014_001, Lee2019_MI |
| Split | `P01-L1-SPLIT-OFFICIAL-R2`; subject-atomic; immutable |
| FULL_TRAIN fit scope | P01 `train`; validation selects/tunes/early-stops; test evaluates only |
| LOW_LABEL fit scope | exact inherited P01 `calibration` budget membership; no train-role supervised labels added |
| Budgets | FULL_TRAIN plus inherited 1/2/4/8/16/32 source events per class where branch is budget-eligible |
| Seeds | R3 frozen deterministic seed policy; classical/Riemannian 1, neural/sequence/SSL 5, SAN-STRAT 20, SAN-PERM 100 |
| Model branches | every R3 portfolio branch receives a planned terminal row; required/selected branches execute; conditional branches execute when their pre-result admission gate passes; diagnostic branches remain diagnostic |
| Prediction behavior | accept every valid decoder prediction; no calibrated confidence, no threshold rejection, no abstention |
| Class order | `left_hand`, `right_hand`; `right_hand` positive for conditional ROC-AUC |
| Expected test denominator | PhysioNetMI 495 + BNCI2014_001 288 + Lee2019_MI 600 = 1,383 eligible CORE test events per successful model/run identity before model-specific terminal failure accounting |
| Failure rule | failure/blocked/incompatible cells remain explicit; no replacement run, hidden exclusion, or denominator laundering |

### 25.3 Mandatory A0 model/run coverage

A0 covers the full predeclared P02 portfolio. Scientific sufficiency requires at minimum one successful classical anchor and one successful Riemannian anchor on every dataset; all other planned branches must still be **attempted or deterministically terminal** under their frozen admission rules. Resource/license/checkpoint/incompatibility outcomes are evidence and do not disappear. EEGNet and external/SSL branches retain their R3 required-attempt/conditional semantics; a failed optional/conditional branch does not erase A0 if the mandatory floor exists, but its failure must remain analysis-visible.

### 25.4 Matching and aggregation

The canonical A0 run-cell key is:

```text
(dataset_id, split_id, window_profile=CORE, evidence_regime,
 budget_id, budget_repeat_id=P01_FROZEN_SINGLE_SUBSET,
 branch_id, model_repeat_index, config_hash, seed_id)
```

Prediction/metric provenance additionally carries subject, session/run, source-event/window identity and checkpoint/model-registry IDs. Participant is the primary independent aggregation unit; windows are never treated as independent inferential replicates.

R3 explicitly materializes all planned A0 run cells in `p02_full_ablation_planned_run_cells_R3.*`. The full portfolio is evaluated at FULL_TRAIN. Low-label cells are created only for `CLS-CSP-LDA`, `RIE-TS-LR`, `DNN-EEGNET`, and conditionally admitted `SSL-CBRAMOD`, because those are the branches whose frozen portfolio contracts mark low-label evidence as claim-ready. Other branches are not silently extended to low-label regimes.

### 25.5 Required metrics and statistical source evidence

Required per supported A0 cell:

- balanced accuracy — primary;
- macro-F1 — required complementary;
- accuracy — required secondary;
- ROC-AUC — conditional on both classes and a lawful finite continuous score;
- confusion matrix and class support;
- prediction completeness and branch terminal coverage;
- participant-level metric table and matched participant-level deltas for predeclared model comparisons;
- 95% participant-cluster uncertainty using 10,000 resamples, BCa with percentile fallback;
- paired two-method comparison: two-sided Wilcoxon on complete participant pairs where inferential support is valid;
- multi-method comparison: Friedman then predeclared paired Wilcoxon post-hoc with Holm correction;
- paired median difference, rank-biserial effect size, and Kendall W for Friedman where applicable.

A weak or null A0 result is a valid result. No model must outperform another for A0 to count as executed.

### 25.6 A0 software implementation

The future notebook must implement these already-frozen components under `src/iharq/layer2_decoders/`:

```text
ablation/a0.py
    build_a0_run_cells(...)
    validate_a0_accept_all_semantics(...)
    evaluate_a0_prediction_partitions(...)
    compute_a0_metric_rows(...)
    build_a0_participant_source_table(...)
    build_a0_matched_comparisons(...)
    export_a0_analysis_sources(...)
```

It reuses the model/training/inference/record/metric components defined elsewhere in this Build Book. No calibration/threshold/selective-prediction function is callable from A0.

### 25.7 A0 outputs

Required outputs include `ModelRegistryRecord`, `PredictionRecord`, `BaselineMetricRecord`, `MatchedComparisonReport` (existing Registry evaluation artifact/profile), `FailureCaseIndex`, A0 terminal ledger, participant-level source table, metric/uncertainty source table, figure-source table, table-source table, Protocol handoff rows, Phase Analysis source bundle, Layer-0 candidate-boundary bundle, Evidence-Map evidence-path rows, Layer-10 source rows, and P03 readiness references.

A0 completion state after execution may be `EXECUTED_RESULTS_PRESERVED_ANALYSIS_INPUTS_COMPLETE` only if all planned A0 run cells have terminal states, mandatory floor coverage exists, metric/denominator/failure outputs validate, and required analysis-source exports exist.

## 26. A4 full-execution contract — ordinary duration / multi-window / ensemble controls

### 26.1 Scientific question

**Question:** Under exactly matched P01 parent events, do the authorized ordinary longer-window, multi-window vote/average, and fixed ordinary ensemble controls change raw decoder performance relative to the matched CORE A0 reference, and what additional evidence-duration/compute burden do they impose?

A4 is an ordinary-control experiment only. It is not calibration, A2 thresholding, IHARQ, learned gating, adaptive weighting, policy learning, dynamic stopping, or selective prediction.

### 26.2 Immutable A4 input substrate

- family: `P01-L1-A4-WINDOW-FAMILY-FREEZE-R2`;
- long profile: `A4_LONG_MATCHED_3P5S_R2`, `+0.0..+3.5 s`, 560 samples @160 Hz;
- multi profile: `A4_MULTI_3X2S_UNIFORM_0P75S_R2`;
- slices: `0:320`, `120:440`, `240:560` corresponding to +0..2.0, +0.75..2.75, +1.5..3.5 s;
- matched parents: 12,910/12,910 globally, therefore the same frozen P01 test parent identities are available for CORE and A4 comparison;
- no padding, clipping, fabrication, parent dropping, or replacement profile.

### 26.3 Frozen A4 condition IDs

| Condition ID | Condition | Mandatory status | Aggregation / fit rule |
|---|---|---|---|
| `A4-C0-CORE` | matched A0 CORE reference | REQUIRED | reuse matched A0 PredictionRecords for the same parent/test identities |
| `A4-C1-LONG-3P5S` | A4 long 3.5-s condition | REQUIRED for every validation-selected A4-eligible role representative that supports its exact input | refit branch on exact A4_LONG representation with frozen family hyperparameters/seed identity; no crop/pad |
| `A4-C2-MULTI-HARD-VOTE` | three 2-s A4 virtual views | REQUIRED | fit/evaluate each frozen view under common branch config; parent-level majority vote; deterministic class-order/tie rule |
| `A4-C3-MULTI-PROB-AVG` | three 2-s A4 virtual views | CONDITIONALLY_REQUIRED | average only genuine, aligned probability vectors; otherwise explicit `NOT_APPLICABLE_SCORE_SEMANTICS` terminal row |
| `A4-C4-MODEL-HARD-VOTE` | fixed ordinary cross-model ensemble | REQUIRED when at least classical + Riemannian representative succeed | pre-result fixed member roles; parent-level hard vote; no learned gating/weights |
| `A4-C5-MODEL-PROB-AVG` | fixed ordinary cross-model ensemble probability average | CONDITIONALLY_REQUIRED | only members with genuine aligned probabilities; otherwise explicit semantic ineligibility |

### 26.4 Representative selection and anti-leakage rule

For A4 role representatives, selection occurs on validation evidence **before test interpretation**:

- classical role: best validation BACC among admitted classical A4-eligible branches; tie → macro-F1 → lower measured validation burden → lexical branch ID;
- Riemannian role: same rule among admitted Riemannian A4-eligible branches;
- compact neural role: EEGNet or admitted frozen neural role under the same pre-result selection rule;
- compact SSL role: CBraMod only if its pre-result license/checkpoint/corpus/input/resource gates pass.

The minimum cross-model ordinary ensemble is the successful classical + Riemannian representatives. Neural/SSL members join only when lawfully admitted. Test results never change membership.

**R3 representative pools are fully frozen:**

- classical/FULL_TRAIN pool: `CLS-CSP-LDA`, `CLS-FBCSP-LR`; low-label pool: `CLS-CSP-LDA` only;
- Riemannian/FULL_TRAIN pool: `RIE-TS-LR`, `RIE-EA-TS`; low-label pool: `RIE-TS-LR` only;
- neural/FULL_TRAIN pool: `DNN-EEGNET`, admitted `DNN-FBCNET`, admitted final `DNN-SEQ`; low-label pool: `DNN-EEGNET` only;
- SSL/FULL_TRAIN and low-label pool: admitted `SSL-CBRAMOD` only; `SSL-REVE` is diagnostic-only and never enters A4 claim-bearing controls;
- `DNN-EGTC` is a diagnostic low-resource fallback and does not enter A4 unless a future authority successor explicitly changes its role before results.

A role representative is selected by **median validation BACC across all successful frozen model repeats for that branch**, then median validation macro-F1, then lower median measured validation burden, then lexical `branch_id`. A branch with no successful eligible repeat is not selectable. After a branch is selected, **all of its frozen model-repeat identities** are carried into A4; no “best seed” is selected. Classical/Riemannian representatives therefore contribute one repeat under the current portfolio, while admitted neural/SSL representatives contribute five.

**Cross-model ensemble repeat pairing is deterministic:** let `R = max(model_repeat_count)` across the admitted member roles. For ensemble repeat `r ∈ [0,R-1]`, a one-repeat member reuses its sole frozen checkpoint, while a five-repeat member uses repeat `r`. If only one-repeat roles are admitted, `R=1`. The ordered member-role vector is fixed before test evaluation. No test result may alter `R`, membership, or pairing.

### 26.5 A4 run-cell identity

Every scientifically distinct A4 condition remains identifiable even when implemented by loops:

```text
P02-A4-{dataset_id}-{role_id}-{branch_id}-{condition_id}-
{evidence_regime}-{budget_id}-{model_repeat_index}-{seed_id}
```

For multi-view conditions, child view rows additionally contain `view_id ∈ {V0,V1,V2}` and link to one parent-level aggregate row. For model ensembles, member model/checkpoint IDs are an ordered immutable membership vector.

### 26.5A Explicit full-ablation planned run-cell expansion

R3 ships `machine_readable/p02_full_ablation_planned_run_cells_R3.csv` and `.yaml`. These are the notebook-authoring run-cell authorities for phase-owned full ablations.

- **A0 (678 planned terminal cells):** every FULL_TRAIN branch/repeat cell is explicitly enumerated; inherited low-label cells are enumerated only for branches whose frozen `low_label_claim_ready=true` contract permits them. `SAN-PERM` uses 100 explicit `permutation_repeat_index` values rather than an implicit loop.
- **A4 (1,218 planned terminal slots):** every dataset × budget × representative-role × repeat-slot × `A4-C0..C3` condition is explicitly enumerated, plus deterministic maximum slots for `A4-C4/C5` cross-model ensembles. Runtime validation selection fills `resolved_branch_id` by the frozen rule above; it does not create a new scientific cell. Inapplicable conditional slots terminate explicitly rather than disappearing.
- Every row contains a stable `planned_run_cell_id`, dataset, budget, repeat, condition, seed identity or deterministic seed rule, comparison reference, required terminal state, notebook stage, gate and analysis-output requirement.

**Total phase-owned full-ablation planned terminal cells: 1,896.** The run-cell expansion is deliberately parameterized only where the **runtime fact itself** (for example license/resource admission or validation-selected representative identity) is unknowable before execution. The resolution algorithm is frozen; no owner/scientific choice remains.

### 26.6 Matching, denominator, failure and unmatched rules

Primary comparison key:

```text
(dataset_id, subject_id, session_or_run_id, source_event_id,
 split_role=test, budget_id, budget_repeat_id,
 role_id, model_repeat_index, config_hash)
```

CORE and A4 rows must share the same parent event. A condition is not silently restricted to easy/common rows. Missing/failed A4 predictions are retained in completeness/attrition evidence; claim-bearing matched deltas use the explicit intersection and separately report the original denominator, matched denominator, unmatched count and reason taxonomy. No unmatched condition is promoted as a confirmatory paired comparison.

### 26.7 A4 metrics/statistics/burden

A4 uses the same performance metrics and participant-cluster uncertainty rules as A0. Each A4-vs-CORE comparison additionally exports:

- paired participant-level metric delta;
- original/matched/unmatched denominator counts;
- evidence duration / observation horizon;
- number of view/model evaluations;
- aggregation operation and member count;
- measured batch-1 inference latency median/P95 and runtime/resource source rows where feasible;
- probability-semantic eligibility for probability averaging;
- negative/null/harmful/equivalent result state without suppression.

Predeclared paired comparisons use Wilcoxon/Holm as frozen by the R3 statistics contract; multi-condition comparisons may use Friedman followed by the predeclared post-hoc rule when support permits.

### 26.8 A4 software implementation

```text
ablation/a4.py
    resolve_a4_role_representatives(...)
    build_a4_condition_cells(...)
    fit_a4_representation_models(...)
    emit_a4_view_predictions(...)
    aggregate_a4_hard_vote(...)
    aggregate_a4_probability_average(...)
    build_fixed_model_ensemble(...)
    match_a4_to_core_parents(...)
    compute_a4_metric_and_burden_rows(...)
    build_a4_matched_comparisons(...)
    export_a4_analysis_sources(...)
```

`aggregate_a4_probability_average` must reject non-probability/misaligned inputs. `fit_a4_representation_models` must reject silent pad/crop/rewindow behavior. The existing CBraMod A4_LONG incompatibility remains fail-closed unless a pre-result verified implementation accepts the exact 700-sample 200-Hz adapter output under a successor config identity.

### 26.9 A4 outputs

Required: per-view and parent-aggregate `PredictionRecord` rows, `ModelRegistryRecord`/checkpoint lineage, `EnsembleControlRecord`, `BaselineMetricRecord`, `MatchedComparisonReport`, `FailureCaseIndex`, burden/source tables, matched-denominator table, figure-source table, table-source table, Protocol handoff rows, complete Phase Analysis source bundle, Layer-0 candidate-boundary bundle, Evidence-Map evidence-path rows, Layer-10 source rows, and P03 readiness references.

A4 completion state after execution may be `EXECUTED_RESULTS_PRESERVED_ANALYSIS_INPUTS_COMPLETE` only when required condition families have terminal evidence, all planned optional/conditional cells have explicit terminal states, required comparisons/metrics/burden/missingness outputs validate, and downstream analysis-source exports exist.

## 27. Full-ablation analysis-input completeness matrix

| Analysis requirement | A0 Kaggle evidence | A4 Kaggle evidence | Required artifact/record |
|---|---|---|---|
| Raw predictions/scores | CORE raw predictions | CORE + long + per-view + aggregate predictions | `PredictionRecord` partitions |
| Model/checkpoint identity | every branch/repeat | every representative/member/condition | `ModelRegistryRecord` |
| Baseline/control metrics | A0 metrics by dataset/participant/run | A4 and matched CORE metrics | `BaselineMetricRecord` |
| Matched comparison | predeclared model comparisons where used | each A4 condition vs matched CORE | `MatchedComparisonReport` |
| Denominators/attrition | expected/valid/missing/terminal | original/matched/unmatched/reason | source denominator tables |
| Subject/session outputs | participant/session metric source rows | matched participant/session deltas | analysis source tables |
| Seed/repetition | exact run IDs | exact run/member/view IDs | run ledger |
| Statistics/uncertainty | 95% participant-cluster sources | paired A4-vs-CORE sources | statistical source tables |
| Negative/null outcomes | retained | retained | negative/result-status rows |
| Failed/blocked/unsupported | retained | retained including score-semantic N/A | `FailureCaseIndex` + terminal ledger |
| Figure/table sources | generated in Kaggle | generated in Kaggle | Layer-10 source bundle |
| Protocol/Analysis/L0/EMap/L10 handoff | complete | complete | governed handoff manifests |

`FULL_P02_ABLATIONS_WITHOUT_COMPLETE_PHASE_ANALYSIS_INPUTS = 0` is a release invariant.

## 28. Downstream ablations and A14 boundary

A1–A3 and A5–A13 are **not** prematurely executed merely because P02 can emit useful source fields. P02 preserves the raw prediction/model/score/class-order/split/budget/seed/provenance foreign keys their lawful owner will later consume. A14 is invalid in config, run cells, schema, CLI, notebook dispatch, reports and handoffs. `A14_POSITIVE_IMPLEMENTATION = 0`.

## 29. Dynamic additional-ablation rule inside the one notebook

The one-notebook rule remains. If a formally accepted authority successor **before result-dependent selection** changes another A0–A13 row to `FULL_EXECUTION_REQUIRED_IN_P02`, Stage 05 must re-enter under a successor configuration and verify that the new ablation has the same completeness dimensions frozen here: implementation, run cells, inputs, conditions, seeds/budgets, matching, metrics/statistics, failures, records, figure/table sources, validators, gates and downstream analysis handoffs. Only then may Stage `18U` dispatch it in the **same notebook lineage**. Technical computability alone never changes ownership.

The following freeze-critical invariants must equal zero:

```text
FULL_P02_ABLATIONS_WITH_UNDEFINED_IMPLEMENTATION = 0
FULL_P02_ABLATIONS_WITH_UNDEFINED_RUN_CELLS = 0
FULL_P02_ABLATIONS_WITH_UNDEFINED_METRICS = 0
FULL_P02_ABLATIONS_WITH_UNDEFINED_COMPARISONS = 0
FULL_P02_ABLATIONS_WITH_UNDEFINED_ANALYSIS_OUTPUTS = 0
FULL_P02_ABLATIONS_DEFERRED_TO_PHASE_ANALYSIS = 0
FULL_P02_ABLATIONS_MISSING_FROM_KAGGLE_PLAN = 0
FULL_P02_ABLATIONS_WITHOUT_KAGGLE_EXECUTION_STAGE = 0
FULL_P02_ABLATIONS_WITHOUT_COMPLETE_PHASE_ANALYSIS_INPUTS = 0
DOWNSTREAM_ABLATIONS_PREMATURELY_EXECUTED = 0
```

**R4 finalization adopts the unchanged R3 scientific ablation decision:** `ALL P02-OWNED ABLATIONS: FULLY IMPLEMENTED FOR EXECUTION`.

# PART VIII - EXPERIMENT AND RUN MATRIX

## 30-31. Dataset × model × budget × seed × control design — exact R3 freeze

The run family grammar is now fully numerical. The notebook expands it deterministically; Stage 05 **verifies** the frozen artifact and may not choose scientific constants.

### Official evidence regimes

1. `FULL_TRAIN`: supervised fit uses P01 `train`; validation is selection/early-stop only; test is final evaluation only.
2. `LOW_LABEL`: supervised fit/adaptation uses only the exact P01 `calibration`-role budget membership (1/2/4/8/16/32 source events per class); validation may select/check; test is final evaluation. **Train-role supervised labels are not added to a LOW_LABEL cell.** External pretrained weights may exist only under their declared provenance and do not change the benchmark label-budget count.
3. A budgeted cell is omitted from claim-ready comparison only through an explicit terminal failure/ineligibility record; no replacement subset is drawn.

### Branch × repeat freeze

| branch group | FULL_TRAIN | LOW_LABEL budgets | model repeats | special repetitions | A4 eligibility |
| --- | --- | --- | --- | --- | --- |
| SAN-MAJ / SAN-PRIOR | yes | diagnostic reference | 1 | — | no |
| SAN-STRAT | yes | diagnostic reference | 20 | stochastic chance seeds | no |
| SAN-PERM | diagnostic | no claim-ready budget curve | 1 pipeline config | 100 grouped label permutations | no |
| DIAG-LOGVAR | yes diagnostic | optional diagnostic | 1 | — | no |
| CSP-LDA / FBCSP-LR / TS-LR | yes | yes | 1 | — | yes; representative role selection for A4 occurs on validation only |
| EA-TS | conditional full/budget | conditional | 1 | — | yes when admitted |
| MDM/FgMDM | diagnostic | no claim-ready curve | 1 | — | no |
| EEGNet | yes | yes | 5 | five deterministic model seeds | yes |
| FBCNet | conditional | conditional | 5 | only after implementation-equivalence gate | yes if admitted |
| DBConformer or EEG-Conformer final sequence slot | conditional | full-train primary; low-label only if resource/admission gate passes | 5 | one final sequence slot; fallback fixed before results | yes if admitted |
| EEG-TCNet | diagnostic fallback | no claim-ready low-label curve | 5 | only if screened fallback invoked pre-result | no |
| CBraMod | conditional | conditional | 5 | audited checkpoint/adaptation only | CORE + A4_MULTI only under current freeze; A4_LONG fail-closed |
| REVE | diagnostic-only | no | 1 diagnostic attempt if resources/provenance pass | — | no |

### Low-label representative portfolio

To avoid turning the one inherited budget ladder into an uncontrolled model zoo, claim-bearing low-label curves are required for the role representatives `CLS-CSP-LDA`, `RIE-TS-LR`, `DNN-EEGNET`, and `SSL-CBRAMOD` only when CBraMod is admitted. `SAN-MAJ` and `SAN-STRAT` remain cheap contextual controls. Additional branches may emit diagnostic budget rows but cannot replace these representatives.

### A4 run cells — R3 complete condition grammar

A4 uses validation-selected role representatives frozen before test interpretation. Every eligible representative expands into separately identifiable `A4-C0` through `A4-C3` cells; the fixed cross-model ensemble expands into `A4-C4` and, when probability semantics permit, `A4-C5`. Every cell retains dataset, source-event parent, label map, split, budget regime, selected hyperparameters and model-seed identity. A4 models may be re-fit on the exact governed A4 representation when input dimensionality requires it; hyperparameters remain validation-frozen and test never selects them.

Run-cell templates are frozen in `p02_full_ablation_execution_contract_R3.yaml`. Parameterized loops are implementation compression only; they may not collapse scientifically distinct condition IDs.

## 32. Seed policy — fully frozen

- `master_seed = 20260804`.
- Derived seed = first 8 hexadecimal digits of `SHA256(canonical_utf8("20260804|P02|dataset_id|run_family_id|budget_id|budget_repeat_id|model_repeat_index|purpose"))`, converted to unsigned integer and reduced modulo `2^31-1`; zero maps to 1.
- Purposes are distinct: `MODEL_INIT`, `SAMPLER`, `AUGMENT`, `DATALOADER`, `PERMUTATION`, `STAT_BOOTSTRAP`, `STAT_TEST`, `CHECKPOINT_TIEBREAK`.
- Deterministic classical/Riemannian branches use one model repeat. Neural/sequence/eligible SSL branches use five model repeats. `SAN-STRAT` uses 20 seeds. `SAN-PERM` uses 100 independently derived permutation seeds.
- P01 budget membership seed remains exactly 20260804 and is **not regenerated** by P02.
- No seed cardinality, seed value, or repetition count may be changed after Stage 05 or because of observed performance.

## 33. Budget policy — exact inherited membership, no fabricated repeats

Consume `P01-L1-LOW-CAL-OFFICIAL-R2` exactly: six calibration-role source-event budgets `{1,2,4,8,16,32}` per class, 18 dataset/budget rows, nested SHA-256-ranked membership, seed 20260804, no validation/test borrowing.

The finished P01 evidence contains **one canonical subset membership per dataset×budget**, not twenty independent subset draws. Therefore:

- `budget_repeat_count = 1` for official P02 use;
- `budget_repeat_id = P01_FROZEN_SINGLE_SUBSET`;
- P02 may cross model seeds over that same subset but may not call those model seeds budget repeats;
- no new P01 budget IDs or membership sets are synthesized;
- low-label curve points may receive participant-cluster uncertainty for the fixed inherited subset, but they must carry `SINGLE_FROZEN_SUBSET_LIMITATION` and may not claim budget-sampling robustness;
- failed/minimum-support points remain visible and are never interpolated.

This resolves the Method-Selection preference for repeated paired draws **without compromising P01 immutability**: the stronger repeat-based inference is simply not available from the accepted upstream evidence and is not fabricated.

## 34-35. Hyperparameter, training and checkpoint freeze

All candidate spaces are frozen before outcomes. Primary selection criterion is validation **balanced accuracy**. Common family tuning cap: maximum **8 successful candidate evaluations** and **12 attempted candidates** per dataset×regime×family; candidate order is canonical lexicographic order. No unused budget transfers to another family.

| branch | exact candidate space / training freeze |
| --- | --- |
| CSP-LDA | CSP components `{4,6,8}`; CSP covariance regularization `oas`; LDA `solver=lsqr`, `shrinkage=auto`; 3 candidates. |
| FBCSP-LR | bands `[8-12,12-16,16-20,20-24,24-28,28-32] Hz`; CSP components/band `{2,4}` × logistic `C={0.1,1,10}`, L2, max_iter=2000; 6 candidates. |
| TS-LR | OAS covariance; tangent metric `riemann`; logistic `C={0.1,1,10}`, L2, max_iter=2000; 3 candidates. |
| EA-TS | train-fitted Euclidean Alignment; inherits selected TS-LR `C`; no extra search. |
| MDM/FgMDM | diagnostic; metric `riemann`; no tuning. |
| EEGNet | architecture fixed to admitted project implementation; `lr={1e-3,3e-4}` × `weight_decay={0,1e-4}` × `dropout={0.25,0.5}` = 8 candidates. |
| FBCNet | only original-author or equivalence-verified implementation; architecture fixed; `lr={1e-3,3e-4}` × `weight_decay={0,1e-4}` = 4 candidates. |
| sequence slot | DBConformer preferred if source/license/interface gates pass, otherwise EEG-Conformer fallback **before result stages**; `lr={3e-4,1e-4}` × `weight_decay={1e-4,1e-3}` = 4 candidates. |
| EEG-TCNet | diagnostic screened fallback; one fixed admitted recipe plus `lr={1e-3,3e-4}` if invoked. |
| CBraMod | no guessed architecture/search. Admission requires exact audited checkpoint and source-defined adaptation recipe. If that recipe is absent/ambiguous, terminal status is `CHECKPOINT_OR_RECIPE_BLOCKED`; branch is not required for A0 floor. |
| REVE | one diagnostic source-defined configuration only if all resource/provenance gates pass; otherwise explicit diagnostic block. |

### Neural optimizer/training rule

- optimizer: AdamW;
- loss: binary cross-entropy/cross-entropy appropriate to registered two-class output; no label smoothing in primary run;
- max epochs: 100;
- early stopping: validation BACC, patience 12 epochs, minimum delta 0.0, restore best checkpoint;
- batch-size ladder: `{64,32,16}` chosen **only** from the predeclared VRAM class at Stage 01; gradient accumulation restores effective batch 64 when batch <64;
- deterministic flags and library seed controls are recorded; nondeterministic kernels are logged and must not silently change run identity;
- final checkpoint tie-break: higher validation BACC → lower validation macro-F1 loss? No: tie-break is higher macro-F1, then lower measured compute burden, then lower parameter/checkpoint bytes, then canonical model ID/candidate ID.

### Training-only augmentation challenger

Primary neural branches use **no augmentation**. One bounded Segmentation-and-Reconstruction training-only challenger is executed for EEGNet at FULL_TRAIN only, using the same five seeds and identical validation/test rules. It is a local diagnostic/training variant, not a new A-number and cannot expand downstream ablation ownership.

### Family resource caps

- tuning hard wall-clock cap: **60 minutes per dataset×regime×family**;
- individual classical/Riemannian candidate cap: 10 minutes;
- individual neural/sequence/SSL candidate cap: 30 minutes;
- final selected neural fit cap: 45 minutes per seed;
- timeout yields `RESOURCE_BLOCKED`/`FAILED_TIMEOUT` and remains in denominators; no interactive extension based on performance.

Every accepted checkpoint must save config hash, model ID, seed, class order, score semantics, package/source revision, training data identity and SHA-256, then reload and reproduce inference within the frozen numeric tolerance.

## 36. Split visibility matrix

| operation | train | calibration | validation | test | fit | selection | reporting |
| --- | --- | --- | --- | --- | --- | --- | --- |
| input validation | read | read | read | read metadata/labels only for integrity; no decisions | NO | NO | integrity only |
| feature/transform fit | YES | only if Protocol explicitly designates adaptation budget | NO FIT | NO | YES on legal fit role | NO | transform lineage |
| model training | YES | only budget/adaptation if explicitly authorized | NO training | NO | YES | NO | training logs |
| hyperparameter selection | inner train | not unless owner designates selection role | YES as frozen selection role/inner relation | NO | bounded candidates | YES without test | all trials |
| checkpoint selection | candidate training | NO unless governed | YES | NO | N/A | YES validation-only | selected + rejected checkpoints |
| budget sampling | NO redesign | consume P01 frozen nested membership | NO | NO | NO | NO adaptive resampling | budget IDs/subset hashes |
| A4 ensemble construction | member models fitted lawfully | NO test-driven member choice | only predeclared compatibility/selection where Protocol allows | NO construction from outcomes | aggregation rule fixed | NO final-test selection | all members/missingness |
| final evaluation | predictions optional diagnostics | budget evidence as governed | selection diagnostics | evaluation only | NO | NO | YES after all selections frozen |


# PART IX - METRICS AND MATCHED COMPARISONS

## 37-42. Metric dictionary — exact P02 selection

| metric_id | name | role | exact P02 rule |
| --- | --- | --- | --- |
| BACC | balanced accuracy | **PRIMARY** | arithmetic mean of recall for the two registered classes; invalid/non-claim-bearing when required true-class support is absent. |
| F1_MACRO | macro-F1 | required complementary | registered class order; `zero_division=0`; absent true class makes the unit non-claim-bearing even though the software value is retained diagnostically. |
| ACC | accuracy | required secondary | correct / valid denominator. |
| ROC_AUC | binary ROC-AUC | conditional | only when both true classes exist and an aligned finite continuous score/native probability for predeclared positive class `right_hand` exists; otherwise `UNSUPPORTED_SCORE_OR_CLASS`. |
| CONFUSION | confusion matrix | required source evidence | rows=true, columns=predicted, canonical class order `[left_hand,right_hand]`; emit support counts. |
| CLASS_SUPPORT | class support | required | valid denominator per true class and all excluded/failed counts. |
| PRED_COMPLETE | PredictionRecord completeness | required support | valid emitted predictions / expected eligible cells with explicit missing reasons. |
| BRANCH_SUCCESS | run-status coverage | required support/negative evidence | planned, attempted, success, failed, blocked, skipped, invalid. |
| A4_DELAY | evidence/latency burden | required A4 | observation duration, window/member count, model evaluations, aggregation overhead, batch-1 compute latency median/P95. |

**Not selected for P02 A0 headline inference:** Cohen kappa, MCC, AUPRC, Brier, NLL/log-loss, ECE, calibration slope/diagram, risk-coverage/rejection/selective metrics, or bespoke metrics. These belong to other owners or require formal future approval.

Aggregation unit is `subject × session × split × budget × model × model_seed × budget_repeat` where applicable; subject is the primary independent reporting unit. Dataset-level estimates are unweighted means of valid subject-level estimates with the full subject distribution visible. Cross-dataset results remain dataset-stratified; no pooled-window or pooled-subject leaderboard is allowed.

## 43. Matched-comparison keys

Minimum key envelope: dataset, subject, session, source event/trial/window parent, split ID/role, preprocessing ID, label map, window profile, budget ID/subset hash, seed/repetition, model family/variant/checkpoint, aggregation unit, score type/class order, comparison identity, MetricDictionary entry and config hash. Unmatched cases are never silently pooled into paired comparisons.

## 44. Unmatched/diagnostic policy

A missing key, unmatched parent, incompatible score kind, missing class, failed branch or incomplete lineage yields explicit diagnostic/unsupported status with denominator/attrition accounting. It does not become zero performance and does not disappear from averages.

## 45. Statistical/uncertainty contract — frozen R3 scientific contract adopted by R4

R4 adopts unchanged the R3-frozen Method-Selection defaults as the P02 **planned scientific execution freeze**; the later post-execution Protocol update must record planned versus actual rather than inventing these during the run.

1. **Confidence level:** 95%.
2. **Bootstrap:** participant-cluster bootstrap, 10,000 resamples, seed derived with purpose `STAT_BOOTSTRAP`; BCa interval when mathematically valid; deterministic percentile bootstrap fallback when BCa is undefined. Fallback reason is recorded.
3. **Two-method confirmatory comparison:** paired subject-level Wilcoxon signed-rank, two-sided, zero differences retained/handled by the registered implementation; use exact mode when library assumptions permit, otherwise the documented approximation. Report paired median difference and matched-pairs rank-biserial correlation.
4. **More than two predeclared methods:** Friedman omnibus over complete participant blocks; report Kendall's W; predeclared paired Wilcoxon post-hoc comparisons follow only within the registered family.
5. **Multiplicity:** Holm family-wise adjustment within each confirmatory family; exploratory comparisons are labeled exploratory and are not mixed into the confirmatory family.
6. **Minimum support:** inferential test requires at least 5 complete participant pairs/blocks; otherwise result is descriptive/`INSUFFICIENT_INFERENTIAL_SUPPORT`.
7. **Confirmatory families:** (a) full-label A0 eligible branches versus the frozen classical anchor within each dataset; (b) each A4 control versus its matched A0/CORE counterpart within dataset×representative-model; (c) bounded A4 ensemble versus its predeclared strongest validation-selected constituent. Low-label curves are **not** confirmatory over budget sampling because only one inherited subset exists per budget.
8. **Cross-dataset synthesis:** dataset-specific effects are primary. No confirmatory random-effects meta-analysis is scheduled in P02 R3; later analysis may request one only through a formally governed Metric/Protocol addition without replacing dataset-specific results.
9. Every interval/test reports participant count, invalid/excluded count, statistic, raw p, Holm-adjusted p where applicable, effect size, software/version, seed and exact matched-key definition.
10. Statistical selection based on observed P02 outcomes is prohibited.

# PART X - RECORDS, SCHEMAS, AND INTERFACES

## 46. Input record matrix

| Record | ID/version | Role | Validation |
| --- | --- | --- | --- |
| DatasetRecord | P01 frozen / 3 | immutable upstream | schema/version/lineage/pointer/hash |
| WindowRecord | P01 frozen / 12910 | immutable upstream | schema/version/lineage/pointer/hash |
| SplitRecord | P01 frozen / 1 | immutable upstream | schema/version/lineage/pointer/hash |
| PreprocessingRecord | P01 frozen / 1 | immutable upstream | schema/version/lineage/pointer/hash |
| LabelMapRecord | P01 frozen / 3 | immutable upstream | schema/version/lineage/pointer/hash |
| ValidationReport | P01 frozen / 1 | immutable upstream | schema/version/lineage/pointer/hash |


## 47. Output record matrix and R2 physical-schema freeze

R2 no longer leaves “create a successor schema later” as an execution-time decision. The exact P02 schema identities and required field envelopes are frozen in `machine_readable/p02_record_schema_freeze_R2.yaml`; WP-P02-02 implements those files before Stage05 and G06 verifies them. P00 physical schemas remain untouched.

| record | P02 schema identity | producer | cardinality rule | consumers |
| --- | --- | --- | --- | --- |
| PredictionRecord | `iharq://schemas/p02/predictionrecord/v1` | Prediction logger | one row per eligible evaluation window × accepted model/checkpoint/seed/regime; failures separately indexed | L3-L10 |
| ModelRegistryRecord | `iharq://schemas/p02/modelregistryrecord/v1` | Model-family registry | one per model/checkpoint/config/seed/branch generation including blocked/failed status | L3-L10/repro |
| BaselineMetricRecord | `iharq://schemas/p02/baselinemetricrecord/v1` | evaluation path | one per governed metric × aggregation cell | Analysis/L10/L0 |
| LowCalibrationCurveRecord | `iharq://schemas/p02/lowcalibrationcurverecord/v1` | Low-calibration builder | one per dataset×representative model×metric curve; contains six attempted budget points and explicit failures | Analysis/L10 |
| SubjectProfileRecord | `iharq://schemas/p02/subjectprofilerecord/v1` | profiler | per subject/session where support gates pass | later descriptive consumers/L10 |
| EnsembleControlRecord | `iharq://schemas/p02/ensemblecontrolrecord/v1` | A4 builder | per predeclared A4 control × matched group | L3/L4/L10/evaluation |
| FailureCaseIndex | `iharq://schemas/p02/failurecaseindex/v1` | cross-cutting | append-only failure rows + indexed release view | Analysis/L10/L0 |
| Layer2ReadinessReport | `iharq://schemas/p02/layer2readinessreport/v1` | readiness validator | one final report plus consumer×branch compatibility rows | P03+ |
| NegativeResultNote | `iharq://schemas/p02/negativeresultnote/v1` | evaluation governance | per governed weak/null/failed result where claim safety requires it | Analysis/L10/L0 |
| DiagnosticOnlyFlag | `iharq://schemas/p02/diagnosticonlyflag/v1` | validation | per downgraded artifact/result | all affected consumers |

`LeakageWarningRecord` remains owner-routed; P02 emits the trigger/source evidence and uses the currently authorized warning representation. `MatchedComparisonReport` remains formal-owner compatible; P02 emits complete matched source tables rather than taking over another layer's physical schema. This is an explicit interface, not an unresolved field.

**Critical rule:** no predecessor schema is edited in place. Any implementation that cannot serialize/validate the frozen R2 successor envelope fails G06 before scientific execution.

## 48-55. Record dossier common requirements

Every P02 record must carry record/schema version, producer/owner, phase/layer, config hash, source IDs/foreign keys, evidence mode, limitation tags, lifecycle/terminal/diagnostic state, branch/model/checkpoint/seed/budget/split/window identities where relevant, and immutable serialization/checksum. Expected cardinality is computed from the frozen run matrix and eligible source denominator; it is never fabricated in advance of that derivation.

# PART XI - SOFTWARE DESIGN

## 56. Physical package tree

```text
src/iharq/layer2_decoders/
  __init__.py
  config.py
  seeds.py
  intake.py
  visibility.py
  transforms.py
  models/
    sanity.py
    classical.py
    riemannian.py
    neural.py
    sequence.py
    ssl.py
  training.py
  checkpoints.py
  registry.py
  prediction.py
  metrics.py
  low_label.py
  profiles.py
  a4_controls.py
  ablation_executor.py
  failures.py
  readiness.py
  bundle.py
  cli.py
  validators/
  records/

configs/phase_02/
  phase.yaml data.yaml split_visibility.yaml budgets.yaml seeds.yaml
  models/*.yaml controls/*.yaml metrics.yaml statistics.yaml resources.yaml outputs.yaml gates.yaml

tests/phase_02/
  unit/ schema/ integration/ leakage/ golden/ checkpoint/ matching/ negative/ reproduction/ bundle/
```

This is a concrete Build Book target layout; it extends the existing canonical package rather than creating a second unrelated codebase.

## 57-60. Public interfaces/configuration/CLI

Stable operations are implemented through existing project conventions. Required interface capabilities: Layer1 intake validation; model construction/fit/checkpoint/reload; PredictionRecord emission; baseline metrics; low-label curve/profile construction; A4 controls; ablation unlock dispatch; readiness validation; final bundle export. CLI should provide preflight, smoke, full-run, resume and bundle-verify commands under the existing IHARQ command framework. No competing runner framework.

## 61-63. Logging/checkpoints/external artifacts

All logs are machine-readable, stage-scoped and branch-scoped. Checkpoints bind run ID/config hash/seed/class order/score semantics/environment/SHA-256/size and reload evidence. External data/model artifacts are pointer-governed with immutable revision/checksum/license/access classification.

# PART XII - ENVIRONMENT, RESOURCES, LICENSES, AND SECURITY

## 64. Kaggle environment — exact R2 runtime contract

P02 uses one notebook and one scientific run lineage. The environment is installed/verified before scientific stages and is immutable afterward.

- Python: `>=3.12,<3.13`; target accepted runtime `3.12.x`.
- Preserve P01 core pins unless the P02 dependency lock explicitly supersedes them: MOABB 1.5.0, MNE 1.12.1, NumPy 2.2.6, SciPy 1.15.3, pandas 2.3.1, scikit-learn 1.7.1, h5py 3.14.0, PyYAML 6.0.2, pydantic 2.11.7, jsonschema 4.25.0, nbformat 5.10.4, pytest 8.4.1.
- P02 model stack lock: PyTorch 2.13.0, Braindecode 1.6.1, pyRiemann 0.12. Exact wheel/package hashes are captured by Stage01 and copied into the execution bundle.
- External source/checkpoint branches (FBCNet-original/equivalent, DBConformer, CBraMod, REVE) must be vendored or immutable-pointer/checksum-resolved **before Stage05**. No live scientific-stage GitHub/model download is allowed.
- Dependency conflicts never create a second execution mode. A conditional branch receives an explicit terminal admission status while the same notebook continues with the mandatory floor.

## 65-66. Resource profile and deterministic admission

Stage01 records CPU count, RAM, GPU name/count, VRAM, CUDA/driver, free disk and package hashes. Admission is deterministic:

| measured environment | neural policy |
| --- | --- |
| CUDA GPU with >=12 GiB VRAM | standard neural class; start batch 64 then fixed ladder 32/16 only on OOM, recording the transition; conditional deep/SSL gates may proceed. |
| CUDA GPU 8-<12 GiB | constrained neural class; start batch 32, gradient accumulation to effective 64; conditional branches admitted only if their documented memory probe passes. |
| CUDA GPU <8 GiB | EEGNet mandatory attempt under batch 16/effective 64; FBCNet/sequence/SSL become `RESOURCE_BLOCKED` unless their preflight probe fits. |
| CPU-only | sanity/classical/Riemannian mandatory; EEGNet receives one bounded smoke/full attempt under the 45-min final-fit cap; other neural/SSL branches are `RESOURCE_BLOCKED` unless a predeclared CPU-compatible probe passes. |

Disk floor for the notebook working set is 8 GiB free before model stages. Checkpoints are retained only for accepted candidates plus explicit diagnostic failures needed for reproduction; large intermediate tensors are streamed and checksummed. Resource blocking is a recorded result and never silently removes a planned branch.

## 67-71. License, provenance, model compatibility and security freeze

Every external implementation/checkpoint has `source_uri_or_package`, immutable revision, license, SHA-256, source publication identity, pretraining corpus/overlap statement, model-input adapter, frozen/trainable parameter policy, class-output mapping, offline reload status and redistribution classification.

Fail-closed terminal statuses are fully defined: `ADMITTED`, `DEPENDENCY_BLOCKED`, `LICENSE_BLOCKED`, `CHECKPOINT_BLOCKED`, `CORPUS_OVERLAP_UNRESOLVED`, `INPUT_INCOMPATIBLE`, `RESOURCE_BLOCKED`, `FAILED`, `DIAGNOSTIC_ONLY`, `SUCCESS`.

Model-local resampling never mutates P01 `WindowRecord`/`PreprocessingRecord`. CBraMod's registered adapter is deterministic polyphase 160→200 Hz (`up=5`, `down=4`) and creates a derived model-input identity: CORE 480→600 samples; A4 virtual 320→400 samples. Current A4_LONG 560→700 samples is fail-closed for CBraMod because the selected patch convention requires compatible exact input length and P02 may not pad/crop to force compatibility; a future verified implementation may reopen that branch only before Stage05 under a new config identity.

Secrets: no API token/checkpoint credential value may enter records, logs, notebook outputs, manifests or final bundle. Final export scans secret-like values, absolute transient paths, raw private data, unresolved placeholders, unsafe ZIP paths and checksum coverage.

# PART XIII - TEST ARCHITECTURE

## 72-83. Test catalog

| test_id | kind | target | expected | gate |
| --- | --- | --- | --- | --- |
| T-CFG-01 | unit | P02 config parser | P02 accepted, P00 compatibility preserved | G05 |
| T-SEED-01 | unit | seed derivation | same semantic run identity -> same derived seed; distinct identity -> distinct deterministic seed | G05 |
| T-BUD-01 | unit | budget loader | exact nested P01 membership; no window-level resampling | G04 |
| T-MOD-01 | unit | model builder | every portfolio branch resolves to role/status/admission gate | G06 |
| T-SCORE-01 | unit | score semantics | class order and native output type explicit; no fabricated probability | G14 |
| T-MET-01 | golden | accuracy/balanced accuracy/F1/AUC/confusion | matches independent fixture expectations including undefined cases | G15 |
| T-ENS-01 | golden | majority vote/probability average | fixed class order and tie policy | G18 |
| T-A4-01 | integration | A4 parent matching | no unmatched row in paired comparison; missing retained | G18 |
| T-ABL-01 | governance | ablation unlock | A0/A4 execute; A1-A3/A5-A13 do not without authority; A14 impossible | G18U |
| T-LEAK-01 | negative | test label firewall | selection/fit attempt using test rejected | G07 |
| T-CHK-01 | checkpoint | save/reload/predict | equivalent inference within frozen tolerance | G13 |
| T-REC-01 | schema | all L2 records | P02 successor schema + lineage + status valid | G06 |
| T-FAIL-01 | negative | failed branch | failure remains visible and excluded only with reason | G19 |
| T-READY-01 | integration | consumer readiness | per-consumer fail-closed, not global success inference | G20 |
| T-BUNDLE-01 | bundle | checksums/path safety/manifest/secret scan | all PASS | G24 |
| T-REPRO-01 | reproduction | deterministic classical branch | clean reload/re-execution reproduces source outputs within tolerance | G24 |


The current cumulative repository baseline was retested after removing generated bytecode: `verify_cumulative_release.py` = **40/40 PASS** and `verify_phase01_release.py` = **24/24 PASS**. The inherited general pytest suite originally reported 23 PASS / 3 FAIL because three tests still asserted historical P00 publication paths. The R2 descriptive diff was discovered during R3 revalidation to be non-applyable by standard `patch`. R3 replaces it with a valid unified diff; applying the R3 patch to the untouched cumulative repository produced **26/26 PASS in 9.40 s**, then cleanup restored the cumulative verifier to 40/40 PASS and the P01 verifier to 24/24 PASS. WP-P02-12 applies this already-tested patch before the Kaggle scientific stages while preserving the historical P00 tests in predecessor history.

# PART XIV - GATES AND EVIDENCE SUFFICIENCY

## 84-85. Gate matrix

| gate_id | requirement | blocking | failure |
| --- | --- | --- | --- |
| G00 | Current project state and authority hashes resolve | True | BLOCK_PREPARATION |
| G01 | P02 environment packages/resource inventory resolvable; branch-specific dependencies isolated | True | BLOCK_CORE or branch-specific RESOURCE/INCOMPATIBLE |
| G02 | Cumulative repository manifest/checksum verification PASS | True | BLOCK |
| G03 | Core and A4 external pointer identities/checksums/version namespaces resolve | True | BLOCK affected substrate |
| G04 | 3 DatasetRecords/12910 WindowRecords/Split/Preprocessing/LabelMap/Validation contract validates without mutation | True | BLOCK and owner-routed P01 defect |
| G05 | Complete R3 scientific execution freeze, run matrix, metrics, exact seeds/repeats/budgets/grids/statistics/resource caps and ablation unlock matrix are present and hash-verified | True | BLOCK OFFICIAL RUN; no notebook-time default filling |
| G06 | P02 schemas/interfaces/fixtures/imports/smoke path pass | True | BLOCK |
| G07 | role firewall, lineage and loaders pass | True | BLOCK |
| G08 | sanity controls emit expected outputs/negative-control behavior | True | BLOCK core measurement spine if lower-bound/pipeline integrity absent |
| G09 | classical floor has >=1 lawful classical anchor | True | BLOCK scientifically useful P02 |
| G10 | Riemannian/robust-classical comparator present | True | BLOCK minimum floor |
| G11 | EEGNet compact neural executes where feasible; resource infeasibility is measured and routed | False | RESOURCE_BLOCKED with explicit evidence consequence |
| G12 | every conditional deep/SSL branch has explicit admission terminal status; no hidden omission | False | branch-specific blocked/skipped; primary floor continues |
| G13 | accepted model checkpoints reload and registry linkage complete | True | affected model INVALID/BLOCKED |
| G14 | PredictionRecord coverage/class order/score semantics/lineage valid | True | affected branch consumer-ineligible |
| G15 | A0 source metrics and denominators complete for eligible primary branches | True | BLOCK A0/evidence sufficiency |
| G16 | legal budget points emitted or explicit failed/ineligible statuses retained | True | curve scope downgraded; no invented/interpolated point |
| G17 | descriptive profiles preserve coverage and no diagnosis/routing | False | diagnostic/omit unsupported profile claim |
| G18 | A4 R2 exact parent matching/class order/aggregation/burden and missingness rules pass | True | BLOCK A4 claim-bearing control evidence |
| G18U | extra ablation runs only if p02_state=FULL_EXECUTION_REQUIRED_IN_P02 + full implementation/evaluation bindings frozen before results | False | NOT_AUTHORIZED/INCOMPATIBLE; never separate mode |
| G19 | all planned/attempted/failed/skipped/blocked rows visible | True | BLOCK release if negative evidence hidden |
| G20 | consumer-specific readiness matrix complete | True | downstream affected consumer blocked/diagnostic |
| G21 | source tables carry exact lineage and limitations | True | not thesis/L10-ready |
| G22 | all downstream handoffs present and source-linked | True | BLOCK phase documentary closure |
| G23 | evidence sufficiency passes or minimal repair route emitted | True | LOOPBACK only relevant scope |
| G24 | manifest/checksums/path safety/secret scan/output inventory PASS | True | BLOCK export/release |


## 86. Evidence-sufficiency decision — full-ablation completion is mandatory

P02 evidence is sufficient only if **every P02-owned full-execution ablation is complete as execution evidence**, not merely prepared.

Required:

```text
required_full_P02_ablations: [A0, A4]
required_full_P02_ablations_executed: ALL
required_ablation_records_present: ALL
required_comparisons_complete: ALL
required_metrics_complete: ALL
required_failure_negative_outcomes_preserved: ALL
required_analysis_source_outputs_complete: ALL
```

For A0, all planned cells must have terminal states and the mandatory classical+Riemannian floor must produce valid raw-decoder evidence per dataset. For A4, the required CORE/LONG/MULTI-HARD-VOTE/fixed ordinary hard-vote condition families must have terminal evidence; probability-average conditions may terminate as explicit semantic `NOT_APPLICABLE` when genuine aligned probabilities are unavailable. Conditional model/resource failures are valid evidence only when preserved; they do not excuse missing mandatory control-family logic.

If either A0 or A4 lacks implementation, planned terminal run coverage, required comparisons, metrics, denominator/missingness accounting, failures/negative results, or Phase-Analysis source outputs, then:

```text
P02_EVIDENCE_SUFFICIENCY = FAIL
```

and the minimum owner-correct repair/rerun loop applies.

## 87-89. Insufficiency/repair loop

The only permitted loopback is evidence insufficiency. Repair the smallest owner-correct scope, preserve the failed attempt, create a successor config/code/checkpoint as required, re-enter from the earliest invalidated stage, regenerate dependent evidence in order and rerun gates. Do not restart unrelated work or silently change the scientific design after seeing test outcomes.

# PART XV - KAGGLE EXECUTION DESIGN

## 90. Notebook identity

```text
notebook_id: IHARQ-P02-COMPLETE-EXECUTION-AND-ANALYSIS-R4
filename: IHARQ_Phase_02_Complete_Execution_and_Analysis_R4.ipynb
notebook_count: 1
second_notebook_justification: NOT_REQUIRED
alternative_execution_modes: PROHIBITED
organization_rule: ONE_NOTEBOOK_FULL_SCOPE
```

## 91. Notebook stage matrix

| stage | purpose | modules | inputs | outputs | gate |
| --- | --- | --- | --- | --- | --- |
| 00 | Identity, authorities, cumulative project-state intake | all governance | cumulative ZIP | authority intake + run identity | G00 |
| 01 | Environment/dependency setup and measured resource inventory | M01/M05/M07/M08 | environment plan | environment report | G01 |
| 02 | Cumulative ZIP, manifest and checksum preflight | M08 | project ZIP | verified intake ledger | G02 |
| 03 | Resolve external P01 core + A4 artifact pointers | M08 | pointer records | resolved immutable artifact map | G03 |
| 04 | Validate P01 input contract; no relabel/resplit/rewindow | M08 | P01 records/shards | input validation report | G04 |
| 05 | Verify immutable P02 R3 scientific execution freeze/run families/model portfolio/ablation matrix | M01/M05/M08 | Build Book R3 + `p02_planned_scientific_execution_freeze_R3.yaml` | verified config hash + run matrix + ablation unlock freeze | G05 |
| 06 | Schema successor/profile, fixture, import and smoke validation | all | schemas/code | schema validation + smoke evidence | G06 |
| 07 | Governed data loaders/cache and role firewall | M01/M02 | HDF5 + manifests | loader/cache evidence | G07 |
| 08 | Sanity controls | M01/M05 | core inputs | sanity models/logs | G08 |
| 09 | Classical anchors | M01/M05 | core inputs | CSP/FBCSP checkpoints/logs | G09 |
| 10 | Riemannian anchors/challengers/diagnostics | M01/M05 | core inputs | TS/EA/MDM artifacts | G10 |
| 11 | Compact neural baseline | M01/M05 | core inputs | EEGNet + eligible neural checkpoints | G11 |
| 12 | Conditional deep/SSL admission and execution | M01/M05/M07 | gates/checkpoints | admitted branch artifacts or explicit block | G12 |
| 13 | Checkpoint round-trip + ModelRegistry closure | M05 | all branch artifacts | ModelRegistryRecord + reload evidence | G13 |
| 14 | Governed inference and PredictionRecord generation | M02 | accepted checkpoints + windows | PredictionRecord partitions | G14 |
| 15 | A0 raw baseline metrics and matched comparisons | M02/M03/M04/M05 | PredictionRecords | A0 metric/source artifacts | G15 |
| 16 | Low-label/low-calibration curves | M03 | budgeted records | LowCalibrationCurveRecord | G16 |
| 17 | Subject/session descriptive profiles | M04 | prediction/metric records | SubjectProfileRecord | G17 |
| 18 | A4 longer/multi-window/fixed ordinary ensemble controls | M06 | A4 R2 + matched model outputs | EnsembleControlRecord + A4 evidence | G18 |
| 18U | Authority-approved fully-unlocked additional P02 ablation executor (single-notebook only) | mapped owner modules | Stage05 frozen unlock matrix | executed extra ablation records or NOT_AUTHORIZED rows | G18U |
| 19 | Failure/missingness/negative-result accounting | cross-cutting | all branch ledgers | FailureCaseIndex + NegativeResultNote + diagnostics | G19 |
| 20 | Downstream-readiness validation | M08 | all records | Layer2ReadinessReport | G20 |
| 21 | Figure-source and table-source datasets | source builders | validated evidence | analysis/L10 source tables | G21 |
| 22 | Protocol/Analysis/Layer0/EvidenceMap/Layer10/P03 handoffs | M08 | validated bundle | governed handoff packets | G22 |
| 23 | Gate matrix and evidence-sufficiency evaluation | M08 | all validation | gate_decision + insufficiency route | G23 |
| 24 | Final execution bundle/checksums/secret scan/export | release | all outputs | immutable P02 bundle | G24 |


Stage `18U` is not a second mode. It is a fail-closed dispatcher in the same notebook. Under the current authority its executable additional-ablation set is empty because A0 and A4 are already handled by Stages 15/18 and every other official ablation is downstream-owned. If a valid authority successor fully unlocks an additional P02-owned ablation before the run, Stage 05 freezes it and Stage 18U executes it in the same notebook. If the change arrives after Stage 05, the notebook re-enters from Stage 05 in a new governed run lineage; it does not append an outcome-driven experiment ad hoc.

## 92. Playbook to notebook crosswalk

| Playbook step | Notebook | Output |
| --- | --- | --- |
| 1 freeze/verify input package | 00-05 | intake/config/authority/ablation freeze |
| 2 declare portfolio/seeds/budgets/resources | 05-06 | run-family/model/gate configs |
| 3 train/run branches | 08-12 | models/checkpoints/logs |
| 4 register provenance | 13 | ModelRegistryRecord |
| 5 emit predictions | 14 | PredictionRecord |
| 6 raw metrics/A0 | 15 | BaselineMetricRecord/A0 tables |
| 7 low-label evidence | 16 | LowCalibrationCurveRecord |
| 8 subject/session evidence | 17 | SubjectProfileRecord |
| 9 A4 ordinary controls | 18 + 18U if lawfully unlocked extra P02 ablation | EnsembleControlRecord/ablation source tables |
| 10 failures/hard cases | 19 | FailureCaseIndex/negative notes |
| 11 downstream compatibility | 20 | Layer2ReadinessReport |
| 12 Layer10 sources | 21 | figure/table source bundle |
| 13 Layer0 boundaries | 19-22 | limitation/diagnostic handoff |
| 14 freeze/handoff | 22-24 | final bundle/handoffs/checksums |


## 93-95. Resume/smoke/export

Resume is stage/checkpoint-based and idempotent: a stage may reuse an accepted output only after config/input/checksum identity matches; otherwise it is invalidated and rerun. Smoke runs use tiny lawful fixtures/subsets and are always `DIAGNOSTIC_ONLY`; they never satisfy official run cells. Final export performs path safety, checksums, secret scan and required-output inventory.

# PART XVI - EXECUTION BUNDLE DESIGN

## 96. Bundle tree

```text
IHARQ_P02_L2_Phase_Execution_Bundle_<config8>_<attempt>/
  authorities/
  configs/
  environment/
  manifests/
  records/
    model_registry/ prediction/ metrics/ low_label/ subject_profiles/ a4_controls/ readiness/ warnings/
  checkpoints/                 # or external pointers if too large
  reports/
    stages/ gates/ leakage/ matching/ resources/ licenses/
  negative_and_failed_results/
  figure_source_data/
  table_source_data/
  handoffs/
    protocol_v1/ phase_analysis/ layer0/ evidence_map/ layer10/ phase03/
  external_artifact_pointers/
  checksums.sha256
  gate_decision.json
```

Large checkpoints may use private external persistence with pointer/checksum manifests if repository/Kaggle limits require it. The compact bundle must remain self-describing and must never omit branch status because bytes live externally.

# PART XVII - DOWNSTREAM GOVERNED HANDOFFS

## 109. Protocol v1.0 handoff

Freeze actual run matrix, numeric grids/caps, seeds/repetitions, metric/statistical settings, accepted deviations, failures, environment, A0/A4 and any additional fully-unlocked P02 ablation evidence.

## 110. Phase Analysis handoff

Provide complete planned/attempted/success/failed ledger, primitive source tables, metrics, uncertainty summaries, matched keys, denominators, attrition, negative results, resource evidence and limitations. Every P02-owned full ablation must already have complete execution/comparison/metric/denominator/failure/statistical-source evidence; Phase Analysis receives analyzable result/failure rows and performs interpretation only, not missing scientific computation.

## 111. Layer 0 handoff

Candidate claims remain bounded to public-data baseline/measurement/low-label/heterogeneity/A4 evidence. Carry exact limitations and diagnostic downgrades; no automatic claim approval.

## 112. Evidence Map handoff

Provide claim-candidate -> finding/Protocol/run/record/artifact/limitation/figure/table/reproduction identities. Deferred/negative results remain map-able as negative evidence.

## 113. Layer 10 source bundle

Provide read-only figure/table/card source datasets and provenance; Layer 10 never retrains/recomputes hidden science.

## 114. Phase 03 handoff

P03 receives immutable model/prediction/class-order/score/probability/checkpoint/budget/split/config/seed/A0/A4/readiness/failure evidence. P03 may calibrate/threshold/selectively predict; P02 may not.

## 115. Future-phase foreign-key compatibility

Every P02 identity is stable/versioned and source-linked. Downstream corrections create successors; no later layer repairs P02 records in place.

# PART XVIII - FAILURE, LIMITATION, RISK, AND INVALIDATION GOVERNANCE

## 116-118. Failure taxonomy, negative results, limitations

Failure axes are separated: method-selection role, planned portfolio role, run terminal outcome, validation/lifecycle state, diagnostic state and downstream readiness. Failed optional branches, weak simple baselines, strong simple baselines, sparse budgets, missing scores, nonconvergence and unmatched comparisons remain queryable. They are not dropped from denominators without an explicit, governed reason.

## 119. Risk register

| risk_id | risk | probability | impact | detection | mitigation | fallback | blocking | owner |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R-P02-01 | Kaggle GPU/runtime variability | MEDIUM | HIGH for conditional neural branches | Stage01 measured resource inventory | adaptive branch gates, checkpointing, classical floor | RESOURCE_BLOCKED optional branch; no silent omission | core only if minimum floor infeasible | Build Book/runtime |
| R-P02-02 | pretrained checkpoint/license/corpus-overlap ambiguity | MEDIUM | HIGH for SSL claim eligibility | Stage12 provenance audit | checksum/license/corpus audit before load | CBraMod skipped; specialist-only portfolio valid | branch-specific | M07/Protocol claim boundary |
| R-P02-03 | class-order/score semantic mismatch | MEDIUM | CRITICAL downstream | Stage13/14 semantic validators | typed score semantics and class mapping | label-only A0 or consumer-specific ineligible | affected consumer | M02/M05 |
| R-P02-04 | P00 foundation schemas hard-coded to P00 | CERTAIN current gap | HIGH | schema/config audit | immutable P02 successor/generalization; preserve P00 profiles | none for official P02; must repair before run | YES pre-run | WP02 |
| R-P02-05 | cumulative repo legacy P00 tests reference historical moved paths | CERTAIN current gap | LOW scientific / MEDIUM CI | pytest 23 pass / 3 fail | make tests cumulative-aware or scope historical tests to predecessor snapshot | current 40/40 cumulative +24/24 P01 verifiers remain authority | NO notebook design; fix before P02 CI freeze | WP12 |
| R-P02-06 | A4 unmatched parent/score incompatibility | MEDIUM | HIGH | matched key/class order/score validator | hard vote fallback when legal; unsupported if lineage absent | unsupported A4 cell retained | for affected A4 comparison | M06 |
| R-P02-07 | low-budget missing class/support | MEDIUM | MEDIUM | budget eligibility checks | use P01 nested subsets only | INELIGIBLE_DIAGNOSTIC_ONLY point; never borrow test/validation | cell-specific | M03 |
| R-P02-08 | result-dependent model/ablation selection | LOW if gates enforced | CRITICAL validity | config hash + Stage05 freeze + test-label audit | all roles/unlocks frozen pre-result | invalidate affected evidence and rerun | YES | Protocol/Build Book |


## 120. Owner decision register — CLOSED

All P02 Build-Book and official-execution parameters required before Kaggle scientific stages remain frozen by the R3 scientific execution freeze and are adopted unchanged by R4. The post-execution Protocol update remains a **recording/reconciliation** step, not a place where the notebook later chooses missing values.

| decision_id | previously open question | R2 binding | blocking now |
| --- | --- | --- | --- |
| OD-P02-PROTO-01 | stochastic repeats / seed cardinality | master 20260804; deterministic branch counts: classical=1, neural/sequence/SSL=5, SAN-STRAT=20, SAN-PERM=100; budget repeat=1 inherited subset | NO |
| OD-P02-PROTO-02 | compact grids / evaluation cap / resource ceiling | exact model grids above; max 8 successful/12 attempted candidates; 60-min family tuning cap; explicit candidate/final-fit caps | NO |
| OD-P02-PROTO-03 | confidence/resampling/tests/multiplicity/A4 inference | 95%; 10,000 participant-cluster resamples; BCa→percentile fallback; Wilcoxon/Friedman; Holm; exact confirmatory families | NO |

`blocking_owner_decisions_for_build_book_or_notebook_authoring = 0`  
`blocking_owner_decisions_for_official_execution = 0`  
`Stage05_behavior = VERIFY_FROZEN_R2_CONFIGURATION_ONLY`

If a future superior authority legitimately changes any binding **before result stages**, it must create a new P02 config/run identity and controlled Stage05 re-entry. The current notebook never fills or modifies these numbers from outcomes.

## 121-122. Invalidation/future reuse

Upstream P01 identity changes invalidate affected P02 descendants. P02 method/implementation correction invalidates dependent model/prediction/metric/control/readiness descendants. Accepted outputs are reused by exact identity/checksum; stale/superseded outputs remain historical and are never silently overwritten.

# PART XIX - IMPLEMENTATION WORK PACKAGES

## 123. Work-package dependency graph

```text
WP00 -> WP01 -> WP02 -> WP03 -> {WP04, WP05} -> WP06 -> WP07 -> WP08 -> WP09 -> WP10
                                      \------------------------------/
all WPs -> WP11 notebook orchestration -> WP12 tests/gates -> WP13 bundle/handoffs
```

## 124. Work-package table

| WP | Scope | Dependencies | Code | Tests | Exit |
| --- | --- | --- | --- | --- | --- |
| WP-P02-00 | Authority/reuse intake | none | authority/current-state readers; supersession rules | source exhaustion + hashes | accepted intake ledger |
| WP-P02-01 | P01 input adapters/validators | WP00 | P01 HDF5/pointer loaders; record join; no-mutation validators | contract/leakage/lineage tests | G04 PASS |
| WP-P02-02 | P02 config/schema successor foundation | WP00-01 | generalize PhaseConfig; P02 config; schema successor profiles; record builders | schema/config/fixture tests | G05-G06 PASS |
| WP-P02-03 | Training/seed/tuning/checkpoint core | WP02 | trainer registry; seed derivation; trial ledger; checkpoint/reload | unit/checkpoint/reproduction tests | branch terminal ledger valid |
| WP-P02-04 | Sanity/classical/Riemannian | WP03 | sanity + CSP/FBCSP/TS + EA/MDM gates | golden/smoke/branch tests | G08-G10 PASS |
| WP-P02-05 | Neural/conditional/SSL | WP03 | EEGNet; FBCNet; sequence slot; CBraMod adapters/gates | resource/license/checkpoint/output tests | all branch statuses explicit |
| WP-P02-06 | Prediction logging | WP04-05 | PredictionRecord builder/partitioned writer | class-order/score/cardinality tests | G14 PASS |
| WP-P02-07 | Metrics/A0 | WP06 | metric dictionary adapters; A0 evaluation; matched comparison sources | golden vectors; denominator tests | G15 PASS |
| WP-P02-08 | Low-label curves/profiles | WP07 | budget curve + subject/session profile builders | nested subset/coverage/negative point tests | G16/G17 |
| WP-P02-09 | A4 controls + unlocked-ablation executor | WP06-08 | long/multi/vote/average/fixed ensemble + generic authority-approved ablation dispatcher | A4 matching/tie/score/unlock tests | G18/G18U |
| WP-P02-10 | Failure/readiness | all execution WPs | failure index; diagnostic flags; readiness matrix | negative/failure/downstream tests | G19/G20 |
| WP-P02-11 | Kaggle orchestration | all | single notebook stage runner; resume/checkpoint state | stage coverage/resume/idempotence | 00-24 mapped |
| WP-P02-12 | Tests/gates/security | all | test catalog; gate runner; secret/path/checksum validation | full preflight | all gates executable |
| WP-P02-13 | Bundle/handoffs | WP10-12 | execution bundle + source tables + downstream handoffs | bundle/manifest/reproduction tests | G21-G24 PASS |


# PART XX - REQUIREMENT TRACEABILITY

## 125. Full authority-to-implementation matrix

| requirement_id | source_authority | source_section | Layer2_module | implementation_component | test | gate | output | downstream_consumer | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| REQ-GOV-01 | Governance V6.1 | single-track phase workflow | all | notebook orchestrator | T-BUNDLE-01 | G24 | execution bundle | project | MAPPED |
| REQ-GOV-02 | Governance V6.1 | one-notebook default | all | notebook orchestrator | T-BUNDLE-01 | G05 | notebook stage manifest | all | MAPPED |
| REQ-GOV-03 | Governance V6.1 | scope non-reduction | all | run matrix + gate engine | T-ABL-01 | G05 | run/attempt ledger | Analysis/L10 | MAPPED |
| REQ-GOV-04 | Governance V6.1 | evidence-insufficiency loopback | all | repair/reentry controller | T-FAIL-01 | G23 | repair/reentry record | Protocol/Analysis | MAPPED |
| REQ-GOV-05 | Governance V6.1 | cumulative reuse-first | M01/M08 | input adapters | T-BUD-01 | G04 | input validation report | all | MAPPED |
| REQ-GOV-06 | Governance V6.1 | full ablation coverage | owner-mapped | ablation unlock controller | T-ABL-01 | G18U | ablation ledger/evidence | Protocol/Analysis/L0/EMap/L10 | MAPPED |
| REQ-GOV-07 | Governance V6.1 | negative evidence preservation | all | failure ledger | T-FAIL-01 | G19 | FailureCaseIndex/NegativeResultNote | Analysis/L0/L10 | MAPPED |
| REQ-PSTATE-01 | Cumulative P00/P01 handoff | P02 entry readiness | M08 | preflight validator | T-READY-01 | G00 | entry validation | P02 | MAPPED |
| REQ-PSTATE-02 | Cumulative P00/P01 handoff | P01 scientific immutability | M01/M08 | input firewall | T-BUD-01 | G04 | input integrity audit | all | MAPPED |
| REQ-PSTATE-03 | Cumulative P00/P01 handoff | external artifact integrity | M01/M08 | pointer resolver | T-REC-01 | G03 | external pointer validation | reproduction | MAPPED |
| REQ-ARCH-M01 | Architecture | Layer 2 official module 1: Baseline trainer | L2-M01 | src/iharq/layer2_decoders | T-MOD-01 | G06 | checkpoints; training logs; model-registry inputs; branch terminal ledger | P03+/Analysis | MAPPED |
| REQ-ARCH-M02 | Architecture | Layer 2 official module 2: Prediction logger | L2-M02 | src/iharq/layer2_decoders | T-MOD-01 | G06 | PredictionRecord; inference logs; score-availability ledger | P03+/Analysis | MAPPED |
| REQ-ARCH-M03 | Architecture | Layer 2 official module 3: Low-calibration curve builder | L2-M03 | src/iharq/layer2_decoders | T-MOD-01 | G06 | LowCalibrationCurveRecord; curve source tables | P03+/Analysis | MAPPED |
| REQ-ARCH-M04 | Architecture | Layer 2 official module 4: Subject difficulty profiler | L2-M04 | src/iharq/layer2_decoders | T-MOD-01 | G06 | SubjectProfileRecord; descriptive source tables | P03+/Analysis | MAPPED |
| REQ-ARCH-M05 | Architecture | Layer 2 official module 5: Model-family registry | L2-M05 | src/iharq/layer2_decoders | T-MOD-01 | G06 | ModelRegistryRecord; checkpoint registry; model-card source bundle | P03+/Analysis | MAPPED |
| REQ-ARCH-M06 | Architecture | Layer 2 official module 6: Ensemble comparison builder | L2-M06 | src/iharq/layer2_decoders | T-MOD-01 | G06 | EnsembleControlRecord; disagreement tables; A4 metrics; burden notes | P03+/Analysis | MAPPED |
| REQ-ARCH-M07 | Architecture | Layer 2 official module 7: Compact SSL adapter | L2-M07 | src/iharq/layer2_decoders | T-MOD-01 | G06 | PredictionRecord; ModelRegistryRecord; admission/failure evidence | P03+/Analysis | MAPPED |
| REQ-ARCH-M08 | Architecture | Layer 2 official module 8: Downstream readiness validator | L2-M08 | src/iharq/layer2_decoders | T-MOD-01 | G06 | Layer2ReadinessReport; compatibility matrix; handoff | P03+/Analysis | MAPPED |
| REQ-METHOD-01 | Method Selection Register | SAN-MAJ: majority/frequency | M01/M05 | model builder/admission + registry | T-MOD-01 | G12 | ModelRegistryRecord + PredictionRecord or explicit terminal row | A0/A4/P03 | MAPPED |
| REQ-METHOD-02 | Method Selection Register | SAN-STRAT: seeded stratified random | M01/M05 | model builder/admission + registry | T-MOD-01 | G12 | ModelRegistryRecord + PredictionRecord or explicit terminal row | A0/A4/P03 | MAPPED |
| REQ-METHOD-03 | Method Selection Register | SAN-PERM: grouped full-pipeline source-event label permutation | M01/M05 | model builder/admission + registry | T-MOD-01 | G12 | ModelRegistryRecord + PredictionRecord or explicit terminal row | A0/A4/P03 | MAPPED |
| REQ-METHOD-04 | Method Selection Register | SAN-PRIOR: training-prior vector | M01/M05 | model builder/admission + registry | T-MOD-01 | G12 | ModelRegistryRecord + PredictionRecord or explicit terminal row | A0/A4/P03 | MAPPED |
| REQ-METHOD-05 | Method Selection Register | DIAG-LOGVAR: log-bandpower/log-variance + L2 logistic | M01/M05 | model builder/admission + registry | T-MOD-01 | G12 | ModelRegistryRecord + PredictionRecord or explicit terminal row | A0/A4/P03 | MAPPED |
| REQ-METHOD-06 | Method Selection Register | CLS-CSP-LDA: CSP + shrinkage LDA | M01/M05 | model builder/admission + registry | T-MOD-01 | G12 | ModelRegistryRecord + PredictionRecord or explicit terminal row | A0/A4/P03 | MAPPED |
| REQ-METHOD-07 | Method Selection Register | CLS-FBCSP-LR: FBCSP + L2 logistic | M01/M05 | model builder/admission + registry | T-MOD-01 | G12 | ModelRegistryRecord + PredictionRecord or explicit terminal row | A0/A4/P03 | MAPPED |
| REQ-METHOD-08 | Method Selection Register | RIE-TS-LR: shrinkage covariance -> tangent space -> L2 logistic | M01/M05 | model builder/admission + registry | T-MOD-01 | G12 | ModelRegistryRecord + PredictionRecord or explicit terminal row | A0/A4/P03 | MAPPED |
| REQ-METHOD-09 | Method Selection Register | RIE-EA-TS: train-safe Euclidean Alignment + tangent/logistic | M01/M05 | model builder/admission + registry | T-MOD-01 | G12 | ModelRegistryRecord + PredictionRecord or explicit terminal row | A0/A4/P03 | MAPPED |
| REQ-METHOD-10 | Method Selection Register | RIE-MDM: MDM/FgMDM | M01/M05 | model builder/admission + registry | T-MOD-01 | G12 | ModelRegistryRecord + PredictionRecord or explicit terminal row | A0/A4/P03 | MAPPED |
| REQ-METHOD-11 | Method Selection Register | DNN-EEGNET: EEGNet | M01/M05 | model builder/admission + registry | T-MOD-01 | G12 | ModelRegistryRecord + PredictionRecord or explicit terminal row | A0/A4/P03 | MAPPED |
| REQ-METHOD-12 | Method Selection Register | DNN-FBCNET: FBCNet | M01/M05 | model builder/admission + registry | T-MOD-01 | G12 | ModelRegistryRecord + PredictionRecord or explicit terminal row | A0/A4/P03 | MAPPED |
| REQ-METHOD-13 | Method Selection Register | DNN-SEQ: DBConformer preferred; EEG Conformer direct fallback/matched comparator | M01/M05 | model builder/admission + registry | T-MOD-01 | G12 | ModelRegistryRecord + PredictionRecord or explicit terminal row | A0/A4/P03 | MAPPED |
| REQ-METHOD-14 | Method Selection Register | DNN-EGTC: EEG-TCNet | M01/M05 | model builder/admission + registry | T-MOD-01 | G12 | ModelRegistryRecord + PredictionRecord or explicit terminal row | A0/A4/P03 | MAPPED |
| REQ-METHOD-15 | Method Selection Register | SSL-CBRAMOD: CBraMod | M01/M05 | model builder/admission + registry | T-MOD-01 | G12 | ModelRegistryRecord + PredictionRecord or explicit terminal row | A0/A4/P03 | MAPPED |
| REQ-METHOD-16 | Method Selection Register | SSL-REVE: REVE | M01/M05 | model builder/admission + registry | T-MOD-01 | G12 | ModelRegistryRecord + PredictionRecord or explicit terminal row | A0/A4/P03 | MAPPED |
| REQ-ABL-A0 | Experiment/Ablation/Evaluation Protocol + Architecture | A0: Raw Decoder / Accept-All Raw Decoder Reference | M01/M02/M03/M04/M05 | ablation/controller + source-field preparation | T-MET-01 | G15 | A0 BaselineMetricRecord + source tables | P03+ consumes immutable A0 | MAPPED |
| REQ-ABL-A1 | Experiment/Ablation/Evaluation Protocol + Architecture | A1: Calibrated Decoder / Calibration Visibility | source-producing L2 modules only | ablation/controller + source-field preparation | T-ABL-01 | G18U | prepared downstream fields / NOT_AUTHORIZED row | L3/P03 | MAPPED |
| REQ-ABL-A2 | Experiment/Ablation/Evaluation Protocol + Architecture | A2: Simple Registered Threshold / Confidence-Threshold Baseline | source-producing L2 modules only | ablation/controller + source-field preparation | T-ABL-01 | G18U | prepared downstream fields / NOT_AUTHORIZED row | L3/P03 | MAPPED |
| REQ-ABL-A3 | Experiment/Ablation/Evaluation Protocol + Architecture | A3: Uncertainty and Selective Prediction | source-producing L2 modules only | ablation/controller + source-field preparation | T-ABL-01 | G18U | prepared downstream fields / NOT_AUTHORIZED row | L3/P03 | MAPPED |
| REQ-ABL-A4 | Experiment/Ablation/Evaluation Protocol + Architecture | A4: Longer-Window, Multi-Window Voting/Averaging and Ordinary Ensemble Controls | M06 | ablation/controller + source-field preparation | T-A4-01 | G18 | EnsembleControlRecord + A4 source tables | P03+ consumes ordinary control evidence | MAPPED |
| REQ-ABL-A5 | Experiment/Ablation/Evaluation Protocol + Architecture | A5: IHARQ-lite / Rule-Based Evidence Verification | source-producing L2 modules only | ablation/controller + source-field preparation | T-ABL-01 | G18U | prepared downstream fields / NOT_AUTHORIZED row | later governed owner | MAPPED |
| REQ-ABL-A6 | Experiment/Ablation/Evaluation Protocol + Architecture | A6: IHARQ + Evidence-Quality Estimator | source-producing L2 modules only | ablation/controller + source-field preparation | T-ABL-01 | G18U | prepared downstream fields / NOT_AUTHORIZED row | later governed owner | MAPPED |
| REQ-ABL-A7 | Experiment/Ablation/Evaluation Protocol + Architecture | A7: IHARQ + RegimeRisk Temporal Trust | source-producing L2 modules only | ablation/controller + source-field preparation | T-ABL-01 | G18U | prepared downstream fields / NOT_AUTHORIZED row | later governed owner | MAPPED |
| REQ-ABL-A8 | Experiment/Ablation/Evaluation Protocol + Architecture | A8: Learning-to-defer / Deferral Comparison | source-producing L2 modules only | ablation/controller + source-field preparation | T-ABL-01 | G18U | prepared downstream fields / NOT_AUTHORIZED row | later governed owner | MAPPED |
| REQ-ABL-A9 | Experiment/Ablation/Evaluation Protocol + Architecture | A9: Supervised Adaptive-IHARQ / Adaptive Readiness Policy | source-producing L2 modules only | ablation/controller + source-field preparation | T-ABL-01 | G18U | prepared downstream fields / NOT_AUTHORIZED row | later governed owner | MAPPED |
| REQ-ABL-A10 | Experiment/Ablation/Evaluation Protocol + Architecture | A10: Contextual Bandit / Simulation-Bounded Immediate-Reward Adaptation | source-producing L2 modules only | ablation/controller + source-field preparation | T-ABL-01 | G18U | prepared downstream fields / NOT_AUTHORIZED row | later governed owner | MAPPED |
| REQ-ABL-A11 | Experiment/Ablation/Evaluation Protocol + Architecture | A11: Reinforcement-Learning Policy / Simulation-Bounded Sequential Policy Learning | source-producing L2 modules only | ablation/controller + source-field preparation | T-ABL-01 | G18U | prepared downstream fields / NOT_AUTHORIZED row | later governed owner | MAPPED |
| REQ-ABL-A12 | Experiment/Ablation/Evaluation Protocol + Architecture | A12: StressForge Stress Tests / Controlled Stress Robustness | source-producing L2 modules only | ablation/controller + source-field preparation | T-ABL-01 | G18U | prepared downstream fields / NOT_AUTHORIZED row | later governed owner | MAPPED |
| REQ-ABL-A13 | Experiment/Ablation/Evaluation Protocol + Architecture | A13: Layer 9 Simulation-Only Embodiment Demo | source-producing L2 modules only | ablation/controller + source-field preparation | T-ABL-01 | G18U | prepared downstream fields / NOT_AUTHORIZED row | later governed owner | MAPPED |
| REQ-ABL-A14 | Experiment/Ablation/Evaluation Protocol + Architecture | A14: ABSENT / PROHIBITED | none | ablation/controller + source-field preparation | T-ABL-01 | G18U | NO_POSITIVE_ARTIFACT; prohibition audit | NONE | MAPPED |
| REQ-REG-01 | Canonical Registry | PredictionRecord | Prediction logger | record builder + validator | T-REC-01 | G06 | PredictionRecord | L3-L10 | MAPPED |
| REQ-REG-02 | Canonical Registry | ModelRegistryRecord | Model-family registry | record builder + validator | T-REC-01 | G06 | ModelRegistryRecord | L3-L10/repro | MAPPED |
| REQ-REG-03 | Canonical Registry | BaselineMetricRecord | evaluation path | record builder + validator | T-REC-01 | G06 | BaselineMetricRecord | Analysis/L10/L0 | MAPPED |
| REQ-REG-04 | Canonical Registry | LowCalibrationCurveRecord | Low-calibration curve builder | record builder + validator | T-REC-01 | G06 | LowCalibrationCurveRecord | Analysis/L10 | MAPPED |
| REQ-REG-05 | Canonical Registry | SubjectProfileRecord | Subject difficulty profiler | record builder + validator | T-REC-01 | G06 | SubjectProfileRecord | L5/L6/L8/L10 as allowed | MAPPED |
| REQ-REG-06 | Canonical Registry | EnsembleControlRecord | Ensemble comparison builder | record builder + validator | T-REC-01 | G06 | EnsembleControlRecord | L3/L4/L10/evaluation | MAPPED |
| REQ-REG-07 | Canonical Registry | FailureCaseIndex | cross-cutting failure index | record builder + validator | T-REC-01 | G06 | FailureCaseIndex | Analysis/L10/L0 | MAPPED |
| REQ-REG-08 | Canonical Registry | Layer2ReadinessReport | Downstream readiness validator | record builder + validator | T-REC-01 | G06 | Layer2ReadinessReport | P03+ and release gate | MAPPED |
| REQ-REG-09 | Canonical Registry | LeakageWarningRecord | validation path | record builder + validator | T-REC-01 | G06 | LeakageWarningRecord | all affected claims/consumers | MAPPED |
| REQ-REG-10 | Canonical Registry | MatchedComparisonReport | evaluation/export adapter | record builder + validator | T-REC-01 | G06 | MatchedComparisonReport | Protocol/L10/L0 | MAPPED |
| REQ-REG-11 | Canonical Registry | NegativeResultNote | evaluation governance | record builder + validator | T-REC-01 | G06 | NegativeResultNote | Analysis/L10/L0 | MAPPED |
| REQ-REG-12 | Canonical Registry | DiagnosticOnlyFlag | evaluation/validation | record builder + validator | T-REC-01 | G06 | DiagnosticOnlyFlag | all | MAPPED |
| REQ-IN-01 | P01 handoff | DatasetRecord | M01/M08 | input adapter | T-REC-01 | G04 | validated DatasetRecord refs | all | MAPPED |
| REQ-IN-02 | P01 handoff | WindowRecord | M01/M02 | window loader | T-REC-01 | G04 | validated WindowRecord refs | models/predictions | MAPPED |
| REQ-IN-03 | P01 handoff | SplitRecord | M01/M08 | split firewall | T-LEAK-01 | G04 | split validation | all | MAPPED |
| REQ-IN-04 | P01 handoff | PreprocessingRecord | M01 | data adapter | T-LEAK-01 | G04 | preprocessing lineage | models | MAPPED |
| REQ-IN-05 | P01 handoff | LabelMapRecord | M02/M05 | label-map validator | T-SCORE-01 | G04 | class-order binding | P03+ | MAPPED |
| REQ-IN-06 | P01 handoff | low-label budget profile | M03 | budget loader | T-BUD-01 | G16 | LowCalibrationCurveRecord | Analysis | MAPPED |
| REQ-IN-07 | P01 A4 R2 | matched A4 substrate | M06 | A4 loader/matcher | T-A4-01 | G18 | A4 matched control evidence | Analysis/L10 | MAPPED |
| REQ-EVAL-01 | Method Selection + Protocol | test-set firewall | all | split visibility enforcement | T-LEAK-01 | G07 | leakage validation | all | MAPPED |
| REQ-EVAL-02 | Method Selection + Protocol | hierarchical seed lineage | M01/M05 | seed service | T-SEED-01 | G05 | seed lineage | reproduction | MAPPED |
| REQ-EVAL-03 | Method Selection + Protocol | bounded hyperparameter selection | M01/M05 | search controller | T-MOD-01 | G05 | attempt ledger + selected checkpoint | Analysis | MAPPED |
| REQ-EVAL-04 | Method Selection + Protocol | checkpoint selection | M01/M05 | checkpoint manager | T-CHK-01 | G13 | checkpoint manifest | P03/reproduction | MAPPED |
| REQ-EVAL-05 | Protocol | metric dictionary | M02/M03/M04 | metric engine | T-MET-01 | G15 | BaselineMetricRecord/source tables | Analysis/L10 | MAPPED |
| REQ-EVAL-06 | Protocol | statistical plan | M03/M04/M06 | statistics source-table builder | T-MET-01 | G05 | primitive paired/stat source tables | Protocol/Analysis | MAPPED |
| REQ-EVAL-07 | Protocol | matched comparison | M03/M06 | matcher | T-A4-01 | G18 | MatchedComparison source/report | Analysis | MAPPED |
| REQ-EVAL-08 | Nuts-and-Bolts | score/class semantics | M02/M05 | prediction serializer | T-SCORE-01 | G14 | PredictionRecord | P03+ | MAPPED |
| REQ-PLAY-01 | Phase Execution Playbook | 14-step P02 execution | all | notebook orchestrator | T-BUNDLE-01 | G24 | stage ledger | all | MAPPED |
| REQ-NB-01 | P02 master prompt | preflight and config freeze | M08/all | preflight controller | T-READY-01 | G07 | preflight gate pack | P02 | MAPPED |
| REQ-NB-02 | P02 master prompt | A0 stage | M02/M03/M04/M05 | A0 evaluator | T-MET-01 | G15 | A0 evidence | Analysis | MAPPED |
| REQ-NB-03 | P02 master prompt | A4 stage | M06 | A4 controller | T-A4-01 | G18 | A4 evidence | Analysis/L10 | MAPPED |
| REQ-NB-04 | Governance + user ablation rule | fully-unlocked ablation same-notebook executor | owner-mapped | ablation dispatcher | T-ABL-01 | G18U | additional ablation evidence/NOT_AUTHORIZED rows | Protocol/Analysis/L0/EMap/L10 | MAPPED |
| REQ-NB-05 | Execution/Evidence Plan | failure/negative accounting | all | failure index | T-FAIL-01 | G19 | FailureCaseIndex + negative results | Analysis/L0/L10 | MAPPED |
| REQ-NB-06 | Execution/Evidence Plan + Layer10 contract | figure/table source data | M02/M03/M04/M06 | source-table builders | T-BUNDLE-01 | G21 | figure/table source bundle | Layer10 | MAPPED |
| REQ-HAND-01 | Playbook | Protocol v1 handoff | M08 | handoff builder | T-READY-01 | G22 | Protocol handoff | Protocol v1.0 | MAPPED |
| REQ-HAND-02 | Playbook | Phase Analysis handoff | M08 | handoff builder | T-READY-01 | G22 | Analysis handoff | Phase Analysis | MAPPED |
| REQ-HAND-03 | Playbook | Layer 0/Evidence Map handoff | M08 | handoff builder | T-READY-01 | G22 | L0/EMap handoff | Layer0/EMap | MAPPED |
| REQ-HAND-04 | Playbook | P03 handoff | M08 | readiness + handoff | T-READY-01 | G20 | Layer2ReadinessReport + P03 handoff | P03 | MAPPED |
| REQ-BUNDLE-01 | Execution/Evidence Plan | final bundle integrity | all | release builder | T-BUNDLE-01 | G24 | immutable P02 bundle | reproduction | MAPPED |
| REQ-SEC-01 | Governance/Nuts-and-Bolts | secret-safe export | all | security scanner | T-BUNDLE-01 | G24 | secret-scan report | release | MAPPED |


## 126. Unmapped-requirement audit

```text
required_requirements_machine_mapped: 89
unmapped_required_P02_requirements: 0
status: PASS
full_task_template_section_coverage: PASS
```

# PART XXI - R4 FINALIZATION EXHAUSTION AND TRACEABILITY

## 88. Requirement traceability

The predecessor R3 requirement traceability remains scientifically valid and R4 extends finalization coverage to the complete 119-section master prompt. `machine_readable/p02_prompt_requirement_exhaustion_R4.csv` maps **119/119** numbered prompt sections to implemented evidence. `UNMAPPED_REQUIRED_P02_REQUIREMENTS = 0`.

## 89. Method traceability

`machine_readable/p02_method_traceability_R4.csv` separately maps all selected/conditional/fallback/diagnostic model branches, every A4 condition, every selected metric, and frozen statistical procedures from Method Selection → Nuts-and-Bolts behavior → module → implementation/config → run cells → outputs → tests. **35/35 rows are mapped.**

- `UNMAPPED_SELECTED_METHODS = 0`
- `SELECTED_METHODS_NOT_IMPLEMENTED = 0`
- `IMPLEMENTED_METHODS_WITHOUT_AUTHORITY = 0`
- `SELECTED_METHODS_WITH_INCOMPLETE_NUTS_AND_BOLTS_BEHAVIOR = 0`

## 90. Evaluation traceability

`machine_readable/p02_evaluation_traceability_R4.csv` freezes **12 expected P02 evaluation families**. Every family maps evaluation requirement → run cells → raw evidence → metric/statistic → record/source data → validator/gate → Phase Analysis consumer.

- `EXPECTED_P02_EVALUATIONS = 12`
- `EXPECTED_EVALUATIONS_WITH_INCOMPLETE_EXECUTION_PLAN = 0`
- `EXPECTED_P02_ANALYSES_WITHOUT_EXECUTION_EVIDENCE = 0`
- `PHASE_ANALYSIS_REQUIRED_BUT_UNEXECUTED_EVALUATIONS = 0`

## 91. Ablation traceability

`machine_readable/p02_ablation_traceability_R4.csv` independently maps A0-A14. A0 and A4 remain `FULL_EXECUTION_REQUIRED_IN_P02`; A1-A3 and A5-A13 remain downstream responsibilities; A14 remains absent/prohibited. All phase-owned full ablations have complete implementation, run-cell, Kaggle-stage, metric/comparison, failure, evidence, and downstream mappings.

- `P02_FULL_ABLATIONS_WITH_INCOMPLETE_TRACEABILITY = 0`
- `FULL_P02_ABLATIONS_WITH_UNDEFINED_IMPLEMENTATION = 0`
- `FULL_P02_ABLATIONS_WITH_UNDEFINED_RUN_CELLS = 0`
- `FULL_P02_ABLATIONS_WITH_UNDEFINED_METRICS = 0`
- `FULL_P02_ABLATIONS_WITH_UNDEFINED_COMPARISONS = 0`
- `FULL_P02_ABLATIONS_WITH_UNDEFINED_ANALYSIS_OUTPUTS = 0`
- `FULL_P02_ABLATIONS_DEFERRED_TO_PHASE_ANALYSIS = 0`
- `FULL_P02_ABLATIONS_MISSING_FROM_KAGGLE_PLAN = 0`
- `DOWNSTREAM_ABLATIONS_PREMATURELY_EXECUTED = 0`

## 92. Artifact traceability

`machine_readable/p02_artifact_traceability_R4.csv` maps all **26** required record/support-output families to producer, notebook stage, path, validator and consumer.

- `REQUIRED_ARTIFACTS_WITHOUT_PRODUCER = 0`
- `REQUIRED_ARTIFACTS_WITHOUT_VALIDATOR = 0`
- `EXPECTED_ARTIFACTS_NOT_PRODUCED_BY_DESIGN = 0`
- `EXPECTED_FIGURES_WITHOUT_SOURCE_DATA = 0`
- `EXPECTED_TABLES_WITHOUT_SOURCE_DATA = 0`
- `MISSING_REQUIRED_EXECUTION_BUNDLE_OUTPUTS = 0`

## 93. Mandatory source-utilization audit

The R4 finalizer directly reviewed and used every source family required by the master prompt. The source hash below is an intake identity, not a claim that formats have identical semantic authority.

| Source family | Review | SHA-256 | Used for |
|---|---|---|---|
| Governance V6.1 | PASS | `c811373c19a7c2c3f6d72cf2aed984e02ffcb07bb448cfc3bdbdf26a35a4f1d9` | workflow, one-notebook/full-scope, repair/evidence sequence |
| Master Architecture Specification | PASS | `ae374c9de061bc5179c9223e7d646c70cf0d98c414007ab6baf95cd68c814f9b` | P02/L2 identity, modules, boundaries, A0/A4 ownership, Module B I/O |
| Canonical Artifact/Record/Interface Registry | PASS | `bdb309f76b9b525ea89cfa56c79a9b7989348e3509febac9ae9fffe7858d1f87` | records, IDs, producers/consumers, ablation ownership |
| Execution and Evidence Plan | PASS | `f31de3453b331d909a8cccbf951a2df61ef7ca38b71df4bde8be95040095da82` | P02 evidence, sufficiency, downstream outputs |
| Experiment/Ablation/Evaluation Protocol v0.1 | PASS | `8b7a393b860bd49a34a794db5c2b80af7f127bc318a112bc7ed3c375ce704813` | fairness, splits, A0-A13, metrics/statistics/failure |
| Complete Phase Execution Playbook | PASS | `176f46950b86db8cd5c23789893955336c818a6fcd10ed36d6c66e096faccc87` | P02 operational stages, gates, handoffs |
| Method Selection and Design Rationale Register | PASS | `b036b02ac65b3bc2595513f4ca8a8137a6273f914e46e1cf6180515e57726749` | selected model/method/control/metric/status decisions |
| Detailed Design and Nuts-and-Bolts | PASS | `4f47c6f511e646b2127cc79f14a5f632b00f5112582a049b46c735e78ded638c` | method implementation behavior, I/O, fitting, failures |
| Previous/current Implementation Build Books | PASS | `05d5bb6d5b9ea2ae331c26c3f18056231361fd815e800cabd6e2ae86b7c9978b` | repository/config/test/manifest conventions and upstream implementation |
| Cumulative Protocol v1.0 through P01 | PASS | `0f4048e39ff1447e9e60d45c4f1e3b345fb3ac369abafb4f32db4ebd0ca655a3` | actual frozen P01 datasets/splits/preprocessing/windows/A4/limitations |
| Phase Analysis through P01 | PASS | `4cafbd1858043d78193d8a17e33e341530a5693285ca9803034036c51f70bb7c` | accepted execution, repairs, limitations, downstream readiness |
| Layer 0 through P01 | PASS | `780e69467b8efa56dddefd8d37c9e19289690bb6cd15a43c39e31bf5b21e832d` | claim ceilings, prohibited/qualified wording |
| Evidence Map through P01 | PASS | `17e8165e5db9fafcc2be9a0618dd8a0f87728a7ef81ed163bb9387f3797f95f8` | claim→evidence/artifact/limitation lineage |
| Layer 10 through P01 | PASS | `ca066c1b61cd632dd3370e03b9d04d62a1f46a6af92263e6687bf8a8f7702ff2` | read-only figure/table/provenance/warning conventions |
| P00 execution evidence | PASS | `c8ad7d75321fa20c47b1590c92a5dc8b3492b45f49fb7417b176484f25e15d9d` | P00 actual engineering test/runtime evidence and lessons |
| P01 execution bundle | PASS | `09c3bb0442d79ddf110cf66fc4fe61fe63e94c7d8ed9f198f606639b4191f16e` | accepted P01 execution evidence, gates/tests/manifests/checksums |
| Prior Kaggle notebook | PASS | `24f3cc58de04ebe74e9b3d28f46b55fe82fccb1f0ac5b7e8eaf5e0f38fe6b638` | working stage/resource/artifact/security patterns; not mechanically duplicated |
| P01→P02 handoff | PASS | `58183e5f06843886bd165418e575b8fd4d02fd83e0f5f48ecff00d515d0ae3b9` | freeze-critical downstream input contract |
| Cumulative project ZIP through P01 | PASS | `dc2708ab70e7746499ae09760456825b54efcf587cae3db3410e6f72b0024542` | controlling continuation state, manifests/code/configs/tests/artifacts |
| Current R3 Build Book predecessor | PASS | `b654abfb4ffa53518ab1fc7f4ab1ef1aaf60614130963850b495c59c1207f747` | predecessor implementation contract subject to R4 independent audit |
| R4 finalization master prompt | PASS | `75a40add857b4a98001a5b7288ef287b177d67590560c179abbc44bc255f3068` | controlling final audit/freeze specification |

`MANDATORY_SOURCE_FAMILIES_NOT_REVIEWED = 0`.

## 94-98. Harmony closure

| Harmony invariant | Result |
|---|---|
| `INTER_AUTHORITY_HARMONY` | PASS |
| `PRIOR_STATE_HARMONY` | PASS |
| `P00_P01_P02_HARMONY` | PASS |
| `L1_L2_L3_BOUNDARY_HARMONY` | PASS |
| `INTRA_BUILD_BOOK_HARMONY` | PASS |

The current Governance/Architecture/Registry/Execution Plan/Protocol/Playbook/Method Selection/Nuts-and-Bolts chain is compatible with the accepted P00/P01 state. R4 changes no accepted P01 evidence and no R3 planned scientific run cell/seed/budget/metric/statistical/A0/A4 condition.

## 25-27 revisited: official modules, required capabilities, and dossier completeness

The official module count remains exactly **8**. R4's `p02_l2_submodule_capability_matrix_R4.yaml` identifies **53 required implementation capabilities** across those eight modules without promoting internal capabilities into extra official modules.

| Module | Required capabilities | Missing |
|---|---:|---:|
| L2-M01 Baseline trainer | 7 | 0 |
| L2-M02 Prediction logger | 7 | 0 |
| L2-M03 Low-calibration curve builder | 6 | 0 |
| L2-M04 Subject difficulty profiler | 6 | 0 |
| L2-M05 Model-family registry | 6 | 0 |
| L2-M06 Ensemble comparison builder | 8 | 0 |
| L2-M07 Compact SSL adapter | 6 | 0 |
| L2-M08 Downstream readiness validator | 7 | 0 |

- `MISSING_OFFICIAL_L2_MODULES = 0`
- `UNAUTHORIZED_OFFICIAL_L2_MODULES = 0`
- `MISSING_REQUIRED_L2_SUBMODULES = 0`

Each official module retains the R3 A-V dossier: identity/authority, P02 purpose, reusable implementation, required change, inputs/outputs, internal/public APIs, algorithm, fit/selection/evaluation scope, configuration, invariants, validators, negative/failure states, logs, records/manifests, resources, licensing/security, ablation/evaluation role, consumers, limitations and definition of done.

# PART XXII - R4 INDEPENDENT AUDITS AND SIMULATIONS

## 102. First full authority-to-implementation audit

**PASS.** All required source families are present/used; module/method/model/record/ablation/evaluation/run/test/gate/artifact/handoff obligations have implementation evidence. Genuine defects identified by this final pass (source-family audit incompleteness, absent standalone traceability families, stale Stage-05 R2 current label, incomplete final summary/certification) are repaired in R4.

## 103. Second independent check

**PASS.** Re-reviewed from the source-authority direction rather than checking only inserted repairs. No missing official L2 module, required capability, selected method, P02-owned ablation, required evaluation, canonical output family, gate, or downstream handoff remains.

## 104. Third omission-focused check

**PASS.** The omission-focused simulation found no remaining Kaggle-time freeze-critical decision. P02 Phase Analysis can consume the planned frozen outputs without new scientific computation; Layer 10 can render source outputs read-only; P03 can consume raw scores/classes/lineage without retraining or score-semantic reverse engineering.

## 105. Adversarial review

**PASS.** Reviewed as EEG/BCI scientist, ML reviewer, thesis examiner, reproducibility auditor, software architect, Kaggle engineer, and P03 consumer. Conditional runtime facts remain fail-closed terminal outcomes, not owner decisions.

## 106. Kaggle implementation simulation

**PASS.** Every notebook stage has frozen implementation target, input, configuration, method behavior, fit/selection/evaluation scope, outputs, failures, tests, gates and export paths. The current notebook identity is `IHARQ-P02-COMPLETE-EXECUTION-AND-ANALYSIS-R4`; it consumes the unchanged R3 scientific execution freeze.

## 107. Phase Analysis simulation

**PASS.** `PHASE_ANALYSIS_REQUIRED_BUT_UNEXECUTED_EVALUATIONS = 0`. Phase Analysis interprets frozen evidence and never completes a missing P02 experiment.

## 108. Layer 10 simulation

**PASS.** `LAYER10_SCIENTIFIC_RECOMPUTATION_REQUIRED = 0` and `LAYER10_REQUIRED_SCIENTIFIC_RECOMPUTATION = 0`.

## 109. P03 simulation

**PASS.** `P03_REQUIRED_RAW_INFORMATION_MISSING = 0` and `P03_SCORE_SEMANTICS_GUESSWORK = 0`.

## 110. Finishing pass

**PASS.** Completeness, specificity, executability, traceability, consistency, previous-Build-Book uniformity, artifact/evaluation/ablation/validation/failure/downstream completeness and professional readability are closed without reducing technical scope.

# PART XXIII - ZERO-UNRESOLVED / SECURITY / DEFINITION OF DONE

## 111. Zero-unresolved certification

- `FREEZE_CRITICAL_UNRESOLVED_ITEMS = 0`
- `AUTHORITY_RESOLVABLE_UNRESOLVED_ITEMS = 0`
- `SCIENTIFIC_DECISIONS_LEFT_TO_KAGGLE = 0`
- `METHODOLOGICAL_DECISIONS_LEFT_TO_KAGGLE = 0`
- `MODEL_DECISIONS_LEFT_TO_KAGGLE = 0`
- `EVALUATION_DECISIONS_LEFT_TO_KAGGLE = 0`
- `ABLATION_DECISIONS_LEFT_TO_KAGGLE = 0`
- `METRIC_DECISIONS_LEFT_TO_KAGGLE = 0`
- `STATISTICAL_DECISIONS_LEFT_TO_KAGGLE = 0`
- `ARTIFACT_DECISIONS_LEFT_TO_KAGGLE = 0`
- `RECORD_SCHEMA_DECISIONS_LEFT_TO_KAGGLE = 0`
- `BLOCKING_OWNER_DECISIONS = 0`

Runtime availability/license/checkpoint/resource compatibility remains a measured fail-closed preflight fact. It cannot authorize new methods, substitute versions, change scientific constants, or create a second execution mode.

## 112. Secret/security certification

`SECRETS = 0`. The future notebook design retains secret redaction, no token serialization, no credential printing, safe paths, final secret scan and fail-closed export.

## 113. Definition-of-done result

All prompt Section 113 checks are implemented and validated. In particular: all seven authorities and governed P00/P01 products are used; 8/8 official modules and 53/53 required capabilities are represented; 16/16 model branches are dispositioned; 12/12 record families and 26/26 record/support artifact families are mapped; A0/A4 are fully executable/evaluable; downstream ablations are not stolen; A14 is absent/prohibited; all required evaluations/runs/metrics/statistics/tests/gates/notebook stages/handoffs are complete in design; no result-dependent design or quality-reducing execution mode is permitted.

# PART XXIV - FINAL VALIDATION SUMMARY AND FREEZE

## 114. Final validation summary

| Validation item | Final result |
|---|---|
| Target phase | P02 |
| Target layer | L2 |
| Governance | PASS |
| Seven-authority exhaustion | PASS |
| Previous Build Book intake | PASS |
| Protocol v1.0 intake | PASS |
| Phase Analysis intake | PASS |
| Layer 0 intake | PASS |
| Evidence Map intake | PASS |
| Layer 10 intake | PASS |
| Execution-evidence intake | PASS |
| Prior-notebook intake | PASS |
| P01→P02 handoff intake | PASS |
| Cumulative ZIP intake | PASS |
| Authority-resolvable decisions | 3/3 |
| Blocking owner decisions | 0 |
| Official L2 modules | 8/8 |
| Required L2 submodules/capabilities | 53/53 |
| Method Selection coverage | PASS |
| Nuts-and-Bolts implementation coverage | PASS |
| Required/core model branches | 7/7 |
| Conditional branches | 4/4 |
| Fallback branches | 1/1 |
| Diagnostic branches | 4/4 |
| Canonical inputs | 8/8 |
| Canonical records | 12/12 |
| Required record/support artifact families | 26/26 |
| A0–A13 ownership/disposition | PASS |
| Full-execution ablations expected in P02 | 2 |
| Fully implemented | 2/2 |
| In run matrix | 2/2 |
| In Kaggle plan | 2/2 |
| Fully evaluated in design | 2/2 |
| Improperly deferred | 0 |
| A14 | ABSENT |
| Required P02 evaluations | 12 |
| Fully implemented in Kaggle plan | 12/12 |
| Missing evaluation implementations | 0 |
| Run matrix | PASS |
| Seed policy | PASS |
| Budget policy | PASS |
| Metrics | PASS |
| Statistics/evaluation | PASS |
| Split visibility | PASS |
| Leakage | PASS |
| Class order | PASS |
| Score semantics | PASS |
| Checkpoint governance | PASS |
| Environment | PASS — pins frozen; Kaggle preflight resolver verification required before science |
| Resources | PASS |
| Licenses | PASS |
| Security | PASS |
| Tests | PASS |
| Negative tests | PASS |
| Gates | PASS |
| Playbook coverage | PASS |
| Kaggle stage coverage | PASS |
| One-notebook full-scope compliance | PASS |
| Execution bundle | PASS |
| Figure-source readiness | PASS |
| Table-source readiness | PASS |
| Protocol v1 handoff | PASS |
| Phase Analysis handoff | PASS |
| Layer 0 handoff | PASS |
| Evidence Map handoff | PASS |
| Layer 10 handoff | PASS |
| P03 handoff | PASS |
| Requirement traceability | PASS |
| Method traceability | PASS |
| Evaluation traceability | PASS |
| Ablation traceability | PASS |
| Artifact traceability | PASS |
| Inter-authority harmony | PASS |
| Prior-state harmony | PASS |
| P00→P01→P02 harmony | PASS |
| L1→L2→L3 harmony | PASS |
| Intra-Build-Book harmony | PASS |
| First audit | PASS |
| Second independent audit | PASS |
| Third omission audit | PASS |
| Adversarial audit | PASS |
| Kaggle simulation | PASS |
| Phase Analysis simulation | PASS |
| Layer 10 simulation | PASS |
| P03 simulation | PASS |
| Finishing pass | PASS |
| Scientific decisions left to Kaggle | 0 |
| Method decisions left to Kaggle | 0 |
| Ablation decisions left to Kaggle | 0 |
| Evaluation decisions left to Kaggle | 0 |
| Metric/statistics decisions left to Kaggle | 0 |
| Artifact/schema decisions left to Kaggle | 0 |
| Freeze-critical unresolved items | 0 |
| Secrets | 0 |
| Freeze-critical blockers | 0 |
| READY FOR P02 KAGGLE NOTEBOOK AUTHORING | YES |

## Complete invariant closure

- `MODEL_BRANCHES_WITH_UNDEFINED_STATUS = 0`
- `UNNECESSARY_REIMPLEMENTATION = 0`
- `UNNECESSARY_P01_ARTIFACT_REGENERATION = 0`
- `INCOMPLETE_REQUIRED_RECORD_DEFINITIONS = 0`
- `MISSING_REQUIRED_RUN_CELLS = 0`
- `FREEZE_CRITICAL_BEHAVIORS_WITHOUT_TEST_OR_VALIDATION = 0`
- `MISSING_REQUIRED_P02_GATES = 0`
- `UNMAPPED_P02_PLAYBOOK_STEPS = 0`
- `REQUIRED_P02_BEHAVIORS_WITHOUT_KAGGLE_STAGE = 0`
- `RELEVANT_P01_LIMITATIONS_LOST_AT_P02_BOUNDARY = 0`
- `P02_ANALYSIS_REQUIREMENTS_WITHOUT_PLANNED_EVIDENCE = 0`
- `P03_REQUIRED_PREDICTION_FIELDS_MISSING = 0`

## 115. Success condition — exact controlling certification

```text
P02_LAYER2_IMPLEMENTATION_BUILD_BOOK_FINALIZATION:

PASS — STRETCH-COMPLETE,
AUTHORITY-EXHAUSTED,
DOUBLE-CHECKED,
TRIPLE-CHECKED,
EVALUATION-COMPLETE,
ABLATION-COMPLETE,
FINALIZED,
FROZEN,
AND READY FOR KAGGLE NOTEBOOK AUTHORING
```

```text
P02 execution:
NOT YET STARTED

P02 implementation contract:
FINALIZED_AND_FROZEN

authority utilization:
COMPLETE

P00/P01 state utilization:
COMPLETE

Layer 2 module coverage:
COMPLETE

Layer 2 submodule coverage:
COMPLETE

Method Selection coverage:
COMPLETE

Nuts-and-Bolts coverage:
COMPLETE

canonical artifact coverage:
COMPLETE

P02 evaluation coverage:
COMPLETE

P02-owned ablation coverage:
COMPLETE

P02-owned ablations:
FULLY IMPLEMENTED FOR KAGGLE EXECUTION

A14:
ABSENT_PROHIBITED

required figure/table source data:
PLANNED

Phase Analysis evidence:
FULLY PREPLANNED

Layer 10 source state:
FULLY PREPLANNED

P03 raw-prediction contract:
COMPLETE

unnecessary upstream regeneration:
NONE

scientific decisions left to Kaggle:
0

methodological decisions left to Kaggle:
0

ablation decisions left to Kaggle:
0

evaluation decisions left to Kaggle:
0

metric/statistics decisions left to Kaggle:
0

artifact/schema decisions left to Kaggle:
0

blocking owner decisions:
0

freeze-critical unresolved items:
0

freeze-critical blockers:
0

NEXT GOVERNED STEP:
CREATE THE COMPLETE PHASE 02 KAGGLE
EXECUTION AND ANALYSIS NOTEBOOK
DIRECTLY FROM THIS FROZEN BUILD BOOK
```

## 116. Blocked condition

Not invoked. No genuine freeze-critical blocker remains. Cosmetic/runtime facts do not qualify as blockers unless they violate the frozen preflight contract.

## 117. Revision logic

R4 is justified because the final master prompt exposed canonical finalization defects in R3's **source-exhaustion/traceability/final-certification layer**, not in R3's scientific experiment design. R3 is preserved under `history/R3/`. The R3 planned scientific execution freeze, run-cell design, seeds, budgets, metrics/statistics, A0/A4 conditions and P01 immutable-input contract are adopted unchanged unless explicitly identified otherwise above. During the final packaging audit, a mislabeled current-surface `p02_notebook_stage_plan_R3.yaml` that had inherited the R4 notebook identity was removed; the genuine R3 predecessor plan was restored under `history/R3/machine_readable/`, while `p02_notebook_stage_plan_R4.yaml` remains the current notebook-authoring derivative. This provenance repair changes no science.

## 118. Final command completion

The complete independent reconstruction, double-check, triple-check, omission review, adversarial review, Kaggle simulation, Phase Analysis simulation, Layer 10 simulation, P03 simulation, repair, derivative regeneration, validation and freeze have been performed. P02 scientific execution remains not started.

# APPENDIX A - R4 source hashes and predecessor identities

- R3 canonical predecessor SHA-256: `b654abfb4ffa53518ab1fc7f4ab1ef1aaf60614130963850b495c59c1207f747`
- Current finalization prompt SHA-256: `75a40add857b4a98001a5b7288ef287b177d67590560c179abbc44bc255f3068`
- Cumulative P00+P01 ZIP SHA-256: `dc2708ab70e7746499ae09760456825b54efcf587cae3db3410e6f72b0024542`
- P01 execution bundle SHA-256: `09c3bb0442d79ddf110cf66fc4fe61fe63e94c7d8ed9f198f606639b4191f16e`

# APPENDIX B - R4 derivative authority boundary

The Markdown Build Book is the canonical P02 implementation authority. DOCX is a format derivative. Machine-readable matrices/validators are deterministic derivatives used for notebook authoring and audit; they do not supersede Architecture/Registry/Governance/Protocol or the canonical Build Book.

# R4 ZERO-UNRESOLVED EXECUTION CERTIFICATION

The P02/L2 Build Book R4 is the final implementation authority for notebook construction. Conditional external branches may terminate as deterministic `RESOURCE_BLOCKED`, `LICENSE_BLOCKED`, `CHECKPOINT_BLOCKED`, `INPUT_INCOMPATIBLE`, or other governed states when runtime facts demand it; such terminal states are not missing design choices.

**Final Build Book decision:** `PASS — STRETCH-COMPLETE / AUTHORITY-EXHAUSTED / DOUBLE-CHECKED / TRIPLE-CHECKED / EVALUATION-COMPLETE / ABLATION-COMPLETE / FINALIZED / FROZEN / READY FOR KAGGLE NOTEBOOK AUTHORING`.
