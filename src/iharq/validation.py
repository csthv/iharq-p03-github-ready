from __future__ import annotations
from pathlib import Path
from typing import Any
import json
from pydantic import ValidationError
from .models import RecordEnvelope
from .schemas import load_schema,errors as schema_errors
from .catalog import by_type
from .lineage import missing_sources
from .errors import ValidationIssue
from .canonical import semantic_hash

A_IDS={f"A{i}" for i in range(14)}
MOCK_TAGS={"MOCK","NON_EMPIRICAL","NON_CLAIM_BEARING"}

def issue(code,msg,path="<root>",owner="BUILD_BOOK",gate="P0-GATE-08"):
    return ValidationIssue(code,msg,path,owner,gate).as_dict()

def validate_bundle(bundle:dict[str,Any],root:str|Path=".")->list[dict]:
    root=Path(root); out=[]; records=bundle.get('records')
    if not isinstance(records,list): return [issue('BUNDLE_RECORDS_TYPE','records must be a list')]
    catalog=by_type(root/'catalogs/record_family_catalog.yaml')
    for i,r in enumerate(records):
        path=f"records/{i}"
        try: RecordEnvelope.model_validate(r)
        except ValidationError as e:
            out += [issue('PYDANTIC_RECORD_INVALID',x['msg'],path+'/'+('/'.join(map(str,x['loc']))),gate='P0-GATE-03') for x in e.errors()]
            continue
        rt=r['record_type']
        if rt not in catalog: out.append(issue('RECORD_TYPE_UNKNOWN',rt,path,'REGISTRY','P0-GATE-03')); continue
        for e in schema_errors(r,load_schema(rt,root/'schemas/records')):
            out.append(issue('SCHEMA_VALIDATION_FAILED',e.message,path+'/'+('/'.join(map(str,e.path))),'REGISTRY','P0-GATE-03'))
        if r['owner_layer']!=catalog[rt]['owner_layer']: out.append(issue('OWNER_MISMATCH',f"expected {catalog[rt]['owner_layer']}",path,'ARCHITECTURE','P0-GATE-03'))
        if r.get('fixture') and not MOCK_TAGS.issubset(set(r.get('fixture_tags',[]))): out.append(issue('FIXTURE_TAGS_MISSING','required mock tags absent',path,'BUILD_BOOK','P0-GATE-06'))
        if r.get('ablation_id') and r['ablation_id'] not in A_IDS: out.append(issue('ABLATION_ID_UNAUTHORIZED',r['ablation_id'],path,'PROTOCOL','P0-GATE-09'))
        if r['lifecycle_status'] in {'SUPERSEDED','INVALIDATED'} and r.get('payload',{}).get('reused_for_acceptance'): out.append(issue('STALE_REUSE','stale artifact reused',path,'REGISTRY','P0-GATE-16'))
        if r['owner_layer']=='L10' and r['evidence_role']=='PRIMARY': out.append(issue('L10_PRIMARY_EVIDENCE_FORBIDDEN','Layer 10 is read-only',path,'LAYER10','P0-GATE-14'))
        if rt in {'ViewDefinition','CardDefinition','DashboardMetricRecord','ClaimEvidenceManifest','ReproductionManifest','PhaseHandoffRecord'} and not r['source_ids']: out.append(issue('L10_SOURCE_REQUIRED','read-only product lacks source lineage',path,'LAYER10','P0-GATE-14'))
        if rt.startswith('Stress') or rt=='MatchedStressPairRecord':
            if 'STRESS_ONLY' not in r['limitation_tags']: out.append(issue('STRESS_LIMITATION_MISSING','STRESS_ONLY required',path,'L8','P0-GATE-16'))
        if rt.startswith('Embodiment') or rt in {'SafetyEventRecord','Layer9RewardTrace','Layer9EmbodimentDemoManifest'}:
            if 'EMBODIMENT_PROXY_ONLY' not in r['limitation_tags']: out.append(issue('EMBODIMENT_LIMITATION_MISSING','EMBODIMENT_PROXY_ONLY required',path,'L9','P0-GATE-16'))
    ids=[r.get('record_id') for r in records]
    if len(ids)!=len(set(ids)): out.append(issue('RECORD_ID_DUPLICATE','duplicate record IDs',owner='REGISTRY',gate='P0-GATE-05'))
    for r in records:
        if r.get('record_id') in r.get('source_ids',[]): out.append(issue('LINEAGE_SELF_REFERENCE','record references itself',r.get('record_id','<unknown>'),'REGISTRY','P0-GATE-10'))
        if not r.get('config_id'): out.append(issue('CONFIG_ID_MISSING','config identity required',r.get('record_id','<unknown>'),'BUILD_BOOK','P0-GATE-04'))
        if r.get('owner_layer')=='L0' and r.get('evidence_role')=='PRIMARY': out.append(issue('L0_PRIMARY_MEASUREMENT_FORBIDDEN','Layer 0 cannot own measurements',r.get('record_id','<unknown>'),'LAYER0','P0-GATE-13'))
    for rid,missing in missing_sources(records).items(): out.append(issue('LINEAGE_SOURCE_MISSING',str(missing),rid,'REGISTRY','P0-GATE-10'))
    c=bundle.get('controls',{})
    if set(c.get('train_ids',[])) & set(c.get('test_ids',[])): out.append(issue('SPLIT_OVERLAP','train/test overlap',owner='PROTOCOL',gate='P0-GATE-08'))
    if c.get('calibration_fit_on_evaluation'): out.append(issue('LEAKAGE_CALIBRATION_EVAL','calibration fit leakage',owner='PROTOCOL',gate='P0-GATE-08'))
    if c.get('chronology_valid') is False: out.append(issue('CHRONOLOGY_INVALID','chronology violation',owner='PROTOCOL',gate='P0-GATE-08'))
    if c.get('matched') is False: out.append(issue('MATCHING_KEYS_MISMATCH','matched comparison mismatch',owner='PROTOCOL',gate='P0-GATE-10'))
    if c.get('denominator_left') is not None and c.get('denominator_left')!=c.get('denominator_right'): out.append(issue('DENOMINATOR_MISMATCH','comparison denominators differ',owner='PROTOCOL',gate='P0-GATE-08'))
    if c.get('metric_definition_present') is False: out.append(issue('METRIC_DEFINITION_MISSING','metric dictionary entry missing',owner='REGISTRY',gate='P0-GATE-08'))
    if c.get('negative_result') and not c.get('negative_visible'): out.append(issue('NEGATIVE_RESULT_HIDDEN','negative result hidden',owner='PLAN',gate='P0-GATE-13'))
    if c.get('diagnostic_only') and not c.get('diagnostic_status_present'): out.append(issue('DIAGNOSTIC_STATUS_MISSING','diagnostic status missing',owner='REGISTRY',gate='P0-GATE-13'))
    if c.get('limitation_weakened'): out.append(issue('LIMITATION_WEAKENED','limitation weakened',owner='LAYER0',gate='P0-GATE-13'))
    if c.get('unsupported_claim'): out.append(issue('CLAIM_UNSUPPORTED','unsupported claim',owner='LAYER0',gate='P0-GATE-13'))
    if c.get('update_enabled') and c.get('update_applied') and not any(r.get('record_type')=='PolicyUpdateTrace' for r in records): out.append(issue('POLICY_UPDATE_TRACE_MISSING','update trace required',owner='L7',gate='P0-GATE-11'))
    if c.get('frozen') and c.get('mutation_count',0): out.append(issue('FROZEN_POLICY_MUTATION','mutation during frozen evaluation',owner='L7',gate='P0-GATE-12'))
    if c.get('frozen') and not c.get('disabled_update_audit'): out.append(issue('FROZEN_UPDATE_AUDIT_MISSING','disabled-update audit missing',owner='L7',gate='P0-GATE-12'))
    if c.get('unresolved_alias_treated_canonical'): out.append(issue('ALIAS_CANONICALIZED_WITHOUT_AUTHORITY','unresolved alias promoted',owner='REGISTRY',gate='P0-GATE-16'))
    if c.get('hash_expected') is not None and c.get('hash_expected')!=c.get('hash_observed'): out.append(issue('SEMANTIC_HASH_MISMATCH','hash mismatch',owner='BUILD_BOOK',gate='P0-GATE-05'))
    if c.get('manifest_complete') is False: out.append(issue('MANIFEST_CLOSURE_FAILED','manifest incomplete',owner='BUILD_BOOK',gate='P0-GATE-15'))
    if c.get('lifecycle_transition_valid') is False: out.append(issue('LIFECYCLE_TRANSITION_INVALID','invalid lifecycle transition',owner='REGISTRY',gate='P0-GATE-16'))
    if c.get('claim_evidence_links_resolve') is False: out.append(issue('CLAIM_EVIDENCE_LINK_MISSING','claim-evidence link unresolved',owner='LAYER0',gate='P0-GATE-13'))
    if c.get('safety_alias_valid') is False: out.append(issue('SAFETY_ALIAS_UNRESOLVED','safety alias unresolved',owner='REGISTRY',gate='P0-GATE-16'))
    if c.get('unsafe_output_path'): out.append(issue('PATH_TRAVERSAL_FORBIDDEN','unsafe output path',owner='BUILD_BOOK',gate='P0-GATE-02'))
    if c.get('secret_like_value'): out.append(issue('SECRET_VALUE_FORBIDDEN','secret-like value present',owner='SECURITY',gate='P0-GATE-17'))
    if c.get('seed_required') and c.get('seed') is None: out.append(issue('SEED_MISSING','required seed absent',owner='PROTOCOL',gate='P0-GATE-05'))
    # Official Layer Audit 1 deterministic controls. These are bundle-level because they verify cross-record joins and noninterference.
    if c.get('expected_config_id'):
        bad_cfg=[r.get('record_id') for r in records if r.get('config_id')!=c['expected_config_id']]
        if bad_cfg: out.append(issue('BUNDLE_CONFIG_IDENTITY_MISMATCH',str(bad_cfg),owner='BUILD_BOOK',gate='P0-GATE-04'))
    for record_id,expected in c.get('record_hashes',{}).items():
        record=next((r for r in records if r.get('record_id')==record_id),None)
        if record is None or semantic_hash(record)!=expected: out.append(issue('RECORD_SEMANTIC_HASH_MISMATCH',record_id,owner='BUILD_BOOK',gate='P0-GATE-05'))
    audit_flags={
      'trial_window_links_resolve':('TRIAL_WINDOW_LINEAGE_MISMATCH','L1','P0-GATE-10'),
      'raw_derived_distinction':('RAW_DERIVED_DISTINCTION_MISSING','L1','P0-GATE-03'),
      'license_access_present':('LICENSE_ACCESS_MISSING','L1','P0-GATE-03'),
      'exclusions_missingness_recorded':('EXCLUSIONS_MISSINGNESS_UNRECORDED','L1','P0-GATE-08'),
      'model_checkpoint_links_resolve':('MODEL_CHECKPOINT_LINK_MISSING','L2','P0-GATE-10'),
      'prediction_model_links_resolve':('PREDICTION_MODEL_LINK_MISMATCH','L2','P0-GATE-10'),
      'prediction_reuse_immutable':('PREDICTION_REUSE_MUTABLE','L2','P0-GATE-16'),
      'seed_environment_config_lineage_complete':('SEED_ENV_CONFIG_LINEAGE_INCOMPLETE','L2','P0-GATE-05'),
      'downstream_calibration_links_resolve':('DOWNSTREAM_CALIBRATION_LINK_MISSING','L2','P0-GATE-10'),
      'calibration_source_links_resolve':('CALIBRATION_SOURCE_LINK_MISMATCH','L3','P0-GATE-10'),
      'fit_evaluation_disjoint':('CALIBRATION_FIT_EVALUATION_OVERLAP','L3','P0-GATE-08'),
      'threshold_valid':('THRESHOLD_INVALID','L3','P0-GATE-08'),
      'high_confidence_wrong_handled':('HIGH_CONFIDENCE_WRONG_UNHANDLED','L3','P0-GATE-13'),
      'l4_interface_resolves':('L4_INTERFACE_UNRESOLVED','L3','P0-GATE-10'),
      'l10_interface_resolves':('L10_INTERFACE_UNRESOLVED','L3','P0-GATE-14'),
      'layer0_noninterference':('LAYER0_NONINTERFERENCE_VIOLATION','LAYER0','P0-GATE-13'),
    }
    for key,(code,owner,gate) in audit_flags.items():
        if key in c and c.get(key) is False: out.append(issue(code,key,owner=owner,gate=gate))

    # Official Layer Audit 2 deterministic controls for L4-L7.
    audit2_flags={
      'evidence_request_links_resolve':('L4_EVIDENCE_REQUEST_LINK_MISSING','L4','P0-GATE-10'),
      'evidence_quality_compatible':('L4_EVIDENCE_INCOMPATIBLE','L4','P0-GATE-10'),
      'iharq_reason_action_valid':('L4_REASON_ACTION_INVALID','L4','P0-GATE-08'),
      'iharq_fallback_supported':('L4_FALLBACK_UNSUPPORTED','L4','P0-GATE-08'),
      'iharq_trace_explanation_present':('L4_TRACE_EXPLANATION_MISSING','L4','P0-GATE-10'),
      'l4_limitations_preserved':('L4_LIMITATION_MISSING','L4','P0-GATE-13'),
      'temporal_predecessor_present':('L5_PREDECESSOR_MISSING','L5','P0-GATE-10'),
      'temporal_windows_compatible':('L5_WINDOWS_INCOMPATIBLE','L5','P0-GATE-08'),
      'temporal_transition_valid':('L5_TRANSITION_INVALID','L5','P0-GATE-08'),
      'recovery_provenance_present':('L5_RECOVERY_PROVENANCE_MISSING','L5','P0-GATE-10'),
      'silent_reset_absent':('L5_SILENT_RESET','L5','P0-GATE-08'),
      'temporal_reuse_valid':('L5_TEMPORAL_REUSE_INVALID','L5','P0-GATE-16'),
      'readiness_boundary_valid':('L6_L7_BOUNDARY_VIOLATION','REGISTRY','P0-GATE-03'),
      'readiness_evidence_links_resolve':('L6_EVIDENCE_LINK_MISSING','L6','P0-GATE-10'),
      'legal_action_constraints_respected':('L6_ACTION_CONSTRAINT_VIOLATION','L6','P0-GATE-08'),
      'cost_reward_budget_present':('L6_COST_REWARD_BUDGET_MISSING','L6','P0-GATE-04'),
      'policy_mode_present':('L6_POLICY_MODE_MISSING','L6','P0-GATE-04'),
      'update_eligibility_valid':('L6_UPDATE_ELIGIBILITY_INVALID','L6','P0-GATE-11'),
      'adaptive_frozen_separated':('L6_ADAPTIVE_FROZEN_MIXED','L6','P0-GATE-12'),
      'transition_links_resolve':('L7_TRANSITION_LINK_MISMATCH','L7','P0-GATE-10'),
      'session_episode_rollout_links_resolve':('L7_SESSION_EPISODE_ROLLOUT_MISMATCH','L7','P0-GATE-10'),
      'reward_cost_versions_resolve':('L7_REWARD_COST_VERSION_MISSING','L7','P0-GATE-05'),
      'safety_event_links_resolve':('L7_SAFETY_EVENT_LINK_MISSING','L7','P0-GATE-10'),
      'trajectory_lineage_resolves':('L7_TRAJECTORY_LINEAGE_BROKEN','L7','P0-GATE-10'),
      'simulation_limitations_preserved':('L7_SIMULATION_LIMITATION_MISSING','L7','P0-GATE-16'),
      'update_before_after_policy_present':('L7_UPDATE_POLICY_IDENTITIES_MISSING','L7','P0-GATE-11'),
      'update_source_transition_present':('L7_UPDATE_SOURCE_TRANSITION_MISSING','L7','P0-GATE-11'),
      'update_reward_config_seed_present':('L7_UPDATE_REWARD_CONFIG_SEED_MISSING','L7','P0-GATE-11'),
      'update_limitation_present':('L7_UPDATE_LIMITATION_MISSING','L7','P0-GATE-11'),
      'update_simulation_status_present':('L7_UPDATE_SIMULATION_STATUS_MISSING','L7','P0-GATE-11'),
      'frozen_status_present':('L7_FROZEN_STATUS_MISSING','L7','P0-GATE-12'),
      'adaptive_frozen_outputs_distinct':('L7_ADAPTIVE_FROZEN_OUTPUTS_INDISTINGUISHABLE','L7','P0-GATE-12'),
      'layer10_mode_warning_present':('L10_POLICY_MODE_WARNING_MISSING','LAYER10','P0-GATE-14'),
      'uncertainty_abstention_distinct':('L3_L4_UNCERTAINTY_ABSTENTION_COLLAPSED','L4','P0-GATE-10'),
    }
    for key,(code,owner,gate) in audit2_flags.items():
        if key in c and c.get(key) is False: out.append(issue(code,key,owner=owner,gate=gate))
    # Record-level L4-L7 invariants apply only to official Audit 2 bundles.
    audit2_mode=str(bundle.get('bundle_id','')).startswith('P00-OFFICIAL-AUDIT2') or any(k in c for k in audit2_flags)
    by_type_records={}
    for r in records: by_type_records.setdefault(r.get('record_type'),[]).append(r)
    for r in records if audit2_mode else []:
        rt=r.get('record_type'); p=r.get('payload',{}); path=r.get('record_id','<unknown>')
        if rt in {'StateRecord','TransitionRecord','EpisodeRecord','RolloutRecord','PolicyRecord','PolicyUpdateTrace'} and 'SIMULATION_ONLY' not in r.get('limitation_tags',[]):
            out.append(issue('L7_SIMULATION_LIMITATION_MISSING','SIMULATION_ONLY required',path,'L7','P0-GATE-16'))
        if rt in {'EvidenceRequestRecord','EvidenceQualityRecord','IHARQDecisionRecord'} and not r.get('limitation_tags'):
            out.append(issue('L4_LIMITATION_MISSING','L4 foundation limitation required',path,'L4','P0-GATE-13'))
        if rt=='EvidenceRequestRecord' and not p.get('requested_evidence'):
            out.append(issue('L4_EVIDENCE_REQUEST_EMPTY','requested_evidence empty',path,'L4','P0-GATE-08'))
        if rt=='EvidenceQualityRecord' and p.get('compatibility_status')=='INCOMPATIBLE' and p.get('quality_status')=='SUFFICIENT':
            out.append(issue('L4_INCOMPATIBLE_EVIDENCE_ACCEPTED','incompatible evidence cannot be sufficient',path,'L4','P0-GATE-08'))
        if rt=='IHARQDecisionRecord' and p.get('action')=='ACCEPT' and p.get('decision_status') in {'ABSTAINED','DEFERRED','BLOCKED','INVALID'}:
            out.append(issue('L4_DECISION_ACTION_STATUS_CONFLICT','action/status conflict',path,'L4','P0-GATE-08'))
        if rt=='RegimeStateRecord' and p.get('silent_reset'):
            out.append(issue('L5_SILENT_RESET','silent reset forbidden',path,'L5','P0-GATE-08'))
        if rt=='TemporalTrustRecord' and p.get('window_start','') > p.get('window_end',''):
            out.append(issue('L5_REVERSED_CHRONOLOGY','window_start after window_end',path,'L5','P0-GATE-08'))
        if rt=='PolicyActionRecord' and p.get('constraint_status')!='LEGAL':
            out.append(issue('L6_ILLEGAL_POLICY_ACTION','policy action not legal',path,'L6','P0-GATE-08'))
        if rt=='PolicyUpdateTrace':
            if p.get('before_policy_id')==p.get('after_policy_id'):
                out.append(issue('L7_UPDATE_IDENTITIES_UNCHANGED','before/after policy IDs must differ',path,'L7','P0-GATE-11'))
            if p.get('simulation_status')!='SIMULATION_ONLY':
                out.append(issue('L7_UPDATE_SIMULATION_STATUS_MISSING','update must be simulation-only',path,'L7','P0-GATE-11'))
        if rt=='RolloutRecord' and p.get('policy_mode')=='FROZEN_EVALUATION' and (p.get('update_mode')!='DISABLED' or p.get('frozen_status')!='FROZEN' or p.get('output_class')!='FROZEN'):
            out.append(issue('L7_FROZEN_ROLLOUT_INVALID','frozen rollout contract violated',path,'L7','P0-GATE-12'))

    # Official Layer Audit 3 deterministic controls for L8-L10 and global integration.
    audit3_flags={
      'stress_clean_source_present':('L8_CLEAN_SOURCE_MISSING','L8','P0-GATE-10'),
      'stress_profile_schedule_consistent':('L8_PROFILE_SCHEDULE_MISMATCH','L8','P0-GATE-08'),
      'stress_intensity_valid':('L8_INTENSITY_INVALID','L8','P0-GATE-08'),
      'stress_schedule_valid':('L8_SCHEDULE_INVALID','L8','P0-GATE-08'),
      'stress_injection_valid':('L8_INJECTION_INVALID','L8','P0-GATE-08'),
      'stress_seed_present':('L8_SEED_MISSING','L8','P0-GATE-05'),
      'stress_target_compatible':('L8_TARGET_INCOMPATIBLE','L8','P0-GATE-08'),
      'stress_lineage_resolves':('L8_LINEAGE_BREAK','L8','P0-GATE-10'),
      'stress_limitation_preserved':('L8_LIMITATION_MISSING','L8','P0-GATE-13'),
      'stress_identity_reuse_valid':('L8_CHANGED_IDENTITY_REUSED','L8','P0-GATE-16'),
      'stress_matching_valid':('L8_MATCHING_MISMATCH','L8','P0-GATE-10'),
      'platform_identity_present':('L9_PLATFORM_IDENTITY_MISSING','L9','P0-GATE-05'),
      'task_asset_present':('L9_TASK_ASSET_MISSING','L9','P0-GATE-04'),
      'embodiment_config_present':('L9_CONFIG_MISSING','L9','P0-GATE-04'),
      'command_mapping_valid':('L9_COMMAND_MAPPING_INVALID','L9','P0-GATE-08'),
      'embodiment_state_outcome_links_resolve':('L9_STATE_OUTCOME_LINK_MISSING','L9','P0-GATE-10'),
      'safety_reward_links_resolve':('L9_SAFETY_REWARD_LINK_MISSING','L9','P0-GATE-10'),
      'demo_manifest_complete':('L9_DEMO_MANIFEST_INCOMPLETE','L9','P0-GATE-15'),
      'unsafe_actions_blocked':('L9_UNSAFE_ACTION_NOT_BLOCKED','L9','P0-GATE-08'),
      'simulator_failure_preserved':('L9_SIMULATOR_FAILURE_HIDDEN','L9','P0-GATE-16'),
      'embodiment_seed_present':('L9_SEED_MISSING','L9','P0-GATE-05'),
      'l7_l8_links_resolve':('L9_L7_L8_LINK_MISSING','L9','P0-GATE-10'),
      'embodiment_limitations_preserved':('L9_PROXY_LIMITATION_MISSING','L9','P0-GATE-13'),
      'no_real_world_claim':('L9_REAL_WORLD_CLAIM_FORBIDDEN','LAYER0','P0-GATE-13'),
      'source_inventory_valid':('L10_SOURCE_INVENTORY_INVALID','LAYER10','P0-GATE-14'),
      'source_bundles_valid':('L10_SOURCE_BUNDLE_INVALID','LAYER10','P0-GATE-14'),
      'metric_dictionary_resolves':('L10_METRIC_DICTIONARY_UNRESOLVED','LAYER10','P0-GATE-14'),
      'views_cards_sources_resolve':('L10_VIEW_CARD_SOURCE_MISSING','LAYER10','P0-GATE-14'),
      'figure_table_sources_resolve':('L10_FIGURE_TABLE_SOURCE_MISSING','LAYER10','P0-GATE-14'),
      'matched_comparison_preserved':('L10_MATCHED_COMPARISON_LOST','LAYER10','P0-GATE-14'),
      'negatives_diagnostics_failures_visible':('L10_FAILURE_VISIBILITY_LOST','LAYER10','P0-GATE-14'),
      'claim_evidence_lineage_resolves':('L10_CLAIM_EVIDENCE_LINEAGE_MISSING','LAYER10','P0-GATE-14'),
      'provenance_complete':('L10_PROVENANCE_INCOMPLETE','LAYER10','P0-GATE-15'),
      'limitations_warnings_preserved':('L10_WARNING_LIMITATION_LOSS','LAYER10','P0-GATE-14'),
      'exports_traceable':('L10_EXPORT_TRACE_MISSING','LAYER10','P0-GATE-15'),
      'reproduction_manifest_complete':('L10_REPRO_MANIFEST_INCOMPLETE','LAYER10','P0-GATE-15'),
      'phase_status_views_nonfinal':('L10_PREMATURE_FINAL_STATUS','LAYER10','P0-GATE-14'),
      'layer10_read_only':('L10_READ_ONLY_VIOLATION','LAYER10','P0-GATE-14'),
      'layer10_source_immutable':('L10_SOURCE_MUTATION','LAYER10','P0-GATE-14'),
      'no_unauthorized_recomputation':('L10_UNAUTHORIZED_RECOMPUTATION','LAYER10','P0-GATE-14'),
      'global_authority_config_source_chain':('GLOBAL_AUTHORITY_CONFIG_CHAIN_BROKEN','BUILD_BOOK','P0-GATE-10'),
      'run_manifest_complete':('GLOBAL_RUN_MANIFEST_INCOMPLETE','BUILD_BOOK','P0-GATE-15'),
      'validation_evidence_linked':('GLOBAL_VALIDATION_EVIDENCE_UNLINKED','BUILD_BOOK','P0-GATE-15'),
      'candidate_statement_interface_present':('GLOBAL_CANDIDATE_STATEMENT_INTERFACE_MISSING','LAYER0','P0-GATE-13'),
      'layer0_interface_present':('GLOBAL_LAYER0_INTERFACE_MISSING','LAYER0','P0-GATE-13'),
      'future_evidence_map_ids_reserved':('GLOBAL_EVIDENCE_MAP_SLOT_MISSING','GOVERNANCE','P0-GATE-15'),
      'layer10_interface_present':('GLOBAL_LAYER10_INTERFACE_MISSING','LAYER10','P0-GATE-14'),
      'future_release_handoff_slots_present':('GLOBAL_RELEASE_HANDOFF_SLOT_MISSING','BUILD_BOOK','P0-GATE-15'),
      'l0_3_chain_valid':('GLOBAL_L0_3_CHAIN_INVALID','BUILD_BOOK','P0-GATE-10'),
      'l3_7_chain_valid':('GLOBAL_L3_7_CHAIN_INVALID','BUILD_BOOK','P0-GATE-10'),
      'l7_10_chain_valid':('GLOBAL_L7_10_CHAIN_INVALID','BUILD_BOOK','P0-GATE-10'),
      'all_layer_matrix_complete':('GLOBAL_LAYER_MATRIX_INCOMPLETE','BUILD_BOOK','P0-GATE-03'),
      'future_artifact_contracts_complete':('GLOBAL_FUTURE_ARTIFACT_CONTRACT_INCOMPLETE','BUILD_BOOK','P0-GATE-03'),
    }
    for key,(code,owner,gate) in audit3_flags.items():
        if key in c and c.get(key) is False: out.append(issue(code,key,owner=owner,gate=gate))
    audit3_mode=str(bundle.get('bundle_id','')).startswith('P00-OFFICIAL-AUDIT3') or any(k in c for k in audit3_flags)
    for r in records if audit3_mode else []:
        rt=r.get('record_type'); p=r.get('payload',{}); path=r.get('record_id','<unknown>'); limits=set(r.get('limitation_tags',[]))
        if r.get('owner_layer')=='L8' and 'STRESS_ONLY' not in limits:
            out.append(issue('L8_LIMITATION_MISSING','STRESS_ONLY required',path,'L8','P0-GATE-13'))
        if rt=='StressProfileRecord' and (not p.get('clean_source_id') or p.get('seed') is None or not p.get('injection_point')):
            out.append(issue('L8_PROFILE_INCOMPLETE','stress profile incomplete',path,'L8','P0-GATE-08'))
        if rt=='StressScheduleRecord' and (not p.get('schedule') or p.get('seed') is None):
            out.append(issue('L8_SCHEDULE_INVALID','stress schedule incomplete',path,'L8','P0-GATE-08'))
        if rt=='StressApplicationRecord' and p.get('clean_source_overwritten') is not False:
            out.append(issue('L8_CLEAN_SOURCE_OVERWRITE','clean source overwrite forbidden',path,'L8','P0-GATE-16'))
        if rt=='MatchedStressPairRecord' and p.get('match_status')!='MATCHED':
            out.append(issue('L8_MATCHING_MISMATCH','clean/stressed pair unmatched',path,'L8','P0-GATE-10'))
        if r.get('owner_layer')=='L9' and not {'SIMULATION_ONLY','EMBODIMENT_PROXY_ONLY'}<=limits:
            out.append(issue('L9_PROXY_LIMITATION_MISSING','simulation/proxy limitations required',path,'L9','P0-GATE-13'))
        if rt=='CommandMappingRecord' and p.get('mapping_status')!='VALIDATED':
            out.append(issue('L9_COMMAND_MAPPING_INVALID','command mapping not validated',path,'L9','P0-GATE-08'))
        if rt=='SafetyEventRecord' and p.get('simulation_only') is not True:
            out.append(issue('L9_SAFETY_EVENT_NOT_SIMULATION_ONLY','safety event must remain simulation-only',path,'L9','P0-GATE-13'))
        if rt=='EmbodimentOutcomeRecord' and p.get('outcome_status')=='UNSAFE' and not p.get('safety_event_ids'):
            out.append(issue('L9_UNSAFE_OUTCOME_WITHOUT_EVENT','unsafe outcome missing safety event',path,'L9','P0-GATE-10'))
        if r.get('owner_layer')=='L10' and r.get('evidence_role')=='PRIMARY':
            out.append(issue('L10_PRIMARY_EVIDENCE_FORBIDDEN','Layer 10 cannot produce primary evidence',path,'LAYER10','P0-GATE-14'))
        if rt=='DashboardMetricRecord' and (p.get('rendering_only') is not True or p.get('recomputed') is not False):
            out.append(issue('L10_UNAUTHORIZED_RECOMPUTATION','metric must be rendering-only and non-recomputed',path,'LAYER10','P0-GATE-14'))
        if rt in {'DashboardViewRecord','CardRecord','FigureSourceRecord','TableSourceRecord'} and p.get('read_only') is not True:
            out.append(issue('L10_READ_ONLY_VIOLATION','read_only must be true',path,'LAYER10','P0-GATE-14'))
        if rt in {'DashboardViewRecord','CardRecord'} and not p.get('warning_ids'):
            out.append(issue('L10_WARNING_LIMITATION_LOSS','warnings required',path,'LAYER10','P0-GATE-14'))

    claim_class=c.get('unsupported_claim_class')
    if claim_class in {'SCIENTIFIC','CLINICAL','DEPLOYMENT','SAFETY','REGULATORY'}:
        out.append(issue(f'CLAIM_{claim_class}_UNSUPPORTED',f'unsupported {claim_class.lower()} implication',owner='LAYER0',gate='P0-GATE-13'))
    return out

def load_bundle(path:str|Path): return json.loads(Path(path).read_text(encoding='utf-8'))
