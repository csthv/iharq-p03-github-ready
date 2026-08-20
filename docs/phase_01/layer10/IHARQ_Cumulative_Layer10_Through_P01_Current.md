# IHARQ Cumulative Layer 10 Reproducibility and Presentation Package Through P01

**Canonical Layer 10 ID:** `IHARQ-CUMULATIVE-LAYER10-THROUGH-P01-R1`  
**Release ID:** `P00-P01-LAYER10-RELEASE-R1`  
**Status:** `PASS — FINALIZED AND FROZEN`  
**Authority boundary:** Layer 10 is rendering/presentation/reproduction-package authority only; it cannot supersede Evidence Map, Layer 0, Phase Analysis, Protocol, or execution evidence.

## Executive Decision

P00 Layer 10 is preserved byte-for-byte as the validated R2 predecessor. P01 Layer 10 is added as an Evidence-Map-driven, read-only rendering layer. No scientific source value, finding, reviewed claim wording, Protocol rule, Evidence Map relation, or execution artifact is modified.

| Surface | Final state |
|---|---|
| P00 Layer 10 | PRESERVED |
| P01 eligible Evidence Map claims | PROCESSED |
| Source values changed | NO |
| Layer 0 reviewed wording changed | NO |
| Evidence Map changed | NO |
| A14 | ABSENT / PROHIBITED |
| A4 effectiveness | NOT PRESENTED AS ESTABLISHED IN P01 |
| Clinical/deployment effectiveness | NOT PRESENTED AS ESTABLISHED IN P01 |
| Negative evidence | VISIBLE |
| Read-only status | PASS |
| Next governed step | FINAL P01 WHOLE-STACK SYNCHRONIZATION / CLOSURE / P02 AUTHORIZATION REVIEW |

# Part I — Layer 10 Governance and Read-Only Contract

## 1. Authority chain

`Layer 0 reviewed claim → Evidence Map row → Layer 10 rendering`. Layer 10 never creates a claim from a raw result.

## 2. Consolidation statement

- `P00_LAYER10_PRESERVED = YES`
- `P01_LAYER10_ADDED = YES`
- `CUMULATIVE_LAYER10_CREATED = YES`
- `MEASUREMENTS_CHANGED = NO`
- `FINDINGS_CHANGED = NO`
- `PROTOCOL_CHANGED = NO`
- `LAYER0_REVIEWED_WORDING_CHANGED = NO`
- `EVIDENCE_MAP_CHANGED_BY_LAYER10 = NO`

# Part II — P00 Preservation

The complete current P00 Layer 10 directories from `P00-BASIC-LAYER10-PACKAGE-R2` are embedded under `preserved_p00_layer10/`. Manifest-bound predecessor files were rehashed and all matched their R2 hashes.

| P00 surface | Count / status |
|---|---|
| Views | 14 preserved |
| Cards | 14 preserved |
| Exports | 14 preserved |
| Source-value reproduction | preserved PASS |
| Warning parity | preserved PASS |
| Negative visibility | preserved PASS |
| Unexplained artifact loss | 0 |

# Part III — P01 Governed Source State

## 3. Core source inventory

| dataset | subjects | source_files | source_events | accepted_events | source_hz | license | record_id |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PhysioNetMI | 109 | 327 | 9509 | 4918 | 128, 160 | ODC-By-1.0 | IHARQ-DATASETRECORD-20260806-66309cda68771bef |
| BNCI2014_001 | 9 | 18 | 5184 | 2592 | 250 | CC BY-ND 4.0 | IHARQ-DATASETRECORD-20260806-42c424800627b6ee |
| Lee2019_MI | 54 | 108 | 5400 | 5400 | 1000 | GPL-3.0 (maintained source card) | IHARQ-DATASETRECORD-20260806-adb91f25a65e588e |


## 4. Split

Subject is the split unit. The cumulative accepted split is 102 / 35 / 17 / 18 subject groups across train/calibration/validation/test. Leakage wording remains bounded to the implemented registered checks.

