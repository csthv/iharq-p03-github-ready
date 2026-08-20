from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path
from typing import Any

import yaml

ERROR_CODES = {
    'MISSING_LIMITATION',
    'CLAIM_CEILING_INFLATION',
    'MODE_B_UPGRADE',
    'EVIDENCE_MAP_UNAUTHORIZED_PLACEMENT',
    'CLAIM_VERSION_CONFLICT',
    'MISSING_ADVERSE_LINK',
    'LAYER10_WARNING_SUPPRESSION',
    'LAYER10_SOURCE_MUTATION',
    'LAYER10_EXPORT_DRIFT',
    'SCIENTIFIC_SCOPE_VIOLATION',
    'PREMATURE_PHASE0_CLOSURE',
    'PREMATURE_PHASE1_AUTHORIZATION',
}

STANDARD_WARNING_TOKENS = {
    'mode b',
    'non-empirical',
    'python 3.13.5',
    'python 3.11',
    'python 3.12',
    'uv.lock',
    'a0-a13',
    'a14',
    'p0-gate-18',
    'phase 0 is not closed',
    'phase 1 is not authorized',
}


def load_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding='utf-8'))


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding='utf-8'))


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline='', encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def validate_adversarial_fixture(fixture: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    claim = fixture.get('claim', {})
    layer10 = fixture.get('layer10', {})
    card = fixture.get('card', {})
    view = fixture.get('view', {})
    export = fixture.get('export', {})
    ablation = fixture.get('ablation', {})
    closure = fixture.get('closure', {})

    if claim.get('decision') == 'APPROVE_WITH_QUALIFICATIONS' and not claim.get('mandatory_limitations'):
        errors.append('MISSING_LIMITATION')
    if 'scientifically validated' in str(claim.get('allowed_wording', '')).lower():
        errors.append('CLAIM_CEILING_INFLATION')
    if claim.get('timing_mode') == 'B' and claim.get('evidence_class') == 'CONFIRMATORY':
        errors.append('MODE_B_UPGRADE')
    if claim.get('decision') in {'BLOCK', 'REJECT'} and layer10.get('active'):
        errors.append('EVIDENCE_MAP_UNAUTHORIZED_PLACEMENT')
    if claim.get('lifecycle_status') == 'ACTIVE_CURRENT' and claim.get('claim_version') != fixture.get('current_version'):
        errors.append('CLAIM_VERSION_CONFLICT')
    if claim.get('requires_adverse') and not claim.get('adverse_links'):
        errors.append('MISSING_ADVERSE_LINK')
    if card and not card.get('mandatory_warnings'):
        errors.append('LAYER10_WARNING_SUPPRESSION')
    if view.get('source_count') is not None and view.get('displayed_count') != view.get('source_count'):
        errors.append('LAYER10_SOURCE_MUTATION')
    if export and not export.get('filter_id'):
        errors.append('LAYER10_EXPORT_DRIFT')
    if view.get('source_type') == 'READINESS_COUNT' and 'scientific' in str(view.get('metric_label', '')).lower():
        errors.append('SCIENTIFIC_SCOPE_VIOLATION')
    if ablation.get('id') == 'A14' and ablation.get('active'):
        errors.append('SCIENTIFIC_SCOPE_VIOLATION')
    if closure.get('phase0_closed') and closure.get('p0_gate_18') != 'PASS':
        errors.append('PREMATURE_PHASE0_CLOSURE')
    if closure.get('phase1_authorized'):
        errors.append('PREMATURE_PHASE1_AUTHORIZATION')
    return errors


def _verify_release_manifest(root: Path, rel: str) -> tuple[bool, list[str]]:
    path = root / rel
    obj = load_json(path)
    errors: list[str] = []
    for entry in obj['files']:
        fp = root / entry['path']
        if not fp.exists():
            errors.append(f"missing:{entry['path']}")
            continue
        if fp.stat().st_size != entry['bytes']:
            errors.append(f"size:{entry['path']}")
        if hashlib.sha256(fp.read_bytes()).hexdigest() != entry['sha256']:
            errors.append(f"hash:{entry['path']}")
    return not errors, errors


def audit_package(root: Path) -> dict[str, Any]:
    checks: dict[str, bool] = {}
    errors: list[str] = []

    l0 = root / 'reports/layer0/phase_00'
    em = root / 'reports/evidence_map/phase_00'
    l10 = root / 'reports/layer10/phase_00'
    audit = root / 'reports/phase_00_closure_bridge/final_independent_audit_R2'

    intake = load_yaml(l0 / 'claim_intake_register.yaml')['claims']
    dispositions = load_yaml(l0 / 'claim_disposition_register.yaml')['dispositions']
    rows = load_csv(em / 'claim_evidence_matrix.csv')
    source_inventory = load_yaml(l10 / 'layer10_source_inventory.yaml')
    view_catalog = load_yaml(l10 / 'layer10_view_catalog.yaml')['views']
    card_catalog = load_yaml(l10 / 'layer10_card_catalog.yaml')['cards']
    export_catalog = load_yaml(l10 / 'layer10_export_catalog.yaml')['exports']
    parity = load_yaml(l10 / 'layer10_warning_and_limitation_parity.yaml')
    handoff = load_yaml(root / 'reports/phase_00_closure_bridge/phase_0_layer0_evidence_map_layer10_handoff_R2.yaml')['phase_0_layer0_evidence_map_layer10_handoff']

    def add(name: str, condition: bool, message: str) -> None:
        checks[name] = bool(condition)
        if not condition:
            errors.append(message)

    add('claims_current_v2', len(intake) == 7 and len(dispositions) == 7 and all(x['claim_version'] == 'v2' for x in intake + dispositions), 'current claim versions are not all v2')
    add('all_qualified', all(d['decision'] == 'APPROVE_WITH_QUALIFICATIONS' for d in dispositions), 'disposition decision drift')
    add('wording_hashes', all(sha256_text(d['allowed_wording']) == d['allowed_wording_sha256'] for d in dispositions), 'allowed wording hash mismatch')
    add('stale_limitation_removed', all('P00-LIM-005' not in d['mandatory_limitations'] for d in dispositions), 'stale P00-LIM-005 remains current')
    add('current_limitation_present', all('P00-LIM-L0-001' in d['mandatory_limitations'] for d in dispositions if d['claim_id'] in {'P00-CLM-001','P00-CLM-003','P00-CLM-004','P00-CLM-005','P00-CLM-006'}), 'current closure limitation missing')
    add('evidence_map_current_rows', len(rows) == 7 and len({(r['claim_id'], r['claim_version']) for r in rows}) == 7 and all(r['claim_version'] == 'v2' for r in rows), 'Evidence Map current-version closure failure')
    disp_by_id = {d['claim_id']: d for d in dispositions}
    add('evidence_map_wording_hashes', all(r['allowed_wording_sha256'] == disp_by_id[r['claim_id']]['allowed_wording_sha256'] for r in rows), 'Evidence Map wording hash drift')
    add('evidence_map_release_joins', all(r['execution_release_id'] == 'P00-EXECUTION-RELEASE-R2' and r['analysis_release_id'] == 'P00-ANALYSIS-RELEASE-R2' for r in rows), 'Evidence Map release join drift')
    add('source_inventory_current', {s['source_id'] for s in source_inventory['sources']} >= {'P00-EXECUTION-RELEASE-R2','P00-ANALYSIS-RELEASE-R2','P00-LAYER0-RELEASE-R2','P00-EVIDENCE-MAP-RELEASE-R2'}, 'Layer10 source inventory stale')
    add('layer10_inventory', len(view_catalog) == len(card_catalog) == len(export_catalog) == 14, 'Layer10 inventory count mismatch')
    add('layer10_read_only', all(v['read_only'] and not v['recomputation_allowed'] for v in view_catalog), 'Layer10 read-only boundary failure')
    add('layer10_sources_current', all({'P00-LAYER0-RELEASE-R2','P00-EVIDENCE-MAP-RELEASE-R2'}.issubset(set(v['source_releases'])) for v in view_catalog), 'Layer10 view source release drift')
    card_text = '\n'.join((root / f"docs/layer10/phase_00/cards/{i:02d}_{c['view_id']}.md").read_text(encoding='utf-8', errors='ignore') if (root / f"docs/layer10/phase_00/cards/{i:02d}_{c['view_id']}.md").exists() else '' for i,c in enumerate(card_catalog,1)).lower()
    # Check each card file directly by catalog title because filenames are not always title-derived.
    missing_card_scope = []
    for path in sorted((root / 'docs/layer10/phase_00/cards').glob('*.md')):
        txt = path.read_text(encoding='utf-8').lower()
        if 'scope and material limits' not in txt:
            missing_card_scope.append(path.name)
    add('compact_card_scope_warnings', not missing_card_scope, f'compact cards missing scope warnings:{missing_card_scope}')
    add('warning_parity', parity['status'] == 'PASS' and parity['required_items'] == len(parity['parity_rows']) and all(r['status'] == 'PASS' for r in parity['parity_rows']), 'warning parity matrix failure')

    export_errors = []
    for entry in export_catalog:
        p = root / entry['output_path']
        if not p.exists():
            export_errors.append(f'missing:{entry["output_path"]}')
            continue
        obj = load_json(p)
        if obj.get('read_only') is not True or obj.get('recomputation_allowed') is not False:
            export_errors.append(f'readonly:{entry["output_path"]}')
        if obj.get('filter_id') != 'P00-FILTER-ALL-CURRENT-R2':
            export_errors.append(f'filter:{entry["output_path"]}')
        warnings = ' '.join(obj.get('warnings', [])).lower()
        for token in STANDARD_WARNING_TOKENS:
            if token not in warnings:
                export_errors.append(f'warning:{entry["output_path"]}:{token}')
    add('exports_read_only_and_warned', not export_errors, ';'.join(export_errors))

    add('closure_boundaries', handoff['closure']['p0_gate_18'] == 'NOT_DECIDED_BY_THIS_AUDIT' and handoff['closure']['phase0_closed'] is False and handoff['closure']['phase1_authorized'] is False, 'premature closure/authorization')
    add('report_noninterference', load_yaml(audit / 'report_noninterference_change_audit_R2.yaml')['analysis_release_changed'] is False, 'illegal analysis mutation')
    add('readjudication_complete', len(load_csv(audit / 'layer0_independent_readjudication_matrix_R2.csv')) == 7, 'readjudication matrix incomplete')
    add('evidence_map_audit_complete', len(load_csv(audit / 'evidence_map_closure_audit_R2.csv')) == 7, 'Evidence Map audit incomplete')
    add('layer10_audit_complete', len(load_csv(audit / 'layer10_source_value_read_only_audit_R2.csv')) == 14, 'Layer10 value audit incomplete')

    for rel in [
        'reports/layer0/phase_00/layer0_release_manifest.json',
        'reports/evidence_map/phase_00/evidence_map_release_manifest.json',
        'reports/layer10/phase_00/layer10_release_manifest.json',
    ]:
        ok, manifest_errors = _verify_release_manifest(root, rel)
        add(f'manifest:{Path(rel).name}', ok, f'{rel}:{manifest_errors}')

    # Adversarial fixtures must fail with their expected code.
    fixture_errors = []
    for p in sorted((root / 'fixtures/invalid/final_l0_emap_l10_audit').glob('*.json')):
        fixture = load_json(p)
        got = validate_adversarial_fixture(fixture)
        if fixture['expected_error_code'] not in got:
            fixture_errors.append(f'{p.name}:expected={fixture["expected_error_code"]}:got={got}')
    add('adversarial_fail_closed', not fixture_errors, ';'.join(fixture_errors))

    status = 'PASS' if not errors else 'FAIL'
    return {
        'validation_id': 'P00-L0-EMAP-L10-FINAL-AUDIT-VALIDATION-R2',
        'checks_passed': sum(checks.values()),
        'checks_total': len(checks),
        'checks': checks,
        'errors': errors,
        'status': status,
    }
