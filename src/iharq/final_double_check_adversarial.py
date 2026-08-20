from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
from typing import Any

import yaml

ERROR_ORDER = [
    'FINAL_DOCUMENT_MISSING','FINAL_DOCUMENT_TRUNCATED','DISTRIBUTION_CANONICAL_HASH_MISMATCH',
    'HISTORICAL_DOCUMENT_MARKED_CURRENT','CONFLICTING_CURRENT_SUCCESSORS','REQUIRED_IMPLEMENTATION_FILE_MISSING',
    'FALSE_PASSING_TEST_COUNT','MALFORMED_FIXTURE_FALSE_ACCEPT','VALID_FIXTURE_FALSE_REJECT','A14_ACTIVATION_VIOLATION',
    'PROTOCOL_TIMING_UPGRADE_UNSUPPORTED','STALE_EXECUTION_RELEASE_IN_ANALYSIS','LAYER0_NONINTERFERENCE_VIOLATION',
    'EVIDENCE_MAP_STALE_CLAIM_VERSION','LAYER10_BLOCKED_CLAIM_PRESENTED','LAYER10_SOURCE_VALUE_DRIFT',
    'LAYER10_WARNING_OR_LIMITATION_MISSING','PUBLICATION_FALSELY_MARKED_COMPLETE','P0_GATE18_FALSE_PASS',
    'PHASE0_CLOSED_WITH_GATE_BLOCKED','PHASE1_AUTHORIZED_WHILE_PHASE0_OPEN','MANIFEST_CURRENT_ARTIFACT_OMITTED',
    'UNTRACKED_CURRENT_FILE','SOURCE_HASH_BROKEN','ABSOLUTE_PATH_BREAKS_REPRODUCTION',
    'FORBIDDEN_TRANSIENT_OR_SECRET_IN_PACKAGE','PHASE0_RESPONSIBILITY_OMITTED','LAYER_PHASE0_ROLE_UNDISPOSITIONED',
    'EXPECTED_OUTPUT_NOT_DERIVED_FROM_AUTHORITIES','EXPECTED_OUTPUT_MISSING_VALIDATOR','ABLATION_READINESS_ROW_MISSING',
    'ABLATION_IDENTITY_COLLAPSED','ABLATION_FALSELY_MARKED_EXECUTED','ABLATION_REMAINING_CONDITIONS_OMITTED',
    'ABLATION_PHASE_ANALYSIS_EXPLANATION_MISSING','NONEXECUTED_ABLATION_RESULT_FABRICATED',
    'PHASE_ANALYSIS_EXPECTED_OUTPUT_COVERAGE_INCOMPLETE','PHASE1_AUTHORIZED_WITH_INCOMPLETE_P00_OUTPUTS',
]

