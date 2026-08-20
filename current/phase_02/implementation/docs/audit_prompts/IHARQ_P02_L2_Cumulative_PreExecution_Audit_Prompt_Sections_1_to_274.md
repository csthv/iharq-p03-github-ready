# IHARQ PHASE 02 / LAYER 02

# CUMULATIVE PRE-EXECUTION DOUBLE-CHECK, TRIPLE-CHECK, STRETCH-VERSION, CODE-QUALITY, FUNCTIONAL-CORRECTNESS, REPAIR, RECONCILIATION, AND KAGGLE-READINESS PROMPT

> **Scope of this cumulative file:** Sections **1 through 274** only. It intentionally does **not** include Section 0 or any later Sections 275+.
>
> This file merges the original pre-execution audit prompt, the non-deferral/max-completeness extension, the Stretch-Version requirement, and the code-quality/actual-working-functionality extension into one continuous prompt.

---

# 1. PRIMARY OBJECTIVE

Determine whether the created notebook and its companion package constitute a **complete, faithful, professionally engineered executable realization** of the finalized P02/L2 Implementation Build Book and all applicable upstream authorities.

The notebook/package must be complete enough that the user can reasonably proceed to actual Kaggle execution without discovering halfway through that a required input, Layer-2 module/capability, selected model, conditional admission path, ablation, evaluation, metric/statistic, artifact producer, record writer, stage implementation, dependency, test, gate, P01 input, A0/A4 behavior, downstream field, import, dependency, resource assumption, persistence path, resumability path, security rule, or final bundle behavior was never actually implemented.

The objective is:

```text
CREATED NOTEBOOK/PACKAGE
↓
INDEPENDENT EXHAUSTIVE AUDIT
↓
REPAIR ALL GENUINE IMPLEMENTATION DEFECTS
↓
REGENERATE AFFECTED DERIVATIVES
↓
RERUN VALIDATION
↓
ADVERSARIAL REVIEW
↓
KAGGLE EXECUTION SIMULATION
↓
FINAL PRE-EXECUTION READINESS CERTIFICATION
```

# 2. IMPORTANT SCOPE BOUNDARY

This task is **pre-execution implementation validation**, not actual Phase 02 scientific execution.

Do not run the complete governed P02 workload on the real dataset, fabricate P02 results, create fake Protocol/Phase-Analysis/Layer-0/Evidence-Map/Layer-10 findings, or claim Phase 02 has executed.

You **must** run all reasonable non-scientific validation needed to establish implementation quality, including syntax/compile/import checks, schema/config validation, dependency checks, notebook JSON checks, stage-DAG checks, run-matrix expansion, synthetic fixtures, golden-vector tests, negative tests, tiny synthetic training/inference smoke tests, checkpoint save/reload tests, bundle dry-runs, manifest/checksum checks, path-safety scans, secret scans, archive reopen tests, synthetic stage execution, isolated-worker probes, and clean-subprocess imports.

Synthetic outputs must be unmistakably labeled:

```text
FIXTURE
NON_SCIENTIFIC
NOT_P02_EVIDENCE
```

# 3. USE ALL CONTROLLING SOURCES

Audit the notebook/package against the complete controlling project state, not only against itself.

Use:
- Governance V6.1.
- All seven governing authorities: Architecture, Registry, Execution & Evidence Plan, Experiment/Ablation/Evaluation Protocol, Complete Phase Execution Playbook, Method Selection, and Nuts-and-Bolts.
- Final P02/L2 Implementation Build Book R4 and all machine-readable derivatives.
- Cumulative P00/P01 state, final P01 execution bundle, P01 notebook and repair history, cumulative Protocol v1.0, cumulative Phase Analysis, Layer 0, Evidence Map, Layer 10, P01→P02 handoff, and cumulative repository/ZIP.
- The actual P02 notebook, source code, configs, schemas, tests, scripts, machine-readable contracts, stage plans, run matrices, bundle schemas, validation outputs, checksums, README, and package.

# 4. SOURCE-OF-TRUTH ROUTING

Route inconsistencies correctly:

```text
Architecture → phase/layer/module ownership
Registry → records/interfaces/fields/identities/lifecycle
Execution & Evidence Plan → evidence/artifacts/gates/completion
Protocol → experiments/ablations/comparisons/metrics/statistics
Playbook → stage order and execution behavior
Method Selection → selected methods/models/strategies
Nuts-and-Bolts → exact implementation behavior
Implementation Build Book → executable P02 realization
P00/P01 final evidence → inherited state
Protocol/Analysis/L0/EMap/L10 → cumulative governed state
P01→P02 handoff → inherited interface
P02 notebook/package → implementation under review
```

If notebook code disagrees with the frozen Build Book, the notebook is wrong unless a higher authority clearly establishes a Build Book defect.

# 5. BUILD BOOK MUST REMAIN SCIENTIFICALLY AUTHORITATIVE

The P02 notebook must implement the **R3 scientific execution freeze adopted unchanged by R4**.

Do not introduce or remove models, metrics, seeds, budgets, run cells, ablation conditions, selection rules, statistics, denominators, transformations, or downstream responsibilities merely for convenience.

# 6. CREATE A REQUIREMENT-TO-IMPLEMENTATION MASTER LEDGER

Construct a complete ledger:

```text
source authority
→ requirement
→ P02 responsibility
→ L2 module
→ capability/submodule
→ selected method
→ configuration
→ code implementation
→ notebook stage
→ run cell(s)
→ test
→ gate
→ runtime artifact
→ downstream consumer
→ status
```

Required:

```text
UNMAPPED_REQUIRED_P02_REQUIREMENTS = 0
```

# 7. OFFICIAL LAYER-2 MODULE AUDIT

Verify exactly these 8 official modules:

1. L2-M01 Baseline trainer
2. L2-M02 Prediction logger
3. L2-M03 Low-calibration curve builder
4. L2-M04 Subject difficulty profiler
5. L2-M05 Model-family registry
6. L2-M06 Ensemble comparison builder
7. L2-M07 Compact SSL adapter
8. L2-M08 Downstream readiness validator

Verify all **53 required implementation capabilities**. For every capability identify implementation file, function/class, config, input, output, test, stage, artifact, and consumer.

Required:

```text
OFFICIAL_LAYER2_MODULE_COUNT = 8
OFFICIAL_LAYER2_MODULES_IMPLEMENTED = 8
REQUIRED_LAYER2_CAPABILITIES = 53
REQUIRED_LAYER2_CAPABILITIES_IMPLEMENTED = 53
MISSING_REQUIRED_L2_SUBMODULES = 0
```

# 8. STUB / PLACEHOLDER AUDIT

Search all implementation files for `pass`, `NotImplementedError`, TODO, TBD, FIXME, placeholder, dummy, fake result, temporary implementation, mock production output, empty required returns, `SCIENTIFIC_EXECUTION=False`, and equivalent incomplete behavior.

Classify each occurrence. Test/fixture placeholders may be lawful; production freeze-critical placeholders are not.

Required:

```text
FREEZE_CRITICAL_IMPLEMENTATION_PLACEHOLDERS = 0
```

# 9. PHASE CONFIGURATION AUDIT

Verify a true P02-capable configuration system exists, including phase discriminator, P02 fields, model/A0/A4 configs, budgets, seeds, metrics, statistics, resources, outputs, gates, and conditional-model rules.

Require schema validation, round-trip serialization, unknown-field behavior, semantic hashing, and deterministic normalized serialization.

# 10. P01 INPUT CONSUMPTION AUDIT

Verify correct read-only use of DatasetRecords, LabelMapRecords, SplitRecord, PreprocessingRecord, WindowRecords, ValidationReports, core derived-window artifact, A4 R2 artifact, manifests, and the P01→P02 handoff.

Do not resplit, relabel, rewindow, silently modify preprocessing/channels/denominators, or regenerate P01 data.

Required:

```text
P01_REQUIRED_INPUTS_UNRESOLVED = 0
P01_IMMUTABLE_INPUTS_MUTATED = 0
UNNECESSARY_P01_REGENERATION = 0
```

# 11. CORE P01 DATA CONTRACT AUDIT

Where authority verifies them, validate the inherited facts including 3 source datasets, 12,910 official windows, 172 subject shards, 0 invalid official windows, 160 Hz, 480-sample core windows, cue +0.5→+3.5 s, one window per included event, reject-out-of-bounds, and no clipping.

Do not hard-code counts without checking supplied manifests.

# 12. A4 INPUT CONTRACT AUDIT

Verify the final governed A4 R2 substrate, including where authority confirms:

```text
+0.0 → +3.5 s
560 samples
160 Hz
views 0:320, 120:440, 240:560
parent-event coverage 12,910 / 12,910
```

Require no missing/unexpected/duplicate parents, clipping, padding, fabrication, or silent event loss.

# 13. MODEL-PORTFOLIO AUDIT

Verify the 16 frozen branches exactly once:

```text
SAN-MAJ
SAN-STRAT
SAN-PERM
SAN-PRIOR
DIAG-LOGVAR
CLS-CSP-LDA
CLS-FBCSP-LR
RIE-TS-LR
RIE-EA-TS
RIE-MDM
DNN-EEGNET
DNN-FBCNET
DNN-SEQ
DNN-EGTC
SSL-CBRAMOD
SSL-REVE
```

Verify disposition counts:
- required/core 7,
- conditional 4,
- fallback 1,
- diagnostic 4.

For every model verify constructor, adapter, inputs, training, validation selection, checkpointing, prediction, score semantics, failure/resource behavior, admission logic, tests, run cells, and outputs.

Required:

```text
REQUIRED_MODEL_BRANCHES_MISSING = 0
UNAUTHORIZED_MODEL_BRANCHES = 0
```

# 14. CONDITIONAL MODEL AUDIT

Verify deterministic pre-result admission and governed terminal states such as ADMITTED, DEPENDENCY_BLOCKED, LICENSE_BLOCKED, CHECKPOINT_BLOCKED, CORPUS_OVERLAP_UNRESOLVED, INPUT_INCOMPATIBLE, RESOURCE_BLOCKED, CONDITIONAL_SKIP.

No conditional branch may silently disappear or inappropriately block all of P02.

# 15. TEST-SET LEAKAGE AUDIT

Prove final test evidence never selects model, architecture, hyperparameters, checkpoint, seed, representative model, ensemble, budget, or A4 representative.

Verify code, not documentation only. Add negative tests.

Required:

```text
TEST_SELECTION_LEAKAGE = 0
```

# 16. SEED / REPEAT AUDIT

Verify deterministic seed behavior, including the frozen master seed `20260804` where applicable, identity-based subseed derivation, and exact repeat counts. No implicit/unrecorded RNG or seed drift across resume/worker/kernel.

# 17. LOW-LABEL BUDGET AUDIT

Verify inherited budgets `1,2,4,8,16,32`, exact inherited subset membership, and only authorized low-label branches.

Required:

```text
LOW_LABEL_BUDGET_DRIFT = 0
```

# 18. SEARCH / HYPERPARAMETER AUDIT

Verify bounded search with declared candidate list/order, success requirement, validation criterion, tie breaker, early stop, resource cap, and failure classification.

Required:

```text
RESULT_DEPENDENT_SEARCH_EXPANSION = 0
```

# 19. SCORE-SEMANTICS AUDIT

For every branch verify predicted class, class order, probabilities, logits, decision scores, positive-class semantics, and missing-score reason.

Do not fabricate unsupported probabilities.

Required:

```text
P03_SCORE_SEMANTICS_GUESSWORK = 0
```

# 20. CHECKPOINT AUDIT

Every accepted trained branch must support:

```text
train → save → hash → clean reload → inference → equivalence check
```

Checkpoint lineage must bind model, dataset, split, window, budget, seed, config, scientific freeze, and code revision.

Reject stale/mismatched checkpoints.

# 21. A0 OWNERSHIP AUDIT

Verify:

```text
A0 = FULL_EXECUTION_REQUIRED_IN_P02
```

A0 must be actual executable scientific workload, not only schema/config/readiness/future note.

Verify all **678/678** planned A0 cells exist in orchestration with identity, model, dataset, budget, seed, condition, stage, output, metrics, and terminal behavior.

Required:

```text
A0_PLANNED_CELLS = 678
A0_IMPLEMENTED_CELLS = 678
A0_MISSING_CELLS = 0
```

# 22. A0 SCIENTIFIC-BOUNDARY AUDIT

A0 must remain raw-decoder/accept-all reference. No calibration, threshold selection, rejection, abstention, selective-prediction, or A1/A2/A3 behavior may enter A0.

Required:

```text
DOWNSTREAM_BEHAVIOR_LEAKED_INTO_A0 = 0
```

# 23. A4 OWNERSHIP AUDIT

Verify:

```text
A4 = FULL_EXECUTION_REQUIRED_IN_P02
```

