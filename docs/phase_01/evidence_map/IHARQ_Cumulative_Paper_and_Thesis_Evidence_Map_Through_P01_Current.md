---
title: "IHARQ Cumulative Paper and Thesis Evidence Map Through P01"
evidence_map_id: "IHARQ-CUMULATIVE-EVIDENCE-MAP-THROUGH-P01-R1"
revision: "R1"
release_id: "P00-P01-EVIDENCE-MAP-RELEASE-R1"
phases: "P00 + P01"
status: "CUMULATIVE_EVIDENCE_MAP_THROUGH_P01_PASS_FINALIZED_FROZEN"
layer10_readiness: "LAYER10_SOURCE_READY"
---

# IHARQ Cumulative Paper and Thesis Evidence Map Through P01
## Canonical claim-to-evidence, manuscript-placement, reproduction, and Layer 10 traceability authority

> **Authority boundary.** This Evidence Map links and version-pins already-governed claims to evidence. It does **not** approve claims, strengthen reviewed wording, change measurements, modify Protocol, create findings, or run experiments. The Layer-0-reviewed wording copied into this map is immutable.

## Document Control
| Field | Current value |
| --- | --- |
| Canonical Evidence Map ID | IHARQ-CUMULATIVE-EVIDENCE-MAP-THROUGH-P01-R1 |
| Release ID | P00-P01-EVIDENCE-MAP-RELEASE-R1 |
| Revision | R1 — owner-directed P00→P01 cumulative consolidation |
| Phases | P00 + P01 |
| P00 predecessor | P00-EVIDENCE-MAP-RELEASE-R2 / IHARQ-P00-EVIDENCE-MAP-ANNEX-R2 |
| Protocol | IHARQ-PROTOCOL-V1-CUMULATIVE-THROUGH-P01-R1 |
| Cumulative analysis + embedded Layer 0 | IHARQ-CUMULATIVE-PHASE-EVIDENCE-RESULTS-INTERPRETATION-THROUGH-P01-R2-LAYER0-INTEGRATED |
| Embedded Layer 0 authority | IHARQ-CUMULATIVE-LAYER0-THROUGH-P01-R1 |
| P01 scientific freeze | P01-L1-OFFICIAL-RUN-FREEZE-R2 |
| P01 config ID | d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f |
| P01 execution | ACCEPTED |
| Authority | This Markdown is the current controlling cumulative Evidence Map |
| DOCX | Format-equivalent derivative |
| CSV/YAML/JSON | Non-authoritative structured/validation derivatives |
| Next governed step | Layer 10 through P01 |

## Revision / Consolidation History
| Control | Decision |
| --- | --- |
| DOCUMENT_STRUCTURE_CHANGE | P00_AND_P01_EVIDENCE_MAP_CONSOLIDATED |
| P00_EVIDENCE_CHANGED | NO |
| P00_LAYER0_WORDING_CHANGED | NO |
| P01_EVIDENCE_ADDED | YES |
| P01_LAYER0_REVIEWED_CLAIMS_ADDED | YES |
| SCIENTIFIC_RESULTS_CHANGED | NO |
| PROTOCOL_CHANGED | NO |
| CLAIM_APPROVAL_PERFORMED_BY_EVIDENCE_MAP | NO |

## Purpose and non-authority notice
This map answers a single operational question: **for every current reviewed claim, exactly which finding, Protocol contract, run/stage, record/artifact, limitation, output placement, and reproduction route supports or constrains it?** It uses Layer 0 wording verbatim. Where final paper/thesis numbering or Layer 10 artifacts do not yet exist, the map uses explicit controlled states such as `PENDING_FINAL_MANUSCRIPT_STRUCTURE` and `PENDING_LAYER10`; these are lifecycle states, not unresolved drafting placeholders.


# PART I — EVIDENCE MAP GOVERNANCE

## 1. Authority Boundary
The Evidence Map may link, index, version-pin, cross-reference, propagate limitations, record placement, reproduction sources, and lifecycle state. It may not approve or strengthen claims; change reviewed wording; change measurements/counts/metrics/run inclusion; modify Protocol; create findings; or create new experiments.

## 2. Evidence Hierarchy
`EXECUTION / RECORD → MEASURED RESULT → FINDING → SUPPORTED INTERPRETATION → CANDIDATE CLAIM → LAYER 0 REVIEWED CLAIM → EVIDENCE MAP → LAYER 10 / MANUSCRIPT`

## 3. Claim Eligibility States
| State | Meaning |
| --- | --- |
| CURRENT_SUPPORTED | Approved reviewed claim mapped as supported |
| QUALIFIED_CURRENT | Approved-with-qualifications; mandatory limitations/warnings propagate |
| DEFERRED_NOT_MAPPABLE_AS_SUPPORTED | Preserved as future-work/negative governance; not a supported result |
| REJECTED_PROHIBITED_AS_SUPPORTED | Preserved as claim boundary; never a supported result |
| PRESERVED_UNCHANGED | Current P00 R2 row carried forward without semantic change |
| PENDING_LAYER10 | Governed source relation exists; final Layer 10 artifact has not yet been created |
| PENDING_FINAL_MANUSCRIPT_STRUCTURE | Logical placement is governed; final section numbering is not frozen |

## 4. Mapping Rules
- Use exact reviewed wording and exact claim/disposition IDs.
- Use canonical evidence paths when available; do not fabricate record IDs.
- Directories/collections are represented as evidence collections, not fake singleton records.
- Historical failures may support repair/negative-evidence statements but do not replace current accepted evidence for positive claims.
- Deferred/rejected rows remain visible and are never placed as supported Results claims.

## 5. Lifecycle Rules
Current, qualified, deferred, rejected, superseded, historical, pending-Layer10, and pending-manuscript states are kept distinct. Any upstream claim version, finding, Protocol, evidence pointer, denominator, or limitation change triggers refresh of affected map rows.

## 6. Limitation Propagation
Every Layer-0 mandatory limitation is propagated into the corresponding map row and downstream warning/caption/reproduction requirements. Critical limits such as `NON_CLINICAL`, `IMPLEMENTED_CHECKS_ONLY`, and the A4 non-effectiveness boundary must remain evidence-proximate.

## 7. Manuscript / Output Placement Rules
Logical placement is governed without inventing final manuscript section numbers. P01 figures/tables/cards that have not yet been generated by Layer 10 remain `PENDING_LAYER10`. P00 existing Layer 10 links are preserved.

# PART II — P00 PRESERVED EVIDENCE MAP

## 8. P00 Source State
The predecessor map is `P00-EVIDENCE-MAP-RELEASE-R2` / `IHARQ-P00-EVIDENCE-MAP-ANNEX-R2`. Its canonical annex SHA-256 is `ece1471edf1e117770e7cd3966a61267fd51a726a72630929fd70a1a06a80fd6` and the release manifest records seven active current rows. No P01 evidence invalidates any P00 mapping, so all seven are `PRESERVED_UNCHANGED`.

## 9. P00 Reviewed Claims
| Claim | Disposition | Exact reviewed wording | Finding(s) | Ceiling | Lifecycle |
| --- | --- | --- | --- | --- | --- |
| P00-CLM-001/v2 | APPROVE_WITH_QUALIFICATIONS | Under the exact registered local snapshot and verified Python 3.13.5 environment, all 19 registered Phase 0 engineering/foundation conformance cells passed; this is non-empirical Mode B evidence and does not establish scientific effectiveness or Phase 0 closure. | P00-F-001 | ENGINEERING_FOUNDATION_CONFORMANCE | ACTIVE_QUALIFIED_CURRENT |
| P00-CLM-002/v2 | APPROVE_WITH_QUALIFICATIONS | In the frozen local Python 3.13.5 environment, the complete registered deterministic suite passed 102 of 102 tests; cross-version portability is not established. | P00-F-002 | ENGINEERING_FOUNDATION_CONFORMANCE | ACTIVE_QUALIFIED_CURRENT |
| P00-CLM-003/v2 | APPROVE_WITH_QUALIFICATIONS | Within the registered non-empirical fixture inventory, all 19 valid or integrated bundles were accepted and all 178 intentionally malformed categories were rejected as expected, with zero false valid rejections and zero false malformed acceptances. | P00-F-003; P00-F-004 | VALIDATION_EVIDENCE | ACTIVE_QUALIFIED_CURRENT |
| P00-CLM-004/v2 | APPROVE_WITH_QUALIFICATIONS | The frozen Phase 0 package contains and validates the registered foundation inventories of 85 schemas, 35 configuration profiles, and 79 record-family profiles; inventory closure does not establish later-phase scientific effectiveness. | P00-F-005 | ARTIFACT_CLOSURE | ACTIVE_QUALIFIED_CURRENT |
| P00-CLM-005/v2 | APPROVE_WITH_QUALIFICATIONS | All eleven Layer 0–10 foundation interfaces passed the registered Phase 0 integration scope; no later-phase scientific execution or effectiveness result is claimed. | P00-F-006 | FOUNDATION_INTEGRATION | ACTIVE_QUALIFIED_CURRENT |
| P00-CLM-006/v2 | APPROVE_WITH_QUALIFICATIONS | The P00 implementation foundation is complete within its registered local scope, and P01–P15 reusable contract surfaces are ready for later governed annex creation and execution; future empirical outputs have not been produced. | P00-F-007 | CONTRACT_READINESS | ACTIVE_QUALIFIED_CURRENT |
| P00-CLM-007/v2 | APPROVE_WITH_QUALIFICATIONS | The package reproduced from a clean isolated copy under the exact verified Python 3.13.5 and 22-distribution local dependency snapshot; portable cross-version reproducibility is not established. | P00-F-008 | LOCAL_REPRODUCIBILITY | ACTIVE_QUALIFIED_CURRENT |

## 10. P00 Claim / Evidence Matrix
| Claim | Execution / analysis | Tests / gates | Limitations | Existing placement | Layer 10 views | Layer 10 card | Layer 10 export |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P00-CLM-001/v2 | P00-EXECUTION-RELEASE-R2; P00-ANALYSIS-RELEASE-R2 | PYTEST-102-OF-102; registered P0 gates | P00-LIM-002; P00-LIM-003; P00-LIM-004; P00-LIM-L0-001 | Phase 0 foundation/reproducibility appendix — item 1 | ClaimBoundaryView; P00PhaseStatusView | claim_card_01 | claims/claim_01.json |
| P00-CLM-002/v2 | P00-EXECUTION-RELEASE-R2; P00-ANALYSIS-RELEASE-R2 | PYTEST-102-OF-102; registered P0 gates | P00-LIM-001; P00-LIM-002; P00-LIM-003; P00-LIM-004 | Phase 0 foundation/reproducibility appendix — item 2 | ClaimBoundaryView; P00PhaseStatusView | claim_card_02 | claims/claim_02.json |
| P00-CLM-003/v2 | P00-EXECUTION-RELEASE-R2; P00-ANALYSIS-RELEASE-R2 | PYTEST-102-OF-102; registered P0 gates | P00-LIM-004; P00-LIM-L0-001 | Phase 0 foundation/reproducibility appendix — item 3 | ClaimBoundaryView; P00PhaseStatusView | claim_card_03 | claims/claim_03.json |
| P00-CLM-004/v2 | P00-EXECUTION-RELEASE-R2; P00-ANALYSIS-RELEASE-R2 | PYTEST-102-OF-102; registered P0 gates | P00-LIM-004; P00-LIM-L0-001 | Phase 0 foundation/reproducibility appendix — item 4 | ClaimBoundaryView; P00PhaseStatusView | claim_card_04 | claims/claim_04.json |
| P00-CLM-005/v2 | P00-EXECUTION-RELEASE-R2; P00-ANALYSIS-RELEASE-R2 | PYTEST-102-OF-102; registered P0 gates | P00-LIM-003; P00-LIM-004; P00-LIM-L0-001 | Phase 0 foundation/reproducibility appendix — item 5 | ClaimBoundaryView; P00PhaseStatusView | claim_card_05 | claims/claim_05.json |
| P00-CLM-006/v2 | P00-EXECUTION-RELEASE-R2; P00-ANALYSIS-RELEASE-R2 | PYTEST-102-OF-102; registered P0 gates | P00-LIM-003; P00-LIM-004; P00-LIM-L0-001 | Phase 0 foundation/reproducibility appendix — item 6 | ClaimBoundaryView; P00PhaseStatusView | claim_card_06 | claims/claim_06.json |
| P00-CLM-007/v2 | P00-EXECUTION-RELEASE-R2; P00-ANALYSIS-RELEASE-R2 | PYTEST-102-OF-102; registered P0 gates | P00-LIM-001; P00-LIM-002; P00-LIM-003 | Phase 0 foundation/reproducibility appendix — item 7 | ClaimBoundaryView; P00PhaseStatusView | claim_card_07 | claims/claim_07.json |

## 11. P00 Limitations
P00 remains non-empirical Mode B engineering/foundation evidence. Existing P00 limitation and warning relationships are carried forward from the R2 propagation matrix without strengthening or reinterpretation.

## 12. P00 Existing Layer 10 Links
The predecessor P00 Layer 10 package `P00-BASIC-LAYER10-PACKAGE-R2` remains the current P00 read-only visualization/export source. Existing claim-card, warning, view, export, and reproduction relations are preserved; the cumulative Evidence Map does not recompute them.

## 13. P00 Current Validity
`P00_mapping_loss = 0`. The seven P00 reviewed claims, their wording hashes, findings, limitations, placements, Layer 10 relations, and lifecycle rules remain current. Historical V4 workflow statements are provenance only; current Governance V6.1 controls future workflow sequencing.

# PART III — P01 EVIDENCE MAP

## 14. P01 Source State
P01 mapping is grounded in the accepted execution bundle, the frozen cumulative Protocol, the cumulative Phase Analysis with embedded Layer 0, and the structured Layer 0 Evidence Map handoff. The map independently resolves local evidence paths and version-pins the two large external Kaggle artifacts.

## 15. P01 Layer 0 Reviewed Claims
| Claim | Disposition | Reviewed wording | Evidence Map state |
| --- | --- | --- | --- |
| P01-CLM-001/v1 | APPROVED_WITH_QUALIFICATIONS | Within the frozen P01 binary motor-imagery branch, Phase 1 established a checksum-bound, provenance-traceable foundation over the three activated public EEG datasets. | QUALIFIED_CURRENT |
| P01-CLM-002/v1 | APPROVED_WITH_QUALIFICATIONS | The frozen P01 split assigned 172 subject groups wholly and disjointly across train, calibration, validation, and test roles and passed the implemented registered leakage/disjointness checks; this does not prove that every conceivable leakage mechanism is impossible. | QUALIFIED_CURRENT |
| P01-CLM-003/v1 | APPROVED | Under the frozen official core-window policy, all 12,910 accepted events yielded 12,910 valid core windows, with 0/12,910 invalid official core windows. | CURRENT_SUPPORTED |
| P01-CLM-004/v1 | APPROVED_WITH_QUALIFICATIONS | The official P01 core numerical artifact was persisted as 172 lossless HDF5 subject shards covering 12,910 windows and was verified under its Kaggle provider-version/logical-revision/manifest-hash identity contract. | QUALIFIED_CURRENT |
| P01-CLM-005/v1 | APPROVED_WITH_QUALIFICATIONS | P01 applied the ANNOTATE_NOT_REPAIR quality policy across 489 quality summaries: 20 soft/provider flags were retained, 0/489 summaries were hard-invalid, and 0/12,910 official core windows were invalid under the registered criteria. | QUALIFIED_CURRENT |
| P01-CLM-006/v1 | APPROVED_WITH_QUALIFICATIONS | P01 established Layer-1 foundation readiness for each official A0-A13 identity; none of these ablation-effectiveness experiments was executed in P01, and A14 remained absent/prohibited. | QUALIFIED_CURRENT |
| P01-CLM-007/v1 | APPROVED_WITH_QUALIFICATIONS | P01 established a fully matched A4 R2 Layer-1 data substrate for future governed evaluation: 12,910/12,910 parent events are represented without padding, clipping, fabricated samples, or parent-event loss. A4 R2 arose after the +4.0 s feasibility failure and was not evaluated for decoder effectiveness in P01. | QUALIFIED_CURRENT |
| P01-CLM-008/v1 | APPROVED | The accepted P01 execution completed 27/27 registered stages, 16/16 deterministic P01 gates, and 50/50 regression tests with 0 unresolved blockers; final execution-bundle integrity checks also closed. | CURRENT_SUPPORTED |
| P01-CLM-009/v1 | APPROVED_WITH_QUALIFICATIONS | The accepted P01 run used Python 3.12.13 under a documented compatibility amendment and the governed adaptive-disk policy P01-L1-KAGGLE-ADAPTIVE-DISK-R1; the accepted records show no change to the frozen datasets, labels, subject split, core preprocessing, core window policy, or 12,910-event denominator attributable to these runtime/resource amendments. | QUALIFIED_CURRENT |
| P01-CLM-010/v1 | APPROVED_WITH_QUALIFICATIONS | P01 freezes a technical Layer-1 data contract that P02 may consume using the recorded dataset, label-map, split, preprocessing, core-window, and external-artifact identities; silent relabeling, rewindowing, split mutation, denominator substitution, or test-visibility leakage is prohibited. This is technical readiness, not evidence of P02 scientific success. | QUALIFIED_CURRENT |
| P01-CLM-011/v1 | DEFERRED | P01 did not evaluate whether A4 R2 improves decoder performance relative to the core window; that effectiveness question remains deferred to a future governed matched downstream experiment. | DEFERRED_NOT_MAPPABLE_AS_SUPPORTED |
| P01-CLM-012/v1 | REJECTED | P01 is a public, non-clinical data-foundation and execution-validation phase; it does not establish clinical effectiveness, patient benefit, deployment safety, or medical-device readiness. | REJECTED_PROHIBITED_AS_SUPPORTED |

## 16. P01 Claim-to-Finding Mapping
| Claim | Finding(s) | Evidence class | Denominator / population |
| --- | --- | --- | --- |
| P01-CLM-001/v1 | P01-FIND-001 | PROVENANCE_EVIDENCE | 3 datasets; 172 subject groups; 453 source files |
| P01-CLM-002/v1 | P01-FIND-002; P01-FIND-006 | VALIDATION_EVIDENCE | 172 subject groups = 102 train / 35 calibration / 17 validation / 18 test |
| P01-CLM-003/v1 | P01-FIND-003 | INTEGRITY_EVIDENCE | 12,910 accepted events → 12,910 valid core windows; 0 invalid |
| P01-CLM-004/v1 | P01-FIND-004 | INTEGRITY_EVIDENCE | 172 HDF5 shards; 12,910 windows |
| P01-CLM-005/v1 | P01-FIND-005 | VALIDATION_EVIDENCE | 489 quality summaries; 20 soft/provider flags; 0 hard-invalid; 0/12,910 invalid core windows |
| P01-CLM-006/v1 | P01-FIND-008 | READINESS_EVIDENCE | 14 readiness rows A0-A13; executed_in_p01=false; A14 absent |
| P01-CLM-007/v1 | P01-FIND-009; P01-FIND-010 | READINESS_EVIDENCE | 12,910/12,910 matched parents; 12,910 stored 3.5 s tensors; 38,730 virtual 2 s views; 0 invalid |
| P01-CLM-008/v1 | P01-FIND-012 | EXECUTION_EVIDENCE | 27/27 stages; 16/16 gates; 50/50 tests; 0 blockers; 13,164/13,164 bundle checksums |
| P01-CLM-009/v1 | P01-FIND-011 | EXECUTION_EVIDENCE | Python 3.12.13; adaptive disk minimum 6.0 GiB; observed free 18.94 GiB |
| P01-CLM-010/v1 | P01-FIND-014 | READINESS_EVIDENCE | P01→P02 technical handoff over frozen dataset/label/split/preprocessing/window/artifact identities |
| P01-CLM-011/v1 | P01-FIND-009 | UNSUPPORTED_CURRENTLY | No governed A4 effectiveness experiment in P01 |
| P01-CLM-012/v1 | P01-FIND-001; P01-FIND-012 | PROHIBITED_BY_EVIDENCE_SCOPE | P01 public EEG data foundation; no clinical/deployment evaluation |

## 17. P01 Claim-to-Protocol Mapping
| Claim | Protocol analysis IDs | Claim ceiling |
| --- | --- | --- |
| P01-CLM-001/v1 | P01-AC-001-SOURCE-INVENTORY | PUBLIC_EEG_DATA_FOUNDATION |
| P01-CLM-002/v1 | P01-AC-002-SPLIT; P01-AC-005-LEAKAGE | IMPLEMENTED_SPLIT_AND_LEAKAGE_CHECKS |
| P01-CLM-003/v1 | P01-AC-003-DENOMINATOR | DENOMINATOR_AND_MATERIALIZATION_CLOSURE |
| P01-CLM-004/v1 | P01-AC-006-EXTERNAL | EXTERNAL_ARTIFACT_IDENTITY_AND_RETRIEVABILITY |
| P01-CLM-005/v1 | P01-AC-004-QUALITY | REGISTERED_QUALITY_ANNOTATION_AND_HARD_VALIDITY_CLOSURE |
| P01-CLM-006/v1 | P01-AC-007-ABLATION-READINESS | A0_A13_LAYER1_FOUNDATION_READINESS_ONLY |
| P01-CLM-007/v1 | P01-AC-008-A4 | A4_R2_DATA_SUBSTRATE_READINESS_ONLY |
| P01-CLM-008/v1 | P01-AC-010-GATES-REPAIRS | EXECUTION_AND_REPRODUCIBILITY_CLOSURE |
| P01-CLM-009/v1 | P01-AC-009-ENVIRONMENT | RECORDED_RUNTIME_RESOURCE_COMPATIBILITY |
| P01-CLM-010/v1 | P01-AC-003-DENOMINATOR; P01-AC-005-LEAKAGE; P01-AC-006-EXTERNAL; P01-AC-007-ABLATION-READINESS; P01-AC-010-GATES-REPAIRS | P02_TECHNICAL_DATA_CONTRACT_READINESS |
| P01-CLM-011/v1 | P01-AC-008-A4 | NO_P01_A4_EFFECTIVENESS_CLAIM |
| P01-CLM-012/v1 | P01-AC-001-SOURCE-INVENTORY; P01-AC-010-GATES-REPAIRS | NON_CLINICAL_NO_DEPLOYMENT_CLAIM |