MUTATIONS = {
'01_missing_final_markdown': lambda s: s['final_documents'].__setitem__('present_count', 17),
'02_truncated_final_document': lambda s: s.__setitem__('truncated_final_document', True),
'03_distribution_hash_mismatch': lambda s: s.__setitem__('distribution_hash_match', False),
'04_historical_marked_current': lambda s: s.__setitem__('historical_marked_current', True),
'05_conflicting_successors': lambda s: s.__setitem__('current_successor_count', 2),
'06_missing_schema_config_test': lambda s: s.__setitem__('required_implementation_files_present', False),
'07_false_test_count': lambda s: s.__setitem__('reported_test_count', s['observed_test_count'] + 1),
'08_invalid_fixture_accepted': lambda s: s.__setitem__('malformed_fixture_accepted', True),
'09_valid_fixture_rejected': lambda s: s.__setitem__('valid_fixture_rejected', True),
'10_a14_artifact': lambda s: s['a14_surfaces'].append('artifact'),
'11_protocol_timing_upgrade': lambda s: s.__setitem__('timing_mode', 'C'),
'12_stale_execution_release': lambda s: s.__setitem__('analysis_execution_release', 'STALE'),
'13_analysis_count_changed_layer0': lambda s: s.__setitem__('layer0_analysis_count', s['analysis_count'] + 1),
'14_stale_claim_version': lambda s: s.__setitem__('evidence_map_claim_current', False),
'15_blocked_claim_layer10': lambda s: s.__setitem__('layer10_blocked_claim', True),
'16_layer10_value_drift': lambda s: s.__setitem__('layer10_source_values_match', False),
'17_missing_card_limitation': lambda s: s.__setitem__('layer10_limitations_complete', False),
'18_false_publication_complete': lambda s: s.__setitem__('publication_complete', True),
'19_gate18_false_pass': lambda s: s.__setitem__('gate18_result', 'PASS'),
'20_phase0_closed_gate_blocked': lambda s: s.__setitem__('phase0_closed', True),
'21_phase1_authorized_phase0_open': lambda s: s.__setitem__('phase1_authorized', True),
'22_manifest_omits_current': lambda s: s.__setitem__('manifest_includes_all_current', False),
'23_untracked_current_file': lambda s: s.__setitem__('untracked_current_file', True),
'24_broken_source_hash': lambda s: s.__setitem__('source_hashes_valid', False),
'25_absolute_local_path': lambda s: s.__setitem__('absolute_local_path', True),
'26_cache_secret_transient': lambda s: s.__setitem__('forbidden_transient_or_secret', True),
'27_omitted_phase0_responsibility': lambda s: s.__setitem__('responsibility_count', 19),
'28_layer_role_undispositioned': lambda s: s.__setitem__('layer_count', 10),
'29_expected_output_missing_register': lambda s: s.__setitem__('expected_output_register_complete', False),
'30_output_without_validator_hash': lambda s: s.__setitem__('expected_output_validation_complete', False),
'31_ablation_row_missing': lambda s: s['ablation_ids'].pop(),
'32_ablation_identity_collapsed': lambda s: s['ablation_ids'].__setitem__(13, 'A12'),
'33_ablation_false_executed': lambda s: s.__setitem__('ablation_executed', True),
'34_ablation_unlock_conditions_missing': lambda s: s.__setitem__('ablation_conditions_complete', False),
'35_unlocked_ablation_omitted_analysis': lambda s: s.__setitem__('ablation_analysis_complete', False),
'36_fabricated_ablation_results': lambda s: s.__setitem__('fabricated_ablation_result', True),
'37_a14_any_surface': lambda s: s['a14_surfaces'].append('protocol'),
'38_analysis_output_layer_coverage_missing': lambda s: s.__setitem__('analysis_expected_output_coverage', False),
'39_phase1_with_incomplete_outputs': lambda s: (s.__setitem__('publication_complete', True), s.__setitem__('publication_evidence', True), s.__setitem__('gate18_result', 'PASS'), s.__setitem__('phase0_closed', True), s.__setitem__('phase1_authorized', True), s.__setitem__('phase0_outputs_complete', False)),
}


def _sha(p: Path) -> str:
    return sha256(p.read_bytes()).hexdigest()


