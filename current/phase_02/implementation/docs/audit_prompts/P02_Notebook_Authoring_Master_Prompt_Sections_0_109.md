# IHARQ PHASE 02 / LAYER 02

# MASTER PROMPT FOR COMPLETE KAGGLE NOTEBOOK IMPLEMENTATION, STATIC VALIDATION, EXECUTION-BUNDLE ENGINEERING, P01-FAILURE-PREVENTION, AND PRE-EXECUTION RELEASE

---

# 0. ROLE

Act as the **senior IHARQ Kaggle implementation architect, Phase 02 execution engineer, Layer 02 decoder-systems engineer, EEG/BCI machine-learning implementation lead, scientific-computing engineer, reproducibility architect, software-integration engineer, canonical-artifact engineer, experiment-orchestration engineer, ablation-execution engineer, validation and test lead, failure-recovery engineer, Kaggle runtime specialist, package/release engineer, security auditor, and independent pre-execution quality-control authority** for the IHARQ BenchGuard Stretch C project.

A complete, finalized, frozen:

> **IHARQ Phase 02 / Layer 02 Implementation Build Book R4**

already exists.

That Build Book is the controlling implementation specification for this task.

Your task now is **not to redesign Phase 02**.

Your task is to take the finalized Build Book and create the **complete single comprehensive Phase 02 Kaggle execution-and-analysis notebook and its required implementation/support package**, such that the notebook can subsequently be uploaded to Kaggle and executed from beginning to end without discovering that a required scientific, methodological, architectural, software, artifact, evaluation, ablation, validation, persistence, recovery, or downstream-handoff behavior was never implemented.

The principal notebook identity is:

```
IHARQ-P02-COMPLETE-EXECUTION-AND-ANALYSIS-R4

```

and the intended notebook filename is:

```
IHARQ_Phase_02_Complete_Execution_and_Analysis_R4.ipynb

```

The notebook must implement the finalized R4 Build Book **faithfully and completely**.

---

# 1. CRITICAL SCOPE BOUNDARY

This task is:

```
FROZEN BUILD BOOK
↓
NOTEBOOK + IMPLEMENTATION PACKAGE AUTHORING
↓
STATIC / SYNTHETIC / NON-SCIENTIFIC VALIDATION
↓
KAGGLE-READY PACKAGE

```

This task is **not**:

```
P02 SCIENTIFIC EXECUTION

```

Do **not**:

- train the actual P02 models on the complete governed P01 datasets;
- execute the 1,896 official A0/A4 scientific run cells against the real dataset;
- calculate actual P02 scientific metrics;
- claim that A0 or A4 has produced P02 results;
- populate the future Protocol with fabricated execution results;
- populate Phase Analysis with fabricated findings;
- create claims;
- perform Layer 0 review;
- create an Evidence Map result state;
- create Layer 10 result figures from nonexistent P02 results;
- claim P02 completion;
- claim any model performance.

You **may and must**, however, perform non-scientific authoring validation such as:

```
JSON/IPYNB structural validation
Python syntax/compile validation
import-graph validation
package-import validation
schema validation
configuration validation
run-matrix expansion validation
stage-dependency validation
golden-vector metric tests
synthetic-fixture tests
negative tests
mock bundle generation
checkpoint round-trip tests using tiny synthetic fixtures
secret scans
path-safety scans
checksum validation
notebook execution simulation with scientific stages stubbed

```

These tests must prove that the **implementation is ready to execute**, not simulate scientific evidence.

---

# 2. CONTROLLING INPUTS — INSPECT ALL OF THEM

Before writing notebook code, inspect the complete supplied project state.

At minimum use:

## 2.1 Current governance

```
IHARQ Document Stack Governance and Creation Guide V6.1

```

Use it for:

```
single-track workflow
one-notebook default
full-scope requirement
reuse-first behavior
Kaggle-centered execution
output-bundle requirements
evidence-insufficiency loopback
large-artifact pointer governance
phase sequencing

```

## 2.2 The seven governing authorities

Inspect all seven:

```
Master Architecture Specification

Canonical Artifact, Record, and Interface Registry

Execution and Evidence Plan

Experiment, Ablation, and Evaluation Protocol

Complete Phase Execution Playbook

Method Selection and Design Rationale Register

Detailed Design and Nuts-and-Bolts Specification

```

Use them according to authority ownership:

```
Architecture
→ official phase/layer/module ownership
→ A0–A13 ownership
→ cross-layer boundaries

Registry
→ canonical records
→ canonical interfaces
→ fields
→ identities
→ producers/consumers
→ lifecycle semantics

Execution and Evidence Plan
→ what P02 must produce
→ evidence sufficiency
→ negative-result obligations
→ downstream evidence obligations

Protocol
→ experiment fairness
→ run identities
→ comparison rules
→ denominator rules
→ metrics
→ statistical treatment
→ ablation semantics
→ exclusions
→ leakage rules

Playbook
→ operational ordering
→ stage behavior
→ failure/recovery/handoff procedure

Method Selection
→ which methods/models/controls are selected
→ which are conditional/fallback/diagnostic

Nuts-and-Bolts
→ how every selected method actually works
→ transformations
→ model construction
→ fitting
→ prediction
→ aggregation
→ validation
→ failure behavior

```

## 2.3 Final P02/L2 Implementation Build Book R4

Inspect the entire canonical Build Book and all machine-readable R4/R3-adopted implementation derivatives.

Treat:

```
IHARQ-P02-L2-INTEGRATED-BUILD-BOOK-R4

```

as the primary implementation authority.

Use, where supplied:

```
p02_l2_submodule_capability_matrix_R4.yaml

p02_model_portfolio.yaml

p02_planned_scientific_execution_freeze_R3.yaml

p02_run_matrix_R3.yaml

p02_full_ablation_execution_contract_R3.yaml

p02_full_ablation_planned_run_cells_R3.yaml
p02_full_ablation_planned_run_cells_R3.csv

p02_a4_representative_selection_R3.yaml

p02_metric_dictionary.yaml

p02_record_schema_freeze_R2.yaml

p02_output_contract.yaml

p02_gate_matrix_R3.yaml

p02_test_catalog_R3.yaml

p02_notebook_stage_plan_R4.yaml

p02_environment_lock.yaml

p02_responsibility_matrix.yaml

p02_ablation_ownership_matrix_R3.yaml

p02_ablation_traceability_R4.csv

p02_method_traceability_R4.csv

p02_evaluation_traceability_R4.csv

p02_artifact_traceability_R4.csv

p02_prompt_requirement_exhaustion_R4.csv

p02_phase3_handoff_contract.yaml

p02_machine_readable_alias_register_R4.json

```

If a compatibility alias exists, resolve it through the R4 alias/provenance register.

Do not allow an old R2/R3 filename to silently override the R4 current identity.

---

# 3. PRIOR GOVERNED PROJECT STATE — USE, DO NOT RECREATE

Inspect the complete cumulative project state through P01.

At minimum inspect:

```
cumulative P00+P01 repository ZIP

current project status

P01→P02 clean-input handoff

P01 final phase handoff

P01 implementation Build Book

final cumulative Protocol v1.0 through P01

cumulative Phase Analysis through P01

embedded/current Layer 0 state

cumulative Evidence Map through P01

cumulative Layer 10 through P01

```

These establish what P02 actually inherits.

Do not regenerate valid P01 artifacts.

---

# 4. PHASE-01 EXECUTED NOTEBOOK — MANDATORY IMPLEMENTATION-LESSONS AUDIT

Inspect the supplied:

```
Phase_01_Notebook(1).ipynb

```

Do not use it as a template by blindly copying cells.

Use it to reconstruct:

```
actual stage orchestration
worker architecture
environment setup
logging
heartbeats
resource monitoring
checkpointing
external-artifact handling
failure points
same-session recovery
accepted continuation paths
security handling
bundle construction
download/export handling

```

Distinguish:

```
source code
FAILED execution
repair cell
superseded attempt
accepted continuation
final accepted execution

```

Do not assume that a cell was successful because the source code looks correct.

Inspect the final P01 execution bundle as the primary evidence of accepted P01 behavior.

---

# 5. MANDATORY P01 FAILURE-PREVENTION LEDGER

Before implementing P02, create an internal:

```
P02_FROM_P01_FAILURE_PREVENTION_LEDGER

```

For every material P01 failure or repair, record:

```
P01 repair/failure identity
affected stage
root cause
failure class
scientific change? yes/no
implementation consequence for P02
preventative test
preventative preflight
runtime guard
checkpoint/recovery implication
artifact implication
security implication

```

At minimum incorporate the following material lessons.

---

## 5.1 Stale revision / Stage-07 guard problem

P01 encountered a Stage-07 guard that expected an older bootstrap revision even though the live notebook was already on a later accepted revision.

Prevent this in P02.

Requirements:

```
one canonical DISPLAY_REVISION / NOTEBOOK_REVISION

worker revision fingerprint

runtime-source SHA-256

configuration SHA-256

stage-plan SHA-256

scientific-freeze SHA-256

```

Every worker must report these during boot.

Every stage submission must verify:

```
notebook revision
worker revision
runtime-source revision
configuration identity
scientific-freeze identity

```

before expensive work.

Do not hard-code stale predecessor revision names into stage-specific guards.

Create automated tests that would have caught the P01 Stage-07 mismatch before notebook delivery.

---

## 5.2 Imported worker code becoming stale after a runtime fix

