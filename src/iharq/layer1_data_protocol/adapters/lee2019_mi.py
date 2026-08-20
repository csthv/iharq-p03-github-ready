from __future__ import annotations
from .moabb_base import MOABBAdapterBase
class MOABBLee2019MIAdapter(MOABBAdapterBase):
    dataset_class_name="Lee2019_MI"
    def _dataset_kwargs(self): return {"train_run":True,"test_run":False,"resting_state":False,"sessions":[1,2],"subjects":self._subjects()}
    def _label_for_annotation(self,label:str,run_id:str)->str:
        aliases={"left":"left_hand","right":"right_hand"}; s=str(label).strip(); return aliases.get(s,s)