| role | subject_groups | core_windows | subject_pct | window_pct |
| --- | --- | --- | --- | --- |
| train | 102 | 7589 | 59.3 | 58.78 |
| calibration | 35 | 2655 | 20.35 | 20.57 |
| validation | 17 | 1283 | 9.88 | 9.94 |
| test | 18 | 1383 | 10.47 | 10.71 |


## 5. Preprocessing contract

| step | contract |
| --- | --- |
| Source-unit validation | Preserve provider units/metadata; reject unresolved unit ambiguity |
| EEG selection | EEG-only branch; no non-EEG channels in official core |
| Demeaning | Continuous-run demeaning before event window extraction |
| Average reference | Continuous-run average reference |
| Joint resampling | Signal and events jointly resampled to 160 Hz with polyphase resampling; Kaiser β=5.0 |
| Band-pass filtering | 8–32 Hz, 4th-order Butterworth SOS, zero-phase; odd padding; padlen 27 |
| Storage dtype | float32 |
| Official windowing | cue +0.5 to +3.5 s, 480 samples; reject out-of-bounds; no clipping |


## 6. Core data product

Official core: cue +0.5→+3.5 s, 480 samples @160 Hz, 12,910/12,910 accepted-event conservation, 0 invalid official core windows, 172 lossless HDF5 subject shards.

## 7. Quality

489 recording/run summaries, 20 soft/provider flags, 0 hard-invalid summaries, 0/12,910 invalid core windows. **Soft/provider flag ≠ corruption.**

## 8. A4 R2

A4 R2: +0.0→+3.5 s, 560 samples @160 Hz with virtual 2-s views `0:320`, `120:440`, `240:560`; 12,910/12,910 matched parents; 172 shards; no padding/clipping/fabrication/parent loss. **P01 established substrate readiness only; A4 effectiveness was not evaluated in P01.**

## 9. Execution closure

27/27 accepted stages; 16/16 deterministic P01 gates; 50/50 regression tests; 0 unresolved blockers; 13,164/13,164 execution-bundle checksum targets verified. This is **execution/reproducibility closure**, not model-effectiveness validation.

# Part IV — P01 Layer 10 Views

The following 20 source-bound views satisfy the required P01 presentation families without manufacturing redundant charts.

## L10-P01-VIEW-001 — P00→P01 Progression
Show the governed transition from engineering foundation to public-data foundation
**Status:** `CURRENT_RENDERED`
**Claims:** `P01-CLM-001/v1`
**Warnings:** PUBLIC_EEG_ONLY; NON_CLINICAL; BINARY_MI_BRANCH_SCOPE
**Artifact:** `views/p01/L10-P01-VIEW-001.md`

## L10-P01-VIEW-002 — Dataset / Source Inventory
Render the three activated P01 sources and exact governed inventory
**Status:** `CURRENT_RENDERED`
**Claims:** `P01-CLM-001/v1`
**Warnings:** PUBLIC_EEG_ONLY; NON_CLINICAL; BINARY_MI_BRANCH_SCOPE
**Artifact:** `views/p01/L10-P01-VIEW-002.md`

## L10-P01-VIEW-003 — Accepted Event → Window Denominator
Show source events, accepted binary events and one-to-one official core materialization
**Status:** `CURRENT_RENDERED`
**Claims:** `P01-CLM-001/v1;P01-CLM-003/v1`
**Warnings:** NO_MODEL_EFFECT_INFERENCE
**Artifact:** `views/p01/L10-P01-VIEW-003.md`

## L10-P01-VIEW-004 — Subject-Grouped Split
Show exact subject-group and window allocation by role
**Status:** `CURRENT_RENDERED`
**Claims:** `P01-CLM-002/v1`
**Warnings:** IMPLEMENTED_CHECKS_ONLY — leakage conclusion is bounded to the implemented registered checks
**Artifact:** `views/p01/L10-P01-VIEW-004.md`

## L10-P01-VIEW-005 — Frozen Preprocessing Flow
Show the actual frozen P01 preprocessing sequence
**Status:** `CURRENT_RENDERED`
**Claims:** `NO_DIRECT_REVIEWED_CLAIM_REQUIRED`
**Warnings:** No preprocessing-effectiveness inference
**Artifact:** `views/p01/L10-P01-VIEW-005.md`

