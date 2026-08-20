---

title: "IHARQ Cumulative Phase Evidence, Results, and Interpretation Report Through P01"

report_id: "IHARQ-CUMULATIVE-PHASE-EVIDENCE-RESULTS-INTERPRETATION-THROUGH-P01-R2-LAYER0-INTEGRATED"

revision: "R2-LAYER0-INTEGRATED"

phases: ["P00", "P01"]

dominant_analysis_phase: "P01"

status: "FINALIZED_FROZEN_LAYER0_EMBEDDED_READY_FOR_EVIDENCE_MAP"

canonical_protocol_id: "IHARQ-PROTOCOL-V1-CUMULATIVE-THROUGH-P01-R1"

generated_timestamp: "2026-08-08T02:05:22+03:30"

canonical_format: "MARKDOWN"

document_structure_change: true

scientific_result_change: false

protocol_change: false

execution_history_change: false

claim_approval_change: true

layer0_integration_only: true

separate_current_layer0_authority: false

---

# IHARQ BenchGuard Stretch C

# Cumulative Phase Evidence, Results, and Interpretation Report Through P01

## P00 Foundation + P01 Public Data and Split Protocol / Layer 1

> **Canonical cumulative analysis + Layer 0 authority.** This Markdown is the single current cumulative Phase Evidence, Results, and Interpretation authority through P01, with the complete Layer 0 reviewed/dispositioned claim state embedded in clearly separated downstream-governance sections. Phase Analysis findings remain immutable analytical content; Layer 0 governs wording/disposition only. The former standalone reports and Layer 0 records remain provenance sources. The DOCX is a non-authoritative format-equivalent derivative.

> **Concentration rule.** P00 is preserved as inherited engineering/claim-governance context, but **P01 is the dominant analytical phase** in this report. The detailed evidence analysis, numerical reconciliation, execution forensics, A4 treatment, direct findings, limitations, candidate claims, and Layer-0 readiness assessment are therefore centered on P01.

> **Owner-directed Layer 0 integration.** `DOCUMENT_ARCHITECTURE_CHANGE = LAYER0_INTEGRATED_INTO_CUMULATIVE_PHASE_ANALYSIS`; `SEPARATE_CURRENT_LAYER0_AUTHORITY = NO`; `MEASUREMENTS_CHANGED = NO`; `PROTOCOL_CHANGED = NO`; `ANALYSIS_FINDINGS_CHANGED = NO`; `CLAIM_GOVERNANCE_ADDED = YES`. Any standalone Phase-1 Layer 0 file delivered with this package is a convenience derivative only and does not compete with this canonical authority.

> **Authority boundary.** The report consumes the frozen cumulative Protocol and accepted execution evidence. It does not modify Protocol, rerun P01, approve P01 claims, create the final P01 Evidence Map, or perform P01 Layer 10 rendering.

## Document Control

| Field | Resolved value |
| --- | --- |
| canonical report ID | IHARQ-CUMULATIVE-PHASE-EVIDENCE-RESULTS-INTERPRETATION-THROUGH-P01-R2-LAYER0-INTEGRATED |
| revision | R2-LAYER0-INTEGRATED — LAYER0_INTEGRATION_ONLY; analytical findings unchanged |
| phases represented | P00, P01 |
| dominant analysis phase | P01 |
| status | FINALIZED_FROZEN_LAYER0_EMBEDDED_READY_FOR_EVIDENCE_MAP |
| canonical Protocol | IHARQ-PROTOCOL-V1-CUMULATIVE-THROUGH-P01-R1 |
| P01 scientific freeze | P01-L1-OFFICIAL-RUN-FREEZE-R2 |
| P01 config ID | d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f |
| P01 execution bundle | IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip |
| P01 execution bundle SHA-256 | 09c3bb0442d79ddf110cf66fc4fe61fe63e94c7d8ed9f198f606639b4191f16e |
| P01 execution | ACCEPTED |
| P00 current analytical report | IHARQ-P00-PHASE-ANALYSIS-REPORT-R3-LAYER0-CORRECTED |
| P00 analysis release | P00-ANALYSIS-RELEASE-R2 |
| P00 current claim governance | P00-LAYER0-RELEASE-R2; 7 current v2 claims APPROVE_WITH_QUALIFICATIONS |
| P01 predecessor report | IHARQ-P01-EVIDENCE-RESULTS-INTERPRETATION-REPORT-R1 |
| document structure change | YES |
| scientific result / Protocol / execution history change | NO / NO / NO |
| generated timestamp | 2026-08-08T02:05:22+03:30 |

# Executive Summary

By the end of P01, IHARQ has moved from a governed engineering substrate to a governed empirical data substrate. P00 established the record, identity, hashing, validation, manifest, phase/layer-interface and evidence-governance machinery. P01 then used that machinery to freeze and materialize the first real public-EEG scientific foundation. This cumulative report preserves both phases, but its analytical emphasis is intentionally on **P01**, because P01 contains the first substantial empirical data-protocol evidence and is the phase whose candidate claims must now move to Layer 0.

The accepted P01 execution remains **ACCEPTED** and requires no additional computation. Three public EEG datasets—PhysioNetMI, BNCI2014_001 and Lee2019_MI—were activated under a frozen binary left/right motor-imagery task. The accepted denominator is **12,910 events**, conserved one-to-one into **12,910 official core windows**, with **0 / 12,910 invalid official core windows**. The dataset-scoped subject population is **172**, split subject-atomically into train/calibration/validation/test = **102 / 35 / 17 / 18**. Quality evidence comprises **489 recording/run-level summaries**, **20 soft/provider flags**, **0 hard-invalid summaries**, and an `ANNOTATE_NOT_REPAIR` policy. The persisted core product contains **172 lossless HDF5 subject shards**.

P01 also established the Layer-1 readiness foundation for **A0–A13** and preserved **A14 as absent/prohibited**. The A4 +0.0→+4.0 s proposal yielded a genuine negative feasibility result for one valid released event. Rather than pad, clip, fabricate or drop the event, the project froze **A4 R2** at +0.0→+3.5 s (560 samples) with three registered 2-second virtual views `0:320`, `120:440`, `240:560`, retaining **12,910 / 12,910** parent-event coverage. This establishes A4 substrate readiness only; **A4 effectiveness was not executed in P01**.

Execution closure is independently strong at the engineering/evidence level: **27/27 accepted P01 stages**, **16/16 P01 gates**, **50/50 regression tests**, **13,164/13,164 execution-bundle checksum targets**, and **0 unresolved P01 blockers**. Material failures and repair episodes remain visible, including Stage-14 adoption/integration issues, dependency/canonicalization repairs, A4 interface and feasibility work, Stage-07 and Stage-18 integration repairs, and the Stage-26 secret block/R54 clean export recovery. Except for the governed A4 feasibility redesign for a future control, these repairs did not alter the frozen core datasets, labels, split, preprocessing, official core window or denominator.

P00 remains important but secondary in the present document. Its current analysis release is `P00-ANALYSIS-RELEASE-R2`; its claim-facing report is the R3 Layer-0-corrected successor. The historical displayed P00-F-002 denominator was corrected from 92 to **102** without changing the analysis release. P00's seven current claim versions (`P00-CLM-001/v2`…`/v2`) are already `APPROVE_WITH_QUALIFICATIONS` under `P00-LAYER0-RELEASE-R2`, whereas **at the original Phase Analysis freeze, P01 claims remained unapproved candidates/deferred/not-supported statements pending Phase 1 Layer 0**. The embedded Layer 0 sections in this R2 successor now preserve that pre-review history and add the finalized reviewed/dispositioned state without changing the findings.

The original pre-Layer-0 analytical conclusion was: **P00 engineering foundation preserved; P01 data-protocol/evidence foundation accepted; P01 candidate claims and evidence were sufficiently complete, bounded and traceable to proceed to Layer 0.** This R2 successor preserves that analytical conclusion historically and records that Layer 0 has now been applied and finalized. The evidence ceiling remains data provenance, integrity, validation, readiness and execution reproducibility—not decoder superiority, clinical effectiveness, deployment safety, A4 benefit or low-calibration benefit.

# PART I — PROJECT ANALYSIS FRAMEWORK

## 1. Scope and Purpose

This cumulative authority answers what the project demonstrably established through P01 while preserving phase ownership. P00 contributes governed engineering-foundation evidence and already-governed claim history. P01 contributes the dominant empirical data-protocol analysis: source identity, task/label mapping, subject-grouped split, preprocessing, event/window denominators, quality/leakage validation, external persistence, ablation foundations, execution repairs, and downstream technical readiness. The cumulative report does not collapse these evidence classes into one undifferentiated “project success” claim.

## 2. Authority Stack

| Authority | Owner role | Use in cumulative analysis |
| --- | --- | --- |
| Governance V6.1 | workflow/document process | single-track sequence, evidence sufficiency, reuse-first repair, Layer 0/Evidence Map/Layer 10 boundaries |
| Architecture | phase/layer/system/A-ID identity | P00 engineering foundation; P01 empirical anchor; later phase ownership |
| Registry | records/status/interfaces/lineage | canonical IDs, record families, lifecycle, provenance |
| Execution & Evidence Plan | required evidence and completion | gates, negative evidence, handoffs, evidence sufficiency |
| Finalized cumulative Protocol v1.0 | frozen execution/analysis contract | P01 ten analyses, denominators, A0–A13, A4, evidence ceilings |
| Playbook | operating/repair procedure | failed-attempt → repair → rerun interpretation |
| Method Selection | selected methods/data/platforms | scientific/engineering rationale |
| Nuts-and-Bolts | technical implementation behavior | validators, preprocessing/windowing, failure behavior |
| Build Book | intended executable realization | pre-run intent vs accepted execution |
| Execution evidence | what actually happened | primary P00/P01 measured evidence |
| Phase Analysis | findings/interpretation/candidate claims | this cumulative authority; cannot approve P01 claims |
| Layer 0 | claim governance | P00 already governed; P01 is next step |

## 3. Evidence and Interpretation Hierarchy

The hierarchy is **MEASURED RESULT → SUPPORTED INTERPRETATION → CANDIDATE CLAIM → MECHANISM HYPOTHESIS**. P00 current qualified claims are explicitly identified as later Layer-0 dispositions; they are not retroactively relabeled as original report findings. P01 candidate claims remain pending Layer 0. Readiness evidence is never promoted to effectiveness evidence.

## 4. Analysis Boundaries

Through P01 the project may support bounded statements about engineering conformance, public-data provenance, split integrity, preprocessing/window materialization, quality/leakage checks, artifact integrity, A0–A13 foundation readiness, A4 substrate readiness, execution closure and downstream technical readiness. It does not yet support decoder superiority, clinical/deployment effectiveness, A4 performance benefit, low-calibration benefit, uncertainty/calibration benefit, policy benefit, robustness benefit or embodiment effectiveness.

## 5. Cumulative Project Status

| Surface | Current status | Interpretation |
| --- | --- | --- |
| P00 engineering analysis | ANALYSIS_RELEASE_R2 preserved | non-empirical engineering/foundation evidence |
| P00 claim governance | 7 current v2 claims APPROVE_WITH_QUALIFICATIONS | already dispositioned; no new P00 Layer 0 action required |
| P00 Evidence Map / basic Layer 10 | accepted/read-only historical package exists | preserved continuity; not a substitute for P01 products |
| P01 execution | ACCEPTED | primary empirical data-protocol execution complete |
| Protocol through P01 | FROZEN | immutable analysis contract |
| P01 analysis | FINALIZED | dominant content preserved in this cumulative authority |
| P01 Layer 0 | READY, NOT YET PERFORMED | next governed step |
| Evidence Map / Layer 10 for P01 | SOURCE INPUTS READY | await P01 Layer 0 then Evidence Map |

# PART II — PHASE 00 — INHERITED ENGINEERING AND CLAIM-GOVERNANCE FOUNDATION

## 6. P00 Purpose and Evidence Ceiling

P00 established the administrative/engineering substrate: schemas, typed IDs, canonical serialization and hashing, configuration/record inventories, validators and fixtures, manifests, lineage/lifecycle, phase/layer interfaces, A0–A13 identities, no-A14 protection, reproduction and downstream-contract machinery. Its evidence remains **Mode B engineering/retrospective foundation evidence** with ceiling `ENGINEERING_FOUNDATION_CONFORMANCE`; it contains no empirical decoder or effectiveness result.

## 7. P00 Execution and Analytical State

| Surface | Current value |
| --- | --- |
| Execution release | P00-EXECUTION-RELEASE-R2 |
| Analysis release | P00-ANALYSIS-RELEASE-R2 |
| Current claim-facing report | IHARQ-P00-PHASE-ANALYSIS-REPORT-R3-LAYER0-CORRECTED |
| Registered cells | 19/19 PASS |
| Frozen analysis-release tests | 102/102 PASS |
| Valid/integrated bundles | 19/19 accepted |
| Malformed categories | 178/178 rejected |
| Schemas / configs / record families | 85 / 35 / 79 |
| Layer foundations | 11/11 |
| Phase-contract families | 16 |
| P00 empirical ablations | none; A0–A13 readiness-only; A14 rejected |

The P00 R3 report successor corrected one report-owned display defect: `P00-F-002` had shown denominator 92 although the unchanged machine register and current analysis release equal **102**. The correction did not modify any measurement, execution inclusion, finding identity or analysis release. Later P00 Layer 0/Evidence Map/Layer 10 auditing preserved that noninterference.

## 8. P00 Direct Findings — Preserved

| Finding | Evidence class | Denominator | Measured result / bounded meaning |
| --- | --- | --- | --- |
| P00-F-001 | REGISTERED_ENGINEERING_EXECUTION | 19 | 19/19 registered P00 engineering cells passed with terminal PASS |
| P00-F-002 | DETERMINISTIC_TESTING | 102 | 102/102 deterministic tests passed |
| P00-F-003 | POSITIVE_FIXTURE_VALIDATION | 19 | 19/19 valid or integrated bundles accepted; false rejections 0 |
| P00-F-004 | NEGATIVE_VALIDATION | 178 | 178/178 intentionally malformed categories rejected; false acceptances 0 |
| P00-F-005 | ARTIFACT_CLOSURE | 85 schemas; 35 configs; 79 record families | all registered foundation inventories present and validated |
| P00-F-006 | INTEGRATION | 11 layers | 11/11 Layer 0–10 foundation interfaces passed registered P00 integration scope |
| P00-F-007 | FUTURE_CONTRACT_READINESS | 16 phase-contract families | P00 implemented; P01–P15 reusable contract surfaces prepared |
| P00-F-008 | REPRODUCIBILITY | 8 bounded reproduction steps | 8/8 bounded reproduction steps passed under exact local snapshot |
| P00-F-009 | EVALUATION_READINESS | 14 A-identities | A0–A13 readiness hooks present; A14 rejected |

## 9. P00 Claim-Governance Continuity

P00 candidate statements were subsequently governed. The current qualified claim versions are `v2` under `P00-LAYER0-RELEASE-R2`; the accepted P00 Evidence Map release is `P00-EVIDENCE-MAP-RELEASE-R2` and the basic read-only package is `P00-BASIC-LAYER10-PACKAGE-R2`. This cumulative report preserves those dispositions but does not redo them.

| Current claim | Decision | Ceiling | Strongest lawful wording |
| --- | --- | --- | --- |
| P00-CLM-001/v2 | APPROVE_WITH_QUALIFICATIONS | ENGINEERING_FOUNDATION_CONFORMANCE | Under the exact registered local snapshot and verified Python 3.13.5 environment, all 19 registered Phase 0 engineering/foundation conformance cells passed; this is non-empirical Mode B evidence and does not establish scientific effectiveness or Phase 0 closure. |
| P00-CLM-002/v2 | APPROVE_WITH_QUALIFICATIONS | ENGINEERING_FOUNDATION_CONFORMANCE | In the frozen local Python 3.13.5 environment, the complete registered deterministic suite passed 102 of 102 tests; cross-version portability is not established. |
| P00-CLM-003/v2 | APPROVE_WITH_QUALIFICATIONS | VALIDATION_EVIDENCE | Within the registered non-empirical fixture inventory, all 19 valid or integrated bundles were accepted and all 178 intentionally malformed categories were rejected as expected, with zero false valid rejections and zero false malformed acceptances. |
| P00-CLM-004/v2 | APPROVE_WITH_QUALIFICATIONS | ARTIFACT_CLOSURE | The frozen Phase 0 package contains and validates the registered foundation inventories of 85 schemas, 35 configuration profiles, and 79 record-family profiles; inventory closure does not establish later-phase scientific effectiveness. |
| P00-CLM-005/v2 | APPROVE_WITH_QUALIFICATIONS | FOUNDATION_INTEGRATION | All eleven Layer 0–10 foundation interfaces passed the registered Phase 0 integration scope; no later-phase scientific execution or effectiveness result is claimed. |
| P00-CLM-006/v2 | APPROVE_WITH_QUALIFICATIONS | CONTRACT_READINESS | The P00 implementation foundation is complete within its registered local scope, and P01–P15 reusable contract surfaces are ready for later governed annex creation and execution; future empirical outputs have not been produced. |
| P00-CLM-007/v2 | APPROVE_WITH_QUALIFICATIONS | LOCAL_REPRODUCIBILITY | The package reproduced from a clean isolated copy under the exact verified Python 3.13.5 and 22-distribution local dependency snapshot; portable cross-version reproducibility is not established. |

## 10. P00 Limitations and Negative-Evidence Continuity

P00 remains bounded by exact-environment/local-snapshot reproducibility, incomplete cross-version portability, Mode-B/non-empirical scope and historical workflow limitations. Its malformed-fixture results, timeout/repair history, unavailable Python-version checks and deferred historical gates remain negative/diagnostic evidence rather than being erased. These P00 constraints are inherited only where relevant; they do not replace the actual P01 environment or P01 empirical evidence.

## 11. P00 Downstream State and P01 Inheritance

The key P00 contribution to P01 was not a scientific result but a stable contract. P01 reused canonical identity/hashing, record schemas, lineage, validation and A-ID semantics rather than regenerating them. That continuity is scientifically valuable because later P01 records can be linked to upstream governance without changing the rules every phase. P00 therefore remains present in this cumulative report as the foundation and historical claim-governance layer, while P01 supplies the dominant current empirical analysis.

# PART III — PHASE 01 — DOMINANT EMPIRICAL DATA-PROTOCOL ANALYSIS

> The following P01 section preserves the substantive content of the finalized P01 R1 report, now governed inside the single cumulative report. No P01 finding, denominator, evidence ceiling, candidate-claim status, A4 boundary or execution result is strengthened by consolidation.

## P01.1. Phase Identity and Purpose

P01 is the **Public Data and Split Protocol** phase and Layer 1 is its primary implementation owner. Architecture characterizes Phase 1 as the empirical anchor gate: public EEG must be transformed into standardized, split-safe records before downstream decoders, calibration, selective prediction, policy learning, stress evaluation, or embodiment work can be interpreted fairly. The key bottleneck is not merely data availability; it is *identity and comparability*. Without frozen source versions, task mappings, subject-group splits, event timing, preprocessing, window profiles, and lineage, a later performance number cannot be traced to a stable experimental substrate.

Layer 1 therefore owns the public-data/testbed foundation and emits canonical DatasetRecord, LabelMapRecord, SplitRecord, PreprocessingRecord, WindowRecord, quality/validation evidence, dataset/protocol cards, the Layer-1 ablation-readiness manifest, and downstream handoffs. Decoder training and effectiveness are deliberately downstream responsibilities.

## P01.2. Governing Authority Stack

| Authority | What it controls for this report | How used |
| --- | --- | --- |
| Governance V6.1 | Current workflow, source hierarchy, evidence sufficiency, repair loop, post-execution Protocol/Report sequence | Controls report timing, reuse-first policy, negative-result preservation and downstream boundaries |
| Master Architecture | P01/L1 purpose, phase/layer boundaries, A0–A13 identities, P02 dependence | Defines what P01 is allowed to claim as its own work |
| Canonical Registry R44 | Record families, fields, lifecycle/identity/lineage semantics | Used to interpret Dataset/Label/Split/Preprocessing/Window/Validation records |
| Execution & Evidence Plan R41 | Required P01 outputs, evidence/gates/completion conditions | Used to assess evidence sufficiency and closure |
| Protocol v0.1 / finalized Protocol v1.0 | Fairness, splits/leakage, denominators, ablations, exclusions, exact P01 analysis contract | Finalized v1.0 is immutable analysis authority |
| Phase Execution Playbook R41 | Operational order, failure/repair/handoff procedure | Used to interpret repair/reentry chronology |
| Method Selection R2 | Selected datasets/method/platform strategy | Used for rationale, not as proof of execution |
| Nuts-and-Bolts R2 | Technical algorithms/validators/failure behavior | Used to explain implementation behavior |
| Implementation Build Book R10 / P01 Annex R4 | Pre-run executable intent | Compared explicitly with actual execution |
| Accepted P01 execution bundle | Actual measured/executed evidence | Primary source for numerical results |
| This Report | Results synthesis, bounded interpretation, candidate claims and downstream handoffs | Does not change Protocol or approve claims |

## P01.3. Phase 0 Prior State and Reused Foundations

P00 created the engineering substrate that made a record-first P01 possible: canonical JSON schemas, typed identities, JCS/SHA-256 hashing, lineage/lifecycle rules, validation semantics, fixtures, manifests, phase/layer interfaces, the A0–A13 identity set, the no-A14 lock, and downstream document/reproducibility contracts. The direct P00 Protocol history remains Mode-B engineering/retrospective evidence with the ceiling `ENGINEERING_FOUNDATION_CONFORMANCE`; P01 does not retroactively convert that history into empirical scientific evidence.

Reuse was preferable to rebuilding because changing stable upstream identity/hashing/schema infrastructure merely for a new phase would create unnecessary invalidation and risk making P01 records incomparable with the rest of the project. P01 therefore *instantiated and extended* P00's governed record machinery with real public-data records rather than replacing it.

| Inherited surface | P00 state | P01 disposition | Classification |
| --- | --- | --- | --- |
| Canonical record schemas/IDs/hashes | Implemented and validated | Used for real Dataset/Label/Split/Preprocessing/Window records | REUSED_AND_EXTENDED |
| Lineage/lifecycle/manifest rules | Implemented and validated | Applied to P01 empirical records and external pointers | REUSED_AND_EXTENDED |
| A0–A13 identities | Readiness-only identities | Layer-1 matching/readiness rows produced for every A0–A13 | REUSED_AND_EXTENDED |
| A14 prohibition | Rejected/absent | Absence validator PASS; no selector/run/result/claim | REUSED_UNCHANGED |
| Validation/gate framework | Engineering foundation | P01-specific deterministic gates G01–G16 and execution tests | REUSED_AND_EXTENDED |
| Historical Mode-B P00 workflow classification | Historical evidence metadata | Preserved as historical only; current workflow follows Governance V6.1 | SUPERSEDED_WITH_HISTORY_PRESERVED |
| Public-data empirical records | Not produced in P00 | Materialized in P01 | NEW_IN_P01 |

## P01.4. Phase 1 Responsibilities

P01 responsibilities can be understood as a chain of controlled commitments. First, source identity must be known. Second, the supervised task must be explicit. Third, all subject/session/run/event identities must remain traceable through preprocessing. Fourth, split membership must be frozen before any downstream model fitting. Fifth, one official window representation must be materialized without denominator drift. Sixth, quality/leakage checks must determine whether the data substrate is admissible. Seventh, large tensors must be persisted with compact manifests and immutable pointers. Finally, all official A0–A13 future comparisons must have matching keys/readiness surfaces so later phases do not improvise their denominators.

