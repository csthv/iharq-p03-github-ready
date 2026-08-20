# IHARQ BenchGuard Stretch C

**Assessment and Improvement of Reliability in Brain–Computer Interfaces with Low-Cost Calibration for Motor Rehabilitation using Artificial Intelligence, Evidence Verification, and Adaptive Decision Adjustment**

> **Cumulative research snapshot through Phase 03 (P00–P03)**
> **Current scope:** reproducible offline research on public EEG motor-imagery benchmarks
> **Completed phases:** P00, P01, P02, P03
> **Next phase:** P04 — IHARQ Evidence Verification
> **Scientific evidence ceiling:** public-benchmark, offline, non-clinical, non-deployment

---

## Overview

**IHARQ BenchGuard** is a research framework for studying and improving **decision reliability in EEG-based brain–computer interfaces (BCIs)**.

The project is deliberately broader than a conventional decoder benchmark.

Its central question is not only:

> *How accurately can a model predict a motor-intention class?*

but also:

> *When is the available evidence sufficiently reliable to support a decision, and when should the system wait, request additional evidence, defer, fall back, remain uncertain, or block action?*

The project therefore treats a decoder prediction as **one source of evidence**, not as the final authority for an action.

The cumulative architecture connects:

```text
EEG
  ↓
Public-data and protocol anchor
  ↓
Decoder / baseline measurement
  ↓
Calibration and uncertainty
  ↓
IHARQ evidence verification
  ↓
Temporal trust / RegimeRisk
  ↓
Adaptive decision policy
  ↓
Simulated closed-loop evaluation
  ↓
Stress testing
  ↓
Embodiment demonstrations
  ↓
Governed reporting and reproducibility
```

This repository/release represents the cumulative project state **through the completion of P03**.

---

# Current Release

The principal downloadable archive for this GitHub snapshot is:

```text
IHARQ_Cumulative_GitHub_Ready_Through_P03_PostExtension_64_128_256_R1.zip
```

This package represents the cumulative project state after completion of the first four formal phases:

```text
P00 → P01 → P02 → P03
```

It should be treated as a **versioned research snapshot**, not as evidence that downstream phases have already been executed.

The archive preserves the project's code, configurations, records, manifests, checksums, validation materials, historical state, downstream handoffs, and external-artifact pointers required for traceability and continuation.

---

# Project Status

The formal project roadmap contains **16 phases, P00–P15**.

At this snapshot:

| Phase   | Role                                                             | Status                |
| ------- | ---------------------------------------------------------------- | --------------------- |
| **P00** | Repository, governance, schemas, configuration, reproducibility  | **Completed**         |
| **P01** | Public EEG data, label/split protocol, preprocessing and windows | **Completed**         |
| **P02** | Baseline decoders, low-label experiments and A4 controls         | **Completed**         |
| **P03** | Calibration, uncertainty and selective prediction                | **Completed**         |
| **P04** | IHARQ evidence verification                                      | **Next**              |
| P05     | Temporal trust / RegimeRisk                                      | Planned               |
| P06     | Evidence-quality estimation and supervised Adaptive-IHARQ        | Planned               |
| P07     | Learning-to-defer baseline                                       | Planned               |
| P08     | Simulated closed-loop readiness                                  | Planned               |
| P09     | Lite-StressForge                                                 | Planned               |
| P10     | Contextual bandit                                                | Planned               |
| P11     | Reinforcement-learning policy                                    | Planned               |
| P12     | MyoSuite embodiment demonstration                                | Planned               |
| P13     | OpenSim replay/comparison                                        | Optional / downstream |
| P14     | Dashboard and result cards                                       | Planned               |
| P15     | Final thesis integration                                         | Planned               |

### Progress

Formal phase-count progress:

```text
4 / 16 phases = 25%
```

A workload-based planning estimate in the cumulative progress analysis placed completed work at approximately **30%**, reflecting the comparatively heavy infrastructure, data, decoder and trust-foundation work already completed.

That 30% value is a **planning estimate**, not an earned-value metric and not a claim that 30% of the final scientific hypotheses have been proven.

---

# Research Question

The central research question is:

> **Can probability calibration, uncertainty analysis, incremental evidence verification, and adaptive decision control improve the reliability of low-calibration-cost EEG-based BCI decision making, such that the system reasons not only about the predicted class but also about whether the available evidence is adequate for action?**