## L10-P01-VIEW-006 — Official Core Window
Show the official cue-relative timing contract
**Status:** `CURRENT_RENDERED`
**Claims:** `P01-CLM-003/v1`
**Warnings:** NO_MODEL_EFFECT_INFERENCE
**Artifact:** `views/p01/L10-P01-VIEW-006.md`

## L10-P01-VIEW-007 — Quality / Flag Summary
Show governed quality outcomes and annotation policy
**Status:** `CURRENT_RENDERED`
**Claims:** `P01-CLM-005/v1`
**Warnings:** SOFT_FLAG_NOT_EQUIVALENT_TO_CORRUPTION — 0 hard-invalid does not mean artifact-free EEG
**Artifact:** `views/p01/L10-P01-VIEW-007.md`

## L10-P01-VIEW-008 — External Core Dataset
Show version-pinned core persistence and retrieval
**Status:** `CURRENT_RENDERED`
**Claims:** `P01-CLM-004/v1`
**Warnings:** PRIVATE_KAGGLE_EXTERNAL_ARTIFACT_ACCESS; SOURCE_LICENSE_REDISTRIBUTION_CONSTRAINTS
**Artifact:** `views/p01/L10-P01-VIEW-008.md`

## L10-P01-VIEW-009 — A0–A13 Readiness
Show readiness identities without implying effectiveness
**Status:** `CURRENT_RENDERED`
**Claims:** `P01-CLM-006/v1`
**Warnings:** NO_ABLATION_EFFECTIVENESS_IN_P01; READY ≠ EFFECTIVE
**Artifact:** `views/p01/L10-P01-VIEW-009.md`

## L10-P01-VIEW-010 — A14 Prohibition
Keep A14 visibly absent/prohibited
**Status:** `CURRENT_RENDERED`
**Claims:** `P01-CLM-006/v1`
**Warnings:** A14 must never be rendered as active or effective
**Artifact:** `views/p01/L10-P01-VIEW-010.md`

## L10-P01-VIEW-011 — A4 R2 Timing / Readiness
Show exact A4 R2 timing and matched-parent substrate
**Status:** `CURRENT_RENDERED`
**Claims:** `P01-CLM-007/v1;P01-CLM-011/v1`
**Warnings:** P01 established A4 substrate readiness only; A4 effectiveness was not evaluated in P01.; A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01
**Artifact:** `views/p01/L10-P01-VIEW-011.md`

## L10-P01-VIEW-012 — A4 Infeasibility → R2 Repair
Preserve the negative feasibility result and governed repair chronology
**Status:** `CURRENT_RENDERED`
**Claims:** `P01-CLM-007/v1;P01-CLM-011/v1`
**Warnings:** NEGATIVE FEASIBILITY / GOVERNED DESIGN REPAIR; not model effectiveness
**Artifact:** `views/p01/L10-P01-VIEW-012.md`

## L10-P01-VIEW-013 — Environment / Resource Amendments
Show actual accepted runtime and adaptive resource policy
**Status:** `CURRENT_RENDERED`
**Claims:** `P01-CLM-009/v1`
**Warnings:** Compatibility/resource evidence only; no scientific-performance inference
**Artifact:** `views/p01/L10-P01-VIEW-013.md`

## L10-P01-VIEW-014 — Stage / Gate / Test Closure
Render final execution closure
**Status:** `CURRENT_RENDERED`
**Claims:** `P01-CLM-008/v1`
**Warnings:** EXECUTION / REPRODUCIBILITY CLOSURE — NOT EFFECTIVENESS
**Artifact:** `views/p01/L10-P01-VIEW-014.md`

## L10-P01-VIEW-015 — Repair / Rerun Provenance
Show material repairs without traceback noise
**Status:** `CURRENT_RENDERED`
**Claims:** `P01-CLM-008/v1`
**Warnings:** Historical failures are lineage; current accepted evidence controls positive closure claims
**Artifact:** `views/p01/L10-P01-VIEW-015.md`

