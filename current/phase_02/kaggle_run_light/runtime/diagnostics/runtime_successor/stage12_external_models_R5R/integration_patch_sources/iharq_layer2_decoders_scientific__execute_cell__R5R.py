def execute_cell(c,core,freeze,store,schema_path,config_sha,fixture=False,implementation_bindings=None,runtime_overrides=None,data_contract=None,implementation_parameters=None):
    old=store.terminal(c)
    if old:return old
    ds=c['dataset_id'];b=c['branch_slot'];budget=c['budget_id'];seed=int(c['seed_id']);tr=train_rows(core,ds,budget,freeze);va=core.rows(dataset_id=ds,role='validation');te=core.rows(dataset_id=ds,role='test');X,y,_=core.load_rows(tr);Xv,yv,_=core.load_rows(va);Xt,yt,meta=core.load_rows(te);cands=[];fails=[]
    bindings=dict((implementation_bindings or {}).get(b,{}) or {}); overrides=dict(runtime_overrides or {})
    yfit=np.asarray(y,int)
    permutation_provenance=None
    if b=='SAN-PERM':
        rng=np.random.default_rng(seed);yfit=rng.permutation(yfit)
        permutation_provenance={'performed':True,'scope':'LEGAL_FIT_ROLE_SOURCE_EVENTS_ONLY','permutation_seed':seed,'aux_repeat_index':int(c.get('aux_repeat_index',0)),'label_count':int(len(yfit)),'class_support_before':np.bincount(y,minlength=2).astype(int).tolist(),'class_support_after':np.bincount(yfit,minlength=2).astype(int).tolist(),'validation_labels_permuted':False,'test_labels_permuted':False}
    max_success=int(freeze['candidate_caps']['max_successful_per_family']);family_start=time.monotonic();family_cap_s=float(freeze['candidate_caps']['family_tuning_minutes'])*60.0
    candidate_cap_s=float(freeze['candidate_caps']['neural_candidate_minutes'] if b.startswith(('DNN-','SSL-')) else freeze['candidate_caps']['classical_candidate_minutes'])*60.0
    grid=[dict(overrides['fixed_params'])] if overrides.get('fixed_params') is not None else branch_grid(freeze,b,data_contract,implementation_parameters)[:int(freeze['candidate_caps']['max_attempted_per_family'])]
    for i,p in enumerate(grid):
        if time.monotonic()-family_start>=family_cap_s:
            fails.append({'status':'FAILED_TIMEOUT','reason':'FAMILY_TUNING_HARD_WALL_REACHED','candidate_id':f'CAND-{i:02d}','family_cap_seconds':family_cap_s});break
        if len(cands)>=max_success:break
        try:
            with wallclock_limit(candidate_cap_s,f'{b}:CAND-{i:02d}'):
                pp={**bindings,**p,**overrides,**({'fixture_non_scientific_adapter':True} if fixture and (b.startswith('RIE-') or b=='DNN-EEGNET') else {})}
                m=make_adapter(b,seed,X.shape[-1],X.shape[1],pp)
                if hasattr(m,'admission'):
                    adm=m.admission()
                    if adm['status']!='ADMITTED':
                        fails.append({**adm,'candidate_id':f'CAND-{i:02d}'})
                        continue
                t0=time.perf_counter()
                if b.startswith(('DNN-','SSL-')):
                    import torch
                    device='cuda' if torch.cuda.is_available() else 'cpu'
                    m.fit(X,yfit,epochs=int(freeze['neural_training']['max_epochs']),lr=float(p.get('lr',1e-3)),weight_decay=float(p.get('weight_decay',0)),batch_size=int(overrides.get('batch_size',16 if fixture else 64)),effective_batch_target=int(freeze['neural_training']['effective_batch_target']),device=device,X_val=Xv,y_val=yv,patience=int(freeze['neural_training']['patience']),min_delta=float(freeze['neural_training']['min_delta']),restore_best=True,class_weights=overrides.get('class_weights'),augmentation_policy=overrides.get('augmentation_policy'),augmentation_context=overrides.get('augmentation_context'))
                else:
                    m.fit(X,yfit)
                pv=m.predict(Xv);sv=m.scores(Xv);met=evaluate(yv,pv,sv,getattr(m,'score_type',None));burden=time.perf_counter()-t0;storage=_model_storage_bytes(m);candidate_id=f'CAND-{i:02d}'
                cands.append({'model':m,'params':p,'metric':met,'index':i,'candidate_id':candidate_id,'validation_burden_seconds':float(burden),'model_storage_bytes':int(storage)})
        except Exception as e:
            fails.append({'status':_classify_exception(e),'exception':type(e).__name__,'message':str(e)[:300],'candidate_id':f'CAND-{i:02d}'})
    if not cands:
        priority=['RESOURCE_BLOCKED','INPUT_INCOMPATIBLE','LICENSE_BLOCKED','CHECKPOINT_BLOCKED','DEPENDENCY_BLOCKED','CONDITIONAL_SKIP','FAILED']
        statuses={x.get('status','FAILED') for x in fails};status=next((x for x in priority if x in statuses),'FAILED');store.failure(c,{'terminal_status':status,'candidate_failures':fails,'permutation_provenance':permutation_provenance,'training_condition_id':c.get('condition_id'),'augmentation_provenance':getattr(m,'augmentation_provenance',None)});return store.write_terminal(c,status,candidate_failures=fails,permutation_provenance=permutation_provenance,training_condition_id=c.get('condition_id'),augmentation_provenance=getattr(m,'augmentation_provenance',None))
    selected=sorted(cands,key=lambda q:(-q['metric']['BACC'],-q['metric']['F1_MACRO'],q['validation_burden_seconds'],q['model_storage_bytes'],q['candidate_id']))[0]
    m=selected['model'];p=selected['params'];vm=selected['metric'];class_weight_decision={'selected_policy':overrides.get('class_weight_policy','UNIFORM_NO_WEIGHT'),'selected_weights':overrides.get('class_weights'),'test_set_used':False,'selection_required':False}
    if overrides.get('class_weight_binding') and not overrides.get('fixed_class_weight_policy'):
        try:
            m,vm,class_weight_decision=_resolve_class_weight_policy(b,selected,bindings,overrides,X,yfit,Xv,yv,freeze,fixture,seed,overrides['class_weight_binding'])
        except Exception as e:
            status='INPUT_INCOMPATIBLE' if isinstance(e,TrainingPolicyAuthorityError) else _classify_exception(e)
            store.failure(c,{'terminal_status':status,'reason':'CLASS_WEIGHT_CALIBRATION_FAILED','exception':type(e).__name__,'message':str(e)[:300]})
            return store.write_terminal(c,status,reason='CLASS_WEIGHT_CALIBRATION_FAILED',message=str(e)[:300])
    pred=m.predict(Xt);scores=m.scores(Xt);met=evaluate(yt,pred,scores,getattr(m,'score_type',None));lat_repeats=int((implementation_parameters or {}).get('metrics',{}).get('latency_probe_repeats',5));inference_burden=_batch1_latency(m,Xt,lat_repeats);chk=save_roundtrip(m,Xt[:min(4,len(Xt))],store.root/'checkpoints'/f"{c['planned_run_cell_id']}.pkl")
    if chk['status']!='PASS':return store.write_terminal(c,'INVALID',reason='CHECKPOINT_RELOAD_FAILURE',checkpoint_roundtrip=chk,permutation_provenance=permutation_provenance)
    schemas=load_schemas(schema_path);resolved=getattr(m,'resolved_variant',None) or b;model_id=f'{b}:{resolved}:{c["planned_run_cell_id"]}'
    resource_profile={'fixture':fixture,'resolved_variant':resolved,'batch_size':getattr(m,'actual_batch_size',None),'gradient_accumulation':getattr(m,'gradient_accumulation',None),'validation_burden_seconds':class_weight_decision.get('selected_validation_burden_seconds',selected['validation_burden_seconds']),'model_storage_bytes':class_weight_decision.get('selected_model_storage_bytes',selected['model_storage_bytes']),'candidate_id':selected['candidate_id'],**inference_burden}
    mreg=make_record('ModelRegistryRecord',{'model_id':model_id,'family_role':b,'implementation_id':f'IHARQ_P02_L2_RUNTIME_R2:{resolved}','implementation_revision':'R2','license':'PROJECT_OR_DEPENDENCY_LICENSE','checkpoint_id':chk['checkpoint_sha256'],'checkpoint_sha256':chk['checkpoint_sha256'],'model_seed':seed,'input_profile':'CORE_480','class_order':['left_hand','right_hand'],'score_type':m.score_type,'admission_status':'SUCCESS','resource_profile':resource_profile},schemas['ModelRegistryRecord'],config_sha,[c['planned_run_cell_id']]);store.write_records('ModelRegistryRecord',c,[mreg]);prs=[]
    for j,(r,yp) in enumerate(zip(meta,pred)):
        sv=None if scores is None else np.asarray(scores[j]).tolist();prs.append(make_record('PredictionRecord',_payload_prediction(r,model_id,resolved,chk['checkpoint_sha256'],seed,yp,m.score_type,sv,budget),schemas['PredictionRecord'],config_sha,[c['planned_run_cell_id'],r['window_record_id']]))
    pp=store.write_records('PredictionRecord',c,prs);metric_payload={'run_cell_id':c['planned_run_cell_id'],'dataset_id':ds,'branch_id':b,'resolved_variant':resolved,'budget_id':str(budget),'metrics':met,'validation_selection':vm,'validation_burden_seconds':class_weight_decision.get('selected_validation_burden_seconds',selected['validation_burden_seconds']),'model_storage_bytes':class_weight_decision.get('selected_model_storage_bytes',selected['model_storage_bytes']),'selected_candidate_id':selected['candidate_id'],'selected_params':p,'candidate_failures':fails,'observed_denominator':len(pred),'expected_denominator':len(te),'score_type':m.score_type,'inference_burden':inference_burden,'permutation_provenance':permutation_provenance,'class_weight_policy':class_weight_decision.get('selected_policy'),'class_weights':class_weight_decision.get('selected_weights'),'class_weight_calibration':class_weight_decision}
    mp=store.metric(c,metric_payload)
    return store.write_terminal(c,'SUCCESS',prediction_partition=str(pp.relative_to(store.root)),metric_source=str(mp.relative_to(store.root)),checkpoint_sha256=chk['checkpoint_sha256'],observed_denominator=len(pred),selected_params=p,resolved_variant=resolved,score_type=m.score_type,validation_burden_seconds=class_weight_decision.get('selected_validation_burden_seconds',selected['validation_burden_seconds']),model_storage_bytes=class_weight_decision.get('selected_model_storage_bytes',selected['model_storage_bytes']),selected_candidate_id=selected['candidate_id'],inference_burden=inference_burden,permutation_provenance=permutation_provenance,class_weight_policy=class_weight_decision.get('selected_policy'),class_weights=class_weight_decision.get('selected_weights'),class_weight_calibration=class_weight_decision,training_condition_id=c.get('condition_id'),augmentation_provenance=getattr(m,'augmentation_provenance',None))