The project is particularly interested in situations where:

* decoder performance is heterogeneous across datasets or participants;
* confidence does not correspond cleanly to correctness;
* calibration improves probability quality without producing a transferable acceptance policy;
* the system encounters insufficient or contradictory evidence;
* a fixed threshold is unavailable or unstable;
* additional evidence may or may not justify its computational and latency cost;
* temporal nonstationarity changes the reliability of previous operating assumptions.

---

# Main Research Objectives

IHARQ BenchGuard aims to:

1. Build a reproducible pipeline from public EEG data to governed decision evidence.
2. Maintain explicit dataset, split, preprocessing, model, checkpoint, prediction and artifact identities.
3. Compare classical, Riemannian and lightweight/deep neural decoder families.
4. Evaluate full-training and low-label regimes.
5. Measure probability reliability using calibration-sensitive metrics.
6. Separate decoder discrimination from probability reliability and selective-decision quality.
7. Preserve negative, failed, blocked, incompatible and zero-coverage outcomes.
8. Develop IHARQ as an evidence-verification layer rather than a second ordinary classifier.
9. Investigate temporal reliability and regime change through RegimeRisk.
10. Develop adaptive policies for accept/wait/request/defer/fallback/uncertain/unsafe decisions.
11. Evaluate downstream policies in simulated closed-loop and controlled-stress environments.
12. Preserve a strict boundary between offline benchmark evidence and clinical claims.

---

# Architecture

The complete architecture is organized into **Layers L0–L10**.

| Layer   | Name                                              | Primary responsibility                                                        |
| ------- | ------------------------------------------------- | ----------------------------------------------------------------------------- |
| **L0**  | Claim-Safety and Scope Governance                 | Controls scientific claim scope, limitations and evidence ceilings            |
| **L1**  | Public-Data and Protocol Anchor                   | Data, labels, splits, preprocessing, windows and leakage controls             |
| **L2**  | Decoder and Baseline Measurement Spine            | Baseline models, predictions and controlled decoder comparisons               |
| **L3**  | Calibration, Uncertainty and Selective Prediction | Probability calibration, uncertainty, registered thresholds and risk–coverage |
| **L4**  | IHARQ Evidence Verification                       | Incremental/multi-source evidence verification and multi-state decisions      |
| **L5**  | Temporal Trust / RegimeRisk Monitoring            | Drift, instability, confidence trajectory and temporal risk-regime monitoring |
| **L6**  | Adaptive Readiness Policy Layer                   | Rule-based/adaptive policy, evidence-quality estimation, deferral, bandit/RL  |
| **L7**  | Simulated Closed-Loop Readiness Environment       | Evaluation of decision consequences in simulation                             |
| **L8**  | Lite-StressForge                                  | Controlled stress generation and robustness evaluation                        |
| **L9**  | MyoSuite/OpenSim Embodiment Demo                  | Limited simulated mapping of decisions to assisted action                     |
| **L10** | Dashboard, Cards and Reproducibility              | Read-only reporting, provenance, figures, tables and reproducibility          |

Two architectural principles are especially important:

* **L0 does not allow claims to exceed the evidence.**
* **L10 reports evidence but does not retune, repair or reinterpret scientific results.**

---

# Experimental Philosophy

IHARQ is designed around several methodological constraints.

## 1. Frozen identities

Downstream phases consume upstream artifacts without silently redefining them.

Relevant identities include:

```text
dataset
participant
split
label map
preprocessing
window
training policy
label budget
model
checkpoint
prediction
calibration
threshold
metric
comparison
artifact
lineage
```

This prevents an unfavorable downstream result from being "repaired" by quietly changing its upstream substrate.

---

## 2. Separation of data roles

Training, calibration, validation/threshold-selection and TEST roles are treated as distinct.

In particular:

```text
TEST is not used to rescue or retune a rule selected on validation.
```

If a valid threshold cannot be selected from the permitted validation data, that absence is preserved as a legitimate scientific outcome.

---

## 3. Participant-aware inference

Repeated EEG windows from the same participant are not treated as fully independent observations.

Where appropriate, inference is performed at participant or governed group level rather than artificially inflating statistical sample size using event-level pseudo-replication.

---

## 4. Multiple dimensions of reliability