## L10-P01-VIEW-016 — Negative / Deferred / Rejected Claims
Keep unsupported states visible
**Status:** `CURRENT_RENDERED`
**Claims:** `P01-CLM-011/v1;P01-CLM-012/v1`
**Warnings:** Do not render either as a positive result
**Artifact:** `views/p01/L10-P01-VIEW-016.md`

## L10-P01-VIEW-017 — Limitation / Claim-Ceiling Index
Render major P01 limitations and evidence ceilings
**Status:** `CURRENT_RENDERED`
**Claims:** `P01-CLM-001/v1;P01-CLM-002/v1;P01-CLM-003/v1;P01-CLM-004/v1;P01-CLM-005/v1;P01-CLM-006/v1;P01-CLM-007/v1;P01-CLM-008/v1;P01-CLM-009/v1;P01-CLM-010/v1;P01-CLM-011/v1;P01-CLM-012/v1`
**Warnings:** Warnings must remain proximate to affected claim-bearing outputs
**Artifact:** `views/p01/L10-P01-VIEW-017.md`

## L10-P01-VIEW-018 — P01→P02 Technical Handoff
Show exact inherited data contract without predicting P02 success
**Status:** `CURRENT_RENDERED`
**Claims:** `P01-CLM-010/v1`
**Warnings:** TECHNICAL INPUT READY ≠ P02 SCIENTIFIC RESULT; DOCUMENTARY_CLOSURE_SEQUENCE_REMAINS
**Artifact:** `views/p01/L10-P01-VIEW-018.md`

## L10-P01-VIEW-019 — Claim → Evidence → Artifact Provenance
Provide audit chain for all P01 reviewed claims
**Status:** `CURRENT_RENDERED`
**Claims:** `P01-CLM-001/v1;P01-CLM-002/v1;P01-CLM-003/v1;P01-CLM-004/v1;P01-CLM-005/v1;P01-CLM-006/v1;P01-CLM-007/v1;P01-CLM-008/v1;P01-CLM-009/v1;P01-CLM-010/v1;P01-CLM-011/v1;P01-CLM-012/v1`
**Warnings:** Layer 10 renders Evidence Map routes; it does not create new routes
**Artifact:** `views/p01/L10-P01-VIEW-019.md`

## L10-P01-VIEW-020 — Reproduction / Retrieval Index
Make governed reproduction inputs discoverable
**Status:** `CURRENT_RENDERED`
**Claims:** `P01-CLM-001/v1;P01-CLM-002/v1;P01-CLM-003/v1;P01-CLM-004/v1;P01-CLM-005/v1;P01-CLM-006/v1;P01-CLM-007/v1;P01-CLM-008/v1;P01-CLM-009/v1;P01-CLM-010/v1;P01-CLM-011/v1;P01-CLM-012/v1`
**Warnings:** Private Kaggle access and source-license compliance may be required
**Artifact:** `views/p01/L10-P01-VIEW-020.md`

# Part V — P01 Claim Cards

Every P01 reviewed claim has a governed card or negative-view card; exact reviewed wording is reproduced from Layer 0/Evidence Map.

## L10-P01-CARD-001-v1 — P01-CLM-001/v1
**Disposition:** `APPROVED_WITH_QUALIFICATIONS`  
**Layer 10 state:** `ELIGIBLE_WITH_MANDATORY_WARNING`

Within the frozen P01 binary motor-imagery branch, Phase 1 established a checksum-bound, provenance-traceable foundation over the three activated public EEG datasets.

**Mandatory limitations:** PUBLIC_EEG_ONLY, NON_CLINICAL, BINARY_MI_BRANCH_SCOPE
**Warning:** PUBLIC_EEG_ONLY; NON_CLINICAL; BINARY_MI_BRANCH_SCOPE

## L10-P01-CARD-002-v1 — P01-CLM-002/v1
**Disposition:** `APPROVED_WITH_QUALIFICATIONS`  
**Layer 10 state:** `ELIGIBLE_WITH_MANDATORY_WARNING`