## 18. P01 Claim-to-Run / Stage Mapping
| Claim | Stages | Execution role |
| --- | --- | --- |
| P01-CLM-001/v1 | P01-STAGE-05; P01-STAGE-06; P01-STAGE-07 | Current accepted evidence route |
| P01-CLM-002/v1 | P01-STAGE-11; P01-STAGE-17 | Current accepted evidence route |
| P01-CLM-003/v1 | P01-STAGE-13; P01-STAGE-14; P01-STAGE-16 | Current accepted evidence route |
| P01-CLM-004/v1 | P01-STAGE-14; P01-STAGE-15; P01-STAGE-20 | Current accepted evidence route |
| P01-CLM-005/v1 | P01-STAGE-13; P01-STAGE-16 | Current accepted evidence route |
| P01-CLM-006/v1 | P01-STAGE-18 | Current accepted evidence route |
| P01-CLM-007/v1 | P01-STAGE-14; P01-STAGE-15; P01-STAGE-18 | Current accepted evidence route |
| P01-CLM-008/v1 | P01-STAGE-04; P01-STAGE-23; P01-STAGE-24; P01-STAGE-26 | Current accepted evidence route |
| P01-CLM-009/v1 | P01-STAGE-01; P01-STAGE-03 | Current accepted evidence route |
| P01-CLM-010/v1 | P01-STAGE-22; P01-STAGE-23; P01-STAGE-26 | Current accepted evidence route |
| P01-CLM-011/v1 | P01-STAGE-14; P01-STAGE-15 | Negative/deferred governance context |
| P01-CLM-012/v1 | P01-STAGE-06; P01-STAGE-26 | Negative/deferred governance context |

## 19. P01 Claim-to-Record Mapping
| Claim | Canonical record IDs | Collections / ranges |
| --- | --- | --- |
| P01-CLM-001/v1 | IHARQ-DATASETRECORD-20260806-66309cda68771bef; IHARQ-DATASETRECORD-20260806-42c424800627b6ee; IHARQ-DATASETRECORD-20260806-adb91f25a65e588e | NOT_APPLICABLE |
| P01-CLM-002/v1 | IHARQ-SPLITRECORD-20260806-e4e371d332c61e36 | NOT_APPLICABLE |
| P01-CLM-003/v1 | IHARQ-SPLITRECORD-20260806-e4e371d332c61e36; IHARQ-PREPROCESSINGRECORD-20260806-a11b59eeb3861a08 | NOT_APPLICABLE |
| P01-CLM-004/v1 | P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473; IHARQ-SPLITRECORD-20260806-e4e371d332c61e36; IHARQ-PREPROCESSINGRECORD-20260806-a11b59eeb3861a08 | NOT_APPLICABLE |
| P01-CLM-005/v1 | NO_SINGLETON_RECORD_ID | records/quality/ (489 governed quality summaries) |
| P01-CLM-006/v1 | NO_SINGLETON_RECORD_ID | A0-A13 readiness manifest |
| P01-CLM-007/v1 | P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13; P01-L1-A4-WINDOW-FAMILY-FREEZE-R2 | NOT_APPLICABLE |
| P01-CLM-008/v1 | NO_SINGLETON_RECORD_ID | P01-G01...P01-G16; stage_results 00...26 |
| P01-CLM-009/v1 | P01-L1-KAGGLE-ENV-FREEZE-R5; P01-L1-KAGGLE-ADAPTIVE-DISK-R1 | NOT_APPLICABLE |
| P01-CLM-010/v1 | IHARQ-DATASETRECORD-20260806-66309cda68771bef; IHARQ-DATASETRECORD-20260806-42c424800627b6ee; IHARQ-DATASETRECORD-20260806-adb91f25a65e588e; IHARQ-LABELMAPRECORD-20260806-4379781a3b5f5ea9; IHARQ-LABELMAPRECORD-20260806-587dcfff81307768; IHARQ-LABELMAPRECORD-20260806-b551cfd20335896c; IHARQ-SPLITRECORD-20260806-e4e371d332c61e36; IHARQ-PREPROCESSINGRECORD-20260806-a11b59eeb3861a08; P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473; P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13 | NOT_APPLICABLE |
| P01-CLM-011/v1 | P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13; P01-L1-A4-WINDOW-FAMILY-FREEZE-R2 | NOT_APPLICABLE |
| P01-CLM-012/v1 | IHARQ-DATASETRECORD-20260806-66309cda68771bef; IHARQ-DATASETRECORD-20260806-42c424800627b6ee; IHARQ-DATASETRECORD-20260806-adb91f25a65e588e | NOT_APPLICABLE |

## 20. P01 External Artifact Mapping
| Artifact | Provider / dataset | Provider rev | Logical rev | Manifest SHA-256 | Size bytes | Format | Access |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473 | Kaggle / csthv999z/iharq-p01-l1-derived-windows-d03f0a7c869d-20260806222242-68a91473 | 2 | 1 | dc21f418e9a1add62adb346f627d5d729735a5f1ecaa1d771f6fa5cfede627e1 | 1166652764 | LOSSLESS_HDF5_SUBJECT_SHARDS | PRIVATE Kaggle Dataset access + source-license compliance |
| P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13 | Kaggle / csthv999z/iharq-p01-l1-a4-d03f0a7c-9a7c6108 | 1 | 2 | 29124d59907610b1545e0a2b5d1811a4d4a2bf1df64cad49aa880f4721c47305 | 1357362334 | LOSSLESS_HDF5_MATCHED_3P5S_SUBJECT_SHARDS_WITH_REGISTERED_VIRTUAL_MULTIWINDOW_VIEWS | PRIVATE Kaggle Dataset access + source-license compliance |

## 21. P01 Limitation Mapping
| Claim | Mandatory limitations | Required warning |
| --- | --- | --- |
| P01-CLM-001/v1 | PUBLIC_EEG_ONLY; NON_CLINICAL; BINARY_MI_BRANCH_SCOPE | PUBLIC_EEG_ONLY; NON_CLINICAL; BINARY_MI_BRANCH_SCOPE |
| P01-CLM-002/v1 | IMPLEMENTED_CHECKS_ONLY | IMPLEMENTED_CHECKS_ONLY |
| P01-CLM-003/v1 | NO_MODEL_EFFECT_INFERENCE | NO_MODEL_EFFECT_INFERENCE |
| P01-CLM-004/v1 | PRIVATE_KAGGLE_EXTERNAL_ARTIFACT_ACCESS; SOURCE_LICENSE_REDISTRIBUTION_CONSTRAINTS | PRIVATE_KAGGLE_EXTERNAL_ARTIFACT_ACCESS; SOURCE_LICENSE_REDISTRIBUTION_CONSTRAINTS |
| P01-CLM-005/v1 | SOFT_FLAG_NOT_EQUIVALENT_TO_CORRUPTION | SOFT_FLAG_NOT_EQUIVALENT_TO_CORRUPTION |
| P01-CLM-006/v1 | NO_ABLATION_EFFECTIVENESS_IN_P01 | NO_ABLATION_EFFECTIVENESS_IN_P01 |
| P01-CLM-007/v1 | A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01; A4_EFFECTIVENESS_NOT_EXECUTED | A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01; A4_EFFECTIVENESS_NOT_EXECUTED |
| P01-CLM-008/v1 | NO_EFFECTIVENESS_INFERENCE | NO_EFFECTIVENESS_INFERENCE |
| P01-CLM-009/v1 | ACTUAL_RUNTIME_PYTHON_3_12_13_WITH_COMPATIBILITY_AMENDMENT; ADAPTIVE_DISK_RESOURCE_AMENDMENT | ACTUAL_RUNTIME_PYTHON_3_12_13_WITH_COMPATIBILITY_AMENDMENT; ADAPTIVE_DISK_RESOURCE_AMENDMENT |
| P01-CLM-010/v1 | DOCUMENTARY_CLOSURE_SEQUENCE_REMAINS | DOCUMENTARY_CLOSURE_SEQUENCE_REMAINS |
| P01-CLM-011/v1 | A4_EFFECTIVENESS_NOT_EXECUTED; A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01 | A4_EFFECTIVENESS_NOT_EXECUTED; A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01 |
| P01-CLM-012/v1 | PUBLIC_EEG_ONLY; NON_CLINICAL; NO_DEPLOYMENT_CLAIM | PUBLIC_EEG_ONLY; NON_CLINICAL; NO_DEPLOYMENT_CLAIM |

## 22. P01 Manuscript Placement
| Claim | Paper logical placement | Thesis logical placement | Status |
| --- | --- | --- | --- |
| P01-CLM-001/v1 | PROVISIONAL_METHODS_DATA | PROVISIONAL_METHODS_DATA_FOUNDATION | SUPPORTED_PLACEMENT |
| P01-CLM-002/v1 | PROVISIONAL_METHODS_SPLIT_AND_LEAKAGE | PROVISIONAL_METHODS_SPLIT_AND_LEAKAGE | SUPPORTED_PLACEMENT |
| P01-CLM-003/v1 | PROVISIONAL_RESULTS_DATA_FOUNDATION | PROVISIONAL_RESULTS_DATA_FOUNDATION | SUPPORTED_PLACEMENT |
| P01-CLM-004/v1 | PROVISIONAL_METHODS_REPRODUCIBILITY | PROVISIONAL_REPRODUCIBILITY | SUPPORTED_PLACEMENT |
| P01-CLM-005/v1 | PROVISIONAL_RESULTS_DATA_QUALITY | PROVISIONAL_RESULTS_DATA_QUALITY | SUPPORTED_PLACEMENT |
| P01-CLM-006/v1 | PROVISIONAL_METHODS_ABLATION_READINESS | PROVISIONAL_METHODS_ABLATION_READINESS | SUPPORTED_PLACEMENT |
| P01-CLM-007/v1 | PROVISIONAL_RESULTS_DATA_FOUNDATION_WITH_PROXIMATE_A4_WARNING | PROVISIONAL_RESULTS_A4_FOUNDATION_WITH_PROXIMATE_WARNING | SUPPORTED_PLACEMENT |
| P01-CLM-008/v1 | PROVISIONAL_METHODS_REPRODUCIBILITY | PROVISIONAL_REPRODUCIBILITY_AND_AUDIT | SUPPORTED_PLACEMENT |
| P01-CLM-009/v1 | PROVISIONAL_METHODS_REPRODUCIBILITY | PROVISIONAL_REPRODUCIBILITY_ENVIRONMENT | SUPPORTED_PLACEMENT |
| P01-CLM-010/v1 | PROVISIONAL_METHODS_DOWNSTREAM_HANDOFF | PROVISIONAL_DOWNSTREAM_READINESS | SUPPORTED_PLACEMENT |
| P01-CLM-011/v1 | PROVISIONAL_FUTURE_WORK_OR_LIMITATIONS | PROVISIONAL_FUTURE_WORK_OR_LIMITATIONS | FUTURE_WORK_OR_LIMITATIONS_ONLY |
| P01-CLM-012/v1 | PROVISIONAL_LIMITATIONS_OR_CLAIM_BOUNDARY | PROVISIONAL_LIMITATIONS_OR_CLAIM_BOUNDARY | NOT_ELIGIBLE_AS_SUPPORTED_CLAIM |

## 23. P01 Figure / Table / Card Mapping
| Claim | Figure source IDs | Table state | Card state | Layer 10 eligibility |
| --- | --- | --- | --- | --- |
| P01-CLM-001/v1 | P01-FIG-SRC-001; P01-FIG-SRC-002 | PENDING_LAYER10:DATASET_INVENTORY | PENDING_LAYER10 | ELIGIBLE_WITH_MANDATORY_WARNING |
| P01-CLM-002/v1 | P01-FIG-SRC-003 | PENDING_LAYER10:SPLIT_COUNTS | PENDING_LAYER10 | ELIGIBLE_WITH_MANDATORY_WARNING |
| P01-CLM-003/v1 | P01-FIG-SRC-002; P01-FIG-SRC-005 | PENDING_LAYER10:EVENT_WINDOW_COUNTS | PENDING_LAYER10 | ELIGIBLE_FOR_LAYER10 |
| P01-CLM-004/v1 | P01-FIG-SRC-005 | PENDING_LAYER10:EXTERNAL_ARTIFACTS | PENDING_LAYER10 | ELIGIBLE_WITH_MANDATORY_WARNING |
| P01-CLM-005/v1 | NO_CURRENT_ARTIFACT | PENDING_LAYER10:QUALITY_OUTCOMES | PENDING_LAYER10 | ELIGIBLE_WITH_MANDATORY_WARNING |
| P01-CLM-006/v1 | P01-FIG-SRC-009 | PENDING_LAYER10:A0_A13_READINESS | PENDING_LAYER10 | ELIGIBLE_WITH_MANDATORY_WARNING |
| P01-CLM-007/v1 | P01-FIG-SRC-006; P01-FIG-SRC-007 | PENDING_LAYER10:A4_PROFILE | PENDING_LAYER10 | ELIGIBLE_WITH_MANDATORY_WARNING |
| P01-CLM-008/v1 | P01-FIG-SRC-008 | PENDING_LAYER10:GATES_TESTS | PENDING_LAYER10 | ELIGIBLE_FOR_LAYER10 |
| P01-CLM-009/v1 | NO_CURRENT_ARTIFACT | PENDING_LAYER10:ENVIRONMENT_AMENDMENTS | PENDING_LAYER10 | ELIGIBLE_WITH_MANDATORY_WARNING |
| P01-CLM-010/v1 | P01-FIG-SRC-010 | PENDING_LAYER10:P01_P02_HANDOFF | PENDING_LAYER10 | ELIGIBLE_WITH_MANDATORY_WARNING |
| P01-CLM-011/v1 | P01-FIG-SRC-006; P01-FIG-SRC-007 | PENDING_LAYER10:NEGATIVE_DEFERRED_CLAIMS | PENDING_LAYER10 | DEFERRED_NOT_ELIGIBLE_AS_SUPPORTED |
| P01-CLM-012/v1 | P01-FIG-SRC-009 | PENDING_LAYER10:NEGATIVE_DEFERRED_CLAIMS | PENDING_LAYER10 | REJECTED_NOT_ELIGIBLE_AS_SUPPORTED |

## 24. P01 Reproduction Mapping
| Claim | Primary evidence paths | External artifact IDs | Reproduction assets |
| --- | --- | --- | --- |
| P01-CLM-001/v1 | records/datasets/BNCI2014_001/IHARQ-DATASETRECORD-20260806-42c424800627b6ee.json; records/datasets/Lee2019_MI/IHARQ-DATASETRECORD-20260806-adb91f25a65e588e.json; records/datasets/PhysioNetMI/IHARQ-DATASETRECORD-20260806-66309cda68771bef.json; reports/phase_01/sources/source_version_license_report.json | NOT_APPLICABLE | IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip; d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f |
| P01-CLM-002/v1 | records/splits/P01-L1-SPLIT-OFFICIAL-R2/IHARQ-SPLITRECORD-20260806-e4e371d332c61e36.json; reports/phase_01/splits/disjointness.json; reports/phase_01/leakage/leakage_contamination.json | NOT_APPLICABLE | IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip; d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f |
| P01-CLM-003/v1 | records/windows/; external_artifact_pointers/derived_windows_dataset.json | P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473 | IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip; P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473; d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f |
| P01-CLM-004/v1 | reports/phase_01/storage/existing_core_dataset_adoption.json; external_artifact_pointers/derived_windows_dataset.json | P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473 | IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip; P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473; d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f |
| P01-CLM-005/v1 | reports/phase_01/quality/quality_coverage.json; records/quality/ | NOT_APPLICABLE | IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip; d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f |
| P01-CLM-006/v1 | manifests/phase_01/layer1_ablation_readiness_l1_v1.json | NOT_APPLICABLE | IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip; d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f |
| P01-CLM-007/v1 | external_artifact_pointers/a4_window_family_dataset.json; reports/phase_01/storage/a4_derived_output_storage_actual_precommit.json; config_snapshot/p01_l1_a4_window_family_freeze_R2.json | P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13 | IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip; P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13; d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f |
| P01-CLM-008/v1 | reports/phase_01/tests/stage_results.json; gate_decision.json; reports/phase_01/tests/phase0_and_runtime_regression.json; reports/phase_01/repair_reentry.json; checksums.sha256 | NOT_APPLICABLE | IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip; d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f |
| P01-CLM-009/v1 | environment_manifest.json; environment_amendment.json | NOT_APPLICABLE | IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip; d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f |
| P01-CLM-010/v1 | handoffs/phase_01_to_phase_02.yaml; phase2_handoff/phase_01_to_phase_02.yaml | P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473; P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13 | IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip; P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473; P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13; d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f |
| P01-CLM-011/v1 | external_artifact_pointers/a4_window_family_dataset.json; config_snapshot/p01_l1_a4_window_family_freeze_R2.json | P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13 | IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip; P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13; d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f |
| P01-CLM-012/v1 | reports/phase_01/sources/source_version_license_report.json; gate_decision.json | NOT_APPLICABLE | IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip |

## 25. P01 Negative / Deferred / Rejected Claims
| Claim | Disposition | Governed wording | Allowed manuscript use | Supported-result use |
| --- | --- | --- | --- | --- |
| P01-CLM-011/v1 | DEFERRED | P01 did not evaluate whether A4 R2 improves decoder performance relative to the core window; that effectiveness question remains deferred to a future governed matched downstream experiment. | PROVISIONAL_FUTURE_WORK_OR_LIMITATIONS | PROHIBITED |
| P01-CLM-012/v1 | REJECTED | P01 is a public, non-clinical data-foundation and execution-validation phase; it does not establish clinical effectiveness, patient benefit, deployment safety, or medical-device readiness. | PROVISIONAL_LIMITATIONS_OR_CLAIM_BOUNDARY | PROHIBITED |

## P01 Claim Dossiers — human-auditable core

### Dossier 01 — P01-CLM-001/v1
| Field | Mapped value |
| --- | --- |
| Claim identity | P01-CLM-001/v1 |
| Source candidate | P01-CLAIM-CAND-001 |
| Reviewed wording | Within the frozen P01 binary motor-imagery branch, Phase 1 established a checksum-bound, provenance-traceable foundation over the three activated public EEG datasets. |
| Layer 0 disposition | APPROVED_WITH_QUALIFICATIONS / P01-L0-DISP-001 |
| Origin phase | P01 |
| Finding(s) | P01-FIND-001 |
| Protocol contract | P01-AC-001-SOURCE-INVENTORY |
| Execution stage(s) | P01-STAGE-05; P01-STAGE-06; P01-STAGE-07 |
| Record(s) | IHARQ-DATASETRECORD-20260806-66309cda68771bef; IHARQ-DATASETRECORD-20260806-42c424800627b6ee; IHARQ-DATASETRECORD-20260806-adb91f25a65e588e |
| Record collections | NOT_APPLICABLE |
| Primary evidence | records/datasets/BNCI2014_001/IHARQ-DATASETRECORD-20260806-42c424800627b6ee.json; records/datasets/Lee2019_MI/IHARQ-DATASETRECORD-20260806-adb91f25a65e588e.json; records/datasets/PhysioNetMI/IHARQ-DATASETRECORD-20260806-66309cda68771bef.json; reports/phase_01/sources/source_version_license_report.json |
| External source refs | NOT_APPLICABLE |
| Negative/adverse evidence | NONE_MATERIAL |
| Ablation relevance | NOT_APPLICABLE |
| Limitations | PUBLIC_EEG_ONLY; NON_CLINICAL; BINARY_MI_BRANCH_SCOPE |
| Claim ceiling | PUBLIC_EEG_DATA_FOUNDATION |
| Allowed manuscript use | PROVISIONAL_METHODS_DATA / PROVISIONAL_METHODS_DATA_FOUNDATION |
| Figure/table/card eligibility | Figures: P01-FIG-SRC-001; P01-FIG-SRC-002; Tables: PENDING_LAYER10:DATASET_INVENTORY; Cards: PENDING_LAYER10 |
| Reproduction route | IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip; d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f |
| Lifecycle | QUALIFIED_CURRENT |
| Forbidden stronger wording | P01 established a clinically representative or deployment-ready EEG foundation. |