## P01.5. Pre-Run Implementation Contract

The Build Book froze the scientific core before execution as follows:

| Surface | Pre-run frozen intent |
| --- | --- |
| Active datasets | PhysioNetMI; BNCI2014_001; Lee2019_MI |
| Task | binary left_hand vs right_hand; rest/feet/tongue/motor execution/technical/unlabeled online-test events excluded per source |
| Split | SUBJECT; roles train/calibration/validation/test; 0.6/0.2/0.1/0.1; seed 20260804; SHA256-ranked dataset-local subject groups |
| Low-calibration budgets | 1, 2, 4, 8, 16, 32 source events per normalized class from calibration role; nested SHA256-ranked prefixes |
| Preprocessing | EEG-only; event capture; demean; average rereference; joint polyphase event/signal resample to 160 Hz; Kaiser β=5; reflect pad; 8–32 Hz 4th-order Butterworth SOS zero-phase with odd pad/padlen 27; float32 |
| Core window | MI cue +0.5…+3.5 s; 480 samples; one per admitted event; reject OOB; no clipping |
| Quality | ANNOTATE_NOT_REPAIR; hard invalid only for nonfinite/rank/duration/lineage failures; soft warnings retained |
| Environment intent | Kaggle CPU; Python >=3.11,<3.12; exact package pins; legacy 60 GiB free-disk preflight |
| Persistence | large lossless HDF5 tensors external; compact governed metadata/manifests in project state |
| Ablation responsibility | prepare Layer-1 matching/readiness foundations A0–A13; no A14 |
| Downstream | P02 consumes exact Window/Split/Label/Preprocessing identities; no silent reinterpretation |

## P01.6. Executed Notebook and Environment

The accepted notebook lineage is the 00–26 consolidated Kaggle execution with final runtime metadata `P01-L1-KAGGLE-NOTEBOOK-R49-MATCHED-A4-R2` plus same-session integration/security repairs. The accepted environment is not identical to the original Build Book image intent. It used **Python 3.12.13**, Linux x86_64/glibc 2.35, 4 CPUs, 33,659,379,712 bytes RAM, and 20,336,979,968 bytes initial free disk (~18.94 GiB). The exact scientific packages match their required pins; `pin_mismatches` and `required_import_failures` are empty.

The environment amendment is execution-compatibility evidence, not a scientific refreeze. The scientific identity remains `P01-L1-OFFICIAL-RUN-FREEZE-R2` and the config remains `d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f`.

| Package | Actual version |
| --- | --- |
| moabb | 1.5.0 |
| mne | 1.12.1 |
| numpy | 2.2.6 |
| scipy | 1.15.3 |
| pandas | 2.3.1 |
| scikit-learn | 1.7.1 |
| h5py | 3.14.0 |
| pooch | 1.8.2 |
| pyyaml | 6.0.2 |
| pydantic | 2.11.7 |
| jsonschema | 4.25.0 |
| nbformat | 5.10.4 |

## P01.7. Intended-vs-Actual Reconciliation

| Surface | Build Book / pre-run intent | Actual accepted execution | Difference / reason | Scientific consequence | Final status |
| --- | --- | --- | --- | --- | --- |
| Datasets | Three selected sources | Same three sources | None | None | MATCH |
| Labels/exclusions | Frozen binary mapping | Same validated LabelMapRecords | None | None | MATCH |
| Split | Subject-grouped 60/20/10/10 target | Same deterministic allocation with expected group counts | None | None | MATCH |
| Core preprocessing | Frozen R2 sequence | Same PreprocessingRecord | None | None | MATCH |
| Core window | +0.5…+3.5 s / 480 | Same; 12,910/12,910 valid | None | None | MATCH |
| Quality | ANNOTATE_NOT_REPAIR | 489 summaries; 20 soft flags; 0 hard invalid | Observed results only | None | PASS |
| Python | 3.11 intended | 3.12.13 actual | Kaggle runtime compatibility | No scientific values changed | DOCUMENTED_AMENDMENT |
| Disk policy | 60 GiB fixed preflight | adaptive policy; 6.0 GiB effective requirement; 18.94 GiB observed free | Kaggle resource reality | No scientific values changed | DOCUMENTED_AMENDMENT |
| Core persistence | materialize/persist official core | Verified existing exact scientific artifact adopted; no recompute/reupload | Reuse-first lawful adoption | Core bytes/manifest unchanged | PASS |
| A4 | Original proposed +0.0…+4.0 s alternative | R2 matched +0.0…+3.5 s; three registered 2 s views | One valid event cannot supply +4.0 s without fabrication/drop | Changes future A4 alternative profile only; core unchanged | R2 FROZEN FOR FUTURE USE |
| Stage execution | 00–26 expected | 00–26 final identities PASS | Material integration failures repaired | No accepted-core scientific consequence except A4 future-profile correction | PASS |
| Packaging | secret-free final export expected | Initial Stage 26 blocked; R54 clean repack | Credential serialization defect | None | PASS |

## P01.8. Analysis 1 — Source Inventory, Provenance, License, and Checksum Reconciliation

**Analysis contract:** `P01-AC-001-SOURCE-INVENTORY` — evidence ceiling: data provenance/reproducibility only.

| Dataset | Frozen source/revision | Subjects | Source files | Source events in record | Accepted binary events | Source Hz | DatasetRecord | Aggregate SHA-256 | License |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PhysioNetMI | 1.0.0 | 109 | 327 | 9509 | 4918 | 128.0, 160.0 | IHARQ-DATASETRECORD-20260806-66309cda68771bef | 28cd2062983b6236f9a0e7fdee91fc9d8d5aad8eee3ef561cff5828ae89bf2ba | Open Data Commons Attribution License 1.0 (ODC-By-1.0) |
| BNCI2014_001 | 001-2014 provider file set A01T/A01E through A09T/A09E | 9 | 18 | 5184 | 2592 | 250.0 | IHARQ-DATASETRECORD-20260806-42c424800627b6ee | 04a5390f8f36eaadbc0c480ec9377ce1b99caf0b7ab53bad9fda12347995bc49 | Creative Commons Attribution-NoDerivatives 4.0 International (CC BY-ND 4.0) |
| Lee2019_MI | GigaDB dataset DOI 10.5524/100542; MOABB 1.5.0 Lee2019_MI wrapper; labeled offline/train MI runs only | 54 | 108 | 5400 | 5400 | 1000.0 | IHARQ-DATASETRECORD-20260806-adb91f25a65e588e | 3a07b2f302da949efd418a0712d5a9427df34dcb8b027ca553fae8e67a849f78 | GNU General Public License v3.0 as documented by the maintained MOABB source card; source terms retained in DatasetCard |

Across the three DatasetRecords there are **453 source files** and **20,093 source events recorded at source-inventory level**. The official binary task admits **12,910** events. The difference (**7,183**) is not treated as a pool of “negative labels”: it contains source events/classes outside the frozen binary task and technical/provider events according to each LabelMapRecord. This distinction is essential because treating excluded classes as negatives would change the task definition after source intake.

The three sources play complementary roles: PhysioNetMI provides the largest subject base and requires run-context semantics plus the subject-88 rate exception; BNCI provides a standard four-class MI source from which only left/right trials are admitted; Lee provides a high-rate left/right companion whose labeled offline/train branch is used after deterministic event-aware resampling. Exact aggregate hashes and source-specific licenses make the resulting DatasetRecords reproducible without pretending that all raw bytes can be freely redistributed.

**Measured result:** all three DatasetRecords are `VALIDATED`; no screened-out dataset was activated.

**Supported interpretation:** P01 established a traceable, license-aware source portfolio.

**Not supported:** any conclusion about decoder performance or clinical representativeness.

## P01.9. Analysis 2 — Subject-Group Split Allocation and Disjointness

**Analysis contract:** `P01-AC-002-SPLIT` — interpretation ceiling: split/leakage contract correctness.

| Dataset | Subjects | Train subj | Cal subj | Val subj | Test subj | Train windows | Cal windows | Val windows | Test windows |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PhysioNetMI | 109 | 65 | 22 | 11 | 11 | 2949 | 979 | 495 | 495 |
| BNCI2014_001 | 9 | 5 | 2 | 1 | 1 | 1440 | 576 | 288 | 288 |
| Lee2019_MI | 54 | 32 | 11 | 5 | 6 | 3200 | 1100 | 500 | 600 |

| Role | Subject groups | Subject % | Core windows | Window % |
| --- | --- | --- | --- | --- |
| train | 102 | 59.30% | 7589 | 58.78% |
| calibration | 35 | 20.35% | 2655 | 20.57% |
| validation | 17 | 9.88% | 1283 | 9.94% |
| test | 18 | 10.47% | 1383 | 10.71% |

The split unit is the dataset-scoped **subject**, not the window. All sessions, runs, accepted events, and windows of a subject inherit the same role. The deterministic allocation algorithm is `SHA256_RANK_SUBJECT_GROUPS_WITH_LARGEST_REMAINDER_AND_MINIMUM_ONE_GROUP_PER_ROLE` under seed **20260804**. This produces 172 disjoint subject groups and preserves all four roles in every dataset.

Subject grouping matters in EEG because repeated observations from the same person can share stable person-specific structure. A window-level random split could allow those structures to appear in both training and held-out data even if no literal window is duplicated. P01 avoids that failure mode by splitting the subject group before downstream model fitting.

**Measured result:** disjointness `PASS`; no group intersections are reported. **Supported interpretation:** the frozen split is internally disjoint under its declared subject-group contract. **Not supported:** an absolute claim that no conceivable leakage could ever exist outside the implemented checks.

## P01.10. Analysis 3 — Accepted Event/Window Denominator Conservation

**Analysis contract:** `P01-AC-003-DENOMINATOR` — interpretation ceiling: data-materialization closure.

| Dataset | Accepted parent events | Core windows | Invalid core windows | Conservation |
| --- | --- | --- | --- | --- |
| PhysioNetMI | 4918 | 4918 | 0 | 100.00% |
| BNCI2014_001 | 2592 | 2592 | 0 | 100.00% |
| Lee2019_MI | 5400 | 5400 | 0 | 100.00% |
| TOTAL | 12910 | 12910 | 0 | 100.00% |

| Normalized label | Accepted core windows | Share |
| --- | --- | --- |
| left_hand | 6476 | 50.16% |
| right_hand | 6434 | 49.84% |

The denominator chain is:

`admitted source event → frozen split membership → returned jointly-resampled event sample → +80 integer-sample offset → 480-sample core tensor → persisted window identity`.

Every official WindowRecord is validated, all use duration 480 samples and start offset 80 samples, and 12,910 unique parent-event identities are represented. The small global left/right difference (6,476 versus 6,434) comes from the admitted PhysioNet event inventory; BNCI and Lee are exactly balanced. No balancing rule was applied post hoc to alter the denominator.

**Supported interpretation:** the core extraction process did not silently lose accepted events. **Not supported:** a claim that 12,910 events are sufficient to guarantee any later model effect or precision target.

## P01.11. Analysis 4 — Quality / Validation Closure

**Analysis contract:** `P01-AC-004-QUALITY` — interpretation ceiling: quality annotation/data validity.

| Dataset | Quality summaries | Soft/provider flags | Hard-invalid summaries |
| --- | --- | --- | --- |
| PhysioNetMI | 327 | 8 | 0 |
| BNCI2014_001 | 108 | 0 | 0 |
| Lee2019_MI | 54 | 12 | 0 |
| TOTAL | 489 | 20 | 0 |

Quality operates on a different unit from the source-file inventory. The execution contains **453 source files** but **489 quality summaries** because quality is summarized at recording/run-level units, not simply one summary per downloaded file. This is an intentional denominator difference, not an inconsistency.

The governing policy is `ANNOTATE_NOT_REPAIR`. Hard-invalid conditions include nonfinite values, wrong tensor rank, insufficient duration, and missing source-event lineage. Soft annotations include flat-channel proxies, amplitude exceedances, repeated-identical-sample proxies, and source-declared bad trial/channel metadata. P01 recorded **20** soft/provider flags (8 PhysioNetMI, 12 Lee, 0 BNCI), but **0 hard-invalid summaries** and **0/12,910 invalid official windows**.

A soft flag is not equivalent to a corrected defect and is not silently used to remove data. The defensible conclusion is that the frozen hard-validity criteria closed without invalid official windows while diagnostic annotations remain visible.

## P01.12. Analysis 5 — Leakage and Visibility

**Analysis contract:** `P01-AC-005-LEAKAGE` — interpretation ceiling: absence of detected contract leakage under implemented checks.

| Implemented check | Result |
| --- | --- |
| GROUP_DISJOINTNESS | PASS |
| DUPLICATE_SAMPLE | PASS |
| OVERLAP_GROUP | PASS |
| FIT_SCOPE | PASS |
| BUDGET_TEST_CONTAMINATION | PASS |
| Reported issues | 0 |

The leakage audit combines subject-role disjointness with event/window overlap, fit-scope, and budget/test-contamination controls. The low-calibration population is drawn from the calibration role; test visibility is false. The official preprocessing profile itself requires no fitted statistics, but fit-scope infrastructure is still audited because downstream or alternative profiles must not learn from held-out roles.

**Measured result:** the leakage report is `PASS` with no issues. **Supported interpretation:** no contract leakage was detected under the implemented checks. The report deliberately avoids the stronger, untestable statement “leakage is impossible.”

## P01.13. Analysis 6 — External Artifact Persistence and Integrity

**Analysis contract:** `P01-AC-006-EXTERNAL` — interpretation ceiling: retrieval/storage/integrity reproducibility.

| Artifact | Provider/handle | Provider rev | Logical rev | Shards | Primary count | Actual HDF5 bytes | Manifest SHA-256 | Local-copy state |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Official core | csthv999z/iharq-p01-l1-derived-windows-d03f0a7c869d-20260806222242-68a91473 | 2 | 1 | 172 | 12910 | 1166652764 | dc21f418e9a1add62adb346f627d5d729735a5f1ecaa1d771f6fa5cfede627e1 | SHARDS_DELETED_AFTER_VERIFIED_KAGGLE_BLOB_UPLOAD |
| A4 R2 | csthv999z/iharq-p01-l1-a4-d03f0a7c-9a7c6108 | 1 | 2 | 172 | 12910 | 1357362334 | 29124d59907610b1545e0a2b5d1811a4d4a2bf1df64cad49aa880f4721c47305 | A4_SHARDS_DELETED_AFTER_VERIFIED_KAGGLE_BLOB_UPLOAD |

P01 uses **dual persistence**: compact canonical records, indices, hashes, and pointers remain inside the execution/project state; large numerical arrays live in private, immutable/versioned Kaggle Datasets. The official core stores **1,356,625,920 logical float32 bytes (1.263 GiB)** and **1,166,652,764 actual HDF5 bytes (1.087 GiB)**. A4 stores **1,582,730,240 logical bytes (1.474 GiB)** and **1,357,362,334 actual HDF5 bytes (1.264 GiB)**.

The core pointer explicitly distinguishes **provider version 2** from **logical immutable revision 1**: provider version 1 was a historical short-title shell, while version 2 is the verified scientific artifact. This distinction is version semantics, not a conflict. After exact remote-manifest verification, local shard copies were deleted according to policy; reproducibility is preserved through the external Dataset, manifest, indexes, reader, hashes, and record lineage rather than through redundant local gigabyte copies.

## P01.14. Analysis 7 — A0–A13 Foundation Readiness and A14 Absence

**Analysis contract:** `P01-AC-007-ABLATION-READINESS` — interpretation ceiling: foundation readiness only.

| ID | Official identity | P01 readiness | Executed in P01? | Downstream | P01 result |
| --- | --- | --- | --- | --- | --- |
| A0 | Raw Decoder / Accept-All Raw Decoder Reference | FOUNDATION_READY | No | P02-P15 | Layer-1 matching foundation only |
| A1 | Calibrated Decoder / Calibration Visibility | FOUNDATION_READY | No | P02-P15 | Layer-1 matching foundation only |
| A2 | Simple Registered Threshold / Confidence-Threshold Baseline | FOUNDATION_READY | No | P02-P15 | Layer-1 matching foundation only |
| A3 | Uncertainty and Selective Prediction | FOUNDATION_READY | No | P02-P15 | Layer-1 matching foundation only |
| A4 | Longer-Window, Multi-Window Voting/Averaging and Ordinary Ensemble Controls | FOUNDATION_READY | No | P02-P15 | A4 R2 data substrate materialized; confirmatory effectiveness deferred |
| A5 | IHARQ-lite / Rule-Based Evidence Verification | FOUNDATION_READY | No | P02-P15 | Layer-1 matching foundation only |
| A6 | IHARQ + Evidence-Quality Estimator | FOUNDATION_READY | No | P02-P15 | Layer-1 matching foundation only |
| A7 | IHARQ + RegimeRisk Temporal Trust | FOUNDATION_READY | No | P02-P15 | Layer-1 matching foundation only |
| A8 | Learning-to-defer / Deferral Comparison | FOUNDATION_READY | No | P02-P15 | Layer-1 matching foundation only |
| A9 | Supervised Adaptive-IHARQ / Adaptive Readiness Policy | FOUNDATION_READY | No | P02-P15 | Layer-1 matching foundation only |
| A10 | Contextual Bandit / Simulation-Bounded Immediate-Reward Adaptation | FOUNDATION_READY | No | P02-P15 | Layer-1 matching foundation only |
| A11 | Reinforcement-Learning Policy / Simulation-Bounded Sequential Policy Learning | FOUNDATION_READY | No | P02-P15 | Layer-1 matching foundation only |
| A12 | StressForge Stress Tests / Controlled Stress Robustness | FOUNDATION_READY | No | P02-P15 | Layer-1 matching foundation only |
| A13 | Layer 9 Simulation-Only Embodiment Demo | FOUNDATION_READY | No | P02-P15 | Layer-1 matching foundation only |

Every official identity A0–A13 has a `FOUNDATION_READY` Layer-1 row, and every row has `executed_in_p01=false`. That is the correct Layer-1 result: P01 ensures downstream comparisons can reference matched dataset/split/preprocessing/label/window/config keys; it does not run the decoder, calibration, selective-prediction, IHARQ, policy, stress, or embodiment experiments themselves.

### A14 — rejected / absent
The explicit absence audit is `PASS`: `a14_present=false`, `selector_present=false`, `run_present=false`, `result_present=false`, and `claim_present=false`. Local A12.x identities, where they exist elsewhere in the project, are not renamed into A14.

## P01.15. Analysis 8 — A4 R2 Feasibility and Protocol Synchronization

**Analysis contract:** `P01-AC-008-A4` — interpretation ceiling: future A4 substrate readiness, **not A4 effectiveness**.

| Profile/member | Timing | Samples/slice | Physical storage |
| --- | --- | --- | --- |
| A4_LONG_MATCHED_3P5S_R2 | +0.00 → +3.50 s | 560 samples | Stored once per parent event |
| A4_MULTI_3X2S_M1_R2 | +0.00 → +2.00 s | 0:320 | Virtual slice |
| A4_MULTI_3X2S_M2_R2 | +0.75 → +2.75 s | 120:440 | Virtual slice |
| A4_MULTI_3X2S_M3_R2 | +1.50 → +3.50 s | 240:560 | Virtual slice |

The original A4 R1 concept requested a +0.0 to +4.0 second, 640-sample longer tensor. Full-denominator feasibility checking found one valid core parent, `PhysioNetMI:104:0:8:event:24`, whose resampled cue sample is 16,400 and whose source ends at 16,960. The official core (+0.5…+3.5 s) ends exactly at 16,960 and is valid; a +4.0 s A4 tensor would end at 17,040 and therefore require **80 nonexistent samples (0.5 s)**. Exactly one of 12,910 parents fails the 4.0-second request; zero fail +0.0…+3.5 seconds.

The alternatives were scientifically consequential: padding would fabricate data, clipping would make duration unequal, and dropping the event would change the matched denominator. The R2 choice preserves every parent and the same +3.5 s endpoint as core while adding 0.5 s of earlier observation. The three 2-second members are registered views into the one stored 560-sample tensor, avoiding duplicate overlapping bytes.

**Measured result:** 12,910 matched stored tensors, 38,730 virtual-member records, 51,640 total A4 WindowRecords, 12,910 groups, 172 shards, 0 invalid, complete core-parent match. **Protocol state now:** the finalized Protocol has synchronized the R2 identity for future governed use.

**A4 DATA FOUNDATION: READY. A4 EFFECTIVENESS IN P01: NOT EXECUTED.** The R2 origin is retrospective feasibility repair, not prospective P01 evidence of superiority.

## P01.16. Analysis 9 — Environment and Reproducibility Amendment Reconciliation

**Analysis contract:** `P01-AC-009-ENVIRONMENT` — interpretation ceiling: execution reproducibility.

| Surface | Pre-run intent | Actual accepted execution | Classification | Scientific effect |
| --- | --- | --- | --- | --- |
| Python | 3.11 (<3.12) | 3.12.13 | EXECUTION_COMPATIBILITY_CHANGE | None documented |
| Packages | Exact listed pins | All listed pins matched; no import failures | EXECUTION_COMPATIBILITY_CHANGE | None |
| Disk | minimum free 60 GiB | adaptive effective minimum 6.0 GiB; observed free 18.94 GiB | RESOURCE_POLICY_CHANGE | None |
| Source removal | Verified cache removal allowed under pressure | automatic source removal disabled in accepted adaptive policy | RESOURCE_POLICY_CHANGE | None |
| Execution isolation | Kaggle notebook | persistent child worker with heartbeat/timeouts | IMPLEMENTATION/EXECUTION RELIABILITY | None |

The accepted resource amendment is `P01-L1-KAGGLE-ADAPTIVE-DISK-R1`. Its adaptive calculation measured fixed footprint **549,855,386 bytes**, calculated requirement **3,908,544,705 bytes**, and enforced an effective minimum of **6,442,450,944 bytes (6.0 GiB)**. Observed free disk at preflight was **18.94 GiB**, so the accepted run had a positive resource margin without pretending the obsolete 60 GiB threshold had been met.

Reproducibility consequence: a faithful reproduction should use the captured Python 3.12.13/package/runtime environment or explicitly validate a successor environment. Scientific consequence: no dataset, label map, split, core preprocessing, core window, denominator, or metric changed because of these amendments.

## P01.17. Analysis 10 — Gate Closure and Failed/Superseded Attempt Accounting

**Analysis contract:** `P01-AC-010-GATES-REPAIRS` — interpretation ceiling: execution closure/reproducibility.

| Gate | Name | Status | Primary evidence |
| --- | --- | --- | --- |
| P01-G01 | authority_phase0_intake | PASS | manifests/phase_01/test_manifest.json; authority_manifest.json |
| P01-G02 | source_provenance_license | PASS | reports/phase_01/sources/source_version_license_report.json; inputs/source_inventory.json |
| P01-G03 | schema_canonical_object | PASS | reports/phase_01/validation/; records/ |
| P01-G04 | metadata_completeness | PASS | reports/phase_01/metadata/metadata_completeness.json |
| P01-G05 | label_mapping | PASS | reports/phase_01/labels/label_map_validation.json; records/labels/ |
| P01-G06 | preprocessing_fit_scope | PASS | reports/phase_01/preprocessing/fit_scope.json; records/preprocessing/ |
| P01-G07 | split_disjointness | PASS | reports/phase_01/splits/disjointness.json; records/splits/ |
| P01-G08 | leakage_chronology | PASS | reports/phase_01/leakage/leakage_contamination.json |
| P01-G09 | low_calibration_budgets | PASS | reports/phase_01/splits/low_calibration_budgets.csv |
| P01-G10 | window_identity | PASS | reports/phase_01/windows/window_timing_overlap.json; records/windows/ |
| P01-G11 | quality_coverage | PASS | reports/phase_01/quality/quality_coverage.json; records/quality/ |
| P01-G12 | matched_keys_ablation_readiness | PASS | manifests/phase_01/layer1_ablation_readiness_l1_v1.json; reports/phase_01/readiness/matched_key_completeness.csv |
| P01-G13 | cards_limitations | PASS | docs/cards/datasets/; docs/cards/protocols/ |
| P01-G14 | manifest_path_hash_closure | PASS | manifests/phase_01/execution_bundle_manifest.json; checksums.sha256 |
| P01-G15 | phase2_compatibility | PASS | phase2_handoff/phase_01_to_phase_02.yaml |
| P01-G16 | complete_artifact_closure | PASS | manifests/phase_01/layer1_manifest.json; phase_execution_handoff.yaml |