Implement all six conditions:
- A4-C0-CORE
- A4-C1-LONG-3P5S
- A4-C2-MULTI-HARD-VOTE
- A4-C3-MULTI-PROB-AVG
- A4-C4-MODEL-HARD-VOTE
- A4-C5-MODEL-PROB-AVG

Verify **1,218/1,218** planned A4 slots.

Required:

```text
A4_PLANNED_SLOTS = 1218
A4_IMPLEMENTED_SLOTS = 1218
A4_MISSING_SLOTS = 0
```

# 24. TOTAL PHASE-OWNED ABLATION AUDIT

Verify actual implementation expansion:

```text
A0 = 678
A4 = 1,218
TOTAL = 1,896
```

Require 1,896 implemented cells, unique IDs, no missing cells.

# 25. A4 REPRESENTATIVE-SELECTION AUDIT

Verify representative selection is validation-only. Final test data may not choose representative branch, model, seed, or ensemble member.

# 26. A4 COMMON-SUPPORT AUDIT

For every matched comparison export baseline eligible denominator, alternative eligible denominator, matched denominator, unmatched baseline/alternative cases, and missing reasons.

No silent denominator shrinkage.

# 27. ADDITIONAL FULL-EXECUTION ABLATION CONTROLLER

Audit Stage 18U. It must not create a second execution mode.

An additional ablation enters P02 only if pre-result authority marks it `FULL_EXECUTION_REQUIRED_IN_P02` and all implementation requirements are resolved.

If none is unlocked, record:

```text
NO_ADDITIONAL_FULL_EXECUTION_ABLATION_UNLOCKED
```

# 28. A1–A13 OWNERSHIP AUDIT

Verify exact ownership/disposition of A0–A13 and ensure P02 executes only what it owns while producing downstream substrate.

Required:

```text
DOWNSTREAM_ABLATIONS_PREMATURELY_EXECUTED = 0
```

# 29. A14 PROHIBITION

Search notebook, source, configs, run matrix, records, tests, bundle schemas, handoffs.

Only explicit prohibition/absence references are lawful.

Required:

```text
A14 = ABSENT_PROHIBITED
A14_RUN_CELLS = 0
A14_CONFIGS = 0
A14_RESULTS = 0
```

# 30. EVALUATION COMPLETENESS AUDIT

Audit all **12 expected P02 evaluation families**. For each map scientific question, run cells, stage, raw evidence, metric, statistical treatment, record, figure/table source, validator, gate, and Phase Analysis consumer.

Required:

```text
EXPECTED_P02_EVALUATIONS = 12
P02_EVALUATIONS_IMPLEMENTED = 12
EXPECTED_EVALUATIONS_WITH_INCOMPLETE_EXECUTION_PLAN = 0
```

# 31. METRIC AUDIT

Verify every frozen metric definition, implementation, class convention, aggregation, denominator, missing-value handling, participant/session scope, tests, golden vectors, and records. No conflicting duplicate implementations.

# 32. STATISTICAL AUDIT

Verify exact frozen statistical behavior, including where applicable 95% intervals, 10,000 participant-cluster bootstrap resamples, BCa, percentile fallback, Wilcoxon, Friedman, paired Wilcoxon post-hoc, Holm correction, and minimum 5 complete participant pairs/blocks.

Verify code and synthetic tests.

# 33. PARTICIPANT-LEVEL INFERENCE AUDIT

Verify participant-level inference and no window-level pseudoreplication. Test participant aggregation explicitly.

# 34. RECORD-SCHEMA AUDIT

Verify required record families, including at minimum PredictionRecord, ModelRegistryRecord, BaselineMetricRecord, LowCalibrationCurveRecord, SubjectProfileRecord, EnsembleControlRecord, FailureCaseIndex, Layer2ReadinessReport, NegativeResultNote, DiagnosticOnlyFlag, plus every Registry-required support record.

Each requires writer, schema, validator, identity, lineage, lifecycle, stage, consumer.

Required:

```text
REQUIRED_RECORD_FAMILIES_WITHOUT_WRITER = 0
REQUIRED_RECORD_FAMILIES_WITHOUT_VALIDATOR = 0
```

# 35. ARTIFACT COMPLETENESS AUDIT

Audit all required artifact/support families, expected frozen target **26/26**.

Each needs producer, inputs, contents, path, schema, validator, gate, lifecycle, consumer.

Required:

```text
REQUIRED_ARTIFACTS_WITHOUT_PRODUCER = 0
REQUIRED_ARTIFACTS_WITHOUT_VALIDATOR = 0
EXPECTED_ARTIFACTS_NOT_PRODUCED_BY_DESIGN = 0
```

# 36. FIGURE-SOURCE AUDIT

Verify future expected figures have source data, including model comparison, low-label curve, participant/session distributions, A0, A4, failure distributions, score availability, resource status.

Required:

```text
EXPECTED_FIGURES_WITHOUT_SOURCE_DATA = 0
```

# 37. TABLE-SOURCE AUDIT

Verify all expected analytical tables have precomputed source data.

Required:

```text
EXPECTED_TABLES_WITHOUT_SOURCE_DATA = 0
```

# 38. PHASE ANALYSIS EVIDENCE AUDIT

Simulate future Phase Analysis. For every expected analytical question identify the exact emitted artifact.

Required:

```text
P02_ANALYSIS_REQUIREMENTS_WITHOUT_PLANNED_EVIDENCE = 0
PHASE_ANALYSIS_REQUIRED_BUT_UNEXECUTED_EVALUATIONS = 0
```

Phase Analysis must not need to complete missing science.

# 39. PROTOCOL HANDOFF AUDIT

Verify runtime export of everything Protocol v1.0 needs: models, configs, seeds, budgets, run cells, A0, A4, any lawfully admitted extra ablation, environment, metrics, statistics, exclusions, failures, blocks, reruns, amendments, external artifacts, limitations.

# 40. LAYER 0 HANDOFF AUDIT

Verify finding identities, evidence identities, limitation identities, negative-result evidence, evidence ceilings, and claim-boundary inputs without prematurely approving claims.

# 41. EVIDENCE MAP HANDOFF AUDIT

Verify stable IDs for run, model, checkpoint, prediction, metric, ablation, control, failure, figure/table source, external artifact, reproduction asset.

# 42. LAYER 10 HANDOFF AUDIT

Verify Layer 10 can READ → VERIFY → RENDER → PACKAGE without scientific recomputation.

Required:

```text
LAYER10_REQUIRED_SCIENTIFIC_RECOMPUTATION = 0
```

# 43. P03 HANDOFF AUDIT

Verify P03 receives all raw prediction substrate: PredictionRecords, probabilities/logits/decision scores, predicted classes, class order, model/checkpoint IDs, dataset/subject/session/event/window IDs, split role, budget, seed, A0/A4 identity, aggregation identity, failure/missingness, metric dictionary.

Required:

```text
P03_REQUIRED_PREDICTION_FIELDS_MISSING = 0
P03_REQUIRED_RAW_INFORMATION_MISSING = 0
P03_SCORE_SEMANTICS_GUESSWORK = 0
```

# 44. DOWNSTREAM OWNERSHIP AUDIT

Search for accidental Layer-3+ confirmatory science such as CalibrationRecord, UncertaintyRecord, SelectivePredictionRecord, ThresholdRegistryRecord, risk/policy/stress/embodiment decisions.

Required:

```text
L3PLUS_RESPONSIBILITY_STOLEN_BY_P02 = 0
```

# 45. COMPLETE NOTEBOOK-STAGE AUDIT

Use exact R4 stage plan. Verify **26/26 governed stages** with stage ID, purpose, entry point, inputs, dependencies, config, run cells, outputs, tests, gates, failure states, checkpoint/resume behavior, artifact paths, handoff.

Required:

```text
MISSING_NOTEBOOK_STAGES = 0
UNIMPLEMENTED_STAGE_ENTRY_POINTS = 0
```

# 46. STAGE DEPENDENCY DAG AUDIT

Build and validate the real DAG: no missing/impossible dependency, unintended cycle, descendant after failed prerequisite, or unnecessary rerun of unrelated earlier stages.

# 47. STAGE IDEMPOTENCY AUDIT

For every stage determine safe first run, safe retry, partial output detection, completion marker, duplicate protection, atomic output, descendant invalidation.

Required:

```text
UNSAFE_STAGE_RETRIES = 0
```

# 48. DUPLICATE SCRATCH AUDIT

Test repeated stage submission and ensure N expected records cannot become 2N without detection.

Required:

```text
DUPLICATE_SCRATCH_UNDETECTED = 0
```

# 49. REVISION-GUARD AUDIT

Verify one canonical current revision identity across notebook, worker, source package, stage plan, config, scientific freeze.

Required:

```text
STALE_REVISION_GUARDS = 0
```

# 50. ISOLATED-WORKER AUDIT

If workers are used, verify source fingerprint, PID, Python, sys.path, package import, config hash, notebook revision, scientific freeze ID on startup. A stale worker must not continue. Add a synthetic stale-source mismatch test.

# 51. IMPORT-GRAPH AUDIT

Run compileall, clean subprocess imports, clean worker imports, all stage entry-point imports.

Required:

```text
UNRESOLVED_IMPORTS = 0
MALFORMED_SHIMS = 0
MISSING_RUNTIME_MODULES = 0
```

# 52. ENVIRONMENT AUDIT

Verify clean-Kaggle bootstrap and the exact environment contract for Python, CUDA, PyTorch, MNE, MOABB where needed, Braindecode where needed, pyRiemann, NumPy, SciPy, scikit-learn, pandas, h5py, and project modules.

Distinguish frozen environment intent from observed runtime environment.

# 53. DEPENDENCY-PIN AUDIT

For every dependency determine required version, allowed compatibility range if any, installation method, network/cached behavior, import validation, scientific consequence of mismatch.

Required:

```text
UNRESOLVED_FREEZE_CRITICAL_DEPENDENCY = 0
```

# 54. CLEAN-KAGGLE PRE-FLIGHT SIMULATION

Simulate fresh Kaggle session with `/kaggle/input` read-only, `/kaggle/working` empty, declared inputs only, no hidden authoring files.

Required:

```text
UNDECLARED_RUNTIME_FILES = 0
```

# 55. REQUIRED KAGGLE INPUT AUDIT

Document every required input with name, purpose, provider, handle/path, revision, SHA-256, size, required/conditional, license/access, validation method.

Required:

```text
REQUIRED_KAGGLE_INPUTS_NOT_DOCUMENTED = 0
```

# 56. EXTERNAL POINTER AUDIT

Verify provider, handle, revision, hash, size, license, access, retrieval instructions. Do not trust filename only.

# 57. CONDITIONAL CHECKPOINT AUDIT

Verify checkpoint revision/hash/license/corpus-overlap/input/channel/sampling/length/GPU compatibility before expensive work. Unavailable conditional branches must resolve lawfully.

# 58. RESOURCE-PREFLIGHT AUDIT

Estimate input, temporary training files, checkpoints, predictions, A0, A4, metrics, figure/table sources, bundle, safety margin.

Required:

```text
RESOURCE_REQUIREMENTS_UNMEASURED = 0
```

# 59. KAGGLE DISK AUDIT

Ensure no unnecessary P01 duplication, redundant unpacking, unsafe cleanup, deletion of governing inputs, or failure to persist expensive outputs.

# 60. SESSION-EXPIRATION AUDIT

Verify lawful resumability for completed run cells, models, prediction partitions, A0/A4 partitions, metrics, failure partitions, manifest fragments. Every reusable checkpoint validates dependency hashes.

Required:

```text
UNSAFE_STALE_CHECKPOINT_REUSE = 0
```

# 61. REMOTE PERSISTENCE AUDIT

Separate COMPUTE → VALIDATE → FREEZE LOCAL → PERSIST REMOTELY. Remote upload failure must not force scientific recomputation.

Required:

```text
REMOTE_PERSISTENCE_FAILURE_FORCES_SCIENCE_RERUN = 0
```

# 62. PROVIDER-CONSTRAINT PREFLIGHT

Before remote publication validate credentials, username, handle, slug, title length, permission, provider API, versioning, network.

# 63. HEARTBEAT / LOGGING AUDIT

Long stages must persist detailed logs and compact visible heartbeats with stage, elapsed time, run cell, model, dataset, resources, log path.

# 64. FAILURE TAXONOMY AUDIT

Verify governed terminal states such as SUCCESS, FAILED, NONCONVERGENT, RESOURCE_BLOCKED, LICENSE_BLOCKED, CHECKPOINT_BLOCKED, CORPUS_OVERLAP_UNRESOLVED, INPUT_INCOMPATIBLE, CONDITIONAL_SKIP, INVALID, DIAGNOSTIC_ONLY.

Every attempted cell gets exactly one terminal state.

