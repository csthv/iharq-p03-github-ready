# Roadmap

## Immediate publication transaction

1. Verify the delivered main-tree ZIP and release-assets ZIP.
2. Preserve the current GitHub `main` state with a backup branch and annotated tag.
3. Replace the tracked tree through a reviewable branch and pull request; do not force-push `main`.
4. Verify the merged remote tree against the publication manifest.
5. Upload the release-assets package, download it again, and verify the detached SHA-256.
6. Run the separate read-only live GitHub audit.
7. Only after verified publication may P0-GATE-18, Phase 0 closure, and Phase 1 authorization be adjudicated.

## Phase 1 entry conditions

- freeze the P01 Protocol Annex;
- resolve dataset revision, checksum, provenance, and license;
- resolve environment and resource budgets;
- validate split, leakage, and chronology controls;
- reuse the Phase 0 schemas, configurations, contracts, and identity rules;
- keep empirical claims within the future Protocol and Layer 0 ceilings.

No unsupported completion date is promised.