P01 demonstrated that modifying runtime code while an isolated worker had already imported an older version can leave the worker executing stale logic.

P02 must make code-version behavior explicit.

If executable source changes:

```
old worker must not silently continue

```

Require:

```
source fingerprint at worker boot
source fingerprint in every stage result
worker/source mismatch => BLOCK before stage execution

```

If repair were ever needed during actual execution:

```
preserve scientific checkpoints
preserve valid artifacts
preserve logs
stop/restart only the necessary isolated worker where lawful
reconstruct only invalidated state
never restart the whole Kaggle kernel merely by default

```

Do not build a workflow that requires ad-hoc monkey-patching of already-imported scientific logic.

---

## 5.3 Stage-14 core-adoption / dependency-ID normalization problem

P01 encountered semantic-equivalence/adoption problems involving dependent canonical record identities.

P02 must not compare governed artifacts using naive raw-ID equality where the governing contract calls for semantic/dependency-normalized equivalence.

Where P02 consumes P01 records:

```
DatasetRecord
LabelMapRecord
SplitRecord
PreprocessingRecord
WindowRecord

```

verify them in dependency order.

Do not modify them.

Where semantic-equivalence checking is required, normalize only those exact upstream record-ID references that are already proven scientifically equivalent.

Never ignore arbitrary fields to make adoption pass.

Before any expensive P02 training:

```
P01 input manifest verified
P01 record lineage verified
P01 external pointer verified
P01 core data verified
P01 A4 data verified
dependency-normalized adoption verified

```

must all PASS.

---

## 5.4 A4 parent-event mismatch prevention

P01 encountered parent-event matching problems during A4 development.

P02 inherits the final frozen A4 R2 substrate and must not rederive it.

Before any A4 model/control execution, verify:

```
core parent-event census
A4 parent-event census
exact normalized parent identity
expected denominator
no missing expected parent
no unexpected parent
no duplicate parent

```

Frozen expected matched coverage:

```
12,910 / 12,910

```

where confirmed by supplied authority.

If mismatch exists:

```
FAIL_CLOSED

```

Do not:

```
drop unmatched parents silently
invent mappings
clip
pad
fabricate
change the A4 profile

```

---

## 5.5 A4 boundary feasibility lesson

P01 originally explored a longer representation that was not feasible for all valid parent events and ultimately froze the governed R2 profile.

P02 must consume only the frozen R2 representation.

Do not rediscover or revive the old infeasible profile.

Use exactly the governed A4 R2 identities.

Where applicable:

```
long profile:
+0.0 s → +3.5 s
560 samples @ 160 Hz

virtual multi-window members:
0:320
120:440
240:560

```

No:

```
padding
clipping
fabrication
silent event loss

```

is permitted.

---

## 5.6 Stage-15 duplicate scratch / unsafe retry lesson

P01 encountered duplicated scratch material after retrying persistence logic.

P02 must make all scratch/output writers idempotent.

Every generated record partition must have:

```
stable logical identity
attempt identity
expected cardinality
atomic write
completion marker
checksum

```

Before retry:

```
detect existing partial output
classify it
backup if necessary
clean only the invalid target
never append blindly

```

A rerun must never turn:

```
N rows

```

into:

```
2N rows

```

simply because the stage was submitted twice.

Create explicit duplicate-detection tests.

---

## 5.7 Remote artifact persistence must not force scientific recomputation

P01 exposed the danger of coupling expensive scientific computation to external publishing.

P02 must separate:

```
COMPUTE
→ VALIDATE
→ FREEZE LOCAL ARTIFACT
→ OPTIONAL/REQUIRED REMOTE COMMIT

```

If remote commit fails:

```
do not recompute the scientific result

```

Preserve the validated local artifact and retry only persistence.

Any large-output publication path must therefore be resumable independently of training/inference.

---

## 5.8 Kaggle artifact title/slug/API validation

P01 encountered Kaggle artifact mutation problems, including provider/API constraints.

If P02 needs to create or version a Kaggle Dataset or other remote artifact, validate **before expensive scientific execution**:

```
username
authentication availability
remote handle
slug
title length
provider constraints
create/version permission
current provider version
network availability

```

Use short provider-safe titles.

Do not discover a title-length or permission problem after hours of computation.

If remote mutation is not required by the frozen Build Book, do not introduce it unnecessarily.

---

## 5.9 Stage-18 missing-module/import/shim failures

P01 experienced:

```
ModuleNotFoundError
shim syntax error
worker import-path mismatch

```

during a late stage.

P02 must catch these before science begins.

Before Stage 06 or the first scientific stage:

```
python -m compileall
full import graph validation
clean subprocess import probe
clean isolated-worker import probe
all package modules imported
all CLI/stage entry points resolved
all relative/absolute package imports resolved

```

The package must contain every required module from the beginning.

Do not rely on dynamically creating malformed shim files halfway through the run.

If a compatibility shim is genuinely required, ship and test it before execution.

---

## 5.10 Environment-intent vs actual Kaggle environment lesson

P01 showed that the actual Kaggle runtime may differ from the original Build Book environment intent.

P02 must distinguish:

```
FROZEN ENVIRONMENT INTENT
vs
OBSERVED KAGGLE ENVIRONMENT

```

During the notebook preflight:

```
record Python
platform
CPU
RAM
GPU
VRAM
disk
package versions
CUDA/runtime
environment variables relevant to determinism

```

Verify the frozen package set.

If the exact environment cannot be satisfied:

```
BLOCK BEFORE SCIENCE

```

unless the Build Book explicitly defines a lawful compatibility behavior.

Do not silently substitute different scientific packages.

---

## 5.11 Adaptive-disk/resource-policy lesson

Do not hard-code unrealistic resource requirements copied from older phases.

Measure actual Kaggle resources.

Estimate:

```
input footprint
model/checkpoint footprint
temporary fit footprint
prediction-record footprint
figure/table source footprint
bundle footprint
safety margin

```

before expensive stages.

Create:

```
resource_preflight.json
resource_budget.json

```

If insufficient:

```
RESOURCE_BLOCKED

```

before scientific work.

Do not delete governed source artifacts to make space unless the Build Book explicitly permits it.

---

## 5.12 Heartbeats and notebook-output overload

Long scientific stages must produce:

```
persistent worker log
regular heartbeat
elapsed time
resource snapshot
current run-cell ID
current model/ablation identity
checkpoint information

```

Notebook-visible output should be compact.

Do not flood the notebook UI with enormous logs.

The complete log must remain on disk.

A visible heartbeat should reference the full log path.

---

## 5.13 Session-expiration / resumability lesson

P02 is materially more expensive than P01.

Assume the Kaggle session may expire.

Do not create a notebook that requires all expensive work to survive only in RAM.

Lawfully resumable scientific states must be checkpointed.

At minimum preserve:

```
completed stage ledger
completed run-cell ledger
model checkpoints
selected hyperparameter/config identity
PredictionRecord partitions
metric partitions
A0 partitions
A4 partitions
failure partitions
bundle manifest fragments

```

Every persisted piece must be bound to:

```
scientific freeze
config
source input
dataset
split
window
budget
model
seed
run-cell identity

```

A new-session continuation may reuse only artifacts whose hashes and dependency identities still match.

Never reuse stale checkpoints merely because filenames exist.

---

## 5.14 Stage dependency and invalidation

Implement an explicit stage dependency DAG.

If Stage X fails, determine exactly which descendants are invalidated.

Do not automatically rerun all prior stages.

Conversely, do not continue into descendants whose prerequisites have failed.

Every stage result must contain:

```
stage_id
status
attempt_id
inputs
input hashes
outputs
output hashes
dependencies
elapsed time
logs
blockers
observations

```

---

## 5.15 Stage-26 / R54 secret leakage lesson

This is mandatory.

Never serialize:

```
KAGGLE_API_TOKEN
API keys
OAuth tokens
passwords
cookies
private bearer tokens
secret environment values

```

into:

```
environment manifests
logs
notebook output
JSON
YAML
bundle
archives
exception messages

```

Secrets must be obtained through:

```
hidden input
Kaggle Secrets
environment secret provider

```

and retained in memory only where required.

The environment manifest should record only:

```
credential_required: true/false
credential_available: true/false
credential_source_type

```

not the credential value.

Before any export:

```
secret pattern scan
exact live-secret scan where a live secret exists
archive content scan
notebook output scan
environment-manifest scan

```

must PASS.

If contamination is found:

```
BLOCK EXPORT

```

then rebuild affected packaging surfaces without recomputing science.

Never print a detected secret value.

---

# 6. PRIMARY P02 SCIENTIFIC CONTRACT — DO NOT ALTER

The notebook must implement, not redesign, the finalized P02 contract.

The scientific design is:

```
R3 scientific freeze
ADOPTED UNCHANGED BY R4

```

Do not modify it for convenience.

---

# 7. TARGET PHASE / LAYER

```
Phase:
P02 — Baseline Decoders

Primary Layer:
L2 — Decoder and Baseline Measurement Spine

```

P02 must produce the governed raw decoder/prediction measurement substrate required by later reliability/calibration phases.

P02 must stop before downstream Layer-3 scientific responsibilities.

---

# 8. OFFICIAL LAYER-2 MODULE LOCK

Implement exactly these 8 official Layer-2 modules:

```
L2-M01 Baseline trainer

L2-M02 Prediction logger

L2-M03 Low-calibration curve builder

L2-M04 Subject difficulty profiler

L2-M05 Model-family registry

L2-M06 Ensemble comparison builder

L2-M07 Compact SSL adapter

L2-M08 Downstream readiness validator

```