The project deliberately separates three measurement families.

### Decoder discrimination

Examples:

* Balanced Accuracy (BACC)
* Macro-F1
* Accuracy
* ROC-AUC where methodologically lawful

### Probability reliability

Examples:

* Brier score
* Negative log likelihood
* calibration error
* reliability diagnostics

### Selective-decision quality

Examples:

* coverage
* risk/error
* feasibility of a registered rule
* validation-to-TEST transport
* zero-coverage outcomes
* no-legal-threshold outcomes
* decision failures

A high-performing classifier is therefore **not automatically described as reliable**.

---

# Public EEG Data Foundation — P01

P01 transformed three public EEG sources into a common governed motor-imagery substrate:

```text
BNCI2014_001
Lee2019_MI
PhysioNetMI
```

The active binary task is based on:

```text
left-hand vs right-hand motor imagery
```

Inputs outside the governed task are not silently reinterpreted as a negative class.

### P01 cumulative data foundation

| Item                       |                                               Result |
| -------------------------- | ---------------------------------------------------: |
| Active public EEG datasets |                                                    3 |
| Participant groups         |                                                  172 |
| Accepted task events       |                                               12,910 |
| Valid canonical windows    |                                      12,910 / 12,910 |
| Invalid canonical windows  |                                                    0 |
| Subject-role split         | 102 / 35 / 17 / 18 train/calibration/validation/test |

The canonical preprocessing/window pipeline includes:

* EEG-only signal selection;
* event registration;
* demeaning;
* average rereferencing;
* synchronized signal/event resampling to **160 Hz**;
* **8–32 Hz** filtering;
* canonical **+0.5 s to +3.5 s** windows;
* **480 samples** per canonical window;
* quality annotation rather than silent signal repair.

---

# P00 — Governance and Reproducibility Foundation

P00 was intentionally infrastructure-focused rather than an experimental model-performance phase.

Its purpose was to ensure that subsequent results had explicit contracts for:

* schemas;
* run identities;
* configuration;
* lineage;
* lifecycle;
* validation;
* manifests;
* limitations;
* failure handling;
* phase ownership.

Selected closure results include:

| P00 validation item               |                    Result |
| --------------------------------- | ------------------------: |
| Registered engineering cells      |          **19 / 19 PASS** |
| Deterministic tests               |        **102 / 102 PASS** |
| Deliberately malformed inputs     |    **178 / 178 rejected** |
| Layer foundations                 |               **11 / 11** |
| Phase contracts                   | **16 / 16 dispositioned** |
| Limited local reproduction checks |            **8 / 8 PASS** |

A key principle established in P00 is the distinction between:

```text
an experiment being defined
```

and:

```text
scientific evidence from that experiment actually existing
```

Readiness is not reported as a result.

---

# P02 — Decoder and Baseline Evidence

P02 established the raw decoder measurement backbone before adding trust-control layers.

It evaluated classical/Riemannian and neural/deep model families under:

```text
TRAIN_FULL
```

and low-label budgets of:

```text
1, 2, 4, 8, 16, 32, 64, 128, 256
samples per class
```

## Execution closure

After the post-extension work, the A0 surface contained:

| Outcome                       |     Count |
| ----------------------------- | --------: |
| Terminal cells                |   **786** |
| SUCCESS                       |   **765** |
| FAILED                        |     **3** |
| SKIP_CONDITIONAL              |    **15** |
| BLOCKED_DEPENDENCY            |     **3** |
| Participant-level metric rows | **4,590** |
| Metric records                | **3,057** |

Failed and skipped cells remain part of the scientific denominator.

---

## No universal decoder winner

The principal P02 conclusion is that decoder ordering depends materially on:

* dataset;
* participant;
* label budget;
* architecture;
* training policy.

The evidence does **not** support a single universal decoder winner.

This is important for downstream IHARQ design because the future reliability layer should not assume that one model is always the best evidence source.

---

## Low-label behavior is not globally monotonic

Across the frozen low-label trajectories:

* all 12 valid dataset × model paths are non-monotonic over the entire 1–256 range;
* all 12 improve from **64 → 128**;
* 9 of 12 improve from **128 → 256**;
* every 256-label point still remains below its corresponding TRAIN_FULL result.

Reported aggregate values include:

```text
Mean BACC gap, 256 vs FULL: approximately -0.0525
Mean recovery ratio relative to FULL: approximately 0.9188
```

These observations do **not** justify claims such as:

```text
"128 labels is a universal threshold"
```

or:

```text
"256 labels per class is equivalent to full training"
```

---

# A4 Controls — Complexity Is Not Automatically Better

A4 evaluates controls involving longer/multiple windows and simple ensemble configurations.

In the C1–C3 analysis:

```text
1,080 rows
144 paired p-values
0 comparisons significant after Holm correction
```

A genuine adverse ensemble result was also retained: hard voting under one PhysioNetMI TRAIN_FULL condition was worse than the strongest selected member.

The methodological lesson is fundamental to IHARQ:

> **Additional processing, additional models or additional evidence do not receive credit merely for being more complex.**

Every downstream component must demonstrate benefit against an appropriate simpler baseline.

---

# P03 — Calibration, Uncertainty and Selective Prediction

P03 addresses the question:

> **Can the confidence/probability produced by a decoder actually be used reliably for decision making?**

The phase completed:

```text
25 canonical stages
285 canonical analysis groups
108 post-extension supplement groups
```

while preserving failed and superseded attempts.

---

## A1 — Probability Calibration

The evaluated calibration portfolio includes methods such as:

* identity/no recalibration;
* Platt scaling;
* beta calibration;
* quadratic logistic calibration;
* monotone spline calibration.

Selection is governed by validation-side probability quality rather than TEST-side optimization.

Among the 285 canonical groups:

```text
Platt selected:    118 groups
Identity selected: 47 groups (16.5%)
```

The presence of the identity branch is intentional: the system is not forced to recalibrate a score when calibration does not demonstrate acceptable benefit.

---

## Aggregate Calibration Results

On the frozen canonical TEST population:

| Metric                | Raw mean | Selected mean | Δ selected − raw |   95% bootstrap CI |
| --------------------- | -------: | ------------: | ---------------: | -----------------: |
| **Brier**             |   0.5803 |        0.4875 |      **-0.0929** | [-0.1070, -0.0791] |
| **NLL**               |   1.0140 |        0.6811 |      **-0.3328** | [-0.4225, -0.2544] |
| **Calibration error** |   0.1671 |        0.0385 |      **-0.1285** | [-0.1448, -0.1125] |

The aggregate direction therefore supports the conclusion that **selected calibration improves probability quality on average**.

However, improvement is not universal.

The cumulative analysis also retains:

```text
34 groups worse on Brier
29 groups worse on NLL
31 groups worse on calibration error
44 / 285 canonical groups with DETERIORATED status
```

This heterogeneity is scientifically important and is not removed from the report.

---

# A2 — Registered Threshold Transport

P03 does not optimize the selective threshold on TEST.

The intended process is:

```text
validation
  ↓
select a lawful non-empty threshold satisfying the target
  ↓
freeze threshold
  ↓
apply the same rule to TEST
```

Among the 285 canonical groups:

```text
194 / 285 (68.1%) had a legal validation threshold
91 / 285  (31.9%) had NO_LEGAL_THRESHOLD
```

The central result is that **validation-side threshold feasibility and held-out TEST behavior are strongly heterogeneous**.

Even when restricting analysis to groups with a legal rule and positive TEST coverage, the estimated average risk difference does not support a universal risk-reduction claim.

This is one of the main scientific motivations for the next phase.

---

# A3 — Uncertainty and Selective Prediction

P03 also identified an important limitation of the current binary task.

For a binary probability output:

```text
confidence
normalized entropy
top-1 / top-2 margin
```

are transformations of the same underlying probability score and therefore produce the same ranking in the current setting.

They must **not** be counted as three independent pieces of evidence.

This observation directly affects the design of later IHARQ evidence combination.

A useful evidence-verification layer therefore needs genuinely additional information, such as:

* neighboring-window stability;
* independent model/lineage evidence;
* valid disagreement sources;
* signal-quality evidence;
* channel-subset evidence;
* temporal history;
* other independently governed evidence sources.

---

# High-Confidence Errors Remain

Calibration improvement does not eliminate confidently wrong predictions.

Using a diagnostic confidence threshold of at least 0.90, the P03 analysis still identified:

```text
253 confidently wrong canonical predictions
313 confidently wrong supplement predictions
```

