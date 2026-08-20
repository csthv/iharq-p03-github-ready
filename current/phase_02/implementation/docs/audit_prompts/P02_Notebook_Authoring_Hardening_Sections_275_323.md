# 275. MANDATORY PRESERVATION RULE FOR THIS ADDITION

This section and all following additions are **strictly cumulative**.

The entire previously written audit prompt remains binding in full:

```
Sections 0–118
+
Sections 119–167
+
Section 168
+
Sections 169–274
+
Sections 275 onward

```

Do not:

- delete any existing requirement;
- summarize previous sections away;
- replace an earlier requirement with a shorter formulation;
- treat an earlier check as redundant;
- remove any previously required module, capability, model, stage, artifact, evaluation, ablation, test, gate, failure rule, traceability matrix, downstream handoff, simulation, or zero-unresolved invariant;
- weaken any previously required Stretch-Version or production-quality standard.

The additions below strengthen the existing prompt specifically in response to two implementation defects discovered during pre-execution auditing.

They do not authorize any reduction in the rest of the audit.

---

# 276. TWO CURRENT KNOWN IMPLEMENTATION DEFECTS MUST BE TREATED AS REQUIRED REPAIR TARGETS

The current audit has identified two concrete implementation defects:

```
KNOWN_DEFECT_01:
INCOMPLETE 26-STAGE RUNTIME DISPATCHER / STAGE ORCHESTRATION

KNOWN_DEFECT_02:
INCOMPLETE A4 C4/C5 ENSEMBLE-VS-STRONGEST-CONSTITUENT
INFERENTIAL CLOSURE

```

These are **ordinary implementation defects**.

They are not:

```
scientific-owner blockers
method-selection blockers
authority ambiguities
reasons to revise P01
reasons to change P02 scientific design
reasons to weaken A0
reasons to weaken A4
reasons to defer work

```

The auditing model must therefore:

```
FIX THEM
→ INTEGRATE THEM
→ TEST THEM
→ REAUDIT THEM

```

rather than reporting them as unresolved owner decisions.

Required:

```
KNOWN_P02_IMPLEMENTATION_DEFECTS_UNREPAIRED = 0

```

PASS is prohibited until both are resolved.

---

# 277. COMPLETE 26-STAGE RUNTIME DISPATCHER IS A FREEZE-CRITICAL REQUIREMENT

The existence of:

```
stages.py

```

or equivalent runtime-dispatch source is not enough.

The complete governed Phase-02 stage dispatcher must actually orchestrate the real production implementation.

A stage system that merely contains:

```
headings
metadata
stage IDs
placeholder handlers
authoring-time stubs
synthetic-only behavior
generic no-op callbacks

```

does **not** satisfy the Build Book.

The final implementation must wire all governed Phase-02 behaviors into their correct runtime stages.

Required:

```
P02_RUNTIME_STAGES_EXPECTED = 26

P02_RUNTIME_STAGES_WITH_REAL_EXECUTABLE_DISPATCH = 26

P02_RUNTIME_STAGES_STUB_ONLY = 0

P02_RUNTIME_STAGES_METADATA_ONLY = 0

P02_RUNTIME_STAGES_WITHOUT_REAL_STAGE_HANDLER = 0

```

---

# 278. STAGE DISPATCH MUST RESOLVE TO REAL PRODUCTION FUNCTIONS

For every governed stage, trace:

```
stage identity
→ dispatcher
→ concrete stage handler
→ production implementation
→ configuration
→ inputs
→ run cells
→ outputs
→ tests
→ gates
→ terminal states
→ artifacts
→ downstream dependencies

```

The dispatcher may not merely call an abstract placeholder that is expected to be completed later.

Required:

```
STAGE_DISPATCH_TARGETS_WITHOUT_PRODUCTION_IMPLEMENTATION = 0

```

---

# 279. A0 MODEL-FAMILY STAGE WIRING MUST BE COMPLETE

The runtime dispatcher must connect the frozen A0 workload to the correct governed model-family execution stages.

It is not sufficient that:

```
A0 run cells exist

```

and:

```
model training functions exist

```

if the real notebook stage graph does not actually connect them.

The complete chain must be:

```
frozen A0 run-cell expansion
→ model-family routing
→ training/selection where required
→ checkpoint acceptance
→ prediction generation
→ raw score preservation
→ PredictionRecord generation
→ metric evidence
→ terminal-state evidence
→ A0 closure

```

Verify every frozen A0 cell resolves through that chain.

Required:

```
A0_RUN_CELLS_NOT_ROUTED_TO_REAL_MODEL_STAGE = 0

```

---

# 280. MODEL-FAMILY DISPATCH MUST BE EXPLICIT

The stage system must deterministically route relevant A0 cells through their correct implementation families.