### Dossier 02 — P01-CLM-002/v1
| Field | Mapped value |
| --- | --- |
| Claim identity | P01-CLM-002/v1 |
| Source candidate | P01-CLAIM-CAND-002 |
| Reviewed wording | The frozen P01 split assigned 172 subject groups wholly and disjointly across train, calibration, validation, and test roles and passed the implemented registered leakage/disjointness checks; this does not prove that every conceivable leakage mechanism is impossible. |
| Layer 0 disposition | APPROVED_WITH_QUALIFICATIONS / P01-L0-DISP-002 |
| Origin phase | P01 |
| Finding(s) | P01-FIND-002; P01-FIND-006 |
| Protocol contract | P01-AC-002-SPLIT; P01-AC-005-LEAKAGE |
| Execution stage(s) | P01-STAGE-11; P01-STAGE-17 |
| Record(s) | IHARQ-SPLITRECORD-20260806-e4e371d332c61e36 |
| Record collections | NOT_APPLICABLE |
| Primary evidence | records/splits/P01-L1-SPLIT-OFFICIAL-R2/IHARQ-SPLITRECORD-20260806-e4e371d332c61e36.json; reports/phase_01/splits/disjointness.json; reports/phase_01/leakage/leakage_contamination.json |
| External source refs | NOT_APPLICABLE |
| Negative/adverse evidence | NONE_MATERIAL |
| Ablation relevance | NOT_APPLICABLE |
| Limitations | IMPLEMENTED_CHECKS_ONLY |
| Claim ceiling | IMPLEMENTED_SPLIT_AND_LEAKAGE_CHECKS |
| Allowed manuscript use | PROVISIONAL_METHODS_SPLIT_AND_LEAKAGE / PROVISIONAL_METHODS_SPLIT_AND_LEAKAGE |
| Figure/table/card eligibility | Figures: P01-FIG-SRC-003; Tables: PENDING_LAYER10:SPLIT_COUNTS; Cards: PENDING_LAYER10 |
| Reproduction route | IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip; d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f |
| Lifecycle | QUALIFIED_CURRENT |
| Forbidden stronger wording | P01 proves that leakage is impossible. |

### Dossier 03 — P01-CLM-003/v1
| Field | Mapped value |
| --- | --- |
| Claim identity | P01-CLM-003/v1 |
| Source candidate | P01-CLAIM-CAND-003 |
| Reviewed wording | Under the frozen official core-window policy, all 12,910 accepted events yielded 12,910 valid core windows, with 0/12,910 invalid official core windows. |
| Layer 0 disposition | APPROVED / P01-L0-DISP-003 |
| Origin phase | P01 |
| Finding(s) | P01-FIND-003 |
| Protocol contract | P01-AC-003-DENOMINATOR |
| Execution stage(s) | P01-STAGE-13; P01-STAGE-14; P01-STAGE-16 |
| Record(s) | IHARQ-SPLITRECORD-20260806-e4e371d332c61e36; IHARQ-PREPROCESSINGRECORD-20260806-a11b59eeb3861a08 |
| Record collections | NOT_APPLICABLE |
| Primary evidence | records/windows/; external_artifact_pointers/derived_windows_dataset.json |
| External source refs | NOT_APPLICABLE |
| Negative/adverse evidence | NONE_MATERIAL |
| Ablation relevance | NOT_APPLICABLE |
| Limitations | NO_MODEL_EFFECT_INFERENCE |
| Claim ceiling | DENOMINATOR_AND_MATERIALIZATION_CLOSURE |
| Allowed manuscript use | PROVISIONAL_RESULTS_DATA_FOUNDATION / PROVISIONAL_RESULTS_DATA_FOUNDATION |
| Figure/table/card eligibility | Figures: P01-FIG-SRC-002; P01-FIG-SRC-005; Tables: PENDING_LAYER10:EVENT_WINDOW_COUNTS; Cards: PENDING_LAYER10 |
| Reproduction route | IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip; P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473; d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f |
| Lifecycle | CURRENT_SUPPORTED |
| Forbidden stronger wording | Denominator closure proves the dataset will yield strong decoder performance. |

### Dossier 04 — P01-CLM-004/v1
| Field | Mapped value |
| --- | --- |
| Claim identity | P01-CLM-004/v1 |
| Source candidate | P01-CLAIM-CAND-004 |
| Reviewed wording | The official P01 core numerical artifact was persisted as 172 lossless HDF5 subject shards covering 12,910 windows and was verified under its Kaggle provider-version/logical-revision/manifest-hash identity contract. |
| Layer 0 disposition | APPROVED_WITH_QUALIFICATIONS / P01-L0-DISP-004 |
| Origin phase | P01 |
| Finding(s) | P01-FIND-004 |
| Protocol contract | P01-AC-006-EXTERNAL |
| Execution stage(s) | P01-STAGE-14; P01-STAGE-15; P01-STAGE-20 |
| Record(s) | P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473; IHARQ-SPLITRECORD-20260806-e4e371d332c61e36; IHARQ-PREPROCESSINGRECORD-20260806-a11b59eeb3861a08 |
| Record collections | NOT_APPLICABLE |
| Primary evidence | reports/phase_01/storage/existing_core_dataset_adoption.json; external_artifact_pointers/derived_windows_dataset.json |
| External source refs | NOT_APPLICABLE |
| Negative/adverse evidence | NONE_MATERIAL |
| Ablation relevance | NOT_APPLICABLE |
| Limitations | PRIVATE_KAGGLE_EXTERNAL_ARTIFACT_ACCESS; SOURCE_LICENSE_REDISTRIBUTION_CONSTRAINTS |
| Claim ceiling | EXTERNAL_ARTIFACT_IDENTITY_AND_RETRIEVABILITY |
| Allowed manuscript use | PROVISIONAL_METHODS_REPRODUCIBILITY / PROVISIONAL_REPRODUCIBILITY |
| Figure/table/card eligibility | Figures: P01-FIG-SRC-005; Tables: PENDING_LAYER10:EXTERNAL_ARTIFACTS; Cards: PENDING_LAYER10 |
| Reproduction route | IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip; P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473; d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f |
| Lifecycle | QUALIFIED_CURRENT |
| Forbidden stronger wording | The core Dataset is universally public and independently downloadable without access or license constraints. |

### Dossier 05 — P01-CLM-005/v1
| Field | Mapped value |
| --- | --- |
| Claim identity | P01-CLM-005/v1 |
| Source candidate | P01-CLAIM-CAND-005 |
| Reviewed wording | P01 applied the ANNOTATE_NOT_REPAIR quality policy across 489 quality summaries: 20 soft/provider flags were retained, 0/489 summaries were hard-invalid, and 0/12,910 official core windows were invalid under the registered criteria. |
| Layer 0 disposition | APPROVED_WITH_QUALIFICATIONS / P01-L0-DISP-005 |
| Origin phase | P01 |
| Finding(s) | P01-FIND-005 |
| Protocol contract | P01-AC-004-QUALITY |
| Execution stage(s) | P01-STAGE-13; P01-STAGE-16 |
| Record(s) | NO_SINGLETON_RECORD_ID |
| Record collections | records/quality/ (489 governed quality summaries) |
| Primary evidence | reports/phase_01/quality/quality_coverage.json; records/quality/ |
| External source refs | NOT_APPLICABLE |
| Negative/adverse evidence | NONE_MATERIAL |
| Ablation relevance | NOT_APPLICABLE |
| Limitations | SOFT_FLAG_NOT_EQUIVALENT_TO_CORRUPTION |
| Claim ceiling | REGISTERED_QUALITY_ANNOTATION_AND_HARD_VALIDITY_CLOSURE |
| Allowed manuscript use | PROVISIONAL_RESULTS_DATA_QUALITY / PROVISIONAL_RESULTS_DATA_QUALITY |
| Figure/table/card eligibility | Figures: none; Tables: PENDING_LAYER10:QUALITY_OUTCOMES; Cards: PENDING_LAYER10 |
| Reproduction route | IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip; d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f |
| Lifecycle | QUALIFIED_CURRENT |
| Forbidden stronger wording | All P01 EEG was flawless or artifact-free. |

### Dossier 06 — P01-CLM-006/v1
| Field | Mapped value |
| --- | --- |
| Claim identity | P01-CLM-006/v1 |
| Source candidate | P01-CLAIM-CAND-006 |
| Reviewed wording | P01 established Layer-1 foundation readiness for each official A0-A13 identity; none of these ablation-effectiveness experiments was executed in P01, and A14 remained absent/prohibited. |
| Layer 0 disposition | APPROVED_WITH_QUALIFICATIONS / P01-L0-DISP-006 |
| Origin phase | P01 |
| Finding(s) | P01-FIND-008 |
| Protocol contract | P01-AC-007-ABLATION-READINESS |
| Execution stage(s) | P01-STAGE-18 |
| Record(s) | NO_SINGLETON_RECORD_ID |
| Record collections | A0-A13 readiness manifest |
| Primary evidence | manifests/phase_01/layer1_ablation_readiness_l1_v1.json |
| External source refs | NOT_APPLICABLE |
| Negative/adverse evidence | A14_ABSENT_PROHIBITED |
| Ablation relevance | A0; A1; A2; A3; A4; A5; A6; A7; A8; A9; A10; A11; A12; A13 |
| Limitations | NO_ABLATION_EFFECTIVENESS_IN_P01 |
| Claim ceiling | A0_A13_LAYER1_FOUNDATION_READINESS_ONLY |
| Allowed manuscript use | PROVISIONAL_METHODS_ABLATION_READINESS / PROVISIONAL_METHODS_ABLATION_READINESS |
| Figure/table/card eligibility | Figures: P01-FIG-SRC-009; Tables: PENDING_LAYER10:A0_A13_READINESS; Cards: PENDING_LAYER10 |
| Reproduction route | IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip; d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f |
| Lifecycle | QUALIFIED_CURRENT |
| Forbidden stronger wording | P01 demonstrated that A0-A13 ablations are effective. |

### Dossier 07 — P01-CLM-007/v1
| Field | Mapped value |
| --- | --- |
| Claim identity | P01-CLM-007/v1 |
| Source candidate | P01-CLAIM-CAND-007 |
| Reviewed wording | P01 established a fully matched A4 R2 Layer-1 data substrate for future governed evaluation: 12,910/12,910 parent events are represented without padding, clipping, fabricated samples, or parent-event loss. A4 R2 arose after the +4.0 s feasibility failure and was not evaluated for decoder effectiveness in P01. |
| Layer 0 disposition | APPROVED_WITH_QUALIFICATIONS / P01-L0-DISP-007 |
| Origin phase | P01 |
| Finding(s) | P01-FIND-009; P01-FIND-010 |
| Protocol contract | P01-AC-008-A4 |
| Execution stage(s) | P01-STAGE-14; P01-STAGE-15; P01-STAGE-18 |
| Record(s) | P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13; P01-L1-A4-WINDOW-FAMILY-FREEZE-R2 |
| Record collections | NOT_APPLICABLE |
| Primary evidence | external_artifact_pointers/a4_window_family_dataset.json; reports/phase_01/storage/a4_derived_output_storage_actual_precommit.json; config_snapshot/p01_l1_a4_window_family_freeze_R2.json |
| External source refs | P01_EXECUTED_NOTEBOOK_R49_A4_BOUNDARY_EXPLANATION |
| Negative/adverse evidence | P01-NEG-A4-4S-INFEASIBILITY; P01-CLM-011/v1 |
| Ablation relevance | A4 |
| Limitations | A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01; A4_EFFECTIVENESS_NOT_EXECUTED |
| Claim ceiling | A4_R2_DATA_SUBSTRATE_READINESS_ONLY |
| Allowed manuscript use | PROVISIONAL_RESULTS_DATA_FOUNDATION_WITH_PROXIMATE_A4_WARNING / PROVISIONAL_RESULTS_A4_FOUNDATION_WITH_PROXIMATE_WARNING |
| Figure/table/card eligibility | Figures: P01-FIG-SRC-006; P01-FIG-SRC-007; Tables: PENDING_LAYER10:A4_PROFILE; Cards: PENDING_LAYER10 |
| Reproduction route | IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip; P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13; d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f |
| Lifecycle | QUALIFIED_CURRENT |
| Forbidden stronger wording | A4 R2 improves accuracy, AUROC, robustness, or decoder performance. |

### Dossier 08 — P01-CLM-008/v1
| Field | Mapped value |
| --- | --- |
| Claim identity | P01-CLM-008/v1 |
| Source candidate | P01-CLAIM-CAND-008 |
| Reviewed wording | The accepted P01 execution completed 27/27 registered stages, 16/16 deterministic P01 gates, and 50/50 regression tests with 0 unresolved blockers; final execution-bundle integrity checks also closed. |
| Layer 0 disposition | APPROVED / P01-L0-DISP-008 |
| Origin phase | P01 |
| Finding(s) | P01-FIND-012 |
| Protocol contract | P01-AC-010-GATES-REPAIRS |
| Execution stage(s) | P01-STAGE-04; P01-STAGE-23; P01-STAGE-24; P01-STAGE-26 |
| Record(s) | NO_SINGLETON_RECORD_ID |
| Record collections | P01-G01...P01-G16; stage_results 00...26 |
| Primary evidence | reports/phase_01/tests/stage_results.json; gate_decision.json; reports/phase_01/tests/phase0_and_runtime_regression.json; reports/phase_01/repair_reentry.json; checksums.sha256 |
| External source refs | NOT_APPLICABLE |
| Negative/adverse evidence | P01-HISTORICAL-FAILED-EXECUTION |
| Ablation relevance | NOT_APPLICABLE |
| Limitations | NO_EFFECTIVENESS_INFERENCE |
| Claim ceiling | EXECUTION_AND_REPRODUCIBILITY_CLOSURE |
| Allowed manuscript use | PROVISIONAL_METHODS_REPRODUCIBILITY / PROVISIONAL_REPRODUCIBILITY_AND_AUDIT |
| Figure/table/card eligibility | Figures: P01-FIG-SRC-008; Tables: PENDING_LAYER10:GATES_TESTS; Cards: PENDING_LAYER10 |
| Reproduction route | IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip; d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f |
| Lifecycle | CURRENT_SUPPORTED |
| Forbidden stronger wording | Because all gates passed, P01 proved scientific or clinical effectiveness. |

### Dossier 09 — P01-CLM-009/v1
| Field | Mapped value |
| --- | --- |
| Claim identity | P01-CLM-009/v1 |
| Source candidate | P01-CLAIM-CAND-009 |
| Reviewed wording | The accepted P01 run used Python 3.12.13 under a documented compatibility amendment and the governed adaptive-disk policy P01-L1-KAGGLE-ADAPTIVE-DISK-R1; the accepted records show no change to the frozen datasets, labels, subject split, core preprocessing, core window policy, or 12,910-event denominator attributable to these runtime/resource amendments. |
| Layer 0 disposition | APPROVED_WITH_QUALIFICATIONS / P01-L0-DISP-009 |
| Origin phase | P01 |
| Finding(s) | P01-FIND-011 |
| Protocol contract | P01-AC-009-ENVIRONMENT |
| Execution stage(s) | P01-STAGE-01; P01-STAGE-03 |
| Record(s) | P01-L1-KAGGLE-ENV-FREEZE-R5; P01-L1-KAGGLE-ADAPTIVE-DISK-R1 |
| Record collections | NOT_APPLICABLE |
| Primary evidence | environment_manifest.json; environment_amendment.json |
| External source refs | NOT_APPLICABLE |
| Negative/adverse evidence | NONE_MATERIAL |
| Ablation relevance | NOT_APPLICABLE |
| Limitations | ACTUAL_RUNTIME_PYTHON_3_12_13_WITH_COMPATIBILITY_AMENDMENT; ADAPTIVE_DISK_RESOURCE_AMENDMENT |
| Claim ceiling | RECORDED_RUNTIME_RESOURCE_COMPATIBILITY |
| Allowed manuscript use | PROVISIONAL_METHODS_REPRODUCIBILITY / PROVISIONAL_REPRODUCIBILITY_ENVIRONMENT |
| Figure/table/card eligibility | Figures: none; Tables: PENDING_LAYER10:ENVIRONMENT_AMENDMENTS; Cards: PENDING_LAYER10 |
| Reproduction route | IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip; d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f |
| Lifecycle | QUALIFIED_CURRENT |
| Forbidden stronger wording | Environment differences could have no effect whatsoever or are universally irrelevant. |

### Dossier 10 — P01-CLM-010/v1
| Field | Mapped value |
| --- | --- |
| Claim identity | P01-CLM-010/v1 |
| Source candidate | P01-CLAIM-CAND-010 |
| Reviewed wording | P01 freezes a technical Layer-1 data contract that P02 may consume using the recorded dataset, label-map, split, preprocessing, core-window, and external-artifact identities; silent relabeling, rewindowing, split mutation, denominator substitution, or test-visibility leakage is prohibited. This is technical readiness, not evidence of P02 scientific success. |
| Layer 0 disposition | APPROVED_WITH_QUALIFICATIONS / P01-L0-DISP-010 |
| Origin phase | P01 |
| Finding(s) | P01-FIND-014 |
| Protocol contract | P01-AC-003-DENOMINATOR; P01-AC-005-LEAKAGE; P01-AC-006-EXTERNAL; P01-AC-007-ABLATION-READINESS; P01-AC-010-GATES-REPAIRS |
| Execution stage(s) | P01-STAGE-22; P01-STAGE-23; P01-STAGE-26 |
| Record(s) | IHARQ-DATASETRECORD-20260806-66309cda68771bef; IHARQ-DATASETRECORD-20260806-42c424800627b6ee; IHARQ-DATASETRECORD-20260806-adb91f25a65e588e; IHARQ-LABELMAPRECORD-20260806-4379781a3b5f5ea9; IHARQ-LABELMAPRECORD-20260806-587dcfff81307768; IHARQ-LABELMAPRECORD-20260806-b551cfd20335896c; IHARQ-SPLITRECORD-20260806-e4e371d332c61e36; IHARQ-PREPROCESSINGRECORD-20260806-a11b59eeb3861a08; P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473; P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13 |
| Record collections | NOT_APPLICABLE |
| Primary evidence | handoffs/phase_01_to_phase_02.yaml; phase2_handoff/phase_01_to_phase_02.yaml |
| External source refs | NOT_APPLICABLE |
| Negative/adverse evidence | NONE_MATERIAL |
| Ablation relevance | NOT_APPLICABLE |
| Limitations | DOCUMENTARY_CLOSURE_SEQUENCE_REMAINS |
| Claim ceiling | P02_TECHNICAL_DATA_CONTRACT_READINESS |
| Allowed manuscript use | PROVISIONAL_METHODS_DOWNSTREAM_HANDOFF / PROVISIONAL_DOWNSTREAM_READINESS |
| Figure/table/card eligibility | Figures: P01-FIG-SRC-010; Tables: PENDING_LAYER10:P01_P02_HANDOFF; Cards: PENDING_LAYER10 |
| Reproduction route | IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip; P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473; P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13; d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f |
| Lifecycle | QUALIFIED_CURRENT |
| Forbidden stronger wording | P01 proves that P02 will succeed scientifically or that downstream models will perform well. |

### Dossier 11 — P01-CLM-011/v1
| Field | Mapped value |
| --- | --- |
| Claim identity | P01-CLM-011/v1 |
| Source candidate | P01-CLAIM-CAND-011 |
| Reviewed wording | P01 did not evaluate whether A4 R2 improves decoder performance relative to the core window; that effectiveness question remains deferred to a future governed matched downstream experiment. |
| Layer 0 disposition | DEFERRED / P01-L0-DISP-011 |
| Origin phase | P01 |
| Finding(s) | P01-FIND-009 |
| Protocol contract | P01-AC-008-A4 |
| Execution stage(s) | P01-STAGE-14; P01-STAGE-15 |
| Record(s) | P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13; P01-L1-A4-WINDOW-FAMILY-FREEZE-R2 |
| Record collections | NOT_APPLICABLE |
| Primary evidence | external_artifact_pointers/a4_window_family_dataset.json; config_snapshot/p01_l1_a4_window_family_freeze_R2.json |
| External source refs | NOT_APPLICABLE |
| Negative/adverse evidence | P01-NEG-A4-EFFECTIVENESS-NOT-EXECUTED |
| Ablation relevance | A4 |
| Limitations | A4_EFFECTIVENESS_NOT_EXECUTED; A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01 |
| Claim ceiling | NO_P01_A4_EFFECTIVENESS_CLAIM |
| Allowed manuscript use | PROVISIONAL_FUTURE_WORK_OR_LIMITATIONS / PROVISIONAL_FUTURE_WORK_OR_LIMITATIONS |
| Figure/table/card eligibility | Figures: P01-FIG-SRC-006; P01-FIG-SRC-007; Tables: PENDING_LAYER10:NEGATIVE_DEFERRED_CLAIMS; Cards: PENDING_LAYER10 |
| Reproduction route | IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip; P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13; d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f |
| Lifecycle | DEFERRED_NOT_MAPPABLE_AS_SUPPORTED |
| Forbidden stronger wording | A4 R2 improves decoder performance relative to the core window. |