The terminal execution state contains **27 accepted stage identities (00–26)**, **16/16 gates PASS**, **50 tests PASS**, and **0 unresolved blockers**. The final execution bundle has **13,216 ZIP members** and **13,164 checksum rows**; all 13,164 targets independently validate with zero missing or mismatched targets.

The existence of earlier failures does not invalidate the accepted lineage because the workflow was fail-closed: defects stopped affected progress, evidence was preserved, the lawful scope was repaired, and affected stages were rerun or reconstructed without silently treating a failed result as PASS. That conclusion would be invalid if the failures had been hidden or if a repair had changed science without an explicit amendment; neither condition holds in the final evidence.

### Material repair episodes

| Episode | Affected surface | Root cause | Classification | Scientific effect? | Accepted resolution |
| --- | --- | --- | --- | --- | --- |
| R45 | Stage 14/core adoption | Dependency-order record-ID normalization needed for equivalence/adoption | CANONICALIZATION_FIX / IMPLEMENTATION_FIX | No | Existing core adopted after record equivalence + exact remote hash; no core recomputation/reupload |
| R46–R47 | Runtime/canonical serialization | Missing datetime/timezone import; hash-bearing float representation needed governed decimal strings | IMPLEMENTATION_BUG_FIX / CANONICALIZATION_FIX | No | Imports corrected; decimal-string canonicalization restored deterministic identities |
| R48 | A4 child interface/persistence | Child interface/storage identity/resumability issues | IMPLEMENTATION_FIX / PERSISTENCE_FIX | No | A4 interface, reader verification, per-subject checkpoints and exact expected-parent checks hardened |
| R49 | A4 design at Stage 14 | Original +0.0…+4.0 s control infeasible for one valid parent event | SCIENTIFIC_CONTRACT_CHANGE limited to future A4 alternative profile | Yes — A4 alternative only; core unchanged | Replaced proposed A4 R1 with matched +0.0…+3.5 s R2; 12,910/12,910 parents retained; no padding/clipping/drop |
| R50 | Stage 07 | Notebook integration retained stale revision guard | INTEGRATION_FIX | No | Same-session continuation repaired guard; successful earlier work reused |
| R51–R53 | Stage 18 | Bad module import and two recovery-cell integration defects | INTEGRATION_FIX | No | Valid shim/import tested under exact worker environment; Stage 18 rerun once to PASS |
| R54 | Stage 26 release | Live Kaggle credential was serialized into environment evidence; secret scanner correctly blocked release | SECURITY/PACKAGING_FIX | No | Contaminated failed exports deleted, environment values redacted, final ZIPs rebuilt and exact-token scan passed |

## P01.18. Source Dataset Portfolio

The portfolio is deliberately heterogeneous in subject count, sampling rate, and source event vocabulary. P01 does not erase that heterogeneity; it records it and standardizes only the parts required for the common binary branch. PhysioNet contributes 109 subjects and mixed 128/160 Hz source rates; BNCI contributes nine subjects at 250 Hz with a four-class MI vocabulary; Lee contributes 54 subjects at 1000 Hz. The common target is not “all events in all datasets,” but the frozen left/right imagery branch after source-specific exclusions.

## P01.19. Task, Labels, and Exclusions

| Dataset | Included mapping | Excluded source events/classes | LabelMapRecord / hash |
| --- | --- | --- | --- |
| PhysioNetMI | run 4/8/12 T1→left_hand; T2→right_hand | T0 rest/no-action; non-imagery runs not in official branch | IHARQ-LABELMAPRECORD-20260806-4379781a3b5f5ea9 / 4379781a3b5f5ea91f70c560e007de42d8624b4ee0e6a792921079fbd069a663 |
| BNCI2014_001 | 769→left_hand; 770→right_hand | 771 feet; 772 tongue; 276/277 baselines; 768/783/1023/1072/32766 technical/rejected markers | IHARQ-LABELMAPRECORD-20260806-587dcfff81307768 / 587dcfff813077685eaa34b9b204eae5791be7c5d25f2a500ddaff39b0348f84 |
| Lee2019_MI | left_hand→left_hand; right_hand→right_hand | online/test or unlabeled non-official branch excluded by source selection | IHARQ-LABELMAPRECORD-20260806-b551cfd20335896c / b551cfd20335896c762d508e5950c8598772b7d4c75bec5d9ddee8e177bfe105 |

The accepted label denominator is **6,476 left_hand** and **6,434 right_hand**. Excluded source events are not “missing negatives”; they are outside the supervised task by definition. Reclassifying them would change the estimand and invalidate downstream matching.

## P01.20. Split and Leakage Protocol

The split identity is `IHARQ-SPLITRECORD-20260806-e4e371d332c61e36`, protocol `P01-L1-SPLIT-OFFICIAL-R2`, seed 20260804. No final repair changed split membership. Future fitting/selection must respect role visibility; test data remain outside fitting/selection and calibration budgets are drawn only from calibration.

## P01.21. Low-Calibration Budgets

P01 freezes six per-class calibration budgets—**1, 2, 4, 8, 16, 32**—using deterministic nested SHA-256-ranked source-event subsets within the calibration role. There are 18 registered dataset/budget rows. Their existence is an infrastructure result only: P01 did not measure how performance changes with one versus 32 examples per class.

## P01.22. Preprocessing Pipeline

| Order | Operation | Frozen behavior |
| --- | --- | --- |
| 1 | Unit validation/conversion | target volts; metadata conversion required |
| 2 | Event capture | annotations/stim/provider tables; preserve original samples/onsets; fail ambiguous origin |
| 3 | EEG channel selection | EEG only; preserve original order |
| 4 | Demean | over time per continuous run after event capture |
| 5 | Average rereference | selected EEG channels |
| 6 | Joint polyphase resampling | MNE Raw.resample to 160 Hz; event array jointly returned; Kaiser β=5.0; reflect pad; n_jobs=1 |
| 7 | Band-pass | 8–32 Hz; 4th-order Butterworth SOS; scipy sosfiltfilt; zero phase; odd pad; padlen 27 |
| 8 | Cast | float32 |

Joint event/signal resampling is important because the window anchor is an event **sample index**, not merely a floating timestamp. By using the event array returned by the same resampling operation, P01 avoids separately rounding times after rate conversion. Continuous-run filtering occurs before window extraction, so each 3-second window does not suffer an artificial edge filter performed in isolation. P01 did not test whether this preprocessing improves classification; it establishes a common, traceable representation.

## P01.23. Official Core Windowing and Core Data Product Results

| Property | Final value |
| --- | --- |
| anchor | MI cue onset |
| start/stop | +0.5 s → +3.5 s |
| duration | 3.0 s |
| sampling | 160 Hz |
| start offset | 80 samples |
| duration | 480 samples |
| policy | one official window per included source event |
| bounds | reject out of bounds |
| clipping | prohibited |
| dtype | float32 |
| windows | 12,910 |
| invalid | 0 / 12,910 |
| subject shards | 172 |
| logical float32 bytes | 1,356,625,920 |
| actual HDF5 bytes | 1,166,652,764 |
| actual compression ratio | 0.8600 |

The size reduction relative to raw source inventories should not be interpreted as lossy signal compression or data deletion for convenience. The largest reduction comes from scientific extraction: only selected EEG channels, target events, a common frequency band, and one 3-second float32 tensor per accepted event are persisted. HDF5 gzip compression then provides a comparatively modest additional reduction. The output therefore remains lossless with respect to the frozen derived tensor, not a copy of the full raw recordings.

## P01.24. Quality and Validation Results

The quality result is summarized in Analysis 4. The important interpretive separation is: **soft/provider flag ≠ hard invalid ≠ invalid window**. P01 observed 20 soft/provider flags, zero hard-invalid summaries, and zero invalid official core windows. None of those numbers should be converted into a claim that the signals are artifact-free or clinically clean.

## P01.25. External Persistence and Reproducibility Results

The execution bundle is intentionally not the container for gigabytes of HDF5 tensors. Instead, it holds the identities, manifests, hashes, indices, readers, and pointers that connect the compact project state to the exact external numerical Datasets. After verified upload and remote-manifest checks, local shard copies could be removed without breaking identity because the immutable provider/version/hash contract remains. This is why the execution bundle can be complete even though the numerical tensors live externally.

## P01.26. A0–A13 Readiness

The complete readiness table is in Analysis 7 and Appendix E. The substantive result is uniform: every official A identity has the required Layer-1 foundation, but none was scientifically executed in P01. This prevents two opposite errors—omitting later controls because they are not executed yet, or falsely treating infrastructure as an effectiveness result.

## P01.27. A14 Absence

**A14: REJECTED / ABSENT.** No A14 selector, run, result, or claim exists. The absence is explicitly validated and retained for audit visibility rather than relying on silence.

## P01.28. A4 R2 Feasibility, Redesign, and Readiness

Analysis 8 provides the full chronology. The central scientific lesson is methodological: exact denominator matching can constrain an alternative design. The one boundary event made +4.0 seconds infeasible without changing the data. R2 preserves every parent, so future A4 comparisons can start from a denominator-matched substrate. This is a stronger *fairness foundation* than padding or attrition, but it is not evidence about which window performs better.

## P01.29. Environment and Resource Amendments

The actual runtime differs from original intent only on execution-owned surfaces described in Analysis 9. These differences are explicitly carried forward in reproducibility metadata rather than retroactively rewriting the Build Book. That preserves both historical intent and actual execution truth.

## P01.30. Execution Stage Results

| Stage | Purpose | Final status | Material historical note |
| --- | --- | --- | --- |
| 00 | Corrected bootstrap and persistent isolated worker | PASS | — |
| 01 | Environment | PASS | — |
| 02 | Project and input intake | PASS | — |
| 03 | Authority and configuration | PASS | — |
| 04 | Phase 0 regression | PASS | — |
| 05 | Source resolution | PASS | — |
| 06 | Dataset registry | PASS | — |
| 07 | Pass 1: verified source acquisition and bounded loading | PASS | Stale R42/R49 revision guard stopped before worker submission; R50 same-session integration repair; final Stage 07 PASS. |
| 08 | Metadata normalization | PASS | — |
| 09 | Label mapping | PASS | — |
| 10 | Preprocessing compilation | PASS | — |
| 11 | Split construction and frozen fit population | PASS | — |
| 12 | Low-calibration budgets | PASS | — |
| 13 | Pass 2A: bounded preprocessing fit | PASS | — |
| 14 | Adopt verified core and materialize matched A4 R2 | PASS | Core adoption/canonical record-ID normalization plus A4 interface/persistence hardening; R49 A4 R2 materialization; core reused unchanged. |
| 15 | Validate and commit the separate A4 R2 Dataset | PASS | Separate A4 Dataset committed after exact remote-manifest verification. |
| 16 | Record validation | PASS | — |
| 17 | Leakage audit | PASS | — |
| 18 | A0–A13 readiness | PASS | Missing module/import integration episode; R51–R53 same-session repair chain; final Stage 18 PASS. |
| 19 | Cards | PASS | — |
| 20 | Manifests | PASS | — |
| 21 | Negative register | PASS | — |
| 22 | P02 and later compatibility | PASS | — |
| 23 | Evidence sufficiency | PASS | — |
| 24 | Repair metadata | PASS | — |
| 25 | Final export preparation | PASS | — |
| 26 | Terminal decision and bundle export | PASS | Secret scan blocked contaminated package; R54 redacted/repacked without scientific rerun or duplicate Stage-26 identity; final export PASS. |

## P01.31. Failure, Repair, and Rerun Analysis

The repair history contains two fundamentally different classes. Most repairs were implementation/integration/persistence/security corrections: imports, canonical representation, a stale revision guard, worker import resolution, storage verification, and secret-safe packaging. They did not change the scientific core. The A4 R1→R2 episode is different and is explicitly classified as a scientific-contract change **to the proposed future A4 alternative profile**, because feasibility evidence changed the window definition. It did not change the official core, split, labels, or denominator.

The governing pattern was:

`failed/superseded attempt → defect isolated → failed evidence preserved → minimum lawful repair → affected scope rerun/reconstructed → gate closure`.

This pattern matters because a final PASS is credible only if failed attempts are neither hidden nor silently relabeled as accepted.

## P01.32. Gate and Test Closure

The complete G01–G16 matrix is in Analysis 10 / Appendix D. Every gate is PASS, the regression suite is 50/50, and the final blocker list is empty. These are deterministic execution/reproducibility results, not model metrics.

## P01.33. Negative / Failed / Invalid / Excluded Evidence

| Evidence class | Observed P01 outcome | Interpretive treatment |
| --- | --- | --- |
| Historical failed attempt | Stage 07 stale guard; Stage 18 import integration; Stage 26 secret scan block; earlier A4 implementation defects | Preserved as superseded evidence; not counted as accepted final stage results |
| Scientific/design constraint | Original A4 +4.0 s profile infeasible for 1/12,910 valid parents | Negative feasibility result that motivated explicit R2 future profile |
| Invalid official core window | 0 / 12,910 | No denominator attrition under final core profile |
| A4 unmatched parent | 0 / 12,910 | Full matched substrate under R2 |
| Hard-invalid quality summary | 0 / 489 | No hard validity failure under frozen checks |
| Soft/provider quality flag | 20 / 489 summaries | Diagnostic annotations remain visible; not repaired away |
| Leakage issues detected | 0 reported under implemented checks | Supports bounded contract-leakage statement only |
| Current unresolved blocker | 0 | Execution evidence sufficient for report and downstream documentation |

## P01.34. Invalid / Excluded / Unmatched Accounting

Source DatasetRecords enumerate **20,093 source events** and the official binary branch admits **12,910**. Thus **7,183 source events** are outside the accepted binary denominator according to source-specific label/exclusion rules. They are not counted as invalid windows and are not silently converted to negative labels. Core invalid windows are **0/12,910**. A4 unmatched parents are **0/12,910**. Missing or checksum-failed admitted source files are not present in the final accepted source set; source/provenance gates pass.

## P01.35. Direct Phase 1 Findings

| Finding ID | Measured evidence | Supported statement | Evidence class | Limitation |
| --- | --- | --- | --- | --- |
| P01-FIND-001 | 3 active datasets, 172 subject groups, 453 source files; all three DatasetRecords VALIDATED with frozen aggregate SHA-256 identities. | P01 established exact source provenance and dataset identity for the selected public EEG portfolio. | PROVENANCE_EVIDENCE | PUBLIC_EEG_ONLY; source-license/redistribution restrictions apply. |
| P01-FIND-002 | 172 subject groups assigned train/calibration/validation/test = 102/35/17/18; disjointness PASS with no intersections. | The frozen subject-group split satisfies the implemented disjointness contract and preserves whole-subject role assignment. | VALIDATION_EVIDENCE | This establishes contract disjointness, not universal absence of every conceivable leakage mechanism. |
| P01-FIND-003 | 12,910 accepted parent events map one-to-one to 12,910 validated core WindowRecords; 0 invalid core windows. | The official Layer-1 event/window pipeline preserved the accepted-event denominator under the frozen core window policy. | INTEGRITY_EVIDENCE | Does not imply decoder adequacy or statistical power. |
| P01-FIND-004 | 172 subject HDF5 shards, 12,910 windows, float32, 1,166,652,764 uploaded HDF5 bytes; remote manifest hash verified. | The official core derived Dataset is reproducibly identifiable and retrievable under its provider version/logical revision/hash contract. | INTEGRITY_EVIDENCE | Private Kaggle access is required; source licenses continue to govern redistribution. |
| P01-FIND-005 | 489 quality summaries; 20 soft/provider flags; 0 hard-invalid summaries; 0/12,910 invalid official windows; policy ANNOTATE_NOT_REPAIR. | Quality issues were surfaced as governed annotations while hard validity criteria did not reject any official core window. | VALIDATION_EVIDENCE | A soft flag is not proof of physiological corruption, and zero hard-invalid cases is not a claim of artifact-free EEG. |
| P01-FIND-006 | Split disjointness PASS and leakage_contamination status PASS with zero reported issues across group, duplicate, overlap, fit-scope and budget/test-contamination checks. | No contract leakage was detected under the implemented deterministic checks. | VALIDATION_EVIDENCE | Bounded to implemented checks and frozen identities. |
| P01-FIND-007 | 18 budget rows = 3 datasets × six per-class budgets {1,2,4,8,16,32}; all frozen under seed 20260804. | P01 prepared deterministic low-calibration population identities for later evaluation. | READINESS_EVIDENCE | No calibration-performance experiment was executed in P01. |
| P01-FIND-008 | Exactly 14 readiness rows A0…A13, each FOUNDATION_READY and executed_in_p01=false; A14 absence validator PASS. | Layer 1 produced the matching/readiness foundation required by the official A0–A13 ladder without introducing A14. | READINESS_EVIDENCE | Foundation readiness is not ablation effectiveness. |
| P01-FIND-009 | 12,910/12,910 matched parents; 12,910 stored 3.5 s tensors; 38,730 registered virtual 2 s members; 0 invalid; 172 shards. | P01 established a fully matched A4 R2 Layer-1 substrate for future governed evaluation. | READINESS_EVIDENCE | A4 effectiveness was not executed or measured in P01; R2 arose after feasibility evidence. |
| P01-FIND-010 | One valid released parent event (PhysioNetMI:104:0:8:event:24) had only 560 post-cue samples; the 640-sample +4.0 s proposal would require 80 nonexistent samples. | Padding, clipping, fabrication, or event dropping would have changed the comparison; the matched +3.5 s R2 design preserved the complete denominator. | NEGATIVE_EVIDENCE | This is a design-feasibility result, not evidence that R2 performs better than R1 or core. |
| P01-FIND-011 | Accepted execution used Python 3.12.13 with exact package pins and adaptive disk policy; pin mismatches and import failures were zero. | Runtime compatibility/resource amendments changed execution conditions but did not alter datasets, labels, split, core preprocessing, core window, or core denominator. | EXECUTION_EVIDENCE | Reproduction should use the recorded actual environment rather than the original Python 3.11 intent. |
| P01-FIND-012 | 27/27 accepted stages PASS; 16/16 P01 gates PASS; regression suite 50/50 PASS; 0 unresolved blockers; 13,164/13,164 execution-bundle checksum targets valid. | The accepted P01 execution lineage satisfies its deterministic execution, validation, and package-closure contract. | EXECUTION_EVIDENCE | Execution closure does not imply model or clinical effectiveness. |
| P01-FIND-013 | Stage 07, 18 and 26 failures blocked continuation/release until targeted repairs passed; earlier successful scope was reused where lawful. | The execution history demonstrates fail-closed repair/reentry rather than silent acceptance of known defects. | HISTORICAL_FAILED_EVIDENCE | The repair history must remain visible; it is not evidence of scientific superiority. |
| P01-FIND-014 | P02 handoff references the exact core/A4 pointers, split, label maps, preprocessing and profile identities with mutation/leakage prohibitions. | P02 can consume the frozen Layer-1 data substrate without reinterpreting Layer-1 identities. | READINESS_EVIDENCE | Formal phase transition still follows the documentary closure sequence. |

## P01.36. Supported Interpretations

### P01-FIND-001 — Three-source public EEG portfolio was reconciled and validated

**Measured result.** 3 active datasets, 172 subject groups, 453 source files; all three DatasetRecords VALIDATED with frozen aggregate SHA-256 identities.

**Supported interpretation.** P01 established exact source provenance and dataset identity for the selected public EEG portfolio.

**Boundary / not supported.** PUBLIC_EEG_ONLY; source-license/redistribution restrictions apply.

### P01-FIND-002 — Subject-grouped split is disjoint under the implemented contract

**Measured result.** 172 subject groups assigned train/calibration/validation/test = 102/35/17/18; disjointness PASS with no intersections.

**Supported interpretation.** The frozen subject-group split satisfies the implemented disjointness contract and preserves whole-subject role assignment.

**Boundary / not supported.** This establishes contract disjointness, not universal absence of every conceivable leakage mechanism.

### P01-FIND-003 — Accepted-event denominator is conserved through core materialization

**Measured result.** 12,910 accepted parent events map one-to-one to 12,910 validated core WindowRecords; 0 invalid core windows.

**Supported interpretation.** The official Layer-1 event/window pipeline preserved the accepted-event denominator under the frozen core window policy.

**Boundary / not supported.** Does not imply decoder adequacy or statistical power.

### P01-FIND-004 — Official core numerical product was fully materialized and externally verified

**Measured result.** 172 subject HDF5 shards, 12,910 windows, float32, 1,166,652,764 uploaded HDF5 bytes; remote manifest hash verified.

**Supported interpretation.** The official core derived Dataset is reproducibly identifiable and retrievable under its provider version/logical revision/hash contract.

**Boundary / not supported.** Private Kaggle access is required; source licenses continue to govern redistribution.

### P01-FIND-005 — Quality coverage closed without silent repair

**Measured result.** 489 quality summaries; 20 soft/provider flags; 0 hard-invalid summaries; 0/12,910 invalid official windows; policy ANNOTATE_NOT_REPAIR.

**Supported interpretation.** Quality issues were surfaced as governed annotations while hard validity criteria did not reject any official core window.

**Boundary / not supported.** A soft flag is not proof of physiological corruption, and zero hard-invalid cases is not a claim of artifact-free EEG.

### P01-FIND-006 — No contract leakage was detected under implemented checks

**Measured result.** Split disjointness PASS and leakage_contamination status PASS with zero reported issues across group, duplicate, overlap, fit-scope and budget/test-contamination checks.

**Supported interpretation.** No contract leakage was detected under the implemented deterministic checks.

**Boundary / not supported.** Bounded to implemented checks and frozen identities.

### P01-FIND-007 — Low-calibration budget identities were frozen for downstream use

**Measured result.** 18 budget rows = 3 datasets × six per-class budgets {1,2,4,8,16,32}; all frozen under seed 20260804.

**Supported interpretation.** P01 prepared deterministic low-calibration population identities for later evaluation.

**Boundary / not supported.** No calibration-performance experiment was executed in P01.

### P01-FIND-008 — A0–A13 Layer-1 foundations are present and A14 is absent

**Measured result.** Exactly 14 readiness rows A0…A13, each FOUNDATION_READY and executed_in_p01=false; A14 absence validator PASS.

**Supported interpretation.** Layer 1 produced the matching/readiness foundation required by the official A0–A13 ladder without introducing A14.

**Boundary / not supported.** Foundation readiness is not ablation effectiveness.

### P01-FIND-009 — A4 R2 matched data substrate covers the complete core parent-event set

**Measured result.** 12,910/12,910 matched parents; 12,910 stored 3.5 s tensors; 38,730 registered virtual 2 s members; 0 invalid; 172 shards.