This is another reason the project does not equate:

```text
high confidence
```

with:

```text
safe or sufficient evidence for action
```

---

# Cumulative Scientific Findings Through P03

The most important conclusions at this point are:

### 1. Decoder accuracy, probability calibration and decision-policy reliability are different problems

A decoder may discriminate classes reasonably well while producing poorly calibrated scores.

A score can become better calibrated without generating a reliably transferable selective-decision threshold.

---

### 2. Dataset and participant heterogeneity matter

Both decoder ordering and trust-related behavior vary materially across data sources and analysis groups.

The evidence does not support a one-dimensional ranking such as:

```text
best model everywhere
```

or:

```text
best calibrator everywhere
```

---

### 3. There is no universal decoder or calibrator winner

The project therefore motivates an **evidence-aware and eventually adaptive architecture** rather than hard-coding one universally assumed source.

---

### 4. More labels generally help, but not through a simple universal law

Low-label learning curves are not globally monotonic.

Higher budgets improve many trajectories but do not establish a universal threshold at which low-label training becomes equivalent to TRAIN_FULL.

---

### 5. More complexity does not automatically create more value

Multi-window processing, ensembles and future adaptive policies must earn their added complexity through controlled comparison.

---

### 6. Calibration is useful but insufficient

This is arguably the strongest cumulative P03 conclusion:

> **Improving probability calibration does not by itself solve the problem of reliable decision making.**

The gap between calibrated probability quality and transferable decision reliability is the main scientific motivation for P04.

---

### 7. Negative evidence is part of the scientific result

IHARQ deliberately preserves:

* failed runs;
* blocked dependencies;
* conditional skips;
* incompatible inputs;
* no-legal-threshold states;
* zero-coverage states;
* calibration deterioration;
* ineligible evidence sources;
* harmful comparisons;
* confidently wrong predictions;
* unsupported hypotheses.

These outcomes are not treated as disposable missing data.

---

# Current Defensible Claims

At the end of P03, the project evidence supports carefully qualified statements such as:

* A reproducible, fail-closed experimental chain has been established from public EEG data through decoder and trust evidence.
* Selected probability calibration improves aggregate Brier score, NLL and calibration error in the frozen P03 analysis population.
* Calibration improvement is heterogeneous and is not universal across all groups.
* A validation-selected risk threshold is unavailable in a substantial fraction of groups and does not reliably preserve the same risk–coverage behavior on TEST.
* Multiple common uncertainty features in the current binary task are ranking aliases rather than independent evidence sources.
* Additional decoder/ensemble/post-processing complexity does not automatically yield measurable benefit.
* Dataset and participant heterogeneity are important determinants of performance and reliability behavior.

---

# Claims This Release Does **Not** Support

This repository must **not** be interpreted as evidence that:

* the system is clinically safe;
* the system reduces clinical rehabilitation risk;
* the system is deployment-ready;
* the validation risk target is guaranteed on TEST;
* one decoder is universally best;
* one calibrator is universally best;
* 128 labels per class is a universal optimum;
* 256 labels per class is equivalent to full training;
* the complete learning curve is monotonic;
* IHARQ evidence verification has already demonstrated benefit;
* RegimeRisk has already demonstrated benefit;
* an adaptive policy has already demonstrated benefit;
* reinforcement learning has already demonstrated benefit;
* simulated embodiment establishes therapeutic effectiveness.

The present evidence is:

```text
public-benchmark
offline
non-clinical
non-deployment
```

This limitation is intentional.

---

# Ablation Structure

The project uses a governed ablation framework.

Current evidence through P03 covers:

```text
A0 — raw decoder evidence
A1 — calibration
A2 — simple registered threshold
A3 — uncertainty / selective prediction
A4 — window / ensemble / contextual controls
```

Downstream:

```text
A5–A13
```

belong to later phases and should not be reported as experimentally established at this snapshot.

```text
A14
```

is intentionally prohibited in the formal stack to prevent silent ablation-identity drift.

---

# Why IHARQ?

The name is inspired by the conceptual logic of **Hybrid Automatic Repeat reQuest (HARQ)** in communication systems, but the project does **not** claim that neural states behave like retransmittable communication packets.

The translation is conceptual:

```text
communication system:
received message
→ verify quality
→ accept / request more / combine receptions

IHARQ:
decoder output
→ verify evidence quality
→ accept / wait / request additional evidence /
  combine lawful evidence / fallback / remain uncertain
```

In BCI, the same neural state cannot simply be retransmitted.

Additional evidence may instead come from:

* a subsequent temporal window;
* an independently valid model or member;
* a lawful channel subset;
* signal-quality indicators;
* neighboring-window stability;
* model agreement/disagreement;
* other registered evidence sources.

The value of P04 is therefore falsifiable:

> **Does additional evidence genuinely improve decision quality, or does it merely add complexity?**

---

# Canonical IHARQ Decision Vocabulary

The evidence-verification layer uses explicit decision states rather than treating every decoder output as immediately actionable.

The canonical vocabulary includes:

```text
accept
wait
request_evidence
combine_evidence
fallback
uncertain
unsafe
```

These actions are separate from the decoder's motor-intention label.

The decoder answers:

```text
Which motor-intention class is most likely?
```

IHARQ asks:

```text
Is the available evidence adequate to use that prediction?
```

---

# Next Phase — P04

The next formal phase is:

```text
P04 — IHARQ Evidence Verification
```

P04 starts directly from the main P03 failure mode:

> A simple confidence/risk threshold is often unavailable or does not transfer reliably from validation to held-out TEST data.

P04 therefore investigates whether multiple legitimate evidence sources can govern the decision more effectively than a single threshold.

Candidate evidence dimensions include:

* calibrated confidence;
* uncertainty indicators with alias controls;
* signal quality;
* stability across nearby windows;
* availability of valid alternative evidence;
* model agreement/disagreement where genuinely independent;
* explicit reason codes for instability or insufficiency.

The objective is **not simply higher raw classification accuracy**.

Relevant questions include:

* At comparable coverage, can error/risk be reduced?
* At comparable risk, can usable coverage be increased?
* Can no-rule or zero-coverage states be handled transparently rather than hidden?
* What computational burden is added?
* What latency is added?
* Which participants/groups benefit?
* Which participants/groups are harmed?
* When should the system fall back or remain uncertain?

---

# Downstream Roadmap

Following P04:

### P05 — RegimeRisk

Investigates whether temporal history provides reliability information beyond the current snapshot.

Potential signals include:

* confidence trajectory;
* entropy trajectory;
* disagreement;
* quality degradation;
* repeated failures;
* temporal regime changes.

### P06 — Evidence-Quality Estimation / Adaptive IHARQ

Introduces supervised estimation of evidence quality and adaptive readiness decisions.

### P07 — Learning to Defer

Provides an independent deferral baseline so adaptive policies are not compared only with hand-built rules.

### P08 — Simulated Closed Loop

Evaluates decision consequences in a controlled simulated environment.

### P09 — Lite-StressForge

Tests robustness under controlled perturbation/stress conditions.

### P10–P11 — Adaptive Sequential Policies

Investigates contextual-bandit and reinforcement-learning policy extensions.

These methods are downstream hypotheses, not guaranteed improvements.

### P12–P13 — Embodiment

Adds limited simulated embodiment through MyoSuite and, if scientifically justified, OpenSim.

These phases do not transform the project into a clinical study.

### P14–P15 — Presentation, Reproducibility and Thesis Integration

Produces the governed final presentation, reproducibility package, evidence mapping and thesis integration.

---

# Important Methodological Limitations

The cumulative evidence should be interpreted with the following limitations.

## Public, offline EEG

The present datasets are public, offline and predominantly motor-imagery EEG.

Results do not directly generalize to:

* patients;
* therapy effectiveness;
* real-time rehabilitation;
* clinical safety;
* deployed assistive control.

---

## Unequal TEST population sizes

Under the current split, `BNCI2014_001` has only one participant in TEST, limiting between-participant inference for that dataset.

---

## Frozen nested low-label subsets

Low-label experiments use frozen nested membership.

Independent subset-resampling uncertainty has not yet been fully characterized.

---

## Post-hoc extensions remain post-hoc

Some 64/128/256 extensions and Stage S18 sensitivity analyses were added after earlier canonical work.

They improve resolution but must not be retrospectively described as prospectively preregistered evidence.

---

## Binary uncertainty aliases

In the current binary task, confidence, normalized entropy and probability margin are not independent evidence sources.

---