This includes, according to the frozen model portfolio:

```
sanity/control families

classical decoder families

Riemannian families

compact neural families

conditional deep/sequence families

conditional SSL/pretrained families

diagnostic/fallback branches

```

Do not implement one generic dispatcher that silently treats fundamentally different branches identically where the Build Book specifies different admission/training/score/checkpoint behavior.

For each branch verify:

```
branch ID
→ model-family handler
→ admission rule
→ fit logic
→ validation rule
→ checkpoint logic
→ prediction adapter
→ score semantics
→ terminal-state behavior

```

Required:

```
MODEL_BRANCHES_WITH_UNRESOLVED_RUNTIME_ROUTING = 0

```

---

# 281. STAGE-15 A0 CLOSURE MUST BE REAL EXECUTABLE LOGIC

The audit must explicitly verify the real implementation of:

```
STAGE 15 — A0 FULL EXECUTION / CLOSURE / EVALUATION

```

or the exact current Stage-15 identity from the frozen stage plan.

Stage 15 must not merely:

```
mark A0 ready
summarize metadata
assert that earlier model stages ran
write an empty A0 report

```

It must perform the governed A0 closure over actual runtime outputs.

At minimum Stage 15 must verify and/or produce:

```
expected A0 planned-cell census

attempted-cell census

terminal-state census

accepted prediction evidence

PredictionRecord completeness

raw-score semantics

metric evidence

participant-level evidence

low-label evidence where applicable

failure and negative evidence

denominator accounting

model/checkpoint provenance

figure/table source material

A0 downstream analysis inputs

A0 Protocol handoff inputs

A0 Layer-0 evidence source

A0 Evidence-Map identities

A0 Layer-10 source artifacts

A0 P03 raw-prediction substrate

```

Required:

```
STAGE15_A0_CLOSURE_IMPLEMENTED = YES

STAGE15_A0_REQUIRED_CLOSURE_OUTPUTS_MISSING = 0

```

---

# 282. A0 MAY NOT BE CONSIDERED COMPLETE BASED ONLY ON UPSTREAM MODEL STAGES

The notebook may not reason:

```
models ran
therefore A0 is complete

```

A0 is complete only after explicit governed closure verifies:

```
coverage
denominators
terminal states
records
metrics
failures
evidence sources
downstream artifacts

```

Required:

```
A0_COMPLETION_WITHOUT_EXPLICIT_CLOSURE = 0

```

---

# 283. STAGE-18 A4 EXECUTION MUST BE REAL PRODUCTION ORCHESTRATION

The runtime dispatcher must implement the real:

```
STAGE 18 — A4 FULL EXECUTION

```

or exact frozen equivalent.

Stage 18 must orchestrate:

```
A4-C0-CORE

A4-C1-LONG-3P5S

A4-C2-MULTI-HARD-VOTE

A4-C3-MULTI-PROB-AVG

A4-C4-MODEL-HARD-VOTE

A4-C5-MODEL-PROB-AVG

```

using the frozen A4 R2 inputs and frozen representative-selection contract.

It may not merely call generic placeholders or produce metadata declaring the conditions executable.

Required:

```
STAGE18_A4_REAL_EXECUTION_IMPLEMENTED = YES

A4_CONDITIONS_WITHOUT_RUNTIME_HANDLER = 0

```

---

# 284. VALIDATION-SELECTED A4 REPRESENTATIVES MUST ACTUALLY FLOW INTO STAGE 18

The A4 representative-selection contract must not terminate in a YAML/CSV record without being consumed by the runtime dispatcher.

The implementation must perform:

```
validation evidence
→ representative-selection function
→ frozen representative identity
→ Stage-18 A4 runtime inputs
→ C4/C5 ensemble construction

```

Verify selected representative identities are bound to:

```
model branch

model ID

checkpoint ID

seed/repeat identity where applicable

dataset

condition

configuration hash

```

Required:

```
A4_SELECTED_REPRESENTATIVES_NOT_CONSUMED_BY_STAGE18 = 0

```

---

# 285. A4 C4/C5 FIXED-MODEL ENSEMBLES REQUIRE EXPLICIT INFERENTIAL CLOSURE

The current known defect specifically concerns:

```
A4-C4-MODEL-HARD-VOTE

A4-C5-MODEL-PROB-AVG

```

The implementation must not stop after generating ensemble predictions and metrics.

For each C4/C5 ensemble, the evidence layer must explicitly compare it against the:

```
PREDECLARED
VALIDATION-SELECTED
STRONGEST CONSTITUENT

```

according to the frozen A4 representative-selection and statistical contract.

Required:

```
A4_C4_VS_STRONGEST_CONSTITUENT_COMPARISON_IMPLEMENTED = YES

A4_C5_VS_STRONGEST_CONSTITUENT_COMPARISON_IMPLEMENTED = YES

```

