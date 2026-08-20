# IHARQ P02/L2 Kaggle Pre-Execution Certification R4 — Dynamic Training-Policy Resolution

## Terminal decision

> **P02_KAGGLE_PREEXECUTION_AUDIT: PASS — BOTH TRAINING-POLICY BLOCKERS RESOLVED BY PREDECLARED TRAIN/VALIDATION-ONLY ALGORITHMS; TECHNICAL IMPLEMENTATION COMPLETE; ZERO FREEZE-CRITICAL BLOCKERS; READY FOR GOVERNED KAGGLE EXECUTION.**

P02 scientific execution is **NOT STARTED** and no P02 scientific result is contained in this package.

### Resolved blocker logic

- **S&R challenger:** primary EEGNet stays unaugmented. Per dataset, `{0.25,0.50,0.75}` S&R probability candidates are evaluated with all five frozen EEGNet seeds on the legal validation role only; median BACC → median macro-F1 → proximity to 0.5 → lower probability selects the final probability before test. Braindecode `n_segments=None` resolves segment count and the realized value is recorded. Final evidence remains exactly 15 diagnostic dataset×seed cells outside A0/A4.
- **Class weighting:** equal fit-role counts use uniform training. Unequal counts compute the standard `n/(K*n_c)` balanced vector from fit labels only. Uniform vs weighted uses the same selected hyperparameters/seed and legal validation BACC → macro-F1 → uniform tie-break. Only native/verified supported classifiers/losses participate; no unsupported algorithm is rewritten.

### Non-regression

A0 `678/678`; A4 `1218/1218`; official A0+A4 `1896`; A14 absent/prohibited; eight Layer-2 modules/53 capabilities preserved; P00/P01 unchanged; downstream Protocol/Phase-Analysis/Layer0/EvidenceMap/Layer10/P03 artifacts preserved.

### Future documentary action

After the accepted P02 run, synchronize `P02_PREEXECUTION_TRAINING_POLICY_AMENDMENT_R2.yaml` and `P02_FUTURE_PROTOCOL_BUILD_BOOK_SYNC_NOTE_R2.md` into the cumulative Protocol/Build-Book successor. Record realized execution bindings; do **not** retune the policy from test results.

## Final authoring validation counts

- production/runtime stage handlers: **26 / 26**
- official A0 cells: **678 / 678**
- official A4 slots: **1,218 / 1,218**
- official A0+A4 cells: **1,896**
- separate diagnostic S&R final cells: **15**
- regression/golden/negative tests: **74 / 74 PASS**
- strengthened static audit: **78 / 78 PASS**
- real-dispatch fixture: **26 / 26 stages PASS**
- fixture runtime checksums: **311 / 311 PASS**
- upstream cumulative verifier: **40 / 40 PASS**
- P01 verifier: **24 / 24 PASS**
- other same-class freeze-critical policy gaps: **0**
- freeze-critical blockers: **0**

The realized S&R probability, auto-resolved segment count, and per-run class-weight decisions are execution outputs of the predeclared train/validation-only policy. They are not values to be manually entered in Kaggle.

