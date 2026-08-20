---
title: "IHARQ BenchGuard Stretch C - Phase 1 / Layer 1 Independently Audited Fully Instantiated Implementation and Execution Annex"
document_id: "IHARQ-IBB-P01-L1-ANNEX-R4"
revision: "R4"
date: "2026-08-04"
status: "INDEPENDENT_AUDIT_REPAIRED; FULLY_INSTANTIATED_FOR_KAGGLE_CORRECTION"
parent_build_book: "IHARQ-IBB-R10-P01-L1-INDEPENDENT-AUDIT-REPAIRED"
governing_workflow: "Governance V6.1"
supersedes: "IHARQ-IBB-P01-L1-ANNEX-R3"
execution_claim: "NOT EXECUTED; INDEPENDENTLY AUDITED PRE-RUN AUTHORITY FREEZE"
---

# IHARQ Phase 1 / Layer 1 Independently Audited Implementation and Execution Annex R4

> **Controlling purpose.** R4 preserves the complete valid R3 design and official-run freeze, repairs the material exactness defects found by independent reconstruction, and supplies the exact machine-readable authority required to correct the official Kaggle notebook. No Kaggle execution or Phase 1 evidence is claimed.

## 1. Independent executive decision

The three-anchor portfolio remains lawful: PhysioNetMI is the source/provenance anchor, BNCI2014_001 is the benchmark companion, and Lee2019_MI is the larger two-session target companion. Cho2017 and GuttmannFlury2025_MI remain screened and inactive. The independent audit found no need to change Architecture, Registry, Method Selection, Protocol, or Nuts-and-Bolts. Seven Build Book-owned exactness defects required controlled documentary repair.

**Terminal implementation-authority decision:** `P01_L1_IMPLEMENTATION_INDEPENDENT_AUDIT_REPAIRED_AND_PASS`.

## 2. Repair ledger

| Defect ID | R9/R3 condition | R10/R4 repair | Status |
|---|---|---|---|
| DEF-R4-001 | PhysioNet checksum policy ignored provider `SHA256SUMS.txt`. | Verify provider SHA-256 per file, then independently recompute and freeze the IHARQ aggregate. | REPAIRED |
| DEF-R4-002 | Subject 88 was included but per-subject loading was not mandatory. | Load every subject independently; load subject 88 separately at 128 Hz and jointly resample signal/events to 160 Hz. | REPAIRED |
| DEF-R4-003 | BNCI mapping omitted baseline, unknown-cue and eye-movement codes. | Freeze all eleven official provider codes and preserve/block ambiguous code 783. | REPAIRED |
| DEF-R4-004 | Polyphase window/padding and SOS edge length were not exact. | Freeze Kaiser beta 5.0, reflect padding, odd SOS padding and `padlen=27`. | REPAIRED |
| DEF-R4-005 | MOABB distribution identity lacked official package hashes. | Freeze official PyPI wheel and sdist SHA-256; block before download on mismatch. | REPAIRED |
| DEF-R4-006 | Quality evidence register cited only a preprint. | Record the peer-reviewed 2026 article and retain the accessible preprint only for method-detail cross-check. | REPAIRED |
| DEF-R4-007 | Disk values could be read as Kaggle guarantees. | Reclassify them as IHARQ preflight thresholds; block below 60 GB and record actual runtime resources. | REPAIRED |

## 3. Corrected source and checksum freeze

- PhysioNetMI is frozen to PhysioNet EEGMMIDB v1.0.0, DOI `10.13026/C28G6P`, ODC-By-1.0. The provider-published `SHA256SUMS.txt` is mandatory. Every downloaded file must match the provider checksum before the framework computes its own per-file and aggregate hashes.
- BNCI2014_001 remains the official 001-2014 A01T/A01E–A09T/A09E file set under CC BY-ND 4.0. Per-file SHA-256 is computed and frozen after provider-identity verification.
- Lee2019_MI remains GigaDB `10.5524/100542`, offline/train labeled MI only, under the maintained source-card license record.
- Inactive screened sources retain factual cards but cannot enter the run matrix without a versioned authority amendment.

## 4. PhysioNet subject 88 acquisition contract

The official run retains all 109 subjects. Every subject is loaded through a separate `get_data(subjects=[subject_id])` call. Subject 88 is loaded alone at 128 Hz; its continuous EEG and original event array are jointly resampled to 160 Hz. Bulk loading subject 88 with 160 Hz subjects is prohibited and is a deterministic preflight failure.

## 5. Complete BNCI2014_001 event contract

The expected provider event inventory is exactly: `276`, `277`, `768`, `769`, `770`, `771`, `772`, `783`, `1023`, `1072`, `32766`. Codes 769 and 770 are included left/right MI. Feet and tongue are preserved but excluded from the binary branch. Baseline, start, eye-movement and rejected-trial codes remain technical/quality provenance. Code 783 is ambiguous and blocks the affected event while preserving it. Any unlisted observed code blocks the affected source event.

## 6. Exact preprocessing edge contract

The official resampling call is equivalent to:

```python
raw_resampled, events_resampled = raw.resample(
    160.0,
    method="polyphase",
    window=("kaiser", 5.0),
    pad="reflect",
    events=events_original,
    n_jobs=1,
)
```

The 8–32 Hz fourth-order Butterworth filter is designed as SOS and applied by `scipy.signal.sosfiltfilt` with `padtype="odd"`, `padlen=27`, producing an effective forward-backward order of eight. Continuous runs must contain at least 29 samples; official windows are extracted only after continuous-run filtering.

## 7. Dependency and resource preflight

MOABB 1.5.0 is resolved only from official PyPI. The wheel SHA-256 is `8856067aba66fa4389f86e1fbc5cd9c5d52343538ad59193cef103a48a41c297`; the source distribution SHA-256 is `8fd2182f5e35607e0c63de081c3d61a125bc806787270307d58c5ff3eaa31ecb`. A package/hash/import mismatch blocks before source download.

The 60 GB minimum and 90 GB recommendation are project preflight thresholds, not guarantees about Kaggle. Actual free disk, RAM, Python and package identities are recorded at runtime. Free disk below 60 GB blocks acquisition. Sources are processed sequentially with dataset-level checkpoints and verified cache eviction.

## 8. Quality-policy evidence correction

The 500 µV amplitude check remains a soft warning only. It neither rejects nor repairs data and is not described as a universal physiological boundary. The evidence register now uses the peer-reviewed Computers in Biology and Medicine article (2026, 111837, DOI `10.1016/j.compbiomed.2026.111837`) as the current research identity and the accessible preprint only to cross-check the method detail.

## 9. Machine-readable controlling set

The current controlling machine-readable files are the `R2` freeze set under `machine_readable/`. Any R1 file is historical. The central identity is `P01-L1-OFFICIAL-RUN-FREEZE-R2`, inherited by the future Protocol v1.0 P01 annex unless the Governance V6.1 evidence-insufficiency loop creates a versioned amendment and rerun.

## 10. Certification boundary

R4 certifies that project-owned pre-run values are exact enough to correct the Kaggle notebook. It does not certify source download, official execution, gate passage, evidence sufficiency, Phase 1 closure, or Phase 2 authorization.

# Preserved Annex R3 — historical, superseded and non-controlling

---
title: "IHARQ BenchGuard Stretch C - Phase 1 / Layer 1 Fully Instantiated Implementation and Execution Annex"
document_id: "IHARQ-IBB-P01-L1-ANNEX-R3"
revision: "R3"
date: "2026-08-04"
status: "FULLY_INSTANTIATED_FOR_OFFICIAL_KAGGLE_RUN"
parent_build_book: "IHARQ-IBB-R9-P01-L1-FULLY-INSTANTIATED"
governing_workflow: "Governance V6.1"
supersedes: "IHARQ-IBB-P01-L1-ANNEX-R2"
execution_claim: "NOT EXECUTED; EXACT PRE-RUN AUTHORITY FREEZE"
---

# IHARQ Phase 1 / Layer 1 Fully Instantiated Implementation and Execution Annex R3

> **Controlling purpose.** This R3 annex preserves every valid design, module, artifact, gate, test, boundary and handoff from R2, and repairs the one material incompleteness: the official P01 run was not instantiated. R3 freezes one exact executable configuration. It does not claim that Kaggle has run or that P01 evidence exists.

## 1. Executive decision and authority compatibility

The three-anchor dataset portfolio and the Layer 1 implementation design were already accepted by the Method Selection and Build Book authorities. The unresolved values were implementation/run-realization decisions, not permission to invent new science. R3 uses the following compatibility rule:

> The R9/R3 Build Book package owns the exact pre-run physical configuration. The later Protocol v1.0 P01 annex must inherit the frozen values and identities verbatim unless the sole Governance V6.1 evidence-insufficiency loop issues a versioned amendment and rerun.

This resolves the prior deadlock without creating a new mode, changing the Registry, redefining A0-A13, executing downstream science, or claiming results.

## 2. Source intake and verified predecessor identity

| Source | SHA-256 | Use |
|---|---|---|
| Governance V6.1 | c811373c19a7c2c3f6d72cf2aed984e02ffcb07bb448cfc3bdbdf26a35a4f1d9 | single-track, ZIP-first, one-notebook, sole repair loop |
| Seven authorities archive | beb00f47e4a790242d62405dcca799647d849c8dc2ff043c5196cee372607128 | Architecture through Nuts-and-Bolts |
| Phase 0 project package | 3dcbe3e82ec7254ce1bd40568b36409d56050538e69a7264f8f1e431be019ef0 | schemas, IDs, serialization, lineage, tests, contracts |
| R8/R2 implementation archive | c6e6ffff67cdc78c396aca835308a83819e06db3a2c9a81a95c6d25ef6392d29 | predecessor Build Book and annex |
| R3 Kaggle input bundle | 3137b2a851eb64e8633067bd80bfdc1d2bd5bc1e5b2d53b48dc275975f032fae | runtime/config gap audit |
| R3 notebook | b896c8034ca7d91b88ec6a206baf54b96dbe25f7cd1160cbd7b34025453bf3a6 | notebook correction compatibility |

## 3. Unresolved-state root-cause report

The prior package used `null`, empty maps and unresolved access/source tokens because it correctly refused to fabricate source and scientific values. That fail-closed behavior was safe but did not satisfy the owner's direct-run requirement. The root cause was documentary ownership ambiguity between Build Book physical configuration and later Protocol recording. R3 resolves the values now, freezes them, and requires Protocol v1.0 to inherit rather than reselect them.

The corrected boundary is:

```text
Build Book R9 / Annex R3: exact pre-run configuration and source identities
Kaggle R4 correction: implements and executes the frozen configuration
Protocol v1.0 P01 annex: records the exact executed freeze and any versioned repair history
```

## 4. Dataset activation and factual freeze

| Dataset | Status | Active | Release | License | Access | Adapter |
|---|---|---|---|---|---|---|
| PhysioNetMI | PRIMARY_SELECTED | True | 1.0.0 | Open Data Commons Attribution License 1.0 (ODC-By-1.0) | MOABB_1_5_0_OFFICIAL_PHYSIONET_DOWNLOAD | MOABBPhysionetMIAdapter |
| BNCI2014_001 | PRIMARY_SELECTED | True | 001-2014 provider file set A01T/A01E through A09T/A09E | Creative Commons Attribution-NoDerivatives 4.0 International (CC BY-ND 4.0) | MOABB_1_5_0_OFFICIAL_BNCI_DOWNLOAD | MOABBBNCI2014001Adapter |
| Lee2019_MI | PRIMARY_SELECTED_WITH_SOURCE_QUALIFICATIONS | True | GigaDB dataset DOI 10.5524/100542; MOABB 1.5.0 Lee2019_MI wrapper; labeled offline/train MI runs only | GNU General Public License v3.0 as documented by the maintained MOABB source card; source terms retained in DatasetCard | MOABB_1_5_0_OFFICIAL_GIGADB_DOWNLOAD | MOABBLee2019MIAdapter |
| Cho2017 | SCREENED_FALLBACK | False | GigaDB dataset DOI 10.5524/100295; MOABB 1.5.0 source card | Creative Commons Attribution 4.0 International (CC BY 4.0) | NOT_ACTIVE_FOR_P01_OFFICIAL_RUN | NOT_APPLICABLE_TO_ACTIVE_RUN |
| GuttmannFlury2025_MI | SCREENED_CURRENT_DELTA_CANDIDATE | False | Zenodo v1, DOI 10.5281/zenodo.18970793, published 2026-03-12; derived from Synapse DOI 10.7303/syn64005218; MOABB 1.5.0 BDF conversion | Dataset release: CC0 1.0 Universal; publication licensing remains separate | NOT_ACTIVE_FOR_P01_OFFICIAL_RUN | NOT_APPLICABLE_TO_ACTIVE_RUN |

### 4.1 PhysioNetMI

**Role:** source/rest/provenance anchor  
**Official identity:** PhysioNet EEG Motor Movement/Imagery Database (EEGMMIDB)  
**Citation:** Schalk G, McFarland DJ, Hinterberger T, Birbaumer N, Wolpaw JR. BCI2000: A General-Purpose Brain-Computer Interface (BCI) System. IEEE Transactions on Biomedical Engineering. 2004;51(6):1034-1043; dataset DOI 10.13026/C28G6P.  
**Reference:** https://physionet.org/content/eegmmidb/1.0.0/; https://doi.org/10.13026/C28G6P  
**Checksum policy:** COMPUTE_SHA256_PER_DOWNLOADED_FILE_AND_FREEZE_AGGREGATE_BEFORE_ADMISSION  
**Expected structure:** 109 subjects; one MOABB session; 14 provider runs, official P01 subset runs 4/8/12; T0/T1/T2 annotations; subject 88 may be 128 Hz and must be resampled through the frozen profile.  
**Labels:** T0: rest/no action; T1: left-hand imagery in runs 4/8/12; T2: right-hand imagery in runs 4/8/12  
**Limitations:** Run context is mandatory for T1/T2 semantics; Executed-movement and baseline runs are excluded from the official binary MI branch; Subject 88 rate exception must be recorded and resampled deterministically

### 4.2 BNCI2014_001

**Role:** standard four-class MI benchmark companion; official P01 binary left/right branch  
**Official identity:** BNCI Horizon 2020 dataset 001-2014 / BCI Competition IV dataset 2a  
**Citation:** Tangermann M, Müller KR, Aertsen A, et al. Review of the BCI Competition IV. Frontiers in Neuroscience. 2012;6:55. DOI 10.3389/fnins.2012.00055.  
**Reference:** https://bnci-horizon-2020.eu/database/data-sets; https://moabb.neurotechx.com/docs/generated/moabb.datasets.BNCI2014_001.html; https://doi.org/10.3389/fnins.2012.00055  
**Checksum policy:** COMPUTE_SHA256_PER_GDF/MAT_FILE_AND_FREEZE_AGGREGATE_BEFORE_ADMISSION  
**Expected structure:** 9 subjects; 2 sessions; 6 runs/session; 48 trials/run; 576 trials/subject across four classes; P01 retains left/right classes only.  
**Labels:** 769/left_hand; 770/right_hand; 771/feet; 772/tongue; 1023/rejected trial plus technical markers  
**Limitations:** Feet and tongue are preserved as excluded source labels in the official binary branch; EOG channels are metadata/quality channels and not model input; CC BY-ND restrictions prohibit redistributed derived raw-signal variants

### 4.3 Lee2019_MI

**Role:** maximum-scope two-session left/right MI target companion  
**Official identity:** OpenBMI motor-imagery corpus, GigaDB dataset 100542, exposed by MOABB Lee2019_MI  
**Citation:** Lee MH, Kwon OY, Kim YJ, et al. EEG dataset and OpenBMI toolbox for three BCI paradigms: an investigation into BCI illiteracy. GigaScience. 2019;8(5):giz002. DOI 10.1093/gigascience/giz002; data DOI 10.5524/100542.  
**Reference:** https://moabb.neurotechx.com/docs/generated/moabb.datasets.Lee2019_MI.html; https://doi.org/10.1093/gigascience/giz002; https://doi.org/10.5524/100542  
**Checksum policy:** COMPUTE_SHA256_PER_SOURCE_ARCHIVE/FILE_AND_FREEZE_AGGREGATE_BEFORE_ADMISSION  
**Expected structure:** 54 subjects; 2 sessions; 62 EEG channels; 1000 Hz; left/right MI; 4-second trials; labeled offline/train runs only.  
**Labels:** left_hand; right_hand; online/test MI events excluded because classification labels are unavailable or restricted  
**Limitations:** Online/test runs are excluded from supervised P01 records; High-rate source requires deterministic anti-aliased resampling; Source phase and session must remain in lineage

### 4.4 Cho2017

**Role:** subject-diverse left/right MI fallback  
**Official identity:** Cho et al. motor-imagery EEG corpus, GigaDB dataset 100295, MOABB Cho2017 wrapper  
**Citation:** Cho H, Ahn M, Ahn S, Kwon M, Jun SC. EEG datasets for motor imagery brain-computer interface. GigaScience. 2017;6(7):gix034. DOI 10.1093/gigascience/gix034; data DOI 10.5524/100295.  
**Reference:** https://moabb.neurotechx.com/docs/generated/moabb.datasets.Cho2017.html; https://doi.org/10.1093/gigascience/gix034; https://doi.org/10.5524/100295  
**Checksum policy:** COMPUTE_AND_FREEZE_ONLY_IF_ACTIVATED_BY_VERSIONED_AMENDMENT  
**Expected structure:** 52 subjects; 1 session; 64 EEG plus 4 EMG; 512 Hz; left/right MI; 3-second trials; provider bad-trial indices.  
**Labels:** left_hand; right_hand  
**Limitations:** One-session structure weakens cross-session analysis; Screened source is not silently promoted