---

# 286. “STRONGEST CONSTITUENT” MUST BE PREDECLARED THROUGH VALIDATION

The strongest constituent must not be selected using final-test A4 results.

The implementation must determine the comparator through the already frozen validation-only selection logic.

Forbidden:

```
choose strongest constituent from test BACC

choose constituent after observing C4/C5 test result

choose best seed from final test

choose comparator that makes ensemble look favorable

```

Required:

```
A4_STRONGEST_CONSTITUENT_TEST_SET_SELECTION = 0

```

---

# 287. C4 HARD-VOTE COMPARISON CONTRACT

For:

```
A4-C4-MODEL-HARD-VOTE

```

the runtime evidence must include a matched comparison against its predeclared strongest validation-selected constituent.

The implementation must produce:

```
ensemble identity

constituent identities

strongest constituent identity

validation-selection provenance

matched test population

ensemble predictions

strongest-constituent predictions

common-support denominator

unmatched cases

metric values

paired participant-level differences

effect-size source

uncertainty/statistical evidence

failure/missingness evidence

figure source

table source

Phase Analysis input

```

Required:

```
A4_C4_INFERENTIAL_CLOSURE_INCOMPLETE = 0

```

---

# 288. C5 PROBABILITY-AVERAGE COMPARISON CONTRACT

For:

```
A4-C5-MODEL-PROB-AVG

```

the runtime evidence must likewise compare against the predeclared strongest validation-selected constituent.

Before comparison verify:

```
all required ensemble members expose valid governed probabilities

class order matches

probability semantics match

common-support membership matches

no probability fabrication occurs

```

Then produce:

```
ensemble identity

constituent identities

strongest constituent identity

validation-selection provenance

matched population

ensemble probability outputs

ensemble predictions

strongest constituent outputs

common-support denominator

unmatched/missing cases

metrics

paired participant-level differences

effect-size source

uncertainty/statistical evidence

failure/missingness evidence

figure source

table source

Phase Analysis input

```

Required:

```
A4_C5_INFERENTIAL_CLOSURE_INCOMPLETE = 0

```

---

# 289. C4/C5 COMPARISONS MUST USE THE FROZEN PARTICIPANT-LEVEL STATISTICAL CONTRACT

The new C4/C5 comparison family must not introduce a new statistical rule.

Use the already frozen P02 participant-level statistical contract.

Where applicable:

```
participant is inferential unit

matched complete participants

95% confidence

10,000 participant-cluster bootstrap resamples

BCa

percentile fallback if BCa undefined

paired Wilcoxon signed-rank for two-method comparison

Holm correction where multiplicity applies

minimum inferential support = 5 complete participant pairs

```

If support is insufficient:

```
DESCRIPTIVE_ONLY

```

Do not fabricate inferential results.

Required:

```
A4_C4_C5_STATISTICS_NOT_USING_FROZEN_CONTRACT = 0

```

---

# 290. C4/C5 MATCHING MUST BE PARTICIPANT-ALIGNED AND COMMON-SUPPORT SAFE

The comparison must not compare ensemble and constituent results over different hidden populations.

For each dataset/comparison export:

```
eligible ensemble participants

eligible constituent participants

matched participant set

matched event/window support

excluded participants

exclusion reason

ensemble denominator

constituent denominator

matched denominator

```

Required:

```
A4_C4_C5_UNMATCHED_INFERENCE = 0

```

---

# 291. C4/C5 FAILURE AND MISSINGNESS MUST BE PRESERVED

If one ensemble member:

```
fails

is blocked

lacks probability output

has incompatible support

has missing checkpoint

produces invalid scores

```

the corresponding C4/C5 state must resolve through governed failure/missingness behavior.

Do not silently:

```
drop the model

replace the model

change ensemble membership

switch comparator

shrink denominator without accounting

```

Required:

```
A4_C4_C5_SILENT_ENSEMBLE_MEMBERSHIP_MUTATION = 0

```

---

# 292. C4/C5 COMPARISON ARTIFACTS MUST BE EXPLICITLY EXPORTED

For each applicable C4/C5 comparison, produce governed source artifacts sufficient for later analysis.

At minimum:

```
comparison identity

dataset identity

ensemble identity

strongest constituent identity

matched participant IDs or governed hashes/references

matched denominators

metric source values

paired difference source

statistical source/result

uncertainty source

failure/missingness source

figure-source row

table-source row

Protocol handoff reference

Phase Analysis reference

Layer-0 evidence source

Evidence-Map identity

Layer-10 source reference

```

Required:

```
A4_C4_C5_REQUIRED_ARTIFACTS_NOT_EXPORTABLE = 0

```

---