Do not add a ninth official architecture module.

Internal helper components are allowed.

The R4 Build Book contains 53 required implementation capabilities across these eight modules.

Every one must map to:

```
source code
config
notebook stage
test
gate
artifact
downstream consumer

```

Required:

```
MISSING_OFFICIAL_L2_MODULES = 0

MISSING_REQUIRED_L2_SUBMODULES = 0

```

---

# 9. SOFTWARE ARCHITECTURE

Implement the real scientific package under the existing project namespace.

Use:

```
src/iharq/layer2_decoders/

```

with cohesive internal subpackages/modules for, at minimum:

```
config
identity
seeds

data
input_adapters
visibility
transforms

models
training
selection
checkpoints

registry
prediction
scores

metrics
statistics

low_label
subject_profiles

a0
a4
ensemble_controls

ablation_controller

records
schemas
writers

failures
negative_results

resources
environment
security

readiness
handoffs

bundle
validation
cli
stage_runner

```

Exact filenames may follow the current repository conventions, but there must be one coherent implementation.

Do not create a parallel competing Layer-2 codebase.

---

# 10. PHASE CONFIGURATION

Implement the frozen P02 successor configuration contract.

Do not reuse a P00-only PhaseConfig as if it already supported P02.

Implement the Build-Book-defined P02 phase configuration, including:

```
P02PhaseConfigV1

```

or the exact R4 schema identity.

Maintain backward compatibility with valid P00/P01 config parsing where required.

Require:

```
round-trip serialization
schema validation
semantic hash
unknown-field rejection where specified
phase discriminator
no silent P00→P02 coercion

```

Use:

```
configs/phase_02/

```

with governed config families including:

```
phase.yaml
data.yaml
split_visibility.yaml
budgets.yaml
seeds.yaml

models/
controls/

metrics.yaml
resources.yaml
outputs.yaml
gates.yaml

```

No hidden notebook-local scientific constants.

---

# 11. IMMUTABLE P01 INPUT CONTRACT

P02 must consume P01 outputs read-only.

Never modify:

```
DatasetRecord
LabelMapRecord
SplitRecord
PreprocessingRecord
WindowRecord
ValidationReport
P01 external artifact pointer
core windows
A4 R2 substrate

```

Expected inherited project facts include, where verified:

```
DatasetRecords:       3
WindowRecords:   12,910
SplitRecord:          1
PreprocessingRecord:  1
LabelMapRecords:      3
ValidationReport:     1

subject shards:     172

```

Core profile:

```
cue +0.5 s → +3.5 s
480 samples
160 Hz
one window per included event
reject out of bounds
no clipping

```

A4 R2 profile:

```
+0.0 s → +3.5 s
560 samples @160 Hz

virtual members:
0:320
120:440
240:560

matched parents:
12,910 / 12,910

```

Verify all hashes/pointers before use.

Do not relabel.

Do not resplit.

Do not rewindow.

Do not “repair” P01.

Do not regenerate the 1+ GB P01 datasets unnecessarily.

---

# 12. CLASS AND SCORE SEMANTICS

Class order must be explicit and frozen from authority.

Prediction evidence must preserve, where applicable:

```
predicted class
class order

native logits
native probabilities
native decision scores

score type
positive-class identity
score availability
missingness reason

```

Do not fabricate probabilities from a model that does not natively define the governed probability output unless the Build Book specifically defines the lawful transformation.

Do not allow P03 to reverse-engineer score semantics later.

---

# 13. MODEL PORTFOLIO — COMPLETE 16-BRANCH DISPOSITION

Implement the exact 16 branch identities and statuses from the Build Book.

At minimum the frozen portfolio includes:

```
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

Do not infer branch roles from names.

Read exact status/admission/search/score behavior from:

```
p02_model_portfolio.yaml

```

Preserve the final R4 disposition counts:

```
required/core:
7 / 7

conditional:
4 / 4

fallback:
1 / 1

diagnostic:
4 / 4

```

Conditional branches must resolve deterministically into governed terminal states such as:

```
ADMITTED
DEPENDENCY_BLOCKED
LICENSE_BLOCKED
CHECKPOINT_BLOCKED
CORPUS_OVERLAP_UNRESOLVED
INPUT_INCOMPATIBLE
RESOURCE_BLOCKED
DIAGNOSTIC_ONLY

```

A conditional model being unavailable must not invalidate mandatory A0 baseline coverage.

---

# 14. NO TEST-SET MODEL SELECTION

The final test set may never choose:

```
model
architecture
hyperparameters
checkpoint
seed
budget
ablation
ensemble
threshold
representation

```

All selection must occur through the frozen train/validation contract.

Test labels are evaluation-only.

Include explicit leakage tests that attempt to violate this rule and must fail.

---

# 15. FROZEN SEED / REPEAT POLICY

Use the exact R3 scientific freeze.

Master seed:

```
20260804

```

Derive subseeds deterministically from canonical run identity and purpose using the Build-Book-defined SHA-256 procedure.

Preserve the frozen repeat policy, including where applicable:

```
deterministic classical/Riemannian:
1

neural / sequence / eligible SSL:
5 model repeats

SAN-STRAT:
20

SAN-PERM:
100

P01 inherited budget subset:
1

```

Do not invent repeated budget subsets that never existed in P01.

Propagate:

```
SINGLE_FROZEN_SUBSET_LIMITATION

```

where required.

---

# 16. LOW-LABEL CONTRACT

Use the inherited exact budgets:

```
1
2
4
8
16
32

source events per class

```

P02 must consume the exact inherited P01 budget membership.

Do not:

```
regenerate
resample
redraw
replace

```

the budget subsets.

Apply low-label evaluation only to model branches explicitly marked eligible by the frozen portfolio.

Do not expand low-label evaluation to all 16 branches merely because it is programmatically easy.

---

# 17. SEARCH / TRAINING BOUNDS

Implement the exact frozen bounded search grids.

No open-ended search.

No “try more models until something performs well.”

For every branch define from the Build Book:

```
candidate ordering
max attempted candidates
max successful candidates
early stopping
resource cap
validation selection rule
checkpoint tie breaker
terminal failure behavior

```

Validation chooses.

Test evaluates.

---

# 18. STATISTICAL CONTRACT

Implement the frozen R3 statistical contract adopted by R4.

At minimum where applicable:

```
confidence level:
95%

participant-cluster bootstrap:
10,000 resamples

primary interval:
BCa

fallback if BCa undefined:
percentile

two-method paired confirmatory comparison:
Wilcoxon signed-rank

multi-method omnibus:
Friedman

post-hoc:
predeclared paired Wilcoxon

multiplicity:
Holm

minimum inferential support:
5 complete participant pairs/blocks

```

Participant, not individual windows, is the inferential unit where the authority specifies participant-level inference.

When inferential support is insufficient:

```
descriptive-only

```

Do not fabricate inferential certainty.

---

# 19. CANONICAL P02 RECORD IMPLEMENTATION

Implement the exact R4-frozen successor schemas.

Do not leave schema design for Kaggle execution time.

Required P02 record families include the Build-Book-frozen forms of:

```
PredictionRecord

ModelRegistryRecord

BaselineMetricRecord

LowCalibrationCurveRecord

SubjectProfileRecord

EnsembleControlRecord

FailureCaseIndex

Layer2ReadinessReport

NegativeResultNote

DiagnosticOnlyFlag

```

plus every other Registry-required canonical/support record in the frozen P02 output contract.

Preserve:

```
record identity
record type
schema version
phase
layer
config hash
source lineage
run-cell identity
dataset
subject/session/event/window
split role
budget
seed
model
checkpoint
class order
score semantics
limitations
lifecycle
terminal status

```

as applicable.

Unknown or invalid schemas must fail before result acceptance.

---

# 20. A0 — FULL EXECUTION REQUIRED

A0 is not merely “ready.”

A0 is:

```
FULL_EXECUTION_REQUIRED_IN_P02

```

Implement the complete A0 raw-decoder / accept-all reference.

A0 must not include Layer-3 calibration/selective behavior.

No:

```
calibration
confidence-threshold optimization
rejection
abstention
A1
A2
A3

```

may leak into A0.

The frozen planned A0 execution surface contains:

```
678 terminal scientific cells

```

The notebook must contain the deterministic run-cell expansion required to produce those cells when actually run on Kaggle.

Every A0 cell must have:

```
unique run-cell ID
dataset
model
budget
seed
repeat
configuration
split
fit scope
selection scope
evaluation scope
expected outputs
expected denominator
status
failure handling

```

No A0 cell may exist only in a document and be absent from notebook orchestration.

---

# 21. A4 — FULL EXECUTION REQUIRED

A4 is also:

```
FULL_EXECUTION_REQUIRED_IN_P02

```

Implement the exact ordinary-control experiment families:

```
A4-C0-CORE

A4-C1-LONG-3P5S

A4-C2-MULTI-HARD-VOTE

A4-C3-MULTI-PROB-AVG

A4-C4-MODEL-HARD-VOTE

A4-C5-MODEL-PROB-AVG

```

The frozen A4 surface contains:

```
1,218 terminal scientific slots

```

Every A4 slot must have deterministic identity and terminal evidence requirements.

Implement:

```
core vs long comparison
multi-window hard vote
multi-window probability averaging
ordinary model hard vote
ordinary model probability averaging

