# IHARQ P02/L2 Kaggle Pre-Execution Certification R5 — Hugging Face Conditional Asset Retrieval

> **PASS — READY FOR GOVERNED KAGGLE EXECUTION.**

R5 is an operational successor only. It does not alter the frozen P02 scientific design, A0/A4 cells, training-policy resolution, metrics/statistics, record schemas, claim boundaries, or downstream handoffs. P02 scientific execution remains **NOT STARTED**.

## Hugging Face retrieval

- Separate conditional-checkpoint Kaggle Dataset: **not required for the normal R5 run**.
- Preferred unattended token source: Kaggle Secret `HF_TOKEN`.
- Interactive fallback: hidden `getpass()` immediately before Stage 03.
- Public CBraMod may proceed with no token.
- Token passes directly to governed Hub download calls, is never hard-coded/persisted, and is cleared after Stage 03.
- Pre-attached verified conditional assets remain an offline fallback.
- CBraMod: exact immutable Braindecode Hugging Face revision/checkpoint hash enforced before admission.
- REVE: authentication support exists, but current P02 blocks download/admission at the scientific pretraining-corpus-overlap gate. A token cannot override that gate.

## Non-regression

- A0: **678 / 678**
- A4: **1,218 / 1,218**
- official A0+A4: **1,896**
- runtime stages: **26 / 26**
- tests: **82 / 82 PASS**
- strengthened static audit: **91 / 91 PASS**
- fixture: **26 / 26 stages PASS; 311 / 311 runtime checksums; CRC PASS**
- cumulative P00+P01 verifier: **40 / 40 PASS**
- P01 verifier: **24 / 24 PASS**
- freeze-critical blockers: **0**

Use `docs/KAGGLE_RUN_GUIDE_R5_HF.md`.