# 293. PHASE ANALYSIS MUST RECEIVE C4/C5 CLOSURE DIRECTLY

The future Phase Analysis must not calculate the missing ensemble-vs-constituent comparisons itself.

P02 Kaggle execution must already produce the evidence.

Required:

```
A4_C4_C5_COMPARISON_DEFERRED_TO_PHASE_ANALYSIS = 0

```

---

# 294. LAYER 10 MUST NOT RECOMPUTE C4/C5 COMPARISONS

Layer 10 must receive source data sufficient to render:

```
ensemble vs strongest constituent

```

without recomputing scientific metrics/statistics.

Required:

```
A4_C4_C5_LAYER10_SCIENTIFIC_RECOMPUTATION_REQUIRED = 0

```

---

# 295. STAGE 18U MUST BE FULLY EXECUTABLE

The known dispatcher defect also includes Stage:

```
18U

```

The final stage dispatcher must contain real logic for:

```
authority check

unlock-state evaluation

complete-contract verification

additional-ablation admission

run-cell loading/expansion

runtime execution

artifact generation

failure handling

evaluation closure

downstream evidence generation

```

If no additional P02 ablation has been lawfully unlocked, Stage 18U must still execute real validation logic and emit:

```
NO_ADDITIONAL_FULL_EXECUTION_ABLATION_UNLOCKED

```

with evidence proving the check occurred.

Required:

```
STAGE18U_IMPLEMENTED = YES

STAGE18U_STUB_ONLY = 0

```

---

# 296. FAILURE-EVIDENCE STAGE WIRING MUST BE COMPLETE

The dispatcher must include actual late-stage aggregation of:

```
failed run cells

blocked branches

nonconvergence

NaN/Inf

input incompatibility

checkpoint failure

resource block

license block

network/provider block where relevant

unmatched A4 cases

missing probabilities

diagnostic-only outcomes

negative/null outcomes

```

This must produce actual:

```
FailureCaseIndex

NegativeResultNote

DiagnosticOnlyFlag

```

or exact frozen equivalents.

Required:

```
FAILURE_EVIDENCE_AGGREGATION_STAGE_MISSING = 0

```

---

# 297. READINESS STAGE WIRING MUST BE COMPLETE

The downstream-readiness validator must operate on actual runtime evidence.

It must verify:

```
required PredictionRecords

score semantics

class order

records

metrics

A0 closure

A4 closure

C4/C5 inferential closure

failure evidence

figure/table sources

handoffs

P03 fields

bundle state

```

Do not allow a readiness report to return PASS based only on config/stage-plan completeness.

Required:

```
READINESS_VALIDATOR_ACCEPTS_METADATA_ONLY = 0

```

---

# 298. FIGURE-SOURCE GENERATION MUST BE ACTUALLY WIRED INTO RUNTIME

The real stage graph must produce figure-source artifacts.

At minimum include all expected P02 source families already required elsewhere in the prompt.

Specifically ensure A4 source data includes:

```
core vs long

multi-window vs core

C4 ensemble vs strongest constituent

C5 ensemble vs strongest constituent

```

Required:

```
FIGURE_SOURCE_STAGE_NOT_WIRED_TO_RUNTIME = 0

```

---

# 299. TABLE-SOURCE GENERATION MUST BE ACTUALLY WIRED INTO RUNTIME

Likewise table-source data must be generated by runtime code and not merely described.

Include C4/C5 comparison tables.

Required:

```
TABLE_SOURCE_STAGE_NOT_WIRED_TO_RUNTIME = 0

```

---

# 300. HANDOFF-EVIDENCE GENERATION MUST BE RUNTIME-WIRED

The actual dispatcher must populate:

```
Protocol handoff

Phase Analysis handoff

Layer 0 handoff

Evidence Map handoff

Layer 10 source handoff

P03 handoff

```

from actual accepted runtime records/artifacts.

No handoff may depend on manual later reconstruction.

Required:

```
HANDOFF_GENERATORS_NOT_WIRED_TO_RUNTIME = 0

```

---

# 301. FINAL RUNTIME BUNDLE GENERATION MUST BE PART OF THE STAGE GRAPH

The complete runtime dispatcher must culminate in actual bundle production.

The final bundle stage must gather:

```
records

metrics

checkpoints/pointers

failures

negative results

figures

tables

logs

manifests

handoffs

gate results

environment

config

run cells

checksums

```

and validate the resulting archive.

Required:

```
FINAL_RUNTIME_BUNDLE_STAGE_STUB_ONLY = 0

FINAL_RUNTIME_BUNDLE_GENERATION_NOT_IMPLEMENTED = 0

```

---

# 302. NO “LOWER-LEVEL FUNCTIONS EXIST, SO DISPATCH IS COMPLETE” ACCEPTANCE