### 4.5 GuttmannFlury2025_MI

**Role:** current-delta three-session MI candidate  
**Official identity:** Guttmann-Flury et al. Eye-BCI multimodal motor-imagery dataset; MOABB GuttmannFlury2025_MI BDF/Zenodo conversion  
**Citation:** Guttmann-Flury and colleagues. Three-session motor imagery/motor execution EEG dataset. Scientific Data. 2025. DOI 10.1038/s41597-025-04861-9.  
**Reference:** https://zenodo.org/records/18970793; https://doi.org/10.5281/zenodo.18970793; https://doi.org/10.7303/syn64005218; https://moabb.neurotechx.com/docs/generated/moabb.datasets.GuttmannFlury2025_MI.html; https://doi.org/10.1038/s41597-025-04861-9  
**Checksum policy:** COMPUTE_AND_FREEZE_ONLY_IF_ACTIVATED_BY_VERSIONED_AMENDMENT  
**Expected structure:** 31 subjects; 1-3 sessions per subject (63 sessions total); 40 trials/session (20 left, 20 right); 62 scalp EEG + 2 mastoid + 1 EOG + 1 STIM = 66 channels; 1000 Hz; right-mastoid reference; 2 s fixation + 4 s imagery + 1-1.5 s rest.  
**Labels:** left_hand_mi; right_hand_mi; motor-execution labels excluded from MI-only future branch  
**Limitations:** Not active; the official P01 freeze does not download or process it; any later promotion must preserve the 62-EEG/2-mastoid/EOG/STIM channel taxonomy, the variable 1-3-session structure and MI-only event semantics; the Zenodo data release is CC0 while the associated article's publication license is a separate surface

## 5. Label-map freeze

The official task is binary left-hand versus right-hand motor imagery. Every original event is preserved; exclusion is explicit. PhysioNet T1/T2 is interpreted only in imagery runs 4, 8 and 12. BNCI feet/tongue and technical events remain source records but are excluded from the harmonized branch. Lee online/test unlabeled events are excluded. Unknown events block the affected source event rather than being guessed.

The exact machine-readable map is `p01_l1_label_mapping_freeze_R1.yaml`.

## 6. Preprocessing freeze

The single official profile is:

```text
validate units as volts
→ capture source events and original sample indices before channel dropping/resampling
→ select EEG channels while retaining auxiliary-channel metadata
→ demean each continuous run
→ common-average reference
→ jointly resample continuous EEG and event onsets to 160 Hz with the pinned MNE polyphase path
→ fourth-order zero-phase Butterworth SOS band-pass at 8-32 Hz
→ float32 output and preserve original/resampled event indices
```

There is no Layer 1 train-fitted standardization and no held-out-statistic use. The official derived profile is: validate/convert to volts -> capture original event onsets and source sample indices before channel dropping or resampling -> EEG channels only -> per-run demeaning -> average reference -> jointly resample the continuous EEG and event array to 160 Hz with MNE's event-aware polyphase path -> fourth-order 8-32 Hz Butterworth SOS zero-phase filtering -> float32. No train-fitted transform is used. The original and returned resampled event indices are both retained in lineage; independent float-time reconstruction of event samples is prohibited.

A separate notch is disabled because the final 32 Hz high cutoff excludes 50/60 Hz. Provider preprocessing history is recorded and never overwritten.

## 7. Split freeze

| Dataset | train | calibration | validation | test |
|---|---|---|---|---|
| PhysioNetMI | 65 | 22 | 11 | 11 |
| BNCI2014_001 | 5 | 2 | 1 | 1 |
| Lee2019_MI | 32 | 11 | 5 | 6 |

The split unit is subject. The exact role ratio is 0.60/0.20/0.10/0.10 with seed `20260804`. Subjects are SHA-256 ranked and assigned by largest remainder with a minimum of one subject per role. Sessions, runs, events and windows cannot cross subject-role boundaries.

## 8. Low-calibration budget freeze

The calibration role produces nested, class-balanced subsets of `1, 2, 4, 8, 16, 32` source events per class using seed `20260804`. Selection uses source-event identities only and never observes validation/test outcomes. Insufficient support marks that budget diagnostic-only; it never borrows held-out events.

## 9. Window freeze

Each included event yields exactly one 3.0-second window from cue `+0.5 s` to `+3.5 s`. The event anchor is the event sample returned by the jointly resampled event array, not a separately rounded floating-point timestamp. At 160 Hz the window adds an exact start offset of `80` samples and uses duration/stride `480` samples. Each record retains both the original-source and resampled event samples. Out-of-bounds windows are rejected; they are never clipped. The parent source event is the overlap group and immutable lineage root.

## 10. Quality freeze

Quality is annotation-only. Hard invalid states are nonfinite values, invalid shape/duration and missing source-event lineage. Soft flags include exactly zero channel standard deviation after demeaning (`0 V`, an exact flat-line detector), absolute amplitude above `5e-4 V` (500 µV, a conservative impossible-amplitude warning), provider bad-channel/trial flags, and at least 160 repeated identical samples. No automatic interpolation, deletion or repair is permitted. Threshold distributions are exported so any later change is a versioned repair, not silent retuning.

## 11. Kaggle environment freeze

- Container: `gcr.io/kaggle-images/python:v168` with immutable digest recorded in the environment freeze.
- Python: 3.11 line defined by the immutable image; exact patch is captured in `environment_manifest.json` before execution.
- Accelerator: CPU.
- Internet: enabled for official provider downloads.
- MOABB: 1.5.0; MNE: 1.12.1; all other package versions are pinned in the machine-readable environment freeze.
- Resources: at least 16 GB RAM and 60 GB free disk; 30 GB/90 GB recommended.
- Execution: sequential dataset processing and dataset-level checkpoints; resume only when source/config hashes match.

## 12. Official run matrix

| run_cell_id | dataset_id | task | preprocessing_profile | split_protocol | budget_profile | window_profile | quality_profile | required_gates | output_scope |
|---|---|---|---|---|---|---|---|---|---|
| P01-RUN-PHYSIONETMI | PhysioNetMI | BINARY_LEFT_RIGHT_MI | P01-L1-PREPROCESS-OFFICIAL-R1 | P01-L1-SPLIT-OFFICIAL-R1 | P01-L1-LOW-CAL-OFFICIAL-R1 | P01-L1-WINDOW-OFFICIAL-R1 | P01-L1-QUALITY-OFFICIAL-R1 | P01-G01..P01-G16 | all canonical/supporting P01 outputs for dataset |
| P01-RUN-BNCI2014_001 | BNCI2014_001 | BINARY_LEFT_RIGHT_MI | P01-L1-PREPROCESS-OFFICIAL-R1 | P01-L1-SPLIT-OFFICIAL-R1 | P01-L1-LOW-CAL-OFFICIAL-R1 | P01-L1-WINDOW-OFFICIAL-R1 | P01-L1-QUALITY-OFFICIAL-R1 | P01-G01..P01-G16 | all canonical/supporting P01 outputs for dataset |
| P01-RUN-LEE2019_MI | Lee2019_MI | BINARY_LEFT_RIGHT_MI | P01-L1-PREPROCESS-OFFICIAL-R1 | P01-L1-SPLIT-OFFICIAL-R1 | P01-L1-LOW-CAL-OFFICIAL-R1 | P01-L1-WINDOW-OFFICIAL-R1 | P01-L1-QUALITY-OFFICIAL-R1 | P01-G01..P01-G16 | all canonical/supporting P01 outputs for dataset |
| P01-RUN-CROSS-DATASET-CLOSURE | ALL_ACTIVE | MANIFEST_GATE_AND_HANDOFF_CLOSURE | P01-L1-PREPROCESS-OFFICIAL-R1 | P01-L1-SPLIT-OFFICIAL-R1 | P01-L1-LOW-CAL-OFFICIAL-R1 | P01-L1-WINDOW-OFFICIAL-R1 | P01-L1-QUALITY-OFFICIAL-R1 | P01-G01..P01-G16 | Layer1Manifest, readiness, cards, gate decision, P02/later handoffs, complete bundle |

## 13. Exact artifact and gate mapping

All existing R2 canonical and supporting outputs remain required. Every source-specific record uses the frozen dataset, label, preprocessing, split, budget, window and quality identities. P01-G02 cannot pass until official bytes are downloaded and their per-file/aggregate hashes are frozen. P01-G04-G11 validate the exact frozen profiles. P01-G12 proves fourteen A0-A13 readiness rows and A14 absence. P01-G13-G16 close cards, manifests, paths, P02 compatibility and the complete execution bundle.

A material source/config change invalidates affected descendants and requires a new freeze revision, notebook/input identity and run ID.

## 14. Evidence-insufficiency repair versioning

Only the Governance V6.1 loop is permitted:

```text
preserve failed run and bundle
→ identify source/config/code owner
→ amend the minimum scope
→ issue new freeze/config/notebook/run identities
→ rerun affected branch or all descendants when an upstream identity changes
→ regenerate the complete bundle
→ reevaluate P01-G01-P01-G16
```

No same-identity silent correction is lawful.

## 15. Protocol v1.0 inheritance contract

The future P01 Protocol v1 annex must import `p01_l1_official_run_configuration_freeze_R1.yaml` and the actual execution identities. It may report deviations and versioned reruns; it may not select different values retrospectively or describe result-dependent changes as pre-registered.

## 16. Notebook correction contract

The R3 notebook is not the executable final because it predates this freeze. `p01_l1_notebook_correction_contract_R1.yaml` defines the controlled R4 correction: official MOABB adapters, exact maps, event-aware joint signal/event resampling, preprocessing operations, exact grouped split allocation, offset windows, quality checks, source checksum admission, package pins and full artifact/card/handoff propagation. The next notebook task must implement the contract without reopening the scientific choices.

## 17. Zero-unresolved-state certification

The context-aware audit scans active-run fields in the current R3 annex and machine-readable package. Historical R2 text is retained below as superseded provenance and is excluded from current-value evaluation. Current active-run configuration contains no null, empty mapping, unresolved token, deferred value or owner-choice placeholder.

**Terminal status:** `P01_L1_IMPLEMENTATION_FULLY_INSTANTIATED_FOR_NOTEBOOK_CORRECTION`.

## 18. Boundary statement

This package freezes the official run but does not execute it. It does not claim source download success, P01 evidence, Protocol v1 completion, Phase Analysis, Layer 0 disposition, Evidence Map update, Layer 10 completion, P01 closure or P02 authorization.


# Preserved predecessor annex R2 - historical, superseded and non-controlling

> The complete R2 predecessor follows without omission. Current values are controlled by Sections 1-18 above.

---
title: "IHARQ BenchGuard Stretch C - Phase 1 / Layer 1 Integrated Implementation and Execution Annex"
document_id: "IHARQ-IBB-P01-L1-ANNEX-R2"
revision: "R2"
date: "2026-08-04"
status: "INDEPENDENT-AUDIT-REPAIRED-AND-PASS; KAGGLE-NOTEBOOK-NOT-YET-CREATED; P01-NOT-EXECUTED"
parent_build_book: "IHARQ-IBB-R8-P01-L1-INDEPENDENT-AUDIT-REPAIRED"
governing_workflow: "Governance V6.1"
supersedes: "IHARQ-IBB-P01-L1-ANNEX-R1"
---

# IHARQ Phase 1 / Layer 1 Integrated Implementation and Execution Annex R2

> **Current controlling successor.** R2 repairs the R1 implementation authority after an independent source reconstruction. It remains a design and implementation authority only. It does not claim a Kaggle run, official dataset validation, P01 evidence, Protocol v1 completion, Phase Analysis, Layer 0 disposition, Evidence Map update, Layer 10 completion, P01 closure, or P02 authorization.

# 1. Independent Audit Repair Decision

The R1 target, parent continuity, eleven official Layer 1 responsibilities, selected dataset strategy, single-notebook direction, A0-A13 readiness boundary, A14 rejection, and Phase 0 reuse logic were substantially correct. The independent audit nevertheless found four major documentary/package defects:

1. `AUTHORITY_USE_UNTRACEABLE` - R1 source-utilization rows did not provide exact source locations per requirement.
2. `ARTIFACT_MANIFEST_LINK_MISSING` and `ARTIFACT_VALIDATOR_MISSING` - R1 artifact closure rows used generic producers/paths and omitted required validators, tests, gates, manifest links, and failure behavior.
3. `KAGGLE_SPEC_INCOMPLETE` / `EXECUTION_BUNDLE_INCOMPLETE` - the six-hundred-byte R1 notebook companion was an outline, not an immediately actionable full-scope execution contract.
4. `PHASE2_HANDOFF_INCOMPLETE` - the R1 handoff listed artifacts but did not define profiles, validators, terminal states, invalidation, acknowledgment, or later consumers.
5. `WORD_DELIVERY_INCOMPLETE` - the R1 Master Word edition contained only the current annex/control material rather than the complete inherited Build Book body requested by the owner.

All defects are within Build Book/documentary packaging authority. No Architecture, Registry, Plan, Protocol v0.1, Playbook, Method Selection, Nuts-and-Bolts, or Phase 0 scientific artifact requires change.

# 2. Controlling Relationship and Precedence

- Parent: `IHARQ-IBB-R8-P01-L1-INDEPENDENT-AUDIT-REPAIRED`.
- Predecessor annex: `IHARQ-IBB-P01-L1-ANNEX-R1`, preserved under `history/`.
- R2 controls all P01/L1 implementation design, machine companions, notebook specification, artifact closure, gates, and handoff where it is more specific.
- The complete valid R1 annex remains preserved after the current R2 control sections for provenance.
- Governance V6.1 controls over stale historical Mode A/B/C, smoke-track, GitHub-primary, and CI-gate statements in inherited predecessor text.

# 3. Exact Authority and Requirement Closure

R2 uses the independent source-reconstruction and requirement-closure matrices. Every row provides an authority ID, exact section, obligation, current document location, companion and closure status.

- Source reconstruction: `independent_audit/IHARQ_P01_L1_Independent_Source_Reconstruction_Matrix_R1.csv`.
- Requirement closure: `independent_audit/IHARQ_P01_L1_Independent_Requirement_Closure_Matrix_R1.csv`.
- Current source utilization: `reports/phase_01_implementation/p01_l1_source_utilization_matrix_R2.csv`.

# 4. Phase 0 Reuse and Invalidation

The R6 Phase 0 Build Book and P00 annex are preserved. R2 reuses stable identity, serialization, hashing, lifecycle, lineage, schemas, validation, fixtures, CLI, Layer 0 and Layer 10 boundaries. It requires P01-specific repair only for the empty P01 artifact profile, execution environment, Layer 1 implementation stub, P01 fixtures, and consumer-specific commands. See `p01_l1_phase0_reuse_and_invalidation_matrix_R2.csv`.

# 5. P01/L1 Scope and Boundaries

- **Target:** `P01 - Public Data and Split Protocol`.
- **Primary implementation owner:** `L1 - Public-Data and Protocol Anchor`.
- **L0:** supplies and later adjudicates claim/limitation boundaries; it does not implement data processing.
- **L10:** future read-only consumer; it does not recompute, repair, or promote evidence.
- **Excluded:** decoder training/performance, calibration, IHARQ, RegimeRisk, policies, stress, embodiment, final claims, and downstream ablation performance.

# 6. Dataset and Source Strategy

The Build Book may implement adapters only for the statuses accepted by Method Selection. It may not decide dataset scientific role. Exact source revision, license, checksum, citation and access are P01-G02 prerequisites. The current portfolio remains: primary/accepted MI sources as recorded by Method Selection (including PhysioNetMI/EEGMMI, BNCI2014_001/BCI IV-2a, and Lee2019_MI/OpenBMI); Cho2017 and GuttmannFlury2025_MI remain screened or conditional according to the controlling register. No candidate is promoted by implementation convenience.

# 7. Complete Physical Architecture

```text
src/iharq/layer1_data_protocol/
  __init__.py
  models.py
  dataset_registry.py
  adapters/base.py
  adapters/physionet_mi.py
  adapters/bnci2014_001.py
  adapters/lee2019_mi.py
  metadata.py
  labels.py
  preprocessing.py
  quality.py
  splits.py
  budgets.py
  windows.py
  validation.py
  leakage.py
  cards.py
  readiness.py
  manifests.py
  bundle.py
  pipeline.py
  kaggle_adapter.py
```

Config families are `configs/datasets/`, `configs/preprocessing/`, `configs/splits/`, `configs/budgets/`, `configs/windows/`, `configs/quality/`, `configs/validation/`, and `configs/cards/`. Tests mirror modules under `tests/layer1/`; generated outputs follow the exact path classes in the R2 artifact matrix.

# 8. Detailed Module Dossiers

## L1-MOD-01 - Dataset registry manager