# 65. NEGATIVE-EVIDENCE AUDIT

Preserve failed fits, nonconvergence, NaN/Inf, blocks, incompatibilities, missing scores/probabilities, reload failures, unmatched comparisons, sparse budgets, insufficient participant support, null/negative outcomes.

# 66. TEST CATALOG AUDIT

Verify unit, schema, config, integration, import, worker-import, lineage, leakage, class-order, score-semantics, metrics, golden-vector, seed, budget, subject-profile, checkpoint, A0, A4, matched-comparison, conditional-admission, failure, resources, security, bundle, reproduction, idempotency, dependency, duplicate-scratch tests.

Required:

```text
FREEZE_CRITICAL_BEHAVIORS_WITHOUT_TEST_OR_VALIDATION = 0
```

# 67. NEGATIVE TEST AUDIT

Actively test wrong class order, leakage, invalid lineage/checkpoint/config, missing score, A4 mismatch, unsafe path, secret injection, stale worker, duplicate run ID/scratch, downstream ownership violation, A14 attempt.

# 68. GOLDEN-VECTOR TEST AUDIT

Independently compute expected BACC, F1, ACC, AUC where applicable, confusion matrix, hard vote, probability average, participant aggregation, paired differences, Holm correction, seed derivation.

# 69. GATE AUDIT

Verify all **26 P02 gates** with ID, owner, requirement, validator, evidence path, pass/fail criterion, repair owner, dependent stage.

Required:

```text
P02_GATES_EXPECTED = 26
P02_GATES_IMPLEMENTED = 26
MISSING_REQUIRED_P02_GATES = 0
```

# 70. BUNDLE-CONTRACT AUDIT

Verify runtime bundle can actually produce README, authority/source/environment/notebook/config manifests, inputs, records, checkpoints/pointers, raw outputs, metrics, diagnostics, negative/failed results, figure/table sources, logs, manifests, analysis inputs, Protocol/L0/EMap/L10/P03 handoffs, gate decision, phase handoff, checksums.

Required:

```text
MISSING_REQUIRED_EXECUTION_BUNDLE_OUTPUTS = 0
```

# 71. PARTIAL-FAILURE BUNDLE AUDIT

Simulate a mid-run failure and verify truthful partial bundle distinguishing accepted, partial, failed, unexecuted, blockers.

# 72. MANIFEST AUDIT

Verify runtime generation of authority, input, environment, config, run-cell, checkpoint, record, artifact, failure, external-pointer, bundle manifests; all versioned/checksummed.

# 73. CHECKSUM AUDIT

Use SHA-256. Generate/reopen synthetic dry-run archive, CRC check, safe paths, all targets, missing/mismatch check.

Required:

```text
CHECKSUM_MISSING = 0
CHECKSUM_MISMATCH = 0
```

# 74. PATH-SAFETY AUDIT

Search for authoring-machine paths including `/mnt/data/`, `/Users/`, author home, temp paths, Windows local drives, unsafe `../../`.

Required:

```text
TRANSIENT_AUTHORING_PATHS = 0
```

# 75. SECRET AUDIT

Scan notebook/source/output/config/logs/manifests/archives/environment for tokens, keys, passwords, cookies, OAuth/private credentials. Never print found values.

Required:

```text
SECRETS = 0
```

# 76. FILE-DOWNLOAD / EXPORT AUDIT

Verify final outputs are written to `/kaggle/working/`, not only FileLink, and final summary prints filename, path, size, SHA-256 and retrieval instructions.

# 77. NOTEBOOK JSON AUDIT

Validate nbformat, cell structure, metadata, order, stage headings, syntax, no malformed outputs/fake results/false completion state.

# 78. STRUCTURED FILE AUDIT

Parse every JSON, JSONL, YAML, CSV, IPYNB.

Required:

```text
STRUCTURED_PARSE_FAILURES = 0
```

# 79. IMPORTABLE PACKAGE AUDIT

Major implementation logic should live in importable project modules where practical; notebook orchestrates rather than becoming a monolithic script.

# 80. NOTEBOOK SELF-CONTAINMENT AUDIT

The notebook/package must run from declared Kaggle inputs without hidden files.

Required:

```text
HIDDEN_REQUIRED_FILES = 0
```

# 81. ONE-NOTEBOOK FULL-SCOPE AUDIT

Exactly one scientific execution notebook; no fast/A0/A4/SSL/analysis/optional scientific notebook split.

Required:

```text
SCIENTIFIC_NOTEBOOK_COUNT = 1
```

# 82. NO QUALITY-REDUCTION AUDIT

Verify no work was removed because the notebook was long, models expensive, A4 large, 1,896 cells inconvenient, tests numerous, or artifact handling difficult.

Required:

```text
QUALITY_REDUCTION_FOR_CONVENIENCE = 0
```

# 83. NO UNAUTHORIZED COMPLEXITY AUDIT

Remove accidental duplicate modules/configs/current authorities/run matrices/schemas/artifact identities/P01 data/execution paths while preserving intentional history.

# 84. P01 FAILURE-REGRESSION AUDIT

Verify safeguards for stale revision, stale worker code, dependency-ID mismatch, A4 parent mismatch, duplicate scratch retry, late import, malformed shim, worker path mismatch, unrealistic disk preflight, provider/API constraints, remote persistence recomputation, session expiration, checkpoint mismatch, secret serialization, contaminated bundle, download fragility.

Create `P02_P01_FAILURE_REGRESSION_AUDIT.csv`.

Required:

```text
P01_FAILURE_PREVENTION_ITEMS_UNRESOLVED = 0
```

# 85. FIRST COMPLETE AUDIT

Perform complete source-authority → implementation audit. Repair genuine defects rather than merely report them.

# 86. SECOND INDEPENDENT AUDIT

Re-review repaired package from scratch and ask: would this truly implement all P02 if Run All were pressed? Repair new defects.

# 87. THIRD OMISSION-FOCUSED AUDIT

Focus only on omissions across Build Book, capabilities, models, conditional states, run cells, stages, tests, gates, artifacts, records, evaluations, A0/A4 cells, Phase Analysis evidence, Layer-10 sources, P03 fields, limitations, inputs, imports, resume, retry, remote failures, secrets. Repair every real omission.

# 88. ADVERSARIAL SCIENTIFIC REVIEW

Act as senior EEG/BCI scientist, ML reviewer, reproducibility reviewer, thesis examiner. Seek leakage, invalid fairness/denominators/inferential units/class semantics/model selection/post-hoc design/A0 contamination/A4 mismatch/downstream theft.

# 89. ADVERSARIAL SOFTWARE REVIEW

Try to break imports, configs, schemas, stage runner, checkpoint manager, writers, atomic writes, parallelism, resume, artifact resolution, manifests, bundle generation, checksums.

# 90. ADVERSARIAL KAGGLE REVIEW

Test clean kernel, declared inputs only, GPU/no GPU, network/no network, private artifact availability, missing conditional checkpoint, low disk, session restart, stage retry, worker restart, partial scratch, corrupt checkpoint/pointer, remote failure, missing secret, final ZIP export.

# 91. RUN-ALL SIMULATION

Simulate notebook sequentially. For every cell/stage ask what variables/files/packages/inputs/outputs/dependencies/failures/resume states exist.

Required:

```text
RUN_ALL_UNDEFINED_REFERENCES = 0
RUN_ALL_MISSING_DEPENDENCIES = 0
```

# 92. CLEAN-SUBPROCESS SIMULATION

Do not trust imports that work only because the current session already imported/patched something. Perform clean-process checks.

# 93. ISOLATED-WORKER SIMULATION

If workers exist, start one using only final package inputs. Require worker-ready PASS.

# 94. SYNTHETIC END-TO-END SMOKE TEST

Use tiny synthetic EEG-like fixture through input adapter → visibility → baseline model → training → checkpoint → prediction → PredictionRecord → metric → subject profile → A0 path → A4 aggregation → failure record → gate → bundle writer → handoff schema.

Purpose is integration correctness, not scientific validity.

# 95. CHECKPOINT RESUME SIMULATION

Tiny fixture: train → save → terminate → new process → load → verify dependencies → resume/infer → equivalence.

# 96. STAGE-RETRY SIMULATION

Run a synthetic stage twice; verify no duplication.

# 97. PARTIAL-FAILURE SIMULATION

Cause a controlled failure; verify logging, terminal state, dependency invalidation, upstream preservation, failure bundle, no false completion.

# 98. PHASE ANALYSIS SIMULATION

Pretend P02 execution succeeded and try writing future analysis using emitted artifacts only. If any required analysis lacks evidence, notebook design is incomplete; repair it.

# 99. PROTOCOL SIMULATION

Ensure every actual execution fact future Protocol needs has a runtime field/artifact.

# 100. LAYER 0 SIMULATION

Ensure evidence/limitation/negative-result state needed for future claim review is preserved.

# 101. EVIDENCE MAP SIMULATION

Ensure future findings can trace to stable run/record/artifact/metric/failure/figure/table identities.

# 102. LAYER 10 SIMULATION

Ensure no scientific recomputation is required.

# 103. P03 SIMULATION

Act as P03 engineer. It must consume scores/class order/checkpoint/window/A0/A4/budget/seed/missingness/blocked status programmatically without asking P02 developers.

# 104. FULL TRACEABILITY REGENERATION

After repairs regenerate Build Book→Notebook, method, evaluation, ablation, artifact, module/capability, stage, run-cell, gate, P01-regression coverage. All must reference current repaired package.

# 105. HUMAN/MACHINE PARITY

README, notebook documentation, configs, YAML, CSV, source code, schemas, tests must not contradict each other.

Required:

```text
HUMAN_MACHINE_DRIFT = 0
```

# 106. CURRENT/PREDECESSOR PROVENANCE AUDIT

Search stale R2/R3/current IDs, old stage plans/configs/scientific status. Historical references allowed only if clearly marked.

Required:

```text
STALE_AUTHORITY_CONFLICTS = 0
```

# 107. SECURITY/PACKAGING FINAL PASS

Remove transient outputs; keep clearly marked fixtures only; scan secrets/paths; parse structures; compile; run tests; validate notebook; regenerate checksums.

# 108. FINAL PACKAGE REBUILD

If any file changed, regenerate affected notebook/package/matrices/README/checksums and rebuild ZIP. Never leave stale hashes.

# 109. POST-PACKAGE VALIDATION

Validate the actual ZIP: CRC, safe members, inventory, checksums, structured parse, notebook/source/config/tests presence, no secrets/transient paths/broken internal refs.

# 110. FINAL PRE-EXECUTION READINESS MATRIX

Produce a comprehensive matrix containing at least:
- Governance/seven authorities/R4/P00-P01/P01 notebook/P01→P02 handoff utilization.
- L2 modules 8/8, capabilities 53/53.
- Model branches 16/16: core 7, conditional 4, fallback 1, diagnostic 4.
- P01 immutable input, core window, A4 R2, class order, score semantics, leakage.
- Seeds, budgets, search bounds.
- A0 678/678, A4 1,218/1,218, total 1,896/1,896.
- A1-A3/A5-A13 ownership, A14 absence.
- Evaluations 12/12.
- Record/artifact families complete, artifact/support 26/26.
- Metrics, statistics, participant inference.
- Notebook stages 26/26, dependencies/idempotency/retry/worker revision.
- Environment/dependencies/bootstrap/inputs/pointers/resources.
- Resume/checkpoints/remote persistence.
- Tests/negative/golden/gates 26/26.
- Figure/table source data.
- Protocol/Analysis/L0/EMap/L10/P03 handoffs.
- All traceability surfaces.
- P01 regression.
- compile/import/worker/structured/IPYNB/synthetic/checkpoint/retry/failure/bundle/security/path/checksum/post-ZIP.
- Scientific execution = NO; fabricated evidence = NO; unresolved defects/blockers counts; readiness YES/NO.

# 111. ZERO-UNRESOLVED CONDITION

Before PASS require all existing zero invariants, including:

```text
UNMAPPED_REQUIRED_P02_REQUIREMENTS = 0
MISSING_REQUIRED_L2_SUBMODULES = 0
REQUIRED_MODEL_BRANCHES_MISSING = 0
A0_MISSING_CELLS = 0
A4_MISSING_SLOTS = 0
FULL_P02_ABLATIONS_WITH_UNDEFINED_IMPLEMENTATION = 0
FULL_P02_ABLATIONS_WITH_UNDEFINED_RUN_CELLS = 0
FULL_P02_ABLATIONS_WITH_UNDEFINED_METRICS = 0
FULL_P02_ABLATIONS_WITH_UNDEFINED_COMPARISONS = 0
FULL_P02_ABLATIONS_WITH_UNDEFINED_ANALYSIS_OUTPUTS = 0
EXPECTED_EVALUATIONS_WITH_INCOMPLETE_EXECUTION_PLAN = 0
EXPECTED_FIGURES_WITHOUT_SOURCE_DATA = 0
EXPECTED_TABLES_WITHOUT_SOURCE_DATA = 0
REQUIRED_ARTIFACTS_WITHOUT_PRODUCER = 0
REQUIRED_ARTIFACTS_WITHOUT_VALIDATOR = 0
REQUIRED_RECORD_FAMILIES_WITHOUT_WRITER = 0
REQUIRED_RECORD_FAMILIES_WITHOUT_VALIDATOR = 0
REQUIRED_P02_BEHAVIORS_WITHOUT_KAGGLE_STAGE = 0
UNIMPLEMENTED_STAGE_ENTRY_POINTS = 0
UNRESOLVED_IMPORTS = 0
MISSING_REQUIRED_P02_GATES = 0
P02_ANALYSIS_REQUIREMENTS_WITHOUT_PLANNED_EVIDENCE = 0
LAYER10_REQUIRED_SCIENTIFIC_RECOMPUTATION = 0
P03_REQUIRED_PREDICTION_FIELDS_MISSING = 0
P03_REQUIRED_RAW_INFORMATION_MISSING = 0
P03_SCORE_SEMANTICS_GUESSWORK = 0
RELEVANT_P01_LIMITATIONS_LOST_AT_P02_BOUNDARY = 0
P01_FAILURE_PREVENTION_ITEMS_UNRESOLVED = 0
TRANSIENT_AUTHORING_PATHS = 0
SECRETS = 0
FREEZE_CRITICAL_IMPLEMENTATION_PLACEHOLDERS = 0
FREEZE_CRITICAL_IMPLEMENTATION_BLOCKERS = 0
```

# 112. IMPORTANT DISTINCTION — READY DOES NOT MEAN EXECUTED

A successful result means:

```text
P02 implementation: COMPLETE
P02 notebook: PRE-EXECUTION VALIDATED
P02 companion package: PRE-EXECUTION VALIDATED
P02 scientific execution: NOT YET STARTED
```

Do not call P02 scientifically complete.

# 113. BLOCKED CONDITION

If a genuine freeze-critical issue remains, issue:

```text
P02_KAGGLE_PREEXECUTION_AUDIT:
BLOCKED
```

For each blocker report blocker ID, source authority, lawful owner, affected Build Book requirement/module/capability/model/ablation/evaluation/run cells/stage/artifact, exact defect, why authority cannot resolve it, minimum repair, whether Build Book/P00/P01/notebook revision is required, and Kaggle/downstream consequences.

Do not manufacture blockers or misclassify ordinary coding defects.

# 114. REPAIR POLICY

For every repairable implementation defect:

```text
find defect
→ identify governing requirement
→ repair minimum correct scope
→ synchronize dependent implementation
→ regenerate affected artifacts
→ rerun affected tests
→ rerun full audit
```

Do not change frozen science merely to fix code.

# 115. SUCCESS CONDITION

PASS requires authority/prior-state/input/module/capability/method/model/A0/A4/ablation/evaluation/run-matrix/record/artifact/stage/test/gate/failure/checkpoint/environment/Kaggle-input/bundle/downstream/P01-hardening/security/static/synthetic/post-package completeness and zero freeze-critical ambiguity.

# 116. REQUIRED SUCCESS CERTIFICATION

If all requirements pass, state exactly:

```text
P02_KAGGLE_PREEXECUTION_AUDIT:

PASS — BUILD-BOOK-EXHAUSTIVE,
AUTHORITY-CONSISTENT,
PRIOR-STATE-CONSISTENT,
INPUT-COMPLETE,
MODULE-COMPLETE,
CAPABILITY-COMPLETE,
MODEL-COMPLETE,
ABLATION-COMPLETE-IN-IMPLEMENTATION,
EVALUATION-COMPLETE-IN-IMPLEMENTATION,
ARTIFACT-COMPLETE-IN-DESIGN,
P01-FAILURE-HARDENED,
RUNNABILITY-VALIDATED,
STATICALLY-VALIDATED,
SYNTHETICALLY-VALIDATED,
SECURITY-VALIDATED,
POST-PACKAGE-VALIDATED,
AND READY FOR ACTUAL KAGGLE EXECUTION
```

Then state the final readiness facts: P02 execution NOT STARTED, notebook/package complete, Governance/seven authorities/P00-P01/handoff complete, 8/8 modules, 53/53 capabilities, 16/16 branches, A0 678/678 executable, A4 1,218/1,218 executable, total 1,896/1,896, A14 prohibited, 12/12 evaluations, 26/26 artifact/support, 26/26 stages/gates, P01 inputs resolved, figure/table source design complete, all downstream handoffs complete, regression safeguards PASS, clean bootstrap/compile/import/synthetic/negative/checkpoint/resume/bundle/security/checksum/post-package PASS, 0 defects/blockers, no fabricated science.

# 117. REQUIRED OUTPUTS

Deliver repaired/final artifacts, including:
1. corrected notebook,
2. corrected package ZIP,
3. detached SHA,
4. comprehensive audit report,
5. Build Book→Notebook traceability,
6. module/capability coverage,
7. model coverage,
8. A0/A4 run-cell audit,
9. evaluation audit,
10. artifact audit,
11. gate audit,
12. P01 regression audit,
13. clean-Kaggle/bootstrap audit,
14. environment/dependency audit,
15. import/compile validation,
16. synthetic/golden report,
17. negative-test report,
18. checkpoint/resume/retry audit,
19. bundle dry-run,
20. secret/path audit,
21. final ZIP validation,
22. exact Kaggle inputs,
23. user actions before Run All,
24. final PASS/BLOCKED certification.

# 118. FINAL COMMAND

Perform the complete independent pre-execution double-check, triple-check, adversarial review, reconciliation, repair, runnability validation, artifact/ablation/evaluation/dependency/prior-state/downstream validation, using all authorities, Build Book R4, P00/P01 state, P01 execution bundle/notebook/history, Protocol/Analysis/L0/EMap/L10, handoff, repository, created P02 notebook/package.

Do not merely confirm file existence. Verify actual executable behavior, validation, artifact generation, and downstream consumption.

If P02 is expected to execute/evaluate/compare/measure/preserve/export/handoff something, the actual notebook behavior must exist and be runnable.

If A0 or A4 is P02-owned, every required run cell/comparison/metric/statistic/failure/record/artifact/downstream output must be executable, not merely described.

If a later document/phase requires P02 information, Kaggle execution must generate it now rather than force later scientific reconstruction.

Perform all audit/repair/simulation/rebuild/reopen/verify passes and issue PASS only with zero freeze-critical defects.

# 119. ABSOLUTE NON-DEFERRAL / NO-POSTPONEMENT IMPLEMENTATION DOCTRINE

Anything P02 owns and the finalized Build Book requires must already be **fully implemented** before PASS.

A required P02 responsibility may not count as complete merely because it is documented, planned, registered, configured, schema/interface-defined, listed in a run matrix, represented by a heading/class/future hook, marked READY/FOUNDATION_READY/INPUT_AVAILABLE/SUPPORTED, or deferred to Kaggle implementation/runtime coding, Phase Analysis, Layer 0, Evidence Map, Layer 10, P03, another notebook, patch, or package.

Required:

```text
P02_OWNED_REQUIRED_BEHAVIORS_POSTPONED = 0
```

# 120. WHAT “FULLY IMPLEMENTED” MEANS

For each P02-owned requirement verify the full chain:

```text
authority
→ Build Book
→ owner
→ source implementation
→ config
→ input/output contracts
→ schema/record where required
→ notebook stage
→ stage entry point
→ run-cell mapping where scientific
→ dependencies
→ tests/negative tests
→ gate
→ failure/terminal behavior
→ logging
→ checkpoint/resume where applicable
→ artifact writer/validator
→ bundle path
→ downstream consumer
→ Phase Analysis evidence / L0 / EMap / L10 / P03 handoff where applicable
```

Required:

```text
P02_REQUIRED_BEHAVIORS_WITH_PARTIAL_IMPLEMENTATION = 0
```

# 121. NO “IMPLEMENT LATER” ACCEPTANCE

Search for implement later, future work, pending implementation/integration, stub/skeleton/hook, defer, TODO/TBD/FIXME, NotImplementedError, pass, return None, dummy/mock production output, and equivalent.

Fixtures may be lawful only when not standing in for required P02 production behavior.

Required:

```text
FREEZE_CRITICAL_IMPLEMENT_LATER_MARKERS = 0
P02_OWNED_FEATURES_DEFERRED_TO_FUTURE_IMPLEMENTATION = 0
```

# 122. DOCUMENTATION-ONLY IMPLEMENTATION IS NOT IMPLEMENTATION

Every required behavior described in README/Markdown/Build Book/YAML/CSV/JSON/notebook comments/docstrings must have executable code where execution is required.

Required:

```text
DOCUMENTED_REQUIRED_BEHAVIORS_WITHOUT_EXECUTABLE_IMPLEMENTATION = 0
```

# 123. CONFIG-ONLY IMPLEMENTATION IS NOT IMPLEMENTATION

Every model/ablation/metric/statistical/stage/artifact/gate/resource config must be consumed by real code.

Required:

```text
CONFIGURED_REQUIRED_BEHAVIORS_WITHOUT_CONSUMER_CODE = 0
```

# 124. SCHEMA-ONLY IMPLEMENTATION IS NOT IMPLEMENTATION

Every required schema needs writer, identity allocator, lineage binder, validator, stage, path, manifest registration, consumer.

Required:

```text
REQUIRED_SCHEMAS_WITHOUT_RUNTIME_PRODUCER = 0
```

# 125. CLASS/FUNCTION-NAME-ONLY IMPLEMENTATION IS NOT IMPLEMENTATION

Reject named functions/classes that contain pass, NotImplementedError, constant/empty/fake production outputs, silent bypass, placeholder records.

Required:

```text
NAMED_BUT_NONFUNCTIONAL_REQUIRED_IMPLEMENTATIONS = 0
```

# 126. STAGE-HEADING-ONLY IMPLEMENTATION IS NOT IMPLEMENTATION

Every one of the 26 stages needs callable entry point, dependencies, config, input checks, implementation calls, output paths, terminal states, tests, gate evidence, logs, resume behavior.

Required:

```text
NOTEBOOK_STAGES_WITHOUT_EXECUTABLE_IMPLEMENTATION = 0
```

# 127. RUN-MATRIX-ONLY IMPLEMENTATION IS NOT IMPLEMENTATION

All 1,896 P02-owned full-ablation cells must resolve from run ID through model/condition/config/dataset/budget/seed/stage/execution/output/metric/failure.

Required:

```text
PLANNED_RUN_CELLS_WITHOUT_EXECUTABLE_RESOLUTION = 0
```

# 128. GATE-NAME-ONLY IMPLEMENTATION IS NOT IMPLEMENTATION

All 26 gates need executable validator, evidence, pass/fail criterion, caller, downstream enforcement.

Required:

```text
DECLARED_GATES_WITHOUT_EXECUTABLE_VALIDATOR = 0
```

# 129. TEST-NAME-ONLY IMPLEMENTATION IS NOT IMPLEMENTATION

Each declared test must exist, import, run, assert the intended invariant, fail invalid fixtures, pass valid ones where applicable.

Required:

```text
DECLARED_TESTS_WITHOUT_EXECUTABLE_TEST = 0
```

# 130. ARTIFACT-NAME-ONLY IMPLEMENTATION IS NOT IMPLEMENTATION

Every required artifact/support family needs producer, writer, path, schema, validator, manifest registration, consumer.

Required:

```text
DECLARED_ARTIFACTS_WITHOUT_RUNTIME_GENERATOR = 0
```

# 131. HANDOFF-NAME-ONLY IMPLEMENTATION IS NOT IMPLEMENTATION

Protocol, Phase Analysis, Layer 0, Evidence Map, Layer 10, P03 handoffs need real runtime/bundle population logic and exact required fields.

Required:

```text
DECLARED_HANDOFFS_WITHOUT_POPULATION_LOGIC = 0
```

# 132. NO POSTPONEMENT TO PHASE ANALYSIS

Metrics, comparisons, matched denominators, statistics, participant summaries, model/A0/A4 results, failure/negative censuses required for Phase Analysis must be produced by P02 execution.

Required:

```text
P02_SCIENCE_DEFERRED_TO_PHASE_ANALYSIS = 0
```

# 133. NO POSTPONEMENT TO LAYER 0

Layer 0 reviews evidence/claims; it must not generate missing P02 science.

Required:

```text
P02_SCIENCE_DEFERRED_TO_LAYER0 = 0
```

# 134. NO POSTPONEMENT TO EVIDENCE MAP

Evidence Map maps evidence; it must not create missing evidence.

Required:

```text
P02_SCIENCE_DEFERRED_TO_EVIDENCE_MAP = 0
```

# 135. NO POSTPONEMENT TO LAYER 10

Layer 10 reads/verifies/renders/packages/exports; it must not calculate missing P02 results.

Required:

```text
P02_SCIENCE_DEFERRED_TO_LAYER10 = 0
LAYER10_REQUIRED_SCIENTIFIC_RECOMPUTATION = 0
```

# 136. NO POSTPONEMENT TO P03

P03 may do its own Layer-3 science but must not reconstruct missing Layer-2 information.

Required:

```text
P02_LAYER2_INFORMATION_DEFERRED_TO_P03 = 0
```

# 137. NO POSTPONEMENT TO A SECOND NOTEBOOK

No required P02 science may be deferred into another Kaggle notebook, A0/A4/SSL/analysis/cleanup/postprocessing/artifact notebook.

Required:

```text
P02_REQUIRED_SCIENCE_DEFERRED_TO_SECOND_NOTEBOOK = 0
SCIENTIFIC_NOTEBOOK_COUNT = 1
```

# 138. NO POSTPONEMENT TO MANUAL USER INTERVENTION

The owner must not need to paste/edit code, choose methods/seeds/metrics/run cells/ensembles, fix schemas/imports/stages, merge artifacts, or reconstruct records mid-run.

Required:

```text
FREEZE_CRITICAL_MANUAL_INTERVENTIONS_DURING_RUN = 0
```

Declared Kaggle input attachment and lawful secret provisioning are allowed.

# 139. NO POSTPONEMENT THROUGH CONDITIONAL STATUS ABUSE

Mandatory P02 work may not be mislabeled conditional/optional/diagnostic/future/resource-dependent to avoid implementation.

Required:

```text
MANDATORY_P02_WORK_MISCLASSIFIED_AS_CONDITIONAL = 0
```

# 140. NO POSTPONEMENT THROUGH RESOURCE CONVENIENCE

Mandatory scope may not be dropped because GPU time is high, A4 expensive, 1,896 cells large, notebook long, artifacts numerous.

Required:

```text
MANDATORY_P02_SCOPE_DROPPED_FOR_RESOURCE_CONVENIENCE = 0
```

# 141. NO POSTPONEMENT THROUGH “FOUNDATION READY”

For P02-owned full-execution responsibilities, FOUNDATION_READY is insufficient. A0 and A4 require actual executable orchestration.

Required:

```text
P02_FULL_EXECUTION_ABLATIONS_ONLY_FOUNDATION_READY = 0
```

# 142. A0 MAXIMUM-COMPLETENESS AUDIT

Beyond 678 run IDs, verify A0 covers sanity controls, required/eligible models, full/low-label cells, seeds/repeats, training, selection, checkpoints, predictions, score semantics, metrics, participant aggregation, failures/negative results, records/manifests, figure/table sources, Protocol/Analysis/L0/EMap/L10/P03 outputs.

Required:

```text
A0_REQUIRED_BEHAVIORS_NOT_IMPLEMENTED = 0
```

# 143. A4 MAXIMUM-COMPLETENESS AUDIT

Beyond 1,218 slots, verify C0–C5, A4 R2 input, parent matching/common support, representative selection, hard/probability voting, model ensembles, score eligibility, burden/disagreement, metrics, matched differences, statistics, failures/negative outcomes, records, figure/table sources, Protocol/Analysis/L0/EMap/L10 outputs.

Required:

```text
A4_REQUIRED_BEHAVIORS_NOT_IMPLEMENTED = 0
```

# 144. ALL UNLOCKED P02 EVALUATIONS MUST BE EXECUTABLE

Any fully specified P02-owned required evaluation must be executable now, not merely planned/ready/analysis-only.

Required:

```text
FULLY_UNLOCKED_P02_EVALUATIONS_NOT_EXECUTABLE = 0
```

# 145. ALL FULLY UNLOCKED P02 ABLATIONS MUST BE EXECUTABLE

Any lawfully fully unlocked P02 ablation must have implementation, run cells, stage, metrics, comparisons, artifacts, tests, gates, analysis inputs in the same notebook.

Required:

```text
FULLY_UNLOCKED_P02_ABLATIONS_NOT_EXECUTABLE = 0
```

# 146. FULL FUNCTIONALITY AUDIT PER MODULE

For each module ask: if documentation/YAML disappeared, could executable code still perform the required P02 role?

Required:

```text
L2_MODULES_DOCUMENTATION_COMPLETE_BUT_FUNCTIONALLY_INCOMPLETE = 0
```

# 147. MAXIMUM ARTIFACT PRODUCTION AUDIT

Every mandatory governed artifact must have executable producer logic. Classify each artifact as mandatory/conditional/diagnostic/external/historical/not-applicable.

Required:

```text
MANDATORY_P02_ARTIFACTS_NOT_GENERATABLE = 0
```

# 148. MAXIMUM EVIDENCE-PRESERVATION AUDIT

Preserve successful, failed, blocked, negative/null, unmatched, missing-score, resource/license/checkpoint failures, runtime info, selection provenance, denominators, seeds.

Required:

```text
REQUIRED_P02_EVIDENCE_DROPPED_FOR_CONVENIENCE = 0
```

# 149. MAXIMUM DOWNSTREAM READINESS AUDIT

Simulate Protocol, Phase Analysis, Layer 0, Evidence Map, Layer 10, P03. All must have complete information without rerun/reconstruction/recomputation.

Required:

```text
DOWNSTREAM_CONSUMERS_REQUIRING_MISSING_P02_INFORMATION = 0
```

# 150. MAXIMUM FAILURE-HANDLING AUDIT

Every required scientific branch needs a governed terminal behavior; no uncaught/unknown/manual-fix/rerun-everything path unless the whole phase truly blocks.

Required:

```text
REQUIRED_P02_BRANCHES_WITHOUT_TERMINAL_FAILURE_BEHAVIOR = 0
```

# 151. MAXIMUM RESUMABILITY AUDIT

Where technically/scientifically appropriate, successful expensive work must survive kernel/worker/session/packaging/remote failures without unrelated recomputation.

Required:

```text
EXPENSIVE_COMPLETED_P02_WORK_WITHOUT_LAWFUL_RESUME_PATH = 0
```

# 152. MAXIMUM PRE-FLIGHT COMPLETENESS AUDIT

Anything knowable before expensive work—inputs/hashes/schema/imports/dependencies/packages/resources/checkpoints/licenses/provider rules/A4 match/class order/run expansion/output paths/secrets—must be determined before science.

Required:

```text
PREDETERMINABLE_FATAL_DEFECTS_DISCOVERABLE_ONLY_AFTER_SCIENCE_START = 0
```

# 153. IMPLEMENTATION-COVERAGE PERCENTAGE IS NOT ENOUGH

98%/99%/almost everything is not enough if any freeze-critical behavior is missing. Completion is categorical.

# 154. PREVIOUSLY IMPLEMENTED PARTS MUST NOT REGRESS

After every repair rerun all previously valid module/model/A0/A4/record/stage/gate/bundle/P01-regression tests.

Required:

```text
PREVIOUSLY_VALID_IMPLEMENTATION_REGRESSIONS = 0
```

# 155. NO PROMPT-REQUIREMENT LOSS DURING AUDIT

Preserve and execute every requirement in this cumulative Sections 1–274 file. Create a prompt-requirement exhaustion matrix.

Required:

```text
AUDIT_PROMPT_SECTIONS_NOT_EXECUTED = 0
```

# 156. FOUR-WAY COMPLETENESS TEST

Every requirement must pass:
A. specification completeness,
B. implementation completeness,
C. execution/orchestration completeness,
D. evidence completeness.

Required:

```text
SPECIFIED_BUT_NOT_IMPLEMENTED = 0
IMPLEMENTED_BUT_NOT_ORCHESTRATED = 0
ORCHESTRATED_BUT_NOT_EVIDENCE_PRODUCING = 0
EVIDENCE_PRODUCED_BUT_NOT_DOWNSTREAM_TRACEABLE = 0
```

# 157. END-TO-END CHAIN AUDIT

For every important responsibility prove:

```text
authority
→ Build Book
→ config
→ source
→ stage
→ run cell
→ model/control
→ execution
→ record
→ metric/statistic
→ artifact
→ manifest
→ bundle
→ downstream handoff
```

Required:

```text
BROKEN_P02_END_TO_END_REQUIREMENT_CHAINS = 0
```

# 158. NON-SCIENTIFIC SUPPORT CODE MUST ALSO BE COMPLETE

Verify loaders/resolvers/hashing/logging/heartbeat/resources/stage runner/checkpoints/writers/atomic writes/manifests/bundle/checksums/security/archive/resume/failure/handoff generators.

Required:

```text
FREEZE_CRITICAL_SUPPORT_COMPONENTS_NOT_IMPLEMENTED = 0
```

# 159. RUN ALL MUST NOT REQUIRE CODE EDITING

After declared inputs/secrets, Run All must not require mid-run scientific code edits.

Required:

```text
RUN_ALL_REQUIRES_MID_EXECUTION_CODE_EDIT = 0
```

# 160. FINAL ABSOLUTE DEFERMENT AUDIT

Search all later/future/defer/pending/manual/placeholder/follow-up/Phase-Analysis-will-calculate/Layer10-will-calculate/P03-will-derive/notebook-will-decide concepts. Classify lawful downstream vs unlawfully deferred P02 responsibility.

Required:

```text
UNLAWFULLY_DEFERRED_P02_RESPONSIBILITIES = 0
```

# 161. STRICT PASS RULE

PASS is forbidden for P02-owned requirements that remain only specified/configured/planned/schema-ready/interface-ready/foundation-ready/partial/manual/future-patch/downstream-computation dependent.

PASS requires:

```text
REQUIRED
+ OWNED BY P02
+ FULLY DEFINED
+ FULLY IMPLEMENTED
+ FULLY ORCHESTRATED
+ FULLY VALIDATED
+ FULLY ARTIFACT-PRODUCING
+ FULLY TRACEABLE
```

# 162. EXPANDED ZERO-UNRESOLVED INVARIANTS

Require all previous zero invariants plus:

```text
P02_OWNED_REQUIRED_BEHAVIORS_POSTPONED = 0
P02_REQUIRED_BEHAVIORS_WITH_PARTIAL_IMPLEMENTATION = 0
FREEZE_CRITICAL_IMPLEMENT_LATER_MARKERS = 0
P02_OWNED_FEATURES_DEFERRED_TO_FUTURE_IMPLEMENTATION = 0
DOCUMENTED_REQUIRED_BEHAVIORS_WITHOUT_EXECUTABLE_IMPLEMENTATION = 0
CONFIGURED_REQUIRED_BEHAVIORS_WITHOUT_CONSUMER_CODE = 0
REQUIRED_SCHEMAS_WITHOUT_RUNTIME_PRODUCER = 0
NAMED_BUT_NONFUNCTIONAL_REQUIRED_IMPLEMENTATIONS = 0
NOTEBOOK_STAGES_WITHOUT_EXECUTABLE_IMPLEMENTATION = 0
PLANNED_RUN_CELLS_WITHOUT_EXECUTABLE_RESOLUTION = 0
DECLARED_GATES_WITHOUT_EXECUTABLE_VALIDATOR = 0
DECLARED_TESTS_WITHOUT_EXECUTABLE_TEST = 0
DECLARED_ARTIFACTS_WITHOUT_RUNTIME_GENERATOR = 0
DECLARED_HANDOFFS_WITHOUT_POPULATION_LOGIC = 0
P02_SCIENCE_DEFERRED_TO_PHASE_ANALYSIS = 0
P02_SCIENCE_DEFERRED_TO_LAYER0 = 0
P02_SCIENCE_DEFERRED_TO_EVIDENCE_MAP = 0
P02_SCIENCE_DEFERRED_TO_LAYER10 = 0
P02_LAYER2_INFORMATION_DEFERRED_TO_P03 = 0
P02_REQUIRED_SCIENCE_DEFERRED_TO_SECOND_NOTEBOOK = 0
FREEZE_CRITICAL_MANUAL_INTERVENTIONS_DURING_RUN = 0
MANDATORY_P02_WORK_MISCLASSIFIED_AS_CONDITIONAL = 0
MANDATORY_P02_SCOPE_DROPPED_FOR_RESOURCE_CONVENIENCE = 0
P02_FULL_EXECUTION_ABLATIONS_ONLY_FOUNDATION_READY = 0
A0_REQUIRED_BEHAVIORS_NOT_IMPLEMENTED = 0
A4_REQUIRED_BEHAVIORS_NOT_IMPLEMENTED = 0
FULLY_UNLOCKED_P02_EVALUATIONS_NOT_EXECUTABLE = 0
FULLY_UNLOCKED_P02_ABLATIONS_NOT_EXECUTABLE = 0
L2_MODULES_DOCUMENTATION_COMPLETE_BUT_FUNCTIONALLY_INCOMPLETE = 0
MANDATORY_P02_ARTIFACTS_NOT_GENERATABLE = 0
REQUIRED_P02_EVIDENCE_DROPPED_FOR_CONVENIENCE = 0
DOWNSTREAM_CONSUMERS_REQUIRING_MISSING_P02_INFORMATION = 0
REQUIRED_P02_BRANCHES_WITHOUT_TERMINAL_FAILURE_BEHAVIOR = 0
EXPENSIVE_COMPLETED_P02_WORK_WITHOUT_LAWFUL_RESUME_PATH = 0
PREDETERMINABLE_FATAL_DEFECTS_DISCOVERABLE_ONLY_AFTER_SCIENCE_START = 0
PREVIOUSLY_VALID_IMPLEMENTATION_REGRESSIONS = 0
AUDIT_PROMPT_SECTIONS_NOT_EXECUTED = 0
SPECIFIED_BUT_NOT_IMPLEMENTED = 0
IMPLEMENTED_BUT_NOT_ORCHESTRATED = 0
ORCHESTRATED_BUT_NOT_EVIDENCE_PRODUCING = 0
EVIDENCE_PRODUCED_BUT_NOT_DOWNSTREAM_TRACEABLE = 0
BROKEN_P02_END_TO_END_REQUIREMENT_CHAINS = 0
FREEZE_CRITICAL_SUPPORT_COMPONENTS_NOT_IMPLEMENTED = 0
RUN_ALL_REQUIRES_MID_EXECUTION_CODE_EDIT = 0
UNLAWFULLY_DEFERRED_P02_RESPONSIBILITIES = 0
```