The frozen P01 split assigned 172 subject groups wholly and disjointly across train, calibration, validation, and test roles and passed the implemented registered leakage/disjointness checks; this does not prove that every conceivable leakage mechanism is impossible.

**Mandatory limitations:** IMPLEMENTED_CHECKS_ONLY
**Warning:** IMPLEMENTED_CHECKS_ONLY

## L10-P01-CARD-003-v1 — P01-CLM-003/v1
**Disposition:** `APPROVED`  
**Layer 10 state:** `ELIGIBLE_FOR_LAYER10`

Under the frozen official core-window policy, all 12,910 accepted events yielded 12,910 valid core windows, with 0/12,910 invalid official core windows.

**Mandatory limitations:** NO_MODEL_EFFECT_INFERENCE
**Warning:** NO_MODEL_EFFECT_INFERENCE

## L10-P01-CARD-004-v1 — P01-CLM-004/v1
**Disposition:** `APPROVED_WITH_QUALIFICATIONS`  
**Layer 10 state:** `ELIGIBLE_WITH_MANDATORY_WARNING`

The official P01 core numerical artifact was persisted as 172 lossless HDF5 subject shards covering 12,910 windows and was verified under its Kaggle provider-version/logical-revision/manifest-hash identity contract.

**Mandatory limitations:** PRIVATE_KAGGLE_EXTERNAL_ARTIFACT_ACCESS, SOURCE_LICENSE_REDISTRIBUTION_CONSTRAINTS
**Warning:** PRIVATE_KAGGLE_EXTERNAL_ARTIFACT_ACCESS; SOURCE_LICENSE_REDISTRIBUTION_CONSTRAINTS

## L10-P01-CARD-005-v1 — P01-CLM-005/v1
**Disposition:** `APPROVED_WITH_QUALIFICATIONS`  
**Layer 10 state:** `ELIGIBLE_WITH_MANDATORY_WARNING`

P01 applied the ANNOTATE_NOT_REPAIR quality policy across 489 quality summaries: 20 soft/provider flags were retained, 0/489 summaries were hard-invalid, and 0/12,910 official core windows were invalid under the registered criteria.

**Mandatory limitations:** SOFT_FLAG_NOT_EQUIVALENT_TO_CORRUPTION
**Warning:** SOFT_FLAG_NOT_EQUIVALENT_TO_CORRUPTION

## L10-P01-CARD-006-v1 — P01-CLM-006/v1
**Disposition:** `APPROVED_WITH_QUALIFICATIONS`  
**Layer 10 state:** `ELIGIBLE_WITH_MANDATORY_WARNING`

P01 established Layer-1 foundation readiness for each official A0-A13 identity; none of these ablation-effectiveness experiments was executed in P01, and A14 remained absent/prohibited.

**Mandatory limitations:** NO_ABLATION_EFFECTIVENESS_IN_P01
**Warning:** NO_ABLATION_EFFECTIVENESS_IN_P01

## L10-P01-CARD-007-v1 — P01-CLM-007/v1
**Disposition:** `APPROVED_WITH_QUALIFICATIONS`  
**Layer 10 state:** `ELIGIBLE_WITH_MANDATORY_WARNING`

P01 established a fully matched A4 R2 Layer-1 data substrate for future governed evaluation: 12,910/12,910 parent events are represented without padding, clipping, fabricated samples, or parent-event loss. A4 R2 arose after the +4.0 s feasibility failure and was not evaluated for decoder effectiveness in P01.

**Mandatory limitations:** A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01, A4_EFFECTIVENESS_NOT_EXECUTED
**Warning:** A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01; A4_EFFECTIVENESS_NOT_EXECUTED

## L10-P01-CARD-008-v1 — P01-CLM-008/v1
**Disposition:** `APPROVED`  
**Layer 10 state:** `ELIGIBLE_FOR_LAYER10`

The accepted P01 execution completed 27/27 registered stages, 16/16 deterministic P01 gates, and 50/50 regression tests with 0 unresolved blockers; final execution-bundle integrity checks also closed.

**Mandatory limitations:** NO_EFFECTIVENESS_INFERENCE
**Warning:** NO_EFFECTIVENESS_INFERENCE

