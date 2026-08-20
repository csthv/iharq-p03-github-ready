# IHARQ P02/L2 Cumulative Pre-Execution Audit R4 — Dynamic Training-Policy Resolution

## Decision
`P02_KAGGLE_PREEXECUTION_AUDIT: PASS`

The two predecessor scientific-freeze blockers remain genuine gaps in the historical Protocol/Build-Book state, but they are now resolved by owner-authorized, research-grounded **predeclared resolution algorithms** that use legal training/validation evidence only. No test result selects S&R probability, segment count, class-weight policy, hyperparameters, checkpoint, or model family.

### Blocker 1
EEGNet primary remains unaugmented. The separate FULL_TRAIN S&R diagnostic uses a compact dataset-level validation grid `[0.25,0.50,0.75]`, all five frozen EEGNet seeds, median BACC → macro-F1 → proximity to 0.5 → lower probability. Braindecode `n_segments=None` resolves segment count. Final diagnostic evidence remains exactly 15 cells outside A0/A4.

### Blocker 2
No arbitrary imbalance threshold is introduced. Equal fit-role counts use uniform training. Unequal counts compute standard balanced weights from fit labels only and compare weighted vs uniform under the same selected hyperparameters/seed on validation BACC → macro-F1 → uniform tie-break. Unsupported algorithms are not retrofitted.

### Non-regression
P00/P01 unchanged; A0=678, A4=1218, official total=1896; A14 absent/prohibited; eight L2 modules and downstream artifacts preserved.
