from pathlib import Path
import pandas as pd, numpy as np
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'figure_source_data'; OUT=ROOT/'figures'; OUT.mkdir(exist_ok=True)

def save(name):
    plt.tight_layout(); plt.savefig(OUT/name,dpi=180); plt.close()
# cumulative phase progression
p=pd.read_csv(SRC/'CUM_FIG_01_Phase_Dependency_source.csv')
fig,ax=plt.subplots(figsize=(10,7.2)); ax.axis('off')
ys=[0.80,0.50,0.20]
for y,(_,r) in zip(ys,p.iterrows()):
    txt=(f"{r['phase']} — {r['scientific_objective']}\n"
         f"Inherited: {'None' if pd.isna(r['inherited_evidence']) else r['inherited_evidence']}\n"
         f"New work: {r['new_work']}\n"
         f"Output: {r['primary_output']} | Findings: {r['finding_range']}\n"
         f"Handoff: {r['downstream_consequence']}")
    ax.text(0.5,y,txt,ha='center',va='center',fontsize=9,wrap=True,
            bbox=dict(boxstyle='round,pad=0.7',facecolor='white',edgecolor='black'))
for y1,y2 in zip(ys[:-1],ys[1:]):
    ax.annotate('',xy=(0.5,y2+0.10),xytext=(0.5,y1-0.10),arrowprops=dict(arrowstyle='->'))
ax.set_title('IHARQ governed phase progression through P02')
save('L10-CUM-FIG-001.png')
# ablation evolution — compact lifecycle table, preserving full source CSV separately
q=pd.read_csv(SRC/'CUM_FIG_02_Ablation_Evolution_source.csv')
def status_code(x):
    x=str(x)
    if 'PROHIBITED' in x or 'REJECTED' in x: return 'PROHIB'
    if 'EXECUTED_RESOURCE' in x or 'STAGE18S_POST_HOC' in x or 'EXPLICIT_LIMITATIONS' in x: return 'EXEC*'
    if 'EXECUTED_COMPLETE' in x: return 'EXEC'
    if 'MATCHED_R2_SUBSTRATE' in x: return 'READY+'
    if 'FOUNDATION_READY' in x: return 'READY'
    if 'NOT_APPLICABLE' in x or 'DOWNSTREAM' in x: return 'DOWN'
    return x[:14]
cell=[]
for _,r in q.iterrows():
    cell.append([r['ablation_id'],status_code(r['P00']),status_code(r['P01']),status_code(r['P02']),status_code(r['current_cumulative_status'])])
fig,ax=plt.subplots(figsize=(9,7.5)); ax.axis('off')
tbl=ax.table(cellText=cell,colLabels=['Ablation','P00','P01','P02','Current'],cellLoc='center',loc='center',bbox=[0.05,0.10,0.90,0.82])
tbl.auto_set_font_size(False); tbl.set_fontsize(8); tbl.scale(1,1.25)
ax.set_title('Ablation evidence evolution through P02')
ax.text(0.5,0.035,'READY = foundation available; READY+ = matched A4 R2 substrate; EXEC = executed complete; EXEC* = executed with explicit limitations; DOWN = downstream/not applicable to P02; PROHIB = rejected/prohibited.',ha='center',va='bottom',fontsize=7,wrap=True)
save('L10-CUM-FIG-002.png')
# evidence role evolution
q=pd.read_csv(SRC/'CUM_FIG_03_Evidence_Role_Evolution_source.csv')
fig,ax=plt.subplots(figsize=(9,5)); ax.axis('off');
for i,(_,r) in enumerate(q.iterrows()): ax.text(0.02,0.92-i*0.12,' | '.join(str(x) for x in r.tolist()),fontsize=9,va='top')
ax.set_title('Evidence role evolution through P02')
save('L10-CUM-FIG-003.png')
# claim disposition counts
q=pd.read_csv(SRC/'Claim_Disposition_Counts.csv'); fig,ax=plt.subplots(figsize=(7,4.5)); ax.bar(q.disposition,q['count']); ax.set_ylabel('Claims'); ax.set_title('Layer 0 claim dispositions through P02'); plt.xticks(rotation=25,ha='right'); save('L10-CUM-FIG-004.png')
# A0 full training
q=pd.read_csv(SRC/'P02_Table_A0_fulltrain_branch_summary.csv'); branches=['CLS-CSP-LDA','CLS-FBCSP-LR','RIE-TS-LR','RIE-EA-TS','DNN-EEGNET','DNN-FBCNET','DNN-SEQ','SSL-CBRAMOD']; p=q[q.branch_id.isin(branches)].pivot(index='branch_id',columns='dataset_id',values='BACC_mean').reindex(branches); ax=p.plot(kind='bar',figsize=(11,6)); ax.set_ylabel('Participant-first mean BACC'); ax.set_title('P02 A0 full-training performance by dataset'); ax.set_ylim(0.4,0.9); plt.xticks(rotation=35,ha='right'); save('L10-P02-FIG-001.png')
# participant distributions Lee / Physio
pp=pd.read_csv(SRC/'P02_Table_A0_participant_first_fulltrain_source.csv'); sel=['CLS-CSP-LDA','RIE-TS-LR','DNN-EEGNET','DNN-SEQ']
for n,ds in [(9,'Lee2019_MI'),(10,'PhysioNetMI')]:
    d=pp[(pp.dataset_id==ds)&pp.branch_id.isin(sel)]; arr=[d[d.branch_id==b].BACC.dropna().values for b in sel]; fig,ax=plt.subplots(figsize=(8,5)); ax.boxplot(arr,tick_labels=sel,showmeans=True); ax.set_ylabel('Participant-first BACC'); ax.set_title(f'P02 participant heterogeneity - {ds}'); plt.xticks(rotation=25,ha='right'); save(f'L10-P02-FIG-{n:03d}.png')
