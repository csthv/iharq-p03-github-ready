# IHARQ BenchGuard Stretch C — Document Stack Governance and Creation Guide

> **Current revision:** V6.1 — single-track, ZIP-first, Kaggle-centered, full-depth consolidated-notebook phase workflow  
> **Supersedes:** V6 wherever V6.1 clarifies that notebook consolidation changes only execution organization and never reduces scientific, implementation, ablation, validation, analysis, or artifact scope  
> **Revision purpose:** retain the single direct phase process while making explicit that one or two consolidated notebooks must still perform the complete required scientific and engineering workload. The owner supplies one cumulative project ZIP; the phase master prompt inspects all prior work; one integrated phase implementation document is created; one comprehensive Kaggle notebook is prepared and executed when computation is required; insufficient evidence triggers the only permitted loopback; the completed run is documented in Protocol v1.0; the Phase Analysis Report is created; Layer 0 reviews claims; the Evidence Map is updated; Layer 10 creates the governed presentation and reproducibility package; and the cumulative project ZIP is updated for the next phase. GitHub and Hugging Face are optional complementary storage locations only for artifacts too large for the cumulative ZIP.  
> **Current status:** `[V6 GOVERNING GUIDE] [SINGLE-TRACK] [ZIP-FIRST] [REUSE-FIRST] [KAGGLE-CENTERED] [ONE-NOTEBOOK-DEFAULT] [FULL-ABLATION-AND-LAYER-COVERAGE] [NO-QUALITY-REDUCTION] [EVIDENCE-INSUFFICIENCY-LOOPBACK-ONLY] [FINAL-GITHUB-MIGRATION-DEFERRED]`

---

# 0. Governing principle

The project proceeds through one clear phase workflow.

```text
Owner supplies the cumulative project ZIP
→ phase master prompt inspects all prior work and all governing documents
→ reuse, gap, responsibility, dependency, and invalidation analysis
→ one integrated phase implementation document
→ one comprehensive Kaggle notebook when computation is required
→ execute and export the complete phase result bundle
→ determine whether the evidence is sufficient
    ├── YES: continue forward
    └── NO: repair only the relevant implementation/notebook/run scope and rerun
→ create or update the Phase Protocol v1.0 annex
→ create the Phase Evidence, Results, and Interpretation Report
→ apply Layer 0 claim and limitation review
→ update the Paper and Thesis Evidence Map
→ create the Layer 10 reproducibility and presentation package
→ update the cumulative project ZIP
→ begin the next phase
```

There are no alternative workflow modes.

## 0.1 Consolidation does not reduce scope

The one-notebook default is an **organization and orchestration rule only**.

It does not permit reducing, omitting, merging away, weakening, or simplifying any required:

- participating-layer implementation;
- ablation or control condition;
- baseline;
- matched comparison;
- seed or run cell;
- dataset or split;
- metric;
- statistical analysis;
- uncertainty analysis;
- diagnostic;
- negative or failed-result treatment;
- validation;
- figure-source dataset;
- table-source dataset;
- checkpoint;
- record;
- manifest;
- handoff;
- downstream artifact.

The complete work required by the Architecture, Registry, Execution and Evidence Plan, Protocol, Playbook, Method Selection, Nuts-and-Bolts, and current phase responsibilities must still be performed.

The simplification is:

```text
many required scientific and engineering operations
→ organized as sections, functions, configs, and run cells
→ inside one comprehensive notebook and one structured output bundle
```

It is not:

```text
fewer notebooks
→ fewer experiments, fewer ablations, fewer outputs, or lower analytical depth
```

Where two notebooks are genuinely required, the same full-scope rule applies across both notebooks.


There is no routine GitHub pull step.

There is no routine GitHub synchronization step.

There is no requirement to create many notebooks, many phase repositories, or many transport packages.

The only normal loopback is the evidence-insufficiency loop:

```text
insufficient, invalid, incomplete, or unusable evidence
→ identify the lawful defect owner
→ repair the minimum necessary scope
→ rerun the affected Kaggle execution
→ reevaluate evidence sufficiency
```

After evidence becomes sufficient, the workflow continues forward and does not restart the entire phase.

---

# Part I — Authority stack

## 1. Why the authority stack remains necessary

IHARQ BenchGuard Stretch C spans:

- Layers 0–10;
- Phases P00–P15;
- Ablations A0–A13;
- implementation;
- computation;
- analysis;
- claim governance;
- evidence mapping;
- reproducibility and presentation;
- thesis and paper outputs.

One document cannot safely own all decisions. The authority stack remains separated by responsibility.

## 2. Governing documents

The project uses:

```text
00. Document Stack Governance and Creation Guide
01. Master Architecture Specification
02. Canonical Artifact, Record, and Interface Registry
03. Execution and Evidence Plan
04. Experiment, Ablation, and Evaluation Protocol v0.1
05. Complete Phase Execution Playbook
06. Integrated Layers 0–10 Method Selection and Design Rationale Register
07. Integrated Layers 0–10 Detailed Design and Nuts-and-Bolts Specification
08. Implementation Build Book
09. Experiment, Ablation, and Evaluation Protocol v1.0
10. Paper and Thesis Evidence Map
```

Generated governed phase products are:

```text
11. Phase Evidence, Results, and Interpretation Report
12. Phase Layer 0 Claim Review and Disposition Record
13. Phase Layer 10 Reproducibility, Dashboard, Cards, Figures, Tables, and Export Package
14. Final Cross-Phase Results Synthesis Report
15. Reproduction, Release, and Archival Package
```

## 3. Authority ownership

| Question | Owner |
|---|---|
| What is the system and what does each layer own? | Architecture |
| What are the official records, fields, statuses, interfaces, and lifecycle rules? | Registry |
| What must each phase produce and what makes it complete? | Execution and Evidence Plan |
| What scientific fairness, comparison, ablation, split, and leakage rules must be preserved? | Protocol v0.1 and Protocol v1.0 |
| How does a phase proceed operationally? | Phase Execution Playbook |
| Which methods, models, datasets, platforms, and strategies are selected? | Method Selection |
| How do accepted methods work internally? | Nuts-and-Bolts |
| How is the project implemented, configured, executed, tested, and packaged? | Implementation Build Book |
| What exact run was performed and what analysis contract applies? | Protocol v1.0 |
| What did the phase produce and what did the analysis find? | Phase Evidence Report |
| Which claims and wording are permitted? | Layer 0 |
| Which exact evidence supports which claim and manuscript/output location? | Evidence Map |
| How are governed results rendered and reproduced? | Layer 10 |

A later document may reflect an earlier authority but may not silently replace it.

---

# Part II — Primary project-state strategy

## 4. The cumulative ZIP is the working project state

From Phase 1 onward, the owner supplies one cumulative ZIP containing the complete current project state.

Recommended naming:

```text
IHARQ_Project_State_After_Phase_<NN>_R<REV>.zip
```

The ZIP is the main continuation package for the next phase.

It should contain, as applicable:

- Governance V6;
- all seven core authority documents;
- the current Implementation Build Book;
- all current code;
- schemas;
- configurations;
- contracts;
- fixtures;
- tests;
- scripts;
- notebooks;
- completed phase packages;
- Protocol v1.0 master and completed phase annexes;
- Phase Evidence Reports;
- Layer 0 dispositions;
- Evidence Map master and phase annexes;
- Layer 10 packages;
- manifests;
- hashes;
- supersession records;
- limitations;
- handoffs;
- pointers to external oversized artifacts.

## 5. No routine GitHub intake

The phase master prompt must not require:

- cloning a GitHub repository;
- using GitHub CLI;
- using a GitHub connector;
- pulling a branch;
- reading project state from Git history.

When the cumulative ZIP is supplied, the ZIP is the primary input.

GitHub may contain a partial or complementary representation, but it is not the controlling working state during intermediate phases.

## 6. ZIP integrity requirements

Every cumulative ZIP must include:

```text
project_state_manifest.yaml
project_state_checksums.sha256
current_document_index.md
current_artifact_index.csv
external_artifact_pointer_manifest.yaml
phase_handoff.yaml
```

The phase master prompt must verify:

- ZIP CRC;
- file count;
- checksums;
- current versus historical status;
- required authority presence;
- required handoff presence;
- external pointer completeness;
- absence of unsafe paths;
- absence of secrets and temporary files.

---

# Part III — Single phase master prompt

## 7. Purpose

For every new phase, one master phase prompt receives:

- Governance V6;
- the seven core authorities;
- the cumulative project ZIP;
- the target phase;
- any owner-supplied decisions or constraints.

The master prompt must inspect the complete package and produce the plan and implementation document for the next phase.

## 8. Required phase declaration

The owner supplies:

```yaml
target_phase: ""
phase_objective: ""
available_compute: "KAGGLE"
current_project_zip: ""
known_external_artifacts: []
known_constraints: []
```

The prompt derives the rest from the ZIP.

The owner should not need to manually reconstruct all prior phase and layer status when the package already records it.

## 9. Required intake analysis

The master prompt must determine:

- completed phases;
- incomplete phases;
- current Protocol annexes;
- existing Phase Reports;
- current Layer 0 decisions;
- current Evidence Map annexes;
- current Layer 10 packages;
- implemented layers;
- reusable layer capabilities;
- reusable artifacts;
- stale or invalid artifacts;
- unresolved dependencies;
- target-phase participating layers;
- expected target-phase outputs;
- required ablations or controls;
- required computational work;
- required non-computational work;
- downstream consumers.

## 10. Reuse-first rule

Before requesting any new implementation or run, determine whether an existing implementation or artifact can be reused.

Reuse is permitted when the relevant identity matches, including:

- source dataset;
- split;
- preprocessing;
- method;
- model;
- configuration;
- seed where relevant;
- Protocol role;
- evidence status;
- validity;
- lineage;
- limitation status.

Do not recreate an artifact merely because a new phase is beginning.

Do not rewrite a layer implementation when the existing reusable implementation already satisfies the target phase.

## 11. Gap classification

For every target-phase responsibility, assign one:

```text
REUSE_EXISTING_IMPLEMENTATION_AND_ARTIFACT
REUSE_IMPLEMENTATION_WITH_NEW_PHASE_CONFIG
REUSE_IMPLEMENTATION_AND_EXECUTE_NEW_RUN
EXTEND_EXISTING_IMPLEMENTATION
CREATE_MISSING_IMPLEMENTATION
CREATE_MISSING_DOCUMENT_OR_MANIFEST
NOT_APPLICABLE_WITH_REASON
BLOCKED_BY_MISSING_INPUT
```

## 12. One integrated implementation document

Create one phase implementation document:

```text
IHARQ_Phase_<NN>_Integrated_Implementation_and_Execution_Plan_R<REV>.md
```

It must include:

1. target-phase purpose;
2. authority intake;
3. prior-state summary;
4. participating layers;
5. responsibility matrix;
6. reuse decisions;
7. missing capabilities;
8. required implementation changes;
9. phase configurations;
10. Kaggle notebook design;
11. expected inputs;
12. expected outputs;
13. tests and validators;
14. evidence sufficiency rules;
15. evidence-insufficiency repair loop;
16. Protocol v1.0 handoff;
17. Phase Analysis handoff;
18. Layer 0 handoff;
19. Evidence Map handoff;
20. Layer 10 handoff;
21. cumulative ZIP update requirements.

Do not split the implementation plan into many independent documents unless a genuinely separate technical subsystem cannot be represented clearly in the integrated document.

## 13. Layer ownership remains explicit

Although there is one integrated phase implementation document, each layer’s responsibilities must remain distinguishable.

For every participating layer include:

```yaml
layer_id: ""
phase_responsibility: ""
existing_capability: ""
reuse_decision: ""
implementation_change: ""
phase_config: ""
inputs: []
outputs: []
tests: []
downstream_consumers: []
limitations: []
```

One integrated document does not mean mixed or unclear ownership.

---

# Part IV — Kaggle-centered execution

## 14. When Kaggle is used

Use Kaggle when the phase requires meaningful computation, including:

- model training;
- model evaluation;
- calibration;
- uncertainty analysis;
- ablations;
- temporal analysis;
- policy evaluation;
- stress testing;
- simulation;
- embodiment;
- large-scale analysis;
- GPU or high-memory execution.

Small document checks, schema checks, parsing, and light deterministic validation may run locally.

## 15. Notebook-count rule

Use one comprehensive notebook by default.

This notebook is the consolidated execution container for the **complete** target-phase workload. It must include every required layer operation, ablation, baseline, control, matched comparison, metric, diagnostic, validation, and exported artifact. Notebook consolidation must never be used as a reason to reduce scientific scope or omit required work.

Recommended name:

```text
IHARQ_Phase_<NN>_Complete_Execution_and_Analysis_R<REV>.ipynb
```

A second notebook is allowed only when one notebook is technically impractical because of a real constraint such as:

- incompatible runtime environments;
- execution and analysis cannot fit within one Kaggle session;
- a large immutable first-stage output must be consumed by a separate second-stage run;
- Kaggle resource limits make one notebook impossible.

A second notebook requires a short justification.

Do not create separate notebooks merely because:

- several layers participate;
- several ablations exist;
- several datasets exist;
- several result sections exist;
- the notebook becomes long.

A long but organized notebook is acceptable.

The notebook should be modular internally, using:

- clear numbered sections;
- importable project modules;
- reusable functions;
- configuration-driven run matrices;
- explicit layer subsections;
- explicit ablation subsections;
- deterministic run-cell identifiers;
- resumable checkpoints where lawful;
- one final organized export stage.

Each scientifically distinct ablation or control must retain its own identity, inputs, configuration, outputs, status, and analysis. Several ablations may be executed by one parameterized loop or shared function, but their records and results must remain separately traceable.


## 16. Notebook structure

The notebook should contain:

1. title, phase identity, and authority references;
2. current project-state ZIP identity;
3. environment setup;
4. package and dependency installation;
5. configuration loading;
6. input and external-pointer resolution;
7. deterministic preflight checks;
8. reusable artifact resolution;
9. required implementation import or generation;
10. target-phase execution;
11. all required ablations and controls;
12. all required metrics;
13. diagnostics;
14. negative and failed-result preservation;
15. evidence sufficiency evaluation;
16. figure-source data;
17. table-source data;
18. complete bundle generation;
19. checksums and manifests;
20. final downloadable outputs.

Authority-bearing logic should remain in importable modules where practical, but the notebook must be self-contained enough to run from a clean Kaggle environment.

## 17. Complete output bundle

The notebook must export one organized phase execution bundle containing the complete outputs of every required layer, ablation, baseline, control, comparison, metric, diagnostic, and validation:

```text
phase_<NN>_execution_bundle_<RUN_ID>/
    README.md
    authority_manifest.json
    source_project_state_manifest.json
    environment_manifest.json
    notebook_manifest.json
    config_snapshot/
    inputs/
    records/
    raw_outputs/
    metrics/
    diagnostics/
    negative_and_failed_results/
    figure_source_data/
    table_source_data/
    logs/
    checkpoints_or_external_pointers/
    manifests/
    analysis_inputs/
    protocol_v1_handoff/
    layer0_handoff/
    evidence_map_handoff/
    layer10_source_bundle/
    gate_decision.json
    phase_execution_handoff.yaml
    checksums.sha256
```


Even though the notebook count is small, the exported artifacts must remain professionally separated by identity and purpose. A single notebook must not collapse distinct scientific outputs into one opaque file.

At minimum, the bundle must make it possible to retrieve independently:

- each run cell;
- each ablation/control result;
- each baseline result;
- each matched-comparison record;
- each metric record;
- each negative or failed result;
- each figure-source dataset;
- each table-source dataset;
- each layer handoff;
- each downstream evidence link.

The bundle must preserve every major output needed by:

- Protocol v1.0;
- Phase Analysis;
- Layer 0;
- Evidence Map;
- Layer 10;
- later phases;
- thesis figures and tables;
- reproduction.

## 18. Large outputs

When an artifact is too large for the cumulative ZIP:

- upload it to Hugging Face or GitHub Release storage;
- use an immutable revision;
- calculate SHA-256;
- record size;
- record license and access requirements;
- include retrieval instructions;
- include an exact pointer inside the cumulative ZIP.

GitHub should not be used for routine small-file synchronization.

Hugging Face is preferred for large models, datasets, and structured ML artifacts.

GitHub Releases may be used for large release archives when appropriate.

---

# Part V — The only loopback

## 19. Evidence sufficiency decision

After the Kaggle run, determine whether the phase produced sufficient valid evidence.

Evidence is sufficient when:

- required outputs exist;
- required tests pass;
- required records validate;
- required ablations or controls were executed or lawfully classified;
- required metrics were produced;
- invalid, failed, negative, blocked, and unmatched outcomes were preserved;
- source and environment identity are complete;
- manifests and checksums close;
- outputs are usable by Protocol v1.0 and Phase Analysis;
- no unresolved blocking defect remains.

## 20. Insufficient evidence

Evidence is insufficient when:

- a required output is missing;
- a required run failed;
- the notebook did not preserve a needed result;
- a required ablation or control did not execute;
- a schema or lineage check failed;
- the run is not reproducible;
- evidence cannot support the required phase conclusions;
- a blocking limitation remains unresolved.

## 21. Repair loop

The only normal loopback is:

```text
evidence insufficient
→ identify exact defect
→ identify lawful owner
→ repair the minimum necessary implementation, config, input, or notebook section
→ preserve the failed evidence
→ rerun only the affected execution scope
→ regenerate the complete bundle
→ reevaluate evidence sufficiency
```

Do not restart all prior phases.

Do not rebuild unaffected layers.

Do not create a new process branch.

Do not create an additional governance track.

Repeat only until:

- evidence becomes sufficient;
- the phase is lawfully blocked;
- the owner explicitly defers the phase.

## 22. Repair ownership

| Defect | Repair owner |
|---|---|
| missing module/file/command/test | Implementation Build Book and code |
| wrong algorithm or validator | Nuts-and-Bolts |
| wrong selected method | Method Selection |
| missing/incorrect record or field | Registry revision |
| missing phase output or gate | Execution and Evidence Plan |
| wrong phase procedure | Playbook |
| wrong comparison or analysis rule | Protocol |
| unsupported interpretation | Phase Analysis or Layer 0 |
| broken evidence link | Evidence Map |
| wrong public rendering | Layer 10 |

---

# Part VI — Protocol v1.0 after execution

## 23. Single Protocol rule

After sufficient execution evidence exists, create or update the Protocol v1.0 phase annex.

There are no Protocol timing modes.

The phase annex must faithfully record:

- what was implemented;
- what was executed;
- datasets;
- splits;
- models;
- methods;
- configs;
- seeds;
- ablations;
- controls;
- metrics;
- comparisons;
- exclusions;
- invalid and failed cases;
- environment;
- exact run IDs;
- exact analysis inputs;
- exact evidence status;
- limitations;
- any reruns and their reasons.

## 24. No post-hoc manipulation

Although Protocol v1.0 is completed after the Kaggle run, it must not rewrite the execution history or hide result-dependent changes.

Rules:

- record what actually happened;
- preserve all failed and superseded attempts;
- do not change metrics because results were inconvenient;
- do not remove negative results;
- do not change exclusions without recording and rerunning the affected analysis;
- do not describe an unplanned comparison as pre-registered;
- when a change is made after observing results, record it explicitly;
- when the change affects evidence sufficiency, use the same repair-and-rerun loop.

This is one integrity rule, not a separate workflow mode.

## 25. Protocol outputs

Create:

```text
docs/authorities/protocol_v1_0/master_protocol.md
docs/authorities/protocol_v1_0/phases/phase_<NN>_annex.md
docs/authorities/protocol_v1_0/machine_readable/run_matrix.yaml
docs/authorities/protocol_v1_0/machine_readable/analysis_contract.yaml
```

The phase annex becomes the exact execution-and-analysis record for the phase.

---

# Part VII — Phase Analysis Report

## 26. Purpose

The Phase Evidence, Results, and Interpretation Report answers:

```text
What did this phase implement, execute, produce, fail to produce, and show?
```

## 27. Required contents

The report must include:

1. phase identity and objective;
2. governing authorities;
3. prior-state and reused artifacts;
4. implementation completed for the phase;
5. Kaggle notebook identity;
6. environment;
7. inputs;
8. executed runs;
9. failed and repaired runs;
10. output inventory;
11. required tests and gates;
12. all required ablations and controls;
13. primary and secondary metrics;
14. uncertainty or intervals where applicable;
15. subgroup, temporal, stress, simulation, or embodiment analyses where applicable;
16. figure-source data;
17. table-source data;
18. negative and null findings;
19. invalid, blocked, excluded, and unmatched cases;
20. direct findings;
21. supported interpretations;
22. candidate claims;
23. mechanism hypotheses clearly labelled as hypotheses;
24. limitations;
25. downstream readiness;
26. Layer 0 handoff;
27. Evidence Map handoff;
28. Layer 10 source handoff.

## 28. Ablation coverage


The requirement to use one or very few notebooks does not reduce the required ablation-analysis depth. Every applicable A0–A13 cell and every required sub-ablation must still be executed, preserved, analyzed, and reported according to the controlling Protocol and phase responsibilities.

For every A0–A13 relevant to the target phase, state:

- official identity;
- whether the required foundation already existed;
- whether it was reused;
- whether it was executed in this phase;
- configuration;
- comparison;
- outputs;
- result;
- limitation;
- downstream consequence.

For A0–A13 not executed in the phase, state why they were not applicable.

A14 must remain rejected.

Do not omit an ablation simply because its implementation existed in an earlier phase.

## 29. Interpretation hierarchy

Use:

```text
measured result
→ supported interpretation
→ candidate claim
→ mechanism hypothesis, when justified
```

Do not treat candidate claims as approved before Layer 0.

---

# Part VIII — Layer 0, Evidence Map, and Layer 10

## 30. Layer 0

After the Phase Analysis Report, Layer 0 reviews every candidate claim.

Layer 0 may:

- approve;
- qualify;
- downgrade;
- defer;
- reject;
- block;
- require limitations;
- require safer wording.

Layer 0 may not change:

- measurements;
- counts;
- metrics;
- run inclusion;
- source evidence;
- Protocol records.

## 31. Evidence Map

After Layer 0, update the phase annex of the Paper and Thesis Evidence Map.

For every reviewed claim include:

```text
claim_id
reviewed_claim_text
phase_id
protocol_cell_ids
run_ids
record_ids
analysis_release_id
ablation_ids
figure_ids
table_ids
card_ids
limitations
manuscript_sections
reproduction_assets
layer0_disposition_id
```

The Evidence Map organizes and links evidence.

It does not approve claims.

## 32. Layer 10

After the Evidence Map, Layer 10 creates:

- reproducibility package;
- result cards;
- phase dashboard/status view;
- figures;
- tables;
- exports;
- provenance views;
- claim-evidence views;
- negative-result views;
- limitation warnings;
- release manifest.

Layer 10 is read-only.

It must not rerun, repair, retune, reclassify, or strengthen evidence.

---

# Part IX — Updated cumulative ZIP

## 33. End-of-phase package

After Layer 10, create:

```text
IHARQ_Project_State_After_Phase_<NN>_R<REV>.zip
```

This becomes the complete input for the next phase.

## 34. Required package contents

Include:

- current Governance V6;
- current seven core authorities;
- current Build Book;
- current code;
- schemas/configs/contracts/tests/scripts;
- current Kaggle notebook;
- current phase execution bundle or local-sized subset;
- pointers to external oversized artifacts;
- Protocol v1.0 master and phase annex;
- Phase Analysis Report;
- Layer 0 disposition;
- Evidence Map annex;
- Layer 10 package;
- phase handoff;
- current document index;
- current artifact index;
- current and historical manifests;
- checksums;
- supersession records;
- limitations;
- downstream readiness.

## 35. No unnecessary duplication

The ZIP should not contain:

- repeated identical copies of large artifacts;
- many copies of the same notebook;
- all temporary Kaggle files;
- caches;
- environments;
- secrets;
- redundant raw logs when a complete canonical log bundle already exists.

Preserve important history, but do not make the current package unreadable.

Use:

```text
current/
history/
external_pointers/
```

or an equivalent clear structure.

---

# Part X — External storage

## 36. Complementary role only

During intermediate phases:

- the cumulative ZIP is primary;
- GitHub is optional;
- Hugging Face is optional;
- external platforms store only oversized artifacts or public complements.

## 37. External pointer record

Every external artifact must have:

```yaml
artifact_id: ""
provider: ""
repository_or_dataset: ""
immutable_revision: ""
path_or_filename: ""
sha256: ""
size_bytes: ""
format: ""
license: ""
access_requirements: ""
producer_phase: ""
consumer_phases: []
retrieval_instructions: ""
local_copy_status: ""
```

A URL without revision and checksum is not sufficient.

## 38. Heavy artifact examples

Externalize when genuinely necessary:

- model checkpoints;
- large derived datasets;
- large simulation rollouts;
- large stress bundles;
- large evaluation releases;
- final archive assets.

Keep small manifests, summaries, configs, and pointers inside the cumulative ZIP.

---

# Part XI — Final migration

## 39. Intermediate phases

Do not require full GitHub publication after every phase.

Do not require GitHub connector use.

Do not require GitHub CLI.

Do not require continuous repository synchronization.

## 40. Final project completion

After all required phases are complete:

```text
complete cross-phase synthesis
→ final Layer 0 review
→ consolidate project-wide Evidence Map
→ create final Layer 10 package
→ perform clean reproduction
→ create the clean professional GitHub repository
→ upload heavy release assets
→ verify the final publication
→ freeze the project
```

Only then migrate the complete curated project to GitHub.

The final GitHub repository should be a clean public derivative of the complete cumulative project state.

---

# Part XII — Required phase outputs

## 41. Minimum per-phase output set

Every completed phase must produce, as applicable:

```text
01. Integrated Phase Implementation and Execution Plan
02. Kaggle Notebook
03. Phase Execution Bundle
04. Protocol v1.0 Phase Annex
05. Phase Evidence, Results, and Interpretation Report
06. Layer 0 Claim Review and Disposition
07. Evidence Map Phase Annex
08. Layer 10 Reproducibility and Presentation Package
09. Phase Handoff
10. Updated Cumulative Project ZIP
```

## 42. No redundant output rule

Do not recreate an output when:

- the exact same artifact already exists;
- its identity and validity remain unchanged;
- the new phase can lawfully reference it.

Create a new output when:

- the scientific condition changed;
- the configuration changed;
- the source changed;
- the evidence role changed;
- the artifact was invalidated;
- the phase requires a new derived result.

---

# Part XIII — Validation and closure

## 43. Phase completion

A phase is ready to close when:

- all required responsibilities are dispositioned;
- required implementations exist;
- required Kaggle execution completed;
- evidence is sufficient;
- required outputs exist;
- Protocol v1.0 phase annex exists;
- Phase Analysis Report exists;
- Layer 0 completed;
- Evidence Map updated;
- Layer 10 completed;
- limitations are explicit;
- external pointers resolve;
- cumulative ZIP validates;
- downstream handoff exists.

## 44. Blocking conditions

Do not close a phase when:

- evidence remains insufficient;
- a required output is missing;
- a blocking validation fails;
- a required ablation/control is omitted;
- Protocol does not match the actual run;
- Phase Analysis is incomplete;
- Layer 0 claims are unresolved;
- Evidence Map links are broken;
- Layer 10 strengthens or recomputes evidence;
- the cumulative ZIP is incomplete or corrupt.

Use the evidence-insufficiency loop where repair is possible.

Otherwise return a precise blocked status.

---

# Part XIV — Machine-readable workflow

## 45. Single-track phase handoff

```yaml
phase_handoff:
  phase_id: ""
  phase_status: ""

  source_project_state:
    zip_filename: ""
    zip_sha256: ""
    manifest_id: ""

  prior_state:
    completed_phases: []
    implemented_layers: []
    reusable_artifacts: []
    external_artifacts: []

  implementation:
    document_id: ""
    participating_layers: []
    reused_capabilities: []
    new_capabilities: []
    extended_capabilities: []

  kaggle:
    notebook_id: ""
    notebook_count: 1
    second_notebook_justification: ""
    execution_bundle_id: ""
    evidence_sufficiency: ""
    repair_iterations: []

  protocol_v1:
    master_id: ""
    phase_annex_id: ""
    run_matrix_id: ""
    analysis_contract_id: ""

  analysis:
    report_id: ""
    findings: []
    ablation_coverage: []
    limitations: []

  layer0:
    disposition_id: ""
    approved_claims: []
    qualified_claims: []
    blocked_claims: []

  evidence_map:
    annex_id: ""
    mapped_claims: []
    mapped_figures: []
    mapped_tables: []

  layer10:
    package_id: ""
    cards: []
    figures: []
    tables: []
    exports: []
    reproduction_manifest: ""

  next_project_state:
    zip_filename: ""
    zip_sha256: ""
    manifest_id: ""

  external_pointers: []
  open_blockers: []
  next_phase_readiness: ""
```

---

# Part XV — Anti-overcomplication rules

## 45.1 Anti-overcomplication is not anti-comprehensiveness

The anti-overcomplication policy applies to the number of workflow branches, notebooks, repositories, duplicated documents, and redundant transport artifacts.

It does not apply to required scientific or engineering content.

Never use this policy to justify:

- dropping an ablation;
- reducing a run matrix;
- omitting a baseline;
- skipping a metric;
- removing a validation;
- weakening an analysis;
- combining scientifically distinct results without traceability;
- failing to export required artifacts;
- shortening the Phase Analysis Report below the depth required by the evidence.


## 46. Required simplicity rules

Do not:

- introduce multiple workflow modes;
- create separate protocol timing tracks;
- require GitHub for normal phase continuation;
- create many notebooks;
- create one notebook per layer;
- create one notebook per ablation;
- reduce ablation coverage because notebook count is limited;
- reduce the run matrix, metrics, diagnostics, or exported artifacts to keep a notebook short;
- create many repositories;
- create many nearly identical reports;
- rerun unchanged upstream layers;
- regenerate large prior artifacts;
- add optional process branches that do not solve an actual problem;
- create additional governance documents when the current document can own the rule;
- use external platforms for small artifacts;
- create separate loopbacks for every document.

## 47. Allowed complexity

Complexity is justified only when required by:

- actual scientific validity;
- actual implementation dependency;
- actual Kaggle runtime limitation;
- actual incompatible environment;
- actual artifact-size limit;
- actual evidence insufficiency;
- actual invalidation;
- actual downstream requirement.

Every added artifact, notebook, or external pointer must have a clear purpose.

---

# Part XVI — Final governing summary

## 48. Single-track project workflow

```text
Use the owner-supplied cumulative ZIP as the project state.
Inspect all prior work and all governing documents.
Determine what the target phase requires.
Reuse every valid implementation and artifact.
Create one integrated phase implementation document.
Create one comprehensive Kaggle notebook when computation is required, while preserving the complete required layer, ablation, baseline, comparison, metric, validation, and artifact scope.
Execute the phase and export one complete organized bundle.
If evidence is insufficient, repair only the relevant scope and rerun.
When evidence is sufficient, create the Phase Protocol v1.0 annex.
Create the Phase Evidence, Results, and Interpretation Report.
Apply Layer 0.
Update the Evidence Map.
Create the Layer 10 package.
Create the updated cumulative project ZIP.
Proceed to the next phase.
Use GitHub or Hugging Face only for artifacts too large for the ZIP.
Migrate the complete curated project to GitHub after all phases are finished.
```

## 49. Final principle

> Keep one clear phase path, reuse what already exists, execute the complete required scientific and engineering scope inside one or at most two well-organized Kaggle notebooks, preserve every required ablation, comparison, validation, analysis, and artifact, loop back only when the evidence is not sufficient, and continue forward through Protocol v1.0, Phase Analysis, Layer 0, Evidence Map, Layer 10, and the next cumulative project ZIP.