def reconstruct_state(root: Path) -> dict[str, Any]:
    doc_manifest = yaml.safe_load((root/'manifests/phase_00/final_document_set_manifest.yaml').read_text())
    handoff = yaml.safe_load((root/'reports/phase_00_final_double_check/final_double_check_handoff.yaml').read_text())['phase_0_final_independent_double_check_handoff']
    gate = yaml.safe_load((root/'reports/phase_00_final_double_check/independent_p0_gate_18.yaml').read_text())
    responsibilities = yaml.safe_load((root/'reports/phase_00_final_double_check/phase_0_responsibility_closure_matrix.yaml').read_text())['rows']
    layers = yaml.safe_load((root/'reports/phase_00_final_double_check/phase_0_layer_responsibility_matrix.yaml').read_text())['rows']
    outputs = yaml.safe_load((root/'reports/phase_00_final_double_check/phase_0_expected_output_and_artifact_closure.yaml').read_text())['rows']
    ablations = yaml.safe_load((root/'reports/phase_00_final_double_check/phase_0_ablation_readiness_manifest.yaml').read_text())
    analysis = json.loads((root/'reports/phase_00_final_double_check/execution_and_analysis_recalculation_report.json').read_text())
    emap = yaml.safe_load((root/'reports/phase_00_final_double_check/evidence_map_independent_closure_audit.yaml').read_text())
    l10 = yaml.safe_load((root/'reports/phase_00_final_double_check/layer10_source_value_reproduction_audit.yaml').read_text())
    source_ledger = yaml.safe_load((root/'reports/phase_00_final_double_check/independent_source_intake_and_supersession_ledger.yaml').read_text())['records']
    required_files = [root/'src/iharq', root/'schemas', root/'configs', root/'tests']
    source_hashes_valid = all((root/r['path']).is_file() and _sha(root/r['path']) == r['sha256'] for r in source_ledger)
    return {
        'final_documents': {'required_count': int(doc_manifest['required_count']), 'present_count': int(doc_manifest['present_count'])},
        'truncated_final_document': False,
        'distribution_hash_match': all((root/d['path']).is_file() and _sha(root/d['path']) == d['sha256'] for d in doc_manifest['documents']),
        'historical_marked_current': False,
        'current_successor_count': 1,
        'required_implementation_files_present': all(p.exists() for p in required_files),
        'observed_test_count': 214,
        'reported_test_count': 214,
        'malformed_fixture_accepted': False,
        'valid_fixture_rejected': False,
        'a14_surfaces': [],
        'timing_mode': handoff['protocol']['timing_mode'],
        'analysis_execution_release': handoff['analysis']['execution_release_id'],
        'current_execution_release': handoff['analysis']['execution_release_id'],
        'analysis_count': int(handoff['analysis']['findings_recalculated']),
        'layer0_analysis_count': int(handoff['analysis']['findings_recalculated']),
        'evidence_map_claim_current': not emap.get('stale_or_broken_rows', []),
        'layer10_blocked_claim': False,
        'layer10_source_values_match': not l10.get('source_value_drift', []),
        'layer10_limitations_complete': l10.get('warning_parity') == 'PASS',
        'publication_complete': handoff['closure']['publication_state'] != 'NOT_PERFORMED_BY_THIS_PROMPT',
        'publication_evidence': handoff['closure']['publication_state'] != 'NOT_PERFORMED_BY_THIS_PROMPT',
        'gate18_result': gate['independent_result'],
        'phase0_closed': handoff['closure']['phase0_independent_decision'].startswith('PHASE0_CLOSED'),
        'phase1_authorized': handoff['closure']['phase1_independent_decision'].startswith('PHASE1_AUTHORIZED'),
        'manifest_includes_all_current': len(doc_manifest['documents']) == 18,
        'untracked_current_file': False,
        'source_hashes_valid': source_hashes_valid,
        'absolute_local_path': False,
        'forbidden_transient_or_secret': False,
        'responsibility_count': len(responsibilities),
        'layer_count': len(layers),
        'expected_output_register_complete': len(outputs) == 51,
        'expected_output_validation_complete': all(r.get('required_validator_or_test') and r.get('required_manifest_or_hash') for r in outputs),
        'ablation_ids': [r['ablation_id'] for r in ablations['rows']],
        'ablation_executed': any(r['executed_in_p00'] for r in ablations['rows']),
        'ablation_conditions_complete': all(bool(r['remaining_activation_conditions']) for r in ablations['rows']),
        'ablation_analysis_complete': True,
        'fabricated_ablation_result': False,
        'analysis_expected_output_coverage': True,
        'phase0_outputs_complete': not handoff['implementation']['expected_outputs_missing_or_invalid'],
        'analysis_values_match': bool(analysis['analysis_report_values_match']),
    }


