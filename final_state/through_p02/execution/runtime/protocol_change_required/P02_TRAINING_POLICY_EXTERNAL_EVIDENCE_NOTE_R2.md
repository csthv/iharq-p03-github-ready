# P02 Training-Policy External Evidence Note R2

This note supports but does not supersede IHARQ authority.

## Segmentation/Reconstruction
- Braindecode `SegmentationReconstruction(probability, n_segments=None, random_state=None)` implements label-aware temporal segment reconstruction; with `n_segments=None`, the library automatically resolves segment count.
- Braindecode's official augmentation-search tutorial states that the best EEG augmentation is task-dependent, keeps an explicit identity baseline, and evaluates augmentation strengths by validation/CV. The tutorial uses application probability 0.5 as a conventional transform probability for several searched augmentations.
- IHARQ therefore freezes a compact validation-only S&R probability grid `[0.25, 0.50, 0.75]` centered on the conventional 0.5, while delegating segment count to the pinned library's documented auto-resolution. This is a project-specific bounded selection rule, not a claim of universal optimality.

## Class weighting
- scikit-learn defines `class_weight="balanced"` as `n_samples / (n_classes * np.bincount(y))` from the supplied labels; `None` is uniform.
- PyTorch `CrossEntropyLoss(weight=...)` supports a 1-D per-class weight vector and identifies this as useful with unbalanced training data.
- IHARQ avoids an arbitrary imbalance-ratio threshold: equal train counts use uniform loss; unequal counts trigger a validation-only comparison of uniform vs the standard balanced vector. Test evidence is excluded from the decision.

## Sources (checked 2026-08-09)
- Braindecode SegmentationReconstruction API: https://braindecode.org/stable/generated/braindecode.augmentation.SegmentationReconstruction.html
- Braindecode augmentation search tutorial: https://braindecode.org/stable/auto_examples/advanced_training/plot_data_augmentation_search.html
- scikit-learn compute_class_weight: https://scikit-learn.org/stable/modules/generated/sklearn.utils.class_weight.compute_class_weight.html
- PyTorch CrossEntropyLoss: https://docs.pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html
