# Security and data-handling policy

This cumulative repository through P02 contains governed source code, schemas, manifests, documentary evidence, lightweight scientific records, and immutable pointers to external heavy artifacts. It must not contain live credentials or private session URLs.

- Never commit literal Hugging Face, Kaggle, OAuth, API, password, cookie, or session credentials.
- P00/P01 external artifact access and P02 external artifact access use distinct symbolic credential classes where governed: `IHARQ_HF_TOKEN_PRE_P02` and `IHARQ_HF_TOKEN_P02`.
- The complete P02 working-space snapshot is referenced by immutable repository/revision/manifest identity; heavy artifacts must be verified by the recorded SHA-256 values after retrieval.
- Historical security incidents remain documentary history only; literal secret values must never be reproduced.
- The repository is public-benchmark/non-clinical and does not establish medical-device or deployment safety.
- Suspected credential exposure requires immediate rotation/revocation followed by a sanitized incident record.