- **Physical capability:** `L1-01`
- **Paths:** `dataset_registry.py`
- **Typed inputs:** DatasetSourceProfile, DatasetAdmissionDecision.
- **Public interfaces:** `resolve_alias; verify_source; admit_dataset; emit_dataset_record`.
- **Outputs:** DatasetRecord; source/version/license report.
- **Configuration:** only typed dataset/preprocessing/split/budget/window/quality/validation/card/manifest fields applicable to this module; unresolved numerical values remain execution prerequisites.
- **Invariants:** deterministic identity; idempotent rerun; source-faithful provenance; explicit missingness; fail-closed validation; no held-out fit leakage; no silent repair.
- **Validators:** schema, source-fact, identity/hash, lineage/lifecycle, and module-specific invariant checks.
- **Tests:** unit, valid/invalid fixture, property, failure reason, idempotence, integration, and clean-reproduction coverage.
- **Stable reason codes:** `SOURCE_UNRESOLVED; LICENSE_UNRESOLVED; CHECKSUM_MISMATCH; DATASET_NOT_ADMITTED`.
- **Downstream:** P02-P15 plus Layer 0/Evidence Map/Layer 10 only on their lawful surfaces.
## L1-MOD-02 - Dataset loader

- **Physical capability:** `L1-02`
- **Paths:** `adapters/base.py; adapters/<dataset>.py`
- **Typed inputs:** DatasetSourceProfile, AccessContext.
- **Public interfaces:** `probe; download_or_resolve_cache; load_source; enumerate_events`.
- **Outputs:** raw source inventory; loader provenance; DatasetRecord updates.
- **Configuration:** only typed dataset/preprocessing/split/budget/window/quality/validation/card/manifest fields applicable to this module; unresolved numerical values remain execution prerequisites.
- **Invariants:** deterministic identity; idempotent rerun; source-faithful provenance; explicit missingness; fail-closed validation; no held-out fit leakage; no silent repair.
- **Validators:** schema, source-fact, identity/hash, lineage/lifecycle, and module-specific invariant checks.
- **Tests:** unit, valid/invalid fixture, property, failure reason, idempotence, integration, and clean-reproduction coverage.
- **Stable reason codes:** `SOURCE_UNAVAILABLE; ACCESS_DENIED; FORMAT_UNSUPPORTED; SOURCE_COUNT_DRIFT`.
- **Downstream:** P02-P15 plus Layer 0/Evidence Map/Layer 10 only on their lawful surfaces.
## L1-MOD-03 - Metadata normalizer

- **Physical capability:** `L1-03`
- **Paths:** `metadata.py`
- **Typed inputs:** source metadata and loader inventory.
- **Public interfaces:** `normalize_hierarchy; normalize_channels; normalize_sampling; record_conflict`.
- **Outputs:** DatasetRecord; metadata completeness report.
- **Configuration:** only typed dataset/preprocessing/split/budget/window/quality/validation/card/manifest fields applicable to this module; unresolved numerical values remain execution prerequisites.
- **Invariants:** deterministic identity; idempotent rerun; source-faithful provenance; explicit missingness; fail-closed validation; no held-out fit leakage; no silent repair.
- **Validators:** schema, source-fact, identity/hash, lineage/lifecycle, and module-specific invariant checks.
- **Tests:** unit, valid/invalid fixture, property, failure reason, idempotence, integration, and clean-reproduction coverage.
- **Stable reason codes:** `REQUIRED_METADATA_MISSING; METADATA_CONFLICT; HIERARCHY_INVALID`.
- **Downstream:** P02-P15 plus Layer 0/Evidence Map/Layer 10 only on their lawful surfaces.
## L1-MOD-04 - Task and label ontology mapper

- **Physical capability:** `L1-04`
- **Paths:** `labels.py`
- **Typed inputs:** original labels, task profile.
- **Public interfaces:** `map_label; validate_mapping; classify_exclusion`.
- **Outputs:** LabelMapRecord; label validation report.
- **Configuration:** only typed dataset/preprocessing/split/budget/window/quality/validation/card/manifest fields applicable to this module; unresolved numerical values remain execution prerequisites.
- **Invariants:** deterministic identity; idempotent rerun; source-faithful provenance; explicit missingness; fail-closed validation; no held-out fit leakage; no silent repair.
- **Validators:** schema, source-fact, identity/hash, lineage/lifecycle, and module-specific invariant checks.
- **Tests:** unit, valid/invalid fixture, property, failure reason, idempotence, integration, and clean-reproduction coverage.
- **Stable reason codes:** `LABEL_UNKNOWN; LABEL_AMBIGUOUS; TASK_INCOMPATIBLE; PROXY_LIMITATION_MISSING`.
- **Downstream:** P02-P15 plus Layer 0/Evidence Map/Layer 10 only on their lawful surfaces.
## L1-MOD-05 - Preprocessing registry and lawful executor

- **Physical capability:** `L1-05`
- **Paths:** `preprocessing.py`
- **Typed inputs:** source signal, preprocessing config, split fit population.
- **Public interfaces:** `compile_pipeline; fit_train_only; transform; emit_record`.
- **Outputs:** PreprocessingRecord; fit-scope report; derived signal pointers.
- **Configuration:** only typed dataset/preprocessing/split/budget/window/quality/validation/card/manifest fields applicable to this module; unresolved numerical values remain execution prerequisites.
- **Invariants:** deterministic identity; idempotent rerun; source-faithful provenance; explicit missingness; fail-closed validation; no held-out fit leakage; no silent repair.
- **Validators:** schema, source-fact, identity/hash, lineage/lifecycle, and module-specific invariant checks.
- **Tests:** unit, valid/invalid fixture, property, failure reason, idempotence, integration, and clean-reproduction coverage.
- **Stable reason codes:** `FIT_SCOPE_LEAKAGE; UNSUPPORTED_OPERATION; CHANNEL_POLICY_FAILURE; NONDETERMINISTIC_TRANSFORM`.
- **Downstream:** P02-P15 plus Layer 0/Evidence Map/Layer 10 only on their lawful surfaces.
## L1-MOD-06 - Artifact and channel-quality annotator

- **Physical capability:** `L1-06`
- **Paths:** `quality.py`
- **Typed inputs:** source/derived signals and source quality metadata.
- **Public interfaces:** `annotate_channels; annotate_trials; annotate_windows; summarize_coverage`.
- **Outputs:** ArtifactFlagRecord; quality coverage report.
- **Configuration:** only typed dataset/preprocessing/split/budget/window/quality/validation/card/manifest fields applicable to this module; unresolved numerical values remain execution prerequisites.
- **Invariants:** deterministic identity; idempotent rerun; source-faithful provenance; explicit missingness; fail-closed validation; no held-out fit leakage; no silent repair.
- **Validators:** schema, source-fact, identity/hash, lineage/lifecycle, and module-specific invariant checks.
- **Tests:** unit, valid/invalid fixture, property, failure reason, idempotence, integration, and clean-reproduction coverage.
- **Stable reason codes:** `QUALITY_SOURCE_ABSENT; BAD_CHANNEL_POLICY_UNRESOLVED; SILENT_REPAIR_ATTEMPT`.
- **Downstream:** P02-P15 plus Layer 0/Evidence Map/Layer 10 only on their lawful surfaces.
## L1-MOD-07 - Split and protocol manager

- **Physical capability:** `L1-07`
- **Paths:** `splits.py; budgets.py`
- **Typed inputs:** DatasetRecord, LabelMapRecord, split/budget configs.
- **Public interfaces:** `build_groups; assign_roles; allocate_budget; verify_disjointness`.
- **Outputs:** SplitRecord; budget table; attrition report.
- **Configuration:** only typed dataset/preprocessing/split/budget/window/quality/validation/card/manifest fields applicable to this module; unresolved numerical values remain execution prerequisites.
- **Invariants:** deterministic identity; idempotent rerun; source-faithful provenance; explicit missingness; fail-closed validation; no held-out fit leakage; no silent repair.
- **Validators:** schema, source-fact, identity/hash, lineage/lifecycle, and module-specific invariant checks.
- **Tests:** unit, valid/invalid fixture, property, failure reason, idempotence, integration, and clean-reproduction coverage.
- **Stable reason codes:** `SUBJECT_OVERLAP; SESSION_OVERLAP; SOURCE_EVENT_OVERLAP; BUDGET_CONTAMINATION`.
- **Downstream:** P02-P15 plus Layer 0/Evidence Map/Layer 10 only on their lawful surfaces.
## L1-MOD-08 - Trial/window generator

- **Physical capability:** `L1-08`
- **Paths:** `windows.py`
- **Typed inputs:** source events/trials, SplitRecord, PreprocessingRecord, window config.
- **Public interfaces:** `generate_windows; assign_overlap_group; inherit_lineage; validate_boundaries`.
- **Outputs:** WindowRecord; window timing/overlap report.
- **Configuration:** only typed dataset/preprocessing/split/budget/window/quality/validation/card/manifest fields applicable to this module; unresolved numerical values remain execution prerequisites.
- **Invariants:** deterministic identity; idempotent rerun; source-faithful provenance; explicit missingness; fail-closed validation; no held-out fit leakage; no silent repair.
- **Validators:** schema, source-fact, identity/hash, lineage/lifecycle, and module-specific invariant checks.
- **Tests:** unit, valid/invalid fixture, property, failure reason, idempotence, integration, and clean-reproduction coverage.
- **Stable reason codes:** `WINDOW_OUT_OF_BOUNDS; PARENT_LINEAGE_MISSING; OVERLAP_GROUP_COLLISION; SPLIT_INHERITANCE_MISMATCH`.
- **Downstream:** P02-P15 plus Layer 0/Evidence Map/Layer 10 only on their lawful surfaces.
## L1-MOD-09 - Data validation and leakage auditor

- **Physical capability:** `L1-09`
- **Paths:** `validation.py; leakage.py`
- **Typed inputs:** all records/configs/source inventories.
- **Public interfaces:** `validate_schema; audit_leakage; reconcile_counts; validate_matching_keys`.
- **Outputs:** ValidationReport; leakage report; matched-key report.
- **Configuration:** only typed dataset/preprocessing/split/budget/window/quality/validation/card/manifest fields applicable to this module; unresolved numerical values remain execution prerequisites.
- **Invariants:** deterministic identity; idempotent rerun; source-faithful provenance; explicit missingness; fail-closed validation; no held-out fit leakage; no silent repair.
- **Validators:** schema, source-fact, identity/hash, lineage/lifecycle, and module-specific invariant checks.
- **Tests:** unit, valid/invalid fixture, property, failure reason, idempotence, integration, and clean-reproduction coverage.
- **Stable reason codes:** `SCHEMA_INVALID; LEAKAGE_DETECTED; COUNT_MISMATCH; MATCH_KEY_MISSING`.
- **Downstream:** P02-P15 plus Layer 0/Evidence Map/Layer 10 only on their lawful surfaces.
## L1-MOD-10 - Dataset-card and protocol-card generator

- **Physical capability:** `L1-10A`
- **Paths:** `cards.py`
- **Typed inputs:** accepted records/manifests/limitations.
- **Public interfaces:** `build_dataset_card; build_protocol_card; verify_source_parity`.
- **Outputs:** DatasetCard; ProtocolCard.
- **Configuration:** only typed dataset/preprocessing/split/budget/window/quality/validation/card/manifest fields applicable to this module; unresolved numerical values remain execution prerequisites.
- **Invariants:** deterministic identity; idempotent rerun; source-faithful provenance; explicit missingness; fail-closed validation; no held-out fit leakage; no silent repair.
- **Validators:** schema, source-fact, identity/hash, lineage/lifecycle, and module-specific invariant checks.
- **Tests:** unit, valid/invalid fixture, property, failure reason, idempotence, integration, and clean-reproduction coverage.
- **Stable reason codes:** `CARD_SOURCE_DRIFT; LIMITATION_MISSING; FORBIDDEN_CLAIM_TEXT`.
- **Downstream:** P02-P15 plus Layer 0/Evidence Map/Layer 10 only on their lawful surfaces.
## L1-MOD-11 - Provenance and manifest builder

- **Physical capability:** `L1-10B`
- **Paths:** `manifests.py; bundle.py; readiness.py`
- **Typed inputs:** all outputs, tests, gates, configs, environment.
- **Public interfaces:** `build_layer1_manifest; build_readiness; build_bundle; verify_hash_closure`.
- **Outputs:** Layer1Manifest; readiness JSON; output/test/gate manifests; handoff.
- **Configuration:** only typed dataset/preprocessing/split/budget/window/quality/validation/card/manifest fields applicable to this module; unresolved numerical values remain execution prerequisites.
- **Invariants:** deterministic identity; idempotent rerun; source-faithful provenance; explicit missingness; fail-closed validation; no held-out fit leakage; no silent repair.
- **Validators:** schema, source-fact, identity/hash, lineage/lifecycle, and module-specific invariant checks.
- **Tests:** unit, valid/invalid fixture, property, failure reason, idempotence, integration, and clean-reproduction coverage.
- **Stable reason codes:** `MANIFEST_INCOMPLETE; HASH_MISMATCH; PATH_UNRESOLVED; A14_PRESENT`.
- **Downstream:** P02-P15 plus Layer 0/Evidence Map/Layer 10 only on their lawful surfaces.

# 9. Canonical and Governed Artifact Closure

| Artifact | Canonicality | Producer | Exact path class | Validator | Gates | Consumers |
|---|---|---|---|---|---|---|
| `DatasetRecord` | CANONICAL | `L1-MOD-01/L1-MOD-03` | `records/datasets/<dataset_id>/<record_id>.json` | `validate_schema+source_identity` | `P01-G02/P01-G03` | P02-P15 |
| `WindowRecord` | CANONICAL | `L1-MOD-08` | `records/windows/<dataset_id>/<split_id>/<record_id>.json` | `validate_schema+window_lineage` | `P01-G03/P01-G10` | P02-P15 |
| `SplitRecord` | CANONICAL | `L1-MOD-07` | `records/splits/<protocol_id>/<record_id>.json` | `validate_schema+disjointness` | `P01-G07/P01-G08/P01-G09` | P02-P15 |
| `PreprocessingRecord` | CANONICAL | `L1-MOD-05` | `records/preprocessing/<profile_id>/<record_id>.json` | `validate_schema+fit_scope` | `P01-G03/P01-G06` | P02-P15 |
| `LabelMapRecord` | CANONICAL | `L1-MOD-04` | `records/labels/<dataset_id>/<record_id>.json` | `validate_schema+label_coverage` | `P01-G03/P01-G05` | P02-P15 |
| `ArtifactFlagRecord` | CANONICAL_WHERE_SUPPORTED | `L1-MOD-06` | `records/quality/<dataset_id>/<record_id>.json` | `validate_schema+source_support` | `P01-G03/P01-G11` | P02-P15 |
| `ValidationReport` | CANONICAL | `L1-MOD-09` | `reports/phase_01/validation/<report_id>.json` | `validate_schema+gate_reconciliation` | `P01-G03..P01-G16` | Protocol/Analysis/P02-P15 |
| `Layer1Manifest` | CANONICAL_MANIFEST | `L1-MOD-11` | `manifests/phase_01/layer1_manifest.json` | `validate_schema+hash/path closure` | `P01-G14/P01-G16` | All consumers |
| `DatasetCard` | GOVERNED_ARTIFACT | `L1-MOD-10` | `docs/cards/datasets/<dataset_id>.md` | `card_source_parity` | `P01-G13` | Layer0/L10/P02-P15 |
| `ProtocolCard` | GOVERNED_ARTIFACT | `L1-MOD-10` | `docs/cards/protocols/<protocol_id>.md` | `card_source_parity` | `P01-G13` | Layer0/L10/P02-P15 |
| `AblationReadiness` | GOVERNED_READINESS | `L1-MOD-11` | `manifests/phase_01/layer1_ablation_readiness_l1_v1.json` | `readiness_row_completeness+A14_absence` | `P01-G12` | P02-P15 |

Supporting reports, manifests, gate evidence, negative registers, execution-bundle manifest and P02 handoff are separately closed in `p01_l1_expected_output_and_artifact_closure_R2.csv`. A referenced output without a validator, gate, path and manifest link is not closed.

# 10. Configuration Contract

The implementation must expose typed fields without inventing unresolved values:

- **Dataset profile:** dataset ID/aliases, role/status, source/revision, DOI/URL, license, access method, checksum, adapter, task, subject/session/run/event/channel/sampling facts, inclusion/exclusion and limitations.
- **Preprocessing profile:** source-native versus derived operations, units, resampling, filters, referencing, channel policy, normalization, fit scope, transform ordering and deterministic config identity.
- **Split profile:** split unit, grouping keys, roles, deterministic seed, stratification rules, repetition/fold identity, purge/embargo/overlap rules and attrition policy.
- **Budget profile:** allocation unit, class-aware rule, permitted fit roles, deterministic seed, budget IDs and insufficient-class behavior.
- **Window profile:** event anchor, start/end/duration, stride, overlap group, bounds policy, label/quality/split inheritance and invalid-window behavior.
- **Quality profile:** source-supported fields, missingness, bad-channel/trial/window thresholds only when authority/config approves them, and no silent repair.
- **Validation/card/manifest profiles:** required gates, status/reason vocabulary, limitation inheritance, source parity, output paths and hash closure.