**Supported interpretation.** P01 established a fully matched A4 R2 Layer-1 substrate for future governed evaluation.

**Boundary / not supported.** A4 effectiveness was not executed or measured in P01; R2 arose after feasibility evidence.

### P01-FIND-010 — A4 4.0 s proposal produced a genuine feasibility constraint result

**Measured result.** One valid released parent event (PhysioNetMI:104:0:8:event:24) had only 560 post-cue samples; the 640-sample +4.0 s proposal would require 80 nonexistent samples.

**Supported interpretation.** Padding, clipping, fabrication, or event dropping would have changed the comparison; the matched +3.5 s R2 design preserved the complete denominator.

**Boundary / not supported.** This is a design-feasibility result, not evidence that R2 performs better than R1 or core.

### P01-FIND-011 — Execution environment amendments preserved the scientific core contract

**Measured result.** Accepted execution used Python 3.12.13 with exact package pins and adaptive disk policy; pin mismatches and import failures were zero.

**Supported interpretation.** Runtime compatibility/resource amendments changed execution conditions but did not alter datasets, labels, split, core preprocessing, core window, or core denominator.

**Boundary / not supported.** Reproduction should use the recorded actual environment rather than the original Python 3.11 intent.

### P01-FIND-012 — Final execution and gate closure are complete

**Measured result.** 27/27 accepted stages PASS; 16/16 P01 gates PASS; regression suite 50/50 PASS; 0 unresolved blockers; 13,164/13,164 execution-bundle checksum targets valid.

**Supported interpretation.** The accepted P01 execution lineage satisfies its deterministic execution, validation, and package-closure contract.

**Boundary / not supported.** Execution closure does not imply model or clinical effectiveness.

### P01-FIND-013 — Material failure episodes were fail-closed and superseded explicitly

**Measured result.** Stage 07, 18 and 26 failures blocked continuation/release until targeted repairs passed; earlier successful scope was reused where lawful.

**Supported interpretation.** The execution history demonstrates fail-closed repair/reentry rather than silent acceptance of known defects.

**Boundary / not supported.** The repair history must remain visible; it is not evidence of scientific superiority.

### P01-FIND-014 — P01 provides a technically usable P02 data contract

**Measured result.** P02 handoff references the exact core/A4 pointers, split, label maps, preprocessing and profile identities with mutation/leakage prohibitions.

**Supported interpretation.** P02 can consume the frozen Layer-1 data substrate without reinterpreting Layer-1 identities.

**Boundary / not supported.** Formal phase transition still follows the documentary closure sequence.

## P01.37. Candidate Claims for Layer 0

These are **candidates**, not approved claims. Layer 0 owns final disposition and wording.

| Candidate ID | Proposed wording | Findings | Evidence class | Support | Limitations | Ceiling | Status | Priority |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P01-CLAIM-CAND-001 | Phase 1 established a checksum-bound, provenance-traceable three-dataset public EEG foundation for the IHARQ binary motor-imagery branch. | P01-FIND-001 | PROVENANCE_EVIDENCE | DIRECT | PUBLIC_EEG_ONLY, NON_CLINICAL | Data provenance and reproducibility only | CANDIDATE_FOR_LAYER0_REVIEW | HIGH |
| P01-CLAIM-CAND-002 | The frozen P01 split is subject-grouped and passed the implemented disjointness and leakage checks. | P01-FIND-002, P01-FIND-006 | VALIDATION_EVIDENCE | DIRECT_BOUNDED | IMPLEMENTED_CHECKS_ONLY | Contract leakage/disjointness correctness | QUALIFICATION_LIKELY_REQUIRED | HIGH |
| P01-CLAIM-CAND-003 | The official Layer-1 pipeline conserved the complete accepted-event denominator: 12,910 accepted events produced 12,910 valid core windows. | P01-FIND-003 | INTEGRITY_EVIDENCE | DIRECT | NO_MODEL_EFFECT_INFERENCE | Data materialization closure | CANDIDATE_FOR_LAYER0_REVIEW | HIGH |
| P01-CLAIM-CAND-004 | The official core numerical Dataset was persisted as 172 lossless HDF5 subject shards and verified by immutable provider/version/manifest identities. | P01-FIND-004 | INTEGRITY_EVIDENCE | DIRECT | PRIVATE_KAGGLE_EXTERNAL_ARTIFACT_ACCESS, SOURCE_LICENSE_CONSTRAINTS | Retrieval/storage reproducibility | CANDIDATE_FOR_LAYER0_REVIEW | MEDIUM |
| P01-CLAIM-CAND-005 | P01 quality processing followed an annotate-not-repair policy; 20 soft/provider flags were preserved while no hard-invalid summary or official core window was observed. | P01-FIND-005 | VALIDATION_EVIDENCE | DIRECT_BOUNDED | SOFT_FLAG_NOT_EQUIVALENT_TO_CORRUPTION | Quality annotation and hard-validity closure | QUALIFICATION_LIKELY_REQUIRED | MEDIUM |
| P01-CLAIM-CAND-006 | P01 established the Layer-1 readiness foundation for all official A0–A13 identities while preserving A14 as absent/prohibited. | P01-FIND-008 | READINESS_EVIDENCE | DIRECT | NO_ABLATION_EFFECTIVENESS_IN_P01 | Foundation readiness only | CANDIDATE_FOR_LAYER0_REVIEW | HIGH |
| P01-CLAIM-CAND-007 | P01 established a 12,910-event fully matched A4 R2 data substrate for future governed evaluation, without padding, clipping, fabrication, or parent-event loss. | P01-FIND-009, P01-FIND-010 | READINESS_EVIDENCE | DIRECT_BOUNDED | A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01 | Future A4 substrate readiness; not A4 effectiveness | QUALIFICATION_LIKELY_REQUIRED | HIGH |
| P01-CLAIM-CAND-008 | The accepted P01 execution closed all 27 stages, 16 deterministic gates, and 50 regression tests with zero unresolved blockers. | P01-FIND-012 | EXECUTION_EVIDENCE | DIRECT | NO_EFFECTIVENESS_INFERENCE | Execution/reproducibility closure | CANDIDATE_FOR_LAYER0_REVIEW | HIGH |
| P01-CLAIM-CAND-009 | P01 runtime compatibility and resource amendments preserved the frozen scientific core data contract while recording the actual Python 3.12.13 environment. | P01-FIND-011 | EXECUTION_EVIDENCE | DIRECT_BOUNDED | ACTUAL_RUNTIME_PYTHON_3_12_13_WITH_COMPATIBILITY_AMENDMENT, ADAPTIVE_DISK_RESOURCE_AMENDMENT | Execution reproducibility | QUALIFICATION_LIKELY_REQUIRED | MEDIUM |
| P01-CLAIM-CAND-010 | P01 provides a frozen technical data contract that P02 can consume without silent relabeling, rewindowing, split mutation, denominator substitution, or test leakage. | P01-FIND-014 | READINESS_EVIDENCE | DIRECT | DOCUMENTARY_CLOSURE_SEQUENCE_REMAINS | Downstream technical readiness | CANDIDATE_FOR_LAYER0_REVIEW | HIGH |
| P01-CLAIM-CAND-011 | A4 R2 improves decoder performance relative to the core window. | P01-FIND-009 | READINESS_EVIDENCE | NONE_FROM_P01 | A4_EFFECTIVENESS_NOT_EXECUTED | Not claimable from P01 | NOT_SUPPORTED_BY_P01 | HIGH |
| P01-CLAIM-CAND-012 | The P01 data foundation demonstrates clinical effectiveness or deployment safety. | P01-FIND-001, P01-FIND-012 | EXECUTION_EVIDENCE | NONE_FROM_P01 | NON_CLINICAL, NO_DEPLOYMENT_CLAIM | Not claimable from P01 | NOT_SUPPORTED_BY_P01 | HIGH |

## P01.38. Mechanism Hypotheses

### P01-HYP-001
**HYPOTHESIS — NOT DIRECTLY ESTABLISHED BY P01**

Keeping every subject entirely within one split role should reduce identity-specific leakage pathways that could arise from subject signatures shared across train and held-out roles.

Basis: P01-FIND-002, P01-FIND-006.

### P01-HYP-002
**HYPOTHESIS — NOT DIRECTLY ESTABLISHED BY P01**

Joint signal/event resampling and integer sample anchoring should reduce event-alignment drift relative to independent floating-time reconstruction, improving cross-dataset matching stability.

Basis: P01-FIND-003.

### P01-HYP-003
**HYPOTHESIS — NOT DIRECTLY ESTABLISHED BY P01**

The matched 3.5-second A4 design should enable a fairer future longer-window comparison than padding the sole boundary-short event or dropping it, because the parent-event denominator remains identical.

Basis: P01-FIND-009, P01-FIND-010.

### P01-HYP-004
**HYPOTHESIS — NOT DIRECTLY ESTABLISHED BY P01**

Externalizing large lossless numerical tensors while retaining compact manifests and exact hashes should reduce local storage pressure without sacrificing governed artifact identity.

Basis: P01-FIND-004, P01-FIND-009, P01-FIND-011.

## P01.39. Limitations

| Limitation ID | Scope | Description | Evidence consequence | Claim consequence | Blocking? | Downstream inheritance |
| --- | --- | --- | --- | --- | --- | --- |
| PUBLIC_EEG_ONLY | P01 and downstream inherited | The empirical substrate is public benchmark/research EEG, not a clinical or deployment population. | Supports public-data provenance and benchmark data-contract claims only. | No clinical generalization or deployment claims. | NO | P02-P15; Layer 0 |
| NON_CLINICAL | Project/P01 | No clinical cohort, clinical endpoint, or treatment outcome is present. | Evidence is non-clinical. | Clinical benefit/effectiveness claims prohibited. | NO | All claim-bearing outputs |
| NO_DEPLOYMENT_CLAIM | Project/P01 | P01 does not evaluate deployed real-world control, operational safety, or medical-device behavior. | Execution validity cannot be extrapolated to deployment safety. | Deployment/safety claims prohibited. | NO | Layer 0 and later deployment-related phases |
| PRIVATE_KAGGLE_EXTERNAL_ARTIFACT_ACCESS | P01 external persistence | Core and A4 numerical HDF5 artifacts are private Kaggle Datasets. | Reproduction requires authorized access plus exact provider revision and manifest-hash verification. | No effect on scientific content, but constrains independent retrieval. | NO | P02-P15 reproducibility |
| A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01 | A4 | A4 R2 was introduced after a real +4.0 s boundary infeasibility was observed. | R2 is frozen prospectively for future downstream use but is not an originally preregistered P01 effectiveness condition. | No A4 effectiveness claim from P01. | NO | P02 A4 and Layer 0 |
| ACTUAL_RUNTIME_PYTHON_3_12_13_WITH_COMPATIBILITY_AMENDMENT | Execution environment | Build Book intended Python 3.11, while accepted Kaggle execution used Python 3.12.13 under a documented compatibility amendment. | Exact reproduction should use actual captured environment or validate equivalence. | No scientific claim consequence when science/config remains unchanged. | NO | Reproduction |
| ADAPTIVE_DISK_RESOURCE_AMENDMENT | Execution resources | Governed amendment `P01-L1-KAGGLE-ADAPTIVE-DISK-R1` replaced the legacy 60 GiB preflight with an adaptive measured requirement with 6.0 GiB effective minimum; observed free disk was 18.94 GiB. | Resource policy differs from pre-run intent but was recorded and fail-safe. | No scientific claim consequence. | NO | Reproduction |
| SOURCE_LICENSE_REDISTRIBUTION_CONSTRAINTS | Dataset persistence | Source-specific licenses, especially BNCI CC BY-ND, constrain redistribution of raw/derived signal bytes. | Bundle carries metadata/hashes/pointers rather than unrestricted raw-data redistribution. | No performance consequence; affects artifact distribution. | NO | Repository/release packaging |
| BINARY_MI_BRANCH_SCOPE | P01 task | P01 official supervised denominator is left-hand versus right-hand imagery only; rest, feet, tongue, execution, technical and unlabeled online/test events are excluded as defined per source. | Results describe the frozen binary task only. | No claims about excluded tasks/classes. | NO | P02-P15 |

## P01.40. Evidence Ceiling

P01 can directly support statements about source provenance, reproducible intake, frozen labels/exclusions, split identity/disjointness, preprocessing/window implementation, denominator closure, quality/lineage/integrity, external persistence, A0–A13 readiness, A14 absence, A4 substrate readiness, and execution/gate closure.

P01 cannot by itself support decoder superiority, accuracy/AUROC gains, calibration benefit, selective-prediction benefit, A4 performance benefit, IHARQ benefit, temporal-trust benefit, policy-learning benefit, stress robustness, embodiment effectiveness, clinical effectiveness, treatment benefit, deployment safety, or real-world control. No p-values, confidence intervals, effect sizes, decoder accuracies, or model comparisons are introduced in this report because they are not P01 analyses.

## P01.41. Phase 0 → Phase 1 Progression

| Dimension | P00 | P01 |
| --- | --- | --- |
| Primary role | Engineering/admin foundation | Governed empirical data foundation |
| Evidence class | ENGINEERING_FOUNDATION_CONFORMANCE / historical Mode B | Execution, provenance, validation, integrity and readiness evidence |
| Real public EEG | No empirical dataset execution | Three validated public EEG sources |
| Canonical records | Schemas/fixtures/contracts | Real Dataset/Label/Split/Preprocessing/Window/quality records |
| A0–A13 | Readiness identities only | Layer-1 matching foundations ready; still not effectiveness |
| External numerical artifacts | Not required for P00 | Core and A4 HDF5 Datasets persisted externally |
| Downstream readiness | Foundation for P01 | Technical data contract for P02 and later phases |

P01 does not replace P00; it is the first empirical instantiation of P00’s governed substrate.

## P01.42. Role of P01 in the Overall IHARQ Architecture

Downstream model work cannot safely precede P01 because later phases need stable answers to basic questions: which subject is this, which dataset/version produced the event, which task label is legal, which split role owns the subject, what preprocessing/window generated the tensor, what quality flags apply, and which parent-event key allows matched comparisons. If any of those identities drift after model training, model comparisons can become unfair or irreproducible.

P01 therefore freezes the data substrate that later decoder (P02), calibration/selective prediction, IHARQ/evidence-quality, temporal trust, deferral/policy, stress, and embodiment phases consume. It deliberately leaves model fitting, metric effects, uncertainty quality, policy utility, robustness, and embodiment outcomes unresolved for their owning phases.

## P01.43. Phase 2 and Downstream Readiness

| Consumer/work | Technical readiness | Documentary readiness | Scientifically executed in P01? | Condition |
| --- | --- | --- | --- | --- |
| P02 baseline decoders | TECHNICALLY READY | Protocol + this report ready; formal transition follows closure chain | NO | consume exact core/split/labels/preprocessing/window identities |
| Future A4 evaluation | TECHNICALLY READY | A4 R2 synchronized in Protocol | NO | use exact R2 profiles and matched parent keys |
| Low-calibration evaluation | INFRASTRUCTURE READY | Budget identities frozen | NO | use registered calibration subsets only |
| Later calibration/uncertainty | DATA FOUNDATION READY | Downstream Protocol cells required | NO | no test visibility |
| Stress/temporal/policy/embodiment | UPSTREAM DATA FOUNDATION READY | Later phase contracts required | NO | inherit P01 identities and limitations |
| Evidence Map | SOURCE IDS READY | Waits for Layer 0 disposition | NOT APPLICABLE | map claims after Layer 0 |
| Layer 10 | READ-ONLY SOURCES READY | Waits for governed Evidence Map | NOT APPLICABLE | no hidden recomputation |

## P01.44. Phase 2 Handoff

P02 may consume the official core Dataset pointer `csthv999z/iharq-p01-l1-derived-windows-d03f0a7c869d-20260806222242-68a91473` (provider v2/logical rev1, manifest `dc21f418e9a1add62adb346f627d5d729735a5f1ecaa1d771f6fa5cfede627e1`), split record `IHARQ-SPLITRECORD-20260806-e4e371d332c61e36`, the three validated LabelMapRecords, preprocessing record `IHARQ-PREPROCESSINGRECORD-20260806-a11b59eeb3861a08`, the official core +0.5…+3.5 s profile, config `d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f`, and limitation tags. A4 may be invoked only under `A4_LONG_MATCHED_3P5S_R2` / `A4_MULTI_3X2S_UNIFORM_0P75S_R2` with parent-event matching.

P02 is prohibited from silently relabeling, rewindowing, changing split membership, substituting denominators, using test information during fitting/selection, or substituting another A4 profile. Any such change is an amendment/invalidation event rather than an implementation convenience.

## P01.45. Layer 0 Handoff

Layer 0 receives the candidate-claim register, direct findings, exact evidence paths, limitations, negative evidence, claim ceilings and wording risks. **No claim in this report is Layer-0 approved.** The highest-priority review risks are overgeneralizing “no detected leakage,” interpreting zero invalid windows as artifact-free EEG, treating A0–A13 readiness as effectiveness, and overstating A4 R2 as demonstrated performance benefit.

## P01.46. Evidence Map Handoff

The report provides stable `P01-FIND-*` and `P01-CLAIM-CAND-*` identifiers plus record/artifact/stage paths. The Evidence Map should link only Layer-0-dispositioned claims to those sources and later assign manuscript/thesis locations; this report does not perform that final mapping.

## P01.47. Layer 10 Source Handoff

Layer 10 may render the saved inventory, split, denominator, quality, A0–A13, A4 chronology, repair, gate, external-artifact and limitation tables. It may not recompute hidden experimental logic, retune thresholds, omit negative evidence, or strengthen candidate claims.

## P01.48. Recommended Figures and Tables

| Figure ID | Purpose | Source artifacts | Source fields | Allowed interpretation |
| --- | --- | --- | --- | --- |
| P01-FIG-SRC-001 | P00→P01 progression | P00 final report + P01 architecture/handoff | phase role, inherited/new surfaces | Engineering foundation → empirical data foundation only |
| P01-FIG-SRC-002 | Source → accepted event → core window flow | DatasetRecords + WindowRecords | 20,093 source events; 12,910 admitted; by-dataset counts | Denominator/accounting; not model performance |
| P01-FIG-SRC-003 | Subject split allocation | SplitRecord + disjointness report | subject counts by role/dataset | Split structure only |
| P01-FIG-SRC-004 | Preprocessing chain | PreprocessingRecord | ordered operations and parameters | Implementation contract only |
| P01-FIG-SRC-005 | Core denominator conservation | WindowRecords + pointer | accepted/core/persisted counts | Materialization closure |
| P01-FIG-SRC-006 | Core vs A4 timing | core window freeze + A4 pointer | +0.5–3.5 vs +0–3.5 and three subviews | Timing/readiness only |
| P01-FIG-SRC-007 | A4 R1 failure → R2 design | notebook R49 boundary evidence + A4 freeze | one 4 s failure; 0 3.5 s failures | Feasibility chronology; no effect claim |
| P01-FIG-SRC-008 | Stage/repair chronology | stage results + repair ledger | 00–26 and R45–R54 material episodes | Execution history |
| P01-FIG-SRC-009 | Evidence ceiling | Protocol + findings/claims | claimable vs deferred categories | Claim-boundary illustration |
| P01-FIG-SRC-010 | P01→P02 handoff graph | P02 handoff + pointers | required record/profile IDs | Technical consumption contract |

Recommended source tables are already represented in this report: source dataset reconciliation, subject/event/window counts, split counts, preprocessing freeze, quality results, A0–A13 readiness, A4 profiles, external artifacts, gates, repair history, limitations, and candidate claims.

## P01.49. Reproducibility and Retrieval Guide

A downstream reproducer should begin with the finalized Protocol `IHARQ-PROTOCOL-V1-CUMULATIVE-THROUGH-P01-R1`, this report, and the accepted execution bundle SHA-256 `09c3bb0442d79ddf110cf66fc4fe61fe63e94c7d8ed9f198f606639b4191f16e`. Verify the execution-bundle checksum manifest before trusting internal paths. For the official core, attach the private Kaggle Dataset `csthv999z/iharq-p01-l1-derived-windows-d03f0a7c869d-20260806222242-68a91473` at provider version **2**, verify manifest `dc21f418e9a1add62adb346f627d5d729735a5f1ecaa1d771f6fa5cfede627e1`, load the declared window-to-shard index, then read the HDF5 group/row specified for each WindowRecord. For A4, attach `csthv999z/iharq-p01-l1-a4-d03f0a7c-9a7c6108` at provider version **1**, verify manifest `29124d59907610b1545e0a2b5d1811a4d4a2bf1df64cad49aa880f4721c47305`, and preserve `P01-L1-A4-WINDOW-FAMILY-FREEZE-R2` profile identities.

Reproduction must preserve the exact label maps, subject split, preprocessing record, window/profile identity and config. If any of those identities change, affected descendants are no longer the same P01 substrate and must be treated as an amended lineage.

## P01.50. Phase 1 Analysis Conclusion

P01 achieved the purpose Architecture assigns to the empirical anchor gate: it transformed heterogeneous public EEG sources into a common, traceable, split-safe Layer-1 substrate while keeping source provenance, exclusions, event timing, quality annotations, denominator identities and external persistence auditable. The result is not a model-performance finding. It is a validated *precondition* for fair downstream model-performance findings.

The strongest evidence is deterministic closure: the three-source portfolio is checksum-bound; all 172 subject groups are assigned disjointly; 12,910 admitted events conserve one-to-one into 12,910 official core windows; 0 official windows are invalid; quality flags remain visible under annotate-not-repair; no contract leakage is detected under implemented checks; the core and A4 numerical artifacts are remotely verified; A0–A13 foundations are complete with A14 absent; A4 R2 preserves the complete matched denominator; and all final stages/gates/tests/package checks close.

The repair history strengthens auditability precisely because it is not hidden. Most repairs are engineering/integration/security changes with no scientific effect. A4 R1→R2 is explicitly segregated as a feasibility-driven change to a future alternative profile and is not promoted to confirmatory evidence. This separation preserves the no-post-hoc rule.

## P01.51. Documentary Closure / Next-Step Decision

**P01 execution: ACCEPTED.**  
**Protocol v1.0 through P01: FROZEN.**  
**Phase 1 Evidence, Results, and Interpretation Report: COMPLETE subject to final package validation below.**  
**Additional P01 computation: NOT REQUIRED.**  
**Current unresolved report blockers: 0.**  
**Candidate claims: READY FOR LAYER 0 REVIEW.**  
**Evidence Map inputs: READY.**  
**Layer 10 source inputs: READY.**  
**Next governed step: PHASE 1 LAYER 0 CLAIM REVIEW AND DISPOSITION.**

This does **not** state that Phase 1 is fully closed. Layer 0, Evidence Map, Layer 10, and cumulative project-state update remain downstream documentary obligations.

# PART IV — CUMULATIVE THROUGH-P01 SYNTHESIS

## 43. P00→P01 Progression

| Dimension | P00 | P01 | Cumulative meaning |
| --- | --- | --- | --- |
| Primary evidence class | engineering/foundation conformance | empirical data-protocol, validation, integrity and readiness evidence | project progressed from governed infrastructure to governed real-data substrate |
| Canonical records | schemas/IDs/validation machinery | real Dataset/Label/Split/Preprocessing/Window records | record-first architecture instantiated on actual EEG |
| Ablations | A0–A13 identities/readiness hooks; no empirical execution | Layer-1 foundations for A0–A13; executed_in_p01=false | official ladder is structurally prepared without false effectiveness claims |
| A14 | rejected | absent/prohibited validator PASS | no A14 introduced |
| Claims | 7 engineering candidates later qualified by P00 Layer 0 | 12 P01 candidate/deferred/not-supported rows pending P01 Layer 0 | claim governance remains phase-aware |
| External numerical data | not required for P00 | core + A4 HDF5 persisted externally with manifests/pointers | first large governed scientific data products now exist |
| Next scientific capability | future phase contracts | P02 can consume frozen Layer-1 contract | decoder/model work can now begin without redefining data substrate |

