from __future__ import annotations
import numpy as np
from sklearn.metrics import balanced_accuracy_score,f1_score,accuracy_score,roc_auc_score,confusion_matrix

def _valid_score_matrix(scores,n):
    a=np.asarray(scores,float)
    if a.ndim!=2 or a.shape!=(n,2): raise ValueError(f'INVALID_SCORE_SHAPE:{a.shape}:expected={(n,2)}')
    if not np.all(np.isfinite(a)): raise ValueError('NONFINITE_SCORE_VALUES')
    return a

def evaluate(y,p,scores=None,score_type=None):
    y=np.asarray(y,int); p=np.asarray(p,int)
    if y.shape!=p.shape: raise ValueError('Y_PRED_SHAPE_MISMATCH')
    if not set(np.unique(y)).issubset({0,1}) or not set(np.unique(p)).issubset({0,1}): raise ValueError('BINARY_CLASS_CONVENTION_VIOLATION')
    out={'BACC':float(balanced_accuracy_score(y,p)),'F1_MACRO':float(f1_score(y,p,average='macro',zero_division=0)),'ACC':float(accuracy_score(y,p)),'CONFUSION':confusion_matrix(y,p,labels=[0,1]).tolist(),'CLASS_SUPPORT':[int((y==0).sum()),int((y==1).sum())],'PRED_COMPLETE':int(len(p))}
    if scores is None:
        out.update(ROC_AUC=None,ROC_AUC_STATUS='NOT_AVAILABLE_NO_CONTINUOUS_SCORE'); return out
    a=_valid_score_matrix(scores,len(y))
    if len(np.unique(y))<2:
        out.update(ROC_AUC=None,ROC_AUC_STATUS='NOT_APPLICABLE_SINGLE_CLASS'); return out
    # ROC-AUC is a ranking metric. It may use a governed continuous right-hand score even when it is not a calibrated probability.
    out.update(ROC_AUC=float(roc_auc_score(y,a[:,1])),ROC_AUC_STATUS='PASS',ROC_AUC_SCORE_TYPE=score_type or 'UNDECLARED_CONTINUOUS_SCORE')
    return out

def hard_vote(arrs):
    a=np.stack(arrs); n=a.shape[1]; pred=[]; ties=0
    if a.ndim!=2 or a.shape[0]<1: raise ValueError('HARD_VOTE_INPUT_SHAPE')
    for i in range(n):
        c=np.bincount(a[:,i].astype(int),minlength=2)
        if c[0]==c[1]: ties+=1
        pred.append(int(np.argmax(c)))
    return np.array(pred),ties

def probability_average(arrs):
    a=np.stack([np.asarray(x,float) for x in arrs])
    if a.ndim!=3 or a.shape[2]!=2 or not np.all(np.isfinite(a)): raise ValueError('INVALID_PROBABILITY_ENSEMBLE_INPUT')
    if np.any(a<0) or np.any(a>1) or not np.allclose(a.sum(axis=2),1,atol=1e-6): raise ValueError('NON_GOVERNED_PROBABILITY_INPUT')
    out=np.mean(a,axis=0); return out/out.sum(1,keepdims=True)