# 11. Preprocessing, Split, Budget and Window Algorithms

1. Resolve and hash the effective config before data transformation.
2. Preserve source-native bytes/inventory and original metadata.
3. Build group identities and split roles before any fit operation and before window materialization when the source-event atomicity rule requires it.
4. Fit preprocessing only on the declared legal population; serialize fit identity and population hash.
5. Apply deterministic transforms without reading held-out statistics.
6. Allocate low-calibration budgets from eligible training/calibration source events only; use class-aware deterministic selection and explicit insufficiency status.
7. Generate windows from immutable parent source-event/trial identity, inherit split/label/preprocessing/quality lineage, and assign overlap groups.
8. Audit all group intersections, duplicate source lineage, fit population, budget membership, timing bounds and overlap/purge rules.
9. Reject or downgrade affected branches with stable reason codes; preserve failed evidence.

# 12. Full-Scope Kaggle Notebook Specification

The single notebook is `IHARQ_Phase_01_Layer_01_Complete_Public_Data_and_Split_Execution_R1.ipynb`. One notebook is an organization rule only. It must execute every required dataset branch, Layer 1 responsibility, validation, readiness row, card, report and manifest.

| Index | Section | Definition of done |
|---|---|---|
| 00 | Title/control | Record P01/L1 IDs, authority hashes, notebook hash, intended bundle ID. |
| 01 | Environment | Install exact pinned dependencies; capture Python/CUDA/package/environment identity. |
| 02 | Cumulative ZIP intake | Verify ZIP/hash/manifest/safe extraction; resolve P00 Build Book and P01 contracts. |
| 03 | Authority/config resolution | Load authority manifest, dataset/preprocess/split/budget/window/quality profiles; calculate semantic hashes. |
| 04 | P00 foundation regression | Run package import, schema/config/contract, identity/hash/lifecycle and A14 rejection checks. |
| 05 | Dataset source resolution | Resolve exact active sources, revisions, licenses, checksums, citations, access and cache paths. |
| 06 | Dataset registry | Create admission decisions, DatasetRecord roots and inclusion/exclusion reports. |
| 07 | Source acquisition/loading | Download or resolve cache; verify bytes; load source-faithful events and source inventory. |
| 08 | Metadata normalization | Normalize hierarchy/channels/sampling while preserving original values, conflicts and missingness. |
| 09 | Label mapping | Create LabelMapRecord and exclusions/proxy-intent limits; validate complete included-label coverage. |
| 10 | Preprocessing compilation | Compile source-native/derived pipeline; record exact operations, units, channel policy and fit scope. |
| 11 | Split construction | Construct group-safe roles before window generation; reconcile membership/attrition. |
| 12 | Low-calibration budgets | Allocate deterministic class-aware calibration subsets with seed and no held-out contamination. |
| 13 | Preprocessing fit/transform | Fit only on legal populations; transform; emit PreprocessingRecord and derived pointers. |
| 14 | Quality annotation | Create source-supported ArtifactFlagRecord or explicit unavailable status; no silent repair. |
| 15 | Window generation | Create lineage-preserving WindowRecord with bounds, parent event, overlap and inherited identities. |
| 16 | Schema/lifecycle/lineage validation | Validate every canonical record, stable ID, hash, lifecycle and foreign key. |
| 17 | Leakage/contamination audit | Run subject/session/run/event/window/duplicate/fit/budget leakage checks and chronology/purge checks. |
| 18 | A0-A13 readiness | Generate 14 separately traceable rows; required keys or NOT_READY reason; prove A14 absent. |
| 19 | Cards | Generate DatasetCard/ProtocolCard from saved sources; preserve limitations and prohibited claims. |
| 20 | Manifests | Generate Layer1Manifest, input/output/test/gate manifests and complete checksums. |
| 21 | Negative/failure register | Preserve all failed, excluded, missing, blocked, invalid and diagnostic-only outcomes. |
| 22 | P02/later compatibility | Run P02 consumer validator and produce exact phase handoff plus later-consumer map. |
| 23 | Evidence sufficiency | Evaluate P01-G01..G16 deterministically and emit terminal gate decision. |
| 24 | Repair re-entry metadata | If insufficient, identify owner and affected scope; never hide failure; define rerun identity. |
| 25 | Bundle export | Write complete phase bundle, ZIP it, hash it, list external oversized pointers if any. |
| 26 | Final summary | Print IDs, counts, gates, limitations, bundle paths/hashes and exact next step. |

The notebook and bundle contract is fully machine-readable in `p01_l1_kaggle_notebook_specification_R2.yaml`. No smoke, fast, reduced, fixture-only or alternative execution mode exists.

# 13. A0-A13 Readiness and A14 Rejection

R2 requires fourteen separately traceable A0-A13 readiness rows, each with official role, owner, activation phase, required Layer 1 keys/records, missing-key behavior, diagnostic-only behavior, invalidation trigger, and readiness output path. `activated_in_p01` and `executed_in_p01` are false. A14 is rejected and must not appear in an active config, readiness row, run, result, claim or card.

# 14. Deterministic Gates

| Gate | Name | Procedure | Stable failure codes | Repair owner | Output |
|---|---|---|---|---|---|
| `P01-G01` | Authority and Phase 0 intake | verify hashes, safe paths, current IDs and contract resolution | `AUTHORITY_MISSING|HASH_MISMATCH|CONTRACT_UNRESOLVED` | Build Book/intake | `reports/phase_01/gates/P01-G01.json` |
| `P01-G02` | Source/provenance/license | resolve exact revision, citation, access, license, checksum and source byte identity | `SOURCE_UNRESOLVED|LICENSE_UNRESOLVED|CHECKSUM_MISMATCH|ACCESS_BLOCKED` | Dataset registry/owner | `reports/phase_01/gates/P01-G02.json` |
| `P01-G03` | Schema and canonical object | JSON Schema validation plus ID/lifecycle/lineage/hash checks | `SCHEMA_INVALID|ID_INVALID|LINEAGE_MISSING|LIFECYCLE_INVALID` | Registry/implementation | `reports/phase_01/gates/P01-G03.json` |
| `P01-G04` | Metadata completeness | reconcile subject/session/run/event/channel/rate fields and explicit missingness | `METADATA_REQUIRED_MISSING|HIERARCHY_INVALID|COUNT_DRIFT` | Metadata/source | `reports/phase_01/gates/P01-G04.json` |
| `P01-G05` | Label mapping | prove contextual coverage, exclusions, rest/no-action and proxy limits | `LABEL_UNKNOWN|LABEL_AMBIGUOUS|PROXY_LIMITATION_MISSING` | Labels/Method Selection | `reports/phase_01/gates/P01-G05.json` |
| `P01-G06` | Preprocessing fit scope | prove fitted state uses permitted training/calibration populations only | `FIT_SCOPE_LEAKAGE|TRANSFORM_ID_DRIFT|SOURCE_PROVENANCE_LOST` | Preprocessing/Protocol | `reports/phase_01/gates/P01-G06.json` |
| `P01-G07` | Split disjointness | set-intersection tests across declared group keys and count reconciliation | `SUBJECT_OVERLAP|SESSION_OVERLAP|EVENT_OVERLAP|ATTRITION_MISMATCH` | Splits | `reports/phase_01/gates/P01-G07.json` |
| `P01-G08` | Leakage and chronology | audit subject/session/run/source-event/window/duplicate/fit leakage and purge/embargo | `LEAKAGE_DETECTED|CHRONOLOGY_INVALID|PURGE_FAILURE` | Validation/splits/windows | `reports/phase_01/gates/P01-G08.json` |
| `P01-G09` | Low-calibration budgets | verify class-aware deterministic allocation, seed and no test contamination | `BUDGET_INVALID|BUDGET_CONTAMINATION|SEED_MISSING` | Splits/Protocol | `reports/phase_01/gates/P01-G09.json` |
| `P01-G10` | Window identity | verify bounds, parent lineage, overlap groups and inherited split/label/preprocessing | `WINDOW_INVALID|PARENT_MISSING|OVERLAP_COLLISION|INHERITANCE_MISMATCH` | Windows | `reports/phase_01/gates/P01-G10.json` |
| `P01-G11` | Quality coverage | verify source-supported annotations or explicit unavailable status; prohibit silent repair | `QUALITY_COVERAGE_INCOMPLETE|UNSUPPORTED_FLAG|SILENT_REPAIR` | Quality | `reports/phase_01/gates/P01-G11.json` |
| `P01-G12` | Matched keys/A0-A13 readiness | verify 14 rows, required keys or diagnostic-only reason, and no A14 | `READINESS_ROW_MISSING|MATCH_KEY_MISSING|A14_PRESENT` | Validation/Protocol | `reports/phase_01/gates/P01-G12.json` |
| `P01-G13` | Cards and limitations | source-parity, limitation-preservation and forbidden-claim scan | `CARD_SOURCE_DRIFT|LIMITATION_MISSING|FORBIDDEN_CLAIM` | Cards/Layer0 | `reports/phase_01/gates/P01-G13.json` |
| `P01-G14` | Manifest/path/hash closure | verify every required output path, bytes, hash, lifecycle and manifest foreign key | `MANIFEST_INCOMPLETE|PATH_UNRESOLVED|HASH_MISMATCH|FOREIGN_KEY_BROKEN` | Manifests | `reports/phase_01/gates/P01-G14.json` |
| `P01-G15` | Phase 2 compatibility | validate exact record profiles, terminal status, limitations and invalidation contract | `P02_CONTRACT_INVALID|REQUIRED_INPUT_MISSING|DIAGNOSTIC_BRANCH_PROMOTED` | Integration/L2 | `reports/phase_01/gates/P01-G15.json` |
| `P01-G16` | Complete artifact closure | close expected-output matrix with lawful terminal state and evidence link for every row | `ARTIFACT_MISSING|TEST_MISSING|GATE_UNRESOLVED|UNLAWFUL_TERMINAL_STATE` | Phase owner | `reports/phase_01/gates/P01-G16.json` |

# 15. Evidence-Insufficiency Loopback

```text
insufficient, invalid, incomplete, or unusable P01 evidence
→ preserve failed bundle and exact gate decision
→ identify exact defect and lawful owner
→ repair only the minimum implementation/config/input/notebook scope
→ issue new code/config/run identity
→ invalidate only affected descendants
→ rerun the affected branch, or the full branch when source/split/preprocess/label/window identity changed
→ regenerate the complete bundle
→ reevaluate P01-G01 through P01-G16
```

No narrative override may convert a deterministic failure into a pass.

# 16. Downstream and Closure Handoffs

- P02 handoff is specified in `p01_l1_phase2_handoff_contract_R2.yaml`, including exact profiles, paths, validation, terminal states, consumer invariants and invalidation triggers.
- Protocol v1 handoff receives exact run/config/source/record/gate identities and all deviations.
- Phase Analysis receives accepted and failed outputs, denominators, exclusions, limitations and A0-A13 readiness.
- Layer 0 receives candidate-claim source fields and limitations only.
- Evidence Map receives exact evidence IDs only after Layer 0.
- Layer 10 receives a saved read-only source bundle only after mapping authorization.

# 17. Open Decisions and Execution Boundary

R2 is ready to authorize creation of the one full notebook. Official Kaggle execution remains blocked until exact source profiles, access, tested environment, numerical config and Phase 1 entry acknowledgment are resolved. These are recorded in `p01_l1_open_decision_register_R2.yaml`; none is silently invented.

# 18. R2 Definition of Done

R2 is complete because the predecessor and P00 provenance are preserved; exact source use is traceable; all 11 responsibilities have detailed physical dossiers; every expected artifact has exact path/validator/test/gate/manifest/consumer/failure fields; the 27-section notebook and complete bundle are specified; all 16 gates are deterministic; A0-A13/A14 are explicit; the P02/later handoff is exact; machine companions parse and agree; the full Word and Markdown successors are generated; and local regression/adversarial/package/rendering checks pass.

It remains **not** proof of P01 implementation or execution.

# Preserved R1 Annex for Provenance

<!-- BEGIN EXACT R1 ANNEX; SHA-256 b458f18b477b983cbe448f0fa35a70f003fcb9e158865ac4a1968b37f954a48c -->

---
title: "IHARQ BenchGuard Stretch C - Phase 1 / Layer 1 Integrated Implementation and Execution Annex"
document_id: "IHARQ-IBB-P01-L1-ANNEX-R1"
revision: "R1"
date: "2026-08-04"
status: "IMPLEMENTATION-AUTHORITY-COMPLETE; KAGGLE-NOTEBOOK-NOT-YET-CREATED; P01-NOT-EXECUTED"
parent_build_book: "IHARQ-IBB-R7-P01-L1-CONTINUATION"
governing_workflow: "Governance V6.1"
---

# IHARQ Phase 1 / Layer 1 Integrated Implementation and Execution Annex R1

> **Controlling boundary.** This annex is the current implementation authority for P01/L1 and a governed continuation of the Master Implementation Build Book. It specifies physical implementation and Kaggle readiness. It does not report a Phase 1 run, complete Protocol v1.0, approve claims, update the Evidence Map, create the final Layer 10 package, close Phase 1, or authorize Phase 2.

> **Single-track rule.** The intended sequence is implementation document -> one full Kaggle notebook -> evidence-sufficiency check -> minimum repair/rerun only if necessary -> P01 Protocol v1.0 annex -> Phase Analysis -> Layer 0 -> Evidence Map -> Layer 10 -> cumulative ZIP successor.


# Document Navigation

1. Document control and parent relationship
2. Authority manifest and source utilization
3. Phase 0 intake/reuse/invalidation
4. P01 identity, scope and layer participation
5. Layer 1 responsibility and module crosswalk
6. Selected dataset and method strategy
7. Input and output contracts
8. Physical package and API architecture
9. Module implementation dossiers
10. Configuration and environment
11. Source access/licensing
12. Preprocessing/splits/budgets/windows
13. Validation/leakage/cards/manifests
14. A0-A13 readiness and A14 rejection
15. Kaggle notebook and bundle
16. Tests, gates and evidence loopback
17. Work packages and roadmap
18. Layer 0/Evidence Map/Layer 10 handoffs
19. Phase 2/later handoff
20. Risks/open decisions
21. Definition of done and machine handoff
22. Final self-audit

# 1. Document Control and Parent Build Book Relationship

| Field | Value |
|---|---|
| Annex ID | `IHARQ-IBB-P01-L1-ANNEX-R1` |
| Parent successor | `IHARQ-IBB-R7-P01-L1-CONTINUATION` |
| Predecessor Build Book | `IHARQ-IBB-R6-P00-NO-EXTERNAL-CI-GATE` distribution snapshot SHA-256 `39ac0a940c5fbf24ebd7e655d368089ff1ec54d69b94ba05408d3d4d921fda84` |
| Phase | `P01 - Public Data and Split Protocol` |
| Primary layer | `L1 - Public-Data and Protocol Anchor` |
| Supporting boundaries | `L0` claim/scope governance; `L10` read-only downstream consumer |
| Workflow | V6.1 single-track, ZIP-first, one full notebook, no smoke track |
| Maturity | `IMPLEMENTATION-AUTHORITY-COMPLETE` |
| Kaggle | Notebook specification complete; notebook not created or executed |
| Empirical evidence | None claimed |

The annex supersedes the predecessor's **current** P01/L1 planning statements, smoke-path requirement, Protocol timing-mode instructions and routine GitHub publication assumptions. Those older statements remain historical provenance only. Unrelated layers and phases remain preserved and are not rewritten.


# 2. Authority Manifest