## L10-P01-CARD-009-v1 — P01-CLM-009/v1
**Disposition:** `APPROVED_WITH_QUALIFICATIONS`  
**Layer 10 state:** `ELIGIBLE_WITH_MANDATORY_WARNING`

The accepted P01 run used Python 3.12.13 under a documented compatibility amendment and the governed adaptive-disk policy P01-L1-KAGGLE-ADAPTIVE-DISK-R1; the accepted records show no change to the frozen datasets, labels, subject split, core preprocessing, core window policy, or 12,910-event denominator attributable to these runtime/resource amendments.

**Mandatory limitations:** ACTUAL_RUNTIME_PYTHON_3_12_13_WITH_COMPATIBILITY_AMENDMENT, ADAPTIVE_DISK_RESOURCE_AMENDMENT
**Warning:** ACTUAL_RUNTIME_PYTHON_3_12_13_WITH_COMPATIBILITY_AMENDMENT; ADAPTIVE_DISK_RESOURCE_AMENDMENT

## L10-P01-CARD-010-v1 — P01-CLM-010/v1
**Disposition:** `APPROVED_WITH_QUALIFICATIONS`  
**Layer 10 state:** `ELIGIBLE_WITH_MANDATORY_WARNING`

P01 freezes a technical Layer-1 data contract that P02 may consume using the recorded dataset, label-map, split, preprocessing, core-window, and external-artifact identities; silent relabeling, rewindowing, split mutation, denominator substitution, or test-visibility leakage is prohibited. This is technical readiness, not evidence of P02 scientific success.

**Mandatory limitations:** DOCUMENTARY_CLOSURE_SEQUENCE_REMAINS
**Warning:** DOCUMENTARY_CLOSURE_SEQUENCE_REMAINS

## L10-P01-CARD-011-v1 — P01-CLM-011/v1
**Disposition:** `DEFERRED`  
**Layer 10 state:** `NEGATIVE_VIEW_ONLY`

P01 did not evaluate whether A4 R2 improves decoder performance relative to the core window; that effectiveness question remains deferred to a future governed matched downstream experiment.

**Mandatory limitations:** A4_EFFECTIVENESS_NOT_EXECUTED, A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01
**Warning:** A4_EFFECTIVENESS_NOT_EXECUTED; A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01

## L10-P01-CARD-012-v1 — P01-CLM-012/v1
**Disposition:** `REJECTED`  
**Layer 10 state:** `NEGATIVE_VIEW_ONLY`

P01 is a public, non-clinical data-foundation and execution-validation phase; it does not establish clinical effectiveness, patient benefit, deployment safety, or medical-device readiness.

**Mandatory limitations:** PUBLIC_EEG_ONLY, NON_CLINICAL, NO_DEPLOYMENT_CLAIM
**Warning:** PUBLIC_EEG_ONLY; NON_CLINICAL; NO_DEPLOYMENT_CLAIM

# Part VI — Figures

All figures are source-bound display transformations only. PNG and SVG exports are provided together with JSON source manifests.

## P01-FIG-SRC-001 — P00→P01 progression
Claims: `P01-CLM-001/v1`  
Warning: PUBLIC_EEG_ONLY; NON_CLINICAL; no model-effectiveness inference  
Exports: `figures/exports/P01-FIG-SRC-001.png`, `figures/exports/P01-FIG-SRC-001.svg`

## P01-FIG-SRC-002 — Source → accepted event → core window flow
Claims: `P01-CLM-001/v1;P01-CLM-003/v1`  
Warning: Denominator/accounting only; not model performance  
Exports: `figures/exports/P01-FIG-SRC-002.png`, `figures/exports/P01-FIG-SRC-002.svg`

## P01-FIG-SRC-003 — Subject split allocation
Claims: `P01-CLM-002/v1`  
Warning: IMPLEMENTED_CHECKS_ONLY  
Exports: `figures/exports/P01-FIG-SRC-003.png`, `figures/exports/P01-FIG-SRC-003.svg`