Any nonzero item prohibits PASS unless proven not to belong to P02.

# 163. EXPANDED FINAL READINESS MATRIX

Add rows for postponed/partial/documentation-only/config-only/schema-only/named-only/stage-only/run-matrix-only/gate-only/test-only/artifact-only/handoff-only requirements, A0/A4 complete behaviors, fully unlocked evaluations/ablations, all deferral counts = 0, specified-but-not-implemented/orchestrated/evidence/downstream-traceability counts = 0, broken chains = 0, support components complete, Run All source edits = NO, maximum implementation completeness PASS/FAIL.

# 164. EXPANDED SUCCESS CONDITION

PASS means everything P02 is expected to perform/evaluate/generate/validate/preserve/expose/package/handoff is implemented to maximum governed degree before scientific execution, with maximum completeness/artifact production/evidence preservation/runnability/resilience and no unauthorized science.

# 165. EXPANDED SUCCESS CERTIFICATION

Append a certification that nothing required remains merely planned/foundation-ready/documentation-only/config-only/schema-only/stubbed/partial/manual/deferred, and that all P02-owned functionality is defined, implemented, orchestrated, validated, artifact-producing, failure-aware, resumable where required, downstream-traceable.

State all postponement/partial/deferment counts as zero; A0/A4 and all fully unlocked evaluations/ablations fully implemented; runtime artifacts and downstream evidence fully generatable.

# 166. FINAL NON-DEFERRAL COMMAND

Before PASS ask:
1. Is there anything P02 itself is supposed to do that the implementation expects someone/later document/phase/notebook/patch to implement or calculate?
2. Is there any required artifact/evaluation/ablation/metric/statistical/failure/figure/table/Protocol/Analysis/L0/EMap/L10/P03 item the notebook cannot generate when executed?
3. Did any repair regress previously correct behavior?

All three answers must be NO.

# 167. FINAL PRESERVATION RULE

No earlier source/module/capability/model/A0/A4/evaluation/metric/statistic/record/artifact/figure/table/stage/test/gate/failure/checkpoint/environment/resource/Kaggle-input/P01-regression/security/bundle/Protocol/Analysis/L0/EMap/L10/P03/traceability/simulation/post-package/zero-unresolved requirement may be omitted because of later additions.

# 168. MANDATORY STRETCH-VERSION EXECUTION STANDARD

The implementation/audit must target the **Stretch Version**: the most complete, mature, production-quality, research-grade implementation lawfully supported by the governed P02 design and P00/P01 inherited state.

When choosing between minimal vs complete governed implementation, barely sufficient vs robust engineering, immediate-cell satisfaction vs full reusable capability, choose the more complete/robust lawful option.

Use stronger validation, failure accounting, resumability, lineage, logging, artifact structure, reproducibility, diagnostics, negative-result preservation, downstream compatibility, tests, schema enforcement, runtime safeguards, manifest coverage, evidence preservation whenever this does not alter frozen science.

Do not reduce scope because simpler/shorter/demo/easy/later/reconstructable. Do not invent science/models/ablations/metrics/statistics/datasets/splits/P01 changes or steal downstream authority.

Required:

```text
P02_IMPLEMENTATION_PROFILE = STRETCH
QUALITY_REDUCTION_TO_AVOID_STRETCH_IMPLEMENTATION = 0
GOVERNED_P02_CAPABILITIES_IMPLEMENTED_ONLY_MINIMALLY_WHEN_FULL_IMPLEMENTATION_WAS_AVAILABLE = 0
LAWFUL_P02_FUNCTIONALITY_OMITTED_FOR_SIMPLICITY = 0
LAWFUL_P02_VALIDATION_OMITTED_FOR_SIMPLICITY = 0
LAWFUL_P02_ARTIFACTS_OMITTED_FOR_SIMPLICITY = 0
LAWFUL_P02_EVIDENCE_OMITTED_FOR_SIMPLICITY = 0
LAWFUL_P02_FAILURE_HANDLING_OMITTED_FOR_SIMPLICITY = 0
LAWFUL_P02_REPRODUCIBILITY_SUPPORT_OMITTED_FOR_SIMPLICITY = 0
```

Final profile must state STRETCH VERSION, full governed scope, maximum practical governed depth, no scientific/functionality/artifact/evaluation/ablation/validation/downstream-evidence reduction.

# 169. MANDATORY CODE-QUALITY, FUNCTIONAL-CORRECTNESS, AND PRODUCTION-ENGINEERING STANDARD

The P02 notebook/package must not only contain all required functionality; it must contain **high-quality, actually working, professionally engineered code**.

Presence in concept/structure is not enough. The implementation itself must be correct.

# 170. CODE MUST ACTUALLY WORK

Required functionality must actually execute correctly. Do not confuse code existence/import/test/stage completion with correct behavior.

For every freeze-critical path verify actual behavior through the strongest reasonable pre-execution test.

Required:

```text
REQUIRED_CODE_PATHS_EXISTING_BUT_NONFUNCTIONAL = 0
REQUIRED_CODE_PATHS_WITH_UNVERIFIED_BEHAVIOR = 0
```

# 171. PRODUCTION-QUALITY CODE STANDARD

Stretch implementation must be correct, deterministic where required, readable, modular, maintainable, testable, traceable, failure-aware, resource-aware, secure, Kaggle-portable, reproducible, well-structured, appropriately documented.

Do not accept poor-quality code merely because one synthetic example passes.

# 172. NO CARELESS OR NEGLECTED IMPLEMENTATION

Search for unfinished branches, ignored errors, dead production code, unused configs/schema fields, unreachable required branches, copy-paste divergence, duplicate scientific rules, debug logic/prints, hard-coded paths/magic constants, silent fallback, catch-all suppression, global mutable state, unbounded caches/output, unsafe writes, unchecked returns/artifacts/checkpoints, missing denominator/missingness, unseeded randomness, nondeterministic run generation, resource/file/process leaks, unclean temp files, orphaned checkpoints, stale manifests/checksums.

Required:

```text
ENGINEERING_NEGLECT_FINDINGS_UNRESOLVED = 0
```

# 173. NO SILENT FAILURE

No freeze-critical `except Exception: pass` or equivalent suppression/empty-output/default/success/drop behavior.

Every caught exception must be classified, safely logged, tied to affected identity, converted to correct terminal state, preserved in failure evidence where required.

Required:

```text
FREEZE_CRITICAL_ERRORS_SILENTLY_SUPPRESSED = 0
```

# 174. EXCEPTION-HANDLING QUALITY AUDIT

For each major exception path identify exception class, expected/unexpected, scientific consequence, stage/run/artifact, terminal status, logging, retry, resume, descendant invalidation.

Broad top-level capture may exist only with preserved traceback and proper classification.

# 175. NO MAGIC SCIENTIFIC CONSTANTS

Seeds, windows, sampling rate, bands, budgets, thresholds, epochs, learning rates, bootstrap count, confidence, tie-breakers, class order must come from governed config/authority rather than scattered literals.

Required:

```text
UNTRACKED_SCIENTIFIC_MAGIC_CONSTANTS = 0
```

# 176. SINGLE SOURCE OF SCIENTIFIC TRUTH

Class order, metric formulas, seed policy, budgets, A4 definitions, run IDs, failure taxonomy, record semantics, statistics, stage IDs must have one current source of truth or validated exact parity.

Required:

```text
CONFLICTING_DUPLICATE_SCIENTIFIC_DEFINITIONS = 0
```

# 177. CODE/CONFIG/SCHEMA CONSISTENCY

Every config field must be parsed/consumed/schema-permitted/tested/manifested where required. Detect unused configs, bypassed constants, unwritten schema fields, writer fields absent from schema, obsolete accepted fields.

Required:

```text
CODE_CONFIG_SCHEMA_DRIFT = 0
```

# 178. FUNCTION CONTRACT QUALITY

Important functions/classes need explicit inputs/types/shapes/units/class order/missingness/output/failure/side effects/determinism/resources.

Especially verify EEG tensor/channel/sample/batch/class/probability/logit conventions.

Required:

```text
FREEZE_CRITICAL_FUNCTION_CONTRACT_AMBIGUITIES = 0
```

# 179. SHAPE / DIMENSION AUDIT

Trace record/window → array → representation → batch → model input/output → score adapter → PredictionRecord for every branch, record expected shapes, test synthetically.

Required:

```text
UNVERIFIED_FREEZE_CRITICAL_SHAPE_TRANSITIONS = 0
```

# 180. DATA-TYPE AUDIT

Verify intended float32 scientific arrays, integer labels, stable strings/IDs, boolean validity flags, sufficient statistical precision; prevent object/stringified/float-label/unwanted float64/precision-loss drift.

Required:

```text
UNINTENDED_DTYPE_DRIFT = 0
```

# 181. NUMERICAL-STABILITY AUDIT

Handle division by zero, log(0), overflow/underflow, singular covariance, zero variance, invalid normalization, NaN/Inf, degenerate classes, empty matched sets, zero denominators with governed failure/fallback.

Required:

```text
UNHANDLED_NUMERICAL_STABILITY_FAILURES = 0
```

# 182. NaN / Inf CONTROL

Validate finite values at loaded windows, transforms, losses, model outputs, scores, metrics, aggregates, statistical inputs, figure/table sources.

Required:

```text
SILENT_NAN_INF_PROPAGATION = 0
```

# 183. DETERMINISM AUDIT

Verify reproducibility across Python random, NumPy, PyTorch, DataLoader workers, CUDA where possible, run ordering, file enumeration, order-sensitive data structures, parallel scheduling. Record honest limitations.

# 184. RANDOMNESS-OWNERSHIP AUDIT

Every scientific random source (`random`, NumPy RNG, torch RNG, DataLoader shuffle/sampler/augmentation) must derive from frozen seed lineage.

Required:

```text
UNREGISTERED_SCIENTIFIC_RANDOMNESS = 0
```

# 185. ALGORITHM CORRECTNESS AUDIT

Compare actual CSP/FBCSP/Riemannian/alignment/EEGNet/deep/ensemble/bootstrap/Wilcoxon/Friedman/Holm behavior to governing method specification.

Required:

```text
SELECTED_METHODS_WITH_IMPLEMENTATION_SEMANTIC_DRIFT = 0
```

# 186. METRIC-CODE CORRECTNESS

Independently validate metric implementation with hand-computable fixtures/library behavior, including labels, positive class, macro/micro, weights, participant aggregation, missing classes, AUC orientation, confusion ordering.

Required:

```text
METRIC_IMPLEMENTATION_DEFECTS_UNRESOLVED = 0
```

# 187. STATISTICAL-CODE CORRECTNESS

Independently verify pairing, participant matching, complete-case filters, bootstrap unit/count, BCa/fallback, Wilcoxon, Friedman, Holm; never treat windows as participant replicates.

Required:

```text
STATISTICAL_IMPLEMENTATION_DEFECTS_UNRESOLVED = 0
```

# 188. A0 CODE-PATH CORRECTNESS

Trace actual A0 run expansion → training → validation selection → checkpoint → raw inference → PredictionRecord → metric → participant aggregation → artifact. Verify no calibration/threshold/abstention/selective logic.

