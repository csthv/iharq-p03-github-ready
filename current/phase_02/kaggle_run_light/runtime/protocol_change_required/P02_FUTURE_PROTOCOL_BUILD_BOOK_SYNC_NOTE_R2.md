# P02 Future Protocol / Build-Book Synchronization Note R2

## Purpose
This note is a **required future synchronization action** created before P02 scientific execution. It does not rewrite P00/P01 and does not create scientific results.

## Why the synchronization is required
The existing Method Selection and Nuts-and-Bolts authorities selected the policies but intentionally left two exact P02 training-policy bindings to Protocol v1.0: (1) Segmentation/Reconstruction numeric resolution and (2) the operational class-weight rule. Owner authorization now freezes the **resolution algorithms** below so Kaggle can resolve them lawfully from train/validation evidence instead of inventing constants.

## Protocol v1.0 P02 successor text to incorporate
1. Primary neural references remain **unaugmented**.
2. A separate diagnostic `DNN-EEGNET`, `FULL_TRAIN` S&R challenger remains outside A0/A4 ownership accounting and cannot enter A4 representative selection or replace the primary P03 substrate.
3. S&R segment count is resolved by the pinned Braindecode public API with `n_segments=None`; the resolved value is recorded per execution.
4. S&R application probability is selected **per dataset before any test inference** from the frozen grid `{0.25, 0.50, 0.75}` using all five frozen EEGNet model seeds, median validation BACC, median validation macro-F1, then proximity to 0.5 and lower probability as deterministic tie-breakers. At least three successful calibration seeds are required; otherwise the diagnostic challenger is terminally unresolved/blocked and is preserved as negative evidence without changing A0.
5. The final challenger still comprises exactly 15 dataset×seed test cells; probability-search fits are internal validation/model-selection work and are not new A-numbers or official A0/A4 cells.
6. S&R donors remain same-dataset, same legal training role, same task, same class; validation/test donors are prohibited.
7. For class weighting, exactly equal training counts short-circuit to uniform loss. If training counts are unequal, a standard training-label-derived `balanced` weight vector `n/(K*n_c)` is computed. After ordinary hyperparameter selection, weighted and unweighted fits with the same selected hyperparameters/seed are compared on the legal validation role using BACC → macro-F1 → unweighted tie-break. Only the selected policy may be evaluated on test.
8. The weighting comparison applies only where the already-selected classifier/loss exposes native or explicitly verified class-weight support **without changing algorithm family**. The current native-support set is `DIAG-LOGVAR`, `CLS-FBCSP-LR`, `RIE-TS-LR`, `RIE-EA-TS`, `DNN-EEGNET`, `DNN-EGTC`, and the `DNN-SEQ` slot when it resolves to the EEGConformer fallback. `CLS-CSP-LDA` and `RIE-MDM` remain unweighted because the selected implementations have no native class-weight mechanism. An external/conditional branch participates only when its adapter explicitly verifies class-weight support; a claimed-supported branch that cannot execute fails closed rather than silently reverting. Equal-per-class low-label budgets remain uniform automatically.
9. Test labels/scores may never choose S&R probability, segment count, class weights, hyperparameters, checkpoint, or model family.

## Future document updates
- **Protocol v1.0:** incorporate the algorithmic policy above and, after execution, record realized per-dataset S&R probabilities and per-run class-weight selections as executed bindings—not as retrospectively predeclared constants.
- **Implementation Build Book:** add a narrow successor note that Stage 05 verifies this amendment and Stages 09–12/11 execute its validation-only training-policy selectors; do not change the eight L2 modules, A0/A4 ownership, or 1,896 official full-ablation cells.
- **Nuts-and-Bolts:** resolve the existing `PROTOCOL-v1.0 SYNC REQUIRED` marker by reference to the Protocol successor; do not rewrite prior method selection.
- **Phase Analysis / Layer 0 / Evidence Map / Layer 10:** consume the emitted selection/effect/failure evidence; do not recompute the selection.

## Non-regression
P00/P01, immutable P01 windows, A0=678, A4=1218, A14 prohibition, record schemas, P03 raw-prediction contract, failure evidence, figure/table source requirements and downstream handoffs remain unchanged.
