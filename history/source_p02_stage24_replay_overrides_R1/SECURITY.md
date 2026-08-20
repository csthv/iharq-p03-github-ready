# Security and data-handling policy

This cumulative repository through P01 contains source code, governed records, manifests, documentary evidence, and pointers to external numerical artifacts. It must not contain live credentials or private session URLs.

- Raw EEG and large derived HDF5 arrays remain external and pointer-governed.
- `KAGGLE_API_TOKEN`, OAuth tokens, passwords, cookies, and session URLs must never be committed.
- The P01 R54 secret-redaction incident remains preserved only as sanitized historical evidence; no secret value is reproduced.
- The repository is non-clinical and does not establish deployment or medical-device safety.
- Report a suspected credential exposure by rotating/revoking the credential first, then documenting the incident without reproducing the secret value.

Historical security files from the P00 and P01 predecessor trees are preserved under `history/`.