## Threshold failure mechanism is not yet causally identified

Poor validation-to-TEST transport is observed, but its causal decomposition may involve:

* finite-support effects;
* participant shift;
* dataset heterogeneity;
* nonstationarity;
* probability geometry;
* other mechanisms.

Later phases are intended to investigate these possibilities.

---

# Reproducibility and Scientific Integrity

The project follows a reproducibility-first approach.

Important principles include:

```text
frozen identities
explicit lineage
role-separated data
no TEST-side rescue
matched comparisons
versioned artifacts
preserved negative results
fail-closed validation
checksums and manifests
explicit limitations
claim ceilings
```

A valid negative result with complete provenance is preferred over a favorable result whose source, comparator or denominator cannot be reconstructed.

---

# Repository / Archive Integrity

The cumulative GitHub-ready package includes integrity and project-state records intended to make the snapshot auditable.

Depending on the exact release snapshot, important top-level materials include records such as:

```text
README.md
CURRENT_PROJECT_STATUS.json
CURRENT_CUMULATIVE_REPOSITORY_MANIFEST.json
REPOSITORY_CHECKSUMS.sha256
current_document_index.md
current_artifact_index.csv
external_artifact_pointer_manifest.yaml
phase_handoff.yaml
```

The project also preserves structured areas for:

```text
artifacts/
configs/
current/
docs/
history/
scripts/
tests/
```

Large scientific assets may be represented by immutable external pointers rather than duplicated unnecessarily inside GitHub.

---

# Downloading This Snapshot

Open the **Releases** section of this GitHub repository and download:

```text
IHARQ_Cumulative_GitHub_Ready_Through_P03_PostExtension_64_128_256_R1.zip
```

Keep the ZIP intact if you want the original transport snapshot.

For analysis or inspection, extract it to a separate directory.

---

# External Artifacts

Some large scientific artifacts are stored externally rather than embedded repeatedly in the repository.

External artifacts should be resolved through their governed pointer records, including as applicable:

```text
provider
repository/dataset
immutable revision
path
SHA-256
byte size
access requirements
producer phase
consumer phase
```

A mutable URL alone is not treated as sufficient provenance.

Private-access credentials must **never** be committed to this repository.

---

# Credentials and Secrets

Never commit literal:

```text
Hugging Face tokens
GitHub personal-access tokens
Kaggle credentials
API keys
passwords
private keys
.env files containing credentials
```

The project may refer to symbolic secret names in configurations or documentation, but the actual secret values must remain outside the repository.

---

# Research Integrity Policy

The following practices are explicitly rejected:

* selecting only favorable runs;
* silently removing failed cells;
* changing a threshold after viewing TEST;
* reporting zero coverage as missing;
* pretending an unavailable comparison passed;
* rewriting post-hoc work as preregistered;
* counting correlated uncertainty transformations as independent evidence;
* treating model complexity as evidence of superiority;
* presenting offline benchmark behavior as clinical safety;
* hiding limitations from figures or summaries.

---

# Interpretation Hierarchy

Scientific interpretation follows:

```text
measured result
    ↓
supported interpretation
    ↓
candidate claim
    ↓
claim-governance review
    ↓
approved/qualified/rejected claim
```

A result is not automatically a publication-level claim.

---

# Scientific Position at the End of P03

At this snapshot, the project has moved beyond infrastructure construction and has a usable experimental backbone for studying reliability.

The cumulative chain is:

```text
P00
governance and reproducibility
    ↓
P01
public EEG substrate and leakage-controlled protocol
    ↓
P02
decoder and low-label evidence
    ↓
P03
calibration, uncertainty and selective-decision evidence
```

The main conclusion is not that the reliability problem has been solved.

It is that the problem has now been **empirically characterized well enough to test the project's central evidence-verification hypothesis**.

What is currently known:

```text
accuracy alone is insufficient
confidence alone is insufficient
calibration is useful but non-universal
simple threshold transport is weak/heterogeneous
negative evidence is scientifically informative
complexity must earn its benefit
```

What remains to be demonstrated:

```text
Can IHARQ evidence verification improve this decision gap?
Can temporal trust add information beyond a snapshot?
Can adaptive policy improve outcomes without unacceptable cost or overfitting?
```

Those questions belong to P04 and later phases.

---

# Scope and Safety Notice