## 44. Cumulative Direct Findings Through P01

The project demonstrably establishes two different classes of foundation evidence through P01. P00 establishes that the governed engineering substrate existed, validated and reproduced within its historical exact-environment boundary. P01 establishes that this substrate was successfully instantiated on the selected real public EEG sources with a closed denominator, subject-grouped split, validated preprocessing/windowing, quality/leakage evidence, external persistence, ablation foundations and a complete accepted execution lineage.

| Finding ID | Phase | Evidence class | Measured result / supported statement |
| --- | --- | --- | --- |
| P00-F-001 | P00 | REGISTERED_ENGINEERING_EXECUTION | 19/19 registered P00 engineering cells passed with terminal PASS |
| P00-F-002 | P00 | DETERMINISTIC_TESTING | 102/102 deterministic tests passed |
| P00-F-003 | P00 | POSITIVE_FIXTURE_VALIDATION | 19/19 valid or integrated bundles accepted; false rejections 0 |
| P00-F-004 | P00 | NEGATIVE_VALIDATION | 178/178 intentionally malformed categories rejected; false acceptances 0 |
| P00-F-005 | P00 | ARTIFACT_CLOSURE | all registered foundation inventories present and validated |
| P00-F-006 | P00 | INTEGRATION | 11/11 Layer 0–10 foundation interfaces passed registered P00 integration scope |
| P00-F-007 | P00 | FUTURE_CONTRACT_READINESS | P00 implemented; P01–P15 reusable contract surfaces prepared |
| P00-F-008 | P00 | REPRODUCIBILITY | 8/8 bounded reproduction steps passed under exact local snapshot |
| P00-F-009 | P00 | EVALUATION_READINESS | A0–A13 readiness hooks present; A14 rejected |
| P01-FIND-001 | P01 | PROVENANCE_EVIDENCE | P01 established exact source provenance and dataset identity for the selected public EEG portfolio. |
| P01-FIND-002 | P01 | VALIDATION_EVIDENCE | The frozen subject-group split satisfies the implemented disjointness contract and preserves whole-subject role assignment. |
| P01-FIND-003 | P01 | INTEGRITY_EVIDENCE | The official Layer-1 event/window pipeline preserved the accepted-event denominator under the frozen core window policy. |
| P01-FIND-004 | P01 | INTEGRITY_EVIDENCE | The official core derived Dataset is reproducibly identifiable and retrievable under its provider version/logical revision/hash contract. |
| P01-FIND-005 | P01 | VALIDATION_EVIDENCE | Quality issues were surfaced as governed annotations while hard validity criteria did not reject any official core window. |
| P01-FIND-006 | P01 | VALIDATION_EVIDENCE | No contract leakage was detected under the implemented deterministic checks. |
| P01-FIND-007 | P01 | READINESS_EVIDENCE | P01 prepared deterministic low-calibration population identities for later evaluation. |
| P01-FIND-008 | P01 | READINESS_EVIDENCE | Layer 1 produced the matching/readiness foundation required by the official A0–A13 ladder without introducing A14. |
| P01-FIND-009 | P01 | READINESS_EVIDENCE | P01 established a fully matched A4 R2 Layer-1 substrate for future governed evaluation. |
| P01-FIND-010 | P01 | NEGATIVE_EVIDENCE | Padding, clipping, fabrication, or event dropping would have changed the comparison; the matched +3.5 s R2 design preserved the complete denominator. |
| P01-FIND-011 | P01 | EXECUTION_EVIDENCE | Runtime compatibility/resource amendments changed execution conditions but did not alter datasets, labels, split, core preprocessing, core window, or core denominator. |
| P01-FIND-012 | P01 | EXECUTION_EVIDENCE | The accepted P01 execution lineage satisfies its deterministic execution, validation, and package-closure contract. |
| P01-FIND-013 | P01 | HISTORICAL_FAILED_EVIDENCE | The execution history demonstrates fail-closed repair/reentry rather than silent acceptance of known defects. |
| P01-FIND-014 | P01 | READINESS_EVIDENCE | P02 can consume the frozen Layer-1 data substrate without reinterpreting Layer-1 identities. |

## 45. Cumulative Supported Interpretation

The strongest lawful cumulative interpretation is that IHARQ now possesses a **reproducible, governed data-and-evidence spine through Layer 1**. The project can proceed to model-building phases without silently changing source identity, labels, split, preprocessing, core window, denominator or A4 profile. This is a major reproducibility and experimental-validity milestone, but it is intentionally narrower than a performance milestone: no decoder, calibration, policy, stress, embodiment, clinical or deployment effectiveness has yet been established.

## 46. Cumulative Candidate / Governed Claim Register

P00 claims are included for continuity but are already governed; **P01 is the active Layer-0 review scope**. No P01 row below is approved by this report.

| Claim | Origin | Report status | Governance disposition | Ceiling | Wording |
| --- | --- | --- | --- | --- | --- |
| P00-CLM-001/v2 | P00 | ALREADY_DISPOSITIONED_IN_P00_LAYER0 | APPROVE_WITH_QUALIFICATIONS | ENGINEERING_FOUNDATION_CONFORMANCE | Under the exact registered local snapshot and verified Python 3.13.5 environment, all 19 registered Phase 0 engineering/foundation conformance cells passed; this is non-empirical Mode B evidence and does not establish scientific effectiveness or Phase 0 closure. |
| P00-CLM-002/v2 | P00 | ALREADY_DISPOSITIONED_IN_P00_LAYER0 | APPROVE_WITH_QUALIFICATIONS | ENGINEERING_FOUNDATION_CONFORMANCE | In the frozen local Python 3.13.5 environment, the complete registered deterministic suite passed 102 of 102 tests; cross-version portability is not established. |
| P00-CLM-003/v2 | P00 | ALREADY_DISPOSITIONED_IN_P00_LAYER0 | APPROVE_WITH_QUALIFICATIONS | VALIDATION_EVIDENCE | Within the registered non-empirical fixture inventory, all 19 valid or integrated bundles were accepted and all 178 intentionally malformed categories were rejected as expected, with zero false valid rejections and zero false malformed acceptances. |
| P00-CLM-004/v2 | P00 | ALREADY_DISPOSITIONED_IN_P00_LAYER0 | APPROVE_WITH_QUALIFICATIONS | ARTIFACT_CLOSURE | The frozen Phase 0 package contains and validates the registered foundation inventories of 85 schemas, 35 configuration profiles, and 79 record-family profiles; inventory closure does not establish later-phase scientific effectiveness. |
| P00-CLM-005/v2 | P00 | ALREADY_DISPOSITIONED_IN_P00_LAYER0 | APPROVE_WITH_QUALIFICATIONS | FOUNDATION_INTEGRATION | All eleven Layer 0–10 foundation interfaces passed the registered Phase 0 integration scope; no later-phase scientific execution or effectiveness result is claimed. |
| P00-CLM-006/v2 | P00 | ALREADY_DISPOSITIONED_IN_P00_LAYER0 | APPROVE_WITH_QUALIFICATIONS | CONTRACT_READINESS | The P00 implementation foundation is complete within its registered local scope, and P01–P15 reusable contract surfaces are ready for later governed annex creation and execution; future empirical outputs have not been produced. |
| P00-CLM-007/v2 | P00 | ALREADY_DISPOSITIONED_IN_P00_LAYER0 | APPROVE_WITH_QUALIFICATIONS | LOCAL_REPRODUCIBILITY | The package reproduced from a clean isolated copy under the exact verified Python 3.13.5 and 22-distribution local dependency snapshot; portable cross-version reproducibility is not established. |
| P01-CLAIM-CAND-001 | P01 | CANDIDATE_FOR_LAYER0_REVIEW | PENDING_P01_LAYER0 | Data provenance and reproducibility only | Phase 1 established a checksum-bound, provenance-traceable three-dataset public EEG foundation for the IHARQ binary motor-imagery branch. |
| P01-CLAIM-CAND-002 | P01 | QUALIFICATION_LIKELY_REQUIRED | PENDING_P01_LAYER0 | Contract leakage/disjointness correctness | The frozen P01 split is subject-grouped and passed the implemented disjointness and leakage checks. |
| P01-CLAIM-CAND-003 | P01 | CANDIDATE_FOR_LAYER0_REVIEW | PENDING_P01_LAYER0 | Data materialization closure | The official Layer-1 pipeline conserved the complete accepted-event denominator: 12,910 accepted events produced 12,910 valid core windows. |
| P01-CLAIM-CAND-004 | P01 | CANDIDATE_FOR_LAYER0_REVIEW | PENDING_P01_LAYER0 | Retrieval/storage reproducibility | The official core numerical Dataset was persisted as 172 lossless HDF5 subject shards and verified by immutable provider/version/manifest identities. |
| P01-CLAIM-CAND-005 | P01 | QUALIFICATION_LIKELY_REQUIRED | PENDING_P01_LAYER0 | Quality annotation and hard-validity closure | P01 quality processing followed an annotate-not-repair policy; 20 soft/provider flags were preserved while no hard-invalid summary or official core window was observed. |
| P01-CLAIM-CAND-006 | P01 | CANDIDATE_FOR_LAYER0_REVIEW | PENDING_P01_LAYER0 | Foundation readiness only | P01 established the Layer-1 readiness foundation for all official A0–A13 identities while preserving A14 as absent/prohibited. |
| P01-CLAIM-CAND-007 | P01 | QUALIFICATION_LIKELY_REQUIRED | PENDING_P01_LAYER0 | Future A4 substrate readiness; not A4 effectiveness | P01 established a 12,910-event fully matched A4 R2 data substrate for future governed evaluation, without padding, clipping, fabrication, or parent-event loss. |
| P01-CLAIM-CAND-008 | P01 | CANDIDATE_FOR_LAYER0_REVIEW | PENDING_P01_LAYER0 | Execution/reproducibility closure | The accepted P01 execution closed all 27 stages, 16 deterministic gates, and 50 regression tests with zero unresolved blockers. |
| P01-CLAIM-CAND-009 | P01 | QUALIFICATION_LIKELY_REQUIRED | PENDING_P01_LAYER0 | Execution reproducibility | P01 runtime compatibility and resource amendments preserved the frozen scientific core data contract while recording the actual Python 3.12.13 environment. |
| P01-CLAIM-CAND-010 | P01 | CANDIDATE_FOR_LAYER0_REVIEW | PENDING_P01_LAYER0 | Downstream technical readiness | P01 provides a frozen technical data contract that P02 can consume without silent relabeling, rewindowing, split mutation, denominator substitution, or test leakage. |
| P01-CLAIM-CAND-011 | P01 | NOT_SUPPORTED_BY_P01 | PENDING_P01_LAYER0 | Not claimable from P01 | A4 R2 improves decoder performance relative to the core window. |
| P01-CLAIM-CAND-012 | P01 | NOT_SUPPORTED_BY_P01 | PENDING_P01_LAYER0 | Not claimable from P01 | The P01 data foundation demonstrates clinical effectiveness or deployment safety. |

## 47. Cumulative Negative / Failed Evidence

Cumulative evidence is not sanitized. P00 preserves intentionally malformed fixture rejections, portability gaps, historical Mode-B status and repaired orchestration failures. P01 preserves failed/superseded runtime attempts, the A4 +4.0 s feasibility failure, integration/canonicalization/security failures and the final zero-invalid/zero-blocker closure. Resolved historical failures are not counted as current blockers, and successful final execution does not erase their evidentiary value.

## 48. Cumulative Limitation Register

| Limitation | Origin | Meaning | Blocking? |
| --- | --- | --- | --- |
| P00-LIM-001 | P00 | Portable registry-resolved cross-version dependency lock remained incomplete; portability beyond the exact verified local snapshot is not established. | False |
| P00-LIM-002 | P00 | P00 reproduction is bound to the exact verified local Python 3.13.5 environment; Python 3.11/3.12 were unavailable in that local analysis environment. | False |
| P00-LIM-003 | P00 | P00 evidence is local-snapshot engineering/reproducibility evidence, not universal environment portability. | False |
| P00-LIM-004 | P00 | P00 is non-empirical Mode B administrative/foundation evidence and cannot establish scientific effectiveness. | False |
| P00-LIM-L0-001 | P00 | P00 Layer 0, Evidence Map, and basic read-only Layer 10 package were completed under the historical P00 workflow; later project workflow is governed by current Governance V6.1 and the cumulative project state. | False |
| PUBLIC_EEG_ONLY | P01 | The empirical substrate is public benchmark/research EEG, not a clinical or deployment population. | False |
| NON_CLINICAL | P01 | No clinical cohort, clinical endpoint, or treatment outcome is present. | False |
| NO_DEPLOYMENT_CLAIM | P01 | P01 does not evaluate deployed real-world control, operational safety, or medical-device behavior. | False |
| PRIVATE_KAGGLE_EXTERNAL_ARTIFACT_ACCESS | P01 | Core and A4 numerical HDF5 artifacts are private Kaggle Datasets. | False |
| A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01 | P01 | A4 R2 was introduced after a real +4.0 s boundary infeasibility was observed. | False |
| ACTUAL_RUNTIME_PYTHON_3_12_13_WITH_COMPATIBILITY_AMENDMENT | P01 | Build Book intended Python 3.11, while accepted Kaggle execution used Python 3.12.13 under a documented compatibility amendment. | False |
| ADAPTIVE_DISK_RESOURCE_AMENDMENT | P01 | Governed amendment P01-L1-KAGGLE-ADAPTIVE-DISK-R1 replaced the legacy 60 GiB preflight with an adaptive measured requirement with 6.0 GiB effective minimum; observed free disk was 18.94 GiB. | False |
| SOURCE_LICENSE_REDISTRIBUTION_CONSTRAINTS | P01 | Source-specific licenses, especially BNCI CC BY-ND, constrain redistribution of raw/derived signal bytes. | False |
| BINARY_MI_BRANCH_SCOPE | P01 | P01 official supervised denominator is left-hand versus right-hand imagery only; rest, feet, tongue, execution, technical and unlabeled online/test events are excluded as defined per source. | False |

## 49. Cumulative Evidence Ceiling

Through P01, lawful project claims are limited to engineering/foundation conformance (P00) and data provenance, identity, integrity, split/leakage contract correctness, preprocessing/window materialization, quality validation, persistence integrity, ablation-foundation readiness and execution reproducibility (P01). The project still lacks evidence for decoder superiority, calibration benefit, A4 performance benefit, IHARQ policy benefit, clinical effectiveness, deployment safety, robustness superiority or embodiment effectiveness.

## 50. Overall Downstream Readiness

| Consumer / activity | Technical readiness | Documentary/evidence readiness | Scientific execution status |
| --- | --- | --- | --- |
| P01 Layer 0 | READY | READY — candidate claims, findings, evidence paths, limitations and negatives supplied | claim review not yet performed |
| P01 Evidence Map | SOURCE_READY | awaits P01 Layer 0 reviewed wording | not a scientific experiment |
| P01 Layer 10 | SOURCE_READY | awaits accepted P01 Evidence Map | read-only rendering not yet performed |
| P02 baseline decoder phase | TECHNICALLY_READY | frozen P01 contract/handoff available | P02 itself not yet executed |
| future A4 comparison | DATA_FOUNDATION_READY | Protocol synchronized; matching profile fixed | effectiveness not yet executed |
| later low-calibration evaluation | POPULATION_IDENTITIES_READY | budgets frozen | performance effect not yet executed |

# PART V — PRE-LAYER-0 GOVERNED HANDOFFS — PRESERVED ANALYSIS-STAGE HISTORY

## 51. Layer 0 Handoff — PRE-LAYER-0 ANALYSIS-STAGE HANDOFF (SUPERSEDED BY EMBEDDED LAYER 0)

**P00 continuity:** P00's seven current qualified claims are already governed under `P00-LAYER0-RELEASE-R2`; they are not reopened by this cumulative report. **P01 active scope:** the P01 candidate/deferred/not-supported register remains exactly the set supplied by the finalized P01 report. Layer 0 must review proposed wording against P01 findings, evidence classes, negative evidence and limitations; it must not infer model or A4 effectiveness from readiness evidence.

| P01 claim | Status entering Layer 0 | Supporting findings | Ceiling | Priority |
| --- | --- | --- | --- | --- |
| P01-CLAIM-CAND-001 | CANDIDATE_FOR_LAYER0_REVIEW | P01-FIND-001 | Data provenance and reproducibility only | HIGH |
| P01-CLAIM-CAND-002 | QUALIFICATION_LIKELY_REQUIRED | P01-FIND-002,P01-FIND-006 | Contract leakage/disjointness correctness | HIGH |
| P01-CLAIM-CAND-003 | CANDIDATE_FOR_LAYER0_REVIEW | P01-FIND-003 | Data materialization closure | HIGH |
| P01-CLAIM-CAND-004 | CANDIDATE_FOR_LAYER0_REVIEW | P01-FIND-004 | Retrieval/storage reproducibility | MEDIUM |
| P01-CLAIM-CAND-005 | QUALIFICATION_LIKELY_REQUIRED | P01-FIND-005 | Quality annotation and hard-validity closure | MEDIUM |
| P01-CLAIM-CAND-006 | CANDIDATE_FOR_LAYER0_REVIEW | P01-FIND-008 | Foundation readiness only | HIGH |
| P01-CLAIM-CAND-007 | QUALIFICATION_LIKELY_REQUIRED | P01-FIND-009,P01-FIND-010 | Future A4 substrate readiness; not A4 effectiveness | HIGH |
| P01-CLAIM-CAND-008 | CANDIDATE_FOR_LAYER0_REVIEW | P01-FIND-012 | Execution/reproducibility closure | HIGH |
| P01-CLAIM-CAND-009 | QUALIFICATION_LIKELY_REQUIRED | P01-FIND-011 | Execution reproducibility | MEDIUM |
| P01-CLAIM-CAND-010 | CANDIDATE_FOR_LAYER0_REVIEW | P01-FIND-014 | Downstream technical readiness | HIGH |
| P01-CLAIM-CAND-011 | NOT_SUPPORTED_BY_P01 | P01-FIND-009 | Not claimable from P01 | HIGH |
| P01-CLAIM-CAND-012 | NOT_SUPPORTED_BY_P01 | P01-FIND-001,P01-FIND-012 | Not claimable from P01 | HIGH |

## 52. Evidence Map Handoff

P00 has an accepted historical Evidence Map release. For P01, stable finding/claim IDs, stage/record/artifact paths, external pointers, limitation tags and figure/table source identities are ready. Final P01 manuscript mappings must wait for Layer 0 reviewed claim versions.

## 53. Layer 10 Source Handoff

P00's basic read-only package is historical continuity only. P01 Layer 10 may later render the saved dataset inventory, split, denominator, quality, A0–A13 readiness, A4 chronology, repair chronology, gate closure, external-artifact and limitation surfaces. It must not recompute hidden evidence or strengthen claim wording.

## 54. P02 Technical Handoff

P02 may consume the exact P01 core Dataset pointer, `config_id=d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f`, subject-grouped SplitRecord, LabelMapRecords, PreprocessingRecord and the official +0.5→+3.5 s / 480-sample core profile. Where A4 is explicitly invoked, it must use `A4_LONG_MATCHED_3P5S_R2` and `A4_MULTI_3X2S_UNIFORM_0P75S_R2` with the frozen parent-event matching. Silent relabeling, rewindowing, split mutation, denominator substitution, A4 substitution and test leakage are prohibited.

# PART VI — PRE-LAYER-0 ANALYSIS READINESS DECISION — PRESERVED HISTORY

## 55. Independent Pre-Layer-0 Readiness Decision — HISTORICAL ANALYSIS FREEZE

The cumulative analytical state through P01 is complete enough for P01 Layer 0. P00 is preserved with its later governance history; P01 has all ten Protocol-required analyses, closed numerical identities, complete failure/repair accounting, bounded interpretations, stable candidate claims, limitations and downstream handoffs. No additional P01 computation is required for the report or Layer-0 intake.

**CUMULATIVE_PHASE_EVIDENCE_RESULTS_INTERPRETATION_THROUGH_P01: PASS — FINALIZED AND FROZEN**

- canonical_report_id: `IHARQ-CUMULATIVE-PHASE-EVIDENCE-RESULTS-INTERPRETATION-THROUGH-P01-R1`
- canonical_revision: `SUCCESSOR_CREATED` — document-architecture consolidation only
- phases represented: `P00, P01`
- dominant analysis phase: `P01`
- P00 preservation: `PASS`
- P01 analysis: `PASS`
- all Protocol-required P01 analyses: `COMPLETE`
- numerical reconciliation: `PASS`
- A0_A13: `COMPLETE`
- A14: `ABSENT_PROHIBITED`
- A4: `FOUNDATION_READINESS_ONLY — NO P01 EFFECTIVENESS CLAIM`
- negative/failed evidence: `PRESERVED`
- candidate claims: `READY_FOR_LAYER0_REVIEW`
- limitations: `COMPLETE`
- inter_level_harmony: `PASS`
- intra_level_harmony: `PASS`
- cross_phase_harmony: `PASS`
- freeze_critical_blockers: `0`
- additional P01 computation required: `NO`
- layer0_readiness: `READY`
- evidence_map_source_readiness: `READY`
- layer10_source_readiness: `READY`

**NEXT GOVERNED STEP: PHASE 1 LAYER 0 CLAIM REVIEW AND DISPOSITION**

## 56. Forward Single-Document Rule

After P02 and each later completed phase, the same cumulative Phase Analysis authority should be extended with a new phase-specific section plus refreshed cumulative synthesis/handoffs. Historical phase-specific reports remain provenance artifacts; only one current cumulative Phase Analysis authority should control at a time.


# PART VII — EMBEDDED LAYER 0 CLAIM GOVERNANCE

> **Layer 0 logical boundary.** Everything in Parts VII–XV is the Layer 0 governance domain embedded into the same canonical file by owner direction. It may govern claim wording/disposition/limitations/eligibility, but it does not change the Phase Analysis measurements, findings, Protocol, execution history, datasets, split, preprocessing, windowing, or source evidence.

> **Integration-only successor.** This R2 revision exists because Layer 0 has been integrated directly into the cumulative analytical authority. The pre-Layer-0 candidate-claim sections above are retained as analytical history. Reviewed claims below are the current downstream claim state.

## L0.1. Authority and Boundaries

Layer 0 governs **claim wording and disposition**. It may approve, qualify, downgrade, defer, reject, block, require limitations, and require safer wording. It may not change measurements, denominators, dataset identities, split assignments, preprocessing, window definitions, run inclusion, execution history, Protocol records, or frozen Phase Analysis findings. If the evidence cannot support a proposed claim, the claim is narrowed, deferred, rejected, or blocked; the evidence is not rewritten.

## L0.2. Evidence Hierarchy

```text
MEASURED RESULT
↓
SUPPORTED INTERPRETATION
↓
CANDIDATE CLAIM
↓
LAYER 0 DISPOSITION
↓
REVIEWED CLAIM TEXT
```

Layer 0 maintains or narrows the semantic strength of candidate wording. It does not upgrade readiness, validation, integrity, or execution evidence into model-effectiveness, clinical, or deployment evidence.