## P01-FIG-SRC-004 — Preprocessing chain
Claims: `NO_DIRECT_REVIEWED_CLAIM_REQUIRED`  
Warning: Implementation contract only; no preprocessing-effectiveness inference  
Exports: `figures/exports/P01-FIG-SRC-004.png`, `figures/exports/P01-FIG-SRC-004.svg`

## L10-P01-FIG-CORE-WINDOW — Official core window
Claims: `P01-CLM-003/v1`  
Warning: NO_MODEL_EFFECT_INFERENCE  
Exports: `figures/exports/L10-P01-FIG-CORE-WINDOW.png`, `figures/exports/L10-P01-FIG-CORE-WINDOW.svg`

## P01-FIG-SRC-005 — Core denominator conservation
Claims: `P01-CLM-003/v1;P01-CLM-004/v1`  
Warning: NO_MODEL_EFFECT_INFERENCE; external access constraints apply  
Exports: `figures/exports/P01-FIG-SRC-005.png`, `figures/exports/P01-FIG-SRC-005.svg`

## P01-FIG-SRC-006 — Core vs A4 timing
Claims: `P01-CLM-007/v1;P01-CLM-011/v1`  
Warning: A4 readiness only; effectiveness not evaluated in P01  
Exports: `figures/exports/P01-FIG-SRC-006.png`, `figures/exports/P01-FIG-SRC-006.svg`

## P01-FIG-SRC-007 — A4 R1 failure → R2 design
Claims: `P01-CLM-007/v1;P01-CLM-011/v1`  
Warning: Retrospective feasibility origin; no effect claim  
Exports: `figures/exports/P01-FIG-SRC-007.png`, `figures/exports/P01-FIG-SRC-007.svg`

## P01-FIG-SRC-008 — Stage/repair chronology
Claims: `P01-CLM-008/v1`  
Warning: Execution history; historical failures are not current positive evidence  
Exports: `figures/exports/P01-FIG-SRC-008.png`, `figures/exports/P01-FIG-SRC-008.svg`

## P01-FIG-SRC-009 — Evidence ceiling
Claims: `P01-CLM-006/v1;P01-CLM-012/v1`  
Warning: PUBLIC_EEG_ONLY; NON_CLINICAL; NO_DEPLOYMENT_CLAIM; NO_ABLATION_EFFECTIVENESS_IN_P01  
Exports: `figures/exports/P01-FIG-SRC-009.png`, `figures/exports/P01-FIG-SRC-009.svg`

## P01-FIG-SRC-010 — P01→P02 handoff graph
Claims: `P01-CLM-010/v1`  
Warning: DOCUMENTARY_CLOSURE_SEQUENCE_REMAINS; no prediction of P02 success  
Exports: `figures/exports/P01-FIG-SRC-010.png`, `figures/exports/P01-FIG-SRC-010.svg`

# Part VII — Tables

Exact CSV exports are provided for the principal governed P01 data/presentation surfaces.

| table_id | title | rows | path |
| --- | --- | --- | --- |
| L10-P01-TBL-001 | Source dataset inventory | 3 | tables/exports/L10-P01-TBL-001.csv |
| L10-P01-TBL-002 | Event/window denominator | 4 | tables/exports/L10-P01-TBL-002.csv |
| L10-P01-TBL-003 | Subject split allocation | 3 | tables/exports/L10-P01-TBL-003.csv |
| L10-P01-TBL-004 | Preprocessing contract | 8 | tables/exports/L10-P01-TBL-004.csv |
| L10-P01-TBL-005 | Quality outcomes | 1 | tables/exports/L10-P01-TBL-005.csv |
| L10-P01-TBL-006 | A0–A13 readiness | 14 | tables/exports/L10-P01-TBL-006.csv |
| L10-P01-TBL-007 | A4 profile | 1 | tables/exports/L10-P01-TBL-007.csv |
| L10-P01-TBL-008 | External artifacts | 2 | tables/exports/L10-P01-TBL-008.csv |
| L10-P01-TBL-009 | Execution closure | 5 | tables/exports/L10-P01-TBL-009.csv |
| L10-P01-TBL-010 | Repair/rerun history | 8 | tables/exports/L10-P01-TBL-010.csv |
| L10-P01-TBL-011 | Reviewed claims | 12 | tables/exports/L10-P01-TBL-011.csv |
| L10-P01-TBL-012 | Limitation register | 20 | tables/exports/L10-P01-TBL-012.csv |
| L10-P01-TBL-013 | Negative/deferred/rejected claims | 2 | tables/exports/L10-P01-TBL-013.csv |
| L10-P01-TBL-014 | P02 handoff | 7 | tables/exports/L10-P01-TBL-014.csv |