```

under the exact frozen representative-selection, score-availability, tie-breaking, common-support, matching, denominator, metric, statistical, and failure rules.

---

# 22. A4 REPRESENTATIVE SELECTION

Use the frozen validation-only representative selection contract.

Never select an ensemble member from final-test performance.

Never select “the best seed.”

The selected branch/family representative must be determined exactly from the Build Book's frozen validation procedure.

All accepted repeats belonging to the selected branch remain represented according to the contract.

---

# 23. CBraMod / A4 INPUT-COMPATIBILITY RULE

If a pretrained/model adapter requires an input length that is incompatible with the frozen A4 560-sample representation, do not silently:

```
pad
crop
clip
interpolate
change window identity
change model semantics

```

unless the Build Book explicitly authorizes the exact model-local transformation.

Otherwise terminal state:

```
INPUT_INCOMPATIBLE

```

Preserve this as evidence.

Do not make the notebook fail globally merely because a conditional external branch is incompatible.

---

# 24. DOWNSTREAM ABLATION OWNERSHIP

Preserve exact A0–A13 ownership.

Current direct P02 completion:

```
A0
A4

```

Downstream:

```
A1
A2
A3
A5
A6
A7
A8
A9
A10
A11
A12
A13

```

according to their exact authority owners.

P02 may create the raw substrate later phases require.

P02 must not perform downstream confirmatory science early.

---

# 25. A14

A14 must remain:

```
ABSENT_PROHIBITED

```

There must be no:

```
A14 config
A14 selector
A14 run cell
A14 scientific result
A14 output record
A14 effectiveness claim

```

Any mention of A14 must be an explicit prohibition/absence statement.

---

# 26. FULLY-UNLOCKED ADDITIONAL P02 ABLATION CONTROLLER

Preserve the Build Book's Stage:

```
18U

```

An additional ablation may enter P02 only if, **before result-dependent selection**, valid authority changes its P02 state to:

```
FULL_EXECUTION_REQUIRED_IN_P02

```

and all required implementation components are already frozen.

Technical computability alone is not sufficient.

Before admission require:

```
authority ownership
scientific authorization
complete method
complete config
run cells
metrics
comparisons
statistics where required
matching
denominator
record schemas
tests
gates
artifact outputs
failure behavior
analysis inputs
resource/license/checkpoint clearance

```

If admitted:

```
execute in the SAME notebook

```

It is not a second execution mode.

If no extra ablation is lawfully unlocked, Stage 18U must record:

```
NO_ADDITIONAL_FULL_EXECUTION_ABLATION_UNLOCKED

```

and PASS without inventing work.

---

# 27. 1,896-CELL EXPANSION VALIDATION

Before notebook release, statically expand the frozen full-ablation run cells.

Verify:

```
A0 = 678

A4 = 1,218

total = 1,896

```

Require:

```
1,896 unique run-cell IDs
0 duplicate IDs
0 missing stage assignments
0 missing model/condition identities
0 missing seed identities
0 missing terminal requirements
0 missing analysis-output requirements

```

Do not execute the real scientific cells during authoring.

---

# 28. FAILURE / TERMINAL-STATUS TAXONOMY

Do not reduce all execution outcomes to PASS/FAIL.

Implement the frozen terminal taxonomy, including where applicable:

```
SUCCESS
FAILED
NONCONVERGENT
RESOURCE_BLOCKED
LICENSE_BLOCKED
CHECKPOINT_BLOCKED
CORPUS_OVERLAP_UNRESOLVED
INPUT_INCOMPATIBLE
CONDITIONAL_SKIP
INVALID
DIAGNOSTIC_ONLY

```

Every attempted cell receives exactly one terminal state.

Failures remain in denominators/accounting where the governing protocol requires.

---

# 29. NEGATIVE EVIDENCE

The runtime bundle must preserve:

```
failed model fits
nonconvergence
NaN/Inf
resource blocks
license blocks
checkpoint blocks
incompatibilities
missing native score
missing probability
checkpoint reload failure
unmatched comparisons
sparse budgets
insufficient participant evidence
negative/null results
diagnostic-only results

```

Do not hide them because a preferred model succeeds.

---

# 30. MODEL CHECKPOINT CONTRACT

Every accepted trained model branch must support:

```
train
→ save
→ SHA-256
→ clean reload
→ inference
→ equivalence validation

```

Checkpoint record must include, where applicable:

```
model ID
branch
run cell
dataset
budget
seed
config hash
source hash
environment identity
checkpoint SHA-256
checkpoint bytes
score semantics
reload result

```

A checkpoint that fails clean reload is not accepted.

---

# 31. COMPLETE TEST ARCHITECTURE

Implement the complete frozen P02 test catalog.

At minimum include:

```
unit tests
schema tests
configuration tests
integration tests
import tests
worker-import tests
lineage tests
leakage tests
class-order tests
score-semantic tests
metric tests
golden-vector tests
seed/reproducibility tests
budget tests
subject-profile tests
checkpoint round-trip tests
A0 tests
A4 tests
matched-comparison tests
conditional-admission tests
failure tests
resource tests
security tests
bundle tests
reproduction tests
stage-idempotency tests
stage-dependency tests
scratch-duplicate tests

```

Required:

```
FREEZE_CRITICAL_BEHAVIORS_WITHOUT_TEST_OR_VALIDATION = 0

```

---

# 32. NEGATIVE TESTING

Explicitly test invalid behavior.

At minimum:

```
wrong class order

train/test leakage

validation/test leakage

invalid record lineage

bad config hash

bad source hash

invalid checkpoint

checkpoint/source mismatch

incompatible channel mapping

missing native score

missing probability

A4 parent mismatch

duplicate source event

duplicate scratch rows

unsafe path

secret leakage

stale worker revision

stale checkpoint revision

invalid configuration

unsupported downstream ablation ownership

attempted A14 creation

```

Each must fail in the intended governed manner.

---

# 33. GOLDEN-VECTOR TESTS

Create small deterministic synthetic fixtures for:

```
BACC
F1
ACC
AUC where applicable
confusion matrix
hard voting
probability averaging
participant aggregation
matched difference
Holm correction
seed derivation
class ordering

```

Use hand-checkable expected values.

Do not use real P02 scientific data for authoring tests.

---

# 34. COMPLETE GATE MATRIX

Implement all 26 frozen gates from the R4/R3 gate matrix.

Every gate requires:

```
gate ID
owner
requirement
validator
evidence artifact
pass criterion
failure behavior
repair owner
dependent stages

```

No stage may self-declare PASS without the governed gate evidence.

Required:

```
MISSING_REQUIRED_P02_GATES = 0

```

---

# 35. EXACT NOTEBOOK STAGE PLAN

Use the exact:

```
p02_notebook_stage_plan_R4.yaml

```

as the controlling stage identity source.

Do not renumber stages from memory.

The final notebook contains the complete frozen stage plan:

```
26 governed stages

```

including Stage:

```
18U

```

for authority-unlocked additional full-execution ablations.

The complete stage flow must cover, at minimum:

```
project/authority intake

environment/resource/security preflight

immutable P01 input verification

R3 scientific-freeze verification

schema/config/import/synthetic smoke tests

data/pointer loading

sanity controls

classical baseline execution

Riemannian execution

compact neural execution

conditional deep/SSL admission and execution

checkpoint/model registry

PredictionRecord generation

A0 full execution

low-label curves

participant/session profiles

A4 full execution

18U dynamic full-ablation dispatcher

failure/negative evidence finalization

downstream readiness

figure/table source generation

Protocol/Analysis/L0/EvidenceMap/Layer10 handoffs

P03 compatibility/evidence sufficiency

final security/bundle/checksum/export

```

Every required:

```
module
model
run cell
ablation
control
metric
statistic
diagnostic
failure process
artifact
test
gate
handoff

```

must map to at least one governed stage.

Required:

```
REQUIRED_P02_BEHAVIORS_WITHOUT_KAGGLE_STAGE = 0

```

---

# 36. STAGE RUNNER ARCHITECTURE

Implement a robust stage runner.

Each stage must support:

```
deterministic stage ID
dependency check
attempt ID
timeout
heartbeat interval
persistent log
compact visible output
resource snapshots
output manifest
terminal status
blocker list

```

Recommended pattern:

```
run_stage(stage_id)

```

with explicit result objects.

Do not bury stage state only in notebook globals.

Persist the accepted stage ledger.

---

# 37. ISOLATED WORKER DESIGN

If using an isolated worker architecture, preserve the beneficial P01 behavior but correct its weaknesses.

Worker boot must verify:

```
worker PID
Python executable
sys.path
source root
source SHA-256
notebook revision
config SHA-256
scientific-freeze ID
package-import probe

```

The notebook kernel and worker may not silently disagree about code revisions.

Full worker logs must be persisted.

Worker restart must not delete scientifically valid checkpoints.

---

# 38. RESOURCE MONITORING

During long stages record:

```
elapsed seconds
CPU utilization
RAM
GPU utilization where available
VRAM
disk total
disk used
disk free
current run-cell ID
current branch/model
current dataset
checkpoint progress

```

Use stage-specific heartbeat intervals.

The scientific design must not change in response to temporary resource readings.

Only Build-Book-defined conditional/resource gates may classify optional branches as RESOURCE\_BLOCKED.

---

# 39. ENVIRONMENT BOOTSTRAP

The notebook must run from a clean Kaggle session.

The notebook itself must:

```
locate its supplied inputs
materialize/import required local source modules
install/verify pinned dependencies
verify exact versions
verify scientific imports
freeze observed environment

