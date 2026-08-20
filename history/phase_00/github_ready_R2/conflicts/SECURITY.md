# Security policy

## Reporting

Report suspected secret exposure, credential leakage, unsafe archive extraction, path traversal, dependency compromise, provenance corruption, manifest tampering, or unauthorized evidence mutation privately to the project owner. Do not open a public issue containing sensitive data.

## Repository expectations

- never commit credentials, tokens, private participant data, or machine-specific secrets;
- reject absolute paths, traversal, symlinks/devices in release archives, and unverified recursive archives;
- keep hashes, manifests, and source identities synchronized;
- fail closed when integrity or provenance cannot be established;
- preserve claim and evidence boundaries during incident repair.

The local publication validator performs secret-pattern, unsafe-path, transient-file, and manifest checks; these checks supplement but do not replace human security review.