### Dossier 12 — P01-CLM-012/v1
| Field | Mapped value |
| --- | --- |
| Claim identity | P01-CLM-012/v1 |
| Source candidate | P01-CLAIM-CAND-012 |
| Reviewed wording | P01 is a public, non-clinical data-foundation and execution-validation phase; it does not establish clinical effectiveness, patient benefit, deployment safety, or medical-device readiness. |
| Layer 0 disposition | REJECTED / P01-L0-DISP-012 |
| Origin phase | P01 |
| Finding(s) | P01-FIND-001; P01-FIND-012 |
| Protocol contract | P01-AC-001-SOURCE-INVENTORY; P01-AC-010-GATES-REPAIRS |
| Execution stage(s) | P01-STAGE-06; P01-STAGE-26 |
| Record(s) | IHARQ-DATASETRECORD-20260806-66309cda68771bef; IHARQ-DATASETRECORD-20260806-42c424800627b6ee; IHARQ-DATASETRECORD-20260806-adb91f25a65e588e |
| Record collections | NOT_APPLICABLE |
| Primary evidence | reports/phase_01/sources/source_version_license_report.json; gate_decision.json |
| External source refs | NOT_APPLICABLE |
| Negative/adverse evidence | P01-NEG-CLINICAL-DEPLOYMENT-NOT-SUPPORTED |
| Ablation relevance | NOT_APPLICABLE |
| Limitations | PUBLIC_EEG_ONLY; NON_CLINICAL; NO_DEPLOYMENT_CLAIM |
| Claim ceiling | NON_CLINICAL_NO_DEPLOYMENT_CLAIM |
| Allowed manuscript use | PROVISIONAL_LIMITATIONS_OR_CLAIM_BOUNDARY / PROVISIONAL_LIMITATIONS_OR_CLAIM_BOUNDARY |
| Figure/table/card eligibility | Figures: P01-FIG-SRC-009; Tables: PENDING_LAYER10:NEGATIVE_DEFERRED_CLAIMS; Cards: PENDING_LAYER10 |
| Reproduction route | IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip |
| Lifecycle | REJECTED_PROHIBITED_AS_SUPPORTED |
| Forbidden stronger wording | The P01 data foundation demonstrates clinical effectiveness or deployment safety. |

# PART IV — SPECIAL GOVERNED SURFACES

## 26. A0–A13 Evidence Map
| Ablation | Official identity | P00 state | P01 state | Execution | Reviewed claims | Future phase | Map status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A0 | Raw Decoder / Accept-All Raw Decoder Reference | READINESS_ONLY_NOT_ACTIVATED | FOUNDATION_READY | NOT_EXECUTED_IN_P01 | P01-CLM-006/v1 | P02-P15 | FOUNDATION_READY_NOT_EFFECTIVENESS |
| A1 | Calibrated Decoder / Calibration Visibility | READINESS_ONLY_NOT_ACTIVATED | FOUNDATION_READY | NOT_EXECUTED_IN_P01 | P01-CLM-006/v1 | P02-P15 | FOUNDATION_READY_NOT_EFFECTIVENESS |
| A2 | Simple Registered Threshold / Confidence-Threshold Baseline | READINESS_ONLY_NOT_ACTIVATED | FOUNDATION_READY | NOT_EXECUTED_IN_P01 | P01-CLM-006/v1 | P02-P15 | FOUNDATION_READY_NOT_EFFECTIVENESS |
| A3 | Uncertainty and Selective Prediction | READINESS_ONLY_NOT_ACTIVATED | FOUNDATION_READY | NOT_EXECUTED_IN_P01 | P01-CLM-006/v1 | P02-P15 | FOUNDATION_READY_NOT_EFFECTIVENESS |
| A4 | Longer-Window, Multi-Window Voting/Averaging and Ordinary Ensemble Controls | READINESS_ONLY_NOT_ACTIVATED | FOUNDATION_READY | NOT_EXECUTED_IN_P01 | P01-CLM-006/v1;P01-CLM-007/v1;P01-CLM-011/v1 | P02-P15 | FOUNDATION_READY_NOT_EFFECTIVENESS |
| A5 | IHARQ-lite / Rule-Based Evidence Verification | READINESS_ONLY_NOT_ACTIVATED | FOUNDATION_READY | NOT_EXECUTED_IN_P01 | P01-CLM-006/v1 | P02-P15 | FOUNDATION_READY_NOT_EFFECTIVENESS |
| A6 | IHARQ + Evidence-Quality Estimator | READINESS_ONLY_NOT_ACTIVATED | FOUNDATION_READY | NOT_EXECUTED_IN_P01 | P01-CLM-006/v1 | P02-P15 | FOUNDATION_READY_NOT_EFFECTIVENESS |
| A7 | IHARQ + RegimeRisk Temporal Trust | READINESS_ONLY_NOT_ACTIVATED | FOUNDATION_READY | NOT_EXECUTED_IN_P01 | P01-CLM-006/v1 | P02-P15 | FOUNDATION_READY_NOT_EFFECTIVENESS |
| A8 | Learning-to-defer / Deferral Comparison | READINESS_ONLY_NOT_ACTIVATED | FOUNDATION_READY | NOT_EXECUTED_IN_P01 | P01-CLM-006/v1 | P02-P15 | FOUNDATION_READY_NOT_EFFECTIVENESS |
| A9 | Supervised Adaptive-IHARQ / Adaptive Readiness Policy | READINESS_ONLY_NOT_ACTIVATED | FOUNDATION_READY | NOT_EXECUTED_IN_P01 | P01-CLM-006/v1 | P02-P15 | FOUNDATION_READY_NOT_EFFECTIVENESS |
| A10 | Contextual Bandit / Simulation-Bounded Immediate-Reward Adaptation | READINESS_ONLY_NOT_ACTIVATED | FOUNDATION_READY | NOT_EXECUTED_IN_P01 | P01-CLM-006/v1 | P02-P15 | FOUNDATION_READY_NOT_EFFECTIVENESS |
| A11 | Reinforcement-Learning Policy / Simulation-Bounded Sequential Policy Learning | READINESS_ONLY_NOT_ACTIVATED | FOUNDATION_READY | NOT_EXECUTED_IN_P01 | P01-CLM-006/v1 | P02-P15 | FOUNDATION_READY_NOT_EFFECTIVENESS |
| A12 | StressForge Stress Tests / Controlled Stress Robustness | READINESS_ONLY_NOT_ACTIVATED | FOUNDATION_READY | NOT_EXECUTED_IN_P01 | P01-CLM-006/v1 | P02-P15 | FOUNDATION_READY_NOT_EFFECTIVENESS |
| A13 | Layer 9 Simulation-Only Embodiment Demo | READINESS_ONLY_NOT_ACTIVATED | FOUNDATION_READY | NOT_EXECUTED_IN_P01 | P01-CLM-006/v1 | P02-P15 | FOUNDATION_READY_NOT_EFFECTIVENESS |

## 27. A14 Prohibition
`A14 = ABSENT / PROHIBITED`. It is not a positive experiment, readiness row, or supported claim. Any A14 occurrence in downstream outputs must retain this negative/prohibitory meaning.

## 28. A4 R2 Evidence Map
A4 is pinned to `P01-L1-A4-WINDOW-FAMILY-FREEZE-R2` with materialized profile `A4_LONG_MATCHED_3P5S_R2` (+0.0 to +3.5 s, 560 samples @160 Hz) and virtual profile `A4_MULTI_3X2S_UNIFORM_0P75S_R2` (0:320, 120:440, 240:560). The artifact `P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13` has 12,910/12,910 matched parents, 172 shards, no padding/clipping/fabrication/parent loss, and manifest `29124d59907610b1545e0a2b5d1811a4d4a2bf1df64cad49aa880f4721c47305`. Its map ceiling is substrate readiness only; `P01-CLM-011/v1` preserves the deferred effectiveness question.

## 29. Clinical / Deployment Claim Boundary
`P01-CLM-012/v1` is rejected as a supported clinical/deployment claim. Its lawful map destinations are limitations, claim-boundary statements, and negative/prohibited-claim views. `PUBLIC_EEG_ONLY`, `NON_CLINICAL`, and `NO_DEPLOYMENT_CLAIM` must propagate anywhere P01 could be clinically misread.

## 30. Leakage Claim Boundary
The split/leakage claim must retain the phrase **under the implemented registered checks** or equivalent exact Layer 0 wording. `no leakage` or `leakage is impossible` is not an authorized short form.

## 31. Quality Warning Boundary
Any quality visual/table/card must preserve `SOFT_FLAG_NOT_EQUIVALENT_TO_CORRUPTION`: 20 soft/provider flags are not equivalent to 20 corrupt recordings, and 0 hard-invalid summaries is not evidence of artifact-free EEG.

## 32. Environment / Resource Amendment Mapping
The execution environment is pinned to Python 3.12.13, `P01-L1-KAGGLE-ENV-FREEZE-R5`, and `P01-L1-KAGGLE-ADAPTIVE-DISK-R1`. This map links those amendments to P01 reproducibility; it does not infer scientific performance from them.

## 33. Repair / Negative Evidence Mapping
| Negative evidence | Related claims | Interpretation effect | Mandatory warning | Visibility |
| --- | --- | --- | --- | --- |
| P01-NEG-A4-4S-INFEASIBILITY | P01-CLM-007/v1;P01-CLM-011/v1 | The +4.0 s candidate profile was infeasible for one valid parent without 80 nonexistent samples; R2 +3.5 s preserves all 12,910 parents. | A4 R2 has retrospective feasibility origin; readiness is not effectiveness. | A4 figure captions; limitation/future-work; negative-result view |
| P01-NEG-A4-EFFECTIVENESS-NOT-EXECUTED | P01-CLM-007/v1;P01-CLM-011/v1 | No P01 decoder-effect comparison exists for A4. | Do not state A4 accuracy/AUROC/robustness superiority from P01. | Deferred claim register; A4 visuals; future work |
| P01-NEG-CLINICAL-DEPLOYMENT-NOT-SUPPORTED | P01-CLM-012/v1 | Public non-clinical data-foundation evidence cannot support clinical effectiveness or deployment safety. | PUBLIC_EEG_ONLY; NON_CLINICAL; NO_DEPLOYMENT_CLAIM | Claim-boundary/limitations; prohibited-claim view |
| P01-HISTORICAL-FAILED-EXECUTION | P01-CLM-008/v1 | Historical Stage 07/18/26 failures are repair/reentry evidence, not the source for the final positive execution-closure claim. | Use current accepted evidence for positive claims; preserve failed attempts as historical lineage. | Reproducibility/audit chronology only |
| P01-QUALITY-SOFT-FLAGS | P01-CLM-005/v1 | 20 soft/provider flags remain visible but do not equal hard invalidity or corruption. | SOFT_FLAG_NOT_EQUIVALENT_TO_CORRUPTION | Quality tables/figures/cards and limitations |
| P01-EXTERNAL-ACCESS-LIMIT | P01-CLM-004/v1;P01-CLM-007/v1;P01-CLM-010/v1 | Core/A4 numerical bytes require private Kaggle access and source-license compliance. | PRIVATE_KAGGLE_EXTERNAL_ARTIFACT_ACCESS; SOURCE_LICENSE_REDISTRIBUTION_CONSTRAINTS | Reproduction package and artifact cards |

# PART V — CUMULATIVE THROUGH-P01 MAP

## 34. Cumulative Claim / Evidence Matrix
| Claim | Phase | Disposition | Finding(s) | Protocol / execution | Evidence assets | Limitations | Placement | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P00-CLM-001/v2 | P00 | APPROVE_WITH_QUALIFICATIONS | P00-F-001 | P00_PROTOCOL_MODE_B_ENGINEERING_FOUNDATION; P00-EXECUTION-RELEASE-R2 | P00_EVIDENCE_MAP_PREDECESSOR_ROW:P00-CLM-001/v2; P00_ANALYSIS_RELEASE:P00-ANALYSIS-RELEASE-R2 | P00-LIM-002; P00-LIM-003; P00-LIM-004; P00-LIM-L0-001 | Methods or Reproducibility Statement Only | PRESERVED_UNCHANGED |
| P00-CLM-002/v2 | P00 | APPROVE_WITH_QUALIFICATIONS | P00-F-002 | P00_PROTOCOL_MODE_B_ENGINEERING_FOUNDATION; P00-EXECUTION-RELEASE-R2 | P00_EVIDENCE_MAP_PREDECESSOR_ROW:P00-CLM-002/v2; P00_ANALYSIS_RELEASE:P00-ANALYSIS-RELEASE-R2 | P00-LIM-001; P00-LIM-002; P00-LIM-003; P00-LIM-004 | Methods or Reproducibility Statement Only | PRESERVED_UNCHANGED |
| P00-CLM-003/v2 | P00 | APPROVE_WITH_QUALIFICATIONS | P00-F-003; P00-F-004 | P00_PROTOCOL_MODE_B_ENGINEERING_FOUNDATION; P00-EXECUTION-RELEASE-R2 | P00_EVIDENCE_MAP_PREDECESSOR_ROW:P00-CLM-003/v2; P00_ANALYSIS_RELEASE:P00-ANALYSIS-RELEASE-R2 | P00-LIM-004; P00-LIM-L0-001 | Methods or Reproducibility Statement Only | PRESERVED_UNCHANGED |
| P00-CLM-004/v2 | P00 | APPROVE_WITH_QUALIFICATIONS | P00-F-005 | P00_PROTOCOL_MODE_B_ENGINEERING_FOUNDATION; P00-EXECUTION-RELEASE-R2 | P00_EVIDENCE_MAP_PREDECESSOR_ROW:P00-CLM-004/v2; P00_ANALYSIS_RELEASE:P00-ANALYSIS-RELEASE-R2 | P00-LIM-004; P00-LIM-L0-001 | Methods or Reproducibility Statement Only | PRESERVED_UNCHANGED |
| P00-CLM-005/v2 | P00 | APPROVE_WITH_QUALIFICATIONS | P00-F-006 | P00_PROTOCOL_MODE_B_ENGINEERING_FOUNDATION; P00-EXECUTION-RELEASE-R2 | P00_EVIDENCE_MAP_PREDECESSOR_ROW:P00-CLM-005/v2; P00_ANALYSIS_RELEASE:P00-ANALYSIS-RELEASE-R2 | P00-LIM-003; P00-LIM-004; P00-LIM-L0-001 | Methods or Reproducibility Statement Only | PRESERVED_UNCHANGED |
| P00-CLM-006/v2 | P00 | APPROVE_WITH_QUALIFICATIONS | P00-F-007 | P00_PROTOCOL_MODE_B_ENGINEERING_FOUNDATION; P00-EXECUTION-RELEASE-R2 | P00_EVIDENCE_MAP_PREDECESSOR_ROW:P00-CLM-006/v2; P00_ANALYSIS_RELEASE:P00-ANALYSIS-RELEASE-R2 | P00-LIM-003; P00-LIM-004; P00-LIM-L0-001 | Methods or Reproducibility Statement Only | PRESERVED_UNCHANGED |
| P00-CLM-007/v2 | P00 | APPROVE_WITH_QUALIFICATIONS | P00-F-008 | P00_PROTOCOL_MODE_B_ENGINEERING_FOUNDATION; P00-EXECUTION-RELEASE-R2 | P00_EVIDENCE_MAP_PREDECESSOR_ROW:P00-CLM-007/v2; P00_ANALYSIS_RELEASE:P00-ANALYSIS-RELEASE-R2 | P00-LIM-001; P00-LIM-002; P00-LIM-003 | Methods or Reproducibility Statement Only | PRESERVED_UNCHANGED |
| P01-CLM-001/v1 | P01 | APPROVED_WITH_QUALIFICATIONS | P01-FIND-001 | P01-AC-001-SOURCE-INVENTORY; P01-STAGE-05; P01-STAGE-06; P01-STAGE-07 | records/datasets/BNCI2014_001/IHARQ-DATASETRECORD-20260806-42c424800627b6ee.json; records/datasets/Lee2019_MI/IHARQ-DATASETRECORD-20260806-adb91f25a65e588e.json | PUBLIC_EEG_ONLY; NON_CLINICAL; BINARY_MI_BRANCH_SCOPE | PROVISIONAL_METHODS_DATA | QUALIFIED_CURRENT |
| P01-CLM-002/v1 | P01 | APPROVED_WITH_QUALIFICATIONS | P01-FIND-002; P01-FIND-006 | P01-AC-002-SPLIT; P01-AC-005-LEAKAGE; P01-STAGE-11; P01-STAGE-17 | records/splits/P01-L1-SPLIT-OFFICIAL-R2/IHARQ-SPLITRECORD-20260806-e4e371d332c61e36.json; reports/phase_01/splits/disjointness.json | IMPLEMENTED_CHECKS_ONLY | PROVISIONAL_METHODS_SPLIT_AND_LEAKAGE | QUALIFIED_CURRENT |
| P01-CLM-003/v1 | P01 | APPROVED | P01-FIND-003 | P01-AC-003-DENOMINATOR; P01-STAGE-13; P01-STAGE-14; P01-STAGE-16 | P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473 | NO_MODEL_EFFECT_INFERENCE | PROVISIONAL_RESULTS_DATA_FOUNDATION | CURRENT_SUPPORTED |
| P01-CLM-004/v1 | P01 | APPROVED_WITH_QUALIFICATIONS | P01-FIND-004 | P01-AC-006-EXTERNAL; P01-STAGE-14; P01-STAGE-15; P01-STAGE-20 | P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473 | PRIVATE_KAGGLE_EXTERNAL_ARTIFACT_ACCESS; SOURCE_LICENSE_REDISTRIBUTION_CONSTRAINTS | PROVISIONAL_METHODS_REPRODUCIBILITY | QUALIFIED_CURRENT |
| P01-CLM-005/v1 | P01 | APPROVED_WITH_QUALIFICATIONS | P01-FIND-005 | P01-AC-004-QUALITY; P01-STAGE-13; P01-STAGE-16 | reports/phase_01/quality/quality_coverage.json; records/quality/ | SOFT_FLAG_NOT_EQUIVALENT_TO_CORRUPTION | PROVISIONAL_RESULTS_DATA_QUALITY | QUALIFIED_CURRENT |
| P01-CLM-006/v1 | P01 | APPROVED_WITH_QUALIFICATIONS | P01-FIND-008 | P01-AC-007-ABLATION-READINESS; P01-STAGE-18 | manifests/phase_01/layer1_ablation_readiness_l1_v1.json | NO_ABLATION_EFFECTIVENESS_IN_P01 | PROVISIONAL_METHODS_ABLATION_READINESS | QUALIFIED_CURRENT |
| P01-CLM-007/v1 | P01 | APPROVED_WITH_QUALIFICATIONS | P01-FIND-009; P01-FIND-010 | P01-AC-008-A4; P01-STAGE-14; P01-STAGE-15; P01-STAGE-18 | P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13 | A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01; A4_EFFECTIVENESS_NOT_EXECUTED | PROVISIONAL_RESULTS_DATA_FOUNDATION_WITH_PROXIMATE_A4_WARNING | QUALIFIED_CURRENT |
| P01-CLM-008/v1 | P01 | APPROVED | P01-FIND-012 | P01-AC-010-GATES-REPAIRS; P01-STAGE-04; P01-STAGE-23; P01-STAGE-24; P01-STAGE-26 | reports/phase_01/tests/stage_results.json; gate_decision.json | NO_EFFECTIVENESS_INFERENCE | PROVISIONAL_METHODS_REPRODUCIBILITY | CURRENT_SUPPORTED |
| P01-CLM-009/v1 | P01 | APPROVED_WITH_QUALIFICATIONS | P01-FIND-011 | P01-AC-009-ENVIRONMENT; P01-STAGE-01; P01-STAGE-03 | environment_manifest.json; environment_amendment.json | ACTUAL_RUNTIME_PYTHON_3_12_13_WITH_COMPATIBILITY_AMENDMENT; ADAPTIVE_DISK_RESOURCE_AMENDMENT | PROVISIONAL_METHODS_REPRODUCIBILITY | QUALIFIED_CURRENT |
| P01-CLM-010/v1 | P01 | APPROVED_WITH_QUALIFICATIONS | P01-FIND-014 | P01-AC-003-DENOMINATOR; P01-AC-005-LEAKAGE; P01-AC-006-EXTERNAL; P01-AC-007-ABLATION-READINESS; P01-AC-010-GATES-REPAIRS; P01-STAGE-22; P01-STAGE-23; P01-STAGE-26 | P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473; P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13 | DOCUMENTARY_CLOSURE_SEQUENCE_REMAINS | PROVISIONAL_METHODS_DOWNSTREAM_HANDOFF | QUALIFIED_CURRENT |
| P01-CLM-011/v1 | P01 | DEFERRED | P01-FIND-009 | P01-AC-008-A4; P01-STAGE-14; P01-STAGE-15 | P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13 | A4_EFFECTIVENESS_NOT_EXECUTED; A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01 | PROVISIONAL_FUTURE_WORK_OR_LIMITATIONS | DEFERRED_NOT_MAPPABLE_AS_SUPPORTED |
| P01-CLM-012/v1 | P01 | REJECTED | P01-FIND-001; P01-FIND-012 | P01-AC-001-SOURCE-INVENTORY; P01-AC-010-GATES-REPAIRS; P01-STAGE-06; P01-STAGE-26 | reports/phase_01/sources/source_version_license_report.json; gate_decision.json | PUBLIC_EEG_ONLY; NON_CLINICAL; NO_DEPLOYMENT_CLAIM | PROVISIONAL_LIMITATIONS_OR_CLAIM_BOUNDARY | REJECTED_PROHIBITED_AS_SUPPORTED |

## 35. P00 → P01 Continuity
| Concept | P00 evidence / claim state | P01 inherited use | P01 new evidence / reviewed claim | Cumulative status |
| --- | --- | --- | --- | --- |
| Record infrastructure | P00 artifact/schema/record foundation claims | Canonical Dataset/Label/Split/Preprocessing/Window records | P01-CLM-001/v1; P01-CLM-010/v1 | CURRENT |
| Hashing / provenance | P00 reproducibility and artifact-closure claims | Source and derived artifact identity | P01-CLM-001/v1; P01-CLM-004/v1 | CURRENT |
| Validation | P00 deterministic validation | P01 split/quality/leakage/gate validation | P01-CLM-002/v1;005/v1;008/v1 | CURRENT |
| A0–A13 framework | P00 readiness-only, not activated | Layer-1 readiness rows | P01-CLM-006/v1; A4 claim 007 | FOUNDATION_READY |
| A14 rule | Rejected/absent | No A14 introduced | P01-CLM-006/v1 | ABSENT_PROHIBITED |
| Reproducibility model | P00 exact local reproduction | P01 Kaggle environment + external artifacts + checksum closure | P01-CLM-004/v1;008/v1;009/v1 | CURRENT |