**IHARQ BenchGuard is currently a research framework evaluated on offline public EEG benchmarks.**

This release is **not**:

* a medical device;
* a clinical decision-support system;
* a rehabilitation treatment;
* a safety certification;
* evidence of therapeutic effectiveness;
* evidence of real-world deployment readiness.

Any future clinical or real-world interpretation would require separate evidence, validation and governance beyond the present project scope.

---

# Academic Context

The project is being developed as a research-focused BCI reliability study with an intended path from reproducible public-data benchmarking toward evidence-aware and adaptive decision control.

The work intentionally emphasizes:

* methodological traceability;
* reproducibility;
* negative-result preservation;
* uncertainty;
* calibration;
* selective prediction;
* controlled ablation;
* evidence governance;
* explicit limitations.

The scientific value is therefore not defined solely by achieving the highest classifier score.

---

# Key Scientific Foundations

The project is situated around research themes including:

* reproducible BCI benchmarking;
* motor-imagery EEG decoding;
* classical and neural EEG models;
* probability calibration;
* uncertainty quantification;
* selective prediction;
* closed-loop BCI simulation;
* adaptive BCI systems;
* semantic/HARQ-inspired reliability concepts;
* nonstationary time-series monitoring;
* musculoskeletal simulation and embodiment.

External literature is used for scientific positioning and method context.

Project performance numbers should be interpreted from **IHARQ's own governed artifacts and evaluation contracts**, not compared naively with externally reported numbers that may use different datasets, splits, preprocessing, tasks or metrics.

---

# Selected Background References

The cumulative project report draws on foundational and contextual work including:

1. Jayaram & Barachant — *MOABB: Trustworthy Algorithm Benchmarking for BCIs*.
2. MOABB — Mother of All BCI Benchmarks documentation.
3. Chevallier et al. — reproducibility benchmarking for EEG-based BCI.
4. Lawhern et al. — *EEGNet*.
5. Schirrmeister et al. — deep convolutional neural networks for EEG decoding and visualization.
6. Research on uncertainty quantification for motor-imagery BCI.
7. Work on online/test-time adaptation for EEG decoding.
8. Closed-loop motor-imagery BCI simulation.
9. Adaptive BCI frameworks.
10. BCI-assisted rehabilitation literature.
11. MyoSuite.
12. OpenSim Moco.
13. Semantic HARQ / reliable semantic communication research.
14. Nonstationary time-series model-selection and regime-monitoring research.

See the project's cumulative scientific documents for the complete bibliography and the exact role of each source.

---

# How to Reference This Release

When referring specifically to this repository snapshot, identify it as:

```text
IHARQ BenchGuard Stretch C
Cumulative GitHub-Ready Repository through Phase 03
Post-Extension 64/128/256
Revision R1
```

When using derived experimental results, also preserve the relevant:

```text
phase
dataset
split
model
budget
configuration
artifact identity
metric
comparison
analysis status
limitations
```

so that results are not separated from their provenance.

---

# Current Bottom Line

> **Through P03, IHARQ BenchGuard has established a reproducible, claim-bounded chain from public EEG data through decoder measurement, probability calibration, uncertainty analysis and selective-decision evaluation. The evidence shows that calibration can improve probability quality substantially on average, but that this improvement does not automatically yield a transferable decision policy. Decoder and calibration performance are heterogeneous, confidently wrong predictions remain, simple thresholds frequently fail or transport poorly, and added complexity is not automatically beneficial. These findings motivate P04: testing whether explicit multi-source evidence verification can improve decision reliability where simple confidence-based acceptance fails.**

---

## Status Summary

```text
Project:                  IHARQ BenchGuard Stretch C
Formal phases:            P00–P15
Completed:                P00–P03
Phase-count progress:     25%
Planning workload estimate: ~30%
Completed layers/evidence: governance, data, decoder, calibration/UQ foundation
Next phase:               P04 — IHARQ Evidence Verification
Current evidence scope:   public-benchmark / offline / non-clinical
Clinical claims:          NOT SUPPORTED
Deployment claims:        NOT SUPPORTED
Repository snapshot:      GitHub-ready through P03
Release revision:         Post-Extension 64/128/256 R1
```

---

**This repository is a cumulative research artifact. Preserve provenance, failures, negative results, checksums, limitations, and historical records when using or extending it.**
