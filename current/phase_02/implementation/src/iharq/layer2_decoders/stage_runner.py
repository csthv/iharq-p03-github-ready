from __future__ import annotations
from pathlib import Path
import json,time,uuid,threading,traceback
from .writers import atomic_json
from .identity import semantic_hash
from .resources import snapshot

class StageRunner:
 def __init__(self,root,plan,revision,heartbeat=60):
  self.root=Path(root);self.root.mkdir(parents=True,exist_ok=True);self.logs=self.root/'logs';self.logs.mkdir(exist_ok=True);self.ledger=self.root/'stage_ledger';self.ledger.mkdir(exist_ok=True);self.gates=self.root/'gate_results';self.gates.mkdir(exist_ok=True);self.plan={str(x['stage']):x for x in plan};self.rev=revision;self.hb=heartbeat
 def path(self,s):return self.ledger/f'stage_{s}.json'
 def accepted(self,s):
  p=self.path(s)
  if not p.exists():return None
  d=json.loads(p.read_text());return d if d.get('status')=='SUCCESS' and d.get('revision_fingerprint')==self.rev else None
 def deps(self,s):
  row=self.plan[str(s)]
  if 'dependencies' in row:return [str(x) for x in row['dependencies']]
  order=list(self.plan);i=order.index(str(s));return [] if i==0 else [order[i-1]]
 def run(self,s,fn,reuse=True):
  s=str(s)
  for d in self.deps(s):
   if not self.accepted(d):raise RuntimeError(f'DEPENDENCY_NOT_ACCEPTED:{s}:{d}')
  if reuse and self.accepted(s):return self.accepted(s)
  att=uuid.uuid4().hex[:12];lp=self.logs/f'stage_{s}_{att}.log';t=time.time();stop=threading.Event();hbpath=self.root/'heartbeats'/f'stage_{s}.json';hbpath.parent.mkdir(exist_ok=True);hb_errors=[]
  def beat():
   while not stop.is_set():
    try:atomic_json(hbpath,{'stage_id':s,'attempt_id':att,'elapsed':time.time()-t,'resource':snapshot(self.root),'revision':self.rev,'heartbeat_status':'PASS'})
    except (OSError,ValueError,TypeError) as e:
     hb_errors.append({'exception':type(e).__name__,'message':str(e)[:240],'elapsed':time.time()-t})
     # Heartbeat failure is fail-soft for science but never silent; it is persisted in the final stage result and log.
    stop.wait(max(1,self.hb))
  th=threading.Thread(target=beat,daemon=True);th.start();status='FAILED';out={};block=[];obs=[]
  with lp.open('w') as log:
   try:out=fn();status='SUCCESS'
   except Exception as e:block=[f'{type(e).__name__}:{str(e)[:500]}'];obs=[traceback.format_exc(limit=12)];log.write(obs[0])
   finally:
    stop.set();th.join(timeout=3)
    if hb_errors:log.write('\nHEARTBEAT_WRITE_ERRORS='+json.dumps(hb_errors,sort_keys=True)+'\n')
  result={'stage_id':s,'status':status,'attempt_id':att,'inputs':{},'input_hashes':{},'outputs':out,'output_hashes':{k:semantic_hash(v) for k,v in out.items()},'dependencies':self.deps(s),'elapsed_seconds':time.time()-t,'log_path':str(lp.relative_to(self.root)),'heartbeat_write_errors':hb_errors,'observability_status':'DEGRADED_HEARTBEAT' if hb_errors else 'PASS','blockers':block,'observations':obs,'revision_fingerprint':self.rev};atomic_json(self.path(s),result);gate=str(self.plan[s].get('gate','G'+s));atomic_json(self.gates/f'{gate}.json',{'gate_id':gate,'stage_id':s,'status':'PASS' if status=='SUCCESS' else 'FAIL','evidence':str(self.path(s).relative_to(self.root)),'blockers':block,'observability_status':result['observability_status']})
  if status!='SUCCESS':raise RuntimeError(f'STAGE_FAILED:{s}:{block}')
  return result
