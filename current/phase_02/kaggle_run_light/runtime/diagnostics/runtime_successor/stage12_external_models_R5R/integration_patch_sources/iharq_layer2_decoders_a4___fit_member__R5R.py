def _fit_member(c,store,core,a4,b,member,schema_path,config_sha,freeze,fixture=False,implementation_bindings=None,runtime_overrides=None):
 ds=c['dataset_id'];budget=c['budget_id'];rep=c['model_repeat_index'];key=f'{ds}__{budget}__{b}__{rep}__{member or "LONG"}';meta=store.root/'diagnostics'/f'A4MEM-{key}.json';rowsf=store.root/'diagnostics'/f'A4MEM-{key}.jsonl'
 if meta.exists() and rowsf.exists():
  old=_j(meta)
  if old.get('config_sha256')==config_sha:return {**old,'rows':_jl(rowsf)}
 tr=_train(a4,core,ds,budget,freeze);va=a4.rows(dataset_id=ds,role='validation');te=a4.rows(dataset_id=ds,role='test');X,y,_=a4.load_rows(tr,member);Xv,yv,_=a4.load_rows(va,member);Xt,yt,rows=a4.load_rows(te,member);p=_params(store,ds,b,budget,rep);pp={**dict((implementation_bindings or {}).get(b,{}) or {}),**p,**dict(runtime_overrides or {}),**({'fixture_non_scientific_adapter':True} if fixture and b.startswith('RIE-') else {})};m=make_adapter(b,int(c['seed_id']),X.shape[-1],X.shape[1],pp)
 if hasattr(m,'admission'):
  a=m.admission()
  if a['status']!='ADMITTED':return {'status':a['status'],'reason':a}
 try:
  if b.startswith(('DNN-','SSL-')):
   import torch
   m.fit(X,y,epochs=1 if fixture else int(freeze['neural_training']['max_epochs']),lr=float(p.get('lr',1e-3)),weight_decay=float(p.get('weight_decay',0.0)),batch_size=int((runtime_overrides or {}).get('batch_size',16 if fixture else freeze['neural_training']['effective_batch_target'])),effective_batch_target=int(freeze['neural_training']['effective_batch_target']),device='cuda' if torch.cuda.is_available() else 'cpu',X_val=Xv,y_val=yv,patience=1 if fixture else int(freeze['neural_training']['patience']),min_delta=float(freeze['neural_training']['min_delta']),restore_best=bool(freeze['neural_training']['restore_best']))
  else:m.fit(X,y)
 except (ImportError,ModuleNotFoundError) as e:return {'status':'DEPENDENCY_BLOCKED','reason':type(e).__name__}
 except ResourceWarning as e:return {'status':'RESOURCE_BLOCKED','reason':str(e)[:200]}
 except Exception as e:return {'status':'FAILED','reason':f'{type(e).__name__}:{str(e)[:200]}'}
 # Measured batch-1 inference burden; this is runtime/resource evidence, not model selection.
 times=[]
 for _ in range(5):
  t0=time.perf_counter();_p=m.predict(Xt[:1]);_s=m.scores(Xt[:1]);times.append(time.perf_counter()-t0)
 pred=m.predict(Xt);scores=m.scores(Xt);chk=save_roundtrip(m,Xt[:4],store.root/'checkpoints'/f'A4MEM-{key}.pkl')
 if chk['status']!='PASS':return {'status':'INVALID','reason':'CHECKPOINT_RELOAD_FAILURE'}
 src=[]
 for i,(r,yp) in enumerate(zip(rows,pred)):src.append({'dataset_id':ds,'event_id':r['event_id'],'window_id':r['window_id'],'window_record_id':r['window_record_id'],'subject_id':r['subject_id'],'session_id':r['session_id'],'split_record_id':r['split_record_id'],'role':r['role'],'y_true':int(yt[i]),'y_pred':int(yp),'score_vector':None if scores is None else np.asarray(scores[i]).tolist(),'score_type':m.score_type})
 atomic_jsonl(rowsf,src);out={'status':'SUCCESS','config_sha256':config_sha,'branch':b,'checkpoint_sha256':chk['checkpoint_sha256'],'model_id':f'{b}:A4:{key}','score_type':m.score_type,'latency_summary':{'batch1_latency_median_s':float(np.median(times)),'batch1_latency_p95_s':float(np.quantile(times,.95)),'repeats':len(times)}};atomic_json(meta,out);return {**out,'rows':src}