# low label per dataset
ll=pd.read_csv(SRC/'P02_Table_low_label_BACC.csv')
for n,ds in [(2,'BNCI2014_001'),(3,'Lee2019_MI'),(4,'PhysioNetMI')]:
    d=ll[ll.dataset_id==ds]; fig,ax=plt.subplots(figsize=(8,5))
    for model in d.model_id.unique():
        m=d[d.model_id==model].sort_values('budget_per_class'); ax.plot(m.budget_per_class,m.value,marker='o',label=model)
    ax.axhline(0.5,linewidth=1); ax.set_xscale('log',base=2); ax.set_xticks([1,2,4,8,16,32],labels=['1','2','4','8','16','32']); ax.set_xlabel('Labels/class - one frozen subset per budget'); ax.set_ylabel('BACC'); ax.set_title(f'P02 low-label BACC - {ds}'); ax.legend(); save(f'L10-P02-FIG-{n:03d}.png')
# Stage11 challenger effect
q=pd.read_csv(SRC/'P02_Table_training_policy_challenger_statistics.csv'); fig,ax=plt.subplots(figsize=(7,4.5)); y=np.arange(len(q)); x=q.median_delta_BACC.values; err=np.vstack([x-q.ci_low.values,q.ci_high.values-x]); ax.errorbar(x,y,xerr=err,fmt='o',capsize=4); ax.axvline(0,linewidth=1); ax.set_yticks(y,q.dataset_id); ax.set_xlabel('Median paired delta BACC'); ax.set_title('Stage 11 diagnostic challenger effect'); save('L10-P02-FIG-005.png')
# A4 condition effects
q=pd.read_csv(SRC/'P02_Table_A4_role_condition_summary.csv'); q=q[q.evaluable_effect_cells>0].copy(); fig,ax=plt.subplots(figsize=(11,7)); labels=(q.dataset_id+' | '+q.role_id+' | '+q.alternative_condition.str.replace('A4-','',regex=False)).tolist(); ax.barh(np.arange(len(q)),q.median_cell_effect.values); ax.axvline(0,linewidth=1); ax.set_yticks(np.arange(len(q)),labels); ax.set_xlabel('Median of comparison-cell median delta BACC'); ax.set_title('P02 A4 C1-C3 role-control effect directions'); save('L10-P02-FIG-006.png')
# Stage18S sign consistency
q=pd.read_csv(SRC/'P02_Table_Stage18S_three_repeat_anchor_stability.csv'); c=q.sign_consistency.value_counts().reindex(['ALL_NEGATIVE','MIXED','ALL_POSITIVE']).fillna(0); fig,ax=plt.subplots(figsize=(7,4.5)); ax.bar(c.index,c.values); ax.set_ylabel('Anchor trajectories (n=45)'); ax.set_title('Stage18S three-repeat sign consistency - post-hoc descriptive'); plt.xticks(rotation=15); save('L10-P02-FIG-007.png')
# failure categories
q=pd.read_csv(SRC/'P02_Table_failure_category_breakdown.csv'); g=q.groupby('failure_code')['count'].sum().sort_values(ascending=False); fig,ax=plt.subplots(figsize=(8,4.8)); ax.bar(g.index,g.values); ax.set_ylabel('FailureCaseIndex records'); ax.set_title('P02 governed non-success categories'); plt.xticks(rotation=25,ha='right'); save('L10-P02-FIG-008.png')