| ID | Authority/asset | Revision | File | SHA-256 | Use | Status |
| --- | --- | --- | --- | --- | --- | --- |
| GOV-V6.1 | Document Stack Governance and Creation Guide V6.1 | V6.1 | 00_IHARQ_Document_Stack_Governance_and_Creation_Guide_V6_1_Single_Track_Full_Depth_Consolidated_Notebook(1).md | c811373c19a7c2c3f6d72cf2aed984e02ffcb07bb448cfc3bdbdf26a35a4f1d9 | Workflow, ZIP-first state, one-notebook full-depth rule, sole evidence-insufficiency loopback | INSPECTED |
| ARCH | Master Architecture Specification | T29 Layout-Corrected R1 | 01_Master_Architecture_Specification_FINAL_T29_LAYOUT_CORRECTED_R1.pdf | ae374c9de061bc5179c9223e7d646c70cf0d98c414007ab6baf95cd68c814f9b | P01/L1 identity, 11 responsibilities, boundaries, records, consumers, readiness | INSPECTED |
| REG | Canonical Artifact, Record, and Interface Registry | R44 | 02_Canonical_Artifact_Record_and_Interface_Registry_FINAL_R44.md | bdb309f76b9b525ea89cfa56c79a9b7989348e3509febac9ae9fffe7858d1f87 | Canonical L1 records, vocabularies, lifecycle, interfaces, readiness artifact | INSPECTED |
| PLAN | Execution and Evidence Plan | R41 | 03_Execution_and_Evidence_Plan_FINAL_R41.md | f31de3453b331d909a8cccbf951a2df61ef7ca38b71df4bde8be95040095da82 | P01 inputs, outputs, gates, exit, handoff, ablation readiness | INSPECTED |
| PROT | Experiment, Ablation, and Evaluation Protocol v0.1 | R42 | 04_Experiment_Ablation_and_Evaluation_Protocol_FINAL_R42.md | 8b7a393b860bd49a34a794db5c2b80af7f127bc318a112bc7ed3c375ce704813 | A0-A13, matched keys, leakage, low-calibration, negative results | INSPECTED |
| PLAY | Complete Phase Execution Playbook | R41 | 05_Complete_Phase_Execution_Playbook_FINAL_R41.md | 176f46950b86db8cd5c23789893955336c818a6fcd10ed36d6c66e096faccc87 | P01 procedural order, failure handling, handoff and closure | INSPECTED |
| METHOD | Integrated Layers 0-10 Method Selection and Design Rationale Register | R2 | 06_Integrated_Layers0_to_10_Method_Selection_and_Design_Rationale_Register_FINAL_R2.md | b036b02ac65b3bc2595513f4ca8a8137a6273f914e46e1cf6180515e57726749 | Dataset portfolio/status, selected preprocessing/split/window/quality/card strategy | INSPECTED |
| NB | Integrated Layers 0-10 Detailed Design and Nuts-and-Bolts Specification | R2 | 07_Integrated_Layers0_to_10_Detailed_Design_and_Nuts_and_Bolts_Specification_FINAL_R2.md | 4f47c6f511e646b2127cc79f14a5f632b00f5112582a049b46c735e78ded638c | Algorithms, validators, invariants, failure behavior, technical profiles | INSPECTED |
| P00-ZIP | Finalized Phase 0 cumulative package | Scholarship Ready R2 | IHARQ_Phase_0_GitHub_Scholarship_Ready_R2(2).zip | 3dcbe3e82ec7254ce1bd40568b36409d56050538e69a7264f8f1e431be019ef0 | Physical foundation, schemas/configs/contracts/tests, current Build Book and P01 contract substrate | INSPECTED |
| IBB-PRE | Current Master Implementation Build Book | R6 P00 no-external-CI-gate | 01_IHARQ_Master_Implementation_Build_Book_Current.md | 39ac0a940c5fbf24ebd7e655d368089ff1ec54d69b94ba05408d3d4d921fda84 | Predecessor implementation authority and L1 dossier/work packages | INSPECTED |
| P00-ANN | Current Phase 0 implementation/finalization annex | R4 | 02_IHARQ_Phase_0_Implementation_and_Finalization_Annex_Current.md | 5cb7d898e4f70523458f6d69acfa940a8f2011390667bd9dec16d3d7e52626bc | P00 provenance and status | INSPECTED |
| P00-P01-HANDOFF | Phase 0 to Phase 1 handoff | R5 | 17_IHARQ_Phase_0_to_Phase_1_Authorization_and_Handoff.md | 2bb0311f0f6bb3731366152106ef77a3daefd0db4e1c64f7674afd7de84310e6 | Entry conditions and historical publication status | INSPECTED |
| PROMPT | P01/L1 implementation continuation master prompt | R1 | IHARQ_Phase_1_Layer_1_Implementation_Build_Book_Continuation_and_Kaggle_Readiness_Master_Prompt_R1(1).md | 5e51429d773c46c860b97d492c1000215f43c331a9081988b5876ee821b4aab9 | Exact task contract and deliverables | INSPECTED |


## 2.1 Authority conflict routing

Conflicts are routed by ownership: Architecture for layer/phase identity; Registry for canonical names/fields/lifecycle; Execution Plan for P01 required outputs/gates; Protocol for matching/leakage/ablation fairness; Playbook for order/repair/handoff; Method Selection for dataset/method status; Nuts-and-Bolts for algorithms/validators; Build Book for paths/APIs/configs/tests; Layer 0 for claim wording; Evidence Map for claim-evidence placement; Layer 10 for read-only rendering. No conflict is silently reconciled.

## 2.2 Source utilization audit

| Source | Sections/surfaces used | Implementation consequence | Disposition |
| --- | --- | --- | --- |
| GOV-V6.1 | Governing principle; Parts II-VI, XIII-XVI | ZIP-first single track, one-notebook consolidation without scope reduction, no smoke track, sole evidence loopback, post-run Protocol/Analysis/L0/Map/L10 sequence | APPLIED |
| ARCH | Layer 1 Chapter 7; Phase 1 roadmap 23.7.2; L1 synchronization addenda | L1 mission/boundary, 11 responsibilities, records, phase identity, downstream consumers and claim ceiling | APPLIED |
| REG | Layer 1 modules/inputs/outputs; canonical record entries 8.1-8.9; vocabularies; evaluation linkage; failure registry | Canonical names, fields/profiles, lifecycle, status/missingness, readiness artifact and no TrialRecord invention | APPLIED |
| PLAN | Phase 1 / Layer 1 evidence obligations and synchronized Layer 1 products | Required inputs/outputs/gates/exit/handoffs and A0-A13 readiness | APPLIED |
| PROT | Layer 1 readiness and A0-A13 matched-comparison controls | Split/leakage/budget/matching/negative-result obligations; A14 prohibited | APPLIED |
| PLAY | Phase 1 procedure, failure/downgrade, handoff and closure | Ordered execution and repair routing | APPLIED |
| METHOD | Layer 1 selected portfolio and three-part strategy | Dataset statuses and accepted protocol/governance methods preserved exactly | APPLIED |
| NB | Layer 1 Category 1-3; split/preprocessing/window/validation/card modules | Technical algorithms, validators, invariants, source conflict handling and implementation handoff | APPLIED |
| P00-ZIP | Current Build Book, P00 annex, P01 config/contracts, schemas, package/tests | Physical reuse substrate and current historical status | APPLIED |

# 3. Phase 0 Intake, Reuse and Invalidation Audit

The Phase 0 package is treated as the supplied cumulative project state. Its valid foundations are reused by identity. Its historical publication-dependent Phase 1 authorization wording is preserved but does not prevent documentary P01/L1 planning under Governance V6.1. Real-data execution remains blocked until the non-publication P01 entry gates and owner decisions below are resolved.

| Foundation | Disposition | Evidence | P01 action |
| --- | --- | --- | --- |
| Authority/config identity core | REUSE_AS_IS | Existing authority/config manifests and semantic identity infrastructure | No P01 change |
| Stable IDs, serialization and hashing | REUSE_AS_IS | Phase 0 implemented foundation | Use for all L1 record/artifact identities |
| Lifecycle, lineage and supersession | REUSE_AS_IS | Phase 0 schemas/profiles | Extend with P01 record instances only |
| JSON Schema validation framework | REUSE_AS_IS | Eight L1 schemas already present | Add DatasetCard/ProtocolCard profiles as governed artifacts, not canonical records |
| P01 phase config and input/output contracts | REUSE_WITH_P01_PROFILE | TEMPLATE_READY/CONTRACT_READY | Resolve expected artifacts, environment, configs and gates in annex/notebook |
| Layer1 package boundary | EXTEND_LAWFULLY | src/iharq/layer1_data_protocol exists as Phase 0 stub | Implement 11 responsibilities under 10-capability grouping |
| Fixture/negative-test infrastructure | REUSE_WITH_P01_PROFILE | P00 valid/malformed framework | Add L1 factual, leakage, split and readiness fixtures |
| CLI/orchestration | REUSE_WITH_P01_PROFILE | P00 local CLI exists | Add P01 validation/bundle commands; Kaggle notebook may call importable APIs |
| Layer 0 vocabularies and boundary | REUSE_AS_IS | Current P00 claim-safety infrastructure | Only limitation/handoff readiness in this task |
| Layer 10 read-only boundary | REUSE_AS_IS | Current P00 package/validators | Define source bundle only; no rendering/recomputation now |
| Environment profile | REPAIR_BEFORE_P01_EXECUTION | P01 points to Python 3.12 template while only P00 3.13.5 was locally verified | Pin after compatibility tests; documentary design remains nonblocking |
| GitHub publication gate | SUPERSEDED | Historical P00 V4 status | Governance V6.1 cumulative ZIP controls; no GitHub gate for P01 Build Book |


## 3.1 Invalidation policy

A change to dataset revision, source bytes, label map, preprocessing identity, split membership, low-calibration budget, window identity, quality policy or validation decision invalidates every descendant that consumes the changed object. Invalidation is topological and append-only: old artifacts remain preserved as `SUPERSEDED` or `INVALIDATED`; new IDs/hashes are issued; unaffected datasets/cells are not rerun.


# 4. Phase 1 Identity, Scope and Layer Participation

**P01 purpose:** establish the public-data, metadata, label, preprocessing, split, low-calibration, window, quality, validation, card, manifest and downstream-readiness foundation on which P02-P15 depend.

**In scope:** acquisition of exact admitted public EEG source revisions; source truth and license evidence; normalized metadata and labels; lawful preprocessing; quality annotation; leakage-safe splits and low-calibration memberships; event-aligned windows; validation; A0-A13 readiness; cards/manifests; full Kaggle execution design and bundle handoff.

**Out of scope:** decoder training/performance, calibration effectiveness, selective prediction, IHARQ outcomes, policy performance, stress robustness, embodiment validity, clinical efficacy/safety, real-device control and final thesis claims.

| Layer | P01 role | Implementation ownership | Boundary |
| --- | --- | --- | --- |
| L1 | Primary producer | All modules, records, reports, cards, manifests, tests and P02 handoff in this annex | Does not own decoder/scientific result or claim approval |
| L0 | Supporting governance | Consumes candidate limitations/claim-safety tags after analysis | Cannot change measurements or source records |
| L10 | Read-only downstream | Consumes cards/manifests/validation/readiness after Evidence Map | Cannot recompute, repair or strengthen evidence |

# 5. Layer 1 Responsibility Matrix

| ID | Official responsibility | Build Book capability | Physical module | Purpose | Primary outputs | Consumers | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| L1-MOD-01 | Dataset registry manager | L1-01 | dataset_registry.py | Resolve accepted dataset aliases, source identities, revisions, licenses, citations, checksums, access methods and eligibility; never infer source truth from a wrapper. | DatasetRecord, source/provenance/license report | P01 primary; P02-P15 downstream | READY_FOR_IMPLEMENTATION_DESIGN |
| L1-MOD-02 | Dataset loader | L1-02 | adapters/base.py and adapters/<dataset>.py | Load exact admitted source revision into a source-faithful intermediate representation; preserve source file/event identifiers and loader provenance. | DatasetRecord, raw source inventory | P01 primary; P02-P15 downstream | READY_FOR_IMPLEMENTATION_DESIGN |
| L1-MOD-03 | Metadata normalizer | L1-03 | metadata.py | Normalize subject/session/run/source-event/channel/sampling metadata while preserving source values, missingness, conflicts and derivation lineage. | DatasetRecord, metadata completeness report | P01 primary; P02-P15 downstream | READY_FOR_IMPLEMENTATION_DESIGN |
| L1-MOD-04 | Task and label ontology mapper | L1-04 | labels.py | Map original dataset labels to governed normalized intent/task labels contextually; preserve original labels, exclusions, rest/no-action and proxy-intent limits. | LabelMapRecord, label-map validation report | P01 primary; P02-P15 downstream | READY_FOR_IMPLEMENTATION_DESIGN |
| L1-MOD-05 | Preprocessing registry and lawful executor | L1-05 | preprocessing.py | Register source-native and derived preprocessing; enforce split-aware fit scope, deterministic transforms, no held-out fitting, and stable preprocessing identity. | PreprocessingRecord, preprocessing fit-scope report | P01 primary; P02-P15 downstream | READY_FOR_IMPLEMENTATION_DESIGN |
| L1-MOD-06 | Artifact and channel-quality annotator | L1-06 | quality.py | Annotate missing/bad channels, short trials, rate mismatches and source-supported artifact evidence; do not silently repair confirmatory source evidence. | ArtifactFlagRecord, quality coverage report | P01 primary; P02-P15 downstream | READY_FOR_IMPLEMENTATION_DESIGN |
| L1-MOD-07 | Split and protocol manager | L1-07 | splits.py | Generate immutable hierarchical subject/session/run/source-event-safe splits, explicit role separation and attrition accounting. | SplitRecord, split-disjointness report | P01 primary; P02-P15 downstream | READY_FOR_IMPLEMENTATION_DESIGN |
| L1-MOD-08 | Trial/window generator | L1-08 | windows.py | Create event-aligned lineage-preserving windows with immutable identity, parent source-event/trial links, timing, stride and overlap-group metadata. | WindowRecord, window timing/overlap report | P01 primary; P02-P15 downstream | READY_FOR_IMPLEMENTATION_DESIGN |
| L1-MOD-09 | Data validation and leakage auditor | L1-09 | validation.py and leakage.py | Validate schemas, metadata, labels, fit scope, split disjointness, temporal/source-event overlap, duplicate lineage, matched keys and downstream compatibility. | ValidationReport, leakage report, matched-key completeness report | P01 primary; P02-P15 downstream | READY_FOR_IMPLEMENTATION_DESIGN |
| L1-MOD-10 | Dataset-card and protocol-card generator | L1-10A | cards.py | Generate source-grounded DatasetCard and ProtocolCard from accepted records/manifests with limitations, exclusions and permitted-use boundaries. | DatasetCard, ProtocolCard | P01 primary; P02-P15 downstream | READY_FOR_IMPLEMENTATION_DESIGN |
| L1-MOD-11 | Provenance and manifest builder | L1-10B | manifests.py and bundle.py | Create Layer1Manifest, readiness artifact, output/test/gate manifests, hashes, failure register and phase handoff. | Layer1Manifest, layer1_ablation_readiness_l1_v1.json, P01 output manifest | P01 primary; P02-P15 downstream | READY_FOR_IMPLEMENTATION_DESIGN |


## 5.1 Ten-capability / eleven-responsibility lossless crosswalk

The predecessor groups the card generator and provenance/manifest builder under capability `L1-10`. They remain two official responsibilities with separate modules, outputs and tests.

| Official ID | Official responsibility | Capability | Proposed path | Mapping | Outputs |
| --- | --- | --- | --- | --- | --- |
| L1-MOD-01 | Dataset registry manager | L1-01 | dataset_registry.py | ONE_TO_ONE | DatasetRecord, source/provenance/license report |
| L1-MOD-02 | Dataset loader | L1-02 | adapters/base.py and adapters/<dataset>.py | ONE_TO_ONE | DatasetRecord, raw source inventory |
| L1-MOD-03 | Metadata normalizer | L1-03 | metadata.py | ONE_TO_ONE | DatasetRecord, metadata completeness report |
| L1-MOD-04 | Task and label ontology mapper | L1-04 | labels.py | ONE_TO_ONE | LabelMapRecord, label-map validation report |
| L1-MOD-05 | Preprocessing registry and lawful executor | L1-05 | preprocessing.py | ONE_TO_ONE | PreprocessingRecord, preprocessing fit-scope report |
| L1-MOD-06 | Artifact and channel-quality annotator | L1-06 | quality.py | ONE_TO_ONE | ArtifactFlagRecord, quality coverage report |
| L1-MOD-07 | Split and protocol manager | L1-07 | splits.py | ONE_TO_ONE | SplitRecord, split-disjointness report |
| L1-MOD-08 | Trial/window generator | L1-08 | windows.py | ONE_TO_ONE | WindowRecord, window timing/overlap report |
| L1-MOD-09 | Data validation and leakage auditor | L1-09 | validation.py and leakage.py | ONE_TO_ONE | ValidationReport, leakage report, matched-key completeness report |
| L1-MOD-10 | Dataset-card and protocol-card generator | L1-10A | cards.py | GROUPED_WITH_L1-10; DISTINCT_CARD RESPONSIBILITY | DatasetCard, ProtocolCard |
| L1-MOD-11 | Provenance and manifest builder | L1-10B | manifests.py and bundle.py | GROUPED_WITH_L1-10; DISTINCT_MANIFEST RESPONSIBILITY | Layer1Manifest, layer1_ablation_readiness_l1_v1.json, P01 output manifest |

# 6. Selected Dataset and Method Strategy

The annex implements, but does not reselect, the accepted three-part strategy:

- **Part A:** MI-first public EEG source, metadata and contextual label foundation.
- **Part B:** split-aware minimal preprocessing; hierarchical group/source-event-safe splits; class-aware low-calibration budgets; event-lineage-preserving windows; annotate-not-repair quality; hard leakage/validation gates.
- **Part C:** DatasetCard, ProtocolCard, Layer1Manifest, `layer1_ablation_readiness_l1_v1.json`, negative-result/downgrade governance and downstream handoffs.

## 6.1 Dataset portfolio and implementation disposition