```

Authority-bearing logic should exist in importable modules.

The notebook may bootstrap those modules into `/kaggle/working`, but it must not depend on an undeclared local path from the authoring machine.

No `/mnt/data/...` path may appear in the delivered notebook/package.

---

# 40. COMPANION IMPLEMENTATION PACKAGE

In addition to the `.ipynb`, produce a clean notebook-authoring package:

```
IHARQ_P02_L2_Kaggle_Notebook_Implementation_Package_R1/

```

containing at minimum:

```
README.md

notebook/
    IHARQ_Phase_02_Complete_Execution_and_Analysis_R4.ipynb

src/
    iharq/
        layer2_decoders/
            ...

configs/
    phase_02/
        ...

contracts/
    ...

machine_readable/
    <required Build Book derivative copies/current aliases>

tests/
    ...

scripts/
    ...

validation/
    notebook_structure_validation.json
    notebook_stage_coverage.csv
    run_cell_coverage.csv
    module_capability_coverage.csv
    method_coverage.csv
    ablation_coverage.csv
    evaluation_coverage.csv
    artifact_coverage.csv
    gate_coverage.csv
    import_validation.json
    compile_validation.txt
    synthetic_test_results.txt
    negative_test_results.txt
    bundle_dry_run_validation.json
    secret_scan.json
    path_safety_scan.json
    final_authoring_validation.json

execution_bundle_schema/
    <empty templates/schemas only — no fabricated scientific results>

checksums.sha256

```

Exact paths may adapt to repository conventions, but functionality may not be omitted.

---

# 41. NOTEBOOK SELF-CONTAINMENT

The notebook must not require the user to manually paste source files into random cells after execution has begun.

All runtime code must be available through:

```
the notebook itself
and/or
the supplied implementation package as a declared Kaggle input

```

Every external dependency must be declared.

Every required project file must have a deterministic resolver.

If a required input is absent:

```
BLOCK IN PREFLIGHT

```

not halfway through training.

---

# 42. REQUIRED USER-SUPPLIED KAGGLE INPUTS

The notebook's opening documentation must clearly enumerate exactly which Kaggle Inputs must be attached before pressing Run All.

At minimum identify, as governed by the supplied project state:

```
cumulative P00+P01 project package or exact required subset

P01 core derived-window Dataset/pointer

P01 A4 R2 Dataset/pointer

P02 notebook implementation package if not completely embedded

any conditionally required pretrained checkpoint assets

```

For every external input state:

```
provider
handle/path
immutable revision
SHA-256
expected size/cardinality
access requirement
license
required/conditional status

```

Do not leave the user to discover missing attachments after Stage 06.

---

# 43. EXTERNAL POINTER RESOLUTION

Every external artifact must resolve through a structured pointer.

Verify:

```
provider
handle
revision
manifest SHA-256
file SHA-256 where applicable
size
schema
access
license

```

Never trust a filename alone.

---

# 44. CONDITIONAL PRETRAINED MODELS

For conditional external/SSL models, preflight:

```
package
checkpoint
exact revision
checksum
license
benchmark corpus overlap
channel compatibility
sampling compatibility
input length
GPU/VRAM

```

before training/inference.

No live scientific-stage download of an unknown mutable checkpoint.

If exact checkpoint provenance cannot be frozen:

```
CHECKPOINT_BLOCKED

```

or the exact frozen Build-Book terminal state.

---

# 45. A0/A4 MATCHED-COMPARISON FAIRNESS

Every matched comparison must preserve exact common support.

Record:

```
eligible baseline denominator
eligible alternative denominator
matched denominator
unmatched baseline cases
unmatched alternative cases
missing reason

```

No unmatched case may silently disappear.

A4 comparisons must use exact frozen parent-event keys.

---

# 46. METRIC IMPLEMENTATION

Implement the frozen metric dictionary exactly.

No notebook-local metric definitions.

Every metric record must contain:

```
metric ID
metric version
formula/implementation identity
dataset
participant aggregation rule
run cells
model
condition
budget
seed
denominator
value
validity
limitations

```

where applicable.

---

# 47. FIGURE-SOURCE DATA

The notebook must export source data now for every future governed figure that P02 Phase Analysis / Layer 10 may need.

At minimum where applicable:

```
model comparisons
low-label curves
participant distributions
session distributions
A0
A4
failure/terminal-state distributions
score availability
resource status

```

Required:

```
EXPECTED_FIGURES_WITHOUT_SOURCE_DATA = 0

```

Do not create final Layer-10 scientific interpretation here.

Create only governed source data and optional diagnostic previews.

---

# 48. TABLE-SOURCE DATA

Export source tables for every expected later result table.

Required:

```
EXPECTED_TABLES_WITHOUT_SOURCE_DATA = 0

```

Phase Analysis must not need to reconstruct a missing scientific table from raw logs.

---

# 49. NO LAYER-10 RECOMPUTATION

Layer 10 must later:

```
READ
VERIFY
RENDER
PACKAGE
EXPORT

```

not:

```
RETRAIN
RECOMPUTE P02 SCIENCE
RETUNE
RECLASSIFY
STRENGTHEN

```

Required:

```
LAYER10_REQUIRED_SCIENTIFIC_RECOMPUTATION = 0

```

---

# 50. PROTOCOL v1.0 HANDOFF

The runtime execution bundle must contain a complete Protocol handoff with the actual executed:

```
environment
models
methods
configs
seeds
budgets
run cells
A0
A4
additional lawfully unlocked ablations
metrics
statistics
comparisons
exclusions
failure cases
blocked branches
reruns
amendments
external artifacts
limitations

```

The notebook authoring package must define the schema now.

Do not populate execution values before execution.

---

# 51. PHASE ANALYSIS HANDOFF

For every expected P02 analysis, identify the exact runtime artifact that will support it.

Required:

```
P02_ANALYSIS_REQUIREMENTS_WITHOUT_PLANNED_EVIDENCE = 0

PHASE_ANALYSIS_REQUIRED_BUT_UNEXECUTED_EVALUATIONS = 0

```

The future Phase Analysis may interpret evidence.

It may not complete missing P02 science.

---

# 52. LAYER 0 HANDOFF

Prepare:

```
candidate finding identity
evidence identity
limitation identity
failure/negative evidence
evidence ceiling
claim-boundary metadata

```

Do not approve claims.

---

# 53. EVIDENCE MAP HANDOFF

Runtime evidence must have stable future mapping identities for:

```
run
model
checkpoint
prediction
metric
ablation
control
figure source
table source
failure
external artifact
reproduction asset

```

---

# 54. LAYER 10 SOURCE HANDOFF

Provide read-only source bundles.

No later Layer 10 scientific recomputation should be necessary.

---

# 55. P03 HANDOFF — FREEZE-CRITICAL

P03 must receive complete raw prediction substrate.

At minimum, where applicable:

```
PredictionRecords
probabilities
logits
decision scores
predicted classes
class order

model IDs
checkpoint IDs

dataset IDs
subject IDs
session IDs
event/window IDs

split role
budget
seed

A0/A4 identity
aggregation identity

failure/missingness
metric dictionary

```

Required:

```
P03_REQUIRED_PREDICTION_FIELDS_MISSING = 0

P03_REQUIRED_RAW_INFORMATION_MISSING = 0

P03_SCORE_SEMANTICS_GUESSWORK = 0

```

---

# 56. NO DOWNSTREAM RESPONSIBILITY THEFT

P02 must not begin producing downstream authority records such as, unless explicitly required merely as non-authoritative schema fixtures:

```
CalibrationRecord
UncertaintyRecord
SelectivePredictionRecord
ThresholdRegistryRecord
policy decisions
risk fusion
stress decisions
embodiment decisions

```

P02 produces substrate.

Later layers perform their own science.

---

# 57. EXECUTION BUNDLE — RUNTIME OUTPUT CONTRACT

When the authored notebook is eventually executed on Kaggle, it must create one organized runtime bundle:

```
IHARQ_P02_L2_Phase_Execution_Bundle_<RUN_ID>/

```

or the exact naming convention frozen by the R4 Build Book.

It must contain, where applicable:

```
README.md

authority_manifest.json
source_project_state_manifest.json
environment_manifest.json
notebook_manifest.json

config_snapshot/

inputs/

records/

checkpoints_or_external_pointers/

raw_outputs/

metrics/

diagnostics/

negative_and_failed_results/

figure_source_data/

table_source_data/

logs/

manifests/

analysis_inputs/

protocol_v1_handoff/

layer0_handoff/

evidence_map_handoff/

layer10_source_bundle/

p03_handoff/

gate_decision.json

phase_execution_handoff.yaml

checksums.sha256

```

Required:

```
MISSING_REQUIRED_EXECUTION_BUNDLE_OUTPUTS = 0

```

Distinct scientific outputs must remain independently retrievable.

Do not collapse the whole phase into one opaque JSON.

---

# 58. PARTIAL / BLOCKED EXECUTION BUNDLE

If actual future Kaggle execution blocks after producing lawful partial evidence, the notebook should still attempt a controlled failure-bundle export.

That bundle must clearly distinguish:

```
accepted evidence
partial evidence
failed evidence
invalid evidence
unexecuted descendants
current blockers

```

It must never mark a partial run as scientifically complete.

---

# 59. MANIFESTS

At runtime generate, at minimum:

```
authority manifest
source project state manifest
environment manifest
notebook manifest
config manifest
input manifest
run-cell manifest
checkpoint manifest
record manifest
artifact manifest
failure/negative manifest
external pointer manifest
bundle manifest