The audit must explicitly reject this reasoning:

```
scientific functions exist
therefore the notebook is executable

```

Actual execution requires:

```
lower-level function
+
stage routing
+
dependency management
+
run-cell routing
+
gate enforcement
+
artifact generation
+
failure handling
+
bundle assembly

```

Required:

```
LOW_LEVEL_IMPLEMENTATION_NOT_CONNECTED_TO_RUNTIME = 0

```

---

# 303. NO “TOP-LEVEL DISPATCH EXISTS, SO SCIENCE IS COMPLETE” ACCEPTANCE

Likewise reject:

```
stage dispatcher exists
therefore the science is implemented

```

Every dispatch target must resolve to functional production code.

Required:

```
RUNTIME_DISPATCH_TARGETS_RESOLVING_TO_STUBS = 0

```

---

# 304. DISPATCHER INTEGRATION TEST

Create an authoring-time synthetic integration test covering the complete stage graph.

Using non-scientific fixtures:

```
Stage 00
→ ...
→ Stage 15 A0 closure
→ ...
→ Stage 18 A4 execution
→ Stage 18U
→ failure/readiness
→ figure/table sources
→ handoffs
→ final bundle

```

Heavy scientific functions may use tiny fixture datasets, but the **real production dispatch path** must be exercised.

The test must assert:

```
every stage handler invoked

every required dependency resolved

A0 closure invoked

A4 closure invoked

C4 comparison invoked

C5 comparison invoked

C4 strongest constituent comparison invoked

C5 strongest constituent comparison invoked

failure evidence generated

readiness evaluated

figure/table sources generated

handoffs populated

bundle generated

checksums validated

```

Required:

```
FULL_STAGE_GRAPH_SYNTHETIC_INTEGRATION_TEST = PASS

```

---

# 305. DISPATCHER STATIC TRACEABILITY MATRIX

Create:

```
P02_STAGE_RUNTIME_IMPLEMENTATION_TRACEABILITY.csv

```

containing, for all 26 stages:

```
stage_id

stage_name

dispatcher function

production handler

source file

inputs

dependencies

run-cell families

models/ablations

outputs

record families

tests

gates

failure states

downstream stages

status

```

Required:

```
STAGES_WITH_INCOMPLETE_RUNTIME_TRACEABILITY = 0

```

---

# 306. A4 COMPARISON TRACEABILITY MATRIX

Create:

```
P02_A4_COMPARISON_TRACEABILITY.csv

```

with at least:

```
A4 comparison family

reference condition

alternative condition

representative-selection rule

matching key

metric family

statistical family

source implementation

runtime stage

artifact outputs

Phase Analysis consumer

Layer 10 consumer

status

```

It must explicitly contain:

```
C1 vs C0

C2 vs C0

C3 vs C0

C4 vs strongest validation-selected constituent

C5 vs strongest validation-selected constituent

```

and any other frozen required A4 comparison.

Required:

```
A4_REQUIRED_COMPARISON_FAMILIES_UNMAPPED = 0

```

---

# 307. C4/C5 GOLDEN/SYNTHETIC TESTS

Create independent small tests for:

```
hard-vote ensemble

probability-average ensemble

strongest-constituent selection from validation

common-support construction

participant matching

paired difference calculation

participant-level statistical input formation

Holm adjustment where applicable

```

Use tiny hand-computable values.

Required:

```
A4_C4_C5_SYNTHETIC_TESTS = PASS

```

---

# 308. NEGATIVE C4/C5 TESTS

Test at least:

```
constituent missing

probability unavailable

class-order mismatch

unmatched participant

empty common support

too few participant pairs

checkpoint mismatch

test-set-based constituent selection attempt

```

Every invalid state must resolve correctly.

Required:

```
A4_C4_C5_NEGATIVE_TESTS = PASS

```

---

# 309. A4 STATISTICAL MULTIPLICITY ACCOUNTING

Verify whether C4/C5 comparison inclusion changes the frozen family of comparisons subject to multiplicity correction.

Do not invent a new correction rule.

Use the exact frozen statistical authority.

If C4/C5 belongs to an already declared comparison family:

```
include it in the frozen multiplicity procedure

```

If it is a separately predeclared family:

```
apply that exact frozen treatment

```

Document the mapping.

Required:

```
A4_C4_C5_MULTIPLICITY_TREATMENT_UNDEFINED = 0

```

---

# 310. C4/C5 RESULT-CARDINALITY AUDIT

For every dataset/eligible representative comparison, verify expected output cardinality.

Detect:

```
missing ensemble result

missing strongest-constituent result

missing matched pair

duplicate comparison row

duplicate statistical result

```

Required:

```
A4_C4_C5_RESULT_CARDINALITY_MISMATCH = 0

```

---