| Dataset/source | Status | Role | Implementation disposition |
| --- | --- | --- | --- |
| PhysioNetMI / EEG Motor Movement/Imagery Dataset | PRIMARY_SELECTED | Source/rest/provenance anchor | Implement adapter after exact source revision, subject-88 mixed-rate handling, license/access/citation/checksum verification. |
| BNCI2014_001 / BCI Competition IV-2a | PRIMARY_SELECTED | Standard four-class MI benchmark companion | Implement adapter with inherited source preprocessing/artifact provenance and session-aware protocol. |
| Lee2019_MI / OpenBMI | PRIMARY_SELECTED_WITH_SOURCE_QUALIFICATIONS | Maximum-scope two-session left/right MI target companion | Implement adapter only after source-phase/wrapper representation and label/channel facts are verified. |
| Cho2017 | SCREENED_FALLBACK | Best subject-diverse left/right MI fallback if Lee2019_MI is unavailable | Prepare adapter interface/profile; activate only by explicit owner decision and source/license verification. |
| GuttmannFlury2025_MI | SCREENED_CURRENT_DELTA_CANDIDATE | Highest-priority current-delta candidate | Do not promote until source-card, channel-count, session/repeated-recording and protocol facts are confirmed. |
| Schirrmeister2017; Zhou2016 | SECONDARY_DIAGNOSTIC_FALLBACK | Secondary or diagnostic fallback | No default Phase 1 activation. |
| BNCI2025_001; BNCI2025_002; Liu2025; P300/ERP/SSVEP families | DIAGNOSTIC_OR_FUTURE_WORK | Future expansion only | Require later label-policy and Layer 0 scope expansion. |
| MOABB; MNE; EEGDash; OpenNeuro; NEMAR | SUPPORTING_INFRASTRUCTURE_NOT_DATASET_SELECTION | Discovery, loading, metadata or benchmark infrastructure | May support access/loadability but cannot define source revision/license truth. |

## 6.2 No-promotion rule

A screened or diagnostic candidate cannot become active because an adapter is easy to implement. Activation requires exact source evidence, license/access acceptance, owner approval and the applicable P01 configuration. Infrastructure libraries may load a dataset but cannot replace source/version/license truth.


# 7. Canonical Input Contract

Every input carries identity, version, hash, producer, validity, lifecycle, lineage, license/access, limitations, consumer and failure behavior.

## 7.1 Phase 0 foundation inputs

- authority, project-state, environment and config manifests;
- P01 input/output contracts;
- schema and record-family catalogs;
- IDs, canonical serialization and semantic hashing;
- lifecycle/lineage/supersession profiles;
- limitation/status/reason vocabularies;
- validators and malformed-fixture infrastructure;
- ArtifactPointerRecord support;
- P01 phase configuration.

## 7.2 Public-data inputs

Exact source revision/identity, checksum, license, citation, access route, raw EEG/source files, source metadata, subject/session/run/source-event hierarchy, channels/rates, source labels/tasks and source-supported quality evidence. No fabricated field is permitted; missingness is explicit.

## 7.3 Configuration families

`dataset_inclusion`, `source_access`, `label_map`, `preprocessing`, `quality`, `split_protocol`, `low_calibration`, `window`, `validation`, `cards`, `manifests`, `kaggle_resources`, `outputs`, `claim_safety` and `external_artifacts`. Numerical values are typed unresolved fields until owner/notebook execution configuration resolves them; the Build Book does not invent Protocol constants.


# 8. Canonical and Governed Output Contract

| Output | Canonicality | Producer | Schema/profile/path | Required meaning | Current status | Consumers |
| --- | --- | --- | --- | --- | --- | --- |
| DatasetRecord | CANONICAL | dataset_registry/metadata | schemas/records/DatasetRecord.schema.json | One immutable record per admitted dataset/source revision and normalized source unit. | SCHEMA_PRESENT_IMPLEMENTATION_PENDING | P02-P15 / L0 / L10 as specified |
| WindowRecord | CANONICAL | windows | schemas/records/WindowRecord.schema.json | One immutable window identity preserving dataset/subject/session/run/source-event/trial lineage. | SCHEMA_PRESENT_IMPLEMENTATION_PENDING | P02-P15 / L0 / L10 as specified |
| SplitRecord | CANONICAL | splits | schemas/records/SplitRecord.schema.json | One immutable split/protocol membership record with group keys, roles, budgets and lineage. | SCHEMA_PRESENT_IMPLEMENTATION_PENDING | P02-P15 / L0 / L10 as specified |
| PreprocessingRecord | CANONICAL | preprocessing | schemas/records/PreprocessingRecord.schema.json | One immutable effective preprocessing identity and fit-scope record. | SCHEMA_PRESENT_IMPLEMENTATION_PENDING | P02-P15 / L0 / L10 as specified |
| LabelMapRecord | CANONICAL | labels | schemas/records/LabelMapRecord.schema.json | Contextual original-to-normalized label map with inclusion/exclusion and limitations. | SCHEMA_PRESENT_IMPLEMENTATION_PENDING | P02-P15 / L0 / L10 as specified |
| ArtifactFlagRecord | CANONICAL_WHERE_SUPPORTED | quality | schemas/records/ArtifactFlagRecord.schema.json | Append-only source/derived quality annotations; absence is represented, not fabricated. | SCHEMA_PRESENT_IMPLEMENTATION_PENDING | P02-P15 / L0 / L10 as specified |
| ValidationReport | CANONICAL | validation | schemas/records/ValidationReport.schema.json | Gate-by-gate validation outcomes, failures, downgrade status and evidence links. | SCHEMA_PRESENT_IMPLEMENTATION_PENDING | P02-P15 / L0 / L10 as specified |
| DatasetCard | GOVERNED_ARTIFACT | cards | docs/cards/datasets/<dataset_id>.md | Reviewer-facing source, task, structure, access, limitation and allowed-use summary. | PROFILE_TO_BE_REALIZED | P02-P15 / L0 / L10 as specified |
| ProtocolCard | GOVERNED_ARTIFACT | cards | docs/cards/protocols/<protocol_id>.md | Split, budget, preprocessing, window, leakage, consumer and limitation summary. | PROFILE_TO_BE_REALIZED | P02-P15 / L0 / L10 as specified |
| Layer1Manifest | CANONICAL/GOVERNED_MANIFEST | manifests | schemas/records/Layer1Manifest.schema.json | Master index of records, configs, hashes, validation, limitations and readiness. | SCHEMA_PRESENT_IMPLEMENTATION_PENDING | P02-P15 / L0 / L10 as specified |
| layer1_ablation_readiness_l1_v1.json | GOVERNED_READINESS_ARTIFACT | validation/manifests | manifests/layer1_ablation_readiness_l1_v1.json | A0-A13 matched-key/source-readiness evidence only; no ablation result. | PROFILE_TO_BE_REALIZED | P02-P15 / L0 / L10 as specified |
| dataset inclusion/exclusion report | SUPPORTING_GOVERNED_OUTPUT | corresponding module | reports/phase_01/... | Required supporting evidence and handoff product | DESIGN_SPECIFIED | Protocol/Analysis/downstream |
| source/provenance/license report | SUPPORTING_GOVERNED_OUTPUT | corresponding module | reports/phase_01/... | Required supporting evidence and handoff product | DESIGN_SPECIFIED | Protocol/Analysis/downstream |
| metadata-completeness report | SUPPORTING_GOVERNED_OUTPUT | corresponding module | reports/phase_01/... | Required supporting evidence and handoff product | DESIGN_SPECIFIED | Protocol/Analysis/downstream |
| label-map validation report | SUPPORTING_GOVERNED_OUTPUT | corresponding module | reports/phase_01/... | Required supporting evidence and handoff product | DESIGN_SPECIFIED | Protocol/Analysis/downstream |
| preprocessing fit-scope report | SUPPORTING_GOVERNED_OUTPUT | corresponding module | reports/phase_01/... | Required supporting evidence and handoff product | DESIGN_SPECIFIED | Protocol/Analysis/downstream |
| split-disjointness report | SUPPORTING_GOVERNED_OUTPUT | corresponding module | reports/phase_01/... | Required supporting evidence and handoff product | DESIGN_SPECIFIED | Protocol/Analysis/downstream |
| subject/session/run/source-event leakage report | SUPPORTING_GOVERNED_OUTPUT | corresponding module | reports/phase_01/... | Required supporting evidence and handoff product | DESIGN_SPECIFIED | Protocol/Analysis/downstream |
| low-calibration budget table | SUPPORTING_GOVERNED_OUTPUT | corresponding module | reports/phase_01/... | Required supporting evidence and handoff product | DESIGN_SPECIFIED | Protocol/Analysis/downstream |
| window timing/overlap/source-event report | SUPPORTING_GOVERNED_OUTPUT | corresponding module | reports/phase_01/... | Required supporting evidence and handoff product | DESIGN_SPECIFIED | Protocol/Analysis/downstream |
| artifact/channel-quality coverage report | SUPPORTING_GOVERNED_OUTPUT | corresponding module | reports/phase_01/... | Required supporting evidence and handoff product | DESIGN_SPECIFIED | Protocol/Analysis/downstream |
| matched-comparison-key completeness report | SUPPORTING_GOVERNED_OUTPUT | corresponding module | reports/phase_01/... | Required supporting evidence and handoff product | DESIGN_SPECIFIED | Protocol/Analysis/downstream |
| downstream compatibility report | SUPPORTING_GOVERNED_OUTPUT | corresponding module | reports/phase_01/... | Required supporting evidence and handoff product | DESIGN_SPECIFIED | Protocol/Analysis/downstream |
| negative-result and diagnostic-only register | SUPPORTING_GOVERNED_OUTPUT | corresponding module | reports/phase_01/... | Required supporting evidence and handoff product | DESIGN_SPECIFIED | Protocol/Analysis/downstream |
| P01 output manifest | SUPPORTING_GOVERNED_OUTPUT | corresponding module | reports/phase_01/... | Required supporting evidence and handoff product | DESIGN_SPECIFIED | Protocol/Analysis/downstream |
| test manifest | SUPPORTING_GOVERNED_OUTPUT | corresponding module | reports/phase_01/... | Required supporting evidence and handoff product | DESIGN_SPECIFIED | Protocol/Analysis/downstream |
| gate decision record | SUPPORTING_GOVERNED_OUTPUT | corresponding module | reports/phase_01/... | Required supporting evidence and handoff product | DESIGN_SPECIFIED | Protocol/Analysis/downstream |
| Phase 1 handoff record | SUPPORTING_GOVERNED_OUTPUT | corresponding module | reports/phase_01/... | Required supporting evidence and handoff product | DESIGN_SPECIFIED | Protocol/Analysis/downstream |
| Kaggle execution-bundle manifest specification | SUPPORTING_GOVERNED_OUTPUT | corresponding module | reports/phase_01/... | Required supporting evidence and handoff product | DESIGN_SPECIFIED | Protocol/Analysis/downstream |


## 8.1 Trial/source-event rule

No standalone canonical `TrialRecord` is created. Trial/source-event lineage is preserved through `WindowRecord` fields and source IDs (`trial_id`, `parent_trial_id`, source-event identity or exact current equivalents), and through split/window manifests.

## 8.2 Failure states

Every output supports applicable states including `CREATED`, `VALIDATED`, `ACCEPTED`, `FAILED`, `BLOCKED`, `INVALID`, `DIAGNOSTIC_ONLY`, `DEFERRED`, `SUPERSEDED` and `INVALIDATED`, with reason, limitation and source links. Failed/negative branches remain in the bundle.


# 9. Physical Software Architecture

```text
src/iharq/layer1_data_protocol/
  __init__.py
  types.py
  errors.py
  status.py
  dataset_registry.py
  adapters/
    __init__.py
    base.py
    physionet_mi.py
    bnci2014_001.py
    lee2019_mi.py
    cho2017.py                 # inactive unless activated
    guttmannflury2025_mi.py    # screened profile only until activated
  metadata.py
  labels.py
  preprocessing.py
  quality.py
  splits.py
  budgets.py
  windows.py
  validation.py
  leakage.py
  cards.py
  manifests.py
  readiness.py
  bundle.py
  kaggle_adapter.py
  pipeline.py
configs/layer1/
contracts/layer1/
tests/layer1/
fixtures/layer1/
```

**API pattern:** deterministic typed functions/classes consume immutable input/config identities and return records plus explicit validation/status objects. File I/O is isolated in adapters and bundle writers. Scientific rules are configuration-backed and source-referenced, not hidden in notebook cells. Every writer is idempotent for identical inputs/config/environment; collision with different content fails closed.

## 9.1 Proposed public interfaces

```python
resolve_dataset_source(dataset_profile, access_context) -> ResolvedDatasetSource
load_dataset(source, loader_config) -> LoadedDataset
normalize_metadata(loaded, metadata_config) -> tuple[DatasetRecord, ...]
build_label_map(dataset_record, label_config) -> LabelMapRecord
apply_preprocessing(dataset_record, split_context, preprocessing_config) -> PreprocessingRecord
annotate_quality(dataset_record, quality_config) -> tuple[ArtifactFlagRecord, ...]
build_splits(dataset_records, split_config) -> tuple[SplitRecord, ...]
build_low_calibration_budgets(split_records, budget_config) -> BudgetManifest
materialize_windows(dataset_records, split_records, window_config) -> tuple[WindowRecord, ...]
audit_layer1(package, validation_config) -> ValidationReport
build_cards(package) -> tuple[DatasetCard, ProtocolCard]
build_layer1_manifest(package) -> Layer1Manifest
build_ablation_readiness(package) -> dict
export_phase_bundle(package, destination) -> BundleManifest
```

These names are Build Book physical proposals. Canonical record names remain Registry-owned.


# 10. Module-by-Module Implementation Dossiers


## 10.1 L1-MOD-01 - Dataset registry manager

- **Capability mapping:** `L1-01`
- **Proposed module:** `src/iharq/layer1_data_protocol/dataset_registry.py`
- **Purpose:** Resolve accepted dataset aliases, source identities, revisions, licenses, citations, checksums, access methods and eligibility; never infer source truth from a wrapper.
- **Inputs:** source-resolved records/configs appropriate to the responsibility, each with identity/hash/lifecycle/limitations.
- **Outputs:** DatasetRecord, source/provenance/license report.
- **Public behavior:** deterministic, configuration-driven, idempotent, restartable and fail-closed; never silently substitutes source data, repairs labels or crosses fit/evaluation boundaries.
- **Logging:** structured event ID, dataset/source/config/run IDs, counts, terminal status, reason codes, limitations and output hashes; no raw participant data in logs.
- **Tests:** unit, schema/contract, valid/invalid fixture, boundary/failure, idempotence and integrated P01 pipeline tests specific to this module.
- **Kaggle use:** imported by the single notebook; all major intermediate and final outputs written into the execution bundle.
- **Failure behavior:** affected branch becomes `BLOCKED`, `INVALID` or `DIAGNOSTIC_ONLY`; failed evidence is preserved; unrelated branches continue only when gate independence is proven.



## 10.2 L1-MOD-02 - Dataset loader

- **Capability mapping:** `L1-02`
- **Proposed module:** `src/iharq/layer1_data_protocol/adapters/base.py and adapters/<dataset>.py`
- **Purpose:** Load exact admitted source revision into a source-faithful intermediate representation; preserve source file/event identifiers and loader provenance.
- **Inputs:** source-resolved records/configs appropriate to the responsibility, each with identity/hash/lifecycle/limitations.
- **Outputs:** DatasetRecord, raw source inventory.
- **Public behavior:** deterministic, configuration-driven, idempotent, restartable and fail-closed; never silently substitutes source data, repairs labels or crosses fit/evaluation boundaries.
- **Logging:** structured event ID, dataset/source/config/run IDs, counts, terminal status, reason codes, limitations and output hashes; no raw participant data in logs.
- **Tests:** unit, schema/contract, valid/invalid fixture, boundary/failure, idempotence and integrated P01 pipeline tests specific to this module.
- **Kaggle use:** imported by the single notebook; all major intermediate and final outputs written into the execution bundle.
- **Failure behavior:** affected branch becomes `BLOCKED`, `INVALID` or `DIAGNOSTIC_ONLY`; failed evidence is preserved; unrelated branches continue only when gate independence is proven.



## 10.3 L1-MOD-03 - Metadata normalizer

- **Capability mapping:** `L1-03`
- **Proposed module:** `src/iharq/layer1_data_protocol/metadata.py`
- **Purpose:** Normalize subject/session/run/source-event/channel/sampling metadata while preserving source values, missingness, conflicts and derivation lineage.
- **Inputs:** source-resolved records/configs appropriate to the responsibility, each with identity/hash/lifecycle/limitations.
- **Outputs:** DatasetRecord, metadata completeness report.
- **Public behavior:** deterministic, configuration-driven, idempotent, restartable and fail-closed; never silently substitutes source data, repairs labels or crosses fit/evaluation boundaries.
- **Logging:** structured event ID, dataset/source/config/run IDs, counts, terminal status, reason codes, limitations and output hashes; no raw participant data in logs.
- **Tests:** unit, schema/contract, valid/invalid fixture, boundary/failure, idempotence and integrated P01 pipeline tests specific to this module.
- **Kaggle use:** imported by the single notebook; all major intermediate and final outputs written into the execution bundle.
- **Failure behavior:** affected branch becomes `BLOCKED`, `INVALID` or `DIAGNOSTIC_ONLY`; failed evidence is preserved; unrelated branches continue only when gate independence is proven.



## 10.4 L1-MOD-04 - Task and label ontology mapper