## L0.3. Disposition Vocabulary

| Disposition | Meaning in this authority |
|---|---|
| APPROVED | Directly supported as reviewed; no special proximate qualifier beyond ordinary evidence context. |
| APPROVED_WITH_QUALIFICATIONS | Supported only with explicit scope/limitation wording or proximity requirements. |
| DOWNGRADED | Only a weaker claim is supportable. |
| DEFERRED | Potentially testable later, but not supportable as a current result. |
| REJECTED | Not supported by current evidence and not permitted as an endorsed current result. |
| BLOCKED | Unsafe/invalid/prohibited or unresolved upstream defect prevents disposition. |

## L0.4. Claim-Wording Principles

- Exact finite facts remain exact when fully verified; caution does not require vagueness.
- Causal verbs are used only when causality is established; otherwise wording remains descriptive/contractual.
- Absolute terms such as *all* or *none* are permitted only when bounded to an exact finite registered denominator.
- “Established”, “validated”, and “verified” are always scoped to the actual object/check.
- Candidate claims never become stronger during Layer 0 review.

## L0.5. Limitation Governance

Canonical cumulative limitations are preserved. Claim-specific boundary tags already present in the frozen candidate register are treated as claim-governance controls, not silently promoted into new Protocol limitation identities. A source shorthand (`SOURCE_LICENSE_CONSTRAINTS`) is normalized in reviewed dispositions to the canonical cumulative limitation `SOURCE_LICENSE_REDISTRIBUTION_CONSTRAINTS`; the original candidate history remains unchanged.

## L0.6. Evidence Ceiling Rules

| Evidence domain | Maximum permissible claim | Prohibited inference |
|---|---|---|
| Source provenance | Source identity, provenance, checksum-bound reproducibility | No clinical representativeness or model performance |
| Split/leakage validation | Passed implemented subject-disjointness/leakage checks | No universal guarantee that leakage is impossible |
| Denominator integrity | Exact accepted-event/core-window conservation | No decoder adequacy or statistical-power inference |
| Quality | Annotation/hard-validity closure under registered criteria | No claim that EEG is flawless/artifact-free |
| External persistence | Retrieval/storage/integrity reproducibility under exact provider/hash contract | No universal public-access claim |
| A0-A13 | Layer-1 foundation readiness | No ablation-effectiveness claim |
| A4 R2 | Matched future substrate readiness | No accuracy/AUROC/robustness/effectiveness claim |
| Environment/resources | Recorded execution reproducibility and amendment history | No universal irrelevance of environment differences |
| Stages/gates/tests | Execution/reproducibility closure | No scientific/clinical effectiveness inference |
| Public EEG branch | Non-clinical benchmark/data-foundation evidence | No clinical effectiveness, patient benefit, deployment safety, or medical-device readiness |

# PART VIII — P00 LAYER 0 CONTINUITY

## L0.7. P00 Prior Layer 0 State

P00 is preserved as the governed engineering/foundation predecessor, not re-adjudicated. Its current claim-facing state uses the Layer-0-corrected P00 analytical lineage and `P00-LAYER0-RELEASE-R2`. The P00 analysis release remained unchanged when the historical displayed test denominator was corrected from 92 to 102. P01 evidence does not invalidate these engineering/foundation claims.

## L0.8. P00 Preserved Reviewed Claims

| Prior claim | Prior disposition | Finding(s) | Ceiling | Current reviewed wording | Limitations | P01 invalidation? | Cumulative status |
|---|---|---|---|---|---|---|---|
| P00-CLM-001/v2 | APPROVED_WITH_QUALIFICATIONS | P00-F-001 | ENGINEERING_FOUNDATION_CONFORMANCE | Under the exact registered local snapshot and verified Python 3.13.5 environment, all 19 registered Phase 0 engineering/foundation conformance cells passed; this is non-empirical Mode B evidence and does not establish scientific effectiveness or Phase 0 closure. | P00-LIM-002; P00-LIM-003; P00-LIM-004; P00-LIM-L0-001 | No | PRESERVED_PRIOR_DISPOSITION |
| P00-CLM-002/v2 | APPROVED_WITH_QUALIFICATIONS | P00-F-002 | ENGINEERING_FOUNDATION_CONFORMANCE | In the frozen local Python 3.13.5 environment, the complete registered deterministic suite passed 102 of 102 tests; cross-version portability is not established. | P00-LIM-001; P00-LIM-002; P00-LIM-003; P00-LIM-004 | No | PRESERVED_PRIOR_DISPOSITION |
| P00-CLM-003/v2 | APPROVED_WITH_QUALIFICATIONS | P00-F-003; P00-F-004 | VALIDATION_EVIDENCE | Within the registered non-empirical fixture inventory, all 19 valid or integrated bundles were accepted and all 178 intentionally malformed categories were rejected as expected, with zero false valid rejections and zero false malformed acceptances. | P00-LIM-004; P00-LIM-L0-001 | No | PRESERVED_PRIOR_DISPOSITION |
| P00-CLM-004/v2 | APPROVED_WITH_QUALIFICATIONS | P00-F-005 | ARTIFACT_CLOSURE | The frozen Phase 0 package contains and validates the registered foundation inventories of 85 schemas, 35 configuration profiles, and 79 record-family profiles; inventory closure does not establish later-phase scientific effectiveness. | P00-LIM-004; P00-LIM-L0-001 | No | PRESERVED_PRIOR_DISPOSITION |
| P00-CLM-005/v2 | APPROVED_WITH_QUALIFICATIONS | P00-F-006 | FOUNDATION_INTEGRATION | All eleven Layer 0–10 foundation interfaces passed the registered Phase 0 integration scope; no later-phase scientific execution or effectiveness result is claimed. | P00-LIM-003; P00-LIM-004; P00-LIM-L0-001 | No | PRESERVED_PRIOR_DISPOSITION |
| P00-CLM-006/v2 | APPROVED_WITH_QUALIFICATIONS | P00-F-007 | CONTRACT_READINESS | The P00 implementation foundation is complete within its registered local scope, and P01–P15 reusable contract surfaces are ready for later governed annex creation and execution; future empirical outputs have not been produced. | P00-LIM-003; P00-LIM-004; P00-LIM-L0-001 | No | PRESERVED_PRIOR_DISPOSITION |
| P00-CLM-007/v2 | APPROVED_WITH_QUALIFICATIONS | P00-F-008 | LOCAL_REPRODUCIBILITY | The package reproduced from a clean isolated copy under the exact verified Python 3.13.5 and 22-distribution local dependency snapshot; portable cross-version reproducibility is not established. | P00-LIM-001; P00-LIM-002; P00-LIM-003 | No | PRESERVED_PRIOR_DISPOSITION |

## L0.9. P00 Limitations

P00 limitations remain engineering/reproducibility limitations: exact local environment binding, incomplete cross-version portability, non-empirical Mode-B evidence scope, and historical workflow boundaries. P01 does not retroactively transform P00 engineering evidence into empirical-effectiveness evidence.

## L0.10. P00 Current Validity

All seven P00 current claim versions remain `PRESERVED_PRIOR_DISPOSITION` / `APPROVED_WITH_QUALIFICATIONS`. Their later Evidence Map and basic read-only Layer 10 status remains provenance context. This cumulative Layer 0 authority does not reopen or strengthen them.

# PART IX — P01 LAYER 0 REVIEW INPUT

## L0.11. P01 Analytical State

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

## L0.12. P01 Findings

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

## L0.13. P01 Candidate Claims

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

## L0.14. P01 Limitations

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

## L0.15. P01 Negative Evidence

- The original +0.0→+4.0 s A4 proposal is a **negative feasibility result** for one real boundary event; it is not hidden.
- The historical Stage 07, Stage 18, and Stage 26 defects were fail-closed, repaired, and closed in the affected scope; they are not current blockers.
- `P01-CLAIM-CAND-011` has no P01 effectiveness evidence.
- `P01-CLAIM-CAND-012` exceeds P01’s public/non-clinical/deployment evidence ceiling.

## L0.16. P01 Evidence Ceilings

P01 may support provenance, data integrity, split integrity, preprocessing execution, denominator closure, registered quality validity, leakage checks under implemented rules, artifact integrity, A0–A13 foundation readiness, A4 substrate readiness, execution reproducibility, and technical downstream readiness. P01 alone may not support decoder superiority, clinical effectiveness, deployment safety, A4 performance benefit, low-calibration benefit, later robustness effects, or embodiment/control effects.

# PART X — P01 CLAIM-BY-CLAIM LAYER 0 REVIEW

## L0.17. P01-CLAIM-CAND-001 → P01-CLM-001/v1

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

## L0.18. P01-CLAIM-CAND-002 → P01-CLM-002/v1

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

## L0.19. P01-CLAIM-CAND-003 → P01-CLM-003/v1

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

## L0.20. P01-CLAIM-CAND-004 → P01-CLM-004/v1

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

## L0.21. P01-CLAIM-CAND-005 → P01-CLM-005/v1

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

## L0.22. P01-CLAIM-CAND-006 → P01-CLM-006/v1

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

## L0.23. P01-CLAIM-CAND-007 → P01-CLM-007/v1

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

## L0.24. P01-CLAIM-CAND-008 → P01-CLM-008/v1

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

## L0.25. P01-CLAIM-CAND-009 → P01-CLM-009/v1

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

## L0.26. P01-CLAIM-CAND-010 → P01-CLM-010/v1

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

## L0.27. P01-CLAIM-CAND-011 → P01-CLM-011/v1

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

## L0.28. P01-CLAIM-CAND-012 → P01-CLM-012/v1

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

# PART XI — P01 LAYER 0 DISPOSITION REGISTERS

## L0.29. Approved Claims

| Reviewed claim | Disposition | Canonical reviewed wording | Ceiling |
|---|---|---|---|
| P01-CLM-003/v1 | APPROVED | Under the frozen official core-window policy, all 12,910 accepted events yielded 12,910 valid core windows, with 0/12,910 invalid official core windows. | DATA_MATERIALIZATION_CLOSURE |
| P01-CLM-008/v1 | APPROVED | The accepted P01 execution completed 27/27 registered stages, 16/16 deterministic P01 gates, and 50/50 regression tests with 0 unresolved blockers; final execution-bundle integrity checks also closed. | EXECUTION_REPRODUCIBILITY_CLOSURE |

## L0.30. Qualified Claims

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

## L0.31. Downgraded Claims

No P01 candidate required a separate `DOWNGRADED` disposition. Where safer wording was required, the core proposition remained supportable and was handled as `APPROVED_WITH_QUALIFICATIONS` rather than pretending that semantic content had been lost.

## L0.32. Deferred Claims

| Reviewed claim | Claim concept | Reason deferred | Future evidence required | Current permitted wording |
|---|---|---|---|---|
| P01-CLM-011/v1 | A4 R2 improves decoder performance relative to the core window. | P01 contains no A4 effectiveness experiment. | Reconsider only after a Protocol-authorized matched A4 effectiveness experiment with downstream model evidence. | P01 did not evaluate whether A4 R2 improves decoder performance relative to the core window; that effectiveness question remains deferred to a future governed matched downstream experiment. |

## L0.33. Rejected Claims

| Reviewed claim | Rejected claim concept | Violated ceiling | Reason | Could later evidence reopen? |
|---|---|---|---|---|
| P01-CLM-012/v1 | The P01 data foundation demonstrates clinical effectiveness or deployment safety. | NOT_CLAIMABLE_FROM_P01 | Public non-clinical data/integrity evidence cannot establish clinical effectiveness or deployment safety. | A future claim would require appropriately governed clinical/deployment evidence from later phases; P01 itself cannot support it. |

## L0.34. Blocked Claims

No P01 candidate is left blocked. Unsupported concepts were dispositioned as deferred or rejected because no unresolved upstream defect prevents Layer 0 completion.

## L0.35. Required P01 Disposition Matrix

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

# PART XII — CROSS-CUTTING LAYER 0 CLAIM GOVERNANCE

## L0.36. A0–A13 Claim Governance

Claim-bearing language for A0–A13 is limited to **Layer-1 foundation readiness**. The readiness manifest contains exactly A0 through A13, with `executed_in_p01=false`; no P01 wording may imply effect size, superiority, robustness benefit, calibration benefit, or any other ablation-effectiveness result.

## L0.37. A14 Prohibition

`A14 = ABSENT / PROHIBITED`. No A14 selector, execution result, candidate effectiveness claim, or supported Evidence Map row may be introduced. Mentions of A14 in this authority are prohibition/absence statements only.

## L0.38. A4 Language Governance

**Permitted from P01:** A4 R2 identity; +0.0→+3.5 s matched profile; 560 samples; registered virtual members 0:320, 120:440, 240:560; 12,910/12,910 parent matching; no padding/clipping/fabrication/loss; future substrate readiness.

**Not permitted from P01:** accuracy improvement, AUROC improvement, robustness improvement, decoder superiority, statistical effectiveness, clinical effect, or any wording that retrospectively treats R2 as an originally preregistered effectiveness condition.

Any A4 figure/table caption must state in substance: **“foundation readiness only; effectiveness not evaluated in P01.”**

## L0.39. Clinical / Deployment Language Governance

Words such as *clinical*, *safe*, *effective*, *deployment-ready*, *real-world validated*, *medical*, and *patient benefit* require evidence not present in P01. `PUBLIC_EEG_ONLY`, `NON_CLINICAL`, and `NO_DEPLOYMENT_CLAIM` are mandatory constraints. The rejected P01 clinical/deployment candidate must remain visible in the negative/forbidden claim register to prevent later reintroduction.

## L0.40. Leakage Wording Governance

Permitted wording is bounded to the implemented checks: “the frozen subject-grouped split passed the registered disjointness/leakage checks” or equivalent. Prohibited wording includes “leakage is impossible”, “the split guarantees no leakage”, and other universal assertions.

## L0.41. Reproducibility and Execution Closure

Exact execution-closure facts (27/27 stages, 16/16 gates, 50/50 regression tests, zero unresolved blockers, checksum closure) may be stated directly. They establish deterministic execution/reproducibility closure only. R54 is a packaging/security repair and is not a scientific-effect limitation.

## L0.42. External Artifact Access

The core and A4 numerical artifacts are private Kaggle Datasets. Reviewed wording may claim exact provider/version/hash-governed retrieval and integrity, but must not imply unrestricted public byte access. Source-specific redistribution constraints remain active.

## L0.43. Causal, Absolute, and Validation-Language Audit

No reviewed P01 claim uses unsupported causal performance language. Exact absolutes are retained only where finite denominators prove them, such as 12,910/12,910 and 27/27. “Established” and “verified” are tied to source identity, data substrate, registered checks, or execution closure—not to unmeasured effectiveness.

# PART XIII — CUMULATIVE GOVERNED CLAIM STATE THROUGH P01

## L0.44. Cumulative Permitted Claim Register

The current cumulative supported claim state consists of the seven preserved P00 qualified claim versions plus ten P01 reviewed claims permitted as `APPROVED` or `APPROVED_WITH_QUALIFICATIONS`. P00 claims remain engineering/foundation claims; P01 claims are public-data provenance, integrity, validation, readiness, and execution/reproducibility claims.

### P01 permitted claims

| Reviewed claim | Disposition | Reviewed wording | Ceiling |
|---|---|---|---|
| P01-CLM-001/v1 | APPROVED_WITH_QUALIFICATIONS | Within the frozen P01 binary motor-imagery branch, Phase 1 established a checksum-bound, provenance-traceable foundation over the three activated public EEG datasets. | DATA_PROVENANCE_REPRODUCIBILITY |
| P01-CLM-002/v1 | APPROVED_WITH_QUALIFICATIONS | The frozen P01 split assigned 172 subject groups wholly and disjointly across train, calibration, validation, and test roles and passed the implemented registered leakage/disjointness checks; this does not prove that every conceivable leakage mechanism is impossible. | IMPLEMENTED_SPLIT_AND_LEAKAGE_CHECKS |
| P01-CLM-003/v1 | APPROVED | Under the frozen official core-window policy, all 12,910 accepted events yielded 12,910 valid core windows, with 0/12,910 invalid official core windows. | DATA_MATERIALIZATION_CLOSURE |
| P01-CLM-004/v1 | APPROVED_WITH_QUALIFICATIONS | The official P01 core numerical artifact was persisted as 172 lossless HDF5 subject shards covering 12,910 windows and was verified under its Kaggle provider-version/logical-revision/manifest-hash identity contract. | RETRIEVAL_STORAGE_INTEGRITY_REPRODUCIBILITY |
| P01-CLM-005/v1 | APPROVED_WITH_QUALIFICATIONS | P01 applied the ANNOTATE_NOT_REPAIR quality policy across 489 quality summaries: 20 soft/provider flags were retained, 0/489 summaries were hard-invalid, and 0/12,910 official core windows were invalid under the registered criteria. | QUALITY_ANNOTATION_AND_HARD_VALIDITY_CLOSURE |
| P01-CLM-006/v1 | APPROVED_WITH_QUALIFICATIONS | P01 established Layer-1 foundation readiness for each official A0-A13 identity; none of these ablation-effectiveness experiments was executed in P01, and A14 remained absent/prohibited. | FOUNDATION_READINESS_ONLY |
| P01-CLM-007/v1 | APPROVED_WITH_QUALIFICATIONS | P01 established a fully matched A4 R2 Layer-1 data substrate for future governed evaluation: 12,910/12,910 parent events are represented without padding, clipping, fabricated samples, or parent-event loss. A4 R2 arose after the +4.0 s feasibility failure and was not evaluated for decoder effectiveness in P01. | FUTURE_A4_SUBSTRATE_READINESS |
| P01-CLM-008/v1 | APPROVED | The accepted P01 execution completed 27/27 registered stages, 16/16 deterministic P01 gates, and 50/50 regression tests with 0 unresolved blockers; final execution-bundle integrity checks also closed. | EXECUTION_REPRODUCIBILITY_CLOSURE |
| P01-CLM-009/v1 | APPROVED_WITH_QUALIFICATIONS | The accepted P01 run used Python 3.12.13 under a documented compatibility amendment and the governed adaptive-disk policy P01-L1-KAGGLE-ADAPTIVE-DISK-R1; the accepted records show no change to the frozen datasets, labels, subject split, core preprocessing, core window policy, or 12,910-event denominator attributable to these runtime/resource amendments. | EXECUTION_REPRODUCIBILITY |
| P01-CLM-010/v1 | APPROVED_WITH_QUALIFICATIONS | P01 freezes a technical Layer-1 data contract that P02 may consume using the recorded dataset, label-map, split, preprocessing, core-window, and external-artifact identities; silent relabeling, rewindowing, split mutation, denominator substitution, or test-visibility leakage is prohibited. This is technical readiness, not evidence of P02 scientific success. | DOWNSTREAM_TECHNICAL_DATA_CONTRACT_READINESS |

## L0.45. Cumulative Limitations

P00 limitations remain attached to P00 claims. P01 limitations are attached claim-by-claim through the limitation-coverage matrix. The most consequential cumulative restrictions through P01 are: non-clinical/public-EEG scope; no deployment claim; no model-effect inference from P01; readiness is not effectiveness; A4 R2 is retrospective-feasibility-origin substrate readiness only; private external-artifact access and source-license redistribution rules; and exact environment/resource-amendment disclosure for reproduction.

## L0.46. Cumulative Claim Ceilings

| Evidence domain | Maximum permissible claim | Prohibited inference |
|---|---|---|
| Source provenance | Source identity, provenance, checksum-bound reproducibility | No clinical representativeness or model performance |
| Split/leakage validation | Passed implemented subject-disjointness/leakage checks | No universal guarantee that leakage is impossible |
| Denominator integrity | Exact accepted-event/core-window conservation | No decoder adequacy or statistical-power inference |
| Quality | Annotation/hard-validity closure under registered criteria | No claim that EEG is flawless/artifact-free |
| External persistence | Retrieval/storage/integrity reproducibility under exact provider/hash contract | No universal public-access claim |
| A0-A13 | Layer-1 foundation readiness | No ablation-effectiveness claim |
| A4 R2 | Matched future substrate readiness | No accuracy/AUROC/robustness/effectiveness claim |
| Environment/resources | Recorded execution reproducibility and amendment history | No universal irrelevance of environment differences |
| Stages/gates/tests | Execution/reproducibility closure | No scientific/clinical effectiveness inference |
| Public EEG branch | Non-clinical benchmark/data-foundation evidence | No clinical effectiveness, patient benefit, deployment safety, or medical-device readiness |

## L0.47. Forbidden / Unsupported Claim Register

| Claim concept | Reason prohibited/deferred | Source / reviewed claim | Status | Future condition to reconsider |
|---|---|---|---|---|
| A4 improves decoder performance | No P01 effectiveness experiment exists | P01-CLAIM-CAND-011 | DEFERRED | Protocol-authorized matched downstream A4 effectiveness experiment |
| P01 demonstrates clinical effectiveness or deployment safety | PUBLIC_EEG_ONLY + NON_CLINICAL + NO_DEPLOYMENT_CLAIM | P01-CLAIM-CAND-012 | REJECTED | Appropriately governed future clinical/deployment evidence; P01 remains non-clinical |
| P01 proves leakage is impossible | Implemented checks cannot establish universal absence | P01-CLM-002/v1 | PROHIBITED_STRONGER_WORDING | Wording must remain tied to tested checks |
| P01 EEG is flawless/artifact-free | Soft/provider flags exist and zero hard-invalid is criterion-bounded | P01-CLM-005/v1 | PROHIBITED_STRONGER_WORDING | Different validated quality authority would be required |
| A0-A13 effectiveness is established | Only readiness infrastructure exists in P01 | P01-CLM-006/v1 | PROHIBITED_STRONGER_WORDING | Downstream governed ablation experiments |
| Passing gates proves scientific effectiveness | Gate/test evidence is execution/reproducibility evidence only | P01-CLM-008/v1 | PROHIBITED_STRONGER_WORDING | Later scientific/model evidence |

## L0.48. Cross-Claim Consistency

- Because A4 effectiveness was not executed, no permitted claim implies A4 superiority.
- Because P01 is non-clinical, no permitted cumulative claim implies clinical efficacy or deployment safety.
- Because A0–A13 are readiness-only in P01, no permitted claim implies ablation effectiveness.
- Because leakage evidence is check-bounded, no permitted claim claims universal leakage impossibility.
- Because gates/tests are execution evidence, no permitted claim treats closure as scientific effectiveness.

## L0.49. Cross-Phase Claim Harmony

P00 engineering/foundation claims remain qualified under their historical evidence ceiling. P01 adds empirical public-data/provenance/validation/readiness evidence but does not retroactively upgrade P00 claims into scientific-effectiveness claims. No P01 evidence invalidates the seven current P00 qualified claim versions.

# PART XIV — UPDATED POST-LAYER-0 GOVERNED HANDOFFS

## L0.50. Evidence Map Handoff

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

## L0.51. Layer 10 Eligibility

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

## L0.52. P02 Claim-Boundary Inheritance

P02 inherits the frozen P01 data contract and all relevant P01 claim ceilings. P02 must not treat Layer 0 approval of P01 readiness claims as evidence that models perform well, A4 works better, calibration helps, clinical value exists, or deployment safety has been established. P02 may consume the exact data/split/label/preprocessing/window/pointer identities and must generate its own Protocol-authorized scientific evidence for model claims.

# PART XV — FINAL EMBEDDED LAYER 0 READINESS DECISION

## L0.53. Final Layer 0 Summary

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

## L0.54. Success Decision

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

# ORIGINAL PHASE ANALYSIS APPENDICES — PRESERVED