# 311. C4/C5 RECORD / ARTIFACT IDENTITY AUDIT

Every C4/C5 comparison must have stable governed identity connecting:

```
run-cell identity

ensemble identity

constituent identity

dataset

participant support

metric

statistical result

figure source

table source

```

Required:

```
A4_C4_C5_BROKEN_EVIDENCE_IDENTITIES = 0

```

---

# 312. C4/C5 FAILURE MUST NOT BLOCK UNRELATED A4 CONDITIONS

If C4 or C5 is unavailable because of a governed condition such as:

```
missing valid probability output

conditional model branch blocked

insufficient common support

```

preserve that failure.

Do not incorrectly erase valid:

```
C0
C1
C2
C3

```

evidence.

Dependency invalidation must be precise.

Required:

```
A4_UNRELATED_VALID_EVIDENCE_INVALIDATED_BY_C4_C5_FAILURE = 0

```

---

# 313. COMPLETE STAGE-TO-BUNDLE CHAIN AUDIT

For every major runtime result prove:

```
stage handler
→ record/artifact
→ manifest
→ bundle path
→ checksum
→ downstream reference

```

At minimum explicitly prove for:

```
A0

A4 C0

A4 C1

A4 C2

A4 C3

A4 C4

A4 C5

C4-vs-strongest comparison

C5-vs-strongest comparison

failures

readiness

figure sources

table sources

P03 handoff

```

Required:

```
STAGE_RESULTS_WITHOUT_BUNDLE_TRACE = 0

```

---

# 314. COMPLETE END-TO-END P02 RUNTIME ORCHESTRATION AUDIT

The final implementation must contain an unbroken runtime execution path:

```
preflight
↓
input verification
↓
scientific freeze verification
↓
schema/import tests
↓
model-family execution
↓
checkpointing
↓
prediction logging
↓
A0 execution
↓
A0 closure
↓
low-label evidence
↓
participant/session profiles
↓
A4 execution
↓
A4 inferential closure
↓
Stage 18U
↓
failure/negative evidence
↓
readiness
↓
figure/table source generation
↓
Protocol / Analysis / Layer0 / EvidenceMap / Layer10 / P03 handoffs
↓
evidence sufficiency
↓
security scan
↓
manifest/checksum closure
↓
runtime bundle

```

Required:

```
BROKEN_P02_RUNTIME_ORCHESTRATION_LINKS = 0

```

---

# 315. SPECIFIC KNOWN-DEFECT REGRESSION TEST

Create a dedicated:

```
P02_KNOWN_DEFECT_REGRESSION_AUDIT.json

```

containing:

```
DEFECT_01:
incomplete 26-stage dispatcher

expected repair:
full real stage dispatch

test:
full stage-graph synthetic integration

result:
PASS / FAIL


DEFECT_02:
missing C4/C5 ensemble-vs-strongest-constituent inferential closure

expected repair:
complete participant-level comparison + export

test:
C4/C5 comparison integration + golden + negative tests

result:
PASS / FAIL

```

Required:

```
KNOWN_DEFECT_REGRESSION_AUDIT = PASS

```

---

# 316. PASS MUST BE BASED ON THE REPAIRED PACKAGE, NOT THE PRE-REPAIR PACKAGE

After fixing these defects:

```
regenerate source package
regenerate notebook if dispatcher changes notebook behavior
regenerate tests
regenerate traceability
regenerate validation reports
regenerate README where needed
regenerate checksums
rebuild ZIP

```

Then rerun the **entire pre-existing Sections 0–274 audit**, not only these new checks.

Required:

```
POST_REPAIR_FULL_AUDIT = PASS

```

---

# 317. NO REGRESSION OF PREVIOUSLY VALID IMPLEMENTATION

The dispatcher/C4-C5 repairs must not break:

```
A0 678-cell implementation

A4 1,218-slot implementation

A4 C0/C1/C2/C3 comparisons

model branches

PredictionRecord generation

low-label logic

participant profiles

checkpointing

failure taxonomy

P01 input immutability

P03 handoff

Layer-10 source generation

resource handling

security

bundle export

```

Required:

```
REPAIR_INDUCED_REGRESSIONS = 0

```

---

# 318. EXPANDED STRICT ZERO-DEFECT INVARIANTS

In addition to **all previously required zero-unresolved invariants**, add:

```
KNOWN_P02_IMPLEMENTATION_DEFECTS_UNREPAIRED = 0

P02_RUNTIME_STAGES_STUB_ONLY = 0

P02_RUNTIME_STAGES_METADATA_ONLY = 0

P02_RUNTIME_STAGES_WITHOUT_REAL_STAGE_HANDLER = 0

STAGE_DISPATCH_TARGETS_WITHOUT_PRODUCTION_IMPLEMENTATION = 0

A0_RUN_CELLS_NOT_ROUTED_TO_REAL_MODEL_STAGE = 0

MODEL_BRANCHES_WITH_UNRESOLVED_RUNTIME_ROUTING = 0

STAGE15_A0_REQUIRED_CLOSURE_OUTPUTS_MISSING = 0

A0_COMPLETION_WITHOUT_EXPLICIT_CLOSURE = 0

A4_CONDITIONS_WITHOUT_RUNTIME_HANDLER = 0

A4_SELECTED_REPRESENTATIVES_NOT_CONSUMED_BY_STAGE18 = 0

A4_C4_INFERENTIAL_CLOSURE_INCOMPLETE = 0

A4_C5_INFERENTIAL_CLOSURE_INCOMPLETE = 0

A4_STRONGEST_CONSTITUENT_TEST_SET_SELECTION = 0

A4_C4_C5_STATISTICS_NOT_USING_FROZEN_CONTRACT = 0

A4_C4_C5_UNMATCHED_INFERENCE = 0

A4_C4_C5_SILENT_ENSEMBLE_MEMBERSHIP_MUTATION = 0

A4_C4_C5_REQUIRED_ARTIFACTS_NOT_EXPORTABLE = 0

A4_C4_C5_COMPARISON_DEFERRED_TO_PHASE_ANALYSIS = 0

A4_C4_C5_LAYER10_SCIENTIFIC_RECOMPUTATION_REQUIRED = 0

STAGE18U_STUB_ONLY = 0

FAILURE_EVIDENCE_AGGREGATION_STAGE_MISSING = 0

READINESS_VALIDATOR_ACCEPTS_METADATA_ONLY = 0

FIGURE_SOURCE_STAGE_NOT_WIRED_TO_RUNTIME = 0

TABLE_SOURCE_STAGE_NOT_WIRED_TO_RUNTIME = 0

HANDOFF_GENERATORS_NOT_WIRED_TO_RUNTIME = 0

FINAL_RUNTIME_BUNDLE_STAGE_STUB_ONLY = 0

FINAL_RUNTIME_BUNDLE_GENERATION_NOT_IMPLEMENTED = 0

LOW_LEVEL_IMPLEMENTATION_NOT_CONNECTED_TO_RUNTIME = 0

RUNTIME_DISPATCH_TARGETS_RESOLVING_TO_STUBS = 0

STAGES_WITH_INCOMPLETE_RUNTIME_TRACEABILITY = 0

A4_REQUIRED_COMPARISON_FAMILIES_UNMAPPED = 0

A4_C4_C5_MULTIPLICITY_TREATMENT_UNDEFINED = 0

A4_C4_C5_RESULT_CARDINALITY_MISMATCH = 0

A4_C4_C5_BROKEN_EVIDENCE_IDENTITIES = 0

A4_UNRELATED_VALID_EVIDENCE_INVALIDATED_BY_C4_C5_FAILURE = 0

STAGE_RESULTS_WITHOUT_BUNDLE_TRACE = 0

BROKEN_P02_RUNTIME_ORCHESTRATION_LINKS = 0

REPAIR_INDUCED_REGRESSIONS = 0

```

Any nonzero item prohibits PASS.

---

# 319. EXPANDED FINAL READINESS MATRIX

Add the following rows to the existing final readiness report:

```
26-stage real runtime dispatcher                 26 / 26

runtime stages remaining stub-only               0

runtime stages remaining metadata-only           0

A0 model-family runtime routing                   PASS

Stage-15 A0 closure                              PASS

A0 closure evidence completeness                 PASS

Stage-18 A4 runtime execution                    PASS

validation-selected A4 representative routing    PASS

A4 C0 vs C1 closure                              PASS

A4 C2 vs C0 closure                              PASS

A4 C3 vs C0 closure                              PASS

A4 C4 vs strongest constituent                   PASS

A4 C5 vs strongest constituent                   PASS

C4/C5 participant-level inference                PASS

C4/C5 frozen statistical contract                PASS

C4/C5 common support                             PASS

C4/C5 failure/missingness accounting             PASS

C4/C5 figure source export                       PASS

C4/C5 table source export                        PASS

C4/C5 Phase Analysis handoff                     PASS

C4/C5 Layer 10 source readiness                  PASS

Stage 18U implementation                         PASS

failure evidence runtime aggregation             PASS

readiness runtime aggregation                    PASS

figure-source runtime generation                 PASS

table-source runtime generation                  PASS

handoff runtime generation                       PASS

final runtime bundle generation                  PASS

full stage-graph synthetic integration           PASS

known-defect regression audit                    PASS

repair regression audit                          PASS

```

---

# 320. UPDATED MAXIMUM-COMPLETENESS INTERPRETATION