- **Capability mapping:** `L1-04`
- **Proposed module:** `src/iharq/layer1_data_protocol/labels.py`
- **Purpose:** Map original dataset labels to governed normalized intent/task labels contextually; preserve original labels, exclusions, rest/no-action and proxy-intent limits.
- **Inputs:** source-resolved records/configs appropriate to the responsibility, each with identity/hash/lifecycle/limitations.
- **Outputs:** LabelMapRecord, label-map validation report.
- **Public behavior:** deterministic, configuration-driven, idempotent, restartable and fail-closed; never silently substitutes source data, repairs labels or crosses fit/evaluation boundaries.
- **Logging:** structured event ID, dataset/source/config/run IDs, counts, terminal status, reason codes, limitations and output hashes; no raw participant data in logs.
- **Tests:** unit, schema/contract, valid/invalid fixture, boundary/failure, idempotence and integrated P01 pipeline tests specific to this module.
- **Kaggle use:** imported by the single notebook; all major intermediate and final outputs written into the execution bundle.
- **Failure behavior:** affected branch becomes `BLOCKED`, `INVALID` or `DIAGNOSTIC_ONLY`; failed evidence is preserved; unrelated branches continue only when gate independence is proven.



## 10.5 L1-MOD-05 - Preprocessing registry and lawful executor

- **Capability mapping:** `L1-05`
- **Proposed module:** `src/iharq/layer1_data_protocol/preprocessing.py`
- **Purpose:** Register source-native and derived preprocessing; enforce split-aware fit scope, deterministic transforms, no held-out fitting, and stable preprocessing identity.
- **Inputs:** source-resolved records/configs appropriate to the responsibility, each with identity/hash/lifecycle/limitations.
- **Outputs:** PreprocessingRecord, preprocessing fit-scope report.
- **Public behavior:** deterministic, configuration-driven, idempotent, restartable and fail-closed; never silently substitutes source data, repairs labels or crosses fit/evaluation boundaries.
- **Logging:** structured event ID, dataset/source/config/run IDs, counts, terminal status, reason codes, limitations and output hashes; no raw participant data in logs.
- **Tests:** unit, schema/contract, valid/invalid fixture, boundary/failure, idempotence and integrated P01 pipeline tests specific to this module.
- **Kaggle use:** imported by the single notebook; all major intermediate and final outputs written into the execution bundle.
- **Failure behavior:** affected branch becomes `BLOCKED`, `INVALID` or `DIAGNOSTIC_ONLY`; failed evidence is preserved; unrelated branches continue only when gate independence is proven.



## 10.6 L1-MOD-06 - Artifact and channel-quality annotator

- **Capability mapping:** `L1-06`
- **Proposed module:** `src/iharq/layer1_data_protocol/quality.py`
- **Purpose:** Annotate missing/bad channels, short trials, rate mismatches and source-supported artifact evidence; do not silently repair confirmatory source evidence.
- **Inputs:** source-resolved records/configs appropriate to the responsibility, each with identity/hash/lifecycle/limitations.
- **Outputs:** ArtifactFlagRecord, quality coverage report.
- **Public behavior:** deterministic, configuration-driven, idempotent, restartable and fail-closed; never silently substitutes source data, repairs labels or crosses fit/evaluation boundaries.
- **Logging:** structured event ID, dataset/source/config/run IDs, counts, terminal status, reason codes, limitations and output hashes; no raw participant data in logs.
- **Tests:** unit, schema/contract, valid/invalid fixture, boundary/failure, idempotence and integrated P01 pipeline tests specific to this module.
- **Kaggle use:** imported by the single notebook; all major intermediate and final outputs written into the execution bundle.
- **Failure behavior:** affected branch becomes `BLOCKED`, `INVALID` or `DIAGNOSTIC_ONLY`; failed evidence is preserved; unrelated branches continue only when gate independence is proven.



## 10.7 L1-MOD-07 - Split and protocol manager

- **Capability mapping:** `L1-07`
- **Proposed module:** `src/iharq/layer1_data_protocol/splits.py`
- **Purpose:** Generate immutable hierarchical subject/session/run/source-event-safe splits, explicit role separation and attrition accounting.
- **Inputs:** source-resolved records/configs appropriate to the responsibility, each with identity/hash/lifecycle/limitations.
- **Outputs:** SplitRecord, split-disjointness report.
- **Public behavior:** deterministic, configuration-driven, idempotent, restartable and fail-closed; never silently substitutes source data, repairs labels or crosses fit/evaluation boundaries.
- **Logging:** structured event ID, dataset/source/config/run IDs, counts, terminal status, reason codes, limitations and output hashes; no raw participant data in logs.
- **Tests:** unit, schema/contract, valid/invalid fixture, boundary/failure, idempotence and integrated P01 pipeline tests specific to this module.
- **Kaggle use:** imported by the single notebook; all major intermediate and final outputs written into the execution bundle.
- **Failure behavior:** affected branch becomes `BLOCKED`, `INVALID` or `DIAGNOSTIC_ONLY`; failed evidence is preserved; unrelated branches continue only when gate independence is proven.



## 10.8 L1-MOD-08 - Trial/window generator

- **Capability mapping:** `L1-08`
- **Proposed module:** `src/iharq/layer1_data_protocol/windows.py`
- **Purpose:** Create event-aligned lineage-preserving windows with immutable identity, parent source-event/trial links, timing, stride and overlap-group metadata.
- **Inputs:** source-resolved records/configs appropriate to the responsibility, each with identity/hash/lifecycle/limitations.
- **Outputs:** WindowRecord, window timing/overlap report.
- **Public behavior:** deterministic, configuration-driven, idempotent, restartable and fail-closed; never silently substitutes source data, repairs labels or crosses fit/evaluation boundaries.
- **Logging:** structured event ID, dataset/source/config/run IDs, counts, terminal status, reason codes, limitations and output hashes; no raw participant data in logs.
- **Tests:** unit, schema/contract, valid/invalid fixture, boundary/failure, idempotence and integrated P01 pipeline tests specific to this module.
- **Kaggle use:** imported by the single notebook; all major intermediate and final outputs written into the execution bundle.
- **Failure behavior:** affected branch becomes `BLOCKED`, `INVALID` or `DIAGNOSTIC_ONLY`; failed evidence is preserved; unrelated branches continue only when gate independence is proven.



## 10.9 L1-MOD-09 - Data validation and leakage auditor

- **Capability mapping:** `L1-09`
- **Proposed module:** `src/iharq/layer1_data_protocol/validation.py and leakage.py`
- **Purpose:** Validate schemas, metadata, labels, fit scope, split disjointness, temporal/source-event overlap, duplicate lineage, matched keys and downstream compatibility.
- **Inputs:** source-resolved records/configs appropriate to the responsibility, each with identity/hash/lifecycle/limitations.
- **Outputs:** ValidationReport, leakage report, matched-key completeness report.
- **Public behavior:** deterministic, configuration-driven, idempotent, restartable and fail-closed; never silently substitutes source data, repairs labels or crosses fit/evaluation boundaries.
- **Logging:** structured event ID, dataset/source/config/run IDs, counts, terminal status, reason codes, limitations and output hashes; no raw participant data in logs.
- **Tests:** unit, schema/contract, valid/invalid fixture, boundary/failure, idempotence and integrated P01 pipeline tests specific to this module.
- **Kaggle use:** imported by the single notebook; all major intermediate and final outputs written into the execution bundle.
- **Failure behavior:** affected branch becomes `BLOCKED`, `INVALID` or `DIAGNOSTIC_ONLY`; failed evidence is preserved; unrelated branches continue only when gate independence is proven.



## 10.10 L1-MOD-10 - Dataset-card and protocol-card generator

- **Capability mapping:** `L1-10A`
- **Proposed module:** `src/iharq/layer1_data_protocol/cards.py`
- **Purpose:** Generate source-grounded DatasetCard and ProtocolCard from accepted records/manifests with limitations, exclusions and permitted-use boundaries.
- **Inputs:** source-resolved records/configs appropriate to the responsibility, each with identity/hash/lifecycle/limitations.
- **Outputs:** DatasetCard, ProtocolCard.
- **Public behavior:** deterministic, configuration-driven, idempotent, restartable and fail-closed; never silently substitutes source data, repairs labels or crosses fit/evaluation boundaries.
- **Logging:** structured event ID, dataset/source/config/run IDs, counts, terminal status, reason codes, limitations and output hashes; no raw participant data in logs.
- **Tests:** unit, schema/contract, valid/invalid fixture, boundary/failure, idempotence and integrated P01 pipeline tests specific to this module.
- **Kaggle use:** imported by the single notebook; all major intermediate and final outputs written into the execution bundle.
- **Failure behavior:** affected branch becomes `BLOCKED`, `INVALID` or `DIAGNOSTIC_ONLY`; failed evidence is preserved; unrelated branches continue only when gate independence is proven.



## 10.11 L1-MOD-11 - Provenance and manifest builder

- **Capability mapping:** `L1-10B`
- **Proposed module:** `src/iharq/layer1_data_protocol/manifests.py and bundle.py`
- **Purpose:** Create Layer1Manifest, readiness artifact, output/test/gate manifests, hashes, failure register and phase handoff.
- **Inputs:** source-resolved records/configs appropriate to the responsibility, each with identity/hash/lifecycle/limitations.
- **Outputs:** Layer1Manifest, layer1_ablation_readiness_l1_v1.json, P01 output manifest.
- **Public behavior:** deterministic, configuration-driven, idempotent, restartable and fail-closed; never silently substitutes source data, repairs labels or crosses fit/evaluation boundaries.
- **Logging:** structured event ID, dataset/source/config/run IDs, counts, terminal status, reason codes, limitations and output hashes; no raw participant data in logs.
- **Tests:** unit, schema/contract, valid/invalid fixture, boundary/failure, idempotence and integrated P01 pipeline tests specific to this module.
- **Kaggle use:** imported by the single notebook; all major intermediate and final outputs written into the execution bundle.
- **Failure behavior:** affected branch becomes `BLOCKED`, `INVALID` or `DIAGNOSTIC_ONLY`; failed evidence is preserved; unrelated branches continue only when gate independence is proven.


# 11. Configuration, Environment and Dependency Architecture

- P01 configuration extends `configs/phases/p01.yaml` without changing canonical phase identity.
- Dataset profiles are separate and status-bearing; inactive/screened profiles cannot execute without explicit activation.
- Every effective config is canonical-serialized and hashed; the execution bundle stores source and resolved snapshots.
- The notebook environment must support the existing Phase 0 package plus accepted EEG loaders/analysis libraries. Exact versions are resolved through compatibility tests before Kaggle execution.
- Current P01's `python312.yaml` reference is a template hook, not proof of a verified environment. The notebook may use an accepted Python 3.11-3.13 environment after all imports and clean reproduction pass.
- Secrets use Kaggle Secrets/environment injection and never enter configs, logs or ZIPs.
- Large caches are disposable and not evidence; source/checksum/manifests are evidence.


# 12. Source Access, Licensing and Dataset Adapter Design

For each active dataset, the registry module must create a source admission decision before download/load. Admission requires exact name/aliases, official source/DOI/archive identity, release or retrieval timestamp where no release exists, license/access/redistribution terms, citation, loader route, checksum policy, expected metadata hierarchy, known factual conflicts and intended P01 role. Wrapper facts are recorded separately from source facts.

The loader cache key is `(dataset_id, source_revision, source_hash, loader_version, loader_config_hash)`. A fallback mirror is accepted only when byte identity or an authority-approved equivalence record is established. Unsupported or unverifiable sources fail closed; they are not silently replaced.


# 13. Preprocessing, Split, Budget and Window Design

## 13.1 Preprocessing

Minimal declared preprocessing is source-aware and split-aware. Source-native transformations are preserved as provenance. Derived train-fitted transformations fit only on permitted training/calibration membership and are then applied immutably. Held-out test/evaluation information cannot influence filter choice, normalization, artifact threshold, channel selection or any fitted transform. Every effective preprocessing pipeline has version, code/config/environment identities and fit-membership hash.

## 13.2 Split protocol

The split engine operates on the highest leakage-risk grouping available: subject, session, run and source event. Random window-level split is prohibited. Source-event atomicity is mandatory. Within-subject, cross-session and cross-subject regimes are created only where dataset structure makes them valid. Membership, exclusions, attrition and class counts reconcile exactly. Adjacent/overlapping windows use overlap groups plus purge/embargo protection where the accepted profile requires it.

## 13.3 Low-calibration budgets

Budgets are class-aware, source-event based, reproducible and identified by dataset/task/split/subject-or-target-group/budget/seed/config. Selection cannot inspect validation/test outcomes. Insufficient class support creates explicit ineligibility or diagnostic-only status; it does not trigger ad hoc budget changes.

## 13.4 Windows

Windows are event-aligned and retain immutable dataset/subject/session/run/source-event/trial lineage, original and normalized labels, sample/time bounds, duration/stride, overlap group, preprocessing ID, split ID, budget context, status and limitations. Numerical timing profiles remain config values to be resolved before real execution.


# 14. Validation, Leakage, Cards and Manifest Design

Validation order is: authority/source admission -> schema/identity -> metadata -> label map -> preprocessing fit scope -> split membership -> window lineage/overlap -> leakage/chronology -> quality coverage -> matched-key/A0-A13 readiness -> cards -> manifests/hashes -> P02 compatibility -> complete closure.

The auditor produces one `ValidationReport` with individual gate entries and machine-readable evidence files. It never rewrites invalid inputs. Cards are projections of accepted records/manifests. `Layer1Manifest` is the immutable index. The readiness artifact records key completeness and downgrade reasons; it is not an ablation result.


# 15. A0-A13 Readiness and A14 Rejection

| A-ID | Official role | Owning layer(s) | Activation phase | P01 source/protocol dependency | P01 status | Failure/invalidation |
| --- | --- | --- | --- | --- | --- | --- |
| A0 | Raw decoder baseline | L2 | P02 | dataset/split/budget/window/preprocessing/label/seed keys for raw prediction baseline | READINESS_ONLY_NOT_EXECUTED_IN_P01 | Missing keys -> NOT_READY/DIAGNOSTIC_ONLY; invalidate descendants after L1 change |
| A1 | Calibrated decoder | L3 | P03 | calibration-fit/evaluation split roles and source prediction lineage | READINESS_ONLY_NOT_EXECUTED_IN_P01 | Missing keys -> NOT_READY/DIAGNOSTIC_ONLY; invalidate descendants after L1 change |
| A2 | Selective prediction / abstention | L3 | P03 | threshold-validation/evaluation separation and matched operating-point keys | READINESS_ONLY_NOT_EXECUTED_IN_P01 | Missing keys -> NOT_READY/DIAGNOSTIC_ONLY; invalidate descendants after L1 change |
| A3 | Longer-window evidence | L3 | P03 | window-family identity, parent-event atomicity and overlap/purge groups | READINESS_ONLY_NOT_EXECUTED_IN_P01 | Missing keys -> NOT_READY/DIAGNOSTIC_ONLY; invalidate descendants after L1 change |
| A4 | Ordinary aggregation/control | L2/L4 | P02/P04 | common source windows, model, seed and ordinary-control configuration keys | READINESS_ONLY_NOT_EXECUTED_IN_P01 | Missing keys -> NOT_READY/DIAGNOSTIC_ONLY; invalidate descendants after L1 change |
| A5 | IHARQ-lite evidence verification | L4 | P04 | complete source/protocol/matched-key substrate and missing-evidence visibility | READINESS_ONLY_NOT_EXECUTED_IN_P01 | Missing keys -> NOT_READY/DIAGNOSTIC_ONLY; invalidate descendants after L1 change |
| A6 | Learned evidence-quality branch | L6 | P06 | quality/metadata/validation source features with decision-time visibility labels | READINESS_ONLY_NOT_EXECUTED_IN_P01 | Missing keys -> NOT_READY/DIAGNOSTIC_ONLY; invalidate descendants after L1 change |
| A7 | Temporal/regime trust component | L5 | P05 | chronological sequence, subject/session/run/source-event identity and no leakage | READINESS_ONLY_NOT_EXECUTED_IN_P01 | Missing keys -> NOT_READY/DIAGNOSTIC_ONLY; invalidate descendants after L1 change |
| A8 | Learning-to-defer/routing | L6 | P07 | route-eligible label/task/source groups, burden/capacity grouping and matching keys | READINESS_ONLY_NOT_EXECUTED_IN_P01 | Missing keys -> NOT_READY/DIAGNOSTIC_ONLY; invalidate descendants after L1 change |
| A9 | Supervised readiness policy | L6 | P06 | target-label provenance, budget/source grouping and frozen evaluation membership | READINESS_ONLY_NOT_EXECUTED_IN_P01 | Missing keys -> NOT_READY/DIAGNOSTIC_ONLY; invalidate descendants after L1 change |
| A10 | Contextual bandit policy | L6/L7 | P10 | behavior-log compatible episode/source identities and immutable evaluation splits | READINESS_ONLY_NOT_EXECUTED_IN_P01 | Missing keys -> NOT_READY/DIAGNOSTIC_ONLY; invalidate descendants after L1 change |
| A11 | Reinforcement-learning policy | L6/L7 | P11 | trajectory-compatible source/session identities and simulator-only boundary metadata | READINESS_ONLY_NOT_EXECUTED_IN_P01 | Missing keys -> NOT_READY/DIAGNOSTIC_ONLY; invalidate descendants after L1 change |
| A12 | StressForge robustness | L8 | P09 | clean-source immutability, derived stressed pair keys and source-window matching | READINESS_ONLY_NOT_EXECUTED_IN_P01 | Missing keys -> NOT_READY/DIAGNOSTIC_ONLY; invalidate descendants after L1 change |
| A13 | Embodiment proxy | L9 | P12/P13 | proxy-intent label limitations, command mapping eligibility and source provenance | READINESS_ONLY_NOT_EXECUTED_IN_P01 | Missing keys -> NOT_READY/DIAGNOSTIC_ONLY; invalidate descendants after L1 change |

