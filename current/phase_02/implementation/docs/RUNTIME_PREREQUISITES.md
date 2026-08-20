# Runtime prerequisites — R5 HF-enabled package

- Kaggle notebook/kernel capable of the frozen Python/package environment.
- Exact dependencies from `requirements-kaggle.txt`; Stage 01 fails closed if the frozen package set cannot be satisfied.
- Required P01 core and A4 inputs attached read-only.
- Cumulative P00+P01 repository ZIP attached under its canonical filename/hash.
- Internet enabled for governed Hugging Face retrieval and lawful exact dependency installation.
- GPU/VRAM, RAM and disk are measured by the existing resource gates; no scientific branch is manually removed to fit the runtime.
- Preferred Hugging Face authentication for unattended runs: Kaggle Secret `HF_TOKEN`; hidden interactive `getpass()` is the fallback.
- The HF token remains memory-only and is cleared after Stage 03. No persistent `huggingface_hub.login()` flow is used by IHARQ.
- The R5 HF cache lives under `/kaggle/working/_iharq_hf_runtime` and is excluded from the final scientific execution bundle; the bundle records only governed repository/revision/hash/status evidence.
- Existing verified pre-attached conditional assets remain a supported offline fallback.
- One full notebook execution lineage. There is no fast/core/ablation/alternative scientific mode.
- Session expiry is anticipated: completed stages, run-cell terminals, predictions, checkpoints, metrics and manifest fragments are persisted with identity/hash bindings and reused only when fingerprints still match.