# 189. A4 CODE-PATH CORRECTNESS

Trace every A4 condition through executable functions: C0 core, C1 frozen long, C2 hard vote, C3 probability average only with valid native probabilities, C4 frozen model representative selection, C5 probability averaging over eligible representatives. Validate common support and parent identity in code.

# 190. VOTING IMPLEMENTATION AUDIT

Hard vote: prediction order, class order, ties, missing predictions, common support.
Probability average: same class order/instance, valid probabilities, normalization, missing member behavior.

Required:

```text
ENSEMBLE_AGGREGATION_IMPLEMENTATION_DEFECTS = 0
```

# 191. DATA-LOADER QUALITY AUDIT

Prevent full dataset RAM duplication, unbounded caching, incorrect shuffle, split mixing, shard omission, duplicate loading, nondeterministic file order, file-handle exhaustion. Stream/chunk where appropriate.

# 192. MEMORY-QUALITY AUDIT

Estimate worst-case memory for EEG batches, model/optimizer/gradients/checkpoints/predictions/aggregation/A4 views/ensembles; perform cleanup as needed.

Required:

```text
FORESEEABLE_MEMORY_EXHAUSTION_WITHOUT_GUARD = 0
```

# 193. GPU MEMORY AUDIT

Move only needed tensors, avoid retained graphs, detach stored predictions, use no_grad/inference, release temporaries, avoid storing all batch outputs on GPU, monitor VRAM where available.

# 194. PERFORMANCE WITHOUT SCIENTIFIC COMPROMISE

Use batching, streaming, vectorized metrics, immutable metadata reuse, run-cell checkpointing, efficient partitioning, no redundant preprocessing/hashing when safe. Never change science for speed.

Required:

```text
AVOIDABLE_MAJOR_PERFORMANCE_DEFECTS_UNRESOLVED = 0
```

# 195. NO ACCIDENTAL RECOMPUTATION

Avoid needless P01 validation/preprocessing/A4 materialization/feature fitting/model training/inference/metric recalculation when valid governed artifacts can be reused.

Required:

```text
UNNECESSARY_EXPENSIVE_RECOMPUTATION = 0
```

# 196. PARALLELISM SAFETY

Verify unique output ownership, no concurrent write collision, deterministic assignment, safe shutdown, exception propagation, seed isolation, GPU scheduling, locking/atomic behavior.

Required:

```text
RACE_CONDITIONS_IN_GOVERNED_OUTPUT_PATHS = 0
```

# 197. THREAD / PROCESS RESOURCE LEAK AUDIT

Repeated synthetic execution must not leave zombies, dangling processes/pools, open files, unreleased GPU workers.

Required:

```text
WORKER_RESOURCE_LEAKS = 0
```

# 198. FILE I/O QUALITY

Use explicit encoding/deterministic serialization, correct JSON/YAML/CSV/JSONL/binary/UTF-8/locale-independent behavior.

# 199. ATOMIC-PERSISTENCE QUALITY

Critical outputs should use temp → validate → flush → atomic move/rename where possible.

Required:

```text
CRITICAL_NONATOMIC_OUTPUT_WRITES = 0
```

# 200. RECORD-WRITER QUALITY

Prevent duplicate IDs, missing required fields, invalid foreign keys, partial records, schema-version ambiguity, undetected overwrite, cross-stage collisions; validate immediately after write.

# 201. MANIFEST QUALITY

Manifest must match bytes actually produced: no pre-mutation hash, stale size/hash, missing file, duplicate path, unregistered artifact, nonexistent registered artifact.

Required:

```text
MANIFEST_REALITY_MISMATCHES = 0
```

# 202. CHECKSUM IMPLEMENTATION QUALITY

Stream large files, SHA-256, avoid loading GB files to memory, report missing/malformed rows, detect duplicates, test failure intentionally.

# 203. PATH-RESOLUTION QUALITY

Use robust path utilities; avoid cwd accidents, string path concatenation, authoring absolute paths, implicit normalization.

# 204. SECURITY-CODE QUALITY

Do not print secrets, serialize full env dicts, log auth headers, blindly include secret-bearing exception objects, or package credentials. Scan final archives.

# 205. INPUT-VALIDATION QUALITY

Do not trust filename/extension/claimed manifest/directory existence alone. Validate identity, revision, schema, hash, size/cardinality where governed.

# 206. DATA-CORRUPTION DETECTION

Detect truncated HDF5, missing shard, unexpected shape/dtype, corrupt checkpoint, invalid JSON/partial JSONL, duplicate records, wrong checksum before science consumes them.

# 207. CODE REUSE WITHOUT HIDDEN COUPLING

Reused IHARQ utilities must be checked for P00/P01/old-directory/old-Python/old-revision assumptions.

Required:

```text
REUSED_COMPONENTS_WITH_UNVALIDATED_P02_ASSUMPTIONS = 0
```

# 208. NO BLIND COPY-PASTE FROM P01

For every reused P01 pattern verify phase/layer identity, input/output records, resources, run cells, checkpoint semantics, downstream consumers.

Required:

```text
P01_COPY_FORWARD_SEMANTIC_DEFECTS = 0
```

# 209. API QUALITY

Internal APIs should be explicit/testable with explicit config/input/run/artifact/logger/seed/stage context where appropriate, avoiding hidden globals.

# 210. GLOBAL-STATE AUDIT

Search mutable global state that could corrupt seed/class order/model/dataset/budget/stage/artifact root across run cells.

Required:

```text
UNSAFE_MUTABLE_GLOBAL_SCIENTIFIC_STATE = 0
```

# 211. FUNCTION-SIDE-EFFECT AUDIT

Important functions should not unexpectedly mutate inputs/global config/delete files/change seed/cwd/manifests unless documented.

# 212. DEAD-CODE AUDIT

Identify production code unreachable from notebook stages/CLI/tests/bundle; classify utility/history/obsolete and remove conflicting obsolete code safely.

Required:

```text
OBSOLETE_CODE_CAUSING_CURRENT_BEHAVIOR_AMBIGUITY = 0
```

# 213. DUPLICATE-IMPLEMENTATION AUDIT

Search duplicate metric/seed/class/A4/run-cell/record-ID/checksum implementations. Consolidate or enforce parity.

Required:

```text
DUPLICATE_IMPLEMENTATIONS_WITH_BEHAVIOR_DRIFT = 0
```

# 214. LOGGING QUALITY

Logs must be structured, bound to stage/run identity, timestamped, compact in notebook, complete on disk, secret-safe.

# 215. ERROR-MESSAGE QUALITY

Errors must state what/where/identity/why/retry legality/science produced/downstream blocks/full-log path, not vague exceptions only.

# 216. OBSERVABILITY AUDIT

Long components must show what is running/completed/failed/blocked/remaining, artifact paths, checkpoint existence.

Required:

```text
LONG_RUNNING_COMPONENTS_WITHOUT_OBSERVABILITY = 0
```

# 217. SCIENTIFIC STATUS MUST NOT BE INFERRED FROM PROCESS EXIT ALONE

Exit code 0 is insufficient; acceptance requires expected artifacts/cardinality/schema/gates/checksums/terminal ledger.

# 218. OUTPUT-CARDINALITY AUDIT

Verify expected cardinalities for run results, parent matches, PredictionRecords, budgets, checkpoints, gates. Unexpected cardinality is failure until explained.

# 219. IDENTITY UNIQUENESS AUDIT

Validate uniqueness of run cells, records, models, checkpoints, stages, artifacts, failures, external pointers.

Required:

```text
DUPLICATE_GOVERNED_IDENTITIES = 0
```

# 220. REFERENTIAL-INTEGRITY AUDIT

Validate foreign keys: Prediction→model/checkpoint/window, Metric→prediction/run, A4 comparison→parent/condition, Failure→run/stage, Handoff→artifact.

Required:

```text
BROKEN_RECORD_FOREIGN_KEYS = 0
```

# 221. SERIALIZATION ROUND-TRIP AUDIT

For important schemas test object → serialize → parse → validate → reconstruct with no semantic/type loss.

# 222. VERSIONING QUALITY

Every freeze-critical schema/config/artifact must be versioned and incompatible versions rejected.

Required:

```text
UNVERSIONED_FREEZE_CRITICAL_SERIALIZED_CONTRACTS = 0
```

# 223. BACKWARD-COMPATIBILITY QUALITY

Test intentional P00/P01-compatible readers; do not break valid predecessors or silently interpret old schema as current P02.

# 224. FAIL-CLOSED BEHAVIOR QUALITY

When identity/hash/class order/schema/checkpoint provenance/split/parent match/scientific config/required input cannot be established, stop safely rather than guess.

Required:

```text
FREEZE_CRITICAL_UNKNOWN_STATES_RESOLVED_BY_GUESSING = 0
```

# 225. FAIL-SOFT BEHAVIOR WHERE AUTHORIZED

Conditional/fallback/diagnostic failures must be recorded and lawful independent work may continue. Distinguish phase blocker, branch blocker, cell failure, diagnostic-only.

# 226. NO BROAD “CONTINUE ON ERROR”

No blanket continue-on-error without governed failure classification.

# 227. CODE REVIEW FOR SCIENTIFIC SEMANTIC BUGS

Audit label inversion, wrong axes/sampling dimension, train/validation/test mixups, subject grouping, budget membership, off-by-one windows, wrong vote/probability axis, omitted model.eval/no_grad, seed reset in batch loop, wrong checkpoint/A4 condition/denominator.

Required:

```text
KNOWN_SCIENTIFIC_SEMANTIC_BUG_CLASSES_UNCHECKED = 0
```

# 228. CODE REVIEW FOR PYTHON-SPECIFIC DEFECTS

Audit mutable defaults, late-binding closures, shadowed imports, accidental variable reuse, bare except, pathlib/string mixing, iterator exhaustion, chained assignment, dtype coercion, device mismatch, CPU/GPU comparisons, state_dict mismatch, nonserializable manifest objects.

# 229. PYTORCH-SPECIFIC QUALITY AUDIT

Verify train/eval, no_grad/inference, optimizer zeroing, loss reduction, device, state_dict, scheduler, early stopping, best checkpoint semantics, deterministic seeds, DataLoader worker seeds, no unintended gradient accumulation.

# 230. SCIKIT-LEARN PIPELINE AUDIT

Ensure train-fitted preprocessing (scaler/CSP/feature selection/calibration-like transforms) never fits on validation/test.

# 231. RIEMANNIAN PIPELINE AUDIT

Verify covariance/tangent/alignment methods and train-only reference fitting.

# 232. PRETRAINED MODEL ADAPTER QUALITY

Validate checkpoint load, architecture, channel map, sampling, input length, normalization, frozen/trainable parts, output semantics, version, license; no silent alteration of frozen P01/A4 science.

# 233. MODEL-OUTPUT VALIDATION

Synthetic inference must verify batch cardinality, class dimension, finite scores, probability ranges/sums where required, valid classes, class order.

# 234. CHECKPOINT-CORRUPTION TEST

Corrupt a fixture checkpoint and verify hash mismatch, reload block, no inference, failure record.

# 235. CONFIG-CORRUPTION TEST

Alter frozen config and verify semantic/config hash mismatch blocks inappropriate checkpoint reuse.

# 236. SOURCE-CODE-REVISION TEST

Alter synthetic source fingerprint and verify stale worker/checkpoint/run-cell reuse cannot continue where source identity matters.

# 237. ARTIFACT-CORRUPTION TEST

Corrupt fixture record/manifest and verify validation catches it before bundle acceptance.

# 238. END-TO-END TEST MUST ASSERT SEMANTICS

Synthetic E2E tests must assert expected IDs, shapes, record count, class order, metric, paths, manifest links, terminal states—not merely “no exception.”

# 239. COVERAGE QUALITY

Distinguish line, branch, requirement, failure-path coverage. Freeze-critical behavioral coverage matters more than raw line %.

# 240. CODE REVIEW INDEPENDENCE

At least one audit pass must distrust existing tests and independently derive expected behavior from authority/Build Book.

# 241. TEST-ORACLE INDEPENDENCE

Important expected values should come from hand computations, independent library behavior, or independent reference calculations—not the implementation itself.

# 242. NO TEST CHEATING

No test-mode bypass of required production behavior.

Required:

```text
TEST_ONLY_BYPASSES_OF_REQUIRED_PRODUCTION_BEHAVIOR = 0
```

# 243. NO SYNTHETIC/REAL PATH DIVERGENCE

Synthetic tests must exercise the same core production functions as real Kaggle execution.

Required:

```text
SYNTHETIC_TESTS_BYPASS_REAL_PRODUCTION_CODE_PATHS = 0
```

# 244. PROFESSIONAL CODE ORGANIZATION

Use coherent package hierarchy, avoid circular imports/giant unrelated utility files, keep scientific responsibilities separable/testable.

