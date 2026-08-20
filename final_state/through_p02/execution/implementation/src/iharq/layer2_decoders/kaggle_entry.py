from __future__ import annotations
from pathlib import Path
import yaml
from .orchestration import Context,HANDLERS,init,finalize
from .stage_runner import StageRunner
def load_plan(root):return yaml.safe_load((Path(root)/'machine_readable/p02_notebook_stage_plan_R4.yaml').read_text())['stages']
class NotebookSession:
 def __init__(self,package_root,work_root,revision,fixture=False,reuse=True):self.package_root=Path(package_root);self.work_root=Path(work_root);self.plan=load_plan(package_root);self.ctx=Context(package_root,work_root,fixture);init(self.ctx);self.runner=StageRunner(work_root,self.plan,revision,2 if fixture else 60);self.reuse=reuse;self.results=[];self.finalization=None
 def set_hf_token(self,token,source='INTERACTIVE_OR_SECRET'):
  # In-memory only: never copy token into stage inputs/artifacts/config/bundles.
  self.ctx.state['_hf_token']=token or None;self.ctx.state['_hf_token_source']=source if token else 'NONE';return {'available':bool(token),'source':self.ctx.state['_hf_token_source'],'value':'REDACTED' if token else 'NOT_SET'}
 def clear_hf_token(self):
  self.ctx.state['_hf_token']=None;self.ctx.state['_hf_token_source']='CLEARED';return {'available':False,'source':'CLEARED'}
 def run(self,s):
  sid=str(s);r=self.runner.run(sid,lambda:HANDLERS[sid](self.ctx),self.reuse);self.results.append(r)
  if sid=='24':self.finalization=finalize(self.ctx,self.runner.ledger)
  return r
 def run_all(self):
  try:
   for x in self.plan:self.run(str(x['stage']))
   return {'status':'PASS','stages':self.results,'finalization':self.finalization}
  except Exception as e:
   failure={'exception':type(e).__name__,'message':str(e)[:500],'completed_stage_count':len(self.results),'next_or_failed_stage':str(self.plan[len(self.results)]['stage']) if len(self.results)<len(self.plan) else None}
   try:self.finalization=finalize(self.ctx,self.runner.ledger,partial=True,failure=failure)
   except Exception as pe:self.finalization={'status':'PARTIAL_BUNDLE_FAILED','failure':failure,'bundle_error':f'{type(pe).__name__}:{str(pe)[:300]}'}
   return {'status':'BLOCKED','stages':self.results,'failure':failure,'finalization':self.finalization}

def authoring_fixture_simulation(package_root,work_root):
 rev={'notebook_revision':'R4','source_sha256':'AUTHORING_FIXTURE_SOURCE','config_sha256':'AUTHORING_FIXTURE_CONFIG','stage_plan_sha256':'AUTHORING_FIXTURE_STAGE_PLAN','scientific_freeze_id':'P02-PLANNED-SCIENTIFIC-EXECUTION-FREEZE-R5'};return NotebookSession(package_root,work_root,rev,True,False).run_all()
def production_session(package_root,work_root,revision):return NotebookSession(package_root,work_root,revision,False,True)