## Appendix A. Numerical Reconciliation

| Metric | P00 current context | P01 accepted result | Cumulative interpretation |
| --- | --- | --- | --- |
| registered/accepted execution units | 19 P00 engineering cells | 27 P01 stages | both phase-specific execution scopes closed |
| deterministic tests | 102 analysis-release tests | 50 P01 regression tests | do not sum as one test suite; different release scopes |
| datasets | not empirical | 3 | P01 first real-data portfolio |
| subjects | not empirical | 172 dataset-scoped groups | P01 split denominator |
| source files | not empirical | 453 | source-file denominator differs from 489 quality-summary denominator |
| accepted events | not empirical | 12,910 | binary-task accepted event denominator |
| core windows | not empirical | 12,910 | one-to-one accepted-event conservation |
| invalid core windows | not empirical | 0 / 12,910 | hard-validity closure |
| quality summaries | not empirical | 489 | recording/run-level validation units |
| soft/provider flags | not empirical | 20 | annotation, not repaired signal |
| core shards | not empirical | 172 | external core HDF5 subjects |
| A4 matched parents | not empirical | 12,910 / 12,910 | foundation readiness only |
| gates | P00 historical gate family | 16/16 P01 deterministic gates PASS | phase-specific closure |
| execution-bundle checksums | P00 separate package integrity | 13,164/13,164 P01 targets valid | P01 evidence integrity |
| current blockers | P00 historical workflow state superseded/preserved | 0 P01 report/execution blockers | P01 ready for Layer 0 |

## Appendix B. P01 Analysis Contract Crosswalk

| Analysis ID | Purpose | Status |
| --- | --- | --- |
| P01-AC-001 | SOURCE INVENTORY | COMPLETE |
| P01-AC-002 | SPLIT | COMPLETE |
| P01-AC-003 | DENOMINATOR CONSERVATION | COMPLETE |
| P01-AC-004 | QUALITY | COMPLETE |
| P01-AC-005 | LEAKAGE | COMPLETE |
| P01-AC-006 | EXTERNAL ARTIFACTS | COMPLETE |
| P01-AC-007 | ABLATION READINESS | COMPLETE |
| P01-AC-008 | A4 | COMPLETE |
| P01-AC-009 | ENVIRONMENT | COMPLETE |
| P01-AC-010 | GATES / REPAIRS | COMPLETE |

## Appendix C. P01 Detailed Source Appendices

> The following appendix material is preserved from the finalized P01 R1 report to retain full run/gate/ablation/repair/artifact/claim/evidence traceability without creating a competing authority.

## Appendix A. Source Utilization Matrix

| Source | Role | Sections/material inspected | Status |
| --- | --- | --- | --- |
| Governance V6.1 | workflow/document authority | current workflow, report timing, evidence/repair/closure rules | USED_AS_AUTHORITY |
| Master Architecture Specification | phase/layer/ablation scope | Layer 1 and Phase 1 sections; P02 dependency | USED_AS_AUTHORITY |
| Canonical Registry R44 | record/identity authority | Dataset/Label/Split/Preprocessing/Window/Validation semantics | USED_AS_AUTHORITY |
| Execution & Evidence Plan R41 | completion/evidence authority | P01 required outputs/gates/negative evidence/handoffs | USED_AS_AUTHORITY |
| Experiment/Ablation/Evaluation Protocol R42 | scientific fairness/ablation authority | A0–A13, split/leakage/denominator/evidence boundaries | USED_AS_AUTHORITY |
| Phase Execution Playbook R41 | operational/repair authority | stage sequencing and repair/reentry interpretation | USED_AS_AUTHORITY |
| Method Selection R2 | selection rationale | selected public data/method/platform decisions | USED_AS_AUTHORITY |
| Nuts-and-Bolts R2 | implementation behavior | technical preprocessing/validation/failure behavior | USED_AS_AUTHORITY |
| Phase 0 whole-stack repository | historical/current inherited state | P00 final report, Protocol, handoffs, validation, Evidence Map precedent | USED_AS_HISTORICAL_CONTEXT |
| Phase 0 final requested-document package R2 | direct documentary predecessor | Build Book/Protocol/P00 state and audits | USED_AS_HISTORICAL_CONTEXT |
| Phase 1 Build Book R10 / P01 Annex R4 | pre-run implementation intent | all R2 freezes, gates, persistence and P02 handoff intent | USED |
| Phase_01_Notebook.ipynb | execution chronology | failed/repair/accepted continuation, A4 boundary, R54 final state | USED_AS_EXECUTION_EVIDENCE |
| P01 execution bundle d03f0a7c869d | primary actual evidence | records, reports, pointers, readiness, tests, gates, checksums, handoffs | USED_AS_EXECUTION_EVIDENCE |
| Final cumulative Protocol through P01 R1 | immutable analysis contract | 10 analysis families, evidence ceilings, exact P01/A4 identities | USED_AS_AUTHORITY |
| Phase 1 Report master prompt | report/output/validation specification | required analyses/structure/handoffs/validation | USED |

## Appendix B. Full P01 Analysis Contract Crosswalk

| Analysis ID | Analysis | Unit | Denominator | Aggregation | Ceiling | Report location |
| --- | --- | --- | --- | --- | --- | --- |
| P01-AC-001-SOURCE-INVENTORY | Source inventory/provenance/license/checksum | Dataset/file | all active sources | counts + exact hashes | Data provenance/reproducibility only | Sections 8/18 |
| P01-AC-002-SPLIT | Subject-group split allocation/disjointness | Subject group/window | 172 subjects / 12,910 windows | role counts/disjointness | Split/leakage correctness | Sections 9/20 |
| P01-AC-003-DENOMINATOR | Accepted event/window conservation | Accepted parent event | 12,910 | dataset/role counts | Data-materialization closure | Section 10/23 |
| P01-AC-004-QUALITY | Quality/validation closure | Quality summary/window | 489 summaries / 12,910 windows | flag/hard-invalid counts | Quality annotation/validity | Sections 11/24 |
| P01-AC-005-LEAKAGE | Leakage/visibility checks | Subject/event/window/budget | all memberships | boolean deterministic checks | Absence of detected contract leakage under implemented checks | Sections 12/20 |
| P01-AC-006-EXTERNAL | External persistence/integrity | Artifact/shard/index | core + A4 | version/hash/size/count | Retrieval/storage/integrity reproducibility | Sections 13/25 |
| P01-AC-007-ABLATION-READINESS | A0–A13 readiness/A14 absence | Ablation identity | 14 official identities | readiness disposition | Foundation readiness only | Sections 14/26/27 |
| P01-AC-008-A4 | A4 R2 feasibility/synchronization | Parent event/A4 view | 12,910 parents | matched counts/profile/boundary | Future substrate readiness; not effectiveness | Sections 15/28 |
| P01-AC-009-ENVIRONMENT | Environment/amendments | Execution environment | one accepted environment | versions/resources/amendments | Execution reproducibility | Sections 16/29 |
| P01-AC-010-GATES-REPAIRS | Gate/repair closure | Gate/stage/repair | 16 gates / 27 stages | status/blocker/classification | Execution closure | Sections 17/30–32 |

## Appendix C. Run / Stage Matrix

| Stage | Purpose | Status | Repair history |
| --- | --- | --- | --- |
| P01-STAGE-00 | Corrected bootstrap and persistent isolated worker | PASS | — |
| P01-STAGE-01 | Environment | PASS | — |
| P01-STAGE-02 | Project and input intake | PASS | — |
| P01-STAGE-03 | Authority and configuration | PASS | — |
| P01-STAGE-04 | Phase 0 regression | PASS | — |
| P01-STAGE-05 | Source resolution | PASS | — |
| P01-STAGE-06 | Dataset registry | PASS | — |
| P01-STAGE-07 | Pass 1: verified source acquisition and bounded loading | PASS | Stale R42/R49 revision guard stopped before worker submission; R50 same-session integration repair; final Stage 07 PASS. |
| P01-STAGE-08 | Metadata normalization | PASS | — |
| P01-STAGE-09 | Label mapping | PASS | — |
| P01-STAGE-10 | Preprocessing compilation | PASS | — |
| P01-STAGE-11 | Split construction and frozen fit population | PASS | — |
| P01-STAGE-12 | Low-calibration budgets | PASS | — |
| P01-STAGE-13 | Pass 2A: bounded preprocessing fit | PASS | — |
| P01-STAGE-14 | Adopt verified core and materialize matched A4 R2 | PASS | Core adoption/canonical record-ID normalization plus A4 interface/persistence hardening; R49 A4 R2 materialization; core reused unchanged. |
| P01-STAGE-15 | Validate and commit the separate A4 R2 Dataset | PASS | Separate A4 Dataset committed after exact remote-manifest verification. |
| P01-STAGE-16 | Record validation | PASS | — |
| P01-STAGE-17 | Leakage audit | PASS | — |
| P01-STAGE-18 | A0–A13 readiness | PASS | Missing module/import integration episode; R51–R53 same-session repair chain; final Stage 18 PASS. |
| P01-STAGE-19 | Cards | PASS | — |
| P01-STAGE-20 | Manifests | PASS | — |
| P01-STAGE-21 | Negative register | PASS | — |
| P01-STAGE-22 | P02 and later compatibility | PASS | — |
| P01-STAGE-23 | Evidence sufficiency | PASS | — |
| P01-STAGE-24 | Repair metadata | PASS | — |
| P01-STAGE-25 | Final export preparation | PASS | — |
| P01-STAGE-26 | Terminal decision and bundle export | PASS | Secret scan blocked contaminated package; R54 redacted/repacked without scientific rerun or duplicate Stage-26 identity; final export PASS. |

## Appendix D. Gate Matrix

| Gate | Name | Owner | Status | Blockers | Evidence |
| --- | --- | --- | --- | --- | --- |
| P01-G01 | authority_phase0_intake | GOVERNANCE_AND_PHASE0 | PASS | 0 | manifests/phase_01/test_manifest.json; authority_manifest.json |
| P01-G02 | source_provenance_license | METHOD_SELECTION_AND_OWNER | PASS | 0 | reports/phase_01/sources/source_version_license_report.json; inputs/source_inventory.json |
| P01-G03 | schema_canonical_object | REGISTRY | PASS | 0 | reports/phase_01/validation/; records/ |
| P01-G04 | metadata_completeness | L1_METADATA | PASS | 0 | reports/phase_01/metadata/metadata_completeness.json |
| P01-G05 | label_mapping | L1_LABELS | PASS | 0 | reports/phase_01/labels/label_map_validation.json; records/labels/ |
| P01-G06 | preprocessing_fit_scope | PROTOCOL_AND_L1_PREPROCESSING | PASS | 0 | reports/phase_01/preprocessing/fit_scope.json; records/preprocessing/ |
| P01-G07 | split_disjointness | PROTOCOL_AND_L1_SPLITS | PASS | 0 | reports/phase_01/splits/disjointness.json; records/splits/ |
| P01-G08 | leakage_chronology | PROTOCOL_AND_L1_LEAKAGE | PASS | 0 | reports/phase_01/leakage/leakage_contamination.json |
| P01-G09 | low_calibration_budgets | PROTOCOL_AND_L1_BUDGETS | PASS | 0 | reports/phase_01/splits/low_calibration_budgets.csv |
| P01-G10 | window_identity | L1_WINDOWS | PASS | 0 | reports/phase_01/windows/window_timing_overlap.json; records/windows/ |
| P01-G11 | quality_coverage | L1_QUALITY | PASS | 0 | reports/phase_01/quality/quality_coverage.json; records/quality/ |
| P01-G12 | matched_keys_ablation_readiness | PROTOCOL_AND_L1_READINESS | PASS | 0 | manifests/phase_01/layer1_ablation_readiness_l1_v1.json; reports/phase_01/readiness/matched_key_completeness.csv |
| P01-G13 | cards_limitations | L0_BOUNDARY_AND_L1_CARDS | PASS | 0 | docs/cards/datasets/; docs/cards/protocols/ |
| P01-G14 | manifest_path_hash_closure | BUILD_BOOK_AND_L1_MANIFESTS | PASS | 0 | manifests/phase_01/execution_bundle_manifest.json; checksums.sha256 |
| P01-G15 | phase2_compatibility | BUILD_BOOK_AND_P02_CONSUMER | PASS | 0 | phase2_handoff/phase_01_to_phase_02.yaml |
| P01-G16 | complete_artifact_closure | EXECUTION_PLAN_AND_L1_BUNDLE | PASS | 0 | manifests/phase_01/layer1_manifest.json; phase_execution_handoff.yaml |

## Appendix E. A0–A13 Matrix

| ID | Official identity | Foundation | Executed P01 | Downstream | Limitation |
| --- | --- | --- | --- | --- | --- |
| A0 | Raw Decoder / Accept-All Raw Decoder Reference | FOUNDATION_READY | No | P02-P15 | Layer-1 matching foundation only |
| A1 | Calibrated Decoder / Calibration Visibility | FOUNDATION_READY | No | P02-P15 | Layer-1 matching foundation only |
| A2 | Simple Registered Threshold / Confidence-Threshold Baseline | FOUNDATION_READY | No | P02-P15 | Layer-1 matching foundation only |
| A3 | Uncertainty and Selective Prediction | FOUNDATION_READY | No | P02-P15 | Layer-1 matching foundation only |
| A4 | Longer-Window, Multi-Window Voting/Averaging and Ordinary Ensemble Controls | FOUNDATION_READY | No | P02-P15 | A4 R2 data substrate materialized; confirmatory effectiveness deferred |
| A5 | IHARQ-lite / Rule-Based Evidence Verification | FOUNDATION_READY | No | P02-P15 | Layer-1 matching foundation only |
| A6 | IHARQ + Evidence-Quality Estimator | FOUNDATION_READY | No | P02-P15 | Layer-1 matching foundation only |
| A7 | IHARQ + RegimeRisk Temporal Trust | FOUNDATION_READY | No | P02-P15 | Layer-1 matching foundation only |
| A8 | Learning-to-defer / Deferral Comparison | FOUNDATION_READY | No | P02-P15 | Layer-1 matching foundation only |
| A9 | Supervised Adaptive-IHARQ / Adaptive Readiness Policy | FOUNDATION_READY | No | P02-P15 | Layer-1 matching foundation only |
| A10 | Contextual Bandit / Simulation-Bounded Immediate-Reward Adaptation | FOUNDATION_READY | No | P02-P15 | Layer-1 matching foundation only |
| A11 | Reinforcement-Learning Policy / Simulation-Bounded Sequential Policy Learning | FOUNDATION_READY | No | P02-P15 | Layer-1 matching foundation only |
| A12 | StressForge Stress Tests / Controlled Stress Robustness | FOUNDATION_READY | No | P02-P15 | Layer-1 matching foundation only |
| A13 | Layer 9 Simulation-Only Embodiment Demo | FOUNDATION_READY | No | P02-P15 | Layer-1 matching foundation only |

**A14:** ABSENT / PROHIBITED; absence audit PASS.

## Appendix F. Repair / Rerun Ledger

| Episode | Surface | Root cause | Classification | Scientific effect | Resolution |
| --- | --- | --- | --- | --- | --- |
| R45 | Stage 14/core adoption | Dependency-order record-ID normalization needed for equivalence/adoption | CANONICALIZATION_FIX / IMPLEMENTATION_FIX | No | Existing core adopted after record equivalence + exact remote hash; no core recomputation/reupload |
| R46–R47 | Runtime/canonical serialization | Missing datetime/timezone import; hash-bearing float representation needed governed decimal strings | IMPLEMENTATION_BUG_FIX / CANONICALIZATION_FIX | No | Imports corrected; decimal-string canonicalization restored deterministic identities |
| R48 | A4 child interface/persistence | Child interface/storage identity/resumability issues | IMPLEMENTATION_FIX / PERSISTENCE_FIX | No | A4 interface, reader verification, per-subject checkpoints and exact expected-parent checks hardened |
| R49 | A4 design at Stage 14 | Original +0.0…+4.0 s control infeasible for one valid parent event | SCIENTIFIC_CONTRACT_CHANGE limited to future A4 alternative profile | Yes — A4 alternative only; core unchanged | Replaced proposed A4 R1 with matched +0.0…+3.5 s R2; 12,910/12,910 parents retained; no padding/clipping/drop |
| R50 | Stage 07 | Notebook integration retained stale revision guard | INTEGRATION_FIX | No | Same-session continuation repaired guard; successful earlier work reused |
| R51–R53 | Stage 18 | Bad module import and two recovery-cell integration defects | INTEGRATION_FIX | No | Valid shim/import tested under exact worker environment; Stage 18 rerun once to PASS |
| R54 | Stage 26 release | Live Kaggle credential was serialized into environment evidence; secret scanner correctly blocked release | SECURITY/PACKAGING_FIX | No | Contaminated failed exports deleted, environment values redacted, final ZIPs rebuilt and exact-token scan passed |

## Appendix G. External Artifact Register

| Artifact ID | Provider handle | Provider rev | Logical rev | Format | Count/size | Manifest SHA-256 | Access/retrieval |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473 | csthv999z/iharq-p01-l1-derived-windows-d03f0a7c869d-20260806222242-68a91473 | 2 | 1 | LOSSLESS_HDF5_SUBJECT_SHARDS | 12910 windows; 1,166,652,764 bytes | dc21f418e9a1add62adb346f627d5d729735a5f1ecaa1d771f6fa5cfede627e1 | PRIVATE; exact provider version + manifest + window-to-shard index |
| P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13 | csthv999z/iharq-p01-l1-a4-d03f0a7c-9a7c6108 | 1 | 2 | LOSSLESS_HDF5_MATCHED_3P5S_SUBJECT_SHARDS_WITH_REGISTERED_VIRTUAL_MULTIWINDOW_VIEWS | 12910 stored events; 51640 records; 1,357,362,334 bytes | 29124d59907610b1545e0a2b5d1811a4d4a2bf1df64cad49aa880f4721c47305 | PRIVATE; exact provider version + manifest + A4 indexes |

## Appendix H. Limitation Register

| ID | Scope | Description | Evidence consequence | Claim consequence | Blocking | Downstream |
| --- | --- | --- | --- | --- | --- | --- |
| PUBLIC_EEG_ONLY | P01 and downstream inherited | The empirical substrate is public benchmark/research EEG, not a clinical or deployment population. | Supports public-data provenance and benchmark data-contract claims only. | No clinical generalization or deployment claims. | NO | P02-P15; Layer 0 |
| NON_CLINICAL | Project/P01 | No clinical cohort, clinical endpoint, or treatment outcome is present. | Evidence is non-clinical. | Clinical benefit/effectiveness claims prohibited. | NO | All claim-bearing outputs |
| NO_DEPLOYMENT_CLAIM | Project/P01 | P01 does not evaluate deployed real-world control, operational safety, or medical-device behavior. | Execution validity cannot be extrapolated to deployment safety. | Deployment/safety claims prohibited. | NO | Layer 0 and later deployment-related phases |
| PRIVATE_KAGGLE_EXTERNAL_ARTIFACT_ACCESS | P01 external persistence | Core and A4 numerical HDF5 artifacts are private Kaggle Datasets. | Reproduction requires authorized access plus exact provider revision and manifest-hash verification. | No effect on scientific content, but constrains independent retrieval. | NO | P02-P15 reproducibility |
| A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01 | A4 | A4 R2 was introduced after a real +4.0 s boundary infeasibility was observed. | R2 is frozen prospectively for future downstream use but is not an originally preregistered P01 effectiveness condition. | No A4 effectiveness claim from P01. | NO | P02 A4 and Layer 0 |
| ACTUAL_RUNTIME_PYTHON_3_12_13_WITH_COMPATIBILITY_AMENDMENT | Execution environment | Build Book intended Python 3.11, while accepted Kaggle execution used Python 3.12.13 under a documented compatibility amendment. | Exact reproduction should use actual captured environment or validate equivalence. | No scientific claim consequence when science/config remains unchanged. | NO | Reproduction |
| ADAPTIVE_DISK_RESOURCE_AMENDMENT | Execution resources | Governed amendment `P01-L1-KAGGLE-ADAPTIVE-DISK-R1` replaced the legacy 60 GiB preflight with an adaptive measured requirement with 6.0 GiB effective minimum; observed free disk was 18.94 GiB. | Resource policy differs from pre-run intent but was recorded and fail-safe. | No scientific claim consequence. | NO | Reproduction |
| SOURCE_LICENSE_REDISTRIBUTION_CONSTRAINTS | Dataset persistence | Source-specific licenses, especially BNCI CC BY-ND, constrain redistribution of raw/derived signal bytes. | Bundle carries metadata/hashes/pointers rather than unrestricted raw-data redistribution. | No performance consequence; affects artifact distribution. | NO | Repository/release packaging |
| BINARY_MI_BRANCH_SCOPE | P01 task | P01 official supervised denominator is left-hand versus right-hand imagery only; rest, feet, tongue, execution, technical and unlabeled online/test events are excluded as defined per source. | Results describe the frozen binary task only. | No claims about excluded tasks/classes. | NO | P02-P15 |

## Appendix I. Candidate Claim Register

| ID | Wording | Finding support | Class | Status | Ceiling |
| --- | --- | --- | --- | --- | --- |
| P01-CLAIM-CAND-001 | Phase 1 established a checksum-bound, provenance-traceable three-dataset public EEG foundation for the IHARQ binary motor-imagery branch. | P01-FIND-001 | PROVENANCE_EVIDENCE | CANDIDATE_FOR_LAYER0_REVIEW | Data provenance and reproducibility only |
| P01-CLAIM-CAND-002 | The frozen P01 split is subject-grouped and passed the implemented disjointness and leakage checks. | P01-FIND-002, P01-FIND-006 | VALIDATION_EVIDENCE | QUALIFICATION_LIKELY_REQUIRED | Contract leakage/disjointness correctness |
| P01-CLAIM-CAND-003 | The official Layer-1 pipeline conserved the complete accepted-event denominator: 12,910 accepted events produced 12,910 valid core windows. | P01-FIND-003 | INTEGRITY_EVIDENCE | CANDIDATE_FOR_LAYER0_REVIEW | Data materialization closure |
| P01-CLAIM-CAND-004 | The official core numerical Dataset was persisted as 172 lossless HDF5 subject shards and verified by immutable provider/version/manifest identities. | P01-FIND-004 | INTEGRITY_EVIDENCE | CANDIDATE_FOR_LAYER0_REVIEW | Retrieval/storage reproducibility |
| P01-CLAIM-CAND-005 | P01 quality processing followed an annotate-not-repair policy; 20 soft/provider flags were preserved while no hard-invalid summary or official core window was observed. | P01-FIND-005 | VALIDATION_EVIDENCE | QUALIFICATION_LIKELY_REQUIRED | Quality annotation and hard-validity closure |
| P01-CLAIM-CAND-006 | P01 established the Layer-1 readiness foundation for all official A0–A13 identities while preserving A14 as absent/prohibited. | P01-FIND-008 | READINESS_EVIDENCE | CANDIDATE_FOR_LAYER0_REVIEW | Foundation readiness only |
| P01-CLAIM-CAND-007 | P01 established a 12,910-event fully matched A4 R2 data substrate for future governed evaluation, without padding, clipping, fabrication, or parent-event loss. | P01-FIND-009, P01-FIND-010 | READINESS_EVIDENCE | QUALIFICATION_LIKELY_REQUIRED | Future A4 substrate readiness; not A4 effectiveness |
| P01-CLAIM-CAND-008 | The accepted P01 execution closed all 27 stages, 16 deterministic gates, and 50 regression tests with zero unresolved blockers. | P01-FIND-012 | EXECUTION_EVIDENCE | CANDIDATE_FOR_LAYER0_REVIEW | Execution/reproducibility closure |
| P01-CLAIM-CAND-009 | P01 runtime compatibility and resource amendments preserved the frozen scientific core data contract while recording the actual Python 3.12.13 environment. | P01-FIND-011 | EXECUTION_EVIDENCE | QUALIFICATION_LIKELY_REQUIRED | Execution reproducibility |
| P01-CLAIM-CAND-010 | P01 provides a frozen technical data contract that P02 can consume without silent relabeling, rewindowing, split mutation, denominator substitution, or test leakage. | P01-FIND-014 | READINESS_EVIDENCE | CANDIDATE_FOR_LAYER0_REVIEW | Downstream technical readiness |
| P01-CLAIM-CAND-011 | A4 R2 improves decoder performance relative to the core window. | P01-FIND-009 | READINESS_EVIDENCE | NOT_SUPPORTED_BY_P01 | Not claimable from P01 |
| P01-CLAIM-CAND-012 | The P01 data foundation demonstrates clinical effectiveness or deployment safety. | P01-FIND-001, P01-FIND-012 | EXECUTION_EVIDENCE | NOT_SUPPORTED_BY_P01 | Not claimable from P01 |

