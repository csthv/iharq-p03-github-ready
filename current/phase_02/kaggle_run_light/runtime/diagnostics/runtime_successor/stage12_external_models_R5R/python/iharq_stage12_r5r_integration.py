

class PromotedExternalAdapter:
    def __init__(self, branch, plugin, admission_record):
        self.branch = str(branch)
        self.plugin = plugin
        self._admission_record = dict(admission_record)
        self.resolved_variant = getattr(plugin, "resolved_variant", self.branch)
        self.score_type = getattr(plugin, "score_type", "SOFTMAX_PROBABILITY")
        self.supports_class_weights = bool(getattr(plugin, "supports_class_weights", False))
        self.augmentation_provenance = getattr(plugin, "augmentation_provenance", None)

    @property
    def model(self):
        return getattr(self.plugin, "model", None)

    def admission(self):
        out = dict(self._admission_record)
        out["resolved_variant"] = self.resolved_variant
        return out

    def fit(self, X, y, **kw):
        self.plugin.fit(X, y, **kw)
        self.resolved_variant = getattr(self.plugin, "resolved_variant", self.resolved_variant)
        return self

    def predict(self, X, **kw):
        return self.plugin.predict(X, **kw)

    def scores(self, X, **kw):
        return self.plugin.predict_scores(X, **kw)

    def __getattr__(self, name):
        if name == "plugin":
            raise AttributeError(name)
        return getattr(self.plugin, name)