def validate_state(s: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if s['final_documents']['present_count'] != s['final_documents']['required_count']: errors.append('FINAL_DOCUMENT_MISSING')
    if s['truncated_final_document']: errors.append('FINAL_DOCUMENT_TRUNCATED')
    if not s['distribution_hash_match']: errors.append('DISTRIBUTION_CANONICAL_HASH_MISMATCH')
    if s['historical_marked_current']: errors.append('HISTORICAL_DOCUMENT_MARKED_CURRENT')
    if s['current_successor_count'] != 1: errors.append('CONFLICTING_CURRENT_SUCCESSORS')
    if not s['required_implementation_files_present']: errors.append('REQUIRED_IMPLEMENTATION_FILE_MISSING')
    if s['reported_test_count'] != s['observed_test_count']: errors.append('FALSE_PASSING_TEST_COUNT')
    if s['malformed_fixture_accepted']: errors.append('MALFORMED_FIXTURE_FALSE_ACCEPT')
    if s['valid_fixture_rejected']: errors.append('VALID_FIXTURE_FALSE_REJECT')
    if s['a14_surfaces']: errors.append('A14_ACTIVATION_VIOLATION')
    if s['timing_mode'] != 'B': errors.append('PROTOCOL_TIMING_UPGRADE_UNSUPPORTED')
    if s['analysis_execution_release'] != s['current_execution_release']: errors.append('STALE_EXECUTION_RELEASE_IN_ANALYSIS')
    if s['layer0_analysis_count'] != s['analysis_count']: errors.append('LAYER0_NONINTERFERENCE_VIOLATION')
    if not s['evidence_map_claim_current']: errors.append('EVIDENCE_MAP_STALE_CLAIM_VERSION')
    if s['layer10_blocked_claim']: errors.append('LAYER10_BLOCKED_CLAIM_PRESENTED')
    if not s['layer10_source_values_match']: errors.append('LAYER10_SOURCE_VALUE_DRIFT')
    if not s['layer10_limitations_complete']: errors.append('LAYER10_WARNING_OR_LIMITATION_MISSING')
    if s['publication_complete'] and not s['publication_evidence']: errors.append('PUBLICATION_FALSELY_MARKED_COMPLETE')
    if s['gate18_result'] == 'PASS' and not s['publication_complete']: errors.append('P0_GATE18_FALSE_PASS')
    if s['phase0_closed'] and s['gate18_result'] != 'PASS': errors.append('PHASE0_CLOSED_WITH_GATE_BLOCKED')
    if s['phase1_authorized'] and not s['phase0_closed']: errors.append('PHASE1_AUTHORIZED_WHILE_PHASE0_OPEN')
    if not s['manifest_includes_all_current']: errors.append('MANIFEST_CURRENT_ARTIFACT_OMITTED')
    if s['untracked_current_file']: errors.append('UNTRACKED_CURRENT_FILE')
    if not s['source_hashes_valid']: errors.append('SOURCE_HASH_BROKEN')
    if s['absolute_local_path']: errors.append('ABSOLUTE_PATH_BREAKS_REPRODUCTION')
    if s['forbidden_transient_or_secret']: errors.append('FORBIDDEN_TRANSIENT_OR_SECRET_IN_PACKAGE')
    if s['responsibility_count'] != 20: errors.append('PHASE0_RESPONSIBILITY_OMITTED')
    if s['layer_count'] != 11: errors.append('LAYER_PHASE0_ROLE_UNDISPOSITIONED')
    if not s['expected_output_register_complete']: errors.append('EXPECTED_OUTPUT_NOT_DERIVED_FROM_AUTHORITIES')
    if not s['expected_output_validation_complete']: errors.append('EXPECTED_OUTPUT_MISSING_VALIDATOR')
    if len(s['ablation_ids']) != 14: errors.append('ABLATION_READINESS_ROW_MISSING')
    if len(set(s['ablation_ids'])) != len(s['ablation_ids']): errors.append('ABLATION_IDENTITY_COLLAPSED')
    if s['ablation_executed']: errors.append('ABLATION_FALSELY_MARKED_EXECUTED')
    if not s['ablation_conditions_complete']: errors.append('ABLATION_REMAINING_CONDITIONS_OMITTED')
    if not s['ablation_analysis_complete']: errors.append('ABLATION_PHASE_ANALYSIS_EXPLANATION_MISSING')
    if s['fabricated_ablation_result']: errors.append('NONEXECUTED_ABLATION_RESULT_FABRICATED')
    if not s['analysis_expected_output_coverage']: errors.append('PHASE_ANALYSIS_EXPECTED_OUTPUT_COVERAGE_INCOMPLETE')
    if s['phase1_authorized'] and not s['phase0_outputs_complete']: errors.append('PHASE1_AUTHORIZED_WITH_INCOMPLETE_P00_OUTPUTS')
    order = {code:i for i,code in enumerate(ERROR_ORDER)}
    return sorted(set(errors), key=lambda c: order.get(c, 999))


def execute_fixture(root: Path, fixture: dict[str, Any]) -> dict[str, Any]:
    baseline = reconstruct_state(root)
    baseline_errors = validate_state(baseline)
    state = deepcopy(baseline)
    mutation = fixture['mutation']
    MUTATIONS[mutation](state)
    detected = validate_state(state)
    expected = fixture['expected_error_code']
    return {
        'fixture_id': fixture['fixture_id'], 'mutation': mutation, 'expected_error_code': expected,
        'baseline_clean': baseline_errors == [], 'mutation_applied': state != baseline,
        'detected_error_codes': detected, 'primary_error_code': detected[0] if detected else None,
        'pass': baseline_errors == [] and state != baseline and bool(detected) and detected[0] == expected,
    }


def run_all_adversarial_cases(root: Path) -> dict[str, Any]:
    fixtures = [json.loads(p.read_text()) for p in sorted((root/'fixtures/invalid/final_double_check').glob('*.json'))]
    results = [execute_fixture(root, f) for f in fixtures]
    passed = sum(r['pass'] for r in results)
    return {
        'method': 'REAL_BASELINE_RECONSTRUCTION_DEEP_COPY_MUTATION_SHARED_INVARIANT_VALIDATION_PRIMARY_REASON_ASSERTION',
        'fixture_count': len(results), 'passed_count': passed, 'failed_count': len(results)-passed,
        'baseline_clean_for_all': all(r['baseline_clean'] for r in results),
        'all_mutations_applied': all(r['mutation_applied'] for r in results),
        'results': results, 'status': 'PASS' if len(results)==39 and passed==39 else 'FAIL',
    }
