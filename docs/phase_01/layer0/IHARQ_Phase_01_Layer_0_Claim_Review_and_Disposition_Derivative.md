---
title: "IHARQ Phase 1 Layer 0 Claim Review and Disposition — Phase-Specific Derivative"
document_id: "IHARQ-P01-LAYER0-DERIVATIVE-R1"
phase: "P01"
status: "NON_AUTHORITATIVE_PHASE_SPECIFIC_DERIVATIVE_FINAL"
canonical_authority: "IHARQ-CUMULATIVE-PHASE-EVIDENCE-RESULTS-INTERPRETATION-THROUGH-P01-R2-LAYER0-INTEGRATED"
canonical_layer0_state: "EMBEDDED_IN_CUMULATIVE_REPORT"
---

# IHARQ BenchGuard Stretch C
# Phase 1 Layer 0 Claim Review and Disposition

> **NON-AUTHORITATIVE PHASE-SPECIFIC DERIVATIVE.** This document is provided separately at owner request for convenient P01-only review. It does **not** compete with the canonical cumulative Phase Analysis + embedded Layer 0 authority. If any drift is ever observed, the integrated cumulative Markdown controls.

> **Scope.** This derivative contains the complete P01 Layer 0 review state: 12/12 candidate claims, reviewed wording, dispositions, limitations, evidence ceilings, forbidden wording, Evidence Map eligibility, Layer 10 eligibility, and P02 claim-boundary inheritance. P00 appears only where unavoidable as inherited governance context.

## Document Control

| Field | Value |
|---|---|
| document ID | `IHARQ-P01-LAYER0-DERIVATIVE-R1` |
| phase | `P01` |
| authority status | `NON_AUTHORITATIVE_PHASE_SPECIFIC_DERIVATIVE` |
| canonical authority | `IHARQ-CUMULATIVE-PHASE-EVIDENCE-RESULTS-INTERPRETATION-THROUGH-P01-R2-LAYER0-INTEGRATED` |
| P01 candidates reviewed | `12/12` |
| dispositions | `2 APPROVED; 8 APPROVED_WITH_QUALIFICATIONS; 1 DEFERRED; 1 REJECTED; 0 BLOCKED` |
| next governed step | `UPDATE PAPER AND THESIS EVIDENCE MAP THROUGH P01` |

# PART I — P01 LAYER 0 AUTHORITY BOUNDARY

Layer 0 governs reviewed wording, disposition, mandatory qualifications/limitations, and downstream claim eligibility. It does not change measurements, counts, findings, Protocol, execution history, datasets, split, preprocessing, or window identities. The cumulative integrated Markdown remains the legal/current authority.

# PART II — P01 REVIEW INPUT

## 11. P01 Analytical State

P01 execution is `ACCEPTED`; the cumulative Protocol and Phase Analysis through P01 are frozen. P01 establishes a governed public-data, split, preprocessing, event/window, quality, leakage, persistence, and downstream-readiness foundation. It does **not** establish decoder superiority, clinical effectiveness, deployment safety, A4 performance benefit, calibration benefit, robustness benefit, or embodiment/control effectiveness.

Key fixed counts used for claim review:

| Surface | Verified value |
|---|---|
| Active datasets | 3 |
| Subject groups | 172 |
| Split roles | train 102; calibration 35; validation 17; test 18 |
| Accepted binary-MI events | 12,910 |
| Official core windows | 12,910 |
| Invalid official core windows | 0/12,910 |
| Quality summaries | 489 |
| Soft/provider flags | 20 |
| Hard-invalid summaries | 0/489 |
| Core HDF5 shards | 172 |
| A4 matched parents | 12,910/12,910 |
| Accepted stages | 27/27 |
| P01 gates | 16/16 PASS |
| Regression tests | 50/50 PASS |
| Unresolved blockers | 0 |

## 12. P01 Findings

