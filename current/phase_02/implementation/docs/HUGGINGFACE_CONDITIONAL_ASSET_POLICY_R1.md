# P02 Hugging Face conditional-asset policy R1

This is an operational retrieval policy, not a new scientific ablation. Conditional HF assets are resolved before Stage 12 and never allowed to bypass license, corpus-overlap, input-compatibility, resource, or checkpoint-integrity gates.

## Authentication

- Preferred unattended Kaggle path: a private Kaggle Secret named `HF_TOKEN`.
- Interactive fallback: the notebook uses a hidden `getpass()` prompt immediately before Stage 03.
- A blank token is allowed when only public eligible assets are needed.
- The token is passed directly to Hugging Face download calls in memory. `login()` is not used, so the notebook does not intentionally persist credentials to Hugging Face config files.
- Evidence may record only credential availability and source type (for example `KAGGLE_SECRET:HF_TOKEN`); token values are prohibited from logs, configs, stage artifacts, manifests and the execution bundle.
- The notebook clears the in-memory token immediately after Stage 03 completes.

## Current P02 branches

### CBraMod

Automatically retrieved from the immutable Braindecode Hugging Face checkpoint repository at the frozen commit in `configs/phase_02/models/huggingface_assets.yaml`. The downloaded checkpoint hash is independently verified before admission. The maintained Braindecode implementation is used through the built-in IHARQ adapter.

### REVE

Hugging Face gated-access support exists, but current P02 does **not** download/admit REVE because the released REVE pretraining corpus overlaps current P02 benchmark sources (PhysioNet/Schalk and Lee2019/OpenBMI). Authentication never overrides that scientific gate. The branch remains diagnostic and visibly blocked.

## Offline fallback

The existing `IHARQ_P02_CONDITIONAL_MODEL_ASSETS.json` pre-attached mechanism remains supported. A verified pre-attached asset is considered before HF retrieval.