# Part VIII — Reproducibility and External Retrieval

## 10. Core external artifact

- ID: `P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473`
- Kaggle provider version: `2`
- IHARQ logical immutable revision: `1`
- Manifest SHA-256: `dc21f418e9a1add62adb346f627d5d729735a5f1ecaa1d771f6fa5cfede627e1`
- Size: 1,166,652,764 bytes
- Access: PRIVATE Kaggle Dataset access + source-license compliance

## 11. A4 external artifact

- ID: `P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13`
- Kaggle provider version: `1`
- Logical revision: `2`
- Manifest SHA-256: `29124d59907610b1545e0a2b5d1811a4d4a2bf1df64cad49aa880f4721c47305`
- Size: 1,357,362,334 bytes
- Access: PRIVATE Kaggle Dataset access + source-license compliance

No credential values are stored in this package.

# Part IX — Negative / Limitation Surfaces

- A4 +4.0 s infeasibility remains visible as a negative feasibility/design-repair result.
- `P01-CLM-011/v1` remains deferred and appears only in future-work/negative/scope-boundary views.
- `P01-CLM-012/v1` remains rejected as supported clinical/deployment evidence.
- 20 soft/provider flags remain visible and are not equated with corruption.
- Historical Stage 07/18/26 failures remain provenance, not current positive evidence.
- External private-access and redistribution constraints remain attached to affected outputs.

# Part X — P01→P02 Read-Only Handoff

The Layer 10 handoff renders the already-governed technical input contract: core Dataset, A4 Dataset, labels, subject split, preprocessing, window profiles, config and limitations. **TECHNICAL INPUT READY ≠ P02 SCIENTIFIC RESULT.**

# Part X-A — Defense, Limitation, and Provenance Cards

## Thesis-defense view
`L10-P01-VIEW-021` provides a bounded answer to “What exactly had the project established by the end of P01?” using only approved/qualified claims and mandatory limitations.

## Dedicated limitation cards
Five major limitation cards preserve clinical/deployment, leakage, quality, A4-effectiveness, and external-access boundaries in compact formats.

## Representative provenance cards
Three provenance cards render claim→finding→Protocol→run/stage→record/artifact chains for the core denominator, A4, and execution closure. They create no new evidence.

# Part XI — Validation and Final Decision

| Validation | Result |
|---|---|
| P00 preservation | PASS |
| Evidence Map coverage | PASS |
| Layer 0 wording parity | PASS |
| Disposition parity | PASS |
| Source-value reproduction | PASS |
| Read-only behavior | PASS |
| P01 views | 20 |
| P01 cards | 12 |
| P01 figures | 11 |
| P01 tables | 14 |
| P00 preserved views/cards/exports | 14 / 14 / 14 |
| Limitation/warning parity | PASS |
| Negative visibility | PASS |
| A0–A13 | PASS |
| A14 | PASS — absent/prohibited |
| A4 readiness boundary | PASS |
| Clinical/deployment boundary | PASS |
| Leakage wording boundary | PASS |
| External artifact representation | PASS |
| Reproduction routes | PASS |
| Claim→Layer10 traceability | PASS |
| Artifact→source traceability | PASS |
| Human/machine no-drift | PASS |
| Foreign keys / paths / checksums | PASS |
| Secrets / placeholders | PASS |
| Freeze-critical blockers | 0 |

> **CUMULATIVE_LAYER10_THROUGH_P01: PASS — FINALIZED AND FROZEN**

**Next governed step:** final Phase-1 whole-stack synchronization, cumulative project-state update, handoff, and formal Phase-1 closure / Phase-2 authorization review.
