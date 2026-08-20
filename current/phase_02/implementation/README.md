# IHARQ P02/L2 Kaggle Notebook Implementation Package R5

## Status

This is the Hugging-Face-enabled operational successor of the validated R4 P02 implementation. It does **not** change P02 scientific design, A0/A4 membership, training-policy resolution, metrics/statistics, record schemas, or downstream contracts.

- notebook: `notebook/IHARQ_Phase_02_Complete_Execution_and_Analysis_R4_HF_R1.ipynb`
- notebook ID: `IHARQ-P02-COMPLETE-EXECUTION-AND-ANALYSIS-R4`
- scientific freeze: `P02-PLANNED-SCIENTIFIC-EXECUTION-FREEZE-R5`
- official A0 cells: 678
- official A4 slots: 1,218
- official A0+A4 total: 1,896
- scientific execution at package authoring time: **NOT STARTED**

## R5 operational change

Conditional Hugging Face assets can be resolved automatically at Stage 03.

- Preferred unattended credential source: Kaggle Secret `HF_TOKEN`.
- Interactive fallback: hidden `getpass()` prompt.
- Token is passed directly to Hub download calls, never hard-coded/persisted, and is cleared after Stage 03.
- Existing pre-attached conditional-asset manifest remains an offline fallback.
- CBraMod is retrieved from the immutable governed Braindecode Hugging Face revision and independently hashed.
- REVE retrieval support exists, but current P02 keeps REVE blocked by the pretraining-corpus-overlap scientific gate; authentication cannot override this.

See `docs/KAGGLE_RUN_GUIDE_R5_HF.md` and `docs/HUGGINGFACE_CONDITIONAL_ASSET_POLICY_R1.md`.