## 36. Cumulative Limitation / Warning Matrix
| Limitation | Origin | Affected claims | Required proximity | Layer 10 warning | Downstream inheritance |
| --- | --- | --- | --- | --- | --- |
| P00-LIM-002 | P00 | P00-CLM-001/v2 | PRESERVE_EXISTING_P00_R2 | PRESENT | PRESERVE_EXISTING_P00_R2 |
| P00-LIM-003 | P00 | P00-CLM-001/v2 | PRESERVE_EXISTING_P00_R2 | PRESENT | PRESERVE_EXISTING_P00_R2 |
| P00-LIM-004 | P00 | P00-CLM-001/v2 | PRESERVE_EXISTING_P00_R2 | PRESENT | PRESERVE_EXISTING_P00_R2 |
| P00-LIM-L0-001 | P00 | P00-CLM-001/v2 | PRESERVE_EXISTING_P00_R2 | PRESENT | PRESERVE_EXISTING_P00_R2 |
| P00-LIM-001 | P00 | P00-CLM-002/v2 | PRESERVE_EXISTING_P00_R2 | PRESENT | PRESERVE_EXISTING_P00_R2 |
| P00-LIM-002 | P00 | P00-CLM-002/v2 | PRESERVE_EXISTING_P00_R2 | PRESENT | PRESERVE_EXISTING_P00_R2 |
| P00-LIM-003 | P00 | P00-CLM-002/v2 | PRESERVE_EXISTING_P00_R2 | PRESENT | PRESERVE_EXISTING_P00_R2 |
| P00-LIM-004 | P00 | P00-CLM-002/v2 | PRESERVE_EXISTING_P00_R2 | PRESENT | PRESERVE_EXISTING_P00_R2 |
| P00-LIM-004 | P00 | P00-CLM-003/v2 | PRESERVE_EXISTING_P00_R2 | PRESENT | PRESERVE_EXISTING_P00_R2 |
| P00-LIM-L0-001 | P00 | P00-CLM-003/v2 | PRESERVE_EXISTING_P00_R2 | PRESENT | PRESERVE_EXISTING_P00_R2 |
| P00-LIM-004 | P00 | P00-CLM-004/v2 | PRESERVE_EXISTING_P00_R2 | PRESENT | PRESERVE_EXISTING_P00_R2 |
| P00-LIM-L0-001 | P00 | P00-CLM-004/v2 | PRESERVE_EXISTING_P00_R2 | PRESENT | PRESERVE_EXISTING_P00_R2 |
| P00-LIM-003 | P00 | P00-CLM-005/v2 | PRESERVE_EXISTING_P00_R2 | PRESENT | PRESERVE_EXISTING_P00_R2 |
| P00-LIM-004 | P00 | P00-CLM-005/v2 | PRESERVE_EXISTING_P00_R2 | PRESENT | PRESERVE_EXISTING_P00_R2 |
| P00-LIM-L0-001 | P00 | P00-CLM-005/v2 | PRESERVE_EXISTING_P00_R2 | PRESENT | PRESERVE_EXISTING_P00_R2 |
| P00-LIM-003 | P00 | P00-CLM-006/v2 | PRESERVE_EXISTING_P00_R2 | PRESENT | PRESERVE_EXISTING_P00_R2 |
| P00-LIM-004 | P00 | P00-CLM-006/v2 | PRESERVE_EXISTING_P00_R2 | PRESENT | PRESERVE_EXISTING_P00_R2 |
| P00-LIM-L0-001 | P00 | P00-CLM-006/v2 | PRESERVE_EXISTING_P00_R2 | PRESENT | PRESERVE_EXISTING_P00_R2 |
| P00-LIM-001 | P00 | P00-CLM-007/v2 | PRESERVE_EXISTING_P00_R2 | PRESENT | PRESERVE_EXISTING_P00_R2 |
| P00-LIM-002 | P00 | P00-CLM-007/v2 | PRESERVE_EXISTING_P00_R2 | PRESENT | PRESERVE_EXISTING_P00_R2 |
| P00-LIM-003 | P00 | P00-CLM-007/v2 | PRESERVE_EXISTING_P00_R2 | PRESENT | PRESERVE_EXISTING_P00_R2 |
| PUBLIC_EEG_ONLY | P01 | P01-CLM-001/v1;P01-CLM-012/v1 | MANDATORY_IN_CLAIM_OR_PROXIMATE_CONTEXT_AND_CAPTION_WHERE_RELEVANT | MANDATORY | P02-P15; Layer 0 |
| NON_CLINICAL | P01 | P01-CLM-001/v1;P01-CLM-012/v1 | MANDATORY_IN_CLAIM_OR_PROXIMATE_CONTEXT_AND_CAPTION_WHERE_RELEVANT | MANDATORY | All claim-bearing outputs |
| BINARY_MI_BRANCH_SCOPE | P01 | P01-CLM-001/v1 | MANDATORY_IN_PROXIMATE_CONTEXT | MANDATORY | P02-P15 |
| IMPLEMENTED_CHECKS_ONLY | P01 | P01-CLM-002/v1 | MANDATORY_IN_CLAIM_OR_PROXIMATE_CONTEXT_AND_CAPTION_WHERE_RELEVANT | MANDATORY | P02-P15 |
| NO_MODEL_EFFECT_INFERENCE | P01 | P01-CLM-003/v1 | MANDATORY_IN_PROXIMATE_CONTEXT | MANDATORY | P02-P15 |
| PRIVATE_KAGGLE_EXTERNAL_ARTIFACT_ACCESS | P01 | P01-CLM-004/v1 | MANDATORY_IN_PROXIMATE_CONTEXT | MANDATORY | P02-P15 reproducibility |
| SOURCE_LICENSE_REDISTRIBUTION_CONSTRAINTS | P01 | P01-CLM-004/v1 | MANDATORY_IN_PROXIMATE_CONTEXT | MANDATORY | Repository/release packaging |
| SOFT_FLAG_NOT_EQUIVALENT_TO_CORRUPTION | P01 | P01-CLM-005/v1 | MANDATORY_IN_CLAIM_OR_PROXIMATE_CONTEXT_AND_CAPTION_WHERE_RELEVANT | MANDATORY | P02-P15 |
| NO_ABLATION_EFFECTIVENESS_IN_P01 | P01 | P01-CLM-006/v1 | MANDATORY_IN_PROXIMATE_CONTEXT | MANDATORY | P02-P15 |
| A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01 | P01 | P01-CLM-007/v1;P01-CLM-011/v1 | MANDATORY_IN_CLAIM_OR_PROXIMATE_CONTEXT_AND_CAPTION_WHERE_RELEVANT | MANDATORY | P02 A4 and Layer 0 |
| A4_EFFECTIVENESS_NOT_EXECUTED | P01 | P01-CLM-007/v1;P01-CLM-011/v1 | MANDATORY_IN_CLAIM_OR_PROXIMATE_CONTEXT_AND_CAPTION_WHERE_RELEVANT | MANDATORY | P02-P15 |
| NO_EFFECTIVENESS_INFERENCE | P01 | P01-CLM-008/v1 | MANDATORY_IN_PROXIMATE_CONTEXT | MANDATORY | P02-P15 |
| ACTUAL_RUNTIME_PYTHON_3_12_13_WITH_COMPATIBILITY_AMENDMENT | P01 | P01-CLM-009/v1 | MANDATORY_IN_PROXIMATE_CONTEXT | MANDATORY | Reproduction |
| ADAPTIVE_DISK_RESOURCE_AMENDMENT | P01 | P01-CLM-009/v1 | MANDATORY_IN_PROXIMATE_CONTEXT | MANDATORY | Reproduction |
| DOCUMENTARY_CLOSURE_SEQUENCE_REMAINS | P01 | P01-CLM-010/v1 | MANDATORY_IN_PROXIMATE_CONTEXT | MANDATORY | P02-P15 |
| NO_DEPLOYMENT_CLAIM | P01 | P01-CLM-012/v1 | MANDATORY_IN_CLAIM_OR_PROXIMATE_CONTEXT_AND_CAPTION_WHERE_RELEVANT | MANDATORY | Layer 0 and later deployment-related phases |

## 37. Cumulative Manuscript Placement Map
| Claim | Phase | Paper | Thesis | Appendix | Status |
| --- | --- | --- | --- | --- | --- |
| P00-CLM-001/v2 | P00 | Methods or Reproducibility Statement Only | Methods / Phase 0 Foundation and Reproducibility | Phase 0 foundation/reproducibility appendix — item 1 | SUPPORTED_PLACEMENT |
| P00-CLM-002/v2 | P00 | Methods or Reproducibility Statement Only | Methods / Phase 0 Foundation and Reproducibility | Phase 0 foundation/reproducibility appendix — item 2 | SUPPORTED_PLACEMENT |
| P00-CLM-003/v2 | P00 | Methods or Reproducibility Statement Only | Methods / Phase 0 Foundation and Reproducibility | Phase 0 foundation/reproducibility appendix — item 3 | SUPPORTED_PLACEMENT |
| P00-CLM-004/v2 | P00 | Methods or Reproducibility Statement Only | Methods / Phase 0 Foundation and Reproducibility | Phase 0 foundation/reproducibility appendix — item 4 | SUPPORTED_PLACEMENT |
| P00-CLM-005/v2 | P00 | Methods or Reproducibility Statement Only | Methods / Phase 0 Foundation and Reproducibility | Phase 0 foundation/reproducibility appendix — item 5 | SUPPORTED_PLACEMENT |
| P00-CLM-006/v2 | P00 | Methods or Reproducibility Statement Only | Methods / Phase 0 Foundation and Reproducibility | Phase 0 foundation/reproducibility appendix — item 6 | SUPPORTED_PLACEMENT |
| P00-CLM-007/v2 | P00 | Methods or Reproducibility Statement Only | Methods / Phase 0 Foundation and Reproducibility | Phase 0 foundation/reproducibility appendix — item 7 | SUPPORTED_PLACEMENT |
| P01-CLM-001/v1 | P01 | PROVISIONAL_METHODS_DATA | PROVISIONAL_METHODS_DATA_FOUNDATION | PENDING_FINAL_MANUSCRIPT_STRUCTURE | SUPPORTED_PLACEMENT |
| P01-CLM-002/v1 | P01 | PROVISIONAL_METHODS_SPLIT_AND_LEAKAGE | PROVISIONAL_METHODS_SPLIT_AND_LEAKAGE | PENDING_FINAL_MANUSCRIPT_STRUCTURE | SUPPORTED_PLACEMENT |
| P01-CLM-003/v1 | P01 | PROVISIONAL_RESULTS_DATA_FOUNDATION | PROVISIONAL_RESULTS_DATA_FOUNDATION | PENDING_FINAL_MANUSCRIPT_STRUCTURE | SUPPORTED_PLACEMENT |
| P01-CLM-004/v1 | P01 | PROVISIONAL_METHODS_REPRODUCIBILITY | PROVISIONAL_REPRODUCIBILITY | PENDING_FINAL_MANUSCRIPT_STRUCTURE | SUPPORTED_PLACEMENT |
| P01-CLM-005/v1 | P01 | PROVISIONAL_RESULTS_DATA_QUALITY | PROVISIONAL_RESULTS_DATA_QUALITY | PENDING_FINAL_MANUSCRIPT_STRUCTURE | SUPPORTED_PLACEMENT |
| P01-CLM-006/v1 | P01 | PROVISIONAL_METHODS_ABLATION_READINESS | PROVISIONAL_METHODS_ABLATION_READINESS | PENDING_FINAL_MANUSCRIPT_STRUCTURE | SUPPORTED_PLACEMENT |
| P01-CLM-007/v1 | P01 | PROVISIONAL_RESULTS_DATA_FOUNDATION_WITH_PROXIMATE_A4_WARNING | PROVISIONAL_RESULTS_A4_FOUNDATION_WITH_PROXIMATE_WARNING | PENDING_FINAL_MANUSCRIPT_STRUCTURE | SUPPORTED_PLACEMENT |
| P01-CLM-008/v1 | P01 | PROVISIONAL_METHODS_REPRODUCIBILITY | PROVISIONAL_REPRODUCIBILITY_AND_AUDIT | PENDING_FINAL_MANUSCRIPT_STRUCTURE | SUPPORTED_PLACEMENT |
| P01-CLM-009/v1 | P01 | PROVISIONAL_METHODS_REPRODUCIBILITY | PROVISIONAL_REPRODUCIBILITY_ENVIRONMENT | PENDING_FINAL_MANUSCRIPT_STRUCTURE | SUPPORTED_PLACEMENT |
| P01-CLM-010/v1 | P01 | PROVISIONAL_METHODS_DOWNSTREAM_HANDOFF | PROVISIONAL_DOWNSTREAM_READINESS | PENDING_FINAL_MANUSCRIPT_STRUCTURE | SUPPORTED_PLACEMENT |
| P01-CLM-011/v1 | P01 | PROVISIONAL_FUTURE_WORK_OR_LIMITATIONS | PROVISIONAL_FUTURE_WORK_OR_LIMITATIONS | PENDING_FINAL_MANUSCRIPT_STRUCTURE | FUTURE_WORK_OR_LIMITATIONS_ONLY |
| P01-CLM-012/v1 | P01 | PROVISIONAL_LIMITATIONS_OR_CLAIM_BOUNDARY | PROVISIONAL_LIMITATIONS_OR_CLAIM_BOUNDARY | PENDING_FINAL_MANUSCRIPT_STRUCTURE | NOT_ELIGIBLE_AS_SUPPORTED_CLAIM |

## 38. Cumulative Figure / Table / Card Map
| Figure/source | Phase | Purpose | Claim(s) | Allowed interpretation | Caption warning | Layer 10 status |
| --- | --- | --- | --- | --- | --- | --- |
| P01-FIG-SRC-001 | P01 | P00→P01 progression | P01-CLM-001/v1 | Engineering foundation → empirical data foundation only | PUBLIC_EEG_ONLY; NON_CLINICAL; BINARY_MI_BRANCH_SCOPE | PENDING_LAYER10 |
| P01-FIG-SRC-002 | P01 | Source → accepted event → core window flow | P01-CLM-001/v1;P01-CLM-003/v1 | Denominator/accounting; not model performance | PUBLIC_EEG_ONLY; NON_CLINICAL; BINARY_MI_BRANCH_SCOPE;NO_MODEL_EFFECT_INFERENCE | PENDING_LAYER10 |
| P01-FIG-SRC-003 | P01 | Subject split allocation | P01-CLM-002/v1 | Split structure only | IMPLEMENTED_CHECKS_ONLY | PENDING_LAYER10 |
| P01-FIG-SRC-005 | P01 | Core denominator conservation | P01-CLM-003/v1;P01-CLM-004/v1 | Materialization closure | NO_MODEL_EFFECT_INFERENCE;PRIVATE_KAGGLE_EXTERNAL_ARTIFACT_ACCESS; SOURCE_LICENSE_REDISTRIBUTION_CONSTRAINTS | PENDING_LAYER10 |
| P01-FIG-SRC-009 | P01 | Evidence ceiling | P01-CLM-006/v1;P01-CLM-012/v1 | Claim-boundary illustration | NO_ABLATION_EFFECTIVENESS_IN_P01;PUBLIC_EEG_ONLY; NON_CLINICAL; NO_DEPLOYMENT_CLAIM | PENDING_LAYER10 |
| P01-FIG-SRC-006 | P01 | Core vs A4 timing | P01-CLM-007/v1;P01-CLM-011/v1 | Timing/readiness only | A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01; A4_EFFECTIVENESS_NOT_EXECUTED;A4_EFFECTIVENESS_NOT_EXECUTED; A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01 | PENDING_LAYER10 |
| P01-FIG-SRC-007 | P01 | A4 R1 failure → R2 design | P01-CLM-007/v1;P01-CLM-011/v1 | Feasibility chronology; no effect claim | A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01; A4_EFFECTIVENESS_NOT_EXECUTED;A4_EFFECTIVENESS_NOT_EXECUTED; A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01 | PENDING_LAYER10 |
| P01-FIG-SRC-008 | P01 | Stage/repair chronology | P01-CLM-008/v1 | Execution history | NO_EFFECTIVENESS_INFERENCE | PENDING_LAYER10 |
| P01-FIG-SRC-010 | P01 | P01→P02 handoff graph | P01-CLM-010/v1 | Technical consumption contract | DOCUMENTARY_CLOSURE_SEQUENCE_REMAINS | PENDING_LAYER10 |
| P01-FIG-SRC-004 | P01 | Preprocessing chain | NO_DIRECT_REVIEWED_CLAIM_REQUIRED | Implementation contract only | Preserve evidence ceiling; no new scientific assertion. | PENDING_LAYER10 |

## 39. Cumulative Reproduction Asset Map
| Claim | Phase | Reproduction assets | Evidence paths | External artifacts | Status |
| --- | --- | --- | --- | --- | --- |
| P00-CLM-001/v2 | P00 | P00-EVIDENCE-MAP-RELEASE-R2;P00-BASIC-LAYER10-PACKAGE-R2;P00-EXECUTION-RELEASE-R2;P00-ANALYSIS-RELEASE-R2 | P00_EVIDENCE_MAP_PREDECESSOR_ROW:P00-CLM-001/v2;P00_ANALYSIS_RELEASE:P00-ANALYSIS-RELEASE-R2 |  | CURRENT |
| P00-CLM-002/v2 | P00 | P00-EVIDENCE-MAP-RELEASE-R2;P00-BASIC-LAYER10-PACKAGE-R2;P00-EXECUTION-RELEASE-R2;P00-ANALYSIS-RELEASE-R2 | P00_EVIDENCE_MAP_PREDECESSOR_ROW:P00-CLM-002/v2;P00_ANALYSIS_RELEASE:P00-ANALYSIS-RELEASE-R2 |  | CURRENT |
| P00-CLM-003/v2 | P00 | P00-EVIDENCE-MAP-RELEASE-R2;P00-BASIC-LAYER10-PACKAGE-R2;P00-EXECUTION-RELEASE-R2;P00-ANALYSIS-RELEASE-R2 | P00_EVIDENCE_MAP_PREDECESSOR_ROW:P00-CLM-003/v2;P00_ANALYSIS_RELEASE:P00-ANALYSIS-RELEASE-R2 |  | CURRENT |
| P00-CLM-004/v2 | P00 | P00-EVIDENCE-MAP-RELEASE-R2;P00-BASIC-LAYER10-PACKAGE-R2;P00-EXECUTION-RELEASE-R2;P00-ANALYSIS-RELEASE-R2 | P00_EVIDENCE_MAP_PREDECESSOR_ROW:P00-CLM-004/v2;P00_ANALYSIS_RELEASE:P00-ANALYSIS-RELEASE-R2 |  | CURRENT |
| P00-CLM-005/v2 | P00 | P00-EVIDENCE-MAP-RELEASE-R2;P00-BASIC-LAYER10-PACKAGE-R2;P00-EXECUTION-RELEASE-R2;P00-ANALYSIS-RELEASE-R2 | P00_EVIDENCE_MAP_PREDECESSOR_ROW:P00-CLM-005/v2;P00_ANALYSIS_RELEASE:P00-ANALYSIS-RELEASE-R2 |  | CURRENT |
| P00-CLM-006/v2 | P00 | P00-EVIDENCE-MAP-RELEASE-R2;P00-BASIC-LAYER10-PACKAGE-R2;P00-EXECUTION-RELEASE-R2;P00-ANALYSIS-RELEASE-R2 | P00_EVIDENCE_MAP_PREDECESSOR_ROW:P00-CLM-006/v2;P00_ANALYSIS_RELEASE:P00-ANALYSIS-RELEASE-R2 |  | CURRENT |
| P00-CLM-007/v2 | P00 | P00-EVIDENCE-MAP-RELEASE-R2;P00-BASIC-LAYER10-PACKAGE-R2;P00-EXECUTION-RELEASE-R2;P00-ANALYSIS-RELEASE-R2 | P00_EVIDENCE_MAP_PREDECESSOR_ROW:P00-CLM-007/v2;P00_ANALYSIS_RELEASE:P00-ANALYSIS-RELEASE-R2 |  | CURRENT |
| P01-CLM-001/v1 | P01 | IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip;d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f | records/datasets/BNCI2014_001/IHARQ-DATASETRECORD-20260806-42c424800627b6ee.json;records/datasets/Lee2019_MI/IHARQ-DATASETRECORD-20260806-adb91f25a65e588e.json;records/datasets/PhysioNetMI/IHARQ-DATASETRECORD-20260806-66309cda68771bef.json;reports/phase_01/sources/source_version_license_report.json |  | CURRENT |
| P01-CLM-002/v1 | P01 | IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip;d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f | records/splits/P01-L1-SPLIT-OFFICIAL-R2/IHARQ-SPLITRECORD-20260806-e4e371d332c61e36.json;reports/phase_01/splits/disjointness.json;reports/phase_01/leakage/leakage_contamination.json |  | CURRENT |
| P01-CLM-003/v1 | P01 | IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip;P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473;d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f | records/windows/;external_artifact_pointers/derived_windows_dataset.json | P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473 | CURRENT |
| P01-CLM-004/v1 | P01 | IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip;P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473;d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f | reports/phase_01/storage/existing_core_dataset_adoption.json;external_artifact_pointers/derived_windows_dataset.json | P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473 | CURRENT |
| P01-CLM-005/v1 | P01 | IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip;d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f | reports/phase_01/quality/quality_coverage.json;records/quality/ |  | CURRENT |
| P01-CLM-006/v1 | P01 | IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip;d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f | manifests/phase_01/layer1_ablation_readiness_l1_v1.json |  | CURRENT |
| P01-CLM-007/v1 | P01 | IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip;P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13;d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f | external_artifact_pointers/a4_window_family_dataset.json;reports/phase_01/storage/a4_derived_output_storage_actual_precommit.json;config_snapshot/p01_l1_a4_window_family_freeze_R2.json | P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13 | CURRENT |
| P01-CLM-008/v1 | P01 | IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip;d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f | reports/phase_01/tests/stage_results.json;gate_decision.json;reports/phase_01/tests/phase0_and_runtime_regression.json;reports/phase_01/repair_reentry.json;checksums.sha256 |  | CURRENT |
| P01-CLM-009/v1 | P01 | IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip;d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f | environment_manifest.json;environment_amendment.json |  | CURRENT |
| P01-CLM-010/v1 | P01 | IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip;P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473;P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13;d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f | handoffs/phase_01_to_phase_02.yaml;phase2_handoff/phase_01_to_phase_02.yaml | P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473;P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13 | CURRENT |
| P01-CLM-011/v1 | P01 | IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip;P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13;d03f0a7c869dd95a2a67e5a32edc501d52bfc3851d8e761ef56595d8bd1ff52f | external_artifact_pointers/a4_window_family_dataset.json;config_snapshot/p01_l1_a4_window_family_freeze_R2.json | P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13 | NEGATIVE_OR_DEFERRED_CONTEXT |
| P01-CLM-012/v1 | P01 | IHARQ_P01_L1_Phase_Execution_Bundle_d03f0a7c869d.zip | reports/phase_01/sources/source_version_license_report.json;gate_decision.json |  | NEGATIVE_OR_DEFERRED_CONTEXT |

