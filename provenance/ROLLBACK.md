# Rollback

The manual publication guide preserves the pre-replacement state with a backup branch and annotated tag before the replacement branch is created.

To roll back after a merged replacement:

1. identify the merge or squash commit;
2. create a new rollback branch from current `main`;
3. revert the replacement commit with `git revert` (preferred when practical), or restore the tree from the recorded backup branch/tag in a new commit;
4. open and review a rollback pull request;
5. do not force-push `main`;
6. preserve any incorrect release as evidence, mark it superseded, and issue a corrected release with new hashes.

The replacement guide records the exact package hashes needed to identify each state.