`A14` is rejected. No A14 selector, configuration, record, readiness row, run, output, card or result may be produced. A malformed A14 fixture must fail closed.


# 16. Kaggle-Ready Full Execution Design

## 16.1 Notebook identity

`IHARQ_Phase_01_Layer_01_Complete_Public_Data_and_Split_Execution_R1.ipynb`

One notebook is planned. A second is not authorized by this annex and may be proposed later only if a demonstrated Kaggle environment/runtime/memory or immutable-stage boundary makes one notebook technically impossible. No smoke-only, fast or fixture-only phase-execution path exists.

## 16.2 Ordered notebook sections

1. phase/source identity and declarations;
2. environment and dependency installation;
3. cumulative ZIP intake and hash verification;
4. Phase 0 foundation and P01 contract validation;
5. authority/config/source profile resolution;
6. license/access/checksum admission;
7. dataset acquisition/loading;
8. metadata normalization;
9. contextual label mapping;
10. preprocessing registration/execution;
11. quality annotation;
12. split and low-calibration construction;
13. window generation;
14. schema/identity/lineage validation;
15. leakage/chronology/overlap audits;
16. matched-key and A0-A13 readiness audit;
17. cards and manifests;
18. negative/failed/blocked outcome preservation;
19. evidence-sufficiency gate;
20. complete bundle/checksum/handoff export.

Notebook consolidation is organizational only: every active dataset, split regime, budget, window profile, validation, readiness row and required artifact remains separately identified and retrievable.

## 16.3 Execution bundle

```text
phase_01_layer_01_execution_bundle_<RUN_ID>/
  README.md
  authority_manifest.json
  source_project_state_manifest.json
  environment_manifest.json
  notebook_manifest.json
  config_snapshot/
  dataset_sources/
  records/{dataset,preprocessing,labels,splits,windows,artifact_flags}/
  reports/{validation,provenance,metadata,leakage,low_calibration,matched_keys,compatibility}/
  cards/
  manifests/
  negative_and_failed_results/
  protocol_v1_handoff/
  analysis_inputs/
  layer0_handoff/
  evidence_map_handoff/
  layer10_source_bundle/
  gate_decision.json
  phase_execution_handoff.yaml
  checksums.sha256
```

No major output may remain only in a transient Kaggle directory. Oversized artifacts are externalized only with immutable pointer, hash, size, license/access and retrieval metadata.


# 17. Test Architecture

| Test family | Required scope | Pass evidence |
| --- | --- | --- |
| unit | All relevant L1 modules/records/contracts for unit | reports/phase_01/tests/unit.json |
| schema | All relevant L1 modules/records/contracts for schema | reports/phase_01/tests/schema.json |
| config | All relevant L1 modules/records/contracts for config | reports/phase_01/tests/config.json |
| contract | All relevant L1 modules/records/contracts for contract | reports/phase_01/tests/contract.json |
| loader | All relevant L1 modules/records/contracts for loader | reports/phase_01/tests/loader.json |
| dataset factual-profile | All relevant L1 modules/records/contracts for dataset factual-profile | reports/phase_01/tests/dataset_factual-profile.json |
| metadata | All relevant L1 modules/records/contracts for metadata | reports/phase_01/tests/metadata.json |
| label-map | All relevant L1 modules/records/contracts for label-map | reports/phase_01/tests/label-map.json |
| preprocessing fit-scope | All relevant L1 modules/records/contracts for preprocessing fit-scope | reports/phase_01/tests/preprocessing_fit-scope.json |
| split disjointness | All relevant L1 modules/records/contracts for split disjointness | reports/phase_01/tests/split_disjointness.json |
| subject/session/run/source-event leakage | All relevant L1 modules/records/contracts for subject/session/run/source-event leakage | reports/phase_01/tests/subject/session/run/source-event_leakage.json |
| window identity and overlap | All relevant L1 modules/records/contracts for window identity and overlap | reports/phase_01/tests/window_identity_and_overlap.json |
| low-calibration budget | All relevant L1 modules/records/contracts for low-calibration budget | reports/phase_01/tests/low-calibration_budget.json |
| artifact flag | All relevant L1 modules/records/contracts for artifact flag | reports/phase_01/tests/artifact_flag.json |
| matched-key completeness | All relevant L1 modules/records/contracts for matched-key completeness | reports/phase_01/tests/matched-key_completeness.json |
| A0-A13 readiness | All relevant L1 modules/records/contracts for A0-A13 readiness | reports/phase_01/tests/A0-A13_readiness.json |
| A14 rejection | All relevant L1 modules/records/contracts for A14 rejection | reports/phase_01/tests/A14_rejection.json |
| card-source consistency | All relevant L1 modules/records/contracts for card-source consistency | reports/phase_01/tests/card-source_consistency.json |
| manifest/path/hash | All relevant L1 modules/records/contracts for manifest/path/hash | reports/phase_01/tests/manifest/path/hash.json |
| negative and malformed fixture | All relevant L1 modules/records/contracts for negative and malformed fixture | reports/phase_01/tests/negative_and_malformed_fixture.json |
| failure-state | All relevant L1 modules/records/contracts for failure-state | reports/phase_01/tests/failure-state.json |
| idempotence | All relevant L1 modules/records/contracts for idempotence | reports/phase_01/tests/idempotence.json |
| restart/recovery | All relevant L1 modules/records/contracts for restart/recovery | reports/phase_01/tests/restart/recovery.json |
| integration | All relevant L1 modules/records/contracts for integration | reports/phase_01/tests/integration.json |
| clean-environment reproduction | All relevant L1 modules/records/contracts for clean-environment reproduction | reports/phase_01/tests/clean-environment_reproduction.json |
| Phase 2 contract | All relevant L1 modules/records/contracts for Phase 2 contract | reports/phase_01/tests/Phase_2_contract.json |
| Layer 0 limitation propagation | All relevant L1 modules/records/contracts for Layer 0 limitation propagation | reports/phase_01/tests/Layer_0_limitation_propagation.json |
| Layer 10 read-only handoff | All relevant L1 modules/records/contracts for Layer 10 read-only handoff | reports/phase_01/tests/Layer_10_read-only_handoff.json |

# 18. Phase 1 Gate Matrix

| Gate | Name | Pass condition | Failure consequence | Repair owner | Evidence |
| --- | --- | --- | --- | --- | --- |
| P01-G01 | Authority and Phase 0 intake | Authority/config/project-state manifests present, hashes match, P01 contracts resolve | Block P01 execution | Build Book/intake | reports/phase_01/gates/P01-G01.json |
| P01-G02 | Source/provenance/license | Exact source revision, citation, access, license and checksum resolved for every active dataset | Block affected dataset | dataset registry/owner | reports/phase_01/gates/P01-G02.json |
| P01-G03 | Schema and canonical object | Every record validates and identity/lifecycle/lineage is complete | Block affected outputs | Registry/implementation | reports/phase_01/gates/P01-G03.json |
| P01-G04 | Metadata completeness | Required subject/session/run/event/channel/rate fields present or explicit missingness/downgrade recorded | Downgrade/block dataset branch | metadata/source | reports/phase_01/gates/P01-G04.json |
| P01-G05 | Label mapping | All included source labels map contextually; exclusions/rest/no-action limits explicit | Block affected task branch | labels/Method Selection | reports/phase_01/gates/P01-G05.json |
| P01-G06 | Preprocessing fit scope | No held-out evaluation information influences fitting/tuning; source-native/derived provenance closed | Invalidate affected descendants | preprocessing/Protocol | reports/phase_01/gates/P01-G06.json |
| P01-G07 | Split disjointness | Declared group keys are disjoint and membership/attrition totals reconcile | Block phase evidence | splits | reports/phase_01/gates/P01-G07.json |
| P01-G08 | Leakage and chronology | No subject/session/run/source-event/window leakage; overlap purge/embargo rules pass where applicable | Block phase evidence | validation/splits/windows | reports/phase_01/gates/P01-G08.json |
| P01-G09 | Low-calibration budgets | Class-aware source-event membership, IDs, seeds and no contamination verified | Block affected budget cells | splits/Protocol | reports/phase_01/gates/P01-G09.json |
| P01-G10 | Window identity | Timing, parent lineage, overlap groups, split/preprocessing/label links complete and immutable | Block affected windows | windows | reports/phase_01/gates/P01-G10.json |
| P01-G11 | Quality coverage | Source-supported quality fields/absence/limitations represented without silent repair | Downgrade or block affected use | quality | reports/phase_01/gates/P01-G11.json |
| P01-G12 | Matched keys and A0-A13 readiness | Required source/protocol keys complete or diagnostic-only reason recorded for every A0-A13 row; A14 absent | Block downstream activation | validation/Protocol | reports/phase_01/gates/P01-G12.json |
| P01-G13 | Cards and limitations | Cards reproduce source records/manifests and preserve Layer 0 limitations | Block card promotion | cards/Layer0 | reports/phase_01/gates/P01-G13.json |
| P01-G14 | Manifest, path and hash closure | Every output is indexed, hash-valid, path-resolvable and lifecycle-consistent | Block bundle acceptance | manifests | reports/phase_01/gates/P01-G14.json |
| P01-G15 | Phase 2 compatibility | P02 consumer contract validates against accepted L1 records and handoff | Block P02 handoff | integration/L2 consumer | reports/phase_01/gates/P01-G15.json |
| P01-G16 | Complete artifact closure | All required records/reports/cards/manifests/tests/gates exist or have lawful terminal states | Block P01 execution acceptance | phase owner | reports/phase_01/gates/P01-G16.json |

# 19. Evidence-Insufficiency Loopback

The only loopback is:

```text
insufficient/invalid/incomplete/unusable evidence
-> identify exact defect and lawful owner
-> preserve failed bundle and gate decision
-> change the minimum necessary implementation/config/input/notebook section
-> issue new code/config/run identity
-> invalidate only affected descendants
-> rerun affected scope when partial rerun safety is proven; otherwise rerun full dataset branch
-> regenerate complete bundle
-> reevaluate P01-G01..P01-G16
```

A full rerun is mandatory after source bytes/revision, label semantics, split membership, preprocessing fit population, window identity, leakage rules or bundle identity changes. Terminal states are `ACCEPTED`, `BLOCKED`, `DEFERRED`, `INVALID` and `DIAGNOSTIC_ONLY` with reasons.


# 20. Work Packages and Implementation Roadmap

| WP | Title | Purpose | Dependency | Outputs | Gates |
| --- | --- | --- | --- | --- | --- |
| WP-L1-01 | Layer 1 contracts and configuration | Freeze physical paths/APIs/config schemas/dataset profiles/fixtures/gates without inventing scientific constants | WP-00-05/P00 foundation | authority/reuse matrices; config and contract successors; source profile templates; fixture plan; open-decision routing | P01-G01..G05 |
| WP-L1-02 | Layer 1 reusable core implementation | Implement importable 11-responsibility Layer 1 package using existing Phase 0 schemas/identity/validation foundations | WP-L1-01 | dataset registry/adapters; metadata/labels; preprocessing/quality; splits/budgets/windows; validation; cards/manifests; tests | P01-G02..G14 |
| WP-L1-03 | Layer 1 full integration, Kaggle execution readiness and handoff | Integrate full real-data path, notebook adapter, bundle exporter, evidence sufficiency and P02/later handoffs; no smoke deliverable | WP-L1-02 | single-notebook specification; execution bundle spec; integration/reproduction tests; P01/P02 handoff builders | P01-G01..G16 |

## 20.1 Task sequence

1. Freeze source/authority/reuse manifests and current P01 physical profile.
2. Resolve or mark every source/environment/Protocol owner decision.
3. Implement contracts/configs/source profiles and fixtures.
4. Implement modules 01-11 in dependency order.
5. Add module and cross-module tests.
6. Add P01 CLI/notebook adapter and bundle exporter.
7. Validate against Phase 0 schemas/identity/lifecycle infrastructure.
8. Validate P02 consumer contract.
9. Freeze the notebook specification and create the notebook in the next task.


# 21. Layer 0, Evidence Map and Layer 10 Handoff Readiness

- **Layer 0:** this annex supplies limitation vocabularies, source/public-data boundaries, diagnostic-only reasons and candidate claim-source fields; no claim is reviewed now.
- **Evidence Map:** the future execution bundle supplies exact run/record/gate/report IDs and figure/table source paths; no map is updated now.
- **Layer 10:** cards, manifests, validation/readiness and source bundle interfaces are defined; Layer 10 remains read-only and is not created now.


# 22. Phase 2 and Later Handoff

The P02 handoff must contain accepted DatasetRecord, LabelMapRecord, PreprocessingRecord, SplitRecord, WindowRecord, optional ArtifactFlagRecord, ValidationReport, DatasetCard, ProtocolCard, Layer1Manifest, readiness artifact, source/license/checksum manifest, effective configs, environment, limitations and exact immutable paths/hashes.

P02 may consume but must not overwrite L1 source records. Any L1 invalidation requires downstream acknowledgment and regeneration. Later phases consume the same identity spine for matching, chronology, stress pairs, simulation and presentation.


# 23. Risks and Open Decisions

| ID | Topic | Classification | Blocks document | Blocks Kaggle | Resolution |
| --- | --- | --- | --- | --- | --- |
| P01-OD-001 | Exact active dataset revisions and immutable source identities | OWNER_DECISION_REQUIRED_BEFORE_REAL_RUN | FALSE | TRUE | Select exact revisions only from current Method Selection portfolio; record URL/DOI/revision/checksum/license/citation. |
| P01-OD-002 | Dataset access credentials/cache and Kaggle download route | EXTERNAL_ACCESS_REQUIRED | FALSE | TRUE | Owner supplies access method/credentials through Kaggle Secrets when required; no credentials in archive. |
| P01-OD-003 | Exact Phase 1 Python/Kaggle environment and dependency pins | BUILD_BOOK_PHYSICAL_DECISION | FALSE | TRUE | Resolve a Python 3.11-3.13 compatible environment; validate MOABB/MNE and source adapters; pin only after actual compatibility checks. |
| P01-OD-004 | Exact numerical preprocessing, split, low-calibration and window constants | PROTOCOL_V1_FIELD_REQUIRED_AFTER_RUN | FALSE | TRUE | Expose typed config fields and constraints now; do not invent values; resolve in the notebook execution configuration and faithfully record in P01 Protocol v1.0. |
| P01-OD-005 | Standalone TrialRecord | RESOLVED_BY_CURRENT_AUTHORITY | FALSE | FALSE | Do not create; preserve trial/source-event identity through WindowRecord parent lineage and source-event fields. |
| P01-OD-006 | GuttmannFlury2025_MI promotion | OWNER_DECISION_REQUIRED_BEFORE_REAL_RUN | FALSE | FALSE | Remain screened candidate until factual source profile and owner activation pass. |
| P01-OD-007 | Intermediate GitHub publication | RESOLVED_BY_CURRENT_AUTHORITY | FALSE | FALSE | Not required under Governance V6.1; cumulative ZIP is primary. External storage only for oversized artifacts. |
| P01-OD-008 | Phase 0 formal closure/publication status versus P01 documentary planning | NONBLOCKING_FOR_DOCUMENT_CREATION | FALSE | TRUE | Preserve historical status. P01 Build Book may be created; real-data execution requires owner acceptance of V6.1 entry and all non-publication P01 gates. |

The open decisions are nonblocking for creation of this implementation authority. P01 real-data Kaggle execution is blocked until P01-OD-001 through P01-OD-004 and the applicable entry authorization are resolved.


# 24. Definition of Done

This annex is complete when authority and source hashes close; P00 reuse is explicit; all 11 responsibilities and 10-capability mapping are covered; the selected dataset/method statuses are preserved; all inputs/outputs/modules/configs/tests/gates/readiness/handoffs are specified; one full notebook and bundle are specified; no smoke path or numerical result is invented; machine companions parse; annex and integrated copy are identical; local bounded checks pass or limitations are recorded.

It is **not** proof that P01 has been implemented or executed.


# 25. Final Self-Audit

- Target is P01/L1, not P02.
- Governance V6.1 controls.
- L1 owns implementation; L0 and L10 boundaries are preserved.
- All seven authorities and the Phase 0 cumulative package were used.
- The R6 Build Book is continued, not recreated.
- P00 capabilities are reused by identity.
- Eleven official responsibilities and ten physical capabilities are mapped losslessly.
- Dataset statuses are preserved; no candidate is promoted.
- No source revision, license, checksum or numerical Protocol constant is invented.
- Eight canonical L1 record schemas are reused; no TrialRecord is invented.
- A0-A13 readiness is complete and non-empirical; A14 is rejected.
- One full Kaggle notebook is specified; no smoke track exists.
- All tests, gates, failures and the sole evidence-insufficiency loopback are specified.
- P02 and later handoffs are complete at design level.
- P01 implementation, execution, evidence, Protocol completion, Phase Analysis, Layer 0, Evidence Map, Layer 10, closure and P02 authorization are not claimed.


<!-- END EXACT R1 ANNEX -->
