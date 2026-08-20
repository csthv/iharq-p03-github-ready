from __future__ import annotations
import re
from .moabb_base import MOABBAdapterBase

class MOABBPhysionetMIAdapter(MOABBAdapterBase):
    dataset_class_name = "PhysionetMI"
    _MOABB_HAND_KEY_TO_SOURCE_RUN = {"0": 4, "1": 8, "2": 12}

    def _dataset_kwargs(self):
        return {"imagined": True, "executed": False}

    @classmethod
    def _normalized_moabb_key(cls, run_id: str) -> str:
        text = str(run_id).strip()
        nums = re.findall(r"\d+", text)
        return str(int(nums[-1])) if nums else text

    def _include_run(self, run_id: str) -> bool:
        return self._normalized_moabb_key(run_id) in self._MOABB_HAND_KEY_TO_SOURCE_RUN

    def _canonical_run_id(self, run_id: str) -> str:
        key = self._normalized_moabb_key(run_id)
        if key not in self._MOABB_HAND_KEY_TO_SOURCE_RUN:
            raise ValueError(f"MOABB PhysioNet run key is outside the frozen hand-imagery branch: {run_id}")
        return str(self._MOABB_HAND_KEY_TO_SOURCE_RUN[key])

    def _run_metadata(self, run_id: str) -> dict:
        key = self._normalized_moabb_key(run_id)
        return {"moabb_run_key": key, "physionet_source_run": self._MOABB_HAND_KEY_TO_SOURCE_RUN[key]}

    def _label_for_annotation(self, label: str, run_id: str) -> str:
        norm = str(label).strip()
        aliases = {"rest": "T0", "left_hand": "T1", "right_hand": "T2"}
        norm = aliases.get(norm, norm)
        return f"run_4_8_12:{norm}"