## 40. Cumulative External Artifact Map
| Artifact | Provider dataset | Provider / logical revision | Manifest | Bytes | Access / license | Retrieval |
| --- | --- | --- | --- | --- | --- | --- |
| P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473 | csthv999z/iharq-p01-l1-derived-windows-d03f0a7c869d-20260806222242-68a91473 | 2 / 1 | dc21f418e9a1add62adb346f627d5d729735a5f1ecaa1d771f6fa5cfede627e1 | 1166652764 | PRIVATE Kaggle Dataset access + source-license compliance; INHERIT_EACH_SOURCE_LICENSE_AND_REDISTRIBUTION_CONSTRAINT_FROM_DATASET_RECORDS | Attach Kaggle provider dataset version 2 (IHARQ logical immutable revision 1); verify manifest SHA-256; load IHARQ_P01_L1_WINDOW_TO_SHARD_INDEX.jsonl; resolve shard filename; read declared HDF5 group/row. |
| P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13 | csthv999z/iharq-p01-l1-a4-d03f0a7c-9a7c6108 | 1 / 2 | 29124d59907610b1545e0a2b5d1811a4d4a2bf1df64cad49aa880f4721c47305 | 1357362334 | PRIVATE Kaggle Dataset access + source-license compliance; INHERIT_SOURCE_LICENSES_AND_REDISTRIBUTION_CONSTRAINTS | Attach exact private Kaggle Dataset provider version 1; verify manifest SHA-256; use registered A4 index/reader and R2 window-family freeze. |

# PART VI — LAYER 10 HANDOFF

## 41. Layer 10 Eligible Claims
| Claim | Disposition | Eligibility | Reviewed wording source |
| --- | --- | --- | --- |
| P00-CLM-001/v2 | APPROVE_WITH_QUALIFICATIONS | PRESERVED_EXISTING_LAYER10 | LAYER_0_REVIEWED_CLAIM |
| P00-CLM-002/v2 | APPROVE_WITH_QUALIFICATIONS | PRESERVED_EXISTING_LAYER10 | LAYER_0_REVIEWED_CLAIM |
| P00-CLM-003/v2 | APPROVE_WITH_QUALIFICATIONS | PRESERVED_EXISTING_LAYER10 | LAYER_0_REVIEWED_CLAIM |
| P00-CLM-004/v2 | APPROVE_WITH_QUALIFICATIONS | PRESERVED_EXISTING_LAYER10 | LAYER_0_REVIEWED_CLAIM |
| P00-CLM-005/v2 | APPROVE_WITH_QUALIFICATIONS | PRESERVED_EXISTING_LAYER10 | LAYER_0_REVIEWED_CLAIM |
| P00-CLM-006/v2 | APPROVE_WITH_QUALIFICATIONS | PRESERVED_EXISTING_LAYER10 | LAYER_0_REVIEWED_CLAIM |
| P00-CLM-007/v2 | APPROVE_WITH_QUALIFICATIONS | PRESERVED_EXISTING_LAYER10 | LAYER_0_REVIEWED_CLAIM |
| P01-CLM-001/v1 | APPROVED_WITH_QUALIFICATIONS | ELIGIBLE_WITH_MANDATORY_WARNING | LAYER_0_REVIEWED_CLAIM |
| P01-CLM-002/v1 | APPROVED_WITH_QUALIFICATIONS | ELIGIBLE_WITH_MANDATORY_WARNING | LAYER_0_REVIEWED_CLAIM |
| P01-CLM-003/v1 | APPROVED | ELIGIBLE_FOR_LAYER10 | LAYER_0_REVIEWED_CLAIM |
| P01-CLM-004/v1 | APPROVED_WITH_QUALIFICATIONS | ELIGIBLE_WITH_MANDATORY_WARNING | LAYER_0_REVIEWED_CLAIM |
| P01-CLM-005/v1 | APPROVED_WITH_QUALIFICATIONS | ELIGIBLE_WITH_MANDATORY_WARNING | LAYER_0_REVIEWED_CLAIM |
| P01-CLM-006/v1 | APPROVED_WITH_QUALIFICATIONS | ELIGIBLE_WITH_MANDATORY_WARNING | LAYER_0_REVIEWED_CLAIM |
| P01-CLM-007/v1 | APPROVED_WITH_QUALIFICATIONS | ELIGIBLE_WITH_MANDATORY_WARNING | LAYER_0_REVIEWED_CLAIM |
| P01-CLM-008/v1 | APPROVED | ELIGIBLE_FOR_LAYER10 | LAYER_0_REVIEWED_CLAIM |
| P01-CLM-009/v1 | APPROVED_WITH_QUALIFICATIONS | ELIGIBLE_WITH_MANDATORY_WARNING | LAYER_0_REVIEWED_CLAIM |
| P01-CLM-010/v1 | APPROVED_WITH_QUALIFICATIONS | ELIGIBLE_WITH_MANDATORY_WARNING | LAYER_0_REVIEWED_CLAIM |
| P01-CLM-011/v1 | DEFERRED | DEFERRED_NOT_ELIGIBLE_AS_SUPPORTED | LAYER_0_REVIEWED_CLAIM |
| P01-CLM-012/v1 | REJECTED | REJECTED_NOT_ELIGIBLE_AS_SUPPORTED | LAYER_0_REVIEWED_CLAIM |

## 42. Required Warnings
| Claim | Required warning / limitation |
| --- | --- |
| P00-CLM-001/v2 | Preserve P00 Mode B non-empirical engineering/foundation evidence ceiling and current qualified wording. |
| P00-CLM-002/v2 | Preserve P00 Mode B non-empirical engineering/foundation evidence ceiling and current qualified wording. |
| P00-CLM-003/v2 | Preserve P00 Mode B non-empirical engineering/foundation evidence ceiling and current qualified wording. |
| P00-CLM-004/v2 | Preserve P00 Mode B non-empirical engineering/foundation evidence ceiling and current qualified wording. |
| P00-CLM-005/v2 | Preserve P00 Mode B non-empirical engineering/foundation evidence ceiling and current qualified wording. |
| P00-CLM-006/v2 | Preserve P00 Mode B non-empirical engineering/foundation evidence ceiling and current qualified wording. |
| P00-CLM-007/v2 | Preserve P00 Mode B non-empirical engineering/foundation evidence ceiling and current qualified wording. |
| P01-CLM-001/v1 | PUBLIC_EEG_ONLY; NON_CLINICAL; BINARY_MI_BRANCH_SCOPE |
| P01-CLM-002/v1 | IMPLEMENTED_CHECKS_ONLY |
| P01-CLM-003/v1 | NO_MODEL_EFFECT_INFERENCE |
| P01-CLM-004/v1 | PRIVATE_KAGGLE_EXTERNAL_ARTIFACT_ACCESS; SOURCE_LICENSE_REDISTRIBUTION_CONSTRAINTS |
| P01-CLM-005/v1 | SOFT_FLAG_NOT_EQUIVALENT_TO_CORRUPTION |
| P01-CLM-006/v1 | NO_ABLATION_EFFECTIVENESS_IN_P01 |
| P01-CLM-007/v1 | A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01; A4_EFFECTIVENESS_NOT_EXECUTED |
| P01-CLM-008/v1 | NO_EFFECTIVENESS_INFERENCE |
| P01-CLM-009/v1 | ACTUAL_RUNTIME_PYTHON_3_12_13_WITH_COMPATIBILITY_AMENDMENT; ADAPTIVE_DISK_RESOURCE_AMENDMENT |
| P01-CLM-010/v1 | DOCUMENTARY_CLOSURE_SEQUENCE_REMAINS |
| P01-CLM-011/v1 | A4_EFFECTIVENESS_NOT_EXECUTED; A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01 |
| P01-CLM-012/v1 | PUBLIC_EEG_ONLY; NON_CLINICAL; NO_DEPLOYMENT_CLAIM |

## 43. Figure Source Registry
| Figure source ID | Purpose | Claims | Source artifacts | Status |
| --- | --- | --- | --- | --- |
| P01-FIG-SRC-001 | P00→P01 progression | P01-CLM-001/v1 | records/datasets/BNCI2014_001/IHARQ-DATASETRECORD-20260806-42c424800627b6ee.json;records/datasets/Lee2019_MI/IHARQ-DATASETRECORD-20260806-adb91f25a65e588e.json;records/datasets/PhysioNetMI/IHARQ-DATASETRECORD-20260806-66309cda68771bef.json;reports/phase_01/sources/source_version_license_report.json | PENDING_LAYER10 |
| P01-FIG-SRC-002 | Source → accepted event → core window flow | P01-CLM-001/v1;P01-CLM-003/v1 | records/datasets/BNCI2014_001/IHARQ-DATASETRECORD-20260806-42c424800627b6ee.json;records/datasets/Lee2019_MI/IHARQ-DATASETRECORD-20260806-adb91f25a65e588e.json;records/datasets/PhysioNetMI/IHARQ-DATASETRECORD-20260806-66309cda68771bef.json;reports/phase_01/sources/source_version_license_report.json;records/windows/;external_artifact_pointers/derived_windows_dataset.json | PENDING_LAYER10 |
| P01-FIG-SRC-003 | Subject split allocation | P01-CLM-002/v1 | records/splits/P01-L1-SPLIT-OFFICIAL-R2/IHARQ-SPLITRECORD-20260806-e4e371d332c61e36.json;reports/phase_01/splits/disjointness.json;reports/phase_01/leakage/leakage_contamination.json | PENDING_LAYER10 |
| P01-FIG-SRC-005 | Core denominator conservation | P01-CLM-003/v1;P01-CLM-004/v1 | records/windows/;external_artifact_pointers/derived_windows_dataset.json;reports/phase_01/storage/existing_core_dataset_adoption.json | PENDING_LAYER10 |
| P01-FIG-SRC-009 | Evidence ceiling | P01-CLM-006/v1;P01-CLM-012/v1 | manifests/phase_01/layer1_ablation_readiness_l1_v1.json;reports/phase_01/sources/source_version_license_report.json;gate_decision.json | PENDING_LAYER10 |
| P01-FIG-SRC-006 | Core vs A4 timing | P01-CLM-007/v1;P01-CLM-011/v1 | external_artifact_pointers/a4_window_family_dataset.json;reports/phase_01/storage/a4_derived_output_storage_actual_precommit.json;config_snapshot/p01_l1_a4_window_family_freeze_R2.json | PENDING_LAYER10 |
| P01-FIG-SRC-007 | A4 R1 failure → R2 design | P01-CLM-007/v1;P01-CLM-011/v1 | external_artifact_pointers/a4_window_family_dataset.json;reports/phase_01/storage/a4_derived_output_storage_actual_precommit.json;config_snapshot/p01_l1_a4_window_family_freeze_R2.json | PENDING_LAYER10 |
| P01-FIG-SRC-008 | Stage/repair chronology | P01-CLM-008/v1 | reports/phase_01/tests/stage_results.json;gate_decision.json;reports/phase_01/tests/phase0_and_runtime_regression.json;reports/phase_01/repair_reentry.json;checksums.sha256 | PENDING_LAYER10 |
| P01-FIG-SRC-010 | P01→P02 handoff graph | P01-CLM-010/v1 | handoffs/phase_01_to_phase_02.yaml;phase2_handoff/phase_01_to_phase_02.yaml | PENDING_LAYER10 |
| P01-FIG-SRC-004 | Preprocessing chain | NO_DIRECT_REVIEWED_CLAIM_REQUIRED | PreprocessingRecord | PENDING_LAYER10 |

## 44. Table Source Registry
P01 table families are governed logical sources only and remain `PENDING_LAYER10`: dataset inventory, event/window counts, split counts, preprocessing freeze, quality outcomes, A0–A13 readiness, A4 profile, external artifacts, gates/tests, repair history, limitations, and reviewed claims. No final table ID is fabricated in this Evidence Map.

## 45. Card Eligibility
P00 existing cards remain preserved. P01 cards are `PENDING_LAYER10`; each may use only the Layer-0-reviewed claim wording/authorized short form and must carry the map-specified limitations/warnings.

## 46. Reproduction Inputs
Layer 10 receives the canonical map, structured claim matrix, P01 execution bundle, exact external artifact pointers, config/environment identities, and existing P00 Layer 10 references. It may render, format, visualize, package, and cross-reference only; it may not recompute, reclassify, retune, strengthen wording, or change evidence.

# PART VII — VALIDATION AND FINAL DECISION

## 47. Path Resolution Validation
| Claim | Path / reference | Status |
| --- | --- | --- |
| P01-CLM-001/v1 | records/datasets/BNCI2014_001/IHARQ-DATASETRECORD-20260806-42c424800627b6ee.json | RESOLVES_LOCAL |
| P01-CLM-001/v1 | records/datasets/Lee2019_MI/IHARQ-DATASETRECORD-20260806-adb91f25a65e588e.json | RESOLVES_LOCAL |
| P01-CLM-001/v1 | records/datasets/PhysioNetMI/IHARQ-DATASETRECORD-20260806-66309cda68771bef.json | RESOLVES_LOCAL |
| P01-CLM-001/v1 | reports/phase_01/sources/source_version_license_report.json | RESOLVES_LOCAL |
| P01-CLM-002/v1 | records/splits/P01-L1-SPLIT-OFFICIAL-R2/IHARQ-SPLITRECORD-20260806-e4e371d332c61e36.json | RESOLVES_LOCAL |
| P01-CLM-002/v1 | reports/phase_01/splits/disjointness.json | RESOLVES_LOCAL |
| P01-CLM-002/v1 | reports/phase_01/leakage/leakage_contamination.json | RESOLVES_LOCAL |
| P01-CLM-003/v1 | records/windows/ | RESOLVES_LOCAL |
| P01-CLM-003/v1 | external_artifact_pointers/derived_windows_dataset.json | RESOLVES_LOCAL |
| P01-CLM-004/v1 | reports/phase_01/storage/existing_core_dataset_adoption.json | RESOLVES_LOCAL |
| P01-CLM-004/v1 | external_artifact_pointers/derived_windows_dataset.json | RESOLVES_LOCAL |
| P01-CLM-005/v1 | reports/phase_01/quality/quality_coverage.json | RESOLVES_LOCAL |
| P01-CLM-005/v1 | records/quality/ | RESOLVES_LOCAL |
| P01-CLM-006/v1 | manifests/phase_01/layer1_ablation_readiness_l1_v1.json | RESOLVES_LOCAL |
| P01-CLM-007/v1 | external_artifact_pointers/a4_window_family_dataset.json | RESOLVES_LOCAL |
| P01-CLM-007/v1 | reports/phase_01/storage/a4_derived_output_storage_actual_precommit.json | RESOLVES_LOCAL |
| P01-CLM-007/v1 | config_snapshot/p01_l1_a4_window_family_freeze_R2.json | RESOLVES_LOCAL |
| P01-CLM-007/v1 | P01_EXECUTED_NOTEBOOK_R49_A4_BOUNDARY_EXPLANATION | CONTROLLED_EXTERNAL_SOURCE_REFERENCE |
| P01-CLM-008/v1 | reports/phase_01/tests/stage_results.json | RESOLVES_LOCAL |
| P01-CLM-008/v1 | gate_decision.json | RESOLVES_LOCAL |
| P01-CLM-008/v1 | reports/phase_01/tests/phase0_and_runtime_regression.json | RESOLVES_LOCAL |
| P01-CLM-008/v1 | reports/phase_01/repair_reentry.json | RESOLVES_LOCAL |
| P01-CLM-008/v1 | checksums.sha256 | RESOLVES_LOCAL |
| P01-CLM-009/v1 | environment_manifest.json | RESOLVES_LOCAL |
| P01-CLM-009/v1 | environment_amendment.json | RESOLVES_LOCAL |
| P01-CLM-010/v1 | handoffs/phase_01_to_phase_02.yaml | RESOLVES_LOCAL |
| P01-CLM-010/v1 | phase2_handoff/phase_01_to_phase_02.yaml | RESOLVES_LOCAL |
| P01-CLM-011/v1 | external_artifact_pointers/a4_window_family_dataset.json | RESOLVES_LOCAL |
| P01-CLM-011/v1 | config_snapshot/p01_l1_a4_window_family_freeze_R2.json | RESOLVES_LOCAL |
| P01-CLM-012/v1 | reports/phase_01/sources/source_version_license_report.json | RESOLVES_LOCAL |
| P01-CLM-012/v1 | gate_decision.json | RESOLVES_LOCAL |

## 48. Validation Summary
| Check | Status | Detail |
| --- | --- | --- |
| p00_count | PASS | 7 |
| p01_count | PASS | 12 |
| p00_release | PASS |  |
| p00_annex_hash | PASS |  |
| p00_wording_hashes | PASS |  |
| p01_wording_hashes | PASS |  |
| p01_dispositions | PASS | Counter({'APPROVED_WITH_QUALIFICATIONS': 8, 'APPROVED': 2, 'DEFERRED': 1, 'REJECTED': 1}) |
| supported_findings | PASS |  |
| all_disposition_ids | PASS |  |
| all_supported_paths | PASS |  |
| no_missing_required_local_paths | PASS | [] |
| limitations_covered | PASS |  |
| a14_prohibited | PASS |  |
| a4_deferred | PASS |  |
| clinical_rejected | PASS |  |
| external_core | PASS |  |
| external_a4 | PASS |  |
| a4_parent_count | PASS |  |
| analysis_exists | PASS |  |
| protocol_exists | PASS |  |

## 49. Source Utilization Matrix
| Source | Authority role | Reviewed | P00 use | P01 use | Claims affected | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Governance V6.1 | Current workflow / Evidence Map sequencing | YES | P00 historical workflow bounded | P01 cumulative sequencing | All | No current conflict | USED_AS_AUTHORITY |
| Seven governing authorities | Architecture/Registry/plan/method authority | YES | P00 identities interpreted | P01 layer/record/ablation boundaries verified | All | No mapping conflict | USED_AS_AUTHORITY |
| P00 implementation/execution | Historical/current P00 evidence | YES | Preserve infrastructure/evidence paths | Inherited foundation | P00 claims | No invalidation | USED_AS_EXECUTION_EVIDENCE |
| P00 Protocol / Analysis / Layer 0 | Historical P00 claim ceiling/wording | YES | Exact current v2 claim wording preserved | Cross-phase boundary | P00 7 claims | No conflict | USED_AS_LAYER0_AUTHORITY |
| P00 Evidence Map R2 | Accepted predecessor map | YES | 7/7 rows preserved | Predecessor release | P00 7 claims | No loss | USED_AS_EXISTING_EVIDENCE_MAP |
| P00 basic Layer 10 R2 | Existing P00 outputs | YES | Existing links preserved | No recomputation | P00 7 claims | No conflict | USED_AS_REPRODUCTION_SOURCE |
| P01 Build Book / executed notebook | Implementation and repair provenance | YES | Not used to override accepted evidence | A4/repro chronology | P01 A4/environment/repairs | Bundle preferred | USED_AS_REPRODUCTION_SOURCE |
| P01 accepted execution bundle | Primary P01 execution evidence | YES | N/A | Exact paths/records/artifacts | P01 claims | All mapped paths resolved | USED_AS_EXECUTION_EVIDENCE |
| Cumulative Protocol v1.0 | Immutable contract/analysis IDs | YES | Current cumulative authority | P01 contract and ceilings | P01 claims | No change | USED_AS_AUTHORITY |
| Cumulative Phase Analysis + embedded Layer 0 | Reviewed claim/finding authority | YES | P00 current state retained | Exact P01 wording/dispositions | All claims | No wording change | USED_AS_LAYER0_AUTHORITY |

