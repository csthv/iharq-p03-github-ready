# P02 Training-Policy Blocker Resolution — External Evidence Note R1

**Status:** supporting rationale for `P02-PREEXEC-TRAINING-POLICY-AMENDMENT-R1`  
**Authority role:** SUPPORTING / NON-SUPERSEDING. This note does not replace IHARQ project authority, the owner-authorized amendment, or the future cumulative Protocol v1.0 / Build Book synchronization.

## 1. Source-exhaustion result inside IHARQ

The project authorities already select the high-level methods and boundaries:

- primary neural training has no stochastic augmentation;
- one separately identified Segmentation-and-Reconstruction (S&R) challenger is permitted/required for EEGNet at FULL_TRAIN only;
- the challenger is training-only and cannot create canonical Layer-1 windows;
- class weighting is permitted only under a predeclared training-fold rule when needed;
- the exact S&R probability/segment count/identity and exact class-weight activation policy were deliberately left to Protocol/Nuts-and-Bolts synchronization.

The pre-execution R2 audit correctly treated those two missing bindings as scientific-freeze blockers instead of Python defaults. Owner authorization then permitted the smallest research-grounded P02-only amendment.

## 2. Segmentation-and-Reconstruction implementation evidence

Braindecode documents `SegmentationReconstruction(probability, n_segments=None, random_state=None)` and describes it as label-aware segment mixing that preserves the original temporal segment order. The transform exposes the application probability, segment count, and random state explicitly and cites Lotte (2015).

IHARQ therefore retains its project-specific implementation rather than replacing it with an opaque notebook-local transform. The implementation preserves the same core algorithmic invariants while enforcing the stronger IHARQ donor boundary: same dataset, same legal training role, same task, same class, and no validation/test donor access. Donor provenance is recorded. The source array is not mutated and augmented tensors are ephemeral.

### Frozen P02 diagnostic value

- `probability = 0.5`
- `n_segments = 4`

These are **not claimed to be universally optimal**. Braindecode's official EEG augmentation examples commonly use a 0.5 application probability for stochastic transforms, and its augmentation-search tutorial emphasizes that augmentation effectiveness and strength are task-dependent. Rommel et al. likewise report that there is no single best EEG augmentation strategy across tasks. Accordingly, P02 uses 0.5 as a fixed moderate diagnostic application rate to avoid opening a new hyperparameter search.

Four segments are used because four is the only S&R segmentation count already exercised by the IHARQ bounded technical feasibility check. That earlier check was not itself scientific authority; the owner-authorized amendment is what promotes four segments into the P02 diagnostic freeze.

## 3. Class-weight evidence and P02-specific decision

Scikit-learn documents uniform weights when `class_weight=None` and its inverse-frequency `balanced` heuristic for unbalanced datasets. PyTorch's `CrossEntropyLoss(weight=...)` likewise describes class weights as particularly useful for unbalanced training sets.

The current governed P02 FULL_TRAIN counts are:

| dataset | left_hand | right_hand |
|---|---:|---:|
| PhysioNetMI | 1490 | 1459 |
| BNCI2014_001 | 720 | 720 |
| Lee2019_MI | 1600 | 1600 |

P01 low-label budgets are equal-per-class by construction. The amendment therefore freezes `NEVER_WEIGHT_P02_CURRENT_FROZEN_INPUTS` with explicit weights `[1.0, 1.0]` for these exact input identities. This is a **phase-specific frozen decision**, not a universal definition of “balanced.” If the governed input identity or counts change, Stage 05 fails closed and a Protocol successor must decide the new policy; code is prohibited from auto-selecting a threshold or formula.

## 4. Why this is the minimal harmonizing repair

The amendment:

- changes no P00/P01 execution or authority;
- leaves primary EEGNet unaugmented;
- leaves the official A0 count at 678;
- leaves the official A4 count at 1,218;
- leaves the official A0+A4 total at 1,896;
- adds exactly 15 separately identified diagnostic training-policy challenger cells (3 datasets x 5 already-frozen EEGNet model seeds);
- adds no A-number and does not create A14;
- does not permit challenger-specific hyperparameter tuning;
- does not allow challenger evidence to enter A4 representative selection or become the P03 primary prediction substrate;
- preserves all normal failure, negative-result, provenance, figure/table, Protocol, Analysis, Layer-0, Evidence-Map, Layer-10, and P03 handoffs.

## 5. External sources

1. Braindecode documentation — `braindecode.augmentation.SegmentationReconstruction`: https://braindecode.org/stable/generated/braindecode.augmentation.SegmentationReconstruction.html
2. Braindecode tutorial — *Searching the best data augmentation on BCIC IV 2a Dataset*: https://braindecode.org/stable/auto_examples/advanced_training/plot_data_augmentation_search.html
3. Lotte, F. (2015). *Signal processing approaches to minimize or suppress calibration time in oscillatory activity-based brain-computer interfaces*. Proceedings of the IEEE, 103(6), 871–890. DOI: 10.1109/JPROC.2015.2404941
4. Rommel, C., Paillard, J., Moreau, T., & Gramfort, A. *Data augmentation for learning predictive models on EEG: a systematic comparison*. arXiv:2206.14483 / later journal publication.
5. scikit-learn documentation — `sklearn.utils.class_weight.compute_class_weight`: https://scikit-learn.org/stable/modules/generated/sklearn.utils.class_weight.compute_class_weight.html
6. PyTorch documentation — `torch.nn.CrossEntropyLoss`: https://docs.pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html

## 6. Future documentary synchronization

When the P02 execution bundle is accepted, copy the exact frozen values and identities from `P02_PREEXECUTION_TRAINING_POLICY_AMENDMENT_R1.yaml` into the single cumulative Protocol v1.0 P02 section and the P02 Build Book successor. This external evidence note should remain supporting rationale; it must not be used to reselect values after observing P02 results.