```

Every manifest must be versioned and checksummed.

---

# 60. CHECKSUMS

Use SHA-256.

The final execution bundle must include:

```
checksums.sha256

```

covering every governed bundle file except unavoidable self-cycles.

After package construction:

```
reopen archive
CRC check
safe-path check
checksum check
missing check
mismatch check
structured parse check

```

---

# 61. PATH SAFETY

Never package:

```
/mnt/data/...
temporary authoring paths
local workstation paths
Kaggle ephemeral absolute paths as portable identities

```

Runtime logs may record observed Kaggle runtime paths where operationally useful, but portable manifests must use governed relative paths/pointers.

Reject ZIP members containing:

```
..
absolute path
unsafe symlink behavior

```

---

# 62. DOWNLOAD / EXPORT USABILITY

The Phase-01 experience showed that notebook-generated `FileLink` URLs may be inconvenient or return 404 depending on Kaggle UI state.

Therefore the final P02 notebook must not rely solely on `FileLink`.

At runtime:

1. create final archives directly under:

```
/kaggle/working/

```

with short stable filenames;

2. print:

```
filename
absolute runtime path
size
SHA-256

```

3. provide `FileLink` only as a convenience;
4. clearly instruct the user that the authoritative artifact is also available from the Kaggle **Output / working files** surface after the run/save;
5. create one top-level download package containing the principal small/medium phase archives if appropriate;
6. do not require a remote upload merely to make the output retrievable.

Do not silently upload project data to Google Drive or another service.

External publishing must occur only if the Build Book explicitly requires it or the user supplies the needed authorization.

---

# 63. LARGE ARTIFACTS

Do not embed large numerical arrays into the cumulative small-file bundle.

For large outputs, follow Governance.

Use governed external persistence only where required.

Every large external artifact pointer must contain:

```
provider
repository/dataset
immutable revision
SHA-256
bytes
license
access
retrieval instructions

```

Scientific bundle must remain reproducible without pretending large bytes are inside the ZIP.

---

# 64. IDEMPOTENCY

Every non-scientific stage should be safely repeatable or explicitly guarded.

Every scientific stage should know:

```
whether output already exists
whether output is complete
whether dependencies match
whether reuse is lawful
whether rerun invalidates descendants

```

Never append blindly.

Never treat the existence of a file as proof that it is valid.

---

# 65. ATOMIC WRITES

Critical JSON/YAML/JSONL/CSV/manifests/checkpoints should use:

```
write temp
flush
fsync where appropriate
validate
atomic rename

```

or equivalent robust behavior.

Avoid leaving half-written files after interruption.

---

# 66. RECORD PARTITIONING

Large record families should be partitioned deterministically, e.g. by appropriate governed identities such as:

```
dataset
model
condition
budget
seed

```

Do not keep millions of records only in RAM until Stage 24.

---

# 67. EVIDENCE SUFFICIENCY

At the end of actual execution, determine whether evidence is sufficient.

Require:

```
required stages terminal
mandatory run cells terminal
required outputs exist
required records validate
A0 complete
A4 complete
lawfully unlocked additional full ablations complete
metrics complete
required statistical inputs/results complete
failure evidence preserved
figure/table sources complete
P03 substrate complete
tests pass
gates pass
manifests close
checksums close
security scan passes

```

If not:

```
EVIDENCE_INSUFFICIENT

```

and produce exact blocker/repair scope.

Do not proceed to later documentary stages as though P02 succeeded.

---

# 68. REPAIR / RERUN POLICY

Only the affected scope should be rerun.

For every future repair compute:

```
root cause
lawful owner
affected stage
affected run cells
affected artifacts
affected descendants
science changed? yes/no
config changed? yes/no
data changed? yes/no
rerun scope
checkpoint reuse legality

```

Never rerun an expensive completed A0/A4 cell merely because a later packaging step failed.

---

# 69. NO MULTIPLE SCIENTIFIC EXECUTION MODES

Do not create:

```
fast mode
light mode
core mode
debug science mode
reduced model mode
reduced ablation mode
optional A4 notebook
separate SSL notebook
separate ablation notebook

```

The notebook has one governed complete execution design.

Diagnostic/synthetic authoring tests are not alternative scientific modes.

---

# 70. NOTEBOOK ORGANIZATION

The notebook may be long.

That is acceptable.

Use:

```
clear Markdown sections
stage IDs
substage IDs
modular functions
configuration-driven loops
importable project modules
compact visible logs
persistent detailed logs
deterministic run-cell IDs
progress indicators
checkpoint state

```

Do not sacrifice completeness for notebook brevity.

---

# 71. NOTEBOOK DOCUMENTATION

The top of the notebook must explain:

```
phase identity
layer identity
Build Book identity
scientific-freeze identity
P01 input identities
A0/A4 responsibilities
A14 prohibition
one-notebook rule
required Kaggle inputs
expected GPU/resources
expected long-running stages
resume behavior
output locations
security behavior
what the notebook will and will not do

```

---

# 72. AUTHORING-TIME STATIC EXECUTION SIMULATION

Before delivery, simulate every stage with:

```
real function resolution
real config loading
real stage dependencies
synthetic/minimal fixture data
scientific-heavy calls stubbed or tiny-fixture bounded

```

Prove for every stage:

```
entry point exists
imports succeed
inputs are defined
outputs paths are defined
tests exist
gate exists
dependency exists
failure path exists
bundle path exists

```

Required:

```
UNIMPLEMENTED_STAGE_ENTRY_POINTS = 0

UNRESOLVED_IMPORTS = 0

UNDEFINED_STAGE_OUTPUTS = 0

REQUIRED_P02_BEHAVIORS_WITHOUT_KAGGLE_STAGE = 0

```

---

# 73. BUILD-BOOK REQUIREMENT EXHAUSTION

Map the full R4 Build Book to notebook implementation.

Create:

```
p02_buildbook_to_notebook_traceability.csv

```

with:

```
Build Book requirement
source authority
L2 module
capability
method/model
run cells
notebook stage
source file/function
config
test
gate
artifact
consumer
status

```

Required:

```
UNMAPPED_REQUIRED_P02_REQUIREMENTS = 0

```

---

# 74. METHOD TRACEABILITY

Create:

```
p02_notebook_method_traceability.csv

```

for every selected/conditional/fallback/diagnostic method.

Required:

```
UNMAPPED_SELECTED_METHODS = 0

SELECTED_METHODS_NOT_IMPLEMENTED = 0

```

---

# 75. EVALUATION TRACEABILITY

Map all 12 expected P02 evaluation families:

```
evaluation
→ run cells
→ notebook stage
→ raw evidence
→ metric/statistic
→ output
→ figure/table source
→ validation
→ Phase Analysis consumer

```

Required:

```
EXPECTED_EVALUATIONS_WITH_INCOMPLETE_EXECUTION_PLAN = 0

```

---

# 76. ABLATION TRACEABILITY

Map A0–A14 explicitly.

Required:

```
P02_FULL_ABLATIONS_WITH_INCOMPLETE_TRACEABILITY = 0

```

A0/A4 must map to actual executable stage logic.

A14 must map only to prohibition.

---

# 77. ARTIFACT TRACEABILITY

For every required output define:

```
artifact ID/type
producer
inputs
contents
schema
relative path
validator
lifecycle
gate
consumer

```

Required:

```
REQUIRED_ARTIFACTS_WITHOUT_PRODUCER = 0

REQUIRED_ARTIFACTS_WITHOUT_VALIDATOR = 0

EXPECTED_ARTIFACTS_NOT_PRODUCED_BY_DESIGN = 0

```

---

# 78. SOURCE UTILIZATION AUDIT

Confirm actual review/use of:

```
Governance V6.1
Architecture
Registry
Execution Plan
Protocol v0.1
Playbook
Method Selection
Nuts-and-Bolts
final R4 Build Book
machine-readable R4/R3 scientific freeze
cumulative Protocol v1.0
Phase Analysis through P01
Layer 0 through P01
Evidence Map through P01
Layer 10 through P01
P00 evidence
P01 execution bundle
Phase-01 notebook
P01→P02 handoff
cumulative project ZIP

```

Required:

```
MANDATORY_SOURCE_FAMILIES_NOT_REVIEWED = 0

```

---

# 79. INTER-AUTHORITY HARMONY

Before notebook release verify:

```
Architecture
↔ Registry
↔ Execution Plan
↔ Protocol
↔ Playbook
↔ Method Selection
↔ Nuts-and-Bolts
↔ Build Book
↔ notebook implementation

```

Final:

```
INTER_AUTHORITY_HARMONY = PASS

```

---

# 80. PRIOR-STATE HARMONY

Verify:

```
notebook
↔ R4 Build Book
↔ Protocol v1.0 through P01
↔ Phase Analysis
↔ Layer 0
↔ Evidence Map
↔ Layer 10
↔ P01 execution evidence
↔ P01→P02 handoff

```

Final:

```
PRIOR_STATE_HARMONY = PASS

```

---

# 81. CROSS-PHASE HARMONY

Preserve:

```
P00
engineering foundation
↓
P01
governed data/split/preprocessing/window substrate
↓
P02
decoder and prediction measurement spine
↓
P03
reliability/calibration consumer

```

Final:

```
P00_P01_P02_HARMONY = PASS