## Appendix J. Evidence Crosswalk

| Finding | Candidate claims | Canonical evidence paths | Limitation |
| --- | --- | --- | --- |
| P01-FIND-001 | P01-CLAIM-CAND-001, P01-CLAIM-CAND-012 | records/datasets/*/*.json; reports/phase_01/sources/source_version_license_report.json | PUBLIC_EEG_ONLY; source-license/redistribution restrictions apply. |
| P01-FIND-002 | P01-CLAIM-CAND-002 | records/splits/P01-L1-SPLIT-OFFICIAL-R2/IHARQ-SPLITRECORD-20260806-e4e371d332c61e36.json; reports/phase_01/splits/disjointness.json | This establishes contract disjointness, not universal absence of every conceivable leakage mechanism. |
| P01-FIND-003 | P01-CLAIM-CAND-003 | records/windows/; external_artifact_pointers/derived_windows_dataset.json | Does not imply decoder adequacy or statistical power. |
| P01-FIND-004 | P01-CLAIM-CAND-004 | reports/phase_01/storage/existing_core_dataset_adoption.json; external_artifact_pointers/derived_windows_dataset.json | Private Kaggle access is required; source licenses continue to govern redistribution. |
| P01-FIND-005 | P01-CLAIM-CAND-005 | reports/phase_01/quality/quality_coverage.json; records/quality/ | A soft flag is not proof of physiological corruption, and zero hard-invalid cases is not a claim of artifact-free EEG. |
| P01-FIND-006 | P01-CLAIM-CAND-002 | reports/phase_01/splits/disjointness.json; reports/phase_01/leakage/leakage_contamination.json | Bounded to implemented checks and frozen identities. |
| P01-FIND-007 | — | reports/phase_01/splits/low_calibration_budgets.csv | No calibration-performance experiment was executed in P01. |
| P01-FIND-008 | P01-CLAIM-CAND-006 | manifests/phase_01/layer1_ablation_readiness_l1_v1.json | Foundation readiness is not ablation effectiveness. |
| P01-FIND-009 | P01-CLAIM-CAND-007, P01-CLAIM-CAND-011 | external_artifact_pointers/a4_window_family_dataset.json; reports/phase_01/storage/a4_derived_output_storage_actual_precommit.json | A4 effectiveness was not executed or measured in P01; R2 arose after feasibility evidence. |
| P01-FIND-010 | P01-CLAIM-CAND-007 | Phase_01_Notebook.ipynb (R49 A4 boundary explanation); config_snapshot/p01_l1_a4_window_family_freeze_R2.json | This is a design-feasibility result, not evidence that R2 performs better than R1 or core. |
| P01-FIND-011 | P01-CLAIM-CAND-009 | environment_manifest.json; environment_amendment.json | Reproduction should use the recorded actual environment rather than the original Python 3.11 intent. |
| P01-FIND-012 | P01-CLAIM-CAND-008, P01-CLAIM-CAND-012 | reports/phase_01/tests/stage_results.json; gate_decision.json; reports/phase_01/tests/phase0_and_runtime_regression.json; checksums.sha256 | Execution closure does not imply model or clinical effectiveness. |
| P01-FIND-013 | — | reports/phase_01/worker_logs/; reports/phase_01/repair_reentry.json; reports/phase_01/runtime/r54_final_export_secret_redaction.json | The repair history must remain visible; it is not evidence of scientific superiority. |
| P01-FIND-014 | P01-CLAIM-CAND-010 | phase2_handoff/phase_01_to_phase_02.yaml; handoffs/phase_01_to_phase_02.yaml | Formal phase transition still follows the documentary closure sequence. |

## Appendix K. Final Report Validation Declaration

The final package validation artifacts independently record section coverage, analysis-contract coverage, numerical reconciliation, A0–A13/no-A14 integrity, A4 no-post-hoc wording, evidence-ceiling checks, source utilization, machine-readable parity, secret/placeholder scanning, DOCX parity/render QA, checksums and ZIP integrity.

**PHASE_01_EVIDENCE_RESULTS_INTERPRETATION_REPORT: PASS — FINALIZED**

- P01 execution: **ACCEPTED**
- Protocol v1.0 through P01: **FROZEN**
- Phase 1 Report: **FINALIZED**
- additional P01 computation: **NOT REQUIRED**
- unresolved report blockers: **0**
- candidate claims: **READY FOR LAYER 0 REVIEW**
- Evidence Map inputs: **READY**
- Layer 10 source inputs: **READY**
- next governed step: **PHASE 1 LAYER 0 CLAIM REVIEW AND DISPOSITION**

This is a report-completion decision, not a declaration that the entire Phase 1 governance lifecycle is closed.

## Appendix D. P00 Current Claim-Governance Register

| Claim version | Finding(s) | Decision | Ceiling | Required limitations |
| --- | --- | --- | --- | --- |
| P00-CLM-001/v2 | P00-F-001 | APPROVE_WITH_QUALIFICATIONS | ENGINEERING_FOUNDATION_CONFORMANCE | P00-LIM-002,P00-LIM-003,P00-LIM-004,P00-LIM-L0-001 |
| P00-CLM-002/v2 | P00-F-002 | APPROVE_WITH_QUALIFICATIONS | ENGINEERING_FOUNDATION_CONFORMANCE | P00-LIM-001,P00-LIM-002,P00-LIM-003,P00-LIM-004 |
| P00-CLM-003/v2 | P00-F-003,P00-F-004 | APPROVE_WITH_QUALIFICATIONS | VALIDATION_EVIDENCE | P00-LIM-004,P00-LIM-L0-001 |
| P00-CLM-004/v2 | P00-F-005 | APPROVE_WITH_QUALIFICATIONS | ARTIFACT_CLOSURE | P00-LIM-004,P00-LIM-L0-001 |
| P00-CLM-005/v2 | P00-F-006 | APPROVE_WITH_QUALIFICATIONS | FOUNDATION_INTEGRATION | P00-LIM-003,P00-LIM-004,P00-LIM-L0-001 |
| P00-CLM-006/v2 | P00-F-007 | APPROVE_WITH_QUALIFICATIONS | CONTRACT_READINESS | P00-LIM-003,P00-LIM-004,P00-LIM-L0-001 |
| P00-CLM-007/v2 | P00-F-008 | APPROVE_WITH_QUALIFICATIONS | LOCAL_REPRODUCIBILITY | P00-LIM-001,P00-LIM-002,P00-LIM-003 |

## Appendix E. Cumulative Candidate Claim Register

| Claim | Origin | Current status | Finding(s) | Ceiling |
| --- | --- | --- | --- | --- |
| P00-CLM-001/v2 | P00 | ALREADY_DISPOSITIONED_IN_P00_LAYER0 | P00-F-001 | ENGINEERING_FOUNDATION_CONFORMANCE |
| P00-CLM-002/v2 | P00 | ALREADY_DISPOSITIONED_IN_P00_LAYER0 | P00-F-002 | ENGINEERING_FOUNDATION_CONFORMANCE |
| P00-CLM-003/v2 | P00 | ALREADY_DISPOSITIONED_IN_P00_LAYER0 | P00-F-003,P00-F-004 | VALIDATION_EVIDENCE |
| P00-CLM-004/v2 | P00 | ALREADY_DISPOSITIONED_IN_P00_LAYER0 | P00-F-005 | ARTIFACT_CLOSURE |
| P00-CLM-005/v2 | P00 | ALREADY_DISPOSITIONED_IN_P00_LAYER0 | P00-F-006 | FOUNDATION_INTEGRATION |
| P00-CLM-006/v2 | P00 | ALREADY_DISPOSITIONED_IN_P00_LAYER0 | P00-F-007 | CONTRACT_READINESS |
| P00-CLM-007/v2 | P00 | ALREADY_DISPOSITIONED_IN_P00_LAYER0 | P00-F-008 | LOCAL_REPRODUCIBILITY |
| P01-CLAIM-CAND-001 | P01 | CANDIDATE_FOR_LAYER0_REVIEW | P01-FIND-001 | Data provenance and reproducibility only |
| P01-CLAIM-CAND-002 | P01 | QUALIFICATION_LIKELY_REQUIRED | P01-FIND-002,P01-FIND-006 | Contract leakage/disjointness correctness |
| P01-CLAIM-CAND-003 | P01 | CANDIDATE_FOR_LAYER0_REVIEW | P01-FIND-003 | Data materialization closure |
| P01-CLAIM-CAND-004 | P01 | CANDIDATE_FOR_LAYER0_REVIEW | P01-FIND-004 | Retrieval/storage reproducibility |
| P01-CLAIM-CAND-005 | P01 | QUALIFICATION_LIKELY_REQUIRED | P01-FIND-005 | Quality annotation and hard-validity closure |
| P01-CLAIM-CAND-006 | P01 | CANDIDATE_FOR_LAYER0_REVIEW | P01-FIND-008 | Foundation readiness only |
| P01-CLAIM-CAND-007 | P01 | QUALIFICATION_LIKELY_REQUIRED | P01-FIND-009,P01-FIND-010 | Future A4 substrate readiness; not A4 effectiveness |
| P01-CLAIM-CAND-008 | P01 | CANDIDATE_FOR_LAYER0_REVIEW | P01-FIND-012 | Execution/reproducibility closure |
| P01-CLAIM-CAND-009 | P01 | QUALIFICATION_LIKELY_REQUIRED | P01-FIND-011 | Execution reproducibility |
| P01-CLAIM-CAND-010 | P01 | CANDIDATE_FOR_LAYER0_REVIEW | P01-FIND-014 | Downstream technical readiness |
| P01-CLAIM-CAND-011 | P01 | NOT_SUPPORTED_BY_P01 | P01-FIND-009 | Not claimable from P01 |
| P01-CLAIM-CAND-012 | P01 | NOT_SUPPORTED_BY_P01 | P01-FIND-001,P01-FIND-012 | Not claimable from P01 |

## Appendix F. Cumulative Limitation Register

| Limitation | Origin | Blocking | Meaning |
| --- | --- | --- | --- |
| P00-LIM-001 | P00 | False | Portable registry-resolved cross-version dependency lock remained incomplete; portability beyond the exact verified local snapshot is not established. |
| P00-LIM-002 | P00 | False | P00 reproduction is bound to the exact verified local Python 3.13.5 environment; Python 3.11/3.12 were unavailable in that local analysis environment. |
| P00-LIM-003 | P00 | False | P00 evidence is local-snapshot engineering/reproducibility evidence, not universal environment portability. |
| P00-LIM-004 | P00 | False | P00 is non-empirical Mode B administrative/foundation evidence and cannot establish scientific effectiveness. |
| P00-LIM-L0-001 | P00 | False | P00 Layer 0, Evidence Map, and basic read-only Layer 10 package were completed under the historical P00 workflow; later project workflow is governed by current Governance V6.1 and the cumulative project state. |
| PUBLIC_EEG_ONLY | P01 | False | The empirical substrate is public benchmark/research EEG, not a clinical or deployment population. |
| NON_CLINICAL | P01 | False | No clinical cohort, clinical endpoint, or treatment outcome is present. |
| NO_DEPLOYMENT_CLAIM | P01 | False | P01 does not evaluate deployed real-world control, operational safety, or medical-device behavior. |
| PRIVATE_KAGGLE_EXTERNAL_ARTIFACT_ACCESS | P01 | False | Core and A4 numerical HDF5 artifacts are private Kaggle Datasets. |
| A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01 | P01 | False | A4 R2 was introduced after a real +4.0 s boundary infeasibility was observed. |
| ACTUAL_RUNTIME_PYTHON_3_12_13_WITH_COMPATIBILITY_AMENDMENT | P01 | False | Build Book intended Python 3.11, while accepted Kaggle execution used Python 3.12.13 under a documented compatibility amendment. |
| ADAPTIVE_DISK_RESOURCE_AMENDMENT | P01 | False | Governed amendment P01-L1-KAGGLE-ADAPTIVE-DISK-R1 replaced the legacy 60 GiB preflight with an adaptive measured requirement with 6.0 GiB effective minimum; observed free disk was 18.94 GiB. |
| SOURCE_LICENSE_REDISTRIBUTION_CONSTRAINTS | P01 | False | Source-specific licenses, especially BNCI CC BY-ND, constrain redistribution of raw/derived signal bytes. |
| BINARY_MI_BRANCH_SCOPE | P01 | False | P01 official supervised denominator is left-hand versus right-hand imagery only; rest, feet, tongue, execution, technical and unlabeled online/test events are excluded as defined per source. |

## Appendix G. Source Utilization Matrix

| Source | Role | Use | Status |
| --- | --- | --- | --- |
| Governance V6.1 | workflow/document authority | P00/P01/cumulative boundaries; evidence sufficiency; downstream order | USED_AS_AUTHORITY |
| Master Architecture Specification | system/phase/layer/A-ID authority | P00 foundation role; P01 empirical anchor role; P02 dependencies | USED_AS_AUTHORITY |
| Canonical Artifact, Record, and Interface Registry | record/status/identity/lineage authority | P00 schema/identity foundation; P01 Dataset/Label/Split/Preprocessing/Window records | USED_AS_AUTHORITY |
| Execution and Evidence Plan | evidence/completeness/gate authority | P00 foundation closure; P01 gates, required artifacts, negative evidence | USED_AS_AUTHORITY |
| Experiment, Ablation, and Evaluation Protocol v0.1 + finalized cumulative Protocol v1.0 | analysis/fairness/denominator authority | P00 historical ceiling; exact ten P01 analyses; A0–A13; no-A14; A4 R2 | USED_AS_AUTHORITY |
| Complete Phase Execution Playbook | execution/repair/handoff procedure | P00/P01 repair and downstream workflow | USED_AS_AUTHORITY |
| Integrated Layers 0–10 Method Selection Register | selected methods/data/platform rationale | P01 source/method rationale; downstream ownership | USED_AS_AUTHORITY |
| Integrated Layers 0–10 Nuts-and-Bolts Specification | implementation/validator/failure behavior | technical interpretation of P00 infrastructure and P01 L1 pipeline | USED_AS_AUTHORITY |
| Phase 0 implementation/execution state | historical engineering evidence | 19 cells, 102-test analysis-release inventory, schemas/configs/records, repair history | USED_AS_HISTORICAL_CONTEXT |
| Phase 0 Analysis R3 Layer0-corrected + analysis release R2 | current P00 analytical history | 9 findings; corrected P00-F-002 denominator; non-empirical ceiling | USED_AS_HISTORICAL_CONTEXT |
| P00 Layer 0 / Evidence Map / basic Layer 10 final audit | post-report P00 claim governance | 7 current qualified claim versions v2; accepted map/read-only outputs; analysis release unchanged | USED_AS_HISTORICAL_CONTEXT |
| Phase 1 Implementation Build Book R10 / P01 Annex R4 | P01 pre-run intent | datasets, labels, split, preprocessing, windowing, environment, gates, A0–A13, persistence | USED_AS_AUTHORITY |
| Executed Phase_01_Notebook.ipynb | P01 chronology | failed/superseded attempts and same-session repair history | USED_AS_EXECUTION_EVIDENCE |
| Accepted P01 execution bundle | primary P01 empirical/execution evidence | records, reports, manifests, gates, pointers, A4, checksums, handoffs | USED_AS_EXECUTION_EVIDENCE |
| Finalized cumulative Protocol v1.0 through P01 | immutable P01 analysis contract | ten P01 analyses, evidence ceilings, downstream boundaries | USED_AS_AUTHORITY |
| Phase 1 Evidence, Results, and Interpretation Report R1 | primary analytical predecessor for P01 | 14 findings, bounded interpretations, 12 candidate/deferred rows, limitations/handoffs | USED_AS_STRUCTURAL_PREDECESSOR |

## Appendix H. Consolidation / Preservation Matrix

| Predecessor | Material | Current location | Preservation status | Semantic change |
| --- | --- | --- | --- | --- |
| IHARQ-P00-PHASE-ANALYSIS-REPORT-R3-LAYER0-CORRECTED | P00 findings, evidence ceiling, correction history | Part II + Appendices D/F/G | PRESERVED_SEMANTICALLY | NO |
| P00-ANALYSIS-RELEASE-R2 | P00 measured evidence identities | Part II | PRESERVED_EXACT_BY_IDENTITY | NO |
| P00 Layer 0/Evidence Map/Layer 10 current state | P00 current v2 qualified claims and governance continuity | Part II §9; Part IV/Appendix D | PRESERVED_SEMANTICALLY | NO |
| IHARQ-P01-EVIDENCE-RESULTS-INTERPRETATION-REPORT-R1 | all P01 substantive analysis sections 1–51 | Part III | MOVED_WITHOUT_CHANGE_EXCEPT_HEADING_NAMESPACE | NO |
| P01 machine-readable findings/claims/limitations/handoffs | P01 structured analytical state | machine_readable/ derivatives + appendices | PRESERVED_SEMANTICALLY | NO |
| IHARQ-PROTOCOL-V1-CUMULATIVE-THROUGH-P01-R1 | immutable analysis contract | referenced throughout; not modified | PRESERVED_BY_REFERENCE | NO |

## Appendix I. Final Validation Declaration

This cumulative report is eligible to freeze only after the finalization suite confirms: all major sources used/dispositioned; P00 current history retained; P01 ten analyses complete; numerical results reverified; P01 execution bundle CRC/checksums pass; A0–A13 complete; A14 absence; A4 no-effectiveness boundary; human/machine parity; DOCX visual parity; no secrets/placeholders/unsafe paths; package checksum closure; 0 freeze-critical blockers.

# EMBEDDED LAYER 0 APPENDICES

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

## Appendix E. P00 Continuity Matrix

| Prior claim | Disposition | Finding(s) | Ceiling | Wording | Limitations | P01 invalidation? | Status |
|---|---|---|---|---|---|---|---|
| P00-CLM-001/v2 | APPROVED_WITH_QUALIFICATIONS | P00-F-001 | ENGINEERING_FOUNDATION_CONFORMANCE | Under the exact registered local snapshot and verified Python 3.13.5 environment, all 19 registered Phase 0 engineering/foundation conformance cells passed; this is non-empirical Mode B evidence and does not establish scientific effectiveness or Phase 0 closure. | P00-LIM-002; P00-LIM-003; P00-LIM-004; P00-LIM-L0-001 | No | PRESERVED_PRIOR_DISPOSITION |
| P00-CLM-002/v2 | APPROVED_WITH_QUALIFICATIONS | P00-F-002 | ENGINEERING_FOUNDATION_CONFORMANCE | In the frozen local Python 3.13.5 environment, the complete registered deterministic suite passed 102 of 102 tests; cross-version portability is not established. | P00-LIM-001; P00-LIM-002; P00-LIM-003; P00-LIM-004 | No | PRESERVED_PRIOR_DISPOSITION |
| P00-CLM-003/v2 | APPROVED_WITH_QUALIFICATIONS | P00-F-003; P00-F-004 | VALIDATION_EVIDENCE | Within the registered non-empirical fixture inventory, all 19 valid or integrated bundles were accepted and all 178 intentionally malformed categories were rejected as expected, with zero false valid rejections and zero false malformed acceptances. | P00-LIM-004; P00-LIM-L0-001 | No | PRESERVED_PRIOR_DISPOSITION |
| P00-CLM-004/v2 | APPROVED_WITH_QUALIFICATIONS | P00-F-005 | ARTIFACT_CLOSURE | The frozen Phase 0 package contains and validates the registered foundation inventories of 85 schemas, 35 configuration profiles, and 79 record-family profiles; inventory closure does not establish later-phase scientific effectiveness. | P00-LIM-004; P00-LIM-L0-001 | No | PRESERVED_PRIOR_DISPOSITION |
| P00-CLM-005/v2 | APPROVED_WITH_QUALIFICATIONS | P00-F-006 | FOUNDATION_INTEGRATION | All eleven Layer 0–10 foundation interfaces passed the registered Phase 0 integration scope; no later-phase scientific execution or effectiveness result is claimed. | P00-LIM-003; P00-LIM-004; P00-LIM-L0-001 | No | PRESERVED_PRIOR_DISPOSITION |
| P00-CLM-006/v2 | APPROVED_WITH_QUALIFICATIONS | P00-F-007 | CONTRACT_READINESS | The P00 implementation foundation is complete within its registered local scope, and P01–P15 reusable contract surfaces are ready for later governed annex creation and execution; future empirical outputs have not been produced. | P00-LIM-003; P00-LIM-004; P00-LIM-L0-001 | No | PRESERVED_PRIOR_DISPOSITION |
| P00-CLM-007/v2 | APPROVED_WITH_QUALIFICATIONS | P00-F-008 | LOCAL_REPRODUCIBILITY | The package reproduced from a clean isolated copy under the exact verified Python 3.13.5 and 22-distribution local dependency snapshot; portable cross-version reproducibility is not established. | P00-LIM-001; P00-LIM-002; P00-LIM-003 | No | PRESERVED_PRIOR_DISPOSITION |

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

# FINAL INTEGRATED AUTHORITY CERTIFICATION

**CANONICAL CUMULATIVE ANALYSIS + LAYER 0 AUTHORITY:** this Markdown report.  
**PHASE ANALYSIS FINDINGS:** preserved analytical content; no scientific-result mutation.  
**LAYER 0 REVIEW:** embedded governed disposition state.  
**DOCX:** format-equivalent derivative.  
**YAML/JSON/CSV:** non-authoritative structured/validation derivatives.  
**Separate P01 Layer 0 document:** non-authoritative phase-specific convenience derivative only.

```text
CUMULATIVE_PHASE_ANALYSIS_WITH_EMBEDDED_LAYER0_THROUGH_P01:
PASS — FINALIZED AND FROZEN

P00 analysis: PRESERVED
P01 analysis: PRESERVED
P00 Layer 0: PRESERVED
P01 Layer 0: APPLIED_AND_FINALIZED
unresolved candidate claims: 0
measurements changed: NO
Protocol changed: NO
analytical findings changed: NO
A14: ABSENT_PROHIBITED
A4 effectiveness: NOT ESTABLISHED IN P01
clinical/deployment effectiveness: NOT ESTABLISHED IN P01
Evidence Map inputs: READY
Layer 10 claim inputs: READY_AFTER_EVIDENCE_MAP
freeze-critical blockers: 0
next governed step: UPDATE THE PAPER AND THESIS EVIDENCE MAP THROUGH P01
```