The existing Stretch-Version and maximum-completeness requirements remain unchanged.

Additionally:

> **A complete P02 implementation requires both the scientific lower-level functions and the complete production runtime orchestration that invokes those functions in the correct governed stages.**

And:

> **A complete A4 implementation requires not only producing C4/C5 ensemble outputs but completing the frozen scientific comparison of those ensembles against their predeclared strongest validation-selected constituent and exporting that inferential evidence for downstream use.**

Therefore:

```
LOWER-LEVEL SCIENTIFIC IMPLEMENTATION
WITHOUT STAGE ORCHESTRATION
=
INCOMPLETE

A4 ENSEMBLE PREDICTIONS
WITHOUT REQUIRED ENSEMBLE-VS-CONSTITUENT
INFERENTIAL CLOSURE
=
INCOMPLETE

```

---

# 321. UPDATED PRE-PASS QUESTIONS

Immediately before issuing PASS, ask:

### Question 1

> Does every one of the 26 governed stages resolve to actual production behavior rather than metadata, headings, or authoring stubs?

Required answer:

```
YES

```

### Question 2

> Are all 678 A0 cells actually routable through the production stage system and explicitly closed/evaluated through Stage 15?

Required answer:

```
YES

```

### Question 3

> Are all 1,218 A4 slots actually routable through Stage 18 and the complete A4 evidence path?

Required answer:

```
YES

```

### Question 4

> Are C4 and C5 explicitly compared against their predeclared validation-selected strongest constituent under the frozen participant-level statistical contract?

Required answer:

```
YES

```

### Question 5

> Are those C4/C5 comparisons exported into records/source tables/figure sources/Phase Analysis/Layer-10 evidence rather than deferred?

Required answer:

```
YES

```

### Question 6

> Does Stage 18U contain real governed dispatch behavior?

Required answer:

```
YES

```

### Question 7

> Do the final failure/readiness/figure/table/handoff/bundle stages consume real runtime outputs?

Required answer:

```
YES

```

If any answer is NO:

```
PASS IS PROHIBITED

```

Repair and repeat.

---

# 322. UPDATED SUCCESS CERTIFICATION ADDITION

The previously required success certification remains mandatory in full.

Append the following only after these new checks pass:

```
KNOWN IMPLEMENTATION DEFECT CLOSURE:

PASS

26-stage runtime dispatcher:
FULLY IMPLEMENTED

production stage handlers:
26 / 26

stage handlers remaining as authoring stubs:
0

A0 run-cell production routing:
COMPLETE

Stage-15 A0 closure:
COMPLETE

A4 production routing:
COMPLETE

Stage-18 A4 execution:
COMPLETE

A4 validation-selected representative routing:
COMPLETE

A4 C4 ensemble-vs-strongest-constituent:
FULLY IMPLEMENTED

A4 C5 ensemble-vs-strongest-constituent:
FULLY IMPLEMENTED

A4 C4/C5 participant-level inferential closure:
COMPLETE

A4 C4/C5 frozen statistics:
COMPLETE

A4 C4/C5 source artifacts:
COMPLETE

A4 C4/C5 Phase Analysis evidence:
COMPLETE

A4 C4/C5 Layer-10 source readiness:
COMPLETE

Stage 18U:
FULLY IMPLEMENTED

failure evidence aggregation:
FULLY IMPLEMENTED

readiness aggregation:
FULLY IMPLEMENTED

figure-source generation:
FULLY IMPLEMENTED

table-source generation:
FULLY IMPLEMENTED

downstream handoff generation:
FULLY IMPLEMENTED

final runtime bundle generation:
FULLY IMPLEMENTED

known implementation defects remaining:
0

regressions introduced during repair:
0

```

---

# 323. FINAL CUMULATIVE PRESERVATION RULE

This addition does not replace any previous part of the prompt.

The complete prompt must contain, in full:

```
Sections 0–118

Sections 119–167

Section 168

Sections 169–274

Sections 275–323

```

Every previous requirement remains mandatory.

The new sections specifically add explicit hard gates for the two defects already discovered:

```
1. incomplete real 26-stage runtime dispatcher

2. incomplete A4 C4/C5
   ensemble-vs-strongest-constituent
   inferential closure

```

They must be **repaired**, not merely documented.

After repair, rerun **all previous audits**, including:

```
Build Book exhaustion

Stretch-Version completeness

code-quality audit

actual-working-code audit

A0 audit

A4 audit

evaluation audit

artifact audit

test audit

gate audit

P01 regression audit

Kaggle simulation

Phase Analysis simulation

Layer 10 simulation

P03 simulation

security audit

bundle audit

post-package audit

zero-unresolved audit

```

Only after the entire cumulative audit returns PASS may the package be declared ready for actual Kaggle execution.