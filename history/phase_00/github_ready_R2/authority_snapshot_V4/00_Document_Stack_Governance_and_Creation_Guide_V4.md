# IHARQ BenchGuard Stretch C — Document Stack Governance and Creation Guide

> **Current revision:** V4 — phase-oriented, real-run-first implementation and evidence-closure edition  
> **Supersedes:** V3 wherever V4 introduces a changed workflow, ordering rule, document set, or execution policy  
> **Revision purpose:** formalize the project owner's chosen post–Nuts-and-Bolts operating model: target-phase orchestration, reuse-first layer implementation, sequential layer work packages, real-run-first execution with conditional smoke-test fallback, selectable Protocol v1.0 timing with explicit evidence-status consequences, phase-level scientific analysis, Layer 0 claim review, Paper and Thesis Evidence Map completion before Layer 10 publication, and GitHub/Kaggle/Hugging Face–oriented artifact governance  
> **Current status:** `[V4 GOVERNING GUIDE] [SEVEN-CORE-DOCUMENT BASELINE] [PHASE-ORIENTED EXECUTION] [REAL-RUN-FIRST] [CONDITIONAL-SMOKE] [PHASE-ANALYSIS FORMALIZED] [EVIDENCE-MAP-BEFORE-LAYER-10]`

---

## 0. Interpretation, precedence, and status of examples

This guide defines the authority, purpose, inputs, outputs, exclusions, sequencing, synchronization, execution behavior, evidence lifecycle, and publication responsibilities of the IHARQ BenchGuard Stretch C document and artifact system.

All examples are **illustrative rather than exhaustive or prescriptive**. A method, dataset, model, simulator, metric, dashboard technology, storage provider, or file layout becomes binding only when accepted by the document that owns that decision and realized through the corresponding implementation and execution authorities.

Where V4 conflicts with V3, **V4 controls**. In particular, V4 makes the following controlled changes:

1. the post-design workflow is **phase-oriented** while implementations remain **layer-owned and reusable**;
2. the default execution path is **real-run-first**, with smoke testing used conditionally rather than automatically;
3. Protocol v1.0 timing is selectable, but the timing determines whether a run may be treated as confirmatory;
4. phase results are closed through a formal analysis, claim, evidence-map, and publication sequence;
5. the Paper and Thesis Evidence Map is updated **before** Layer 10 creates the final phase publication package;
6. no standalone *Document Map and Version Control* document is required;
7. no standalone *Registry Impact and Patch Ledger* document is required;
8. version identity, change history, and Registry evolution are controlled directly through file metadata, repository history, decision references, schema migration notes, manifests, and accepted revisions.

The absence of those two standalone documents does not remove versioning, change control, or schema governance. It changes their **physical location**, not their professional obligation.

---

# Part I — Why the authority stack exists

## 1. The underlying research-engineering problem

IHARQ BenchGuard Stretch C is simultaneously:

- a layered architecture spanning Layers 0–10;
- a record-first evidence and lineage system;
- a public-data benchmarking framework;
- a calibration, uncertainty, and selective-prediction study;
- an IHARQ evidence-verification system;
- a temporal trust and RegimeRisk study;
- an adaptive readiness and decision-policy framework;
- a simulated sequential evaluation environment;
- a controlled robustness and stress-testing framework;
- a simulation-only embodiment and action-consequence demonstration;
- a dashboard, cards, provenance, and reproducibility system;
- and a thesis/paper evidence-production program with strict claim-safety limits.

One document cannot safely own architecture, records, phases, methods, formulas, implementation, execution, statistical analysis, claims, and publication. The stack therefore separates authority while preserving traceability.

## 2. Governing mindset

```text
Architecture defines what the system is and what each layer owns.
Canonical Registry defines official records, artifacts, interfaces, vocabularies, and lifecycle.
Execution and Evidence Plan defines what each phase must produce and what completion means.
Protocol v0.1 preserves scientific fairness, ablation, leakage, and comparison obligations.
Phase Execution Playbook defines how each phase proceeds procedurally.
Method Selection Register defines which concrete choices are accepted and why.
Nuts-and-Bolts defines how accepted choices work internally.
Implementation Build Book defines how reusable layer capabilities and phase runs are coded and operated.
Protocol v1.0 defines the exact registered run and analysis contract.
Phase Evidence Report records what a phase actually produced and what the registered analysis found.
Layer 0 governs interpretation, claim sufficiency, wording, and limitations.
Paper and Thesis Evidence Map links reviewed claims to exact evidence and manuscript locations.
Layer 10 packages and presents the already governed evidence reproducibly.
Cross-Phase Synthesis integrates the complete project evidence.
```

## 3. Authority, reflection, and non-duplication

The same scientific object can appear in several places in different forms without duplicating authority.

Example:

```text
Method Selection:
    selects temperature scaling and records why.

Canonical Registry:
    defines the accepted CalibrationRecord contract.

Nuts-and-Bolts:
    defines fitting logic, split guards, equations, validators, and failure behavior.

Implementation Build Book:
    defines modules, classes, configs, commands, environments, and tests.

Protocol v1.0:
    defines the exact datasets, seeds, matched variants, metrics, and analyses.

Phase Evidence Report:
    records the observed results and candidate interpretations.

Layer 0:
    approves, qualifies, downgrades, or blocks candidate claims.

Evidence Map:
    links the reviewed claim to runs, records, tables, figures, limitations, and manuscript sections.

Layer 10:
    renders the governed table, figure, card, dashboard, and reproduction package.
```

Only Method Selection owns the selection rationale. Only Protocol v1.0 owns the registered comparison. Only the Phase Evidence Report records the phase finding. Only Layer 0 owns final claim disposition. Layer 10 never becomes the source of scientific truth.

---

# Part II — Current document and evidence-product set

## 4. Seven completed core authority documents

The future phase-orchestration process receives the following seven principal completed authorities:

```text
01. Master Architecture Specification
02. Canonical Artifact, Record, and Interface Registry
03. Execution and Evidence Plan
04. Experiment, Ablation, and Evaluation Protocol v0.1
05. Complete Phase Execution Playbook
06. Integrated Layers 0–10 Method Selection and Design Rationale Register
07. Integrated Layers 0–10 Detailed Design / Nuts-and-Bolts Specification
```

These seven documents define the accepted project before implementation and empirical execution.

## 5. Remaining authority documents

```text
08. Implementation Build Book
09. Experiment, Ablation, and Evaluation Protocol v1.0
10. Paper and Thesis Evidence Map
```

These may be physically organized as master documents with phase annexes and layer work packages. Separate phase files are permitted, but they remain governed parts of one project-wide authority and must not drift into incompatible definitions.

## 6. Generated governed evidence products

The execution process also produces:

```text
11. Phase Evidence, Results, and Interpretation Report — one governed report per phase
12. Phase Layer 0 Claim Review and Disposition Record
13. Phase Layer 10 Reproducibility, Dashboard, Cards, and Export Package
14. Final Cross-Phase Results Synthesis Report
15. Reproduction, Release, and Archival Package
```

Items 11–15 report, govern, package, or synthesize what happened. They may not silently select new methods, redefine canonical records, change the registered analysis after seeing results, or invent stronger evidence.

## 7. Recommended physical repository arrangement

```text
docs/
    authorities/
        architecture/
        registry/
        execution_plan/
        protocol_v0_1/
        phase_playbook/
        method_selection/
        nuts_and_bolts/
        implementation_build_book/
        protocol_v1_0/
        paper_thesis_evidence_map/
    phase_packages/
        phase_00/
        phase_01/
        ...
        phase_15/
    synthesis/
    release/
```

A repository manifest, Git history, release tags, file headers, hashes, and supersession notices provide version control without requiring a separate document-map authority.

---

# Part III — Document-by-document authority specification

## 8. Master Architecture Specification

### Primary question

```text
What is the IHARQ BenchGuard Stretch C system, and what does each layer own?
```

### Contains

- Layers 0–10, modules, and submodules;
- system boundaries and noninterference rules;
- high-level data and evidence flows;
- allowed and prohibited cross-layer interactions;
- capability tiers;
- high-level phase and ablation relationships;
- record-first philosophy;
- claim-safety and scope boundaries;
- public-data, simulation-only, stress-only, and embodiment-proxy limitations;
- high-level contribution narrative.

### Produces

- system identity;
- functional graph;
- layer/module ownership model;
- architecture constraints;
- high-level input/output relationships.

### Must not contain

- final method choices;
- implementation classes or commands;
- final statistical run matrix;
- empirical results;
- final thesis wording.

### Example

Correct:

```text
Layer 7 owns simulated state, action, transition, reward, cost, session, and rollout evidence.
```

Incorrect:

```text
Layer 7 must use one exact Python class and one exact reward-weight vector.
```

## 9. Canonical Artifact, Record, and Interface Registry

### Primary question

```text
What are the official records, artifacts, identifiers, interfaces, vocabularies, owners, and lifecycle rules?
```

### Contains

- canonical record and artifact names;
- fields, types, required identifiers, and lineage;
- producer-consumer contracts;
- ownership and mutability;
- lifecycle, validity, supersession, and invalidation semantics;
- status, reason, action, and limitation vocabularies;
- phase and ablation linkage;
- validation obligations;
- Layer 0 and Layer 10 handoff fields;
- aliases and deprecations;
- schema revision history and migration notes within the Registry itself or repository change history.

### Produces

- canonical interface truth;
- stable schema vocabulary;
- validation and lifecycle contracts;
- source-of-truth producer-consumer relationships.

### Must not contain

- first-time scientific selection rationale;
- detailed algorithm derivations;
- repository layout;
- empirical results;
- paper claims.

### Controlled Registry change rule

When implementation or execution reveals a necessary schema change, the discovering work package must issue a documented change request containing the triggering decision, affected schema, compatibility effect, migration requirement, validators, downstream consumers, and accepted revision. The accepted change is then made directly in a new Registry revision and propagated to dependent documents and code. No parallel Registry or separate patch-ledger authority is created.

### Example

The Registry may define `CalibrationRecord` with `source_prediction_id`, `fit_split_id`, `method_id`, `config_hash`, `validity_status`, and lineage. It does not decide that temperature scaling is scientifically preferred.

## 10. Execution and Evidence Plan

### Primary question

```text
What evidence must each Phase 0–15 produce, and what gates make the phase complete and usable?
```

### Contains

For each phase:

- purpose and scope;
- participating layers and modules;
- required input records and upstream packages;
- required outputs and evidence products;
- validation and evidence gates;
- exit criteria;
- downstream dependencies;
- ablation readiness;
- diagnostic-only, downgrade, blocked, and invalid conditions;
- Layer 0, Evidence Map, and Layer 10 closure obligations.

### Produces

- phase evidence roadmap;
- phase definition of done;
- required handoff packages;
- phase-level readiness and completion gates.

### Must not contain

- full run commands;
- final algorithms;
- code layout;
- final run matrix;
- observed results.

### Example

For a calibration phase, the Plan may require calibrated predictions, leakage-validation evidence, metric records, matched comparison artifacts, a Phase Evidence Report, Layer 0 disposition, Evidence Map update, and Layer 10 package.

## 11. Experiment, Ablation, and Evaluation Protocol v0.1

### Primary question

```text
What scientific fairness and comparison obligations must remain preserved while the design is being finalized?
```

### Contains

- A0–A13 definitions and sub-ablation governance;
- baseline obligations;
- matched-comparison principles;
- split, leakage, chronology, and contamination rules;
- metric families and operating-point principles;
- clean/stressed pairing;
- frozen/adaptive separation;
- negative-result and diagnostic-only treatment;
- preliminary statistical expectations;
- claim-safety boundaries.

### Produces

- preliminary scientific fairness contract;
- preserved comparison obligations;
- requirements that Protocol v1.0 must eventually make exact.

### Must not contain

- exact final run cells when feasibility is unresolved;
- code commands;
- observed conclusions.

### Example

It may require that calibrated and uncalibrated variants use identical source predictions, splits, seeds, and evaluation examples, without yet fixing the final seed list.

## 12. Complete Phase Execution Playbook

### Primary question

```text
How does each phase proceed operationally from validated inputs to accepted handoff?
```

### Contains

- entry conditions;
- ordered execution steps;
- participating layer orchestration;
- input loading and output writing;
- gate sequence;
- repair, rollback, and re-entry behavior;
- failure, blocked, and diagnostic-only handling;
- phase analysis handoff;
- Layer 0, Evidence Map, and Layer 10 closure sequence;
- exit checklist.

### Produces

- repeatable phase procedure;
- phase operational audit trail;
- required handoff package.

### Must not contain

- first-time method selection;
- detailed formulas owned by Nuts-and-Bolts;
- exact code layout;
- post-hoc scientific rules.

### Example

A stress phase may require loading a validated clean source bundle and accepted stress profile, creating clean/stressed pairs, validating matching, executing the registered analysis, producing the phase report, applying Layer 0, updating the Evidence Map, and then producing Layer 10 outputs.

## 13. Integrated Layers 0–10 Method Selection and Design Rationale Register

### Primary question

```text
Which concrete methods, datasets, technologies, platforms, strategies, and design options are selected, and why?
```

### Contains

- decision IDs and questions;
- candidates and alternatives;
- literature and technical evidence;
- accepted, rejected, deferred, diagnostic-only, stretch, and future-work options;
- selection rationale;
- architecture and Registry compatibility;
- phase and ablation implications;
- implementation feasibility;
- Layer 0 and Layer 10 consequences;
- required controlled Registry revisions;
- Nuts-and-Bolts handoff.

### Produces

- accepted concrete choices;
- rejected-alternative rationale;
- design obligations;
- Protocol v1.0 inputs;
- documented requests for direct Registry revision when necessary.

### Must not contain

- final formulas or pseudocode;
- final class/file/command design;
- empirical claims.

### Differentiated layer treatment

- Layer 0 selects evidence-governance and claim-audit mechanisms.
- Layers 1–6 select scientific methods, data strategies, models, metrics, and policy strategies.
- Layer 7 selects sequential simulation and policy-evaluation designs.
- Layer 8 selects stress and robustness methodologies.
- Layer 9 selects simulation platforms, mappings, safety gates, and outcome measures.
- Layer 10 selects provenance, dashboard, card, export, and reproducibility technologies.

## 14. Integrated Layers 0–10 Detailed Design / Nuts-and-Bolts Specification

### Primary question

```text
Given the accepted decisions, how exactly do modules, algorithms, validators, transformations, and evidence-writing paths work internally?
```

### Contains

- input/output contracts;
- internal flows;
- function-level responsibilities;
- formulas and computation rules;
- pseudocode;
- state/action/transition definitions;
- feature engineering;
- invariants and validators;
- failure and fallback behavior;
- diagnostic-only propagation;
- lineage and record writing;
- configuration semantics;
- Layer 0, Evidence Map, and Layer 10 hooks;
- implementation handoff.

### Produces

- implementation-neutral technical design;
- testable invariants;
- algorithm and validator specification;
- Build Book obligations.

### Must not contain

- first-time method selection;
- unregistered record names;
- final repository layout;
- empirical results;
- final claims.

### Differentiated depth

- Layer 0: evidence sufficiency, downgrade, wording, and audit logic;
- Layers 1–6: scientific and algorithmic design;
- Layer 7: environment, session, transition, reward, and policy-evaluation design;
- Layer 8: stress engine, schedules, injection, and matching;
- Layer 9: command mapping, simulator adapters, safety gates, and outcomes;
- Layer 10: read-only ingestion, provenance, cards, dashboards, and reproducibility.

## 15. Implementation Build Book

### Primary question

```text
How are the accepted designs converted into reusable software, phase configurations, execution commands, tests, evidence gates, and reproducible runs?
```

### Contains

- repository and package structure;
- reusable layer modules;
- phase-specific configuration profiles;
- classes, functions, interfaces, and adapters;
- environment and dependency specifications;
- Kaggle/local/other compute profiles;
- GitHub and Hugging Face synchronization;
- CLI and notebook entry points;
- real-run and conditional smoke-test modes;
- automated and semantic evidence gates;
- repair and rerun behavior;
- expected records, artifacts, manifests, and paths;
- optional branches and activation conditions;
- rollback, invalidation, and reproduction instructions.

### Produces

- code-ready implementation plan;
- reusable layer work packages;
- phase execution recipes;
- test and evidence-gate plan;
- artifact-storage and publication handoff.

### Must not contain

- hidden scientific choices;
- architecture redesign;
- silent schema changes;
- post-hoc claim interpretation.

### Fundamental V4 implementation rule

A layer is implemented as a **general reusable capability** with stable interfaces and configurable phase profiles. It must not be hard-coded so narrowly to one phase that every later phase must rebuild it. Phase-specific behavior belongs in configuration, orchestration, adapters, or clearly versioned extensions unless the scientific method itself genuinely changes.

## 16. Experiment, Ablation, and Evaluation Protocol v1.0

### Primary question

```text
What exact runs, conditions, variants, seeds, metrics, comparisons, and analyses govern the evidence status of this phase and the final project?
```

### Contains

- exact A0–A13 and sub-ablation cells;
- dataset-to-ablation mapping;
- exact model, calibration, policy, stress, and embodiment configurations;
- seeds, run counts, budgets, and resource limits;
- exact metrics, estimands, summaries, intervals, and statistical analyses;
- matched-comparison keys;
- clean/stressed and simulation/embodiment matrices;
- invalid, blocked, diagnostic-only, and exclusion rules;
- rerun and amendment policy;
- phase annex status and relation to the project-wide protocol.

### Produces

- registered experiment and analysis contract;
- exact evidence-generation matrix;
- scientific status for runs and analyses.

### Must not contain

- implementation code;
- observed conclusions;
- silent post-hoc changes.

### V4 timing modes

The future orchestration prompt must allow the project owner to select one of these modes at the beginning of a phase:

#### Mode A — Protocol-before-claim-bearing-run

The applicable Protocol v1.0 phase annex is frozen after implementation feasibility is understood and before the official run. This is the preferred route for confirmatory or thesis-bearing evidence.

#### Mode B — Direct operational run before final Protocol annex

The real run is executed first to prove functionality, obtain artifacts, or support downstream implementation. A Protocol annex may then be completed for future layers or later phases. The already observed run remains engineering, exploratory, or retrospective evidence unless its rules had been independently fixed beforehand. It must be rerun under a frozen Protocol if confirmatory status is later required.

#### Mode C — Provisional pre-run annex with post-run administrative completion

All scientific choices, comparisons, metrics, and exclusion rules are frozen before execution, while non-scientific metadata or resource fields are completed afterward. This may retain confirmatory status if no result-contingent scientific rule changes occur.

A successful real run does not eliminate Protocol v1.0. It may reduce the need for an earlier feasibility-only protocol draft, but every claim-bearing comparison still requires an auditable analysis contract.

## 17. Paper and Thesis Evidence Map

### Primary question

```text
Which reviewed claims, figures, tables, cards, limitations, and manuscript sections are supported by which exact evidence?
```

### Contains

- candidate and Layer 0–reviewed claim IDs;
- claim-to-record, run, phase, and ablation mapping;
- figure, table, card, and dashboard mapping;
- allowed and prohibited wording;
- required public-data, simulation-only, stress-only, or embodiment-proxy limitations;
- negative-result handling;
- paper/thesis section placement;
- appendix and reproduction mapping;
- per-phase evidence-map annexes merged into one project-wide map.

### Produces

- claim-evidence-manuscript matrix;
- figure/table/card plan;
- limitation and wording control;
- input specification for Layer 10 publication outputs.

### Must not contain

- new methods;
- new experiments;
- unsupported interpretations;
- stronger claims than Layer 0 permits.

### V4 ordering rule

For each phase, the Evidence Map is updated **after the Phase Evidence Report and Layer 0 claim review, but before final Layer 10 publication packaging**. This ensures Layer 10 knows exactly which reviewed claims, evidence links, limitations, figures, tables, and cards it is authorized to render.

## 18. Phase Evidence, Results, and Interpretation Report

### Primary question

```text
What did this phase actually execute, produce, fail to produce, and scientifically show?
```

### Contains

- phase scope and objectives;
- exact authority, source commit, environment, config, and Protocol identities;
- required and produced artifacts;
- included, failed, blocked, excluded, unmatched, and invalid runs;
- data-quality and evidence-gate results;
- registered or explicitly exploratory analyses;
- metrics, comparisons, intervals, and ablations;
- charts and figure-source data;
- improvements, degradations, null effects, and tradeoffs;
- direct findings;
- supported interpretations;
- mechanism hypotheses explicitly labelled as hypotheses;
- candidate claims;
- limitations and unresolved questions;
- downstream readiness;
- inputs prepared for Layer 0, Evidence Map, and Layer 10.

### Must not contain

- hidden changes to Protocol rules;
- silently discarded negative results;
- claims treated as approved before Layer 0 review.

### Interpretation hierarchy

```text
Measured result
→ supported interpretation
→ candidate claim
→ mechanism hypothesis, where justified and clearly labelled
```

A metric improvement does not automatically prove its proposed mechanism.

## 19. Final Cross-Phase Results Synthesis Report

### Primary question

```text
What does the complete, reviewed body of phase evidence jointly establish?
```

### Contains

- contribution-level evidence;
- cross-phase consistency and contradiction;
- interactions among calibration, IHARQ, temporal trust, policy, stress, and embodiment;
- negative and null findings;
- scope limitations;
- unresolved evidence gaps;
- final candidate contribution claims;
- final figure/table priorities;
- links to all Phase Reports, Layer 0 dispositions, Evidence Map entries, and Layer 10 releases.

It synthesizes evidence but does not retroactively alter phase measurements or registered analyses.

---

# Part IV — Differentiated layer treatment

## 20. General rule

A layer requires Method Selection coverage when alternatives could materially change scientific validity, software behavior, evidence interpretation, reproducibility, downstream interfaces, ablation conclusions, claim limits, or implementation feasibility.

A layer requires Nuts-and-Bolts coverage when it contains executable, rule-based, auditable, or reproducibility-critical behavior that must not be improvised in code.

All Layers 0–10 require coverage, but not identical forms.

## 21. Layer coverage matrix

| Layer | Selection character | Method Selection | Nuts-and-Bolts | Typical implementation behavior |
|---|---|---:|---:|---|
| 0 | claim safety, evidence sufficiency, wording, downgrade | specialized | specialized/full | continuous audit and final claim disposition |
| 1 | data, labels, splits, windows, preprocessing | full | full | highly reusable source artifacts |
| 2 | decoder portfolio, controls, normalization | full | full | reusable checkpoints and predictions by identity |
| 3 | calibration, uncertainty, selective prediction | full | full | derived calibration/uncertainty artifacts |
| 4 | IHARQ evidence, rules, reasons, fallback | full | full | reusable decision traces where configs match |
| 5 | temporal features, trust, regime logic, stop-loss | full | full | sequence-dependent derived evidence |
| 6 | evidence quality, policy, deferral, cost learning | full | full | often mode- and policy-specific execution |
| 7 | state/action/transition/reward/session | full | full | stateful trajectory execution |
| 8 | stress taxonomy, schedules, injection, matching | full | full | reusable profiles; new outputs per application condition |
| 9 | simulator, mapping, safety gate, outcomes | integration-oriented full | full | branch/platform/task-specific execution |
| 10 | dashboard, cards, provenance, exports | engineering-oriented full | full | read-only derived presentation packages |

## 22. Layer 0 treatment

Layer 0 governs:

- claim taxonomy;
- evidence sufficiency;
- confirmatory versus exploratory versus diagnostic status;
- public-data, simulation-only, stress-only, and embodiment-proxy tags;
- negative-result propagation;
- allowed and prohibited wording;
- manual, rule-based, and LLM-assisted review boundaries;
- claim-to-artifact traceability;
- final approval, qualification, downgrade, or block.

Layer 0 does not change measurements, normalize inconvenient results, manufacture support, or rerun scientific layers.

## 23. Layers 7–9 treatment

Layer 7, Layer 8, and Layer 9 remain full scientific/software method layers:

- Layer 7 owns stateful sequential evaluation and therefore often requires new trajectories when policies, actions, environments, or seeds change.
- Layer 8 permits reuse of accepted stress definitions but requires new derived artifacts when source, intensity, schedule, seed, injection point, or target changes.
- Layer 9 permits reuse of adapters, mappings, and branch definitions but requires a new execution when platform, task, asset, command mapping, seed, or embodiment condition changes.

## 24. Layer 10 treatment

Layer 10 is scientific infrastructure, not cosmetic presentation. It owns:

- validated evidence ingestion;
- provenance and lineage rendering;
- dashboards and cards;
- ablation and matched-comparison views;
- figure and table exports;
- negative-result visibility;
- claim-evidence display;
- reproduction manifests and release packages;
- read-only enforcement.

Layer 10 must consume the reviewed Evidence Map for the phase before creating final claim-bearing views.

---

# Part V — Phase-oriented post-design operating model

## 25. Governing principle

After the seven core documents are complete, work proceeds **phase by phase**, while implementation remains **layer-owned, reusable, and configuration-driven**.

```text
phase chooses what evidence must be produced;
layer work packages provide reusable capabilities;
phase configs bind those capabilities to the current phase;
artifacts are reused by identity when lawful;
only missing or changed capabilities are implemented or rerun.
```

## 26. Why this is not redundant layer creation

When Phase B needs Layer 1 outputs already accepted in Phase A, Phase B references the existing immutable Layer 1 artifact IDs and hashes. It does not recreate Layer 1.

When Phase B needs the same Layer 2 implementation but a new model variant, it reuses the Layer 2 code and interface while executing a new configuration.

When Phase B needs a genuinely new Layer 2 scientific method, the Method Selection/Nuts-and-Bolts/Build Book chain must be versioned for that extension.

## 27. Phase-start declaration

The future orchestration prompt must begin with a structured phase declaration containing at least:

```text
target_phase
phase_objective
execution_mode
protocol_timing_mode
available_compute
artifact_repositories
completed_phases
implemented_layers
validated_layer_versions
available_phase_reports
available_protocol_annexes
available_evidence_map_annexes
available_layer0_dispositions
available_layer10_packages
known_failures_or_invalidations
```

The project owner must be able to state exactly which phases, layers, artifacts, and analysis packages already exist.

## 28. Required input sources for phase planning

The future orchestration process must inspect:

1. all seven core authority documents;
2. the current Build Book and relevant work packages, if any;
3. the current Protocol v1.0 and phase annexes, if any;
4. previous Phase Evidence Reports;
5. previous Layer 0 dispositions;
6. the master Evidence Map and phase annexes;
7. previous Layer 10 packages;
8. repository manifests, run bundles, code, configs, and tests;
9. GitHub/Hugging Face artifact identities and exact revisions;
10. known invalidations, supersessions, failures, and unresolved dependencies.

It must not rely on an LLM's memory when a versioned source is available.

## 29. Phase dependency and reuse analysis

Before generating any implementation work, the orchestrator must determine:

- which layers the target phase requires;
- which required capabilities already exist;
- which exact artifacts are reusable;
- whether reused artifacts match dataset, split, method, config, seed, Protocol role, evidence mode, and validity requirements;
- which new phase configs are required;
- which layers need only execution;
- which layers require implementation extension;
- which layers require a scientifically new run;
- which upstream changes invalidate descendants;
- the lawful execution order;
- the phase's analysis, Layer 0, Evidence Map, and Layer 10 closure obligations.

## 30. Sequential layer-work-package plan

For every necessary nonredundant layer, the orchestrator should define a sequential work package. The sequence must respect producer-consumer dependencies.

Example:

```text
Layer 1 already accepted and reusable
→ Layer 2 implementation/execution work package consumes Layer 1 artifacts
→ Layer 3 work package consumes accepted Layer 1 and newly accepted Layer 2 artifacts
→ phase-level execution and analysis closes after Layer 3
```

The future orchestrator may generate separate prompts for these work packages, but V4 defines only their required architecture, not their final wording.

---

# Part VI — Future prompt-system specification without writing the prompts

## 31. Master phase-orchestrator prompt purpose

The future master prompt must:

- accept the target phase and execution-state declaration;
- inspect all supplied authorities and repositories;
- identify missing, reusable, stale, invalid, or phase-specific capabilities;
- produce the lawful phase plan;
- identify the exact sequence of required layer prompts;
- avoid redundant layer implementation and artifact generation;
- require general reusable implementations with phase-specific configs;
- specify real-run, optional smoke, evidence-gate, repair, analysis, Layer 0, Evidence Map, and Layer 10 obligations;
- produce explicit handoff requirements between sequential layer prompts.

It must not directly assume that every required layer needs to be rebuilt.

## 32. Required output of the phase-orchestrator prompt

The orchestrator's output should include:

1. authority and repository intake audit;
2. target-phase interpretation;
3. phase entry readiness;
4. layer dependency graph;
5. reusable-artifact table;
6. rerun/extension/implementation decision for every required layer;
7. exact sequential work-package order;
8. per-layer prompt specifications;
9. execution-mode and Protocol-timing decision;
10. evidence-gate requirements;
11. phase-analysis specification;
12. Layer 0 review specification;
13. Evidence Map update specification;
14. Layer 10 publication/reproducibility specification;
15. downstream phase handoff;
16. unresolved issues and lawful owner decisions.

## 33. Per-layer implementation/execution prompt requirements

Every future layer prompt must state:

- target phase and layer;
- authority sources and exact versions;
- reusable upstream artifacts and how to resolve them;
- layer responsibilities and non-authorities;
- general reusable implementation scope;
- current phase-specific configuration profile;
- optional capabilities and activation conditions;
- repository/module/class/function/config design;
- environment and dependency requirements;
- Kaggle/local execution profile;
- GitHub/Hugging Face input/output behavior;
- direct real-run command and expected outputs;
- conditional smoke-test mode;
- deterministic and semantic evidence gates;
- repair loop and defect routing;
- immutable artifact and handoff package;
- downstream consumer contract.

## 34. Reusability requirement for every layer prompt

A layer prompt must not ask for a one-off script whose scientific and software behavior is inseparable from the current phase. It should request:

```text
stable reusable core
+ explicit interfaces
+ configuration schema
+ phase profile
+ adapters where necessary
+ versioned optional extensions
+ tests and evidence gates
```

The current phase should be executable by selecting its profile, while later phases can reuse the same core by changing lawful configuration or invoking a documented extension.

## 35. Sequential handoff requirement

At the end of Layer N, the prompt must require a machine-readable handoff containing:

- implementation version;
- source commit;
- environment identity;
- config identity;
- input artifact IDs;
- output artifact IDs and hashes;
- validity and evidence status;
- tests and gate decisions;
- limitations and failures;
- downstream compatibility;
- exact instructions for Layer N+1.

The next prompt consumes the handoff by reference rather than reconstructing it from prose.

---

# Part VII — Real-run-first implementation and conditional smoke testing

## 36. Default execution policy

V4 adopts **real-run-first** as the default:

```text
complete the lawful implementation work package
→ execute the intended phase run directly
→ validate outputs
→ apply the evidence gate
→ repair and rerun until accepted or lawfully blocked
```

The implementation specification must nevertheless include a bounded smoke-test path so that it can be activated when needed without redesigning the software.

## 37. What “real run” means

A real run uses the intended data path, methods, configurations, outputs, storage, and downstream interfaces for the phase. It is not a toy fixture.

However, a real run can have different scientific status:

- operational/engineering real run;
- exploratory real run;
- registered diagnostic real run;
- confirmatory production real run.

Its status depends on Protocol timing, frozen rules, data use, validity, and evidence gates—not merely on execution scale.

## 38. When smoke testing is optional

A smoke test may be skipped when:

- the reusable implementation already passed relevant gates;
- the new phase changes only a well-validated configuration;
- compute and failure costs are modest;
- execution is reversible and non-destructive;
- upstream/downstream interfaces are stable;
- the direct run provides sufficiently localized diagnostics;
- no new simulator, stressor, policy-update mode, or high-risk branch is introduced.

## 39. When smoke testing should be activated

Use a smoke test before or after an unsuccessful direct run when:

- the full run is expensive or lengthy;
- failure diagnosis would otherwise be ambiguous;
- a new dependency, device, simulator, model family, or environment is introduced;
- stateful trajectories make late failure costly;
- a schema/interface changed;
- data leakage or split errors are plausible;
- destructive overwrite or irreversible publication is possible;
- the direct run failed and the fault must be isolated;
- optional branches have not been validated;
- human safety, privacy, licensing, or restricted-data concerns exist.

## 40. Conditional smoke-test design

The Build Book must specify for every layer:

- minimal valid fixture;
- malformed and negative fixtures;
- expected outputs;
- pass/fail criteria;
- downstream contract test;
- resource ceiling;
- exact relationship between smoke evidence and real-run evidence.

Skipping a smoke test never means skipping validation, evidence gates, or failure recording.

## 41. Real-run evidence gate

Every real run must produce and pass, as applicable:

- authority and configuration resolution;
- schema and lineage validation;
- data split, leakage, chronology, and matching checks;
- environment and dependency capture;
- required artifact closure;
- negative, null, failed, blocked, unmatched, and invalid outcome preservation;
- deterministic checks;
- semantic cross-document audit;
- human/owner decisions where scientific authority is implicated;
- immutable upload and repository pointer publication.

## 42. Repair loop

```text
run
→ machine gate
→ semantic audit
→ lawful owner disposition where required
→ route defect to code, Build Book, Nuts-and-Bolts, Method Selection, Registry, Plan, Playbook, Protocol, Layer 0, Evidence Map, or Layer 10
→ repair only the owning surface
→ invalidate affected descendants
→ rerun affected scope
→ repeat until pass, diagnostic-only acceptance, deferral, or lawful block
```

An LLM may recommend repairs but may not override deterministic failure or scientific authority.

---

# Part VIII — Protocol v1.0 creation within the phase loop

## 43. Protocol prompt selection at phase start

The future orchestration prompt must record:

```text
protocol_timing_mode = A | B | C
```

It must explain the consequences of the selected mode and generate the Protocol v1.0 phase-annex task at the correct point.

## 44. Mode A workflow

```text
implementation ready
→ optional smoke/feasibility evidence
→ freeze phase Protocol annex
→ run claim-bearing production execution
→ registered analysis
```

Use for final ablations, paper claims, thesis tables, and comparisons where confirmatory status matters.

## 45. Mode B workflow

```text
implementation ready
→ direct operational real run
→ evidence gate
→ use artifacts for engineering/downstream development
→ write Protocol annex for future claim-bearing execution
→ rerun later if confirmatory status is required
```

The first run may still be valuable and fully reproducible, but it must be labelled exploratory, engineering, or retrospective when the analysis rules were finalized after observing it.

## 46. Mode C workflow

```text
freeze scientific questions, comparisons, metrics, exclusions, and analysis
→ execute real run
→ complete non-scientific resource and administrative fields
→ verify no result-contingent scientific changes
```

## 47. Protocol annex organization

The project may store:

```text
protocol_v1_0/
    master_protocol.md
    phases/
        phase_01_annex.md
        phase_02_annex.md
        ...
    machine_readable/
        run_matrix.yaml
        analysis_contract.yaml
```

Each phase annex remains part of one coherent Protocol v1.0 authority.

---

# Part IX — Phase execution, analysis, claim review, Evidence Map, and Layer 10 closure

## 48. Complete phase loop

For every target phase:

```text
1. Declare target phase and current execution state.
2. Inspect seven core authorities and all prior governed evidence.
3. Resolve required layers and reusable artifacts.
4. Define sequential nonredundant layer work packages.
5. Implement or extend reusable layer capabilities.
6. Execute direct real runs by default; activate smoke tests when justified.
7. Apply evidence gates and repair loops per layer.
8. Complete all layer outputs required by the phase.
9. Execute the phase-level orchestration and final evidence gate.
10. Run the registered or explicitly exploratory phase analysis.
11. Create the Phase Evidence, Results, and Interpretation Report.
12. Apply Layer 0 claim and limitation review.
13. Update the phase annex of the Paper and Thesis Evidence Map.
14. Apply Layer 10 to produce reproducibility, dashboard, cards, figures, tables, and exports.
15. Publish immutable artifacts and pointers to GitHub/Hugging Face.
16. Issue the downstream handoff and proceed to the next phase.
```

## 49. Why phase analysis is a separate evidence product

Protocol v1.0 defines **what analysis must be performed**. The Build Book defines **how the analysis code runs**. The Playbook defines **when it runs**. The Execution Plan defines **which outputs must exist**. The Phase Evidence Report records **what the analysis found**.

No one of these objects replaces the others.

## 50. Required phase-analysis depth

The Phase Evidence Report should rigorously analyze:

- all unlocked and executed ablations;
- registered baselines and matched comparisons;
- primary and secondary metrics;
- uncertainty and confidence intervals;
- subgroup, robustness, temporal, policy, stress, or embodiment analyses where applicable;
- charts, tables, distributions, and failure patterns;
- improvements, degradations, tradeoffs, and null effects;
- unexpected behavior;
- data quality and missingness;
- negative, invalid, unmatched, blocked, or simulator-invalid results;
- sensitivity and stability;
- practical and scientific meaning;
- downstream implications;
- candidate claims and explicit limitations;
- plausible mechanisms clearly distinguished from demonstrated mechanisms.

## 51. Claim creation lifecycle

```text
registered or explicitly exploratory analysis produces a finding
→ Phase Evidence Report formulates candidate claim
→ Layer 0 checks evidence sufficiency, status, scope, and wording
→ Layer 0 approves, qualifies, downgrades, or blocks
→ Evidence Map records the reviewed claim and exact support
→ Layer 10 renders only the authorized claim-bearing presentation
→ paper/thesis uses the mapped wording and evidence
```

## 52. Example

Suppose the phase finds:

- mean ECE falls from 0.118 to 0.071;
- NLL improves;
- accuracy remains comparable;
- all matched seeds are valid;
- one subgroup benefits less.

The Phase Evidence Report may create:

```text
Candidate claim:
Temperature scaling improved calibration while preserving comparable accuracy.
```

Layer 0 may approve:

```text
Under the registered subject-independent evaluation on Dataset X,
temperature scaling reduced calibration error while preserving comparable classification accuracy;
the improvement was weaker in subgroup Y.
```

The Evidence Map then links the reviewed claim to exact runs, records, comparison IDs, table, figure, limitations, and thesis section. Layer 10 subsequently renders the reviewed table, figure, result card, dashboard view, and reproduction package.

## 53. Layer 0 phase disposition record

For each candidate claim, store:

- claim ID;
- source finding IDs;
- evidence status;
- sufficiency result;
- approved wording;
- mandatory qualifiers;
- blocked wording;
- limitation tags;
- negative-result obligations;
- reviewer/model/human provenance;
- decision timestamp and authority version.

## 54. Per-phase Evidence Map annex

Each completed phase should produce or update:

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

These annexes are merged into one project-wide Evidence Map.

## 55. Layer 10 phase package

After the Evidence Map annex is updated, Layer 10 creates:

- validated evidence inventory;
- phase dashboard and status view;
- model/data/result cards where applicable;
- registered tables and plots;
- ablation and matched-comparison views;
- negative-result panels;
- claim-evidence lineage views;
- static exports;
- reproduction manifest;
- release metadata;
- warnings and diagnostic-only visibility.

Layer 10 may aggregate only according to authorized analysis rules and must not repair, retune, rerun, or strengthen evidence.

---

# Part X — Artifact reuse, derivation, rerun, and invalidation

## 56. Reuse-by-identity rule

The exact same artifact should be reused by multiple phases when its scientific identity is unchanged.

Reuse requires matching, as relevant:

- source data and generation;
- split and preprocessing;
- model/method version;
- semantic config hash;
- seed;
- Protocol role;
- evidence mode;
- validity status;
- limitation tags;
- lineage;
- non-superseded status.

Both phases reference the same artifact ID and hash rather than copying or regenerating it.

## 57. Derived-artifact rule

When the source artifact remains valid but a new phase performs a new lawful analysis or transformation, create a new derived artifact pointing to the unchanged source.

Example:

```text
Layer 2 PredictionBundle
    ├── Layer 3 CalibrationBundle
    ├── Layer 4 IHARQDecisionBundle
    └── later evaluation release
```

## 58. Rerun rule

Rerun only the affected capability when the new phase changes a scientific condition such as:

- dataset, split, preprocessing, or window;
- model or method;
- seed required by the Protocol;
- calibration or policy mode;
- environment, state transition, or trajectory;
- stress profile application, intensity, schedule, or injection point;
- simulator platform, task, asset, or command mapping;
- adaptation/update state;
- evidence mode;
- invalidated upstream authority or artifact.

## 59. Layer-specific reuse tendencies

- Layer 1 artifacts are usually reused broadly when source identity is unchanged.
- Layer 2 checkpoints and predictions are reusable across downstream calibration and IHARQ phases.
- Layers 3–5 outputs are reusable when method, source, split, config, and temporal identity match.
- Layer 6 outputs are often policy-mode and budget specific.
- Layer 7 trajectories usually require new execution when policy, state, action, environment, reward, seed, or stress changes.
- Layer 8 profiles are reusable; stressed outputs are application-specific.
- Layer 9 adapter definitions are reusable; branch trajectories are platform/task/config specific.
- Layer 10 can create several views from one accepted evidence package without rerunning science.
- Layer 0 can review several claims against one evidence package without changing measurements.

## 60. Invalidation and topological regeneration

When an upstream source is corrected or superseded:

1. identify the invalidation root;
2. traverse downstream lineage;
3. mark affected descendants stale or invalid;
4. preserve prior evidence rather than deleting it;
5. regenerate only affected descendants in dependency order;
6. issue new artifact and analysis release IDs;
7. update Layer 0 dispositions, Evidence Map entries, and Layer 10 packages.

---

# Part XI — GitHub, Kaggle, Hugging Face, notebooks, and storage

## 61. GitHub as control plane

GitHub should store:

- all authority documents and phase annexes;
- Build Book and Protocol machine-readable configs;
- code, tests, workflows, and notebooks;
- small fixtures;
- manifests and artifact pointers;
- issues, decisions, review history, and pull requests;
- small reports and summaries;
- release tags and version metadata.

