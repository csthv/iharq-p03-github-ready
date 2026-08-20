def validation_only_fixed_neural_fit(c,core,freeze,fixture=False,implementation_bindings=None,runtime_overrides=None,data_contract=None,implementation_parameters=None):
    """Fit one fixed neural policy candidate and return validation evidence only. Never reads the test role."""
    ds=c['dataset_id'];b=c['branch_slot'];budget=c['budget_id'];seed=int(c['seed_id']);tr=train_rows(core,ds,budget,freeze);va=core.rows(dataset_id=ds,role='validation')
    X,y,_=core.load_rows(tr);Xv,yv,_=core.load_rows(va);bindings=dict((implementation_bindings or {}).get(b,{}) or {});ov=dict(runtime_overrides or {});params=dict(ov.get('fixed_params') or {})
    if not b.startswith(('DNN-','SSL-')):raise ValueError('VALIDATION_ONLY_NEURAL_REQUIRED')
    pp={**bindings,**params,**ov,**({'fixture_non_scientific_adapter':True} if fixture and b=='DNN-EEGNET' else {})};m=make_adapter(b,seed,X.shape[-1],X.shape[1],pp)
    if hasattr(m,'admission'):
        adm=m.admission()
        if adm['status']!='ADMITTED':return {'status':adm['status'],'reason':adm.get('reason'),'validation_only':True,'test_rows_loaded':False}
    try:
        import torch
        device='cuda' if torch.cuda.is_available() else 'cpu';t0=time.perf_counter()
        m.fit(X,np.asarray(y,int),epochs=int(freeze['neural_training']['max_epochs']),lr=float(params.get('lr',1e-3)),weight_decay=float(params.get('weight_decay',0)),batch_size=int(ov.get('batch_size',16 if fixture else 64)),effective_batch_target=int(freeze['neural_training']['effective_batch_target']),device=device,X_val=Xv,y_val=yv,patience=int(freeze['neural_training']['patience']),min_delta=float(freeze['neural_training']['min_delta']),restore_best=True,class_weights=ov.get('class_weights'),augmentation_policy=ov.get('augmentation_policy'),augmentation_context=ov.get('augmentation_context'))
        pv=m.predict(Xv);sv=m.scores(Xv);vm=evaluate(yv,pv,sv,getattr(m,'score_type',None))
        return {'status':'SUCCESS','validation_metrics':vm,'validation_burden_seconds':float(time.perf_counter()-t0),'model_storage_bytes':int(_model_storage_bytes(m)),'augmentation_provenance':getattr(m,'augmentation_provenance',None),'validation_only':True,'test_rows_loaded':False}
    except Exception as e:
        return {'status':_classify_exception(e),'exception':type(e).__name__,'message':str(e)[:300],'validation_only':True,'test_rows_loaded':False}
