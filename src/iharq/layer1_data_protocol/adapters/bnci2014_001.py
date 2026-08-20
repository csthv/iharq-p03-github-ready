from __future__ import annotations
from .moabb_base import MOABBAdapterBase
class MOABBBNCI2014001Adapter(MOABBAdapterBase):
    dataset_class_name="BNCI2014_001"
    def _dataset_kwargs(self): return {"subjects":self._subjects(),"sessions":[0,1],"artifact_handling":"ignore"}
    def _label_for_annotation(self,label:str,run_id:str)->str:
        aliases={"left_hand":"769","right_hand":"770","feet":"771","tongue":"772","unknown":"783","rejected":"1023","eye_movements":"1072","start_trial":"768","start_run":"32766","idling_eyes_open":"276","idling_eyes_closed":"277"}
        s=str(label).strip(); return aliases.get(s,s)