## 50. Harmony / No-Drift Decision
| Audit | Result |
| --- | --- |
| INTER_LEVEL_HARMONY | PASS |
| INTRA_EVIDENCE_MAP_HARMONY | PASS |
| CROSS_PHASE_EVIDENCE_MAP_HARMONY | PASS |
| HUMAN_MACHINE_DRIFT | 0 |
| reviewed_claim_wording_drift | 0 |
| missing_mandatory_limitation_links | 0 |
| supported_claims_without_valid_evidence_route | 0 |
| P00_mapping_loss | 0 |
| P01_reviewed_claims_without_Evidence_Map_row | 0 |
| A14 | ABSENT_PROHIBITED |
| A4 effectiveness | NOT_MAPPED_AS_SUPPORTED |
| Clinical/deployment effectiveness | NOT_MAPPED_AS_SUPPORTED |
| Layer 10 source handoff | READY |

## 51. Final Decision
> **CUMULATIVE_EVIDENCE_MAP_THROUGH_P01: PASS — FINALIZED AND FROZEN**

- P00 Evidence Map: **PRESERVED**
- P01 reviewed claims: **12/12 MAPPED**
- Supported/qualified P01 claims: **10**
- Deferred P01 claims: **1**
- Rejected P01 claims: **1**
- Blocked P01 claims: **0**
- Wording drift: **0**
- Broken supported evidence routes: **0**
- Missing mandatory limitation links: **0**
- Freeze-critical Evidence Map blockers: **0**
- Layer 10 inputs: **READY**
- Next governed step: **CREATE / UPDATE LAYER 10 THROUGH P01**

This decision does **not** declare Phase 1 fully closed; Layer 10, cumulative project-state update, and final phase handoff remain downstream.

# APPENDICES

## Appendix A. Full Claim / Evidence Matrix
| Claim | Phase | Reviewed wording | Disposition | Findings | Protocol | Stages | Records | Artifacts | Limitations | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P00-CLM-001/v2 | P00 | Under the exact registered local snapshot and verified Python 3.13.5 environment, all 19 registered Phase 0 engineering/foundation conformance cells passed; this is non-empirical Mode B evidence and does not establish scientific effectiveness or Phase 0 closure. | APPROVE_WITH_QUALIFICATIONS | P00-F-001 | P00_PROTOCOL_MODE_B_ENGINEERING_FOUNDATION | P00-EXECUTION-RELEASE-R2 |  | P00_EVIDENCE_MAP_PREDECESSOR_ROW:P00-CLM-001/v2; P00_ANALYSIS_RELEASE:P00-ANALYSIS-RELEASE-R2 | P00-LIM-002; P00-LIM-003; P00-LIM-004; P00-LIM-L0-001 | PRESERVED_UNCHANGED |
| P00-CLM-002/v2 | P00 | In the frozen local Python 3.13.5 environment, the complete registered deterministic suite passed 102 of 102 tests; cross-version portability is not established. | APPROVE_WITH_QUALIFICATIONS | P00-F-002 | P00_PROTOCOL_MODE_B_ENGINEERING_FOUNDATION | P00-EXECUTION-RELEASE-R2 |  | P00_EVIDENCE_MAP_PREDECESSOR_ROW:P00-CLM-002/v2; P00_ANALYSIS_RELEASE:P00-ANALYSIS-RELEASE-R2 | P00-LIM-001; P00-LIM-002; P00-LIM-003; P00-LIM-004 | PRESERVED_UNCHANGED |
| P00-CLM-003/v2 | P00 | Within the registered non-empirical fixture inventory, all 19 valid or integrated bundles were accepted and all 178 intentionally malformed categories were rejected as expected, with zero false valid rejections and zero false malformed acceptances. | APPROVE_WITH_QUALIFICATIONS | P00-F-003; P00-F-004 | P00_PROTOCOL_MODE_B_ENGINEERING_FOUNDATION | P00-EXECUTION-RELEASE-R2 |  | P00_EVIDENCE_MAP_PREDECESSOR_ROW:P00-CLM-003/v2; P00_ANALYSIS_RELEASE:P00-ANALYSIS-RELEASE-R2 | P00-LIM-004; P00-LIM-L0-001 | PRESERVED_UNCHANGED |
| P00-CLM-004/v2 | P00 | The frozen Phase 0 package contains and validates the registered foundation inventories of 85 schemas, 35 configuration profiles, and 79 record-family profiles; inventory closure does not establish later-phase scientific effectiveness. | APPROVE_WITH_QUALIFICATIONS | P00-F-005 | P00_PROTOCOL_MODE_B_ENGINEERING_FOUNDATION | P00-EXECUTION-RELEASE-R2 |  | P00_EVIDENCE_MAP_PREDECESSOR_ROW:P00-CLM-004/v2; P00_ANALYSIS_RELEASE:P00-ANALYSIS-RELEASE-R2 | P00-LIM-004; P00-LIM-L0-001 | PRESERVED_UNCHANGED |
| P00-CLM-005/v2 | P00 | All eleven Layer 0–10 foundation interfaces passed the registered Phase 0 integration scope; no later-phase scientific execution or effectiveness result is claimed. | APPROVE_WITH_QUALIFICATIONS | P00-F-006 | P00_PROTOCOL_MODE_B_ENGINEERING_FOUNDATION | P00-EXECUTION-RELEASE-R2 |  | P00_EVIDENCE_MAP_PREDECESSOR_ROW:P00-CLM-005/v2; P00_ANALYSIS_RELEASE:P00-ANALYSIS-RELEASE-R2 | P00-LIM-003; P00-LIM-004; P00-LIM-L0-001 | PRESERVED_UNCHANGED |
| P00-CLM-006/v2 | P00 | The P00 implementation foundation is complete within its registered local scope, and P01–P15 reusable contract surfaces are ready for later governed annex creation and execution; future empirical outputs have not been produced. | APPROVE_WITH_QUALIFICATIONS | P00-F-007 | P00_PROTOCOL_MODE_B_ENGINEERING_FOUNDATION | P00-EXECUTION-RELEASE-R2 |  | P00_EVIDENCE_MAP_PREDECESSOR_ROW:P00-CLM-006/v2; P00_ANALYSIS_RELEASE:P00-ANALYSIS-RELEASE-R2 | P00-LIM-003; P00-LIM-004; P00-LIM-L0-001 | PRESERVED_UNCHANGED |
| P00-CLM-007/v2 | P00 | The package reproduced from a clean isolated copy under the exact verified Python 3.13.5 and 22-distribution local dependency snapshot; portable cross-version reproducibility is not established. | APPROVE_WITH_QUALIFICATIONS | P00-F-008 | P00_PROTOCOL_MODE_B_ENGINEERING_FOUNDATION | P00-EXECUTION-RELEASE-R2 |  | P00_EVIDENCE_MAP_PREDECESSOR_ROW:P00-CLM-007/v2; P00_ANALYSIS_RELEASE:P00-ANALYSIS-RELEASE-R2 | P00-LIM-001; P00-LIM-002; P00-LIM-003 | PRESERVED_UNCHANGED |
| P01-CLM-001/v1 | P01 | Within the frozen P01 binary motor-imagery branch, Phase 1 established a checksum-bound, provenance-traceable foundation over the three activated public EEG datasets. | APPROVED_WITH_QUALIFICATIONS | P01-FIND-001 | P01-AC-001-SOURCE-INVENTORY | P01-STAGE-05; P01-STAGE-06; P01-STAGE-07 | IHARQ-DATASETRECORD-20260806-66309cda68771bef; IHARQ-DATASETRECORD-20260806-42c424800627b6ee; IHARQ-DATASETRECORD-20260806-adb91f25a65e588e | records/datasets/BNCI2014_001/IHARQ-DATASETRECORD-20260806-42c424800627b6ee.json; records/datasets/Lee2019_MI/IHARQ-DATASETRECORD-20260806-adb91f25a65e588e.json | PUBLIC_EEG_ONLY; NON_CLINICAL; BINARY_MI_BRANCH_SCOPE | QUALIFIED_CURRENT |
| P01-CLM-002/v1 | P01 | The frozen P01 split assigned 172 subject groups wholly and disjointly across train, calibration, validation, and test roles and passed the implemented registered leakage/disjointness checks; this does not prove that every conceivable leakage mechanism is impossible. | APPROVED_WITH_QUALIFICATIONS | P01-FIND-002; P01-FIND-006 | P01-AC-002-SPLIT; P01-AC-005-LEAKAGE | P01-STAGE-11; P01-STAGE-17 | IHARQ-SPLITRECORD-20260806-e4e371d332c61e36 | records/splits/P01-L1-SPLIT-OFFICIAL-R2/IHARQ-SPLITRECORD-20260806-e4e371d332c61e36.json; reports/phase_01/splits/disjointness.json | IMPLEMENTED_CHECKS_ONLY | QUALIFIED_CURRENT |
| P01-CLM-003/v1 | P01 | Under the frozen official core-window policy, all 12,910 accepted events yielded 12,910 valid core windows, with 0/12,910 invalid official core windows. | APPROVED | P01-FIND-003 | P01-AC-003-DENOMINATOR | P01-STAGE-13; P01-STAGE-14; P01-STAGE-16 | IHARQ-SPLITRECORD-20260806-e4e371d332c61e36; IHARQ-PREPROCESSINGRECORD-20260806-a11b59eeb3861a08 | P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473 | NO_MODEL_EFFECT_INFERENCE | CURRENT_SUPPORTED |
| P01-CLM-004/v1 | P01 | The official P01 core numerical artifact was persisted as 172 lossless HDF5 subject shards covering 12,910 windows and was verified under its Kaggle provider-version/logical-revision/manifest-hash identity contract. | APPROVED_WITH_QUALIFICATIONS | P01-FIND-004 | P01-AC-006-EXTERNAL | P01-STAGE-14; P01-STAGE-15; P01-STAGE-20 | P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473; IHARQ-SPLITRECORD-20260806-e4e371d332c61e36; IHARQ-PREPROCESSINGRECORD-20260806-a11b59eeb3861a08 | P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473 | PRIVATE_KAGGLE_EXTERNAL_ARTIFACT_ACCESS; SOURCE_LICENSE_REDISTRIBUTION_CONSTRAINTS | QUALIFIED_CURRENT |
| P01-CLM-005/v1 | P01 | P01 applied the ANNOTATE_NOT_REPAIR quality policy across 489 quality summaries: 20 soft/provider flags were retained, 0/489 summaries were hard-invalid, and 0/12,910 official core windows were invalid under the registered criteria. | APPROVED_WITH_QUALIFICATIONS | P01-FIND-005 | P01-AC-004-QUALITY | P01-STAGE-13; P01-STAGE-16 | records/quality/ (489 governed quality summaries) | reports/phase_01/quality/quality_coverage.json; records/quality/ | SOFT_FLAG_NOT_EQUIVALENT_TO_CORRUPTION | QUALIFIED_CURRENT |
| P01-CLM-006/v1 | P01 | P01 established Layer-1 foundation readiness for each official A0-A13 identity; none of these ablation-effectiveness experiments was executed in P01, and A14 remained absent/prohibited. | APPROVED_WITH_QUALIFICATIONS | P01-FIND-008 | P01-AC-007-ABLATION-READINESS | P01-STAGE-18 | A0-A13 readiness manifest | manifests/phase_01/layer1_ablation_readiness_l1_v1.json | NO_ABLATION_EFFECTIVENESS_IN_P01 | QUALIFIED_CURRENT |
| P01-CLM-007/v1 | P01 | P01 established a fully matched A4 R2 Layer-1 data substrate for future governed evaluation: 12,910/12,910 parent events are represented without padding, clipping, fabricated samples, or parent-event loss. A4 R2 arose after the +4.0 s feasibility failure and was not evaluated for decoder effectiveness in P01. | APPROVED_WITH_QUALIFICATIONS | P01-FIND-009; P01-FIND-010 | P01-AC-008-A4 | P01-STAGE-14; P01-STAGE-15; P01-STAGE-18 | P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13; P01-L1-A4-WINDOW-FAMILY-FREEZE-R2 | P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13 | A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01; A4_EFFECTIVENESS_NOT_EXECUTED | QUALIFIED_CURRENT |
| P01-CLM-008/v1 | P01 | The accepted P01 execution completed 27/27 registered stages, 16/16 deterministic P01 gates, and 50/50 regression tests with 0 unresolved blockers; final execution-bundle integrity checks also closed. | APPROVED | P01-FIND-012 | P01-AC-010-GATES-REPAIRS | P01-STAGE-04; P01-STAGE-23; P01-STAGE-24; P01-STAGE-26 | P01-G01...P01-G16; stage_results 00...26 | reports/phase_01/tests/stage_results.json; gate_decision.json | NO_EFFECTIVENESS_INFERENCE | CURRENT_SUPPORTED |
| P01-CLM-009/v1 | P01 | The accepted P01 run used Python 3.12.13 under a documented compatibility amendment and the governed adaptive-disk policy P01-L1-KAGGLE-ADAPTIVE-DISK-R1; the accepted records show no change to the frozen datasets, labels, subject split, core preprocessing, core window policy, or 12,910-event denominator attributable to these runtime/resource amendments. | APPROVED_WITH_QUALIFICATIONS | P01-FIND-011 | P01-AC-009-ENVIRONMENT | P01-STAGE-01; P01-STAGE-03 | P01-L1-KAGGLE-ENV-FREEZE-R5; P01-L1-KAGGLE-ADAPTIVE-DISK-R1 | environment_manifest.json; environment_amendment.json | ACTUAL_RUNTIME_PYTHON_3_12_13_WITH_COMPATIBILITY_AMENDMENT; ADAPTIVE_DISK_RESOURCE_AMENDMENT | QUALIFIED_CURRENT |
| P01-CLM-010/v1 | P01 | P01 freezes a technical Layer-1 data contract that P02 may consume using the recorded dataset, label-map, split, preprocessing, core-window, and external-artifact identities; silent relabeling, rewindowing, split mutation, denominator substitution, or test-visibility leakage is prohibited. This is technical readiness, not evidence of P02 scientific success. | APPROVED_WITH_QUALIFICATIONS | P01-FIND-014 | P01-AC-003-DENOMINATOR; P01-AC-005-LEAKAGE; P01-AC-006-EXTERNAL; P01-AC-007-ABLATION-READINESS; P01-AC-010-GATES-REPAIRS | P01-STAGE-22; P01-STAGE-23; P01-STAGE-26 | IHARQ-DATASETRECORD-20260806-66309cda68771bef; IHARQ-DATASETRECORD-20260806-42c424800627b6ee; IHARQ-DATASETRECORD-20260806-adb91f25a65e588e; IHARQ-LABELMAPRECORD-20260806-4379781a3b5f5ea9; IHARQ-LABELMAPRECORD-20260806-587dcfff81307768; IHARQ-LABELMAPRECORD-20260806-b551cfd20335896c; IHARQ-SPLITRECORD-20260806-e4e371d332c61e36; IHARQ-PREPROCESSINGRECORD-20260806-a11b59eeb3861a08; P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473; P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13 | P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473; P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13 | DOCUMENTARY_CLOSURE_SEQUENCE_REMAINS | QUALIFIED_CURRENT |
| P01-CLM-011/v1 | P01 | P01 did not evaluate whether A4 R2 improves decoder performance relative to the core window; that effectiveness question remains deferred to a future governed matched downstream experiment. | DEFERRED | P01-FIND-009 | P01-AC-008-A4 | P01-STAGE-14; P01-STAGE-15 | P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13; P01-L1-A4-WINDOW-FAMILY-FREEZE-R2 | P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13 | A4_EFFECTIVENESS_NOT_EXECUTED; A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01 | DEFERRED_NOT_MAPPABLE_AS_SUPPORTED |
| P01-CLM-012/v1 | P01 | P01 is a public, non-clinical data-foundation and execution-validation phase; it does not establish clinical effectiveness, patient benefit, deployment safety, or medical-device readiness. | REJECTED | P01-FIND-001; P01-FIND-012 | P01-AC-001-SOURCE-INVENTORY; P01-AC-010-GATES-REPAIRS | P01-STAGE-06; P01-STAGE-26 | IHARQ-DATASETRECORD-20260806-66309cda68771bef; IHARQ-DATASETRECORD-20260806-42c424800627b6ee; IHARQ-DATASETRECORD-20260806-adb91f25a65e588e | reports/phase_01/sources/source_version_license_report.json; gate_decision.json | PUBLIC_EEG_ONLY; NON_CLINICAL; NO_DEPLOYMENT_CLAIM | REJECTED_PROHIBITED_AS_SUPPORTED |

## Appendix B. Reviewed Wording Hash Matrix
| Claim | SHA-256 | Source |
| --- | --- | --- |
| P00-CLM-001/v2 | acd0d4ddf5f6e53ad0e26a8898dcd23f12d6b9c1ec772fd97c8497478db735bf | P00 R2 Evidence Map / Layer 0 |
| P00-CLM-002/v2 | fd0433bb7a4e3f05b2af29a85d881663fc5e8869dd9172921564a76e9865d3a3 | P00 R2 Evidence Map / Layer 0 |
| P00-CLM-003/v2 | 7167fef067a3ff78ef3b13cd57020f6a1f6d97bd0702adf8b93bb90193556fc9 | P00 R2 Evidence Map / Layer 0 |
| P00-CLM-004/v2 | 306cc07bda684fd312de578c48d4f3933df2c6ca5dfb93bf16c664cd49b088dc | P00 R2 Evidence Map / Layer 0 |
| P00-CLM-005/v2 | 193811b063a515c08dff31d75363d0ac90b1fe2f02d406b80380d19cd5134e5f | P00 R2 Evidence Map / Layer 0 |
| P00-CLM-006/v2 | 0805b095d02bcee3927473ab56190df49d15cba101b5fc99b808a0459adf29b2 | P00 R2 Evidence Map / Layer 0 |
| P00-CLM-007/v2 | d5e1b1e0a9eeea91e1f03ddddbd056b5d10f3bcc6a10595d105833caaeb4aab5 | P00 R2 Evidence Map / Layer 0 |
| P01-CLM-001/v1 | 664c1475235f623bbdaaa36ba26edd5c4adb67c9c18569f4459396e89c5f6b8d | Embedded P01 Layer 0 |
| P01-CLM-002/v1 | 3fb7b1d11a0db14c323faff80f5035cd79b479d20571bcc9635ceb21601f4dd6 | Embedded P01 Layer 0 |
| P01-CLM-003/v1 | e8f0eba65ea24b53c423d8adc1c2d7934f492164730d6fba0a7f50aaad4df1d2 | Embedded P01 Layer 0 |
| P01-CLM-004/v1 | 72eaafbcb355737c6e1a3c26c39985d8920a78ea8d043d4825c97494301c6172 | Embedded P01 Layer 0 |
| P01-CLM-005/v1 | fffce437970542436e6a67f83b154772ba40ea95e1f444357dc76c332d07cc3b | Embedded P01 Layer 0 |
| P01-CLM-006/v1 | 9530e521edf347a9337a281e07ec8f7675f54b652d9e2a2aa107bbe3f6192c2e | Embedded P01 Layer 0 |
| P01-CLM-007/v1 | e6c55f132a42163e7e469debbe3b84af58abfa7989845c4131c0a2af86290f41 | Embedded P01 Layer 0 |
| P01-CLM-008/v1 | 5fe3a29ca3e7a78eb3f4dffdfd5253e24438fc7189c94c662fb400d627402c54 | Embedded P01 Layer 0 |
| P01-CLM-009/v1 | 973c575a07010193c62644f51cfddb04dc02075b8c8a7a73b09f4e4c1bad7b56 | Embedded P01 Layer 0 |
| P01-CLM-010/v1 | 8d09e698817c8925b0d0065f179a3f5f85d53e7136f14e9940e077754462856d | Embedded P01 Layer 0 |
| P01-CLM-011/v1 | 310d0218a7ebf5f91456c11da837f0ae8a81c42639627a7bb0c2134ae50709df | Embedded P01 Layer 0 |
| P01-CLM-012/v1 | b85c8e6c22a210747a0ef4e9bf27df7cb4fec7aff49663da11a1471a34a91946 | Embedded P01 Layer 0 |

## Appendix C. Foreign-Key Validation
All P01 supported/qualified claims resolve to one or more frozen findings, Protocol analysis IDs, accepted stage IDs, and retrievable local/external evidence. Directory collections are represented as collections instead of fabricated record identifiers. Controlled pending states are not treated as broken foreign keys.