```

---

# 82. CROSS-LAYER HARMONY

Final:

```
L1 responsibilities remain L1

L2 responsibilities remain L2

L3+ responsibilities remain downstream

L1_L2_L3_BOUNDARY_HARMONY = PASS

```

---

# 83. NO RESULT-DEPENDENT DESIGN

The authored notebook must not contain logic such as:

```
if test BACC > X:
    add another model

if A4 looks promising:
    run another ablation

if test score improves:
    pick this checkpoint

```

All design must be fixed from the Build Book before real results are observed.

---

# 84. NO QUALITY REDUCTION

Do not reduce work because:

```
notebook is long
models are expensive
A4 is large
1,896 cells are inconvenient
tests are numerous
artifact export is complicated

```

Scientific and governance scope controls.

---

# 85. NO UNJUSTIFIED COMPLEXITY

Also do not create complexity for its own sake.

Avoid:

```
duplicate packages
duplicate official modules
duplicate schemas
duplicate notebooks
duplicate P01 datasets
unnecessary cloud persistence
multiple competing run matrices
multiple current config authorities

```

Reuse-first.

---

# 86. NOTEBOOK AUTHORING VALIDATION — PASS 1

Perform a complete Build Book → code audit.

Ask:

```
Does every Build Book requirement exist in source/config/stage/tests?

```

Repair genuine defects.

---

# 87. PASS 2 — INDEPENDENT REVIEW

Re-review the authored notebook/package from scratch.

Do not merely confirm that Pass-1 corrections exist.

Ask whether the full expected P02 state can truly run.

---

# 88. PASS 3 — OMISSION-FOCUSED REVIEW

Ask:

```
What will Kaggle need that is undefined?

Which import could fail late?

Which package could be missing?

Which input could be missing?

Which run cell has no stage?

Which stage has no gate?

Which gate has no evidence?

Which model has no terminal failure path?

Which A0/A4 condition has no implementation?

Which evaluation has no source data?

Which Phase Analysis result would lack evidence?

Which P03 field could be absent?

Which record schema could be underspecified?

Which large artifact might force an unnecessary recomputation?

Which retry could duplicate data?

Which stage could erase checkpoints?

Which secret could leak?

Which final package could be difficult to retrieve?

```

Repair every genuine defect.

---

# 89. PASS 4 — ADVERSARIAL KAGGLE REVIEW

Act as a Kaggle engineer trying to break the notebook.

Test:

```
clean kernel
missing input
read-only /kaggle/input
limited disk
no GPU
GPU available
package resolution failure
checkpoint unavailable
no network
session interruption
stage retry
worker restart
partial scratch
corrupt checkpoint
corrupt pointer
secret unavailable
remote publish denied
archive export

```

Do not change science to make these tests pass.

The notebook must fail early and clearly where a mandatory condition is absent.

---

# 90. PASS 5 — EEG/BCI SCIENTIFIC REVIEW

Verify:

```
no leakage
correct grouped split use
train-fitted transforms
test isolation
correct class order
participant-level inference
proper repeated-run handling
correct A0 behavior
correct A4 matching
no downstream calibration leakage
no A14

```

---

# 91. PASS 6 — PHASE ANALYSIS SIMULATION

Pretend P02 has completed.

Can Phase Analysis answer every expected P02 question from emitted artifacts alone?

If no:

```
repair notebook design

```

Do not instruct Phase Analysis to recompute missing science.

---

# 92. PASS 7 — LAYER 10 SIMULATION

Pretend Layer 10 receives the P02 outputs.

Can it:

```
read
verify
render
package

```

without scientific recomputation?

Required:

```
LAYER10_SCIENTIFIC_RECOMPUTATION_REQUIRED = 0

```

---

# 93. PASS 8 — P03 SIMULATION

Pretend P03 receives the P02 handoff.

Can it consume:

```
native scores
probabilities/logits where available
class order
predictions
lineage
model/checkpoint IDs
failure/missingness

```

without reverse engineering?

Required:

```
P03_REQUIRED_RAW_INFORMATION_MISSING = 0

P03_REQUIRED_PREDICTION_FIELDS_MISSING = 0

P03_SCORE_SEMANTICS_GUESSWORK = 0

```

---

# 94. PASS 9 — P01-FAILURE REGRESSION REVIEW

Explicitly prove that the authored P02 notebook cannot reproduce, through the same root cause, the major P01 defects:

```
stale revision guard
stale imported worker
dependency-ID adoption mismatch
A4 parent mismatch
unsafe retry duplication
publish failure causing recomputation
late missing import
malformed runtime shim
worker sys.path mismatch
unrealistic resource preflight
late provider/title/API discovery
secret serialization
bundle export contamination
download-only-through-FileLink

```

For each create:

```
P01 failure
P02 prevention
test
stage/preflight
status

```

All must PASS.

---

# 95. PASS 10 — SECURITY

Scan the complete authored package.

Require:

```
SECRETS = 0

unsafe paths = 0

live credentials serialized = 0

unresolved placeholders = 0

```

Do not expose any discovered secret.

---

# 96. PASS 11 — STRUCTURED DATA

Parse every:

```
JSON
JSONL fixture
YAML
CSV
IPYNB

```

Require:

```
structured_parse_failures = 0

```

---

# 97. PASS 12 — PYTHON VALIDATION

Require:

```
compileall PASS

clean subprocess import PASS

worker import probe PASS

test suite PASS

```

Do not suppress import errors.

---

# 98. PASS 13 — NOTEBOOK JSON VALIDATION

Validate:

```
nbformat
cell structure
metadata
unique cell/stage IDs where used
no malformed outputs
no embedded authoring-machine paths
no accidental executed P02 scientific outputs

```

The delivered notebook should normally be clean/unexecuted with regard to P02 scientific cells.

It may contain only intentional authoring-validation metadata, not fake P02 results.

---

# 99. PASS 14 — BUNDLE DRY RUN

Using synthetic/minimal fixtures, run the bundle generator.

Validate:

```
directory structure
manifests
checksums
relative paths
structured parse
secret scan
archive CRC
safe paths
handoff schema

```

Do not insert fake scientific evidence into the final execution-bundle template.

Synthetic test bundles must be clearly labeled:

```
FIXTURE
NON_SCIENTIFIC
NOT_P02_EVIDENCE

```

and must not be confused with a future real execution bundle.

---

# 100. AUTHORING PACKAGE CHECKSUMS

Create:

```
checksums.sha256

```

for the notebook-authoring package.

Reopen the ZIP and independently verify every row.

---

# 101. FINAL DELIVERABLE PACKAGE

Produce:

```
IHARQ_P02_L2_Kaggle_Notebook_Implementation_Package_R1.zip

```

containing the complete implementation.

Also provide the primary notebook separately:

```
IHARQ_Phase_02_Complete_Execution_and_Analysis_R4.ipynb

```

And provide a detached:

```
IHARQ_P02_L2_Kaggle_Notebook_Implementation_Package_R1.zip.sha256

```

---

# 102. DO NOT PRECREATE FAKE EXECUTION RESULTS

The authoring package may include:

```
schemas
templates
empty directories
fixtures
golden vectors
mock manifests
synthetic bundle examples

```

but anything synthetic must be unmistakably tagged as:

```
FIXTURE

```

Do not ship fabricated files that look like real:

```
PredictionRecords
BaselineMetricRecords
A0 results
A4 results
Phase Analysis inputs
Layer 0 findings
Evidence Map findings
Layer 10 results

```

---

# 103. FINAL NOTEBOOK READINESS MATRIX

Before delivery produce a final matrix with at least:

```
Governance                           PASS/FAIL
Seven authorities                    PASS/FAIL
R4 Build Book                        PASS/FAIL
P01 state                            PASS/FAIL
P01 notebook lessons                 PASS/FAIL
P01 execution bundle                 PASS/FAIL

Official L2 modules                  8/8
Required L2 capabilities             53/53

Model branches                       16/16
Required/core                        7/7
Conditional                          4/4
Fallback                             1/1
Diagnostic                           4/4

Canonical P02 record families        12/12
Required artifact/support families   26/26

A0 ownership                         FULL_EXECUTION_REQUIRED_IN_P02
A0 planned cells                     678/678 implemented in orchestration

A4 ownership                         FULL_EXECUTION_REQUIRED_IN_P02
A4 planned slots                     1218/1218 implemented in orchestration

Total full-ablation cells            1896/1896

A1-A3                                downstream
A5-A13                               downstream
A14                                  ABSENT

Expected evaluation families         12/12

Run matrix                           PASS/FAIL
Seeds                                PASS/FAIL
Budgets                              PASS/FAIL
Metrics                              PASS/FAIL
Statistics                           PASS/FAIL
Class order                          PASS/FAIL
Score semantics                      PASS/FAIL
Leakage                              PASS/FAIL
Checkpoint governance                PASS/FAIL

Environment setup                    PASS/FAIL
Resource preflight                   PASS/FAIL
External input resolution            PASS/FAIL
Recovery/resume design               PASS/FAIL
Idempotency                          PASS/FAIL
Atomic writes                        PASS/FAIL
Worker revision safety               PASS/FAIL

Tests                                PASS/FAIL
Negative tests                       PASS/FAIL
Golden-vector tests                  PASS/FAIL
Gates                                26/26
Notebook stages                      26/26

Execution bundle                     PASS/FAIL
Figure-source readiness              PASS/FAIL
Table-source readiness               PASS/FAIL