| Finding | Evidence class | Denominator | Measured result | Evidence source(s) | Limitation |
|---|---|---|---|---|---|
| P01-FIND-001 | PROVENANCE_EVIDENCE | 3 active datasets, 172 subject groups, 453 source files; all three DatasetRecords VALIDATED with frozen aggregate SHA-256 identities. | P01 established exact source provenance and dataset identity for the selected public EEG portfolio. | records/datasets/*/*.json; reports/phase_01/sources/source_version_license_report.json | PUBLIC_EEG_ONLY; source-license/redistribution restrictions apply. |
| P01-FIND-002 | VALIDATION_EVIDENCE | 172 subject groups assigned train/calibration/validation/test = 102/35/17/18; disjointness PASS with no intersections. | The frozen subject-group split satisfies the implemented disjointness contract and preserves whole-subject role assignment. | records/splits/P01-L1-SPLIT-OFFICIAL-R2/IHARQ-SPLITRECORD-20260806-e4e371d332c61e36.json; reports/phase_01/splits/disjointness.json | This establishes contract disjointness, not universal absence of every conceivable leakage mechanism. |
| P01-FIND-003 | INTEGRITY_EVIDENCE | 12,910 accepted parent events map one-to-one to 12,910 validated core WindowRecords; 0 invalid core windows. | The official Layer-1 event/window pipeline preserved the accepted-event denominator under the frozen core window policy. | records/windows/; external_artifact_pointers/derived_windows_dataset.json | Does not imply decoder adequacy or statistical power. |
| P01-FIND-004 | INTEGRITY_EVIDENCE | 172 subject HDF5 shards, 12,910 windows, float32, 1,166,652,764 uploaded HDF5 bytes; remote manifest hash verified. | The official core derived Dataset is reproducibly identifiable and retrievable under its provider version/logical revision/hash contract. | reports/phase_01/storage/existing_core_dataset_adoption.json; external_artifact_pointers/derived_windows_dataset.json | Private Kaggle access is required; source licenses continue to govern redistribution. |
| P01-FIND-005 | VALIDATION_EVIDENCE | 489 quality summaries; 20 soft/provider flags; 0 hard-invalid summaries; 0/12,910 invalid official windows; policy ANNOTATE_NOT_REPAIR. | Quality issues were surfaced as governed annotations while hard validity criteria did not reject any official core window. | reports/phase_01/quality/quality_coverage.json; records/quality/ | A soft flag is not proof of physiological corruption, and zero hard-invalid cases is not a claim of artifact-free EEG. |
| P01-FIND-006 | VALIDATION_EVIDENCE | Split disjointness PASS and leakage_contamination status PASS with zero reported issues across group, duplicate, overlap, fit-scope and budget/test-contamination checks. | No contract leakage was detected under the implemented deterministic checks. | reports/phase_01/splits/disjointness.json; reports/phase_01/leakage/leakage_contamination.json | Bounded to implemented checks and frozen identities. |
| P01-FIND-007 | READINESS_EVIDENCE | 18 budget rows = 3 datasets × six per-class budgets {1,2,4,8,16,32}; all frozen under seed 20260804. | P01 prepared deterministic low-calibration population identities for later evaluation. | reports/phase_01/splits/low_calibration_budgets.csv | No calibration-performance experiment was executed in P01. |
| P01-FIND-008 | READINESS_EVIDENCE | Exactly 14 readiness rows A0…A13, each FOUNDATION_READY and executed_in_p01=false; A14 absence validator PASS. | Layer 1 produced the matching/readiness foundation required by the official A0–A13 ladder without introducing A14. | manifests/phase_01/layer1_ablation_readiness_l1_v1.json | Foundation readiness is not ablation effectiveness. |
| P01-FIND-009 | READINESS_EVIDENCE | 12,910/12,910 matched parents; 12,910 stored 3.5 s tensors; 38,730 registered virtual 2 s members; 0 invalid; 172 shards. | P01 established a fully matched A4 R2 Layer-1 substrate for future governed evaluation. | external_artifact_pointers/a4_window_family_dataset.json; reports/phase_01/storage/a4_derived_output_storage_actual_precommit.json | A4 effectiveness was not executed or measured in P01; R2 arose after feasibility evidence. |
| P01-FIND-010 | NEGATIVE_EVIDENCE | One valid released parent event (PhysioNetMI:104:0:8:event:24) had only 560 post-cue samples; the 640-sample +4.0 s proposal would require 80 nonexistent samples. | Padding, clipping, fabrication, or event dropping would have changed the comparison; the matched +3.5 s R2 design preserved the complete denominator. | Phase_01_Notebook.ipynb (R49 A4 boundary explanation); config_snapshot/p01_l1_a4_window_family_freeze_R2.json | This is a design-feasibility result, not evidence that R2 performs better than R1 or core. |
| P01-FIND-011 | EXECUTION_EVIDENCE | Accepted execution used Python 3.12.13 with exact package pins and adaptive disk policy; pin mismatches and import failures were zero. | Runtime compatibility/resource amendments changed execution conditions but did not alter datasets, labels, split, core preprocessing, core window, or core denominator. | environment_manifest.json; environment_amendment.json | Reproduction should use the recorded actual environment rather than the original Python 3.11 intent. |
| P01-FIND-012 | EXECUTION_EVIDENCE | 27/27 accepted stages PASS; 16/16 P01 gates PASS; regression suite 50/50 PASS; 0 unresolved blockers; 13,164/13,164 execution-bundle checksum targets valid. | The accepted P01 execution lineage satisfies its deterministic execution, validation, and package-closure contract. | reports/phase_01/tests/stage_results.json; gate_decision.json; reports/phase_01/tests/phase0_and_runtime_regression.json; checksums.sha256 | Execution closure does not imply model or clinical effectiveness. |
| P01-FIND-013 | HISTORICAL_FAILED_EVIDENCE | Stage 07, 18 and 26 failures blocked continuation/release until targeted repairs passed; earlier successful scope was reused where lawful. | The execution history demonstrates fail-closed repair/reentry rather than silent acceptance of known defects. | reports/phase_01/worker_logs/; reports/phase_01/repair_reentry.json; reports/phase_01/runtime/r54_final_export_secret_redaction.json | The repair history must remain visible; it is not evidence of scientific superiority. |
| P01-FIND-014 | READINESS_EVIDENCE | P02 handoff references the exact core/A4 pointers, split, label maps, preprocessing and profile identities with mutation/leakage prohibitions. | P02 can consume the frozen Layer-1 data substrate without reinterpreting Layer-1 identities. | phase2_handoff/phase_01_to_phase_02.yaml; handoffs/phase_01_to_phase_02.yaml | Formal phase transition still follows the documentary closure sequence. |

## 13. P01 Candidate Claims

| Candidate | Original wording | Finding(s) | Evidence class | Source support | Source limitation tags | Source ceiling |
|---|---|---|---|---|---|---|
| P01-CLAIM-CAND-001 | Phase 1 established a checksum-bound, provenance-traceable three-dataset public EEG foundation for the IHARQ binary motor-imagery branch. | P01-FIND-001 | PROVENANCE_EVIDENCE | DIRECT | PUBLIC_EEG_ONLY; NON_CLINICAL | Data provenance and reproducibility only |
| P01-CLAIM-CAND-002 | The frozen P01 split is subject-grouped and passed the implemented disjointness and leakage checks. | P01-FIND-002; P01-FIND-006 | VALIDATION_EVIDENCE | DIRECT_BOUNDED | IMPLEMENTED_CHECKS_ONLY | Contract leakage/disjointness correctness |
| P01-CLAIM-CAND-003 | The official Layer-1 pipeline conserved the complete accepted-event denominator: 12,910 accepted events produced 12,910 valid core windows. | P01-FIND-003 | INTEGRITY_EVIDENCE | DIRECT | NO_MODEL_EFFECT_INFERENCE | Data materialization closure |
| P01-CLAIM-CAND-004 | The official core numerical Dataset was persisted as 172 lossless HDF5 subject shards and verified by immutable provider/version/manifest identities. | P01-FIND-004 | INTEGRITY_EVIDENCE | DIRECT | PRIVATE_KAGGLE_EXTERNAL_ARTIFACT_ACCESS; SOURCE_LICENSE_REDISTRIBUTION_CONSTRAINTS | Retrieval/storage reproducibility |
| P01-CLAIM-CAND-005 | P01 quality processing followed an annotate-not-repair policy; 20 soft/provider flags were preserved while no hard-invalid summary or official core window was observed. | P01-FIND-005 | VALIDATION_EVIDENCE | DIRECT_BOUNDED | SOFT_FLAG_NOT_EQUIVALENT_TO_CORRUPTION | Quality annotation and hard-validity closure |
| P01-CLAIM-CAND-006 | P01 established the Layer-1 readiness foundation for all official A0–A13 identities while preserving A14 as absent/prohibited. | P01-FIND-008 | READINESS_EVIDENCE | DIRECT | NO_ABLATION_EFFECTIVENESS_IN_P01 | Foundation readiness only |
| P01-CLAIM-CAND-007 | P01 established a 12,910-event fully matched A4 R2 data substrate for future governed evaluation, without padding, clipping, fabrication, or parent-event loss. | P01-FIND-009; P01-FIND-010 | READINESS_EVIDENCE | DIRECT_BOUNDED | A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01 | Future A4 substrate readiness; not A4 effectiveness |
| P01-CLAIM-CAND-008 | The accepted P01 execution closed all 27 stages, 16 deterministic gates, and 50 regression tests with zero unresolved blockers. | P01-FIND-012 | EXECUTION_EVIDENCE | DIRECT | NO_EFFECTIVENESS_INFERENCE | Execution/reproducibility closure |
| P01-CLAIM-CAND-009 | P01 runtime compatibility and resource amendments preserved the frozen scientific core data contract while recording the actual Python 3.12.13 environment. | P01-FIND-011 | EXECUTION_EVIDENCE | DIRECT_BOUNDED | ACTUAL_RUNTIME_PYTHON_3_12_13_WITH_COMPATIBILITY_AMENDMENT; ADAPTIVE_DISK_RESOURCE_AMENDMENT | Execution reproducibility |
| P01-CLAIM-CAND-010 | P01 provides a frozen technical data contract that P02 can consume without silent relabeling, rewindowing, split mutation, denominator substitution, or test leakage. | P01-FIND-014 | READINESS_EVIDENCE | DIRECT | DOCUMENTARY_CLOSURE_SEQUENCE_REMAINS | Downstream technical readiness |
| P01-CLAIM-CAND-011 | A4 R2 improves decoder performance relative to the core window. | P01-FIND-009 | READINESS_EVIDENCE | NONE_FROM_P01 | A4_EFFECTIVENESS_NOT_EXECUTED | Not claimable from P01 |
| P01-CLAIM-CAND-012 | The P01 data foundation demonstrates clinical effectiveness or deployment safety. | P01-FIND-001; P01-FIND-012 | EXECUTION_EVIDENCE | NONE_FROM_P01 | NON_CLINICAL; NO_DEPLOYMENT_CLAIM | Not claimable from P01 |

## 14. P01 Limitations

The cumulative canonical P01 limitation register includes:

- **`PUBLIC_EEG_ONLY`** — The empirical substrate is public benchmark/research EEG, not a clinical or deployment population. Consequence: No clinical generalization or deployment claims.
- **`NON_CLINICAL`** — No clinical cohort, clinical endpoint, or treatment outcome is present. Consequence: Clinical benefit/effectiveness claims prohibited.
- **`NO_DEPLOYMENT_CLAIM`** — P01 does not evaluate deployed real-world control, operational safety, or medical-device behavior. Consequence: Deployment/safety claims prohibited.
- **`PRIVATE_KAGGLE_EXTERNAL_ARTIFACT_ACCESS`** — Core and A4 numerical HDF5 artifacts are private Kaggle Datasets. Consequence: No effect on scientific content, but constrains independent retrieval.
- **`A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01`** — A4 R2 was introduced after a real +4.0 s boundary infeasibility was observed. Consequence: No A4 effectiveness claim from P01.
- **`ACTUAL_RUNTIME_PYTHON_3_12_13_WITH_COMPATIBILITY_AMENDMENT`** — Build Book intended Python 3.11, while accepted Kaggle execution used Python 3.12.13 under a documented compatibility amendment. Consequence: No scientific claim consequence when science/config remains unchanged.
- **`ADAPTIVE_DISK_RESOURCE_AMENDMENT`** — Governed amendment P01-L1-KAGGLE-ADAPTIVE-DISK-R1 replaced the legacy 60 GiB preflight with an adaptive measured requirement with 6.0 GiB effective minimum; observed free disk was 18.94 GiB. Consequence: No scientific claim consequence.
- **`SOURCE_LICENSE_REDISTRIBUTION_CONSTRAINTS`** — Source-specific licenses, especially BNCI CC BY-ND, constrain redistribution of raw/derived signal bytes. Consequence: No performance consequence; affects artifact distribution.
- **`BINARY_MI_BRANCH_SCOPE`** — P01 official supervised denominator is left-hand versus right-hand imagery only; rest, feet, tongue, execution, technical and unlabeled online/test events are excluded as defined per source. Consequence: No claims about excluded tasks/classes.

Additional claim-boundary tags already present in the frozen candidate register are governed here as wording constraints: `IMPLEMENTED_CHECKS_ONLY`, `NO_MODEL_EFFECT_INFERENCE`, `SOFT_FLAG_NOT_EQUIVALENT_TO_CORRUPTION`, `NO_ABLATION_EFFECTIVENESS_IN_P01`, `A4_EFFECTIVENESS_NOT_EXECUTED`, `NO_EFFECTIVENESS_INFERENCE`, and `DOCUMENTARY_CLOSURE_SEQUENCE_REMAINS`.

## 15. P01 Negative Evidence

- The original +0.0→+4.0 s A4 proposal is a **negative feasibility result** for one real boundary event; it is not hidden.
- The historical Stage 07, Stage 18, and Stage 26 defects were fail-closed, repaired, and closed in the affected scope; they are not current blockers.
- `P01-CLAIM-CAND-011` has no P01 effectiveness evidence.
- `P01-CLAIM-CAND-012` exceeds P01’s public/non-clinical/deployment evidence ceiling.

## 16. P01 Evidence Ceilings

P01 may support provenance, data integrity, split integrity, preprocessing execution, denominator closure, registered quality validity, leakage checks under implemented rules, artifact integrity, A0–A13 foundation readiness, A4 substrate readiness, execution reproducibility, and technical downstream readiness. P01 alone may not support decoder superiority, clinical effectiveness, deployment safety, A4 performance benefit, low-calibration benefit, later robustness effects, or embodiment/control effects.


# PART III — P01 CLAIM-BY-CLAIM REVIEW

## 17. P01-CLAIM-CAND-001 → P01-CLM-001/v1

| Field | Layer 0 result |
|---|---|
| Source candidate | P01-CLAIM-CAND-001 |
| Layer 0 disposition ID | P01-L0-DISP-001 |
| Original wording | Phase 1 established a checksum-bound, provenance-traceable three-dataset public EEG foundation for the IHARQ binary motor-imagery branch. |
| Disposition | APPROVED_WITH_QUALIFICATIONS |
| Support class | SUPPORTED_WITH_QUALIFICATION |
| Evidence class | PROVENANCE_EVIDENCE |
| Finding IDs | P01-FIND-001 |
| Protocol analysis IDs | P01-AC-001-SOURCE-INVENTORY |
| Run/stage IDs | P01-STAGE-05; P01-STAGE-06; P01-STAGE-07 |
| Record/artifact IDs | IHARQ-DATASETRECORD-20260806-66309cda68771bef; IHARQ-DATASETRECORD-20260806-42c424800627b6ee; IHARQ-DATASETRECORD-20260806-adb91f25a65e588e |
| Evidence paths | records/datasets/BNCI2014_001/IHARQ-DATASETRECORD-20260806-42c424800627b6ee.json; records/datasets/Lee2019_MI/IHARQ-DATASETRECORD-20260806-adb91f25a65e588e.json; records/datasets/PhysioNetMI/IHARQ-DATASETRECORD-20260806-66309cda68771bef.json; reports/phase_01/sources/source_version_license_report.json |
| Claim ceiling | DATA_PROVENANCE_REPRODUCIBILITY |
| Mandatory limitations / claim-boundary controls | PUBLIC_EEG_ONLY; NON_CLINICAL; BINARY_MI_BRANCH_SCOPE |
| Evidence Map eligibility | ELIGIBLE_WITH_QUALIFICATION |
| Layer 10 eligibility | ELIGIBLE_WITH_QUALIFICATION |
| Future reconsideration | Re-review only if source identities or task scope change. |

**Canonical reviewed wording**

> Within the frozen P01 binary motor-imagery branch, Phase 1 established a checksum-bound, provenance-traceable foundation over the three activated public EEG datasets.

**Safe short form**

> P01 established a checksum-bound three-dataset public EEG foundation.

**Prohibited stronger wording**

> P01 established a clinically representative or deployment-ready EEG foundation.

**Layer 0 reasoning**

The exact source inventory and checksum/provenance records support the foundation claim, but the public benchmark population and binary-MI task scope must remain visible. The claim is therefore qualified rather than broadened toward representativeness or deployment.

## 18. P01-CLAIM-CAND-002 → P01-CLM-002/v1

| Field | Layer 0 result |
|---|---|
| Source candidate | P01-CLAIM-CAND-002 |
| Layer 0 disposition ID | P01-L0-DISP-002 |
| Original wording | The frozen P01 split is subject-grouped and passed the implemented disjointness and leakage checks. |
| Disposition | APPROVED_WITH_QUALIFICATIONS |
| Support class | SUPPORTED_WITH_QUALIFICATION |
| Evidence class | VALIDATION_EVIDENCE |
| Finding IDs | P01-FIND-002; P01-FIND-006 |
| Protocol analysis IDs | P01-AC-002-SPLIT; P01-AC-005-LEAKAGE |
| Run/stage IDs | P01-STAGE-11; P01-STAGE-17 |
| Record/artifact IDs | IHARQ-SPLITRECORD-20260806-e4e371d332c61e36 |
| Evidence paths | records/splits/P01-L1-SPLIT-OFFICIAL-R2/IHARQ-SPLITRECORD-20260806-e4e371d332c61e36.json; reports/phase_01/splits/disjointness.json; reports/phase_01/leakage/leakage_contamination.json |
| Claim ceiling | IMPLEMENTED_SPLIT_AND_LEAKAGE_CHECKS |
| Mandatory limitations / claim-boundary controls | IMPLEMENTED_CHECKS_ONLY |
| Evidence Map eligibility | ELIGIBLE_WITH_QUALIFICATION |
| Layer 10 eligibility | ELIGIBLE_WITH_QUALIFICATION |
| Future reconsideration | Refresh if split identity, visibility rules, or leakage checks change. |

**Canonical reviewed wording**

> The frozen P01 split assigned 172 subject groups wholly and disjointly across train, calibration, validation, and test roles and passed the implemented registered leakage/disjointness checks; this does not prove that every conceivable leakage mechanism is impossible.

**Safe short form**

> P01 subject split passed the registered disjointness/leakage checks.

**Prohibited stronger wording**

> P01 proves that leakage is impossible.

**Layer 0 reasoning**

The subject-group split and registered leakage checks pass exactly, but no finite implemented test suite can prove that every conceivable leakage mechanism is impossible. The qualification is therefore part of the reviewed wording itself.

## 19. P01-CLAIM-CAND-003 → P01-CLM-003/v1

| Field | Layer 0 result |
|---|---|
| Source candidate | P01-CLAIM-CAND-003 |
| Layer 0 disposition ID | P01-L0-DISP-003 |
| Original wording | The official Layer-1 pipeline conserved the complete accepted-event denominator: 12,910 accepted events produced 12,910 valid core windows. |
| Disposition | APPROVED |
| Support class | DIRECT |
| Evidence class | INTEGRITY_EVIDENCE |
| Finding IDs | P01-FIND-003 |
| Protocol analysis IDs | P01-AC-003-DENOMINATOR |
| Run/stage IDs | P01-STAGE-13; P01-STAGE-14; P01-STAGE-16 |
| Record/artifact IDs | IHARQ-SPLITRECORD-20260806-e4e371d332c61e36; IHARQ-PREPROCESSINGRECORD-20260806-a11b59eeb3861a08 |
| Evidence paths | records/windows/; external_artifact_pointers/derived_windows_dataset.json |
| Claim ceiling | DATA_MATERIALIZATION_CLOSURE |
| Mandatory limitations / claim-boundary controls | NO_MODEL_EFFECT_INFERENCE |
| Evidence Map eligibility | ELIGIBLE_FOR_EVIDENCE_MAP |
| Layer 10 eligibility | ELIGIBLE |
| Future reconsideration | Refresh only if accepted-event or core-window identity changes. |

**Canonical reviewed wording**

> Under the frozen official core-window policy, all 12,910 accepted events yielded 12,910 valid core windows, with 0/12,910 invalid official core windows.

**Safe short form**

> 12,910/12,910 accepted events yielded valid official core windows.

**Prohibited stronger wording**

> Denominator closure proves the dataset will yield strong decoder performance.

**Layer 0 reasoning**

This is a finite denominator claim directly established by the canonical evidence. The exact 12,910/12,910 statement is preserved. A model-effect boundary remains contextually mandatory but does not require weakening the factual count.

## 20. P01-CLAIM-CAND-004 → P01-CLM-004/v1

| Field | Layer 0 result |
|---|---|
| Source candidate | P01-CLAIM-CAND-004 |
| Layer 0 disposition ID | P01-L0-DISP-004 |
| Original wording | The official core numerical Dataset was persisted as 172 lossless HDF5 subject shards and verified by immutable provider/version/manifest identities. |
| Disposition | APPROVED_WITH_QUALIFICATIONS |
| Support class | SUPPORTED_WITH_QUALIFICATION |
| Evidence class | INTEGRITY_EVIDENCE |
| Finding IDs | P01-FIND-004 |
| Protocol analysis IDs | P01-AC-006-EXTERNAL |
| Run/stage IDs | P01-STAGE-14; P01-STAGE-15; P01-STAGE-20 |
| Record/artifact IDs | P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473; IHARQ-SPLITRECORD-20260806-e4e371d332c61e36; IHARQ-PREPROCESSINGRECORD-20260806-a11b59eeb3861a08 |
| Evidence paths | reports/phase_01/storage/existing_core_dataset_adoption.json; external_artifact_pointers/derived_windows_dataset.json |
| Claim ceiling | RETRIEVAL_STORAGE_INTEGRITY_REPRODUCIBILITY |
| Mandatory limitations / claim-boundary controls | PRIVATE_KAGGLE_EXTERNAL_ARTIFACT_ACCESS; SOURCE_LICENSE_REDISTRIBUTION_CONSTRAINTS |
| Evidence Map eligibility | ELIGIBLE_WITH_QUALIFICATION |
| Layer 10 eligibility | ELIGIBLE_WITH_QUALIFICATION |
| Future reconsideration | Refresh if provider version, logical revision, manifest hash, or access policy changes. |

**Canonical reviewed wording**

> The official P01 core numerical artifact was persisted as 172 lossless HDF5 subject shards covering 12,910 windows and was verified under its Kaggle provider-version/logical-revision/manifest-hash identity contract.

**Safe short form**

> P01 core data: 172 verified lossless HDF5 subject shards.

**Prohibited stronger wording**

> The core Dataset is universally public and independently downloadable without access or license constraints.

**Layer 0 reasoning**

The artifact identity, shard count, HDF5 lossless storage and manifest/provider identity are directly supported. Private Kaggle access and source-license redistribution constraints prevent a stronger universal-access/reproducibility claim.

## 21. P01-CLAIM-CAND-005 → P01-CLM-005/v1

| Field | Layer 0 result |
|---|---|
| Source candidate | P01-CLAIM-CAND-005 |
| Layer 0 disposition ID | P01-L0-DISP-005 |
| Original wording | P01 quality processing followed an annotate-not-repair policy; 20 soft/provider flags were preserved while no hard-invalid summary or official core window was observed. |
| Disposition | APPROVED_WITH_QUALIFICATIONS |
| Support class | SUPPORTED_WITH_QUALIFICATION |
| Evidence class | VALIDATION_EVIDENCE |
| Finding IDs | P01-FIND-005 |
| Protocol analysis IDs | P01-AC-004-QUALITY |
| Run/stage IDs | P01-STAGE-13; P01-STAGE-16 |
| Record/artifact IDs | records/quality/ (489 governed quality summaries) |
| Evidence paths | reports/phase_01/quality/quality_coverage.json; records/quality/ |
| Claim ceiling | QUALITY_ANNOTATION_AND_HARD_VALIDITY_CLOSURE |
| Mandatory limitations / claim-boundary controls | SOFT_FLAG_NOT_EQUIVALENT_TO_CORRUPTION |
| Evidence Map eligibility | ELIGIBLE_WITH_QUALIFICATION |
| Layer 10 eligibility | ELIGIBLE_WITH_QUALIFICATION |
| Future reconsideration | Refresh if quality rules, summaries, or invalidity criteria change. |

**Canonical reviewed wording**

> P01 applied the ANNOTATE_NOT_REPAIR quality policy across 489 quality summaries: 20 soft/provider flags were retained, 0/489 summaries were hard-invalid, and 0/12,910 official core windows were invalid under the registered criteria.

**Safe short form**

> P01 retained 20 soft flags; hard-invalid summaries and invalid core windows were zero under registered criteria.

**Prohibited stronger wording**

> All P01 EEG was flawless or artifact-free.

**Layer 0 reasoning**

The quality counts and ANNOTATE_NOT_REPAIR policy are directly supported. The wording is qualified to prevent soft/provider flags from being misread as corruption and zero hard-invalid cases from being misread as artifact-free EEG.

## 22. P01-CLAIM-CAND-006 → P01-CLM-006/v1

| Field | Layer 0 result |
|---|---|
| Source candidate | P01-CLAIM-CAND-006 |
| Layer 0 disposition ID | P01-L0-DISP-006 |
| Original wording | P01 established the Layer-1 readiness foundation for all official A0–A13 identities while preserving A14 as absent/prohibited. |
| Disposition | APPROVED_WITH_QUALIFICATIONS |
| Support class | READINESS_ONLY |
| Evidence class | READINESS_EVIDENCE |
| Finding IDs | P01-FIND-008 |
| Protocol analysis IDs | P01-AC-007-ABLATION-READINESS |
| Run/stage IDs | P01-STAGE-18 |
| Record/artifact IDs | A0-A13 readiness manifest |
| Evidence paths | manifests/phase_01/layer1_ablation_readiness_l1_v1.json |
| Claim ceiling | FOUNDATION_READINESS_ONLY |
| Mandatory limitations / claim-boundary controls | NO_ABLATION_EFFECTIVENESS_IN_P01 |
| Evidence Map eligibility | ELIGIBLE_WITH_QUALIFICATION |
| Layer 10 eligibility | ELIGIBLE_WITH_QUALIFICATION |
| Future reconsideration | Effectiveness claims require the relevant downstream governed experiments. |

**Canonical reviewed wording**

> P01 established Layer-1 foundation readiness for each official A0-A13 identity; none of these ablation-effectiveness experiments was executed in P01, and A14 remained absent/prohibited.

**Safe short form**

> A0-A13 Layer-1 foundations are ready; A14 is absent/prohibited.

**Prohibited stronger wording**

> P01 demonstrated that A0-A13 ablations are effective.

**Layer 0 reasoning**

The readiness manifest covers exactly A0-A13 and records executed_in_p01=false. The claim is permitted only as foundation readiness; no ablation-effectiveness inference is allowed. A14 remains absent/prohibited.

## 23. P01-CLAIM-CAND-007 → P01-CLM-007/v1

| Field | Layer 0 result |
|---|---|
| Source candidate | P01-CLAIM-CAND-007 |
| Layer 0 disposition ID | P01-L0-DISP-007 |
| Original wording | P01 established a 12,910-event fully matched A4 R2 data substrate for future governed evaluation, without padding, clipping, fabrication, or parent-event loss. |
| Disposition | APPROVED_WITH_QUALIFICATIONS |
| Support class | READINESS_ONLY |
| Evidence class | READINESS_EVIDENCE |
| Finding IDs | P01-FIND-009; P01-FIND-010 |
| Protocol analysis IDs | P01-AC-008-A4 |
| Run/stage IDs | P01-STAGE-14; P01-STAGE-15; P01-STAGE-18 |
| Record/artifact IDs | P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13; P01-L1-A4-WINDOW-FAMILY-FREEZE-R2 |
| Evidence paths | external_artifact_pointers/a4_window_family_dataset.json; reports/phase_01/storage/a4_derived_output_storage_actual_precommit.json; config_snapshot/p01_l1_a4_window_family_freeze_R2.json; Phase_01_Notebook.ipynb (R49 A4 boundary explanation) |
| Claim ceiling | FUTURE_A4_SUBSTRATE_READINESS |
| Mandatory limitations / claim-boundary controls | A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01; A4_EFFECTIVENESS_NOT_EXECUTED |
| Evidence Map eligibility | ELIGIBLE_WITH_QUALIFICATION |
| Layer 10 eligibility | ELIGIBLE_WITH_QUALIFICATION |
| Future reconsideration | A matched downstream decoder experiment under the frozen A4 R2 contract is required for performance/effect claims. |

**Canonical reviewed wording**

> P01 established a fully matched A4 R2 Layer-1 data substrate for future governed evaluation: 12,910/12,910 parent events are represented without padding, clipping, fabricated samples, or parent-event loss. A4 R2 arose after the +4.0 s feasibility failure and was not evaluated for decoder effectiveness in P01.

**Safe short form**

> A4 R2 substrate: 12,910/12,910 matched parents; effectiveness not evaluated in P01.

**Prohibited stronger wording**

> A4 R2 improves accuracy, AUROC, robustness, or decoder performance.

**Layer 0 reasoning**

The matched A4 R2 substrate is directly established, including 12,910/12,910 coverage and no padding/clipping/fabrication/loss. Because R2 arose after the +4.0 s feasibility failure and no downstream decoder experiment ran in P01, the claim is qualified to readiness only.

## 24. P01-CLAIM-CAND-008 → P01-CLM-008/v1

| Field | Layer 0 result |
|---|---|
| Source candidate | P01-CLAIM-CAND-008 |
| Layer 0 disposition ID | P01-L0-DISP-008 |
| Original wording | The accepted P01 execution closed all 27 stages, 16 deterministic gates, and 50 regression tests with zero unresolved blockers. |
| Disposition | APPROVED |
| Support class | DIRECT |
| Evidence class | EXECUTION_EVIDENCE |
| Finding IDs | P01-FIND-012 |
| Protocol analysis IDs | P01-AC-010-GATES-REPAIRS |
| Run/stage IDs | P01-STAGE-04; P01-STAGE-23; P01-STAGE-24; P01-STAGE-26 |
| Record/artifact IDs | P01-G01...P01-G16; stage_results 00...26 |
| Evidence paths | reports/phase_01/tests/stage_results.json; gate_decision.json; reports/phase_01/tests/phase0_and_runtime_regression.json; reports/phase_01/repair_reentry.json; checksums.sha256 |
| Claim ceiling | EXECUTION_REPRODUCIBILITY_CLOSURE |
| Mandatory limitations / claim-boundary controls | NO_EFFECTIVENESS_INFERENCE |
| Evidence Map eligibility | ELIGIBLE_FOR_EVIDENCE_MAP |
| Layer 10 eligibility | ELIGIBLE |
| Future reconsideration | Refresh if accepted execution lineage or package integrity identity changes. |

**Canonical reviewed wording**

> The accepted P01 execution completed 27/27 registered stages, 16/16 deterministic P01 gates, and 50/50 regression tests with 0 unresolved blockers; final execution-bundle integrity checks also closed.

**Safe short form**

> P01 execution closed 27/27 stages, 16/16 gates, 50/50 tests, with 0 blockers.

**Prohibited stronger wording**

> Because all gates passed, P01 proved scientific or clinical effectiveness.

**Layer 0 reasoning**

The final accepted lineage directly establishes 27/27 stages, 16/16 gates, 50/50 tests and zero blockers. These exact finite closure facts can be approved as stated; they remain execution/reproducibility claims, not effectiveness claims.

## 25. P01-CLAIM-CAND-009 → P01-CLM-009/v1

| Field | Layer 0 result |
|---|---|
| Source candidate | P01-CLAIM-CAND-009 |
| Layer 0 disposition ID | P01-L0-DISP-009 |
| Original wording | P01 runtime compatibility and resource amendments preserved the frozen scientific core data contract while recording the actual Python 3.12.13 environment. |
| Disposition | APPROVED_WITH_QUALIFICATIONS |
| Support class | SUPPORTED_WITH_QUALIFICATION |
| Evidence class | EXECUTION_EVIDENCE |
| Finding IDs | P01-FIND-011 |
| Protocol analysis IDs | P01-AC-009-ENVIRONMENT |
| Run/stage IDs | P01-STAGE-01; P01-STAGE-03 |
| Record/artifact IDs | P01-L1-KAGGLE-ENV-FREEZE-R5; P01-L1-KAGGLE-ADAPTIVE-DISK-R1 |
| Evidence paths | environment_manifest.json; environment_amendment.json |
| Claim ceiling | EXECUTION_REPRODUCIBILITY |
| Mandatory limitations / claim-boundary controls | ACTUAL_RUNTIME_PYTHON_3_12_13_WITH_COMPATIBILITY_AMENDMENT; ADAPTIVE_DISK_RESOURCE_AMENDMENT |
| Evidence Map eligibility | ELIGIBLE_WITH_QUALIFICATION |
| Layer 10 eligibility | ELIGIBLE_WITH_QUALIFICATION |
| Future reconsideration | Refresh if runtime equivalence, package pins, or resource policy changes. |

**Canonical reviewed wording**

> The accepted P01 run used Python 3.12.13 under a documented compatibility amendment and the governed adaptive-disk policy P01-L1-KAGGLE-ADAPTIVE-DISK-R1; the accepted records show no change to the frozen datasets, labels, subject split, core preprocessing, core window policy, or 12,910-event denominator attributable to these runtime/resource amendments.

**Safe short form**

> P01 ran on Python 3.12.13 with governed compatibility/resource amendments and no recorded core-contract change.

**Prohibited stronger wording**

> Environment differences could have no effect whatsoever or are universally irrelevant.

**Layer 0 reasoning**

The accepted environment records establish Python 3.12.13 and the adaptive-disk amendment, while the frozen scientific core identities are recorded unchanged. The reviewed wording uses “no change was recorded” rather than an impossible universal claim that environment differences can never matter.

## 26. P01-CLAIM-CAND-010 → P01-CLM-010/v1

| Field | Layer 0 result |
|---|---|
| Source candidate | P01-CLAIM-CAND-010 |
| Layer 0 disposition ID | P01-L0-DISP-010 |
| Original wording | P01 provides a frozen technical data contract that P02 can consume without silent relabeling, rewindowing, split mutation, denominator substitution, or test leakage. |
| Disposition | APPROVED_WITH_QUALIFICATIONS |
| Support class | READINESS_ONLY |
| Evidence class | READINESS_EVIDENCE |
| Finding IDs | P01-FIND-014 |
| Protocol analysis IDs | P01-AC-003-DENOMINATOR; P01-AC-005-LEAKAGE; P01-AC-006-EXTERNAL; P01-AC-007-ABLATION-READINESS; P01-AC-010-GATES-REPAIRS |
| Run/stage IDs | P01-STAGE-22; P01-STAGE-23; P01-STAGE-26 |
| Record/artifact IDs | IHARQ-DATASETRECORD-20260806-66309cda68771bef; IHARQ-DATASETRECORD-20260806-42c424800627b6ee; IHARQ-DATASETRECORD-20260806-adb91f25a65e588e; IHARQ-LABELMAPRECORD-20260806-4379781a3b5f5ea9; IHARQ-LABELMAPRECORD-20260806-587dcfff81307768; IHARQ-LABELMAPRECORD-20260806-b551cfd20335896c; IHARQ-SPLITRECORD-20260806-e4e371d332c61e36; IHARQ-PREPROCESSINGRECORD-20260806-a11b59eeb3861a08; P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473; P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13 |
| Evidence paths | handoffs/phase_01_to_phase_02.yaml; phase2_handoff/phase_01_to_phase_02.yaml |
| Claim ceiling | DOWNSTREAM_TECHNICAL_DATA_CONTRACT_READINESS |
| Mandatory limitations / claim-boundary controls | DOCUMENTARY_CLOSURE_SEQUENCE_REMAINS |
| Evidence Map eligibility | ELIGIBLE_WITH_QUALIFICATION |
| Layer 10 eligibility | ELIGIBLE_WITH_QUALIFICATION |
| Future reconsideration | Refresh if any upstream frozen identity or handoff contract changes. |

**Canonical reviewed wording**

> P01 freezes a technical Layer-1 data contract that P02 may consume using the recorded dataset, label-map, split, preprocessing, core-window, and external-artifact identities; silent relabeling, rewindowing, split mutation, denominator substitution, or test-visibility leakage is prohibited. This is technical readiness, not evidence of P02 scientific success.

**Safe short form**

> P02 may consume the frozen P01 Layer-1 data contract without silent identity mutation.

**Prohibited stronger wording**

> P01 proves that P02 will succeed scientifically or that downstream models will perform well.

**Layer 0 reasoning**

The P02 handoff and frozen identities support technical data-contract readiness, but not downstream model success. The claim is approved only with explicit technical-readiness and documentary-sequence boundaries.

## 27. P01-CLAIM-CAND-011 → P01-CLM-011/v1

| Field | Layer 0 result |
|---|---|
| Source candidate | P01-CLAIM-CAND-011 |
| Layer 0 disposition ID | P01-L0-DISP-011 |
| Original wording | A4 R2 improves decoder performance relative to the core window. |
| Disposition | DEFERRED |
| Support class | UNSUPPORTED_CURRENTLY |
| Evidence class | READINESS_EVIDENCE |
| Finding IDs | P01-FIND-009 |
| Protocol analysis IDs | P01-AC-008-A4 |
| Run/stage IDs | P01-STAGE-14; P01-STAGE-15 |
| Record/artifact IDs | P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13; P01-L1-A4-WINDOW-FAMILY-FREEZE-R2 |
| Evidence paths | external_artifact_pointers/a4_window_family_dataset.json; config_snapshot/p01_l1_a4_window_family_freeze_R2.json |
| Claim ceiling | NOT_CLAIMABLE_FROM_P01 |
| Mandatory limitations / claim-boundary controls | A4_EFFECTIVENESS_NOT_EXECUTED; A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01 |
| Evidence Map eligibility | DEFERRED_NOT_CURRENTLY_MAPPABLE_AS_SUPPORTED |
| Layer 10 eligibility | NEGATIVE_OR_DEFERRED_REGISTER_ONLY |
| Future reconsideration | Reconsider only after a Protocol-authorized matched A4 effectiveness experiment with downstream model evidence. |

**Canonical reviewed wording**

> P01 did not evaluate whether A4 R2 improves decoder performance relative to the core window; that effectiveness question remains deferred to a future governed matched downstream experiment.

**Safe short form**

> A4 performance benefit was not evaluated in P01.

**Prohibited stronger wording**

> A4 R2 improves decoder performance relative to the core window.

**Layer 0 reasoning**

P01 contains A4 feasibility/readiness evidence but no model-effect experiment. The performance-benefit concept is retained as a future testable question and therefore deferred rather than converted into a readiness claim or deleted.

## 28. P01-CLAIM-CAND-012 → P01-CLM-012/v1

| Field | Layer 0 result |
|---|---|
| Source candidate | P01-CLAIM-CAND-012 |
| Layer 0 disposition ID | P01-L0-DISP-012 |
| Original wording | The P01 data foundation demonstrates clinical effectiveness or deployment safety. |
| Disposition | REJECTED |
| Support class | PROHIBITED_BY_EVIDENCE_SCOPE |
| Evidence class | EXECUTION_EVIDENCE |
| Finding IDs | P01-FIND-001; P01-FIND-012 |
| Protocol analysis IDs | P01-AC-001-SOURCE-INVENTORY; P01-AC-010-GATES-REPAIRS |
| Run/stage IDs | P01-STAGE-06; P01-STAGE-26 |
| Record/artifact IDs | IHARQ-DATASETRECORD-20260806-66309cda68771bef; IHARQ-DATASETRECORD-20260806-42c424800627b6ee; IHARQ-DATASETRECORD-20260806-adb91f25a65e588e |
| Evidence paths | reports/phase_01/sources/source_version_license_report.json; gate_decision.json |
| Claim ceiling | NOT_CLAIMABLE_FROM_P01 |
| Mandatory limitations / claim-boundary controls | PUBLIC_EEG_ONLY; NON_CLINICAL; NO_DEPLOYMENT_CLAIM |
| Evidence Map eligibility | REJECTED_DO_NOT_MAP_AS_SUPPORTED |
| Layer 10 eligibility | NEGATIVE_OR_FORBIDDEN_REGISTER_ONLY |
| Future reconsideration | A future claim would require appropriately governed clinical/deployment evidence from later phases; P01 itself cannot support it. |

**Canonical reviewed wording**

> P01 is a public, non-clinical data-foundation and execution-validation phase; it does not establish clinical effectiveness, patient benefit, deployment safety, or medical-device readiness.

**Safe short form**

> P01 does not establish clinical effectiveness or deployment safety.

**Prohibited stronger wording**

> The P01 data foundation demonstrates clinical effectiveness or deployment safety.

**Layer 0 reasoning**

P01 uses public non-clinical EEG and contains no clinical endpoint or deployed safety evaluation. The proposed effectiveness/safety claim violates the current evidence ceiling and is rejected as a P01-supported result.


# PART IV — P01 DISPOSITION REGISTERS

## 29. Approved Claims

| Reviewed claim | Disposition | Canonical reviewed wording | Ceiling |
|---|---|---|---|
| P01-CLM-003/v1 | APPROVED | Under the frozen official core-window policy, all 12,910 accepted events yielded 12,910 valid core windows, with 0/12,910 invalid official core windows. | DATA_MATERIALIZATION_CLOSURE |
| P01-CLM-008/v1 | APPROVED | The accepted P01 execution completed 27/27 registered stages, 16/16 deterministic P01 gates, and 50/50 regression tests with 0 unresolved blockers; final execution-bundle integrity checks also closed. | EXECUTION_REPRODUCIBILITY_CLOSURE |

## 30. Qualified Claims

| Reviewed claim | Canonical reviewed wording | Mandatory limitations | Proximity requirement |
|---|---|---|---|
| P01-CLM-001/v1 | Within the frozen P01 binary motor-imagery branch, Phase 1 established a checksum-bound, provenance-traceable foundation over the three activated public EEG datasets. | PUBLIC_EEG_ONLY; NON_CLINICAL; BINARY_MI_BRANCH_SCOPE | Mandatory in proximate claim context |
| P01-CLM-002/v1 | The frozen P01 split assigned 172 subject groups wholly and disjointly across train, calibration, validation, and test roles and passed the implemented registered leakage/disjointness checks; this does not prove that every conceivable leakage mechanism is impossible. | IMPLEMENTED_CHECKS_ONLY | Mandatory in proximate claim context |
| P01-CLM-004/v1 | The official P01 core numerical artifact was persisted as 172 lossless HDF5 subject shards covering 12,910 windows and was verified under its Kaggle provider-version/logical-revision/manifest-hash identity contract. | PRIVATE_KAGGLE_EXTERNAL_ARTIFACT_ACCESS; SOURCE_LICENSE_REDISTRIBUTION_CONSTRAINTS | Mandatory in proximate claim context |
| P01-CLM-005/v1 | P01 applied the ANNOTATE_NOT_REPAIR quality policy across 489 quality summaries: 20 soft/provider flags were retained, 0/489 summaries were hard-invalid, and 0/12,910 official core windows were invalid under the registered criteria. | SOFT_FLAG_NOT_EQUIVALENT_TO_CORRUPTION | Mandatory in proximate claim context |
| P01-CLM-006/v1 | P01 established Layer-1 foundation readiness for each official A0-A13 identity; none of these ablation-effectiveness experiments was executed in P01, and A14 remained absent/prohibited. | NO_ABLATION_EFFECTIVENESS_IN_P01 | Mandatory in proximate claim context |
| P01-CLM-007/v1 | P01 established a fully matched A4 R2 Layer-1 data substrate for future governed evaluation: 12,910/12,910 parent events are represented without padding, clipping, fabricated samples, or parent-event loss. A4 R2 arose after the +4.0 s feasibility failure and was not evaluated for decoder effectiveness in P01. | A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01; A4_EFFECTIVENESS_NOT_EXECUTED | Mandatory in proximate claim context |
| P01-CLM-009/v1 | The accepted P01 run used Python 3.12.13 under a documented compatibility amendment and the governed adaptive-disk policy P01-L1-KAGGLE-ADAPTIVE-DISK-R1; the accepted records show no change to the frozen datasets, labels, subject split, core preprocessing, core window policy, or 12,910-event denominator attributable to these runtime/resource amendments. | ACTUAL_RUNTIME_PYTHON_3_12_13_WITH_COMPATIBILITY_AMENDMENT; ADAPTIVE_DISK_RESOURCE_AMENDMENT | Mandatory in proximate claim context |
| P01-CLM-010/v1 | P01 freezes a technical Layer-1 data contract that P02 may consume using the recorded dataset, label-map, split, preprocessing, core-window, and external-artifact identities; silent relabeling, rewindowing, split mutation, denominator substitution, or test-visibility leakage is prohibited. This is technical readiness, not evidence of P02 scientific success. | DOCUMENTARY_CLOSURE_SEQUENCE_REMAINS | Mandatory in proximate claim context |

## 31. Downgraded Claims

No P01 candidate required a separate `DOWNGRADED` disposition. Where safer wording was required, the core proposition remained supportable and was handled as `APPROVED_WITH_QUALIFICATIONS` rather than pretending that semantic content had been lost.

## 32. Deferred Claims

| Reviewed claim | Claim concept | Reason deferred | Future evidence required | Current permitted wording |
|---|---|---|---|---|
| P01-CLM-011/v1 | A4 R2 improves decoder performance relative to the core window. | P01 contains no A4 effectiveness experiment. | Reconsider only after a Protocol-authorized matched A4 effectiveness experiment with downstream model evidence. | P01 did not evaluate whether A4 R2 improves decoder performance relative to the core window; that effectiveness question remains deferred to a future governed matched downstream experiment. |

## 33. Rejected Claims

| Reviewed claim | Rejected claim concept | Violated ceiling | Reason | Could later evidence reopen? |
|---|---|---|---|---|
| P01-CLM-012/v1 | The P01 data foundation demonstrates clinical effectiveness or deployment safety. | NOT_CLAIMABLE_FROM_P01 | Public non-clinical data/integrity evidence cannot establish clinical effectiveness or deployment safety. | A future claim would require appropriately governed clinical/deployment evidence from later phases; P01 itself cannot support it. |

## 34. Blocked Claims

No P01 candidate is left blocked. Unsupported concepts were dispositioned as deferred or rejected because no unresolved upstream defect prevents Layer 0 completion.

## 35. Required P01 Disposition Matrix

| Source candidate | Disposition ID | Reviewed claim | Disposition | Support | Reviewed wording | Mandatory limitations | Evidence Map | Layer 10 |
|---|---|---|---|---|---|---|---|---|
| P01-CLAIM-CAND-001 | P01-L0-DISP-001 | P01-CLM-001/v1 | APPROVED_WITH_QUALIFICATIONS | SUPPORTED_WITH_QUALIFICATION | Within the frozen P01 binary motor-imagery branch, Phase 1 established a checksum-bound, provenance-traceable foundation over the three activated public EEG datasets. | PUBLIC_EEG_ONLY; NON_CLINICAL; BINARY_MI_BRANCH_SCOPE | ELIGIBLE_WITH_QUALIFICATION | ELIGIBLE_WITH_QUALIFICATION |
| P01-CLAIM-CAND-002 | P01-L0-DISP-002 | P01-CLM-002/v1 | APPROVED_WITH_QUALIFICATIONS | SUPPORTED_WITH_QUALIFICATION | The frozen P01 split assigned 172 subject groups wholly and disjointly across train, calibration, validation, and test roles and passed the implemented registered leakage/disjointness checks; this does not prove that every conceivable leakage mechanism is impossible. | IMPLEMENTED_CHECKS_ONLY | ELIGIBLE_WITH_QUALIFICATION | ELIGIBLE_WITH_QUALIFICATION |
| P01-CLAIM-CAND-003 | P01-L0-DISP-003 | P01-CLM-003/v1 | APPROVED | DIRECT | Under the frozen official core-window policy, all 12,910 accepted events yielded 12,910 valid core windows, with 0/12,910 invalid official core windows. | NO_MODEL_EFFECT_INFERENCE | ELIGIBLE_FOR_EVIDENCE_MAP | ELIGIBLE |
| P01-CLAIM-CAND-004 | P01-L0-DISP-004 | P01-CLM-004/v1 | APPROVED_WITH_QUALIFICATIONS | SUPPORTED_WITH_QUALIFICATION | The official P01 core numerical artifact was persisted as 172 lossless HDF5 subject shards covering 12,910 windows and was verified under its Kaggle provider-version/logical-revision/manifest-hash identity contract. | PRIVATE_KAGGLE_EXTERNAL_ARTIFACT_ACCESS; SOURCE_LICENSE_REDISTRIBUTION_CONSTRAINTS | ELIGIBLE_WITH_QUALIFICATION | ELIGIBLE_WITH_QUALIFICATION |
| P01-CLAIM-CAND-005 | P01-L0-DISP-005 | P01-CLM-005/v1 | APPROVED_WITH_QUALIFICATIONS | SUPPORTED_WITH_QUALIFICATION | P01 applied the ANNOTATE_NOT_REPAIR quality policy across 489 quality summaries: 20 soft/provider flags were retained, 0/489 summaries were hard-invalid, and 0/12,910 official core windows were invalid under the registered criteria. | SOFT_FLAG_NOT_EQUIVALENT_TO_CORRUPTION | ELIGIBLE_WITH_QUALIFICATION | ELIGIBLE_WITH_QUALIFICATION |
| P01-CLAIM-CAND-006 | P01-L0-DISP-006 | P01-CLM-006/v1 | APPROVED_WITH_QUALIFICATIONS | READINESS_ONLY | P01 established Layer-1 foundation readiness for each official A0-A13 identity; none of these ablation-effectiveness experiments was executed in P01, and A14 remained absent/prohibited. | NO_ABLATION_EFFECTIVENESS_IN_P01 | ELIGIBLE_WITH_QUALIFICATION | ELIGIBLE_WITH_QUALIFICATION |
| P01-CLAIM-CAND-007 | P01-L0-DISP-007 | P01-CLM-007/v1 | APPROVED_WITH_QUALIFICATIONS | READINESS_ONLY | P01 established a fully matched A4 R2 Layer-1 data substrate for future governed evaluation: 12,910/12,910 parent events are represented without padding, clipping, fabricated samples, or parent-event loss. A4 R2 arose after the +4.0 s feasibility failure and was not evaluated for decoder effectiveness in P01. | A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01; A4_EFFECTIVENESS_NOT_EXECUTED | ELIGIBLE_WITH_QUALIFICATION | ELIGIBLE_WITH_QUALIFICATION |
| P01-CLAIM-CAND-008 | P01-L0-DISP-008 | P01-CLM-008/v1 | APPROVED | DIRECT | The accepted P01 execution completed 27/27 registered stages, 16/16 deterministic P01 gates, and 50/50 regression tests with 0 unresolved blockers; final execution-bundle integrity checks also closed. | NO_EFFECTIVENESS_INFERENCE | ELIGIBLE_FOR_EVIDENCE_MAP | ELIGIBLE |
| P01-CLAIM-CAND-009 | P01-L0-DISP-009 | P01-CLM-009/v1 | APPROVED_WITH_QUALIFICATIONS | SUPPORTED_WITH_QUALIFICATION | The accepted P01 run used Python 3.12.13 under a documented compatibility amendment and the governed adaptive-disk policy P01-L1-KAGGLE-ADAPTIVE-DISK-R1; the accepted records show no change to the frozen datasets, labels, subject split, core preprocessing, core window policy, or 12,910-event denominator attributable to these runtime/resource amendments. | ACTUAL_RUNTIME_PYTHON_3_12_13_WITH_COMPATIBILITY_AMENDMENT; ADAPTIVE_DISK_RESOURCE_AMENDMENT | ELIGIBLE_WITH_QUALIFICATION | ELIGIBLE_WITH_QUALIFICATION |
| P01-CLAIM-CAND-010 | P01-L0-DISP-010 | P01-CLM-010/v1 | APPROVED_WITH_QUALIFICATIONS | READINESS_ONLY | P01 freezes a technical Layer-1 data contract that P02 may consume using the recorded dataset, label-map, split, preprocessing, core-window, and external-artifact identities; silent relabeling, rewindowing, split mutation, denominator substitution, or test-visibility leakage is prohibited. This is technical readiness, not evidence of P02 scientific success. | DOCUMENTARY_CLOSURE_SEQUENCE_REMAINS | ELIGIBLE_WITH_QUALIFICATION | ELIGIBLE_WITH_QUALIFICATION |
| P01-CLAIM-CAND-011 | P01-L0-DISP-011 | P01-CLM-011/v1 | DEFERRED | UNSUPPORTED_CURRENTLY | P01 did not evaluate whether A4 R2 improves decoder performance relative to the core window; that effectiveness question remains deferred to a future governed matched downstream experiment. | A4_EFFECTIVENESS_NOT_EXECUTED; A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01 | DEFERRED_NOT_CURRENTLY_MAPPABLE_AS_SUPPORTED | NEGATIVE_OR_DEFERRED_REGISTER_ONLY |
| P01-CLAIM-CAND-012 | P01-L0-DISP-012 | P01-CLM-012/v1 | REJECTED | PROHIBITED_BY_EVIDENCE_SCOPE | P01 is a public, non-clinical data-foundation and execution-validation phase; it does not establish clinical effectiveness, patient benefit, deployment safety, or medical-device readiness. | PUBLIC_EEG_ONLY; NON_CLINICAL; NO_DEPLOYMENT_CLAIM | REJECTED_DO_NOT_MAP_AS_SUPPORTED | NEGATIVE_OR_FORBIDDEN_REGISTER_ONLY |


# PART V — CROSS-CUTTING P01 CLAIM GOVERNANCE

## 36. A0–A13 Claim Governance

Claim-bearing language for A0–A13 is limited to **Layer-1 foundation readiness**. The readiness manifest contains exactly A0 through A13, with `executed_in_p01=false`; no P01 wording may imply effect size, superiority, robustness benefit, calibration benefit, or any other ablation-effectiveness result.

## 37. A14 Prohibition

`A14 = ABSENT / PROHIBITED`. No A14 selector, execution result, candidate effectiveness claim, or supported Evidence Map row may be introduced. Mentions of A14 in this authority are prohibition/absence statements only.

## 38. A4 Language Governance

**Permitted from P01:** A4 R2 identity; +0.0→+3.5 s matched profile; 560 samples; registered virtual members 0:320, 120:440, 240:560; 12,910/12,910 parent matching; no padding/clipping/fabrication/loss; future substrate readiness.

**Not permitted from P01:** accuracy improvement, AUROC improvement, robustness improvement, decoder superiority, statistical effectiveness, clinical effect, or any wording that retrospectively treats R2 as an originally preregistered effectiveness condition.

Any A4 figure/table caption must state in substance: **“foundation readiness only; effectiveness not evaluated in P01.”**

## 39. Clinical / Deployment Language Governance

Words such as *clinical*, *safe*, *effective*, *deployment-ready*, *real-world validated*, *medical*, and *patient benefit* require evidence not present in P01. `PUBLIC_EEG_ONLY`, `NON_CLINICAL`, and `NO_DEPLOYMENT_CLAIM` are mandatory constraints. The rejected P01 clinical/deployment candidate must remain visible in the negative/forbidden claim register to prevent later reintroduction.

## 40. Leakage Wording Governance

Permitted wording is bounded to the implemented checks: “the frozen subject-grouped split passed the registered disjointness/leakage checks” or equivalent. Prohibited wording includes “leakage is impossible”, “the split guarantees no leakage”, and other universal assertions.

## 41. Reproducibility and Execution Closure

Exact execution-closure facts (27/27 stages, 16/16 gates, 50/50 regression tests, zero unresolved blockers, checksum closure) may be stated directly. They establish deterministic execution/reproducibility closure only. R54 is a packaging/security repair and is not a scientific-effect limitation.

## 42. External Artifact Access

The core and A4 numerical artifacts are private Kaggle Datasets. Reviewed wording may claim exact provider/version/hash-governed retrieval and integrity, but must not imply unrestricted public byte access. Source-specific redistribution constraints remain active.

## 43. Causal, Absolute, and Validation-Language Audit

No reviewed P01 claim uses unsupported causal performance language. Exact absolutes are retained only where finite denominators prove them, such as 12,910/12,910 and 27/27. “Established” and “verified” are tied to source identity, data substrate, registered checks, or execution closure—not to unmeasured effectiveness.


# PART VI — P01 GOVERNED HANDOFFS

## 50. Evidence Map Handoff

The Evidence Map may map the ten supported P01 reviewed claims as supported/qualified claims according to their exact eligibility states. `P01-CLM-011/v1` is retained as deferred negative claim state and must not be mapped as supported; `P01-CLM-012/v1` is rejected and must not be mapped as supported.

| Reviewed claim | Disposition | Finding IDs | Protocol analyses | Run/stage IDs | Evidence paths | Limitations | Evidence Map state |
|---|---|---|---|---|---|---|---|
| P01-CLM-001/v1 | APPROVED_WITH_QUALIFICATIONS | P01-FIND-001 | P01-AC-001-SOURCE-INVENTORY | P01-STAGE-05; P01-STAGE-06; P01-STAGE-07 | records/datasets/BNCI2014_001/IHARQ-DATASETRECORD-20260806-42c424800627b6ee.json; records/datasets/Lee2019_MI/IHARQ-DATASETRECORD-20260806-adb91f25a65e588e.json; records/datasets/PhysioNetMI/IHARQ-DATASETRECORD-20260806-66309cda68771bef.json; reports/phase_01/sources/source_version_license_report.json | PUBLIC_EEG_ONLY; NON_CLINICAL; BINARY_MI_BRANCH_SCOPE | ELIGIBLE_WITH_QUALIFICATION |
| P01-CLM-002/v1 | APPROVED_WITH_QUALIFICATIONS | P01-FIND-002; P01-FIND-006 | P01-AC-002-SPLIT; P01-AC-005-LEAKAGE | P01-STAGE-11; P01-STAGE-17 | records/splits/P01-L1-SPLIT-OFFICIAL-R2/IHARQ-SPLITRECORD-20260806-e4e371d332c61e36.json; reports/phase_01/splits/disjointness.json; reports/phase_01/leakage/leakage_contamination.json | IMPLEMENTED_CHECKS_ONLY | ELIGIBLE_WITH_QUALIFICATION |
| P01-CLM-003/v1 | APPROVED | P01-FIND-003 | P01-AC-003-DENOMINATOR | P01-STAGE-13; P01-STAGE-14; P01-STAGE-16 | records/windows/; external_artifact_pointers/derived_windows_dataset.json | NO_MODEL_EFFECT_INFERENCE | ELIGIBLE_FOR_EVIDENCE_MAP |
| P01-CLM-004/v1 | APPROVED_WITH_QUALIFICATIONS | P01-FIND-004 | P01-AC-006-EXTERNAL | P01-STAGE-14; P01-STAGE-15; P01-STAGE-20 | reports/phase_01/storage/existing_core_dataset_adoption.json; external_artifact_pointers/derived_windows_dataset.json | PRIVATE_KAGGLE_EXTERNAL_ARTIFACT_ACCESS; SOURCE_LICENSE_REDISTRIBUTION_CONSTRAINTS | ELIGIBLE_WITH_QUALIFICATION |
| P01-CLM-005/v1 | APPROVED_WITH_QUALIFICATIONS | P01-FIND-005 | P01-AC-004-QUALITY | P01-STAGE-13; P01-STAGE-16 | reports/phase_01/quality/quality_coverage.json; records/quality/ | SOFT_FLAG_NOT_EQUIVALENT_TO_CORRUPTION | ELIGIBLE_WITH_QUALIFICATION |
| P01-CLM-006/v1 | APPROVED_WITH_QUALIFICATIONS | P01-FIND-008 | P01-AC-007-ABLATION-READINESS | P01-STAGE-18 | manifests/phase_01/layer1_ablation_readiness_l1_v1.json | NO_ABLATION_EFFECTIVENESS_IN_P01 | ELIGIBLE_WITH_QUALIFICATION |
| P01-CLM-007/v1 | APPROVED_WITH_QUALIFICATIONS | P01-FIND-009; P01-FIND-010 | P01-AC-008-A4 | P01-STAGE-14; P01-STAGE-15; P01-STAGE-18 | external_artifact_pointers/a4_window_family_dataset.json; reports/phase_01/storage/a4_derived_output_storage_actual_precommit.json; config_snapshot/p01_l1_a4_window_family_freeze_R2.json; Phase_01_Notebook.ipynb (R49 A4 boundary explanation) | A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01; A4_EFFECTIVENESS_NOT_EXECUTED | ELIGIBLE_WITH_QUALIFICATION |
| P01-CLM-008/v1 | APPROVED | P01-FIND-012 | P01-AC-010-GATES-REPAIRS | P01-STAGE-04; P01-STAGE-23; P01-STAGE-24; P01-STAGE-26 | reports/phase_01/tests/stage_results.json; gate_decision.json; reports/phase_01/tests/phase0_and_runtime_regression.json; reports/phase_01/repair_reentry.json; checksums.sha256 | NO_EFFECTIVENESS_INFERENCE | ELIGIBLE_FOR_EVIDENCE_MAP |
| P01-CLM-009/v1 | APPROVED_WITH_QUALIFICATIONS | P01-FIND-011 | P01-AC-009-ENVIRONMENT | P01-STAGE-01; P01-STAGE-03 | environment_manifest.json; environment_amendment.json | ACTUAL_RUNTIME_PYTHON_3_12_13_WITH_COMPATIBILITY_AMENDMENT; ADAPTIVE_DISK_RESOURCE_AMENDMENT | ELIGIBLE_WITH_QUALIFICATION |
| P01-CLM-010/v1 | APPROVED_WITH_QUALIFICATIONS | P01-FIND-014 | P01-AC-003-DENOMINATOR; P01-AC-005-LEAKAGE; P01-AC-006-EXTERNAL; P01-AC-007-ABLATION-READINESS; P01-AC-010-GATES-REPAIRS | P01-STAGE-22; P01-STAGE-23; P01-STAGE-26 | handoffs/phase_01_to_phase_02.yaml; phase2_handoff/phase_01_to_phase_02.yaml | DOCUMENTARY_CLOSURE_SEQUENCE_REMAINS | ELIGIBLE_WITH_QUALIFICATION |
| P01-CLM-011/v1 | DEFERRED | P01-FIND-009 | P01-AC-008-A4 | P01-STAGE-14; P01-STAGE-15 | external_artifact_pointers/a4_window_family_dataset.json; config_snapshot/p01_l1_a4_window_family_freeze_R2.json | A4_EFFECTIVENESS_NOT_EXECUTED; A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01 | DEFERRED_NOT_CURRENTLY_MAPPABLE_AS_SUPPORTED |
| P01-CLM-012/v1 | REJECTED | P01-FIND-001; P01-FIND-012 | P01-AC-001-SOURCE-INVENTORY; P01-AC-010-GATES-REPAIRS | P01-STAGE-06; P01-STAGE-26 | reports/phase_01/sources/source_version_license_report.json; gate_decision.json | PUBLIC_EEG_ONLY; NON_CLINICAL; NO_DEPLOYMENT_CLAIM | REJECTED_DO_NOT_MAP_AS_SUPPORTED |

## 51. Layer 10 Eligibility

Layer 10 may later render only Layer-0-permitted reviewed claims through accepted Evidence Map rows. Qualified claims must preserve their proximate limitation/warning text. Deferred/rejected concepts may appear only in negative/deferred/prohibited-claim views, never as positive result cards.

| Reviewed claim | Disposition | Layer 10 eligibility | Required warning/qualification |
|---|---|---|---|
| P01-CLM-001/v1 | APPROVED_WITH_QUALIFICATIONS | ELIGIBLE_WITH_QUALIFICATION | PUBLIC_EEG_ONLY; NON_CLINICAL; BINARY_MI_BRANCH_SCOPE |
| P01-CLM-002/v1 | APPROVED_WITH_QUALIFICATIONS | ELIGIBLE_WITH_QUALIFICATION | IMPLEMENTED_CHECKS_ONLY |
| P01-CLM-003/v1 | APPROVED | ELIGIBLE | NO_MODEL_EFFECT_INFERENCE |
| P01-CLM-004/v1 | APPROVED_WITH_QUALIFICATIONS | ELIGIBLE_WITH_QUALIFICATION | PRIVATE_KAGGLE_EXTERNAL_ARTIFACT_ACCESS; SOURCE_LICENSE_REDISTRIBUTION_CONSTRAINTS |
| P01-CLM-005/v1 | APPROVED_WITH_QUALIFICATIONS | ELIGIBLE_WITH_QUALIFICATION | SOFT_FLAG_NOT_EQUIVALENT_TO_CORRUPTION |
| P01-CLM-006/v1 | APPROVED_WITH_QUALIFICATIONS | ELIGIBLE_WITH_QUALIFICATION | NO_ABLATION_EFFECTIVENESS_IN_P01 |
| P01-CLM-007/v1 | APPROVED_WITH_QUALIFICATIONS | ELIGIBLE_WITH_QUALIFICATION | A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01; A4_EFFECTIVENESS_NOT_EXECUTED |
| P01-CLM-008/v1 | APPROVED | ELIGIBLE | NO_EFFECTIVENESS_INFERENCE |
| P01-CLM-009/v1 | APPROVED_WITH_QUALIFICATIONS | ELIGIBLE_WITH_QUALIFICATION | ACTUAL_RUNTIME_PYTHON_3_12_13_WITH_COMPATIBILITY_AMENDMENT; ADAPTIVE_DISK_RESOURCE_AMENDMENT |
| P01-CLM-010/v1 | APPROVED_WITH_QUALIFICATIONS | ELIGIBLE_WITH_QUALIFICATION | DOCUMENTARY_CLOSURE_SEQUENCE_REMAINS |
| P01-CLM-011/v1 | DEFERRED | NEGATIVE_OR_DEFERRED_REGISTER_ONLY | A4_EFFECTIVENESS_NOT_EXECUTED; A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01 |
| P01-CLM-012/v1 | REJECTED | NEGATIVE_OR_FORBIDDEN_REGISTER_ONLY | PUBLIC_EEG_ONLY; NON_CLINICAL; NO_DEPLOYMENT_CLAIM |

## 52. P02 Claim-Boundary Inheritance

P02 inherits the frozen P01 data contract and all relevant P01 claim ceilings. P02 must not treat Layer 0 approval of P01 readiness claims as evidence that models perform well, A4 works better, calibration helps, clinical value exists, or deployment safety has been established. P02 may consume the exact data/split/label/preprocessing/window/pointer identities and must generate its own Protocol-authorized scientific evidence for model claims.


# PART VII — P01 LAYER 0 FINAL DECISION

## 53. Final Layer 0 Summary

| Metric | Result |
|---|---|
| P00 claims preserved | PASS — 7/7 current qualified versions |
| P01 candidate claims reviewed | 12/12 |
| Approved | 2 |
| Approved with qualifications | 8 |
| Downgraded | 0 |
| Deferred | 1 |
| Rejected | 1 |
| Blocked | 0 |
| Claims without disposition | 0 |
| Permitted claims without findings | 0 |
| Permitted claims with broken evidence links | 0 |
| Claims exceeding evidence ceiling | 0 |
| Claims missing mandatory limitations | 0 |
| A0–A13 claim governance | PASS |
| A14 prohibition | PASS |
| A4 effectiveness boundary | PASS |
| Clinical boundary | PASS |
| Deployment boundary | PASS |
| Leakage wording boundary | PASS |
| Measurements unchanged | PASS |
| Protocol unchanged | PASS |
| Phase Analysis findings unchanged | PASS |
| Inter-level harmony | PASS |
| Intra-Layer0 harmony | PASS |
| Cross-phase claim harmony | PASS |
| Evidence Map handoff | PASS |
| Layer 10 eligibility | PASS |
| Freeze-critical blockers | 0 |
| READY FOR EVIDENCE MAP | YES |

## 54. Success Decision

```text
CUMULATIVE_LAYER0_THROUGH_P01:
PASS — FINALIZED AND FROZEN

P00 prior dispositions:
PRESERVED

P01 candidate claims:
FULLY_REVIEWED

unresolved Layer0 claims:
0

measurements changed:
NO

Protocol changed:
NO

Phase Analysis changed:
NO

A14:
ABSENT_PROHIBITED

A4 effectiveness claim:
NOT APPROVED FROM P01

clinical/deployment claims:
NOT APPROVED FROM P01

Evidence Map inputs:
READY

Layer 10 claim inputs:
READY_WITH_LAYER0_GOVERNANCE

freeze-critical blockers:
0

next governed step:
UPDATE THE PAPER AND THESIS EVIDENCE MAP THROUGH P01
```

Layer 0 completion does **not** mean Phase 1 is fully closed. The next governed step is the Paper and Thesis Evidence Map update through P01, followed later by the Layer 10 governed rendering/package and cumulative project-state closure.


# P01 LAYER 0 APPENDICES

## Appendix A. Claim-to-Finding Matrix

| Reviewed claim | Candidate | Disposition | Finding IDs | Evidence class | Ceiling |
|---|---|---|---|---|---|
| P01-CLM-001/v1 | P01-CLAIM-CAND-001 | APPROVED_WITH_QUALIFICATIONS | P01-FIND-001 | PROVENANCE_EVIDENCE | DATA_PROVENANCE_REPRODUCIBILITY |
| P01-CLM-002/v1 | P01-CLAIM-CAND-002 | APPROVED_WITH_QUALIFICATIONS | P01-FIND-002; P01-FIND-006 | VALIDATION_EVIDENCE | IMPLEMENTED_SPLIT_AND_LEAKAGE_CHECKS |
| P01-CLM-003/v1 | P01-CLAIM-CAND-003 | APPROVED | P01-FIND-003 | INTEGRITY_EVIDENCE | DATA_MATERIALIZATION_CLOSURE |
| P01-CLM-004/v1 | P01-CLAIM-CAND-004 | APPROVED_WITH_QUALIFICATIONS | P01-FIND-004 | INTEGRITY_EVIDENCE | RETRIEVAL_STORAGE_INTEGRITY_REPRODUCIBILITY |
| P01-CLM-005/v1 | P01-CLAIM-CAND-005 | APPROVED_WITH_QUALIFICATIONS | P01-FIND-005 | VALIDATION_EVIDENCE | QUALITY_ANNOTATION_AND_HARD_VALIDITY_CLOSURE |
| P01-CLM-006/v1 | P01-CLAIM-CAND-006 | APPROVED_WITH_QUALIFICATIONS | P01-FIND-008 | READINESS_EVIDENCE | FOUNDATION_READINESS_ONLY |
| P01-CLM-007/v1 | P01-CLAIM-CAND-007 | APPROVED_WITH_QUALIFICATIONS | P01-FIND-009; P01-FIND-010 | READINESS_EVIDENCE | FUTURE_A4_SUBSTRATE_READINESS |
| P01-CLM-008/v1 | P01-CLAIM-CAND-008 | APPROVED | P01-FIND-012 | EXECUTION_EVIDENCE | EXECUTION_REPRODUCIBILITY_CLOSURE |
| P01-CLM-009/v1 | P01-CLAIM-CAND-009 | APPROVED_WITH_QUALIFICATIONS | P01-FIND-011 | EXECUTION_EVIDENCE | EXECUTION_REPRODUCIBILITY |
| P01-CLM-010/v1 | P01-CLAIM-CAND-010 | APPROVED_WITH_QUALIFICATIONS | P01-FIND-014 | READINESS_EVIDENCE | DOWNSTREAM_TECHNICAL_DATA_CONTRACT_READINESS |
| P01-CLM-011/v1 | P01-CLAIM-CAND-011 | DEFERRED | P01-FIND-009 | READINESS_EVIDENCE | NOT_CLAIMABLE_FROM_P01 |
| P01-CLM-012/v1 | P01-CLAIM-CAND-012 | REJECTED | P01-FIND-001; P01-FIND-012 | EXECUTION_EVIDENCE | NOT_CLAIMABLE_FROM_P01 |

## Appendix B. Claim-to-Evidence Matrix

| Reviewed claim | Run/stage IDs | Record/artifact IDs | Evidence paths |
|---|---|---|---|
| P01-CLM-001/v1 | P01-STAGE-05; P01-STAGE-06; P01-STAGE-07 | IHARQ-DATASETRECORD-20260806-66309cda68771bef; IHARQ-DATASETRECORD-20260806-42c424800627b6ee; IHARQ-DATASETRECORD-20260806-adb91f25a65e588e | records/datasets/BNCI2014_001/IHARQ-DATASETRECORD-20260806-42c424800627b6ee.json; records/datasets/Lee2019_MI/IHARQ-DATASETRECORD-20260806-adb91f25a65e588e.json; records/datasets/PhysioNetMI/IHARQ-DATASETRECORD-20260806-66309cda68771bef.json; reports/phase_01/sources/source_version_license_report.json |
| P01-CLM-002/v1 | P01-STAGE-11; P01-STAGE-17 | IHARQ-SPLITRECORD-20260806-e4e371d332c61e36 | records/splits/P01-L1-SPLIT-OFFICIAL-R2/IHARQ-SPLITRECORD-20260806-e4e371d332c61e36.json; reports/phase_01/splits/disjointness.json; reports/phase_01/leakage/leakage_contamination.json |
| P01-CLM-003/v1 | P01-STAGE-13; P01-STAGE-14; P01-STAGE-16 | IHARQ-SPLITRECORD-20260806-e4e371d332c61e36; IHARQ-PREPROCESSINGRECORD-20260806-a11b59eeb3861a08 | records/windows/; external_artifact_pointers/derived_windows_dataset.json |
| P01-CLM-004/v1 | P01-STAGE-14; P01-STAGE-15; P01-STAGE-20 | P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473; IHARQ-SPLITRECORD-20260806-e4e371d332c61e36; IHARQ-PREPROCESSINGRECORD-20260806-a11b59eeb3861a08 | reports/phase_01/storage/existing_core_dataset_adoption.json; external_artifact_pointers/derived_windows_dataset.json |
| P01-CLM-005/v1 | P01-STAGE-13; P01-STAGE-16 | records/quality/ (489 governed quality summaries) | reports/phase_01/quality/quality_coverage.json; records/quality/ |
| P01-CLM-006/v1 | P01-STAGE-18 | A0-A13 readiness manifest | manifests/phase_01/layer1_ablation_readiness_l1_v1.json |
| P01-CLM-007/v1 | P01-STAGE-14; P01-STAGE-15; P01-STAGE-18 | P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13; P01-L1-A4-WINDOW-FAMILY-FREEZE-R2 | external_artifact_pointers/a4_window_family_dataset.json; reports/phase_01/storage/a4_derived_output_storage_actual_precommit.json; config_snapshot/p01_l1_a4_window_family_freeze_R2.json; Phase_01_Notebook.ipynb (R49 A4 boundary explanation) |
| P01-CLM-008/v1 | P01-STAGE-04; P01-STAGE-23; P01-STAGE-24; P01-STAGE-26 | P01-G01...P01-G16; stage_results 00...26 | reports/phase_01/tests/stage_results.json; gate_decision.json; reports/phase_01/tests/phase0_and_runtime_regression.json; reports/phase_01/repair_reentry.json; checksums.sha256 |
| P01-CLM-009/v1 | P01-STAGE-01; P01-STAGE-03 | P01-L1-KAGGLE-ENV-FREEZE-R5; P01-L1-KAGGLE-ADAPTIVE-DISK-R1 | environment_manifest.json; environment_amendment.json |
| P01-CLM-010/v1 | P01-STAGE-22; P01-STAGE-23; P01-STAGE-26 | IHARQ-DATASETRECORD-20260806-66309cda68771bef; IHARQ-DATASETRECORD-20260806-42c424800627b6ee; IHARQ-DATASETRECORD-20260806-adb91f25a65e588e; IHARQ-LABELMAPRECORD-20260806-4379781a3b5f5ea9; IHARQ-LABELMAPRECORD-20260806-587dcfff81307768; IHARQ-LABELMAPRECORD-20260806-b551cfd20335896c; IHARQ-SPLITRECORD-20260806-e4e371d332c61e36; IHARQ-PREPROCESSINGRECORD-20260806-a11b59eeb3861a08; P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473; P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13 | handoffs/phase_01_to_phase_02.yaml; phase2_handoff/phase_01_to_phase_02.yaml |
| P01-CLM-011/v1 | P01-STAGE-14; P01-STAGE-15 | P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13; P01-L1-A4-WINDOW-FAMILY-FREEZE-R2 | external_artifact_pointers/a4_window_family_dataset.json; config_snapshot/p01_l1_a4_window_family_freeze_R2.json |
| P01-CLM-012/v1 | P01-STAGE-06; P01-STAGE-26 | IHARQ-DATASETRECORD-20260806-66309cda68771bef; IHARQ-DATASETRECORD-20260806-42c424800627b6ee; IHARQ-DATASETRECORD-20260806-adb91f25a65e588e | reports/phase_01/sources/source_version_license_report.json; gate_decision.json |

## Appendix C. Limitation-to-Claim Matrix

| Reviewed claim | Limitation / constraint | Kind | Proximity requirement | Meaning |
|---|---|---|---|---|
| P01-CLM-001/v1 | PUBLIC_EEG_ONLY | CANONICAL_CUMULATIVE_LIMITATION | MANDATORY_IN_PROXIMATE_CONTEXT | The empirical substrate is public benchmark/research EEG, not a clinical or deployment population. |
| P01-CLM-001/v1 | NON_CLINICAL | CANONICAL_CUMULATIVE_LIMITATION | MANDATORY_IN_PROXIMATE_CONTEXT | No clinical cohort, clinical endpoint, or treatment outcome is present. |
| P01-CLM-001/v1 | BINARY_MI_BRANCH_SCOPE | CANONICAL_CUMULATIVE_LIMITATION | MANDATORY_IN_PROXIMATE_CONTEXT | P01 official supervised denominator is left-hand versus right-hand imagery only; rest, feet, tongue, execution, technical and unlabeled online/test events are excluded as defined per source. |
| P01-CLM-002/v1 | IMPLEMENTED_CHECKS_ONLY | SOURCE_CANDIDATE_CLAIM_BOUNDARY_TAG | MANDATORY_IN_PROXIMATE_CONTEXT | Leakage/disjointness wording is bounded to the implemented registered checks. |
| P01-CLM-003/v1 | NO_MODEL_EFFECT_INFERENCE | SOURCE_CANDIDATE_CLAIM_BOUNDARY_TAG | MANDATORY_IN_METHOD_OR_RESULTS_CONTEXT | Data materialization closure does not support decoder/model-effect inference. |
| P01-CLM-004/v1 | PRIVATE_KAGGLE_EXTERNAL_ARTIFACT_ACCESS | CANONICAL_CUMULATIVE_LIMITATION | MANDATORY_IN_PROXIMATE_CONTEXT | Core and A4 numerical HDF5 artifacts are private Kaggle Datasets. |
| P01-CLM-004/v1 | SOURCE_LICENSE_REDISTRIBUTION_CONSTRAINTS | CANONICAL_CUMULATIVE_LIMITATION | MANDATORY_IN_PROXIMATE_CONTEXT | Source-specific licenses, especially BNCI CC BY-ND, constrain redistribution of raw/derived signal bytes. |
| P01-CLM-005/v1 | SOFT_FLAG_NOT_EQUIVALENT_TO_CORRUPTION | SOURCE_CANDIDATE_CLAIM_BOUNDARY_TAG | MANDATORY_IN_PROXIMATE_CONTEXT | Soft/provider flags are annotations and are not equivalent to physiological corruption. |
| P01-CLM-006/v1 | NO_ABLATION_EFFECTIVENESS_IN_P01 | SOURCE_CANDIDATE_CLAIM_BOUNDARY_TAG | MANDATORY_IN_PROXIMATE_CONTEXT | A0-A13 Layer-1 readiness is not evidence of ablation effectiveness. |
| P01-CLM-007/v1 | A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01 | CANONICAL_CUMULATIVE_LIMITATION | MANDATORY_IN_PROXIMATE_CONTEXT | A4 R2 was introduced after a real +4.0 s boundary infeasibility was observed. |
| P01-CLM-007/v1 | A4_EFFECTIVENESS_NOT_EXECUTED | SOURCE_CANDIDATE_CLAIM_BOUNDARY_TAG | MANDATORY_IN_PROXIMATE_CONTEXT | No A4 decoder-effectiveness experiment was executed in P01. |
| P01-CLM-008/v1 | NO_EFFECTIVENESS_INFERENCE | SOURCE_CANDIDATE_CLAIM_BOUNDARY_TAG | MANDATORY_IN_METHOD_OR_RESULTS_CONTEXT | Execution/test/gate closure is not scientific-effectiveness evidence. |
| P01-CLM-009/v1 | ACTUAL_RUNTIME_PYTHON_3_12_13_WITH_COMPATIBILITY_AMENDMENT | CANONICAL_CUMULATIVE_LIMITATION | MANDATORY_IN_PROXIMATE_CONTEXT | Build Book intended Python 3.11, while accepted Kaggle execution used Python 3.12.13 under a documented compatibility amendment. |
| P01-CLM-009/v1 | ADAPTIVE_DISK_RESOURCE_AMENDMENT | CANONICAL_CUMULATIVE_LIMITATION | MANDATORY_IN_PROXIMATE_CONTEXT | Governed amendment P01-L1-KAGGLE-ADAPTIVE-DISK-R1 replaced the legacy 60 GiB preflight with an adaptive measured requirement with 6.0 GiB effective minimum; observed free disk was 18.94 GiB. |
| P01-CLM-010/v1 | DOCUMENTARY_CLOSURE_SEQUENCE_REMAINS | SOURCE_CANDIDATE_CLAIM_BOUNDARY_TAG | MANDATORY_IN_PROXIMATE_CONTEXT | Technical readiness does not bypass the governed documentary sequence. |
| P01-CLM-011/v1 | A4_EFFECTIVENESS_NOT_EXECUTED | SOURCE_CANDIDATE_CLAIM_BOUNDARY_TAG | MANDATORY_IN_DISPOSITION_AND_NEGATIVE_REGISTER | No A4 decoder-effectiveness experiment was executed in P01. |
| P01-CLM-011/v1 | A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01 | CANONICAL_CUMULATIVE_LIMITATION | MANDATORY_IN_DISPOSITION_AND_NEGATIVE_REGISTER | A4 R2 was introduced after a real +4.0 s boundary infeasibility was observed. |
| P01-CLM-012/v1 | PUBLIC_EEG_ONLY | CANONICAL_CUMULATIVE_LIMITATION | MANDATORY_IN_DISPOSITION_AND_NEGATIVE_REGISTER | The empirical substrate is public benchmark/research EEG, not a clinical or deployment population. |
| P01-CLM-012/v1 | NON_CLINICAL | CANONICAL_CUMULATIVE_LIMITATION | MANDATORY_IN_DISPOSITION_AND_NEGATIVE_REGISTER | No clinical cohort, clinical endpoint, or treatment outcome is present. |
| P01-CLM-012/v1 | NO_DEPLOYMENT_CLAIM | CANONICAL_CUMULATIVE_LIMITATION | MANDATORY_IN_DISPOSITION_AND_NEGATIVE_REGISTER | P01 does not evaluate deployed real-world control, operational safety, or medical-device behavior. |

## Appendix D. Forbidden Wording Register

| Claim concept | Reason | Claim source | Status | Reconsideration |
|---|---|---|---|---|
| A4 improves decoder performance | No P01 effectiveness experiment exists | P01-CLAIM-CAND-011 | DEFERRED | Protocol-authorized matched downstream A4 effectiveness experiment |
| P01 demonstrates clinical effectiveness or deployment safety | PUBLIC_EEG_ONLY + NON_CLINICAL + NO_DEPLOYMENT_CLAIM | P01-CLAIM-CAND-012 | REJECTED | Appropriately governed future clinical/deployment evidence; P01 remains non-clinical |
| P01 proves leakage is impossible | Implemented checks cannot establish universal absence | P01-CLM-002/v1 | PROHIBITED_STRONGER_WORDING | Wording must remain tied to tested checks |
| P01 EEG is flawless/artifact-free | Soft/provider flags exist and zero hard-invalid is criterion-bounded | P01-CLM-005/v1 | PROHIBITED_STRONGER_WORDING | Different validated quality authority would be required |
| A0-A13 effectiveness is established | Only readiness infrastructure exists in P01 | P01-CLM-006/v1 | PROHIBITED_STRONGER_WORDING | Downstream governed ablation experiments |
| Passing gates proves scientific effectiveness | Gate/test evidence is execution/reproducibility evidence only | P01-CLM-008/v1 | PROHIBITED_STRONGER_WORDING | Later scientific/model evidence |

## Appendix F. P01 Disposition Matrix

| Source candidate | Disposition ID | Reviewed claim | Disposition | Support | Reviewed wording | Mandatory limitations | Evidence Map | Layer 10 |
|---|---|---|---|---|---|---|---|---|
| P01-CLAIM-CAND-001 | P01-L0-DISP-001 | P01-CLM-001/v1 | APPROVED_WITH_QUALIFICATIONS | SUPPORTED_WITH_QUALIFICATION | Within the frozen P01 binary motor-imagery branch, Phase 1 established a checksum-bound, provenance-traceable foundation over the three activated public EEG datasets. | PUBLIC_EEG_ONLY; NON_CLINICAL; BINARY_MI_BRANCH_SCOPE | ELIGIBLE_WITH_QUALIFICATION | ELIGIBLE_WITH_QUALIFICATION |
| P01-CLAIM-CAND-002 | P01-L0-DISP-002 | P01-CLM-002/v1 | APPROVED_WITH_QUALIFICATIONS | SUPPORTED_WITH_QUALIFICATION | The frozen P01 split assigned 172 subject groups wholly and disjointly across train, calibration, validation, and test roles and passed the implemented registered leakage/disjointness checks; this does not prove that every conceivable leakage mechanism is impossible. | IMPLEMENTED_CHECKS_ONLY | ELIGIBLE_WITH_QUALIFICATION | ELIGIBLE_WITH_QUALIFICATION |
| P01-CLAIM-CAND-003 | P01-L0-DISP-003 | P01-CLM-003/v1 | APPROVED | DIRECT | Under the frozen official core-window policy, all 12,910 accepted events yielded 12,910 valid core windows, with 0/12,910 invalid official core windows. | NO_MODEL_EFFECT_INFERENCE | ELIGIBLE_FOR_EVIDENCE_MAP | ELIGIBLE |
| P01-CLAIM-CAND-004 | P01-L0-DISP-004 | P01-CLM-004/v1 | APPROVED_WITH_QUALIFICATIONS | SUPPORTED_WITH_QUALIFICATION | The official P01 core numerical artifact was persisted as 172 lossless HDF5 subject shards covering 12,910 windows and was verified under its Kaggle provider-version/logical-revision/manifest-hash identity contract. | PRIVATE_KAGGLE_EXTERNAL_ARTIFACT_ACCESS; SOURCE_LICENSE_REDISTRIBUTION_CONSTRAINTS | ELIGIBLE_WITH_QUALIFICATION | ELIGIBLE_WITH_QUALIFICATION |
| P01-CLAIM-CAND-005 | P01-L0-DISP-005 | P01-CLM-005/v1 | APPROVED_WITH_QUALIFICATIONS | SUPPORTED_WITH_QUALIFICATION | P01 applied the ANNOTATE_NOT_REPAIR quality policy across 489 quality summaries: 20 soft/provider flags were retained, 0/489 summaries were hard-invalid, and 0/12,910 official core windows were invalid under the registered criteria. | SOFT_FLAG_NOT_EQUIVALENT_TO_CORRUPTION | ELIGIBLE_WITH_QUALIFICATION | ELIGIBLE_WITH_QUALIFICATION |
| P01-CLAIM-CAND-006 | P01-L0-DISP-006 | P01-CLM-006/v1 | APPROVED_WITH_QUALIFICATIONS | READINESS_ONLY | P01 established Layer-1 foundation readiness for each official A0-A13 identity; none of these ablation-effectiveness experiments was executed in P01, and A14 remained absent/prohibited. | NO_ABLATION_EFFECTIVENESS_IN_P01 | ELIGIBLE_WITH_QUALIFICATION | ELIGIBLE_WITH_QUALIFICATION |
| P01-CLAIM-CAND-007 | P01-L0-DISP-007 | P01-CLM-007/v1 | APPROVED_WITH_QUALIFICATIONS | READINESS_ONLY | P01 established a fully matched A4 R2 Layer-1 data substrate for future governed evaluation: 12,910/12,910 parent events are represented without padding, clipping, fabricated samples, or parent-event loss. A4 R2 arose after the +4.0 s feasibility failure and was not evaluated for decoder effectiveness in P01. | A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01; A4_EFFECTIVENESS_NOT_EXECUTED | ELIGIBLE_WITH_QUALIFICATION | ELIGIBLE_WITH_QUALIFICATION |
| P01-CLAIM-CAND-008 | P01-L0-DISP-008 | P01-CLM-008/v1 | APPROVED | DIRECT | The accepted P01 execution completed 27/27 registered stages, 16/16 deterministic P01 gates, and 50/50 regression tests with 0 unresolved blockers; final execution-bundle integrity checks also closed. | NO_EFFECTIVENESS_INFERENCE | ELIGIBLE_FOR_EVIDENCE_MAP | ELIGIBLE |
| P01-CLAIM-CAND-009 | P01-L0-DISP-009 | P01-CLM-009/v1 | APPROVED_WITH_QUALIFICATIONS | SUPPORTED_WITH_QUALIFICATION | The accepted P01 run used Python 3.12.13 under a documented compatibility amendment and the governed adaptive-disk policy P01-L1-KAGGLE-ADAPTIVE-DISK-R1; the accepted records show no change to the frozen datasets, labels, subject split, core preprocessing, core window policy, or 12,910-event denominator attributable to these runtime/resource amendments. | ACTUAL_RUNTIME_PYTHON_3_12_13_WITH_COMPATIBILITY_AMENDMENT; ADAPTIVE_DISK_RESOURCE_AMENDMENT | ELIGIBLE_WITH_QUALIFICATION | ELIGIBLE_WITH_QUALIFICATION |
| P01-CLAIM-CAND-010 | P01-L0-DISP-010 | P01-CLM-010/v1 | APPROVED_WITH_QUALIFICATIONS | READINESS_ONLY | P01 freezes a technical Layer-1 data contract that P02 may consume using the recorded dataset, label-map, split, preprocessing, core-window, and external-artifact identities; silent relabeling, rewindowing, split mutation, denominator substitution, or test-visibility leakage is prohibited. This is technical readiness, not evidence of P02 scientific success. | DOCUMENTARY_CLOSURE_SEQUENCE_REMAINS | ELIGIBLE_WITH_QUALIFICATION | ELIGIBLE_WITH_QUALIFICATION |
| P01-CLAIM-CAND-011 | P01-L0-DISP-011 | P01-CLM-011/v1 | DEFERRED | UNSUPPORTED_CURRENTLY | P01 did not evaluate whether A4 R2 improves decoder performance relative to the core window; that effectiveness question remains deferred to a future governed matched downstream experiment. | A4_EFFECTIVENESS_NOT_EXECUTED; A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01 | DEFERRED_NOT_CURRENTLY_MAPPABLE_AS_SUPPORTED | NEGATIVE_OR_DEFERRED_REGISTER_ONLY |
| P01-CLAIM-CAND-012 | P01-L0-DISP-012 | P01-CLM-012/v1 | REJECTED | PROHIBITED_BY_EVIDENCE_SCOPE | P01 is a public, non-clinical data-foundation and execution-validation phase; it does not establish clinical effectiveness, patient benefit, deployment safety, or medical-device readiness. | PUBLIC_EEG_ONLY; NON_CLINICAL; NO_DEPLOYMENT_CLAIM | REJECTED_DO_NOT_MAP_AS_SUPPORTED | NEGATIVE_OR_FORBIDDEN_REGISTER_ONLY |

## Appendix G. Source Utilization Matrix

| Source | Role | Use in Layer 0 | Conflict/status |
|---|---|---|---|
| Governance V6.1 | Layer 0 authority and sequencing | Authority boundary; Evidence Map/Layer 10 order; no evidence mutation | PASS |
| Seven governing authorities | System/record/method/phase constraints | Claim scope and evidence ceilings | PASS |
| Final cumulative Protocol v1.0 through P01 | Immutable execution/analysis contract | P01 ceilings, A0–A13, A14, A4, environment, run matrix | PASS |
| Final cumulative Phase Analysis through P01 | Primary candidate/finding/limitation input | All 12 P01 candidates; 14 P01 findings; P00 continuity | PASS |
| P00 Layer 0 release / final audit | Historical governed claim state | Preserved seven P00 v2 qualified claims; no reopen | PASS |
| P00 Evidence Map / basic Layer 10 | Historical downstream claim use | Continuity only | PASS |
| P01 accepted execution bundle | Primary evidence confirmation | Counts, records, gates, checksums, pointers, handoff, amendments | PASS |
| Executed P01 notebook | Execution/repair chronology | A4 feasibility and repair-history context | PASS |

## Appendix H. Validation Results

Final deterministic validation is written to `validation/Layer0_Final_Validation.json`. It checks candidate completeness, finding integrity, evidence traceability, limitation coverage, claim ceilings, A0–A13/A14/A4 safety, clinical/deployment safety, Protocol/Phase Analysis no-change, P00 continuity, Evidence Map readiness, machine-readable parity, secret/placeholder safety, and final package integrity.



# DERIVATIVE CERTIFICATION

```text
P01_LAYER0_PHASE_SPECIFIC_DERIVATIVE:
PASS — COMPLETE NON-AUTHORITATIVE DERIVATIVE
P01 candidates reviewed: 12/12
Approved: 2
Approved with qualifications: 8
Deferred: 1
Rejected: 1
Blocked: 0
Unresolved: 0
A14: ABSENT_PROHIBITED
A4 effectiveness: NOT APPROVED FROM P01
clinical/deployment effectiveness: NOT APPROVED FROM P01
READY FOR EVIDENCE MAP: YES
```