## Appendix D. Limitation Propagation Matrix
| Limitation | Phase | Claims | Proximity | Caption warning | Downstream |
| --- | --- | --- | --- | --- | --- |
| P00-LIM-002 | P00 | P00-CLM-001/v2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 |
| P00-LIM-003 | P00 | P00-CLM-001/v2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 |
| P00-LIM-004 | P00 | P00-CLM-001/v2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 |
| P00-LIM-L0-001 | P00 | P00-CLM-001/v2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 |
| P00-LIM-001 | P00 | P00-CLM-002/v2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 |
| P00-LIM-002 | P00 | P00-CLM-002/v2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 |
| P00-LIM-003 | P00 | P00-CLM-002/v2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 |
| P00-LIM-004 | P00 | P00-CLM-002/v2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 |
| P00-LIM-004 | P00 | P00-CLM-003/v2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 |
| P00-LIM-L0-001 | P00 | P00-CLM-003/v2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 |
| P00-LIM-004 | P00 | P00-CLM-004/v2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 |
| P00-LIM-L0-001 | P00 | P00-CLM-004/v2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 |
| P00-LIM-003 | P00 | P00-CLM-005/v2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 |
| P00-LIM-004 | P00 | P00-CLM-005/v2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 |
| P00-LIM-L0-001 | P00 | P00-CLM-005/v2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 |
| P00-LIM-003 | P00 | P00-CLM-006/v2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 |
| P00-LIM-004 | P00 | P00-CLM-006/v2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 |
| P00-LIM-L0-001 | P00 | P00-CLM-006/v2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 |
| P00-LIM-001 | P00 | P00-CLM-007/v2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 |
| P00-LIM-002 | P00 | P00-CLM-007/v2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 |
| P00-LIM-003 | P00 | P00-CLM-007/v2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 | PRESERVE_EXISTING_P00_R2 |
| PUBLIC_EEG_ONLY | P01 | P01-CLM-001/v1;P01-CLM-012/v1 | MANDATORY_IN_CLAIM_OR_PROXIMATE_CONTEXT_AND_CAPTION_WHERE_RELEVANT | MANDATORY where visual could be misread | P02-P15; Layer 0 |
| NON_CLINICAL | P01 | P01-CLM-001/v1;P01-CLM-012/v1 | MANDATORY_IN_CLAIM_OR_PROXIMATE_CONTEXT_AND_CAPTION_WHERE_RELEVANT | MANDATORY where visual could be misread | All claim-bearing outputs |
| BINARY_MI_BRANCH_SCOPE | P01 | P01-CLM-001/v1 | MANDATORY_IN_PROXIMATE_CONTEXT | MANDATORY where visual could be misread | P02-P15 |
| IMPLEMENTED_CHECKS_ONLY | P01 | P01-CLM-002/v1 | MANDATORY_IN_CLAIM_OR_PROXIMATE_CONTEXT_AND_CAPTION_WHERE_RELEVANT | MANDATORY where visual could be misread | P02-P15 |
| NO_MODEL_EFFECT_INFERENCE | P01 | P01-CLM-003/v1 | MANDATORY_IN_PROXIMATE_CONTEXT | MANDATORY where visual could be misread | P02-P15 |
| PRIVATE_KAGGLE_EXTERNAL_ARTIFACT_ACCESS | P01 | P01-CLM-004/v1 | MANDATORY_IN_PROXIMATE_CONTEXT | MANDATORY where visual could be misread | P02-P15 reproducibility |
| SOURCE_LICENSE_REDISTRIBUTION_CONSTRAINTS | P01 | P01-CLM-004/v1 | MANDATORY_IN_PROXIMATE_CONTEXT | MANDATORY where visual could be misread | Repository/release packaging |
| SOFT_FLAG_NOT_EQUIVALENT_TO_CORRUPTION | P01 | P01-CLM-005/v1 | MANDATORY_IN_CLAIM_OR_PROXIMATE_CONTEXT_AND_CAPTION_WHERE_RELEVANT | MANDATORY where visual could be misread | P02-P15 |
| NO_ABLATION_EFFECTIVENESS_IN_P01 | P01 | P01-CLM-006/v1 | MANDATORY_IN_PROXIMATE_CONTEXT | MANDATORY where visual could be misread | P02-P15 |
| A4_R2_RETROSPECTIVE_FEASIBILITY_ORIGIN_NOT_CONFIRMATORY_IN_P01 | P01 | P01-CLM-007/v1;P01-CLM-011/v1 | MANDATORY_IN_CLAIM_OR_PROXIMATE_CONTEXT_AND_CAPTION_WHERE_RELEVANT | MANDATORY where visual could be misread | P02 A4 and Layer 0 |
| A4_EFFECTIVENESS_NOT_EXECUTED | P01 | P01-CLM-007/v1;P01-CLM-011/v1 | MANDATORY_IN_CLAIM_OR_PROXIMATE_CONTEXT_AND_CAPTION_WHERE_RELEVANT | MANDATORY where visual could be misread | P02-P15 |
| NO_EFFECTIVENESS_INFERENCE | P01 | P01-CLM-008/v1 | MANDATORY_IN_PROXIMATE_CONTEXT | MANDATORY where visual could be misread | P02-P15 |
| ACTUAL_RUNTIME_PYTHON_3_12_13_WITH_COMPATIBILITY_AMENDMENT | P01 | P01-CLM-009/v1 | MANDATORY_IN_PROXIMATE_CONTEXT | MANDATORY where visual could be misread | Reproduction |
| ADAPTIVE_DISK_RESOURCE_AMENDMENT | P01 | P01-CLM-009/v1 | MANDATORY_IN_PROXIMATE_CONTEXT | MANDATORY where visual could be misread | Reproduction |
| DOCUMENTARY_CLOSURE_SEQUENCE_REMAINS | P01 | P01-CLM-010/v1 | MANDATORY_IN_PROXIMATE_CONTEXT | MANDATORY where visual could be misread | P02-P15 |
| NO_DEPLOYMENT_CLAIM | P01 | P01-CLM-012/v1 | MANDATORY_IN_CLAIM_OR_PROXIMATE_CONTEXT_AND_CAPTION_WHERE_RELEVANT | MANDATORY where visual could be misread | Layer 0 and later deployment-related phases |

## Appendix E. Manuscript Placement Matrix
| Claim | Paper | Thesis | Appendix | Figure | Table | Card | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P00-CLM-001/v2 | Methods or Reproducibility Statement Only | Methods / Phase 0 Foundation and Reproducibility | Phase 0 foundation/reproducibility appendix — item 1 | P00_EXISTING_LAYER10 | P00_EXISTING_LAYER10 | claim_card_01 | SUPPORTED_PLACEMENT |
| P00-CLM-002/v2 | Methods or Reproducibility Statement Only | Methods / Phase 0 Foundation and Reproducibility | Phase 0 foundation/reproducibility appendix — item 2 | P00_EXISTING_LAYER10 | P00_EXISTING_LAYER10 | claim_card_02 | SUPPORTED_PLACEMENT |
| P00-CLM-003/v2 | Methods or Reproducibility Statement Only | Methods / Phase 0 Foundation and Reproducibility | Phase 0 foundation/reproducibility appendix — item 3 | P00_EXISTING_LAYER10 | P00_EXISTING_LAYER10 | claim_card_03 | SUPPORTED_PLACEMENT |
| P00-CLM-004/v2 | Methods or Reproducibility Statement Only | Methods / Phase 0 Foundation and Reproducibility | Phase 0 foundation/reproducibility appendix — item 4 | P00_EXISTING_LAYER10 | P00_EXISTING_LAYER10 | claim_card_04 | SUPPORTED_PLACEMENT |
| P00-CLM-005/v2 | Methods or Reproducibility Statement Only | Methods / Phase 0 Foundation and Reproducibility | Phase 0 foundation/reproducibility appendix — item 5 | P00_EXISTING_LAYER10 | P00_EXISTING_LAYER10 | claim_card_05 | SUPPORTED_PLACEMENT |
| P00-CLM-006/v2 | Methods or Reproducibility Statement Only | Methods / Phase 0 Foundation and Reproducibility | Phase 0 foundation/reproducibility appendix — item 6 | P00_EXISTING_LAYER10 | P00_EXISTING_LAYER10 | claim_card_06 | SUPPORTED_PLACEMENT |
| P00-CLM-007/v2 | Methods or Reproducibility Statement Only | Methods / Phase 0 Foundation and Reproducibility | Phase 0 foundation/reproducibility appendix — item 7 | P00_EXISTING_LAYER10 | P00_EXISTING_LAYER10 | claim_card_07 | SUPPORTED_PLACEMENT |
| P01-CLM-001/v1 | PROVISIONAL_METHODS_DATA | PROVISIONAL_METHODS_DATA_FOUNDATION | PENDING_FINAL_MANUSCRIPT_STRUCTURE | P01-FIG-SRC-001;P01-FIG-SRC-002 | PENDING_LAYER10:DATASET_INVENTORY | PENDING_LAYER10 | SUPPORTED_PLACEMENT |
| P01-CLM-002/v1 | PROVISIONAL_METHODS_SPLIT_AND_LEAKAGE | PROVISIONAL_METHODS_SPLIT_AND_LEAKAGE | PENDING_FINAL_MANUSCRIPT_STRUCTURE | P01-FIG-SRC-003 | PENDING_LAYER10:SPLIT_COUNTS | PENDING_LAYER10 | SUPPORTED_PLACEMENT |
| P01-CLM-003/v1 | PROVISIONAL_RESULTS_DATA_FOUNDATION | PROVISIONAL_RESULTS_DATA_FOUNDATION | PENDING_FINAL_MANUSCRIPT_STRUCTURE | P01-FIG-SRC-002;P01-FIG-SRC-005 | PENDING_LAYER10:EVENT_WINDOW_COUNTS | PENDING_LAYER10 | SUPPORTED_PLACEMENT |
| P01-CLM-004/v1 | PROVISIONAL_METHODS_REPRODUCIBILITY | PROVISIONAL_REPRODUCIBILITY | PENDING_FINAL_MANUSCRIPT_STRUCTURE | P01-FIG-SRC-005 | PENDING_LAYER10:EXTERNAL_ARTIFACTS | PENDING_LAYER10 | SUPPORTED_PLACEMENT |
| P01-CLM-005/v1 | PROVISIONAL_RESULTS_DATA_QUALITY | PROVISIONAL_RESULTS_DATA_QUALITY | PENDING_FINAL_MANUSCRIPT_STRUCTURE | NO_CURRENT_ARTIFACT | PENDING_LAYER10:QUALITY_OUTCOMES | PENDING_LAYER10 | SUPPORTED_PLACEMENT |
| P01-CLM-006/v1 | PROVISIONAL_METHODS_ABLATION_READINESS | PROVISIONAL_METHODS_ABLATION_READINESS | PENDING_FINAL_MANUSCRIPT_STRUCTURE | P01-FIG-SRC-009 | PENDING_LAYER10:A0_A13_READINESS | PENDING_LAYER10 | SUPPORTED_PLACEMENT |
| P01-CLM-007/v1 | PROVISIONAL_RESULTS_DATA_FOUNDATION_WITH_PROXIMATE_A4_WARNING | PROVISIONAL_RESULTS_A4_FOUNDATION_WITH_PROXIMATE_WARNING | PENDING_FINAL_MANUSCRIPT_STRUCTURE | P01-FIG-SRC-006;P01-FIG-SRC-007 | PENDING_LAYER10:A4_PROFILE | PENDING_LAYER10 | SUPPORTED_PLACEMENT |
| P01-CLM-008/v1 | PROVISIONAL_METHODS_REPRODUCIBILITY | PROVISIONAL_REPRODUCIBILITY_AND_AUDIT | PENDING_FINAL_MANUSCRIPT_STRUCTURE | P01-FIG-SRC-008 | PENDING_LAYER10:GATES_TESTS | PENDING_LAYER10 | SUPPORTED_PLACEMENT |
| P01-CLM-009/v1 | PROVISIONAL_METHODS_REPRODUCIBILITY | PROVISIONAL_REPRODUCIBILITY_ENVIRONMENT | PENDING_FINAL_MANUSCRIPT_STRUCTURE | NO_CURRENT_ARTIFACT | PENDING_LAYER10:ENVIRONMENT_AMENDMENTS | PENDING_LAYER10 | SUPPORTED_PLACEMENT |
| P01-CLM-010/v1 | PROVISIONAL_METHODS_DOWNSTREAM_HANDOFF | PROVISIONAL_DOWNSTREAM_READINESS | PENDING_FINAL_MANUSCRIPT_STRUCTURE | P01-FIG-SRC-010 | PENDING_LAYER10:P01_P02_HANDOFF | PENDING_LAYER10 | SUPPORTED_PLACEMENT |
| P01-CLM-011/v1 | PROVISIONAL_FUTURE_WORK_OR_LIMITATIONS | PROVISIONAL_FUTURE_WORK_OR_LIMITATIONS | PENDING_FINAL_MANUSCRIPT_STRUCTURE | P01-FIG-SRC-006;P01-FIG-SRC-007 | PENDING_LAYER10:NEGATIVE_DEFERRED_CLAIMS | PENDING_LAYER10 | FUTURE_WORK_OR_LIMITATIONS_ONLY |
| P01-CLM-012/v1 | PROVISIONAL_LIMITATIONS_OR_CLAIM_BOUNDARY | PROVISIONAL_LIMITATIONS_OR_CLAIM_BOUNDARY | PENDING_FINAL_MANUSCRIPT_STRUCTURE | P01-FIG-SRC-009 | PENDING_LAYER10:NEGATIVE_DEFERRED_CLAIMS | PENDING_LAYER10 | NOT_ELIGIBLE_AS_SUPPORTED_CLAIM |

## Appendix F. Negative / Deferred Claim Register
| ID / Claim | Disposition / Type | Reason / effect | Future condition / allowed use |
| --- | --- | --- | --- |
| P01-CLM-011/v1 | DEFERRED | A4 effectiveness was not evaluated in P01 | Future governed matched decoder experiment; current use: future work/limitations |
| P01-CLM-012/v1 | REJECTED | Public non-clinical P01 evidence cannot establish clinical/deployment effectiveness | Requires future appropriate clinical/deployment evidence; current use: claim boundary/limitations |
| P01-NEG-A4-4S-INFEASIBILITY | NEGATIVE_EVIDENCE | The +4.0 s candidate profile was infeasible for one valid parent without 80 nonexistent samples; R2 +3.5 s preserves all 12,910 parents. | A4 figure captions; limitation/future-work; negative-result view |
| P01-NEG-A4-EFFECTIVENESS-NOT-EXECUTED | NEGATIVE_EVIDENCE | No P01 decoder-effect comparison exists for A4. | Deferred claim register; A4 visuals; future work |
| P01-NEG-CLINICAL-DEPLOYMENT-NOT-SUPPORTED | NEGATIVE_EVIDENCE | Public non-clinical data-foundation evidence cannot support clinical effectiveness or deployment safety. | Claim-boundary/limitations; prohibited-claim view |
| P01-HISTORICAL-FAILED-EXECUTION | NEGATIVE_EVIDENCE | Historical Stage 07/18/26 failures are repair/reentry evidence, not the source for the final positive execution-closure claim. | Reproducibility/audit chronology only |
| P01-QUALITY-SOFT-FLAGS | NEGATIVE_EVIDENCE | 20 soft/provider flags remain visible but do not equal hard invalidity or corruption. | Quality tables/figures/cards and limitations |
| P01-EXTERNAL-ACCESS-LIMIT | NEGATIVE_EVIDENCE | Core/A4 numerical bytes require private Kaggle access and source-license compliance. | Reproduction package and artifact cards |

## Appendix G. A0–A13 Register
| ID | Official identity | P01 status | Executed in P01 | Map status | Limitations |
| --- | --- | --- | --- | --- | --- |
| A0 | Raw Decoder / Accept-All Raw Decoder Reference | FOUNDATION_READY | NOT_EXECUTED_IN_P01 | FOUNDATION_READY_NOT_EFFECTIVENESS | NO_ABLATION_EFFECTIVENESS_IN_P01 |
| A1 | Calibrated Decoder / Calibration Visibility | FOUNDATION_READY | NOT_EXECUTED_IN_P01 | FOUNDATION_READY_NOT_EFFECTIVENESS | NO_ABLATION_EFFECTIVENESS_IN_P01 |
| A2 | Simple Registered Threshold / Confidence-Threshold Baseline | FOUNDATION_READY | NOT_EXECUTED_IN_P01 | FOUNDATION_READY_NOT_EFFECTIVENESS | NO_ABLATION_EFFECTIVENESS_IN_P01 |
| A3 | Uncertainty and Selective Prediction | FOUNDATION_READY | NOT_EXECUTED_IN_P01 | FOUNDATION_READY_NOT_EFFECTIVENESS | NO_ABLATION_EFFECTIVENESS_IN_P01 |
| A4 | Longer-Window, Multi-Window Voting/Averaging and Ordinary Ensemble Controls | FOUNDATION_READY | NOT_EXECUTED_IN_P01 | FOUNDATION_READY_NOT_EFFECTIVENESS | NO_ABLATION_EFFECTIVENESS_IN_P01;A4_EFFECTIVENESS_NOT_EXECUTED |
| A5 | IHARQ-lite / Rule-Based Evidence Verification | FOUNDATION_READY | NOT_EXECUTED_IN_P01 | FOUNDATION_READY_NOT_EFFECTIVENESS | NO_ABLATION_EFFECTIVENESS_IN_P01 |
| A6 | IHARQ + Evidence-Quality Estimator | FOUNDATION_READY | NOT_EXECUTED_IN_P01 | FOUNDATION_READY_NOT_EFFECTIVENESS | NO_ABLATION_EFFECTIVENESS_IN_P01 |
| A7 | IHARQ + RegimeRisk Temporal Trust | FOUNDATION_READY | NOT_EXECUTED_IN_P01 | FOUNDATION_READY_NOT_EFFECTIVENESS | NO_ABLATION_EFFECTIVENESS_IN_P01 |
| A8 | Learning-to-defer / Deferral Comparison | FOUNDATION_READY | NOT_EXECUTED_IN_P01 | FOUNDATION_READY_NOT_EFFECTIVENESS | NO_ABLATION_EFFECTIVENESS_IN_P01 |
| A9 | Supervised Adaptive-IHARQ / Adaptive Readiness Policy | FOUNDATION_READY | NOT_EXECUTED_IN_P01 | FOUNDATION_READY_NOT_EFFECTIVENESS | NO_ABLATION_EFFECTIVENESS_IN_P01 |
| A10 | Contextual Bandit / Simulation-Bounded Immediate-Reward Adaptation | FOUNDATION_READY | NOT_EXECUTED_IN_P01 | FOUNDATION_READY_NOT_EFFECTIVENESS | NO_ABLATION_EFFECTIVENESS_IN_P01 |
| A11 | Reinforcement-Learning Policy / Simulation-Bounded Sequential Policy Learning | FOUNDATION_READY | NOT_EXECUTED_IN_P01 | FOUNDATION_READY_NOT_EFFECTIVENESS | NO_ABLATION_EFFECTIVENESS_IN_P01 |
| A12 | StressForge Stress Tests / Controlled Stress Robustness | FOUNDATION_READY | NOT_EXECUTED_IN_P01 | FOUNDATION_READY_NOT_EFFECTIVENESS | NO_ABLATION_EFFECTIVENESS_IN_P01 |
| A13 | Layer 9 Simulation-Only Embodiment Demo | FOUNDATION_READY | NOT_EXECUTED_IN_P01 | FOUNDATION_READY_NOT_EFFECTIVENESS | NO_ABLATION_EFFECTIVENESS_IN_P01 |

## Appendix H. External Artifact Register
| Artifact | Dataset | Provider rev | Logical rev | Manifest SHA-256 | Bytes | Retrieval |
| --- | --- | --- | --- | --- | --- | --- |
| P01-L1-DERIVED-WINDOWS-d03f0a7c869dd95a-20260806222242-68a91473 | csthv999z/iharq-p01-l1-derived-windows-d03f0a7c869d-20260806222242-68a91473 | 2 | 1 | dc21f418e9a1add62adb346f627d5d729735a5f1ecaa1d771f6fa5cfede627e1 | 1166652764 | Attach Kaggle provider dataset version 2 (IHARQ logical immutable revision 1); verify manifest SHA-256; load IHARQ_P01_L1_WINDOW_TO_SHARD_INDEX.jsonl; resolve shard filename; read declared HDF5 group/row. |
| P01-L1-A4-DERIVED-WINDOWS-4cd080393345e8aa-20260807143013-663eab13 | csthv999z/iharq-p01-l1-a4-d03f0a7c-9a7c6108 | 1 | 2 | 29124d59907610b1545e0a2b5d1811a4d4a2bf1df64cad49aa880f4721c47305 | 1357362334 | Attach exact private Kaggle Dataset provider version 1; verify manifest SHA-256; use registered A4 index/reader and R2 window-family freeze. |

## Appendix I. Source Utilization Matrix
| Source | Role | Status |
| --- | --- | --- |
| Governance V6.1 | Current workflow / Evidence Map sequencing | USED_AS_AUTHORITY |
| Seven governing authorities | Architecture/Registry/plan/method authority | USED_AS_AUTHORITY |
| P00 implementation/execution | Historical/current P00 evidence | USED_AS_EXECUTION_EVIDENCE |
| P00 Protocol / Analysis / Layer 0 | Historical P00 claim ceiling/wording | USED_AS_LAYER0_AUTHORITY |
| P00 Evidence Map R2 | Accepted predecessor map | USED_AS_EXISTING_EVIDENCE_MAP |
| P00 basic Layer 10 R2 | Existing P00 outputs | USED_AS_REPRODUCTION_SOURCE |
| P01 Build Book / executed notebook | Implementation and repair provenance | USED_AS_REPRODUCTION_SOURCE |
| P01 accepted execution bundle | Primary P01 execution evidence | USED_AS_EXECUTION_EVIDENCE |
| Cumulative Protocol v1.0 | Immutable contract/analysis IDs | USED_AS_AUTHORITY |
| Cumulative Phase Analysis + embedded Layer 0 | Reviewed claim/finding authority | USED_AS_LAYER0_AUTHORITY |

## Appendix J. Evidence Map Audit Log
The package includes `evidence_map_audit_log.jsonl`, preserving P00 predecessor retention, each P01 mapping addition, validation, and final freeze as structured append-only-style records.