Large raw results and checkpoints should generally not be committed to ordinary Git history.

## 62. Kaggle or equivalent as compute plane

Kaggle may execute:

- notebook-based implementation and runs;
- training and evaluation;
- sweeps and ablations;
- simulator and stress jobs;
- phase analysis pipelines;
- bundle generation.

Every run must resolve exact GitHub code and exact Hugging Face/input revisions, then write a complete immutable run bundle.

## 63. Hugging Face or equivalent as artifact/publication plane

Use versioned artifact repositories for:

- checkpoints and models;
- derived datasets;
- structured run bundles;
- large records and outputs;
- phase analysis releases;
- reproduction packages;
- cards and release assets;
- optional Layer 10 Space or static dashboard assets.

## 64. Synchronization workflow

```text
Kaggle loads exact GitHub commit and artifact revisions
→ executes run
→ builds manifests and hashes
→ uploads large artifacts to Hugging Face
→ commits small pointer manifest and report to GitHub
→ evidence gate inspects exact revisions
→ phase analysis consumes governed bundles
→ Layer 0/Evidence Map/Layer 10 packages publish new governed revisions
```

## 65. Notebook policy

Notebooks are permitted for interactive execution and diagnosis, but authority-bearing logic should live in importable, testable modules.

A professional notebook should:

- run from a clean state;
- load frozen configs;
- import project packages;
- avoid hidden cell-order state;
- save complete manifests and bundles;
- support direct real run and conditional smoke mode;
- expose errors without silently repairing results.

## 66. Canonical storage model

```text
runs/<run_id>/
    authority_manifest.json
    environment_manifest.json
    config_snapshot/
    inputs/
    records/
    raw_outputs/
    metrics/
    diagnostics/
    logs/
    checkpoints/
    manifests/
    layer0_handoff/
    evidence_map_handoff/
    layer10_source_bundle/
    gate_decision.json

evaluations/<evaluation_release_id>/
    protocol_snapshot/
    included_runs.json
    excluded_runs.json
    metric_records/
    matched_comparisons/
    ablation_tables/
    statistical_results/
    negative_results/
    diagnostic_only_results/
    figure_source_data/
    table_source_data/
    phase_report/
    layer0_disposition/
    evidence_map_annex/
    layer10_package/
    reproducibility_manifest.json
```

Raw outputs remain immutable. Revised analysis creates a new evaluation release.

## 67. Minimum run bundle

```text
run_manifest.json
authority_manifest.json
environment_manifest.json
config_snapshot/
input_manifest.json
output_manifest.json
test_report.json, when tests execute
validation_report.json
negative_test_report.json, when applicable
resource_profile.json
logs/
records/
artifacts/
layer0_handoff/
evidence_map_handoff/
layer10_source_bundle/
gate_decision.json
```

## 68. Secrets, licensing, and access

- never commit tokens or credentials;
- use repository and compute secrets;
- record dataset and model licenses;
- separate public, private, and restricted artifacts;
- publish only artifacts whose redistribution is lawful;
- preserve access requirements in reproduction manifests;
- do not weaken privacy or licensing controls to simplify LLM access.

---

# Part XII — Exact order from the current project stage

## 69. Stage 1 — Prepare the phase-oriented control system

1. establish the repository structure and current-source manifest;
2. create the master Build Book skeleton with reusable layer work packages and phase profiles;
3. define evidence gates, repair routing, and bundle schemas;
4. create Protocol v1.0 master skeleton and phase-annex template;
5. create Paper and Thesis Evidence Map master skeleton and phase-annex template;
6. create Phase Evidence Report, Layer 0 disposition, and Layer 10 package templates;
7. establish GitHub, Kaggle, Hugging Face, secrets, and release conventions.

## 70. Stage 2 — Select the first target phase

1. declare the target phase;
2. declare completed phases, implemented layers, valid artifacts, prior reports, Protocol annexes, Evidence Map annexes, and Layer 10 packages;
3. inspect the seven core authorities and repositories;
4. determine reuse, rerun, extension, and implementation needs;
5. generate the sequential layer-work-package plan.

## 71. Stage 3 — Execute required layer work packages

For each required nonredundant layer:

1. create or update its Build Book work package;
2. preserve general reusable implementation;
3. add the current phase profile;
4. execute the real run directly by default;
5. activate smoke testing where justified;
6. apply the evidence gate;
7. repair and rerun affected scope;
8. publish the accepted handoff;
9. proceed to the next dependent layer.

## 72. Stage 4 — Resolve Protocol timing and execute the phase

- Mode A: freeze the phase annex before the claim-bearing run;
- Mode B: execute operationally first, then create the annex for later claim-bearing use;
- Mode C: freeze scientific rules before the run and complete non-scientific fields afterward.

Then execute the complete phase orchestration and preserve every valid, invalid, negative, blocked, unmatched, and failed outcome.

## 73. Stage 5 — Analyze and close the phase

1. run the registered or explicitly exploratory analysis;
2. create the Phase Evidence, Results, and Interpretation Report;
3. create candidate claims and mechanism hypotheses with proper status;
4. apply Layer 0 claim and limitation review;
5. update the Paper and Thesis Evidence Map phase annex;
6. apply Layer 10 to create the reproducibility and presentation package;
7. publish exact artifacts and pointers;
8. issue downstream readiness and invalidation information.

## 74. Stage 6 — Repeat for later phases

The next phase receives:

- all seven core authorities;
- current Build Book;
- Protocol v1.0 and completed annexes;
- previous Phase Reports;
- Layer 0 dispositions;
- Evidence Map annexes;
- Layer 10 packages;
- exact GitHub/Hugging Face artifacts and revisions;
- reuse and invalidation state.

It reuses valid implementations and artifacts and creates only the missing or scientifically changed scope.

## 75. Stage 7 — Final synthesis and release

1. complete all required phases and analyses;
2. create the Final Cross-Phase Results Synthesis Report;
3. perform final Layer 0 review across contribution-level claims;
4. consolidate the project-wide Evidence Map;
5. generate final Layer 10 dashboard, cards, figures, tables, and reproduction package;
6. execute clean reproduction;
7. reconcile hashes and expected numerical tolerances;
8. release and archive exact documents, code, Protocol, evidence, and manuscript links;
9. freeze the final project state.

---

# Part XIII — Worked examples

## 76. Example A — Phase reuses an earlier layer artifact

Assume Phase A produced a validated Layer 1 dataset/split bundle:

```text
artifact_id: L1-DATA-004
split_id: SUBJECT-INDEPENDENT-V2
config_hash: 8c...91
artifact_hash: 2a...ef
validity: ACCEPTED
```

Phase B requires the same data and split. It records `L1-DATA-004` as an input and does not rerun Layer 1.

Phase B then implements or executes Layer 2 using that bundle and publishes:

```text
artifact_id: L2-PRED-011
source_artifact_id: L1-DATA-004
model_profile: BASELINE-CNN-V1
seed: 3
validity: ACCEPTED
```

A later calibration phase and IHARQ phase can both reuse `L2-PRED-011` if the exact source prediction identity is lawful for their Protocol cells.

## 77. Example B — Same implementation, new phase configuration

Layer 8 stress injection code is already accepted. Phase A used:

```text
stress_profile: DROPOUT-LOW
seed: 1
injection_point: decoder_output
```

Phase B requires:

```text
stress_profile: DROPOUT-HIGH
seed: 4
injection_point: decoder_output
```

The Layer 8 implementation is reused. A new phase config and stressed artifact are created. The layer is not reimplemented.

## 78. Example C — Real run first, Protocol afterward

A new simulator adapter is implemented and executed directly to determine whether the environment can instantiate and emit the required records. The run passes the evidence gate and is saved reproducibly.

Because the exact comparison and outcome-analysis rules were completed afterward, the run is labelled:

```text
engineering/feasibility evidence
```

It may support statements about successful bounded execution, but not a pre-registered comparative claim. If the project later wants a claim-bearing A13 comparison, it freezes the relevant Protocol annex and reruns the required cells.

## 79. Example D — Full phase closure

For a calibration phase:

```text
reuse Layer 1 data and Layer 2 predictions
→ execute Layer 3 calibration under phase profile
→ pass real-run evidence gate
→ run registered metrics and matched analysis
→ write Phase Calibration Evidence Report
→ Layer 0 qualifies the candidate claim
→ update Evidence Map with exact runs, table, figure, and thesis section
→ Layer 10 renders calibration card, curves, table, dashboard, and reproduction manifest
→ publish GitHub pointer and Hugging Face evaluation release
```

---

# Part XIV — Change control and quality assurance

## 80. Routing newly discovered requirements

| Discovery | Owning destination |
|---|---|
| new layer/module responsibility | Architecture, only if genuinely architectural |
| new/changed record, field, status, or interface | new controlled Registry revision with migration and propagation notes |
| new phase obligation, gate, or output | Execution and Evidence Plan |
| changed phase procedure or handoff | Phase Execution Playbook |
| new method/platform/technology choice | Method Selection Register |
| new algorithm, formula, validator, or failure rule | Nuts-and-Bolts |
| new file, class, config, command, environment, test, or repository behavior | Implementation Build Book |
| new comparison, metric, matching, exclusion, or statistical rule | Protocol v1.0 |
| observed phase finding or candidate interpretation | Phase Evidence Report |
| claim sufficiency, wording, limitation, or block | Layer 0 |
| claim-to-evidence-to-manuscript link | Paper and Thesis Evidence Map |
| view, card, figure, table, provenance, or release package | Layer 10 |

## 81. Direct Registry revision governance

Every accepted Registry change must record:

- triggering issue or decision;
- old and new schema version;
- exact field/interface change;
- compatibility and migration;
- affected artifacts and phases;
- validator and test updates;
- invalidation consequences;
- propagation completion.

This information may live in Registry revision notes, Git commit/PR history, decision records, and migration files. No additional standalone ledger document is required.

## 82. Maturity labels

```text
[SKELETON]
[RESEARCH-IN-PROGRESS]
[CANDIDATE-DECISIONS]
[PROVISIONALLY-SELECTED]
[ACCEPTED]
[DESIGN-COMPLETE]
[IMPLEMENTATION-READY]
[IMPLEMENTED]
[REAL-RUN-EXECUTED]
[SMOKE-VERIFIED]
[EVIDENCE-GATE-PASS]
[EXPLORATORY]
[REGISTERED-DIAGNOSTIC]
[CONFIRMATORY]
[DIAGNOSTIC-ONLY]
[INTERFACE-STABLE]
[PHASE-CLOSED]
[SUPERSEDED]
[INVALIDATED]
[FROZEN]
```

## 83. Document and evidence completeness checklist

Verify that:

1. authority and non-authority are explicit;
2. inputs and outputs use canonical identities;
3. target phase and execution state are declared;
4. prior layer artifacts are reused where lawful;
5. new layer implementations are reusable beyond one phase;
6. phase-specific behavior is configured rather than hard-coded where possible;
7. real-run and conditional smoke paths are documented;
8. evidence gates are explicit;
9. Protocol timing mode and evidence consequences are explicit;
10. negative, null, failed, invalid, blocked, and unmatched outcomes remain visible;
11. Phase Evidence Report separates findings, interpretations, candidate claims, and hypotheses;
12. Layer 0 review precedes Evidence Map claim finalization;
13. Evidence Map update precedes final Layer 10 publication packaging;
14. exact GitHub/Hugging Face revisions are retained;
15. raw evidence remains immutable;
16. invalidation propagates topologically;
17. later phases consume prior handoffs by reference;
18. final claims resolve to exact evidence and limitations.

## 84. Anti-patterns

Avoid:

- rebuilding every required layer for every phase;
- copying artifacts without preserving one canonical identity;
- reusing an artifact for a scientific condition it never represented;
- writing one-off phase scripts where reusable layer capability is possible;
- skipping all validation because smoke testing is optional;
- calling a post-hoc operational run confirmatory;
- finalizing comparison rules after inspecting results and hiding that fact;
- letting an LLM override deterministic gate failure;
- routing every defect to the Build Book;
- allowing implementation convenience to change scientific design silently;
- treating Layer 0 as a result-normalization layer;
- applying Layer 10 before evidence and claims are governed;
- letting Layer 10 recompute or strengthen results;
- creating claims directly from charts without a Phase Evidence Report and Layer 0 disposition;
- maintaining incompatible per-phase Protocol or Evidence Map authorities;
- storing the only copy of evidence in a transient notebook or compute environment;
- overwriting prior runs or analysis releases;
- hiding optional branches rather than implementing and labelling their activation conditions;
- omitting negative and invalid outcomes from publication views.

---

# Part XV — V4 governing summary

## 85. Fundamental operating model

```text
Seven core authorities define the accepted project.
A target phase is declared.
All existing phase and layer state is inspected.
Reusable artifacts and implementations are resolved first.
Only missing or scientifically changed layer work packages are created.
Every layer is implemented as reusable capability plus phase configuration.
The intended real run is attempted directly by default.
Smoke testing remains available and is activated when risk, cost, novelty, or failure diagnosis justifies it.
Every run passes evidence gates and repair loops.
Protocol v1.0 timing is selected explicitly, and evidence status follows that timing.
The phase executes completely.
A rigorous Phase Evidence, Results, and Interpretation Report records what happened.
Layer 0 reviews candidate claims and limitations.
The Paper and Thesis Evidence Map is updated with exact reviewed claim-evidence links.
Layer 10 then creates the authorized reproducibility, dashboard, card, figure, table, and release package.
Artifacts and pointers are versioned through GitHub and Hugging Face, with Kaggle or equivalent providing compute.
The next phase reuses prior valid capabilities and evidence rather than recreating them.
Final cross-phase synthesis, clean reproduction, publication, and freeze occur only after complete lineage is auditable.
```

## 86. Final principle

> Proceed by phase, build by reusable layer capability, reuse by immutable identity, rerun only changed scientific conditions, attempt the intended real execution directly when responsible, use smoke tests as a conditional diagnostic safeguard, distinguish operational evidence from claim-bearing evidence, analyze every phase rigorously, govern claims through Layer 0, map reviewed claims before Layer 10 publication, and preserve the entire project through exact code, configuration, artifact, analysis, and manuscript lineage.
