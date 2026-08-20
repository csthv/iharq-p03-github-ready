from __future__ import annotations
import hashlib, math
import numpy as np

class TrainingPolicyAuthorityError(RuntimeError):
    """Raised when an owner-authorized P02 training-policy contract is absent or violated."""

def validate_training_policy_binding(binding:dict)->dict:
    aug=dict(binding.get('augmentation_challenger') or {}); cw=dict(binding.get('class_weighting') or {}); missing=[]
    if aug.get('required_by_build_book'):
        for k in ('branch_id','scope','probability_resolution','segment_count_resolution','seed_namespace','run_cell_condition_identity','donor_pool_identity','run_cell_manifest','run_cell_count'):
            if aug.get(k) in (None,'',[],{}): missing.append('augmentation_challenger.'+k)
        pr=aug.get('probability_resolution') or {}; cand=pr.get('candidates') or []
        if pr.get('type')!='VALIDATION_ONLY_DATASET_LEVEL_GRID_SEARCH' or len(cand)<2 or any(not 0<float(x)<1 for x in cand):missing.append('augmentation_challenger.probability_resolution')
        if pr.get('test_set_access')!='PROHIBITED' or not pr.get('selection_frozen_before_test'):missing.append('augmentation_challenger.probability_no_test')
        sr=aug.get('segment_count_resolution') or {}
        if sr.get('type')!='BRAINCDECODE_PUBLIC_API_AUTO_N_SEGMENTS' or sr.get('requested_n_segments','NOT_NONE') is not None:missing.append('augmentation_challenger.segment_count_resolution')
        if not aug.get('run_cells_frozen') or int(aug.get('run_cell_count',0))!=15:missing.append('augmentation_challenger.final_run_cells')
    if cw.get('policy')!='VALIDATION_SELECTED_UNIFORM_VS_BALANCED_WHEN_TRAIN_COUNTS_UNEQUAL':missing.append('class_weighting.policy')
    trig=cw.get('trigger') or {}; formula=cw.get('balanced_formula') or {}; sel=cw.get('selection') or {}
    if trig.get('type')!='EXACT_TRAIN_COUNT_EQUALITY_THEN_VALIDATION_POLICY_COMPARISON':missing.append('class_weighting.trigger')
    if formula.get('type')!='SKLEARN_COMPUTE_CLASS_WEIGHT_BALANCED':missing.append('class_weighting.formula')
    if sel.get('test_set_access')!='PROHIBITED' or sel.get('tie_break')!='UNIFORM_NO_WEIGHT':missing.append('class_weighting.selection')
    blockers=list(binding.get('freeze_critical_blockers',[]) or [])
    return {'status':'PASS' if not missing and not blockers else 'BLOCKED','missing':missing,'blockers':blockers}

def derive_augmentation_seed(namespace:str,dataset_id:str,model_seed:int,model_repeat_index:int,epoch_index:int,probability_candidate:float|None=None)->int:
    fields=[namespace,dataset_id,int(model_seed),int(model_repeat_index),int(epoch_index)]
    if probability_candidate is not None:fields.append(f'{float(probability_candidate):.8f}')
    v=int(hashlib.sha256('|'.join(map(str,fields)).encode()).hexdigest()[:8],16)%(2**31-1)
    return 1 if v==0 else v

def _documented_auto_segments(n_times:int)->int:
    """Fixture-only fallback matching Braindecode's documented factor/sqrt auto rule."""
    n=int(n_times)
    if n<2:raise TrainingPolicyAuthorityError('SEGREC_TOO_FEW_TIME_SAMPLES')
    factors=[k for k in range(1,int(math.sqrt(n))+1) if n%k==0]
    if not factors:raise TrainingPolicyAuthorityError('SEGREC_AUTO_SEGMENT_FACTOR_NOT_FOUND')
    return int(factors[-1])

def resolve_segment_count(X,y,*,policy:dict,seed:int,fixture:bool=False)->dict:
    X=np.asarray(X); y=np.asarray(y)
    if X.ndim!=3 or len(X)!=len(y):raise TrainingPolicyAuthorityError('SEGREC_RESOLVER_INPUT_INVALID')
    if (policy or {}).get('type')!='BRAINCDECODE_PUBLIC_API_AUTO_N_SEGMENTS':raise TrainingPolicyAuthorityError('SEGREC_RESOLVER_POLICY_INVALID')
    try:
        import torch
        from braindecode.augmentation import SegmentationReconstruction
        # Public API resolves the parameter. Use a small actual-shape, two-class representative batch.
        take=[]
        for cls in sorted(set(y.tolist())):
            take.extend(np.flatnonzero(y==cls)[:min(8,int(np.sum(y==cls)))].tolist())
        if len(take)<2:raise TrainingPolicyAuthorityError('SEGREC_RESOLVER_REQUIRES_TWO_CLASSES')
        xt=torch.as_tensor(X[take],dtype=torch.float32); yt=torch.as_tensor(y[take],dtype=torch.long)
        tr=SegmentationReconstruction(probability=1.0,n_segments=None,random_state=int(seed)); params=tr.get_augmentation_params(xt,yt); n=int(params['n_segments'])
        source='BRAINCDECODE_PUBLIC_API'
    except (ImportError,ModuleNotFoundError) as exc:
        if not fixture:raise TrainingPolicyAuthorityError('SEGREC_BRAINCDECODE_RESOLVER_UNAVAILABLE') from exc
        n=_documented_auto_segments(X.shape[-1]);source='FIXTURE_DOCUMENTED_FALLBACK'
    if n<2 or n>X.shape[-1]:raise TrainingPolicyAuthorityError(f'SEGREC_RESOLVED_SEGMENTS_INVALID:{n}')
    return {'status':'PASS','n_segments':n,'resolver_source':source,'n_times':int(X.shape[-1]),'fixture':bool(fixture)}

def segmentation_reconstruction(X,y,*,probability:float,n_segments:int,seed:int):
    X=np.asarray(X);y=np.asarray(y);probability=float(probability);n_segments=int(n_segments);seed=int(seed)
    if X.ndim!=3 or len(X)!=len(y):raise ValueError('SEGREC_INPUT_SHAPE_INVALID')
    if not 0<=probability<=1:raise ValueError('SEGREC_PROBABILITY_INVALID')
    if n_segments<2 or n_segments>X.shape[-1]:raise ValueError('SEGREC_SEGMENT_COUNT_INVALID')
    rng=np.random.default_rng(seed);out=X.copy();donor_log=[];bounds=np.linspace(0,X.shape[-1],n_segments+1,dtype=int)
    for i in range(len(X)):
        if rng.random()>=probability:continue
        peers=np.flatnonzero(y==y[i]);peers=peers[peers!=i]
        if len(peers)==0:raise TrainingPolicyAuthorityError('SEGREC_INSUFFICIENT_SAME_CLASS_DONORS')
        for q,(a,b) in enumerate(zip(bounds[:-1],bounds[1:])):
            d=int(rng.choice(peers));out[i,:,a:b]=X[d,:,a:b];donor_log.append({'target_index':int(i),'segment_index':int(q),'donor_index':d,'class':int(y[i]),'start':int(a),'stop':int(b)})
    return out,{'status':'PASS','probability':probability,'n_segments':n_segments,'seed':seed,'donor_log':donor_log,'source_unchanged':not np.shares_memory(out,X)}

def balanced_class_weights(y)->tuple[list[float],dict]:
    y=np.asarray(y,int);counts=np.bincount(y,minlength=2).astype(int)
    if np.any(counts<=0):raise TrainingPolicyAuthorityError('CLASS_WEIGHT_MISSING_CLASS')
    from sklearn.utils.class_weight import compute_class_weight
    w=compute_class_weight(class_weight='balanced',classes=np.array([0,1],dtype=int),y=y).astype(float)
    expected=len(y)/(2.0*counts.astype(float))
    if not np.allclose(w,expected,rtol=0,atol=1e-12):raise TrainingPolicyAuthorityError('CLASS_WEIGHT_LIBRARY_FORMULA_MISMATCH')
    return w.tolist(),{'counts':counts.tolist(),'weights':w.tolist(),'formula':'SKLEARN_BALANCED_n_over_Knc'}

def class_weight_policy_candidates(y,binding:dict)->dict:
    y=np.asarray(y,int);counts=np.bincount(y,minlength=2).astype(int)
    if np.any(counts<=0):raise TrainingPolicyAuthorityError('CLASS_WEIGHT_MISSING_CLASS')
    equal=bool(counts[0]==counts[1]);out=[{'policy':'UNIFORM_NO_WEIGHT','weights':None}]
    evidence={'counts':counts.tolist(),'exactly_equal':equal,'selection_required':not equal}
    if not equal:
        w,ev=balanced_class_weights(y);out.append({'policy':'SKLEARN_BALANCED_TRAIN_FOLD','weights':w});evidence.update(ev)
    return {'candidates':out,'evidence':evidence}

def select_validation_policy(results:list[dict],*,primary_metric='BACC',secondary_metric='F1_MACRO',uniform_tie_break=True)->dict:
    good=[r for r in results if r.get('status')=='SUCCESS']
    if not good:raise TrainingPolicyAuthorityError('TRAINING_POLICY_NO_SUCCESSFUL_VALIDATION_CANDIDATE')
    # Exact deterministic ordering; uniform wins only an exact BACC/F1 tie.
    def key(r):
        m=r['validation_metrics']; return (-float(m[primary_metric]),-float(m[secondary_metric]),0 if uniform_tie_break and r.get('policy')=='UNIFORM_NO_WEIGHT' else 1,str(r.get('policy')))
    s=sorted(good,key=key)[0]
    return {'selected_policy':s['policy'],'selected_weights':s.get('weights'),'validation_metrics':s['validation_metrics'],'candidate_results':results,'test_set_used':False}

def select_sr_probability(results:list[dict],binding:dict)->dict:
    pr=binding['augmentation_challenger']['probability_resolution'];minimum=int(pr['minimum_successful_seeds']);summ=[]
    for prob in map(float,pr['candidates']):
        q=[r for r in results if float(r['probability'])==prob and r.get('status')=='SUCCESS']
        if len(q)<minimum:
            summ.append({'probability':prob,'status':'INSUFFICIENT_SUCCESSFUL_SEEDS','successful_seeds':len(q)});continue
        summ.append({'probability':prob,'status':'ELIGIBLE','successful_seeds':len(q),'median_validation_BACC':float(np.median([r['validation_metrics']['BACC'] for r in q])),'median_validation_F1_MACRO':float(np.median([r['validation_metrics']['F1_MACRO'] for r in q]))})
    eligible=[r for r in summ if r['status']=='ELIGIBLE']
    if not eligible:raise TrainingPolicyAuthorityError('SEGREC_PROBABILITY_SELECTION_INSUFFICIENT')
    selected=sorted(eligible,key=lambda r:(-r['median_validation_BACC'],-r['median_validation_F1_MACRO'],abs(r['probability']-float(pr['tie_break_reference_probability'])),r['probability']))[0]
    return {'status':'PASS','selected_probability':selected['probability'],'candidate_summaries':summ,'selection_scope':'VALIDATION_ONLY','test_set_used':False,'tie_break':['BACC','F1_MACRO','PROXIMITY_TO_0P5','LOWER_PROBABILITY']}
