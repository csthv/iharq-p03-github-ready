def _fit_weighted_policy_candidate(branch,bindings,params,overrides,X,y,Xv,yv,freeze,fixture,seed):
    pp={**bindings,**params,**overrides,**({'fixture_non_scientific_adapter':True} if fixture and (branch.startswith('RIE-') or branch=='DNN-EEGNET') else {})}
    m=make_adapter(branch,seed,X.shape[-1],X.shape[1],pp)
    if not getattr(m,'supports_class_weights',False):
        raise TrainingPolicyAuthorityError('CLASS_WEIGHT_POLICY_UNSUPPORTED_BY_ADAPTER:'+branch)
    weights=overrides['class_weights']; t0=time.perf_counter()
    if branch.startswith(('DNN-','SSL-')):
        import torch
        device='cuda' if torch.cuda.is_available() else 'cpu'
        m.fit(X,y,epochs=int(freeze['neural_training']['max_epochs']),lr=float(params.get('lr',1e-3)),weight_decay=float(params.get('weight_decay',0)),batch_size=int(overrides.get('batch_size',16 if fixture else 64)),effective_batch_target=int(freeze['neural_training']['effective_batch_target']),device=device,X_val=Xv,y_val=yv,patience=int(freeze['neural_training']['patience']),min_delta=float(freeze['neural_training']['min_delta']),restore_best=True,class_weights=weights,augmentation_policy=overrides.get('augmentation_policy'),augmentation_context=overrides.get('augmentation_context'))
    else:
        m.fit(X,y,class_weights=weights)
    pv=m.predict(Xv);sv=m.scores(Xv);vm=evaluate(yv,pv,sv,getattr(m,'score_type',None))
    return {'status':'SUCCESS','policy':'SKLEARN_BALANCED_TRAIN_FOLD','weights':list(map(float,weights)),'model':m,'validation_metrics':vm,'validation_burden_seconds':float(time.perf_counter()-t0),'model_storage_bytes':int(_model_storage_bytes(m))}