Protocol handoff                     PASS/FAIL
Phase Analysis handoff               PASS/FAIL
Layer 0 handoff                      PASS/FAIL
Evidence Map handoff                 PASS/FAIL
Layer 10 handoff                     PASS/FAIL
P03 handoff                          PASS/FAIL

Build Book traceability              PASS/FAIL
Method traceability                  PASS/FAIL
Evaluation traceability              PASS/FAIL
Ablation traceability                PASS/FAIL
Artifact traceability                PASS/FAIL

P01 failure-prevention regression    PASS/FAIL

Compile/import                       PASS/FAIL
IPYNB structure                      PASS/FAIL
Structured parse                     PASS/FAIL
Bundle dry run                       PASS/FAIL
Secret scan                          PASS/FAIL
Path safety                          PASS/FAIL
Checksums                            PASS/FAIL

Scientific P02 execution performed   NO

Scientific results fabricated        NO

Freeze-critical implementation
decisions left unresolved            0

READY FOR KAGGLE EXECUTION           YES/NO

```

---

# 104. ZERO-UNRESOLVED AUTHORING CONDITION

Before declaring the notebook ready:

```
SCIENTIFIC_DECISIONS_LEFT_TO_NOTEBOOK_AUTHOR = 0

METHODOLOGICAL_DECISIONS_LEFT_TO_NOTEBOOK_AUTHOR = 0

MODEL_DECISIONS_LEFT_TO_NOTEBOOK_AUTHOR = 0

ABLATION_DECISIONS_LEFT_TO_NOTEBOOK_AUTHOR = 0

EVALUATION_DECISIONS_LEFT_TO_NOTEBOOK_AUTHOR = 0

METRIC_DECISIONS_LEFT_TO_NOTEBOOK_AUTHOR = 0

STATISTICAL_DECISIONS_LEFT_TO_NOTEBOOK_AUTHOR = 0

RECORD_SCHEMA_DECISIONS_LEFT_TO_NOTEBOOK_AUTHOR = 0

ARTIFACT_DECISIONS_LEFT_TO_NOTEBOOK_AUTHOR = 0

STAGE_DECISIONS_LEFT_TO_NOTEBOOK_AUTHOR = 0

P01_FAILURE_PREVENTION_ITEMS_UNRESOLVED = 0

FREEZE_CRITICAL_IMPLEMENTATION_PLACEHOLDERS = 0

SECRETS = 0

```

Runtime facts such as actual Kaggle GPU availability are not design decisions.

They must resolve through already-defined gates.

---

# 105. BLOCKED CONDITION

If the supplied frozen Build Book or project state contains a **genuine freeze-critical contradiction that cannot be resolved from authority**, do not invent an answer.

Report:

```
P02_KAGGLE_NOTEBOOK_AUTHORING:
BLOCKED

```

and for each blocker provide:

```
blocker_id
source authority
lawful owner
affected Build Book requirement
affected module
affected model
affected ablation
affected evaluation
affected stage
affected artifact
exact unresolved issue
why supplied authority cannot resolve it
minimum repair
Build Book revision required? YES/NO
P01 rerun required? YES/NO
notebook consequence
downstream consequence

```

Do not classify ordinary coding defects as owner blockers.

Fix coding defects yourself.

Do not classify runtime-conditional branch unavailability as an unresolved design decision when the Build Book already defines its fail-closed terminal status.

---

# 106. REPAIR POLICY DURING NOTEBOOK AUTHORING

If you discover an implementation defect:

```
identify
→ determine lawful source
→ repair minimum necessary implementation scope
→ synchronize dependent code/config/tests
→ rerun affected validation

```

Do not silently change the scientific Build Book.

If a genuine Build Book defect is discovered:

```
preserve current Build Book
→ identify exact defect
→ do not invent replacement science
→ report BLOCKED unless authority already provides the answer

```

---

# 107. REQUIRED FINAL RESPONSE

When the task is complete, provide:

1. the complete notebook:

```
IHARQ_Phase_02_Complete_Execution_and_Analysis_R4.ipynb

```

2. the complete notebook implementation package:

```
IHARQ_P02_L2_Kaggle_Notebook_Implementation_Package_R1.zip

```

3. detached SHA-256;
4. final authoring validation report;
5. P01 failure-prevention regression report;
6. Build-Book→Notebook traceability matrix;
7. a concise description of required Kaggle inputs;
8. a concise description of expected runtime outputs;
9. any genuine runtime prerequisites the user must configure before pressing Run All;
10. the final readiness decision.

Do not merely print notebook code into chat if files can be created.

Actually create the `.ipynb` and package.

---

# 108. REQUIRED SUCCESS CERTIFICATION

Issue PASS only if the authored notebook and package satisfy the complete frozen Build Book.

If successful, state exactly:

```
P02_KAGGLE_NOTEBOOK_AUTHORING:

PASS — COMPLETE,
BUILD-BOOK-EXHAUSTIVE,
P01-FAILURE-HARDENED,
ONE-NOTEBOOK-FULL-SCOPE,
ABLATION-COMPLETE-IN-IMPLEMENTATION,
EVALUATION-COMPLETE-IN-IMPLEMENTATION,
BUNDLE-COMPLETE-IN-DESIGN,
STATICALLY_VALIDATED,
SYNTHETICALLY_TESTED,
SECURITY-CHECKED,
AND READY FOR KAGGLE EXECUTION

```

Then state:

```
P02 scientific execution:
NOT YET STARTED

P02 notebook:
CREATED

P02 notebook implementation package:
CREATED

R4 Build Book coverage:
COMPLETE

official Layer-2 modules:
8 / 8

required Layer-2 capabilities:
53 / 53

model branches:
16 / 16

A0:
678 / 678 PLANNED CELLS IMPLEMENTED IN ORCHESTRATION

A4:
1,218 / 1,218 PLANNED SLOTS IMPLEMENTED IN ORCHESTRATION

total P02-owned full-ablation cells:
1,896 / 1,896 IMPLEMENTED IN ORCHESTRATION

A14:
ABSENT_PROHIBITED

expected P02 evaluations:
12 / 12 IMPLEMENTED IN ORCHESTRATION

required artifact/support families:
26 / 26

notebook stages:
26 / 26

single-notebook rule:
PASS

P01 failure-prevention safeguards:
PASS

compile/import validation:
PASS

synthetic/golden validation:
PASS

negative tests:
PASS

bundle dry run:
PASS

secret scan:
PASS

path-safety scan:
PASS

checksums:
PASS

scientific P02 results created:
NO

fabricated scientific evidence:
NO

freeze-critical implementation decisions unresolved:
0

NEXT GOVERNED ACTION:

UPLOAD / ATTACH THE DECLARED KAGGLE INPUTS
AND RUN THE COMPLETE PHASE 02 NOTEBOOK
ON KAGGLE

```

---

# 109. FINAL COMMAND

Now inspect the complete supplied IHARQ project state and the finalized Phase 02 / Layer 02 Implementation Build Book R4.

Inspect the supplied Phase-01 notebook and final execution evidence deeply enough to understand the actual implementation failures, repair history, continuation strategy, resource behavior, persistence issues, import issues, revision-guard problems, A4 problems, security incident, and final accepted package behavior.

Do not merely narrate those problems.

**Engineer them out of the P02 notebook before execution.**

Then create:

```
ONE COMPLETE
PHASE 02 / LAYER 02
KAGGLE EXECUTION-AND-ANALYSIS NOTEBOOK

```

plus its professional implementation/support package.

Implement the entire frozen Build Book without omitting:

```
modules
capabilities
methods
models
baselines
controls
A0
A4
fully unlocked P02 ablations
run cells
seeds
budgets
metrics
statistics
records
artifacts
negative results
failures
diagnostics
tests
gates
figures-source data
table-source data
Protocol handoff
Phase Analysis handoff
Layer 0 handoff
Evidence Map handoff
Layer 10 handoff
P03 handoff
reproducibility
security
recovery
bundle generation
checksums

```

Preserve the one-notebook full-scope rule.

Do not compromise quality.

Do not compromise functionality.

Do not compromise scientific scope.

Do not compromise ablation completeness.

Do not compromise evaluation completeness.

Do not compromise artifact coverage.

Do not compromise failure preservation.

Do not compromise downstream compatibility.

Do not recreate valid P01 data.

Do not introduce A14.

Do not let Layer 2 steal Layer 3+ science.

Do not leave a scientific decision for Kaggle runtime.

Do not create fake P02 results during authoring.

Do not allow a late import, revision, persistence, duplicate-scratch, resource, external-artifact, or secret-handling defect that could reasonably have been detected before expensive execution.

Before delivery:

```
DOUBLE-CHECK EVERYTHING

THEN RE-REVIEW IT INDEPENDENTLY

THEN PERFORM AN OMISSION-FOCUSED THIRD PASS

THEN ATTEMPT TO BREAK IT AS A KAGGLE ENGINEER

THEN SIMULATE PHASE ANALYSIS

THEN SIMULATE LAYER 10

THEN SIMULATE P03

THEN RUN STATIC/SYNTHETIC VALIDATION AGAIN

THEN PACKAGE

THEN REOPEN THE FINAL PACKAGE

THEN VERIFY ITS CHECKSUMS, STRUCTURE, SECURITY,
AND NOTEBOOK/PACKAGE CONSISTENCY

ONLY THEN DECLARE IT READY

```

The final notebook must be the **direct executable realization of the frozen P02/L2 Build Book**, not an approximation of it.