from __future__ import annotations
import numpy as np
from scipy.stats import wilcoxon,friedmanchisquare,norm,rankdata

def paired_bootstrap(diffs,seed,n,level):
    x=np.asarray(diffs,float); x=x[np.isfinite(x)]
    if len(x)<2:return {'status':'DESCRIPTIVE_ONLY','n':len(x),'method':'NONE'}
    rng=np.random.default_rng(seed); ests=np.array([np.median(rng.choice(x,len(x),replace=True)) for _ in range(int(n))]); alpha=(1-level)/2
    theta=float(np.median(x)); prop=float(np.mean(ests<theta)); z0=norm.ppf(np.clip(prop,1e-6,1-1e-6))
    jack=np.array([np.median(np.delete(x,i)) for i in range(len(x))]); jm=float(jack.mean()); ss=float(np.sum((jm-jack)**2)); den=6*(ss**1.5)
    if not np.isfinite(den) or den<=0:
        lo,hi=np.quantile(ests,[alpha,1-alpha]); method='PERCENTILE_FALLBACK_DEGENERATE_ACCELERATION'
    else:
        acc=float(np.sum((jm-jack)**3)/den)
        def adj(a):
            z=norm.ppf(a); denom=1-acc*(z0+z)
            if not np.isfinite(denom) or abs(denom)<1e-12:return np.nan
            return norm.cdf(z0+(z0+z)/denom)
        qs=np.array([adj(alpha),adj(1-alpha)],float)
        if not np.all(np.isfinite(qs)) or np.any(qs<0) or np.any(qs>1) or qs[0]>qs[1]:
            lo,hi=np.quantile(ests,[alpha,1-alpha]); method='PERCENTILE_FALLBACK_UNDEFINED_BCA'
        else:
            lo,hi=np.quantile(ests,qs); method='BCa'
    return {'status':'PASS','n':len(x),'estimate':theta,'low':float(lo),'high':float(hi),'level':float(level),'method':method,'resamples':int(n)}

def wilcoxon_paired(a,b,min_n=5):
    a=np.asarray(a,float); b=np.asarray(b,float); m=np.isfinite(a)&np.isfinite(b); a=a[m];b=b[m];d=a-b
    nz=d!=0
    if np.any(nz):
        ranks=rankdata(np.abs(d[nz]));den=float(ranks.sum());rb=float((ranks[d[nz]>0].sum()-ranks[d[nz]<0].sum())/den) if den else 0.0
    else:rb=0.0
    if len(a)<min_n:return {'status':'DESCRIPTIVE_ONLY','n':len(a),'p_value':None,'statistic':None,'median_difference':float(np.median(d)) if len(d) else None,'rank_biserial':rb}
    try:r=wilcoxon(a,b,alternative='two-sided',zero_method='wilcox')
    except ValueError:return {'status':'DESCRIPTIVE_ONLY','n':len(a),'p_value':1.0,'statistic':0.0,'median_difference':float(np.median(d)) if len(d) else None,'rank_biserial':rb}
    return {'status':'PASS','n':len(a),'p_value':float(r.pvalue),'statistic':float(r.statistic),'median_difference':float(np.median(d)),'rank_biserial':rb}

def holm(pvals):
    items=sorted((k,float(v)) for k,v in pvals.items() if v is not None);m=len(items);out={};prev=0
    for i,(k,p) in enumerate(items):prev=max(prev,(m-i)*p);out[k]=min(prev,1.0)
    return out

def friedman(groups,min_n=5):
    if len(groups)<3:return {'status':'NOT_APPLICABLE','n':min(map(len,groups)) if groups else 0,'kendall_W':None}
    n=min(map(len,groups));k=len(groups)
    if n<min_n:return {'status':'DESCRIPTIVE_ONLY','n':n,'k':k,'kendall_W':None}
    arr=[np.asarray(g,float)[:n] for g in groups]
    if any(not np.all(np.isfinite(x)) for x in arr):raise ValueError('FRIEDMAN_NONFINITE_INPUT')
    r=friedmanchisquare(*arr);w=float(r.statistic/(n*(k-1))) if n>0 and k>1 else None
    return {'status':'PASS','n':n,'k':k,'statistic':float(r.statistic),'p_value':float(r.pvalue),'kendall_W':w}
