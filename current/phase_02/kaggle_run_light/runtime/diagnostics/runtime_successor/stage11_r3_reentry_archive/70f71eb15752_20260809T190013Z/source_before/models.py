from __future__ import annotations
import importlib
import inspect
import sys,hashlib
from pathlib import Path
import numpy as np

PROBABILITY_SCORE_TYPES={
    'NATIVE_PROBABILITY','SOFTMAX_PROBABILITY','TRAIN_PRIOR_PROBABILITY'
}

class Adapter:
    score_type='HARD_LABEL_ONLY'
    resolved_variant=None
    def fit(self,X,y,**kw): return self
    def predict(self,X,**kw): raise RuntimeError('ABSTRACT_ADAPTER_PREDICT_CALLED')
    def scores(self,X,**kw): return None
    def admission(self): return {'status':'ADMITTED'}

class BlockedAdapter(Adapter):
    def __init__(self,status,reason,branch=None):
        self._status=status; self._reason=reason; self.branch=branch; self.resolved_variant=None
    def admission(self): return {'status':self._status,'reason':self._reason}
    def predict(self,X,**kw): raise RuntimeError(f'{self._status}:{self._reason}')

class Majority(Adapter):
    def fit(self,X,y,**kw): self.c=int(np.bincount(y,minlength=2).argmax()); return self
    def predict(self,X,**kw): return np.full(len(X),self.c)

class Stratified(Adapter):
    score_type='TRAIN_PRIOR_PROBABILITY'
    def __init__(self,seed): self.r=np.random.default_rng(seed)
    def fit(self,X,y,**kw): self.p=np.bincount(y,minlength=2)/len(y); return self
    def predict(self,X,**kw): return self.r.choice([0,1],len(X),p=self.p)
    def scores(self,X,**kw): return np.tile(self.p,(len(X),1))

class Prior(Majority):
    score_type='TRAIN_PRIOR_PROBABILITY'
    def fit(self,X,y,**kw): super().fit(X,y); self.p=np.bincount(y,minlength=2)/len(y); return self
    def scores(self,X,**kw): return np.tile(self.p,(len(X),1))

class LogVar(Adapter):
    score_type='NATIVE_PROBABILITY'
    supports_class_weights=True
    def __init__(self,C=1.0,max_iter=2000): self.C=float(C); self.max_iter=int(max_iter)
    def _z(self,X): return np.log(np.var(X,axis=-1)+1e-8)
    def fit(self,X,y,**kw):
        from sklearn.linear_model import LogisticRegression
        cw=kw.get('class_weights'); class_weight=None if cw is None else {0:float(cw[0]),1:float(cw[1])}
        self.m=LogisticRegression(C=self.C,max_iter=self.max_iter,penalty='l2',class_weight=class_weight).fit(self._z(X),y); return self
    def predict(self,X,**kw): return self.m.predict(self._z(X))
    def scores(self,X,**kw): return self.m.predict_proba(self._z(X))

class CSPLDA(Adapter):
    score_type='NATIVE_PROBABILITY'
    def __init__(self,n=8,reg='oas',solver='lsqr',shrinkage='auto'):
        self.n=int(n); self.reg=reg; self.solver=solver; self.shrinkage=shrinkage
    def fit(self,X,y,**kw):
        from mne.decoding import CSP
        from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
        self.csp=CSP(n_components=min(self.n,X.shape[1]),reg=self.reg,log=True,norm_trace=False)
        z=self.csp.fit_transform(X,y)
        self.m=LinearDiscriminantAnalysis(solver=self.solver,shrinkage=self.shrinkage).fit(z,y)
        return self
    def predict(self,X,**kw): return self.m.predict(self.csp.transform(X))
    def scores(self,X,**kw): return self.m.predict_proba(self.csp.transform(X))

class FBCSP(Adapter):
    score_type='NATIVE_PROBABILITY'
    supports_class_weights=True
    def __init__(self,n=2,C=1,bands=None,fs=None,filter_order=None,reg='oas',max_iter=2000):
        self.n=int(n); self.C=float(C); self.bands=[tuple(x) for x in (bands or [])];
        if fs is None or filter_order is None: raise ValueError('FBCSP_FROZEN_FS_AND_FILTER_ORDER_REQUIRED')
        self.fs=float(fs); self.filter_order=int(filter_order); self.reg=reg; self.max_iter=int(max_iter)
        if not self.bands: raise ValueError('FBCSP_BANDS_REQUIRED_FROM_FROZEN_CONFIG')
    def _features(self,X,fit=False,y=None):
        from scipy.signal import butter,sosfiltfilt
        from mne.decoding import CSP
        out=[]
        if fit: self.csps=[]
        for i,(a,b) in enumerate(self.bands):
            sos=butter(self.filter_order,[a,b],btype='bandpass',fs=self.fs,output='sos')
            z=sosfiltfilt(sos,X,axis=-1)
            c=self.csps[i] if not fit else CSP(n_components=min(self.n,X.shape[1]),reg=self.reg,log=True,norm_trace=False)
            out.append(c.transform(z) if not fit else c.fit_transform(z,y))
            if fit: self.csps.append(c)
        return np.concatenate(out,1)
    def fit(self,X,y,**kw):
        from sklearn.linear_model import LogisticRegression
        cw=kw.get('class_weights'); class_weight=None if cw is None else {0:float(cw[0]),1:float(cw[1])}
        self.m=LogisticRegression(C=self.C,max_iter=self.max_iter,penalty='l2',class_weight=class_weight).fit(self._features(X,True,y),y); return self
    def predict(self,X,**kw): return self.m.predict(self._features(X))
    def scores(self,X,**kw): return self.m.predict_proba(self._features(X))

class Riemann(Adapter):
    @property
    def supports_class_weights(self): return self.kind!='RIE-MDM'
    def __init__(self,kind,C=1,align=False,covariance='oas',tangent_metric='riemann',max_iter=2000):
        self.kind=kind; self.C=float(C); self.align=bool(align); self.covariance=covariance; self.tangent_metric=tangent_metric; self.max_iter=int(max_iter)
        self.score_type='DISTANCE_DERIVED_SIMPLEX' if kind=='RIE-MDM' else 'NATIVE_PROBABILITY'
    @staticmethod
    def _trial_cov(X):
        X=np.asarray(X,float); X=X-X.mean(axis=-1,keepdims=True)
        return np.einsum('nct,ndt->ncd',X,X)/max(1,X.shape[-1]-1)
    @staticmethod
    def _invsqrt(C,eps=1e-10):
        C=(np.asarray(C,float)+np.asarray(C,float).T)/2
        w,v=np.linalg.eigh(C); w=np.maximum(w,eps)
        return (v*(1/np.sqrt(w)))@v.T
    def _fit_alignment(self,X):
        # Train-safe Euclidean Alignment: reference is derived exclusively from the legal fit data.
        R=self._trial_cov(X).mean(axis=0)
        self.ea_reference_covariance_=R
        self.ea_whitener_=self._invsqrt(R)
    def _aligned(self,X):
        X=np.asarray(X,float)
        return np.einsum('cd,ndt->nct',self.ea_whitener_,X) if self.align else X
    def _cov(self,X):
        from pyriemann.estimation import Covariances
        return Covariances(estimator=self.covariance).transform(self._aligned(X))
    def fit(self,X,y,**kw):
        from pyriemann.tangentspace import TangentSpace
        from pyriemann.classification import MDM
        from sklearn.linear_model import LogisticRegression
        if self.align: self._fit_alignment(X)
        C=self._cov(X)
        if self.kind=='RIE-MDM': self.m=MDM(metric=self.tangent_metric).fit(C,y); return self
        self.ts=TangentSpace(metric=self.tangent_metric); z=self.ts.fit_transform(C)
        cw=kw.get('class_weights'); class_weight=None if cw is None else {0:float(cw[0]),1:float(cw[1])}
        self.m=LogisticRegression(C=self.C,max_iter=self.max_iter,penalty='l2',class_weight=class_weight).fit(z,y); return self
    def predict(self,X,**kw):
        z=self._cov(X) if self.kind=='RIE-MDM' else self.ts.transform(self._cov(X))
        return self.m.predict(z)
    def scores(self,X,**kw):
        z=self._cov(X) if self.kind=='RIE-MDM' else self.ts.transform(self._cov(X))
        if self.kind!='RIE-MDM': return self.m.predict_proba(z)
        d=np.asarray(self.m.transform(z),float)
        # Governed diagnostic distance-derived simplex. It is explicitly not a calibrated/native probability.
        d=d-d.min(axis=1,keepdims=True); q=np.exp(-d); den=q.sum(axis=1,keepdims=True)
        return q/np.where(den<=0,1,den)


def _construct(cls,**kwargs):
    """Instantiate maintained models without silently passing unsupported kwargs."""
    sig=inspect.signature(cls)
    if any(p.kind==inspect.Parameter.VAR_KEYWORD for p in sig.parameters.values()): return cls(**kwargs)
    return cls(**{k:v for k,v in kwargs.items() if k in sig.parameters})


class FixtureNeural(Adapter):
    """NON-SCIENTIFIC fixture-only neural surrogate used only to exercise orchestration.

    It accepts the same training-policy interface as the production neural adapter but uses
    a tiny logistic model. make_adapter can return it only when fixture_non_scientific_adapter=True.
    """
    supports_class_weights=True
    score_type='NATIVE_PROBABILITY'
    resolved_variant='FIXTURE_NEURAL_SURROGATE_NOT_P02_EVIDENCE'
    def __init__(self,seed=0,C=1.0): self.seed=int(seed); self.C=float(C); self.actual_batch_size=None; self.gradient_accumulation=1
    def _z(self,X): return np.log(np.var(np.asarray(X,float),axis=-1)+1e-8)
    def fit(self,X,y,**kw):
        from sklearn.linear_model import LogisticRegression
        Xfit=np.asarray(X,float); y=np.asarray(y,int); ap=kw.get('augmentation_policy'); self.augmentation_provenance={'enabled':bool(ap),'fixture':True,'condition_id':None if not ap else ap.get('condition_id')}
        if ap:
            from .training_policy import resolve_segment_count,derive_augmentation_seed,segmentation_reconstruction
            ctx=dict(kw.get('augmentation_context') or {}); rseed=derive_augmentation_seed(ap['seed_namespace'],ctx.get('dataset_id','FIXTURE'),self.seed,int(ctx.get('model_repeat_index',0)),0,ap.get('probability'))
            seg=resolve_segment_count(Xfit,y,policy=ap.get('segment_count_resolution') or {'type':'BRAINCDECODE_PUBLIC_API_AUTO_N_SEGMENTS'},seed=rseed,fixture=True)
            Xfit,prov=segmentation_reconstruction(Xfit,y,probability=float(ap['probability']),n_segments=int(seg['n_segments']),seed=rseed)
            self.augmentation_provenance.update({'probability':float(ap['probability']),'segment_resolution':seg,'donor_segment_count':len(prov['donor_log'])})
        cw=kw.get('class_weights'); class_weight=None if cw is None else {0:float(cw[0]),1:float(cw[1])}
        self.m=LogisticRegression(C=self.C,max_iter=500,class_weight=class_weight,random_state=self.seed).fit(self._z(Xfit),y)
        self.actual_batch_size=int(kw.get('batch_size',16)); return self
    def predict(self,X,**kw): return self.m.predict(self._z(X))
    def scores(self,X,**kw): return self.m.predict_proba(self._z(X))

class BraindecodeAdapter(Adapter):
    supports_class_weights=True
    score_type='SOFTMAX_PROBABILITY'
    def __init__(self,variant,seed,input_samples,n_chans,dropout=.25):
        self.variant=variant; self.branch=variant; self.seed=int(seed); self.input_samples=int(input_samples); self.n_chans=int(n_chans); self.dropout=float(dropout); self.resolved_variant=variant
    def _model_class(self):
        from braindecode import models
        mapping={'EEGNet':'EEGNetv4','EEGConformer':'EEGConformer','EEGTCNet':'EEGTCNet'}
        name=mapping[self.variant]
        if not hasattr(models,name): raise ImportError(f'BRAINCDECODE_MODEL_MISSING:{name}')
        return getattr(models,name)
    def admission(self):
        try: self._model_class()
        except (ImportError,ModuleNotFoundError) as e: return {'status':'DEPENDENCY_BLOCKED','reason':str(e),'resolved_variant':self.variant}
        return {'status':'ADMITTED','resolved_variant':self.variant}
    def _build(self):
        import torch
        cls=self._model_class(); torch.manual_seed(self.seed)
        kw={'n_chans':self.n_chans,'n_outputs':2,'n_times':self.input_samples,'drop_prob':self.dropout,'dropout':self.dropout}
        return _construct(cls,**kw)
    @staticmethod
    def _is_oom(e):
        return isinstance(e,RuntimeError) and ('out of memory' in str(e).lower() or 'cuda error: out of memory' in str(e).lower())
    def fit(self,X,y,epochs=100,lr=1e-3,weight_decay=0,batch_size=64,effective_batch_target=64,device='cpu',X_val=None,y_val=None,patience=12,min_delta=0,restore_best=True,class_weights=None,**kw):
        import torch
        from torch.utils.data import TensorDataset,DataLoader
        if int(batch_size) not in {64,32,16}: raise ValueError('BATCH_SIZE_NOT_IN_FROZEN_LADDER')
        self.model=self._build().to(device); opt=torch.optim.AdamW(self.model.parameters(),lr=lr,weight_decay=weight_decay); cw=None if class_weights is None else torch.tensor(class_weights,dtype=torch.float32,device=device); lossfn=torch.nn.CrossEntropyLoss(weight=cw)
        X_base=np.asarray(X,dtype=np.float32); y_base=np.asarray(y,dtype=np.int64)
        augmentation_policy=kw.get('augmentation_policy')
        augmentation_context=dict(kw.get('augmentation_context') or {})
        resolved_segments=None; segment_resolution=None
        if augmentation_policy:
            from .training_policy import resolve_segment_count,derive_augmentation_seed
            resolver_seed=derive_augmentation_seed(augmentation_policy['seed_namespace'],augmentation_context['dataset_id'],self.seed,augmentation_context['model_repeat_index'],0,augmentation_policy.get('probability'))
            segment_resolution=resolve_segment_count(X_base,y_base,policy=augmentation_policy.get('segment_count_resolution') or {'type':'BRAINCDECODE_PUBLIC_API_AUTO_N_SEGMENTS'},seed=resolver_seed,fixture=bool(augmentation_policy.get('fixture',False)))
            resolved_segments=int(segment_resolution['n_segments'])
        self.augmentation_provenance={'enabled':bool(augmentation_policy),'condition_id':None if not augmentation_policy else augmentation_policy.get('condition_id'),'probability':None if not augmentation_policy else float(augmentation_policy['probability']),'segment_resolution':segment_resolution,'epochs':[]}
        accum=max(1,int(np.ceil(int(effective_batch_target)/int(batch_size)))); best=-np.inf; wait=0; state=None
        try:
            for epoch_index in range(int(epochs)):
                X_epoch=X_base
                aug_summary=None
                if augmentation_policy:
                    from .training_policy import segmentation_reconstruction,derive_augmentation_seed
                    aug_seed=derive_augmentation_seed(augmentation_policy['seed_namespace'],augmentation_context['dataset_id'],self.seed,augmentation_context['model_repeat_index'],epoch_index,augmentation_policy.get('probability'))
                    X_epoch,prov=segmentation_reconstruction(X_base,y_base,probability=float(augmentation_policy['probability']),n_segments=resolved_segments,seed=aug_seed)
                    aug_summary={'epoch_index':int(epoch_index),'seed':int(aug_seed),'probability':float(augmentation_policy['probability']),'n_segments':int(resolved_segments),'augmented_target_count':len({x['target_index'] for x in prov['donor_log']}),'donor_segment_count':len(prov['donor_log'])}
                    self.augmentation_provenance['epochs'].append(aug_summary)
                gen=torch.Generator(); gen.manual_seed(int(self.seed)+int(epoch_index))
                ds=TensorDataset(torch.tensor(X_epoch,dtype=torch.float32),torch.tensor(y_base,dtype=torch.long)); dl=DataLoader(ds,batch_size=int(batch_size),shuffle=True,generator=gen)
                self.model.train(); opt.zero_grad(set_to_none=True); pending=0
                for xb,yb in dl:
                    loss=lossfn(self.model(xb.to(device)),yb.to(device))/accum; loss.backward(); pending+=1
                    if pending%accum==0: opt.step(); opt.zero_grad(set_to_none=True)
                if pending%accum: opt.step(); opt.zero_grad(set_to_none=True)
                if X_val is not None:
                    from sklearn.metrics import balanced_accuracy_score
                    pv=self.predict(X_val,device=device); score=balanced_accuracy_score(y_val,pv)
                    if score>best+float(min_delta): best=float(score); wait=0; state={k:v.detach().cpu().clone() for k,v in self.model.state_dict().items()}
                    else: wait+=1
                    if wait>=int(patience): break
        except RuntimeError as e:
            if self._is_oom(e):
                if torch.cuda.is_available(): torch.cuda.empty_cache()
                raise ResourceWarning(f'CUDA_OOM_AT_FROZEN_BATCH:{batch_size}') from e
            raise
        if restore_best and state is not None: self.model.load_state_dict(state)
        self.device=device; self.actual_batch_size=int(batch_size); self.gradient_accumulation=accum; return self
    def predict(self,X,device=None,**kw): return np.argmax(self.scores(X,device=device),1)
    def scores(self,X,device=None,**kw):
        import torch
        d=device or getattr(self,'device','cpu'); self.model.eval()
        with torch.no_grad(): z=self.model(torch.tensor(X,dtype=torch.float32).to(d)); return torch.softmax(z,1).cpu().numpy()

class External(Adapter):
    score_type='DECLARED_BY_EXTERNAL_IMPLEMENTATION'
    @property
    def supports_class_weights(self): return bool(self.params.get('class_weight_support_verified',False))
    def __init__(self,branch,params): self.branch=branch; self.params=dict(params or {}); self.plugin=None; self.resolved_variant=self.params.get('variant_name',branch)
    @staticmethod
    def _sha(p):
        h=hashlib.sha256()
        with open(p,'rb') as f:
            for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
        return h.hexdigest()
    def admission(self):
        mod=self.params.get('implementation_module'); lic=self.params.get('license_status')
        if not mod: return {'status':'DEPENDENCY_BLOCKED','reason':'IMMUTABLE_IMPLEMENTATION_MODULE_NOT_ATTACHED','resolved_variant':self.resolved_variant}
        py=self.params.get('python_path')
        if py:
            pp=str(Path(py).resolve())
            if pp not in sys.path:sys.path.insert(0,pp)
        try: m=importlib.import_module(mod)
        except (ImportError,ModuleNotFoundError) as e: return {'status':'DEPENDENCY_BLOCKED','reason':type(e).__name__,'resolved_variant':self.resolved_variant}
        except Exception as e: return {'status':'INVALID','reason':f'IMPLEMENTATION_IMPORT_ERROR:{type(e).__name__}:{str(e)[:160]}','resolved_variant':self.resolved_variant}
        if not hasattr(m,'build_iharq_adapter'): return {'status':'DEPENDENCY_BLOCKED','reason':'ENTRYPOINT_MISSING','resolved_variant':self.resolved_variant}
        exp_mod=self.params.get('module_sha256')
        if exp_mod:
            mf=Path(getattr(m,'__file__',''))
            if not mf.is_file() or self._sha(mf)!=exp_mod:return {'status':'CHECKPOINT_BLOCKED','reason':'IMPLEMENTATION_MODULE_HASH_MISMATCH','resolved_variant':self.resolved_variant}
        if lic not in {'CAN_EXECUTE','CAN_STORE','CAN_REDISTRIBUTE','POINTER_ONLY'}: return {'status':'LICENSE_BLOCKED','reason':'LICENSE_STATUS_NOT_EXECUTABLE','resolved_variant':self.resolved_variant}
        chk=self.params.get('checkpoint_path')
        if self.params.get('checkpoint_required',False) and (not chk or not Path(chk).is_file()): return {'status':'CHECKPOINT_BLOCKED','reason':'CHECKPOINT_REQUIRED_OR_MISSING','resolved_variant':self.resolved_variant}
        exp_chk=self.params.get('checkpoint_sha256')
        if chk and exp_chk and self._sha(chk)!=exp_chk:return {'status':'CHECKPOINT_BLOCKED','reason':'CHECKPOINT_HASH_MISMATCH','resolved_variant':self.resolved_variant}
        return {'status':'ADMITTED','resolved_variant':self.resolved_variant}
    def _p(self):
        if self.plugin is None:
            a=self.admission()
            if a['status']!='ADMITTED': raise RuntimeError(a['status']+':'+a.get('reason',''))
            m=importlib.import_module(self.params['implementation_module'])
            self.plugin=m.build_iharq_adapter(branch_id=self.branch,checkpoint_path=self.params.get('checkpoint_path'),config=self.params.get('plugin_config',{}))
            self.score_type=getattr(self.plugin,'score_type',self.score_type); self.resolved_variant=getattr(self.plugin,'resolved_variant',self.resolved_variant)
        return self.plugin
    def fit(self,X,y,**kw): self._p().fit(X,y,**kw); return self
    def predict(self,X,**kw): return np.asarray(self._p().predict(X),int)
    def scores(self,X,**kw): return self._p().predict_scores(X) if hasattr(self._p(),'predict_scores') else None

class FBCNetConditional(External):
    def admission(self):
        eq=str(self.params.get('implementation_equivalence','UNVERIFIED')).upper()
        if eq not in {'ORIGINAL_AUTHOR','VERIFIED_EQUIVALENT'}:
            return {'status':'DEPENDENCY_BLOCKED','reason':'FBCNET_IMPLEMENTATION_EQUIVALENCE_NOT_VERIFIED','resolved_variant':'FBCNet'}
        self.resolved_variant='FBCNet'
        return super().admission()

class SequenceSlot(Adapter):
    score_type='SOFTMAX_PROBABILITY'
    @property
    def supports_class_weights(self):
        try:return bool(getattr(self._resolve(),'supports_class_weights',False))
        except Exception:return False
    def __init__(self,seed,input_samples,n_chans,params):
        self.seed=seed; self.input_samples=input_samples; self.n_chans=n_chans; self.params=dict(params or {}); self.delegate=None; self.resolved_variant=None
    def _resolve(self):
        if self.delegate is not None: return self.delegate
        db=dict(self.params.get('dbconformer',{})); db.setdefault('variant_name','DBConformer')
        ext=External('DNN-SEQ',db); adm=ext.admission()
        if adm['status']=='ADMITTED': self.delegate=ext; self.resolved_variant='DBConformer'; self.score_type=ext.score_type; return ext
        if not self.params.get('allow_eegconformer_fallback',True):
            self.delegate=BlockedAdapter(adm['status'],adm.get('reason','DBCONFORMER_NOT_ADMITTED'),'DNN-SEQ'); return self.delegate
        fb=BraindecodeAdapter('EEGConformer',self.seed,self.input_samples,self.n_chans,self.params.get('dropout',.25)); fadm=fb.admission()
        if fadm['status']!='ADMITTED':
            self.delegate=BlockedAdapter(fadm['status'],f'DBCONFORMER={adm.get("reason")};EEGCONFORMER={fadm.get("reason")}','DNN-SEQ'); return self.delegate
        self.delegate=fb; self.resolved_variant='EEGConformer'; self.score_type=fb.score_type; return fb
    def admission(self):
        d=self._resolve(); a=d.admission(); a=dict(a); a['resolved_variant']=self.resolved_variant or a.get('resolved_variant'); return a
    def fit(self,X,y,**kw): d=self._resolve(); d.fit(X,y,**kw); self.score_type=d.score_type; self.resolved_variant=getattr(d,'resolved_variant',self.resolved_variant); return self
    def predict(self,X,**kw): return self._resolve().predict(X,**kw)
    def scores(self,X,**kw): return self._resolve().scores(X,**kw)


class SSLConditional(External):
    def admission(self):
        a=super().admission()
        if a['status']!='ADMITTED':return a
        required={
            'corpus_overlap_status':'PASS',
            'input_compatibility_status':'PASS',
            'channel_montage_status':'PASS',
            'source_recipe_verified':True,
            'sampling_adapter_verified':True,
            'target_sampling_hz':200,
        }
        bad=[k for k,v in required.items() if self.params.get(k)!=v]
        if bad:return {'status':'INPUT_INCOMPATIBLE','reason':'SSL_QUALIFICATION_GATES_FAILED:'+','.join(bad),'resolved_variant':self.resolved_variant}
        if not self.params.get('checkpoint_sha256'):return {'status':'CHECKPOINT_BLOCKED','reason':'SSL_CHECKPOINT_SHA_REQUIRED','resolved_variant':self.resolved_variant}
        return a


def make_adapter(branch,seed,input_samples,n_chans,params=None):
    p=dict(params or {})
    if p.get('fixture_non_scientific_adapter') and branch.startswith('RIE-'): return LogVar(C=p.get('C',1))
    if p.get('fixture_non_scientific_adapter') and branch=='DNN-EEGNET': return FixtureNeural(seed,p.get('C',1.0))
    if branch=='SAN-MAJ': return Majority()
    if branch=='SAN-STRAT': return Stratified(seed)
    if branch=='SAN-PRIOR': return Prior()
    if branch=='DIAG-LOGVAR': return LogVar(C=p.get('C',1),max_iter=p.get('max_iter',2000))
    if branch in {'SAN-PERM','CLS-CSP-LDA'}: return CSPLDA(p.get('n_components',8),p.get('csp_reg','oas'),p.get('lda_solver','lsqr'),p.get('lda_shrinkage','auto'))
    if branch=='CLS-FBCSP-LR': return FBCSP(p.get('n_components',2),p.get('C',1),bands=p.get('bands_hz'),fs=p.get('fs'),filter_order=p.get('filter_order',4),reg=p.get('csp_reg','oas'),max_iter=p.get('max_iter',2000))
    if branch in {'RIE-TS-LR','RIE-EA-TS','RIE-MDM'}: return Riemann(branch,p.get('C',1),branch=='RIE-EA-TS',p.get('covariance','oas'),p.get('tangent_metric','riemann'),p.get('max_iter',2000))
    if branch=='DNN-EEGNET': return BraindecodeAdapter('EEGNet',seed,input_samples,n_chans,p.get('dropout',.25))
    if branch=='DNN-FBCNET': return FBCNetConditional(branch,p)
    if branch=='DNN-SEQ': return SequenceSlot(seed,input_samples,n_chans,p)
    if branch=='DNN-EGTC':
        if not p.get('fallback_activated',False): return BlockedAdapter('CONDITIONAL_SKIP','EEGTCNET_FALLBACK_NOT_ACTIVATED_PRE_RESULT',branch)
        return BraindecodeAdapter('EEGTCNet',seed,input_samples,n_chans,p.get('dropout',.25))
    if branch in {'SSL-CBRAMOD','SSL-REVE'}: return SSLConditional(branch,p)
    return External(branch,p)