# 245. DOCUMENTATION ACCURACY

Docstrings/comments/README must describe current implementation; stale instructions removed/marked.

Required:

```text
DOCUMENTATION_IMPLEMENTATION_DRIFT = 0
```

# 246. CODE STYLE MUST SUPPORT CORRECTNESS

Repair poor style that increases defect risk—extreme functions, deep nesting, cryptic state, copy-pasted science, hidden mutation, ambiguous names—without risky cosmetic refactors.

# 247. LINT / STATIC QUALITY CHECKS

Where practical detect syntax errors, undefined names, unused critical imports, duplicate definitions, unreachable code, invalid types. Harmless style alone should not block release.

# 248. TYPE/INTERFACE QUALITY

Use type hints for important record/run/stage/model/artifact/config interfaces where they materially improve correctness.

# 249. DEPENDENCY MINIMALITY AND NECESSITY

Every added package needs a reason; avoid unnecessary large dependencies.

Required:

```text
UNJUSTIFIED_RUNTIME_DEPENDENCIES = 0
```

# 250. DEPENDENCY IMPORT LOCATION

Avoid loading large optional packages at boot when branches are conditional; use controlled imports while still preflighting before science.

# 251. VERSION-CONFLICT AUDIT

Test frozen dependencies can coexist. If environment limits resolver testing, distinguish version existence, local compatibility, and Kaggle Stage 01/05 verification. Do not claim compatibility without evidence.

# 252. KAGGLE PORTABILITY

Avoid systemd, privileged Docker, root-only mutation, GUI, interactive terminal prompts, persistent daemons unless lawfully handled.

# 253. NO INTERACTIVE FREEZE-CRITICAL QUESTIONS MID-RUN

No mid-run questions about model/seed/budget/A4/continue/checkpoint/metric.

Required:

```text
FREEZE_CRITICAL_INTERACTIVE_PROMPTS = 0
```

# 254. SAFE OPTIONAL USER INPUTS

Operational inputs like private credentials or already-frozen handles may be user-supplied but must be validated before science and may not change scientific design.

# 255. NO HIDDEN NETWORK DEPENDENCY

Inventory every network call as required/conditional/optional-publication/not-allowed.

Required:

```text
UNDECLARED_NETWORK_DEPENDENCIES = 0
```

# 256. OFFLINE / NETWORK-BLOCKED BEHAVIOR

Pre-attached required artifacts should not need network; conditional downloads must resolve through frozen terminal behavior if network is absent.

# 257. TIMEOUT QUALITY

Potentially unbounded external/subprocess operations should have reasonable timeout/watchdog where appropriate and heartbeat.

# 258. SUBPROCESS QUALITY

Capture stdout/stderr, check exit code, safely record command, never include secrets, timeout where appropriate, propagate failure.

# 259. SHELL-COMMAND SAFETY

Avoid unsafe shell interpolation; quote paths; do not build commands from untrusted external strings unnecessarily.

# 260. ARCHIVE QUALITY

ZIP must use stable relative paths, exclude caches/credentials/redundant upstream data/unsafe symlinks, preserve needed files.

# 261. PACKAGE SIZE QUALITY

Avoid duplicate P01 data/checkpoints/temp renders/__pycache__/unnecessary large fixtures while preserving required evidence.

# 262. OUTPUT RETRIEVAL QUALITY

At completion print structured artifact summary: artifact, role, path, size, SHA-256.

# 263. FINAL RUN SUMMARY QUALITY

Distinguish scientific vs engineering completion, mandatory/conditional cells, successes/failures/blocks/diagnostic, A0/A4, tests, gates, bundle, security, downstream readiness. Do not just print “Done.”

# 264. ASSERTION QUALITY

Use explicit validators/exceptions for runtime conditions; assertions only for true invariants where optimization disabling is not a concern.

# 265. USER-FACING ERROR QUALITY

User-actionable preflight failures must say what failed, expected identity/handle/hash, and exact action to fix—not merely FileNotFoundError.

# 266. INTERNAL ERROR QUALITY

Unexpected programming errors must retain traceback and stage/run identities while keeping visible output concise.

# 267. ZERO CODE-QUALITY DEFECT CONDITION

Before PASS require:

```text
REQUIRED_CODE_PATHS_EXISTING_BUT_NONFUNCTIONAL = 0
REQUIRED_CODE_PATHS_WITH_UNVERIFIED_BEHAVIOR = 0
ENGINEERING_NEGLECT_FINDINGS_UNRESOLVED = 0
FREEZE_CRITICAL_ERRORS_SILENTLY_SUPPRESSED = 0
UNTRACKED_SCIENTIFIC_MAGIC_CONSTANTS = 0
CONFLICTING_DUPLICATE_SCIENTIFIC_DEFINITIONS = 0
CODE_CONFIG_SCHEMA_DRIFT = 0
FREEZE_CRITICAL_FUNCTION_CONTRACT_AMBIGUITIES = 0
UNVERIFIED_FREEZE_CRITICAL_SHAPE_TRANSITIONS = 0
UNINTENDED_DTYPE_DRIFT = 0
UNHANDLED_NUMERICAL_STABILITY_FAILURES = 0
SILENT_NAN_INF_PROPAGATION = 0
UNREGISTERED_SCIENTIFIC_RANDOMNESS = 0
SELECTED_METHODS_WITH_IMPLEMENTATION_SEMANTIC_DRIFT = 0
METRIC_IMPLEMENTATION_DEFECTS_UNRESOLVED = 0
STATISTICAL_IMPLEMENTATION_DEFECTS_UNRESOLVED = 0
ENSEMBLE_AGGREGATION_IMPLEMENTATION_DEFECTS = 0
FORESEEABLE_MEMORY_EXHAUSTION_WITHOUT_GUARD = 0
AVOIDABLE_MAJOR_PERFORMANCE_DEFECTS_UNRESOLVED = 0
UNNECESSARY_EXPENSIVE_RECOMPUTATION = 0
RACE_CONDITIONS_IN_GOVERNED_OUTPUT_PATHS = 0
WORKER_RESOURCE_LEAKS = 0
CRITICAL_NONATOMIC_OUTPUT_WRITES = 0
MANIFEST_REALITY_MISMATCHES = 0
REUSED_COMPONENTS_WITH_UNVALIDATED_P02_ASSUMPTIONS = 0
P01_COPY_FORWARD_SEMANTIC_DEFECTS = 0
UNSAFE_MUTABLE_GLOBAL_SCIENTIFIC_STATE = 0
OBSOLETE_CODE_CAUSING_CURRENT_BEHAVIOR_AMBIGUITY = 0
DUPLICATE_IMPLEMENTATIONS_WITH_BEHAVIOR_DRIFT = 0
LONG_RUNNING_COMPONENTS_WITHOUT_OBSERVABILITY = 0
DUPLICATE_GOVERNED_IDENTITIES = 0
BROKEN_RECORD_FOREIGN_KEYS = 0
UNVERSIONED_FREEZE_CRITICAL_SERIALIZED_CONTRACTS = 0
FREEZE_CRITICAL_UNKNOWN_STATES_RESOLVED_BY_GUESSING = 0
KNOWN_SCIENTIFIC_SEMANTIC_BUG_CLASSES_UNCHECKED = 0
TEST_ONLY_BYPASSES_OF_REQUIRED_PRODUCTION_BEHAVIOR = 0
SYNTHETIC_TESTS_BYPASS_REAL_PRODUCTION_CODE_PATHS = 0
DOCUMENTATION_IMPLEMENTATION_DRIFT = 0
UNJUSTIFIED_RUNTIME_DEPENDENCIES = 0
FREEZE_CRITICAL_INTERACTIVE_PROMPTS = 0
UNDECLARED_NETWORK_DEPENDENCIES = 0
```

Any nonzero freeze-critical item prohibits PASS.

# 268. CODE-QUALITY READINESS MATRIX

Add final rows for production-code completeness, behavioral/algorithm/metric/statistical/A0/A4 correctness, shapes, dtypes, numerical stability, NaN/Inf, deterministic randomness, scientific constant governance, code/config/schema parity, record/manifest/foreign-key/identity/checkpoint correctness, corruption handling, revision protection, atomic persistence, parallel safety, process cleanup, memory/GPU/performance, observability, errors/exceptions, fail-closed/fail-soft, package organization, Kaggle portability, network declaration, output retrieval, production/test parity, documentation parity; all unresolved code/functional/scientific-semantic defects = 0; profile = STRETCH/PRODUCTION-QUALITY.

# 269. FUNCTIONAL CAPABILITY CERTIFICATION

The audit must answer whether code can actually perform every required capability, not merely represent it.

PASS requires all required L2 capabilities, P02 scientific paths, record writers, artifact producers, gate validators, tests, failure paths, handoff generators to be actually functional/executable/handled.

# 270. NO-NEGLECT CERTIFICATION

Ask whether any code received less attention because it was secondary/diagnostic/failure/artifact/downstream/inconvenient. If yes, repair.

Specifically inspect negative results, failure records, conditional/fallback/diagnostic branches, resource blocks, checkpoint reload, resume, manifests, security scans, table/figure exports, downstream handoffs, partial-failure bundles.

Required:

```text
P02_IMPLEMENTATION_AREAS_NEGLECTED_DUE_TO_SECONDARY_PRIORITY = 0
```

# 271. FINAL CODE-QUALITY ADVERSARIAL REVIEW

Perform an independent code-quality-only audit trying to make the notebook crash, hang, return wrong results, leak memory, reuse stale state, mix datasets, misorder classes, corrupt/duplicate/lose records/provenance, load wrong checkpoints, mishandle scores, produce stale manifests, fail resume/package, leak credentials. Repair and rerun the full suite.

# 272. FINAL ACTUAL-WORKING-CODE QUESTION

Immediately before PASS ask:

> If every declared Kaggle input is present and frozen runtime prerequisites are satisfied, is there any required P02 behavior still dependent on hope, an untested assumption, a stub, undocumented side effect, silent fallback, or code never exercised through representative synthetic/golden paths?

Required answer:

```text
NO
```

Otherwise do not PASS.

# 273. EXPANDED STRETCH CODE-QUALITY SUCCESS CERTIFICATION

Append:

```text
P02 CODE AND FUNCTIONAL IMPLEMENTATION QUALITY:

PASS — STRETCH-GRADE,
PRODUCTION-QUALITY,
FUNCTIONALLY COMPLETE,
BEHAVIORALLY VALIDATED,
SCIENTIFICALLY FAITHFUL,
FAILURE-AWARE,
RESOURCE-AWARE,
REPRODUCIBLE,
RESUMABLE,
SECURE,
PORTABLE,
AND KAGGLE-RUNNABLE.

required code paths nonfunctional: 0
required code paths behaviorally unverified: 0
scientific-semantic implementation defects: 0
metric implementation defects: 0
statistical implementation defects: 0
A0 implementation defects: 0
A4 implementation defects: 0
record/artifact production defects: 0
checkpoint/resume defects: 0
stage orchestration defects: 0
resource-safety defects: 0
dependency/import defects: 0
manifest/checksum defects: 0
failure-handling defects: 0
security defects: 0
downstream-handoff implementation defects: 0
engineering-neglect findings: 0
actual required capabilities functional: ALL

CODE QUALITY PROFILE:
STRETCH / PRODUCTION-QUALITY
```

# 274. FINAL PRESERVATION AND CUMULATIVE AUTHORITY RULE

Nothing in Sections 169–273 removes or replaces any earlier requirement.

The complete audit prompt in this file contains:

```text
Sections 1–118
+
Sections 119–167
+
Section 168
+
Sections 169–274
```

When apparent overlap exists, perform both checks where they inspect different dimensions:

```text
Does the module exist?
AND
Does it actually work?

Does the run cell exist?
AND
Can it resolve to executable code?

Does the artifact schema exist?
AND
Can production code generate it?

Does the test exist?
AND
Does it genuinely test the required behavior?

Does the stage exist?
AND
Can Run All execute it?

Does the handoff exist?
AND
Can it be populated from runtime evidence?
```

Governing principle:

> **No required functionality may pass solely because it is present in documentation or structure. It must be implemented correctly, work as intended, survive rigorous testing, produce governed outputs, handle governed failures, and integrate correctly with the entire P02 execution chain.**

Final target:

```text
STRETCH-VERSION
+
FULL GOVERNED SCOPE
+
MAXIMUM IMPLEMENTATION COMPLETENESS
+
MAXIMUM PRACTICAL CODE QUALITY
+
ACTUALLY WORKING FUNCTIONALITY
+
ZERO NEGLECTED P02 RESPONSIBILITIES
+
ZERO FREEZE-CRITICAL IMPLEMENTATION DEFECTS
+
READY FOR ACTUAL KAGGLE EXECUTION
```
