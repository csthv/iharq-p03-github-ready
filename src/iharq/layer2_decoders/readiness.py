P03_PREDICTION_FIELDS={
'dataset_id','subject_id','session_id','source_event_id','window_id','split_id','split_role','budget_id','budget_repeat_id','model_id','model_variant','checkpoint_id','model_seed','y_pred','class_order','score_type','score_vector','score_semantics'
}
P03_SUPPORT_FIELDS={
'run_cell_id','ablation_id','condition_id','aggregation_identity','failure_missingness_status','metric_dictionary_reference','config_sha256','scientific_freeze_id'
}
def p03_readiness(prediction_fields,support_fields=None):
 m=sorted(P03_PREDICTION_FIELDS-set(prediction_fields));sm=sorted(P03_SUPPORT_FIELDS-set(support_fields or set()));return {'status':'PASS' if not m and not sm else 'BLOCKED','missing_prediction_fields':m,'missing_support_fields':sm,'required_prediction_fields':sorted(P03_PREDICTION_FIELDS),'required_support_fields':sorted(P03_SUPPORT_FIELDS)}
def evidence_sufficiency(s):
 req=['a0_complete','a4_complete','c4_c5_complete','a4_burden_complete','failure_evidence','figure_table_sources','handoffs','p03_complete','security_pass','readiness_record'];m=[x for x in req if s.get(x) is not True];return {'status':'PASS' if not m else 'EVIDENCE_INSUFFICIENT','missing':m}
