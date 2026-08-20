from __future__ import annotations

from pathlib import Path
from collections import Counter
import json
import numpy as np

from iharq.layer3_calibration_uncertainty import stages as st

AMENDMENT_ID = "P03-L3-IMPL-AMEND-NO-RULE-R1"
FAILURE_CODE_NO_RULE = "NO_LEGAL_THRESHOLD"
NO_RULE_MESSAGE = "No non-empty threshold satisfies the maximum-risk target"


def _is_no_rule_exception(exc: Exception) -> bool:
    return isinstance(exc, ValueError) and NO_RULE_MESSAGE in str(exc)


def _select_or_explicit_no_rule(feature_values, probabilities, labels, target, *, probability_atol):
    """Preserve select_rule semantics; convert only the expected unattainable-target
    exception into an explicit terminal result. Unexpected exceptions still raise."""
    try:
        selected = st.select_rule(
            feature_values,
            probabilities,
            labels,
            target,
            probability_atol=probability_atol,
        )
        return {
            "terminal_status": "SUCCESS",
            "failure_code": None,
            "no_rule": False,
            **selected,
        }
    except Exception as exc:
        if not _is_no_rule_exception(exc):
            raise
        curve_with_index = st.build_risk_coverage(
            feature_values,
            probabilities,
            labels,
            target,
            probability_atol=probability_atol,
        )
        candidates = [
            {k: v for k, v in row.items() if k != "point_index"}
            for row in curve_with_index
        ]
        nonempty = [row for row in candidates if row.get("risk") is not None]
        minimum = (
            min(
                nonempty,
                key=lambda row: (
                    float(row["risk"]),
                    -float(row["coverage"]),
                    float(row["threshold"]),
                ),
            )
            if nonempty else None
        )
        return {
            "terminal_status": "INELIGIBLE",
            "failure_code": FAILURE_CODE_NO_RULE,
            "no_rule": True,
            "rule": None,
            "rule_sha256": None,
            "selection_metrics": None,
            "candidate_count": len(candidates),
            "candidates": candidates,
            "minimum_nonempty_selection": minimum,
            "reason": NO_RULE_MESSAGE,
        }


def stage_14(ctx, out: Path, progress):
    config, protocol = st._config(ctx), st._protocol(ctx)
    atol = float(config["score_semantics"]["probability_atol"])
    selection_role = st._protocol_role(protocol, "threshold_selection")
    group_ids = list(st._group_ids(ctx))
    rows = []
    no_rule_count = 0
    for index, group_id in enumerate(group_ids, start=1):
        descriptor, scores, labels, metadata = st._load_group(ctx, group_id)
        del descriptor, scores
        selection_idx = st._role_indices(metadata, selection_role)
        if not len(selection_idx):
            raise st.GateBlocked("G03-14-A2-SELECT", "THRESHOLD_SELECTION_ROLE_MISSING", group_id)
        st.authorize_view(
            operation="select_threshold",
            source_role=selection_role,
            requested_fields=["scores", "labels"],
            role_map=protocol["scientific"]["roles"]["role_map"],
            field_visibility=protocol["scientific"]["roles"]["field_visibility"],
        )
        probabilities = st._selected_probabilities(ctx, group_id)
        features, _ = st._features(ctx, group_id)
        target = dict(protocol["scientific"]["a2"]["target_profile"])
        target.update({
            "feature_id": "confidence",
            "operator": protocol["scientific"]["a2"]["operator"],
            "tie_policy": protocol["scientific"]["a2"]["tie_policy"],
        })
        selected = _select_or_explicit_no_rule(
            features["confidence"][selection_idx],
            probabilities[selection_idx],
            labels[selection_idx],
            target,
            probability_atol=atol,
        )
        if selected["terminal_status"] != "SUCCESS":
            no_rule_count += 1
        row = {
            "candidate_id": st.deterministic_id("P03-A2-CANDIDATE", {
                "group_id": group_id,
                "selection_role": selection_role,
                "target_profile_id": target["target_profile_id"],
                "terminal_status": selected["terminal_status"],
                "rule_sha256": selected.get("rule_sha256"),
            }),
            "group_id": group_id,
            "selection_role": selection_role,
            "test_role_used": False,
            "target_profile": target,
            "implementation_amendment_id": AMENDMENT_ID,
            **selected,
        }
        rows.append(row)
        st.write_json(out / "groups" / group_id / "a2_rule_candidate.json", row)
        progress(index, len(group_ids), group_id, no_rule_count, "IN_PROGRESS")
    st.write_jsonl(out / "a2_rule_candidates.jsonl", rows)
    success_count = sum(row["terminal_status"] == "SUCCESS" for row in rows)
    terminal_count = len(rows)
    return {
        "status": "PASS",
        "products": ["P03-PROD-026"],
        "a2_candidate_count": terminal_count,
        "a2_terminal_count": terminal_count,
        "a2_success_count": success_count,
        "a2_no_rule_count": no_rule_count,
        "a2_denominator_complete": terminal_count == len(group_ids),
        "a2_rule_candidates": "a2_rule_candidates.jsonl",
        "implementation_amendment_id": AMENDMENT_ID,
    }


def stage_15(ctx, out: Path, progress):
    config, protocol, contract = st._config(ctx), st._protocol(ctx), st._record_contract(ctx)
    atol = float(config["score_semantics"]["probability_atol"])
    eval_role = st._protocol_role(protocol, "evaluation")
    group_ids = list(st._group_ids(ctx))
    records, results = [], []
    no_rule_count = 0
    for index, group_id in enumerate(group_ids, start=1):
        candidate = json.loads(
            (st._stage_dir(ctx, "14") / "groups" / group_id / "a2_rule_candidate.json").read_text(encoding="utf-8")
        )
        descriptor, scores, labels, metadata = st._load_group(ctx, group_id)
        del scores
        eval_idx = st._role_indices(metadata, eval_role)

        if candidate.get("terminal_status") != "SUCCESS" or not isinstance(candidate.get("rule"), dict):
            no_rule_count += 1
            result = {
                "record_id": st.deterministic_id("P03-A2-NO-RULE-APPLICATION", {
                    "group_id": group_id,
                    "candidate_id": candidate.get("candidate_id"),
                    "evaluation_role": eval_role,
                }),
                "group_id": group_id,
                "selection_role": candidate.get("selection_role"),
                "application_role": eval_role,
                "terminal_status": "INELIGIBLE",
                "failure_code": candidate.get("failure_code") or FAILURE_CODE_NO_RULE,
                "reason": candidate.get("reason") or NO_RULE_MESSAGE,
                "rule": None,
                "accepted_count": None,
                "rejected_count": None,
                "coverage": None,
                "risk": None,
                "acceptance_mask_sha256": None,
                "test_metrics_computed": False,
                "synthetic_all_reject_used": False,
                "implementation_amendment_id": AMENDMENT_ID,
            }
            results.append(result)
            progress(index, len(group_ids), group_id, no_rule_count, "IN_PROGRESS")
            continue

        features, _ = st._features(ctx, group_id)
        probabilities = st._selected_probabilities(ctx, group_id)
        applied = st.apply_rule(
            features["confidence"][eval_idx],
            probabilities[eval_idx],
            labels[eval_idx],
            candidate["rule"],
            probability_atol=atol,
        )
        result = {
            "group_id": group_id,
            "selection_role": candidate["selection_role"],
            "application_role": eval_role,
            "terminal_status": "SUCCESS",
            "failure_code": None,
            "rule": candidate["rule"],
            **{k: v for k, v in applied.items() if k != "acceptance_mask"},
            "test_metrics_computed": True,
            "synthetic_all_reject_used": False,
            "implementation_amendment_id": AMENDMENT_ID,
        }
        payload = {
            "selective_id": st.deterministic_id("P03-A2", result),
            "ablation_id": "A2",
            "dataset_id": descriptor["dataset_id"],
            "model_id": descriptor["model_id"],
            "budget_id": descriptor["budget_id"],
            "split_id": descriptor["split_id"],
            "probability_source_id": f"{group_id}:selected",
            "uncertainty_source_id": f"{group_id}:confidence",
            "rule_family": "registered_confidence_floor",
            "threshold_registry_id": None,
            "selection_role": candidate["selection_role"],
            "application_role": eval_role,
            "operator": candidate["rule"]["operator"],
            "tie_policy": candidate["rule"]["tie_policy"],
            "accepted_count": applied["accepted_count"],
            "rejected_count": applied["rejected_count"],
            "coverage": applied["coverage"],
            "risk": applied["risk"],
            "utility": None,
            "acceptance_mask_sha256": applied["acceptance_mask_sha256"],
            "risk_coverage_curve_id": None,
        }
        record = st.make_record(
            "SelectivePredictionRecord",
            ctx,
            "L3-M04",
            payload,
            contract,
            source_artifact_ids=descriptor["source_partition_ids"],
        )
        records.append(record)
        result["record_id"] = record["record_id"]
        results.append(result)
        group_root = out / "groups" / group_id
        group_root.mkdir(parents=True, exist_ok=True)
        np.savez_compressed(group_root / "a2_acceptance_mask.npz", acceptance_mask=applied["acceptance_mask"])
        progress(index, len(group_ids), group_id, no_rule_count, "IN_PROGRESS")

    st.write_jsonl(out / "a2_selective_prediction_records.jsonl", records)
    st.write_jsonl(out / "a2_application_results.jsonl", results)
    terminal_count = len(results)
    return {
        "status": "PASS",
        "products": ["P03-PROD-027"],
        "a2_record_count": len(records),
        "a2_application_result_count": terminal_count,
        "a2_terminal_count": terminal_count,
        "a2_no_rule_count": no_rule_count,
        "a2_denominator_complete": terminal_count == len(group_ids),
        "a2_selective_prediction_records": "a2_selective_prediction_records.jsonl",
        "a2_application_results": "a2_application_results.jsonl",
        "implementation_amendment_id": AMENDMENT_ID,
    }


def stage_16(ctx, out: Path, progress):
    config, protocol, contract = st._config(ctx), st._protocol(ctx), st._record_contract(ctx)
    atol = float(config["score_semantics"]["probability_atol"])
    selection_role = st._protocol_role(protocol, "threshold_selection")
    eval_role = st._protocol_role(protocol, "evaluation")
    records, rule_rows = [], []
    curve_stream = st.AtomicJsonlCsvStream(
        out / "risk_coverage_curve_source.jsonl",
        out / "risk_coverage_curve_source.csv",
        ["curve_id", "group_id", "feature_id", "role", "point_index", "threshold", "accepted_count", "rejected_count", "coverage", "risk"],
    )
    feature_profiles = protocol["scientific"]["a3"]["feature_profiles"]
    group_ids = list(st._group_ids(ctx))
    total = len(group_ids) * len(feature_profiles)
    completed = 0
    no_rule_count = 0
    ineligible_count = 0
    try:
        for group_id in group_ids:
            descriptor, scores, labels, metadata = st._load_group(ctx, group_id)
            del scores
            selection_idx = st._role_indices(metadata, selection_role)
            eval_idx = st._role_indices(metadata, eval_role)
            probabilities = st._selected_probabilities(ctx, group_id)
            features, feature_index = st._features(ctx, group_id)
            for feature_profile in feature_profiles:
                completed += 1
                feature_id = str(feature_profile["feature_id"])
                if feature_id not in features:
                    ineligible_count += 1
                    rule_rows.append({
                        "record_id": st.deterministic_id("P03-A3-FEATURE-UNAVAILABLE", {"group_id": group_id, "feature_id": feature_id}),
                        "group_id": group_id,
                        "feature_id": feature_id,
                        "selection_role": selection_role,
                        "application_role": eval_role,
                        "terminal_status": "INELIGIBLE",
                        "failure_code": "FEATURE_UNAVAILABLE",
                        "reason": "FEATURE_UNAVAILABLE",
                        "rule": None,
                        "rule_sha256": None,
                        "application": None,
                        "curve_id": None,
                        "implementation_amendment_id": AMENDMENT_ID,
                    })
                    progress(completed, total, f"{group_id}:{feature_id}", ineligible_count + no_rule_count, "IN_PROGRESS")
                    continue

                target = dict(protocol["scientific"]["a3"]["working_points"])
                target.update({
                    "feature_id": feature_id,
                    "operator": feature_profile["operator"],
                    "tie_policy": feature_profile["tie_policy"],
                })
                selected = _select_or_explicit_no_rule(
                    features[feature_id][selection_idx],
                    probabilities[selection_idx],
                    labels[selection_idx],
                    target,
                    probability_atol=atol,
                )
                selection_curve = [
                    {"point_index": point_index, **row}
                    for point_index, row in enumerate(selected["candidates"])
                ]
                eval_curve = st.build_risk_coverage(
                    features[feature_id][eval_idx],
                    probabilities[eval_idx],
                    labels[eval_idx],
                    target,
                    probability_atol=atol,
                )
                curve_identity = {
                    "group": group_id,
                    "feature": feature_id,
                    "target_profile_id": target["target_profile_id"],
                    "terminal_status": selected["terminal_status"],
                    "rule_sha256": selected.get("rule_sha256"),
                }
                curve_id = st.deterministic_id("P03-A3-CURVE", curve_identity)
                for row in selection_curve:
                    curve_stream.write({"curve_id": curve_id, "group_id": group_id, "feature_id": feature_id, "role": selection_role, **row})
                for row in eval_curve:
                    curve_stream.write({"curve_id": curve_id, "group_id": group_id, "feature_id": feature_id, "role": eval_role, **row})

                if selected["terminal_status"] != "SUCCESS":
                    no_rule_count += 1
                    rule_row = {
                        "record_id": st.deterministic_id("P03-A3-NO-RULE", curve_identity),
                        "group_id": group_id,
                        "feature_id": feature_id,
                        "selection_role": selection_role,
                        "application_role": eval_role,
                        "terminal_status": "INELIGIBLE",
                        "failure_code": FAILURE_CODE_NO_RULE,
                        "reason": selected.get("reason") or NO_RULE_MESSAGE,
                        "rule": None,
                        "rule_sha256": None,
                        "application": None,
                        "curve_id": curve_id,
                        "minimum_nonempty_selection": selected.get("minimum_nonempty_selection"),
                        "alias_of_feature_id": feature_index[feature_id].get("alias_of_feature_id"),
                        "test_rule_application_performed": False,
                        "synthetic_all_reject_used": False,
                        "implementation_amendment_id": AMENDMENT_ID,
                    }
                    rule_rows.append(rule_row)
                    progress(completed, total, f"{group_id}:{feature_id}", ineligible_count + no_rule_count, "IN_PROGRESS")
                    continue

                applied = st.apply_rule(
                    features[feature_id][eval_idx],
                    probabilities[eval_idx],
                    labels[eval_idx],
                    selected["rule"],
                    probability_atol=atol,
                )
                rule_row = {
                    "group_id": group_id,
                    "feature_id": feature_id,
                    "selection_role": selection_role,
                    "application_role": eval_role,
                    "terminal_status": "SUCCESS",
                    "failure_code": None,
                    "rule": selected["rule"],
                    "rule_sha256": selected["rule_sha256"],
                    "application": {k: v for k, v in applied.items() if k != "acceptance_mask"},
                    "curve_id": curve_id,
                    "alias_of_feature_id": feature_index[feature_id].get("alias_of_feature_id"),
                    "test_rule_application_performed": True,
                    "synthetic_all_reject_used": False,
                    "implementation_amendment_id": AMENDMENT_ID,
                }
                payload = {
                    "selective_id": st.deterministic_id("P03-A3", rule_row),
                    "ablation_id": "A3",
                    "dataset_id": descriptor["dataset_id"],
                    "model_id": descriptor["model_id"],
                    "budget_id": descriptor["budget_id"],
                    "split_id": descriptor["split_id"],
                    "probability_source_id": f"{group_id}:selected",
                    "uncertainty_source_id": f"{group_id}:{feature_id}",
                    "rule_family": "feature_specific_selective_prediction",
                    "threshold_registry_id": None,
                    "selection_role": selection_role,
                    "application_role": eval_role,
                    "operator": selected["rule"]["operator"],
                    "tie_policy": selected["rule"]["tie_policy"],
                    "accepted_count": applied["accepted_count"],
                    "rejected_count": applied["rejected_count"],
                    "coverage": applied["coverage"],
                    "risk": applied["risk"],
                    "utility": None,
                    "acceptance_mask_sha256": applied["acceptance_mask_sha256"],
                    "risk_coverage_curve_id": curve_id,
                }
                record = st.make_record(
                    "SelectivePredictionRecord",
                    ctx,
                    "L3-M04",
                    payload,
                    contract,
                    source_artifact_ids=descriptor["source_partition_ids"],
                )
                records.append(record)
                rule_row["record_id"] = record["record_id"]
                rule_rows.append(rule_row)
                group_root = out / "groups" / group_id
                group_root.mkdir(parents=True, exist_ok=True)
                np.savez_compressed(group_root / f"a3_{feature_id}_acceptance_mask.npz", acceptance_mask=applied["acceptance_mask"])
                progress(completed, total, f"{group_id}:{feature_id}", ineligible_count + no_rule_count, "IN_PROGRESS")
    except Exception:
        curve_stream.preserve_partial()
        raise
    else:
        curve_stream.commit()

    st.write_jsonl(out / "a3_selective_prediction_records.jsonl", records)
    st.write_jsonl(out / "a3_rule_candidates.jsonl", rule_rows)
    terminal_count = len(rule_rows)
    return {
        "status": "PASS",
        "products": ["P03-PROD-028", "P03-PROD-029"],
        "a3_record_count": len(records),
        "curve_point_count": curve_stream.row_count,
        "a3_rule_candidate_count": terminal_count,
        "a3_terminal_count": terminal_count,
        "a3_no_rule_count": no_rule_count,
        "a3_other_ineligible_count": ineligible_count,
        "a3_denominator_complete": terminal_count == total,
        "a3_selective_prediction_records": "a3_selective_prediction_records.jsonl",
        "risk_coverage_curve_source": "risk_coverage_curve_source.jsonl",
        "implementation_amendment_id": AMENDMENT_ID,
    }


def stage_17(ctx, out: Path, progress):
    protocol = st._protocol(ctx)
    store = st.ThresholdStore(out / "threshold_registry")
    candidates = []
    a2 = st._read_jsonl(st._stage_dir(ctx, "14") / "a2_rule_candidates.jsonl")
    a3 = st._read_jsonl(st._stage_dir(ctx, "16") / "a3_rule_candidates.jsonl")
    skipped = []
    for row in a2:
        if row.get("terminal_status") == "SUCCESS" and isinstance(row.get("rule"), dict):
            candidates.append((row["group_id"], "A2", row["rule"], row["selection_role"]))
        else:
            skipped.append({"group_id": row.get("group_id"), "ablation_id": "A2", "feature_id": "confidence", "terminal_status": row.get("terminal_status"), "failure_code": row.get("failure_code")})
    for row in a3:
        if row.get("terminal_status") == "SUCCESS" and isinstance(row.get("rule"), dict):
            candidates.append((row["group_id"], "A3", row["rule"], row["selection_role"]))
        else:
            skipped.append({"group_id": row.get("group_id"), "ablation_id": "A3", "feature_id": row.get("feature_id"), "terminal_status": row.get("terminal_status"), "failure_code": row.get("failure_code")})

    records = []
    for index, (group_id, ablation, rule, selection_role) in enumerate(candidates, start=1):
        descriptor, _, _, _ = st._load_group(ctx, group_id)
        candidate = {
            "threshold_version": "1.0.0",
            "ablation_id": ablation,
            "feature_id": rule["feature_id"],
            "probability_source_id": f"{group_id}:selected",
            "selection_dataset_id": descriptor["dataset_id"],
            "selection_budget_id": descriptor["budget_id"],
            "selection_split_id": descriptor["split_id"],
            "selection_role": selection_role,
            "target_profile_id": rule["target_profile_id"],
            "operator": rule["operator"],
            "threshold_value": rule["threshold_value"],
            "tie_policy": rule["tie_policy"],
            "applicability": {
                "dataset_id": descriptor["dataset_id"],
                "model_id": descriptor["model_id"],
                "budget_id": descriptor["budget_id"],
                "split_id": descriptor["split_id"],
            },
            "permissions": {
                "consumers": protocol["scientific"]["threshold_registry"]["permitted_consumers"],
                "labels_exported": False,
            },
            "effective_from": ctx.created_at_utc,
            "effective_until": None,
            "supersession_reason": None,
        }
        records.append(store.register(candidate))
        progress(index, len(candidates), records[-1]["threshold_id"], len(skipped), "IN_PROGRESS")

    st.write_jsonl(out / "threshold_registry_records.jsonl", records)
    st.write_jsonl(out / "threshold_registry_no_rule_skips.jsonl", skipped)
    return {
        "status": "PASS",
        "products": ["P03-PROD-030", "P03-PROD-031"],
        "threshold_record_count": len(records),
        "threshold_no_rule_skip_count": len(skipped),
        "threshold_registry_records": "threshold_registry_records.jsonl",
        "threshold_registry_index": "threshold_registry/threshold_registry_index.json",
        "threshold_registry_no_rule_skips": "threshold_registry_no_rule_skips.jsonl",
        "implementation_amendment_id": AMENDMENT_ID,
    }


def stage_18(ctx, out: Path, progress):
    config, protocol = st._config(ctx), st._protocol(ctx)
    atol = float(config["score_semantics"]["probability_atol"])
    eval_role = st._protocol_role(protocol, "evaluation")
    group_ids = list(st._group_ids(ctx))
    rows = []
    a2_results = {
        row["group_id"]: row
        for row in st._read_jsonl(st._stage_dir(ctx, "15") / "a2_application_results.jsonl")
    }
    a3_results = st._read_jsonl(st._stage_dir(ctx, "16") / "a3_rule_candidates.jsonl")
    if set(a2_results) != set(group_ids):
        raise st.GateBlocked("G03-18-MATCHED", "A2_TERMINAL_DENOMINATOR_INCOMPLETE", f"observed={len(a2_results)}, expected={len(group_ids)}")

    for index, group_id in enumerate(group_ids, start=1):
        descriptor, _, labels, metadata = st._load_group(ctx, group_id)
        eval_idx = st._role_indices(metadata, eval_role)
        probabilities = st._selected_probabilities(ctx, group_id)
        a1 = st.selective_risk(
            probabilities[eval_idx],
            labels[eval_idx],
            np.ones(len(eval_idx), dtype=bool),
            probability_atol=atol,
        )
        base = {
            "dataset_id": descriptor["dataset_id"],
            "model_id": descriptor["model_id"],
            "budget_id": descriptor["budget_id"],
            "split_id": descriptor["split_id"],
            "eligible_set_sha256": st.sha256_json([metadata[i]["record_id"] for i in eval_idx]),
            "probability_source_id": f"{group_id}:selected",
            "implementation_amendment_id": AMENDMENT_ID,
        }
        rows.append({
            **base,
            "record_id": st.deterministic_id("MATCH-A1", base),
            "ablation_id": "A1",
            "terminal_status": "SUCCESS",
            "failure_code": None,
            "coverage": a1["coverage"],
            "risk": a1["risk"],
        })
        a2 = a2_results[group_id]
        rows.append({
            **base,
            "record_id": a2.get("record_id") or st.deterministic_id("MATCH-A2", a2),
            "ablation_id": "A2",
            "terminal_status": a2.get("terminal_status", "SUCCESS"),
            "failure_code": a2.get("failure_code"),
            "coverage": a2.get("coverage"),
            "risk": a2.get("risk"),
        })
        children = [row for row in a3_results if row.get("group_id") == group_id]
        for a3 in children:
            application = a3.get("application") if isinstance(a3.get("application"), dict) else {}
            rows.append({
                **base,
                "record_id": a3.get("record_id") or st.deterministic_id("MATCH-A3", a3),
                "ablation_id": "A3",
                "feature_id": a3.get("feature_id"),
                "terminal_status": a3.get("terminal_status", "SUCCESS"),
                "failure_code": a3.get("failure_code"),
                "coverage": application.get("coverage"),
                "risk": application.get("risk"),
            })
        progress(index, len(group_ids), group_id, 0, "IN_PROGRESS")

    profile = dict(protocol["scientific"]["matching"])
    profile["required_ablations"] = ["A1", "A2", "A3"]
    expanded = []
    for group_id in group_ids:
        group_rows = [row for row in rows if row["probability_source_id"] == f"{group_id}:selected"]
        children = [row for row in group_rows if row["ablation_id"] == "A3"]
        for child in children:
            feature = child.get("feature_id")
            for row in group_rows:
                if row["ablation_id"] in {"A1", "A2"}:
                    expanded.append({**row, "feature_id": feature})
            expanded.append(child)
    profile["matching_key_fields"] = list(profile["matching_key_fields"]) + ["feature_id"]
    matched = st.build_matched_operating_points(expanded, profile)
    if matched["unmatched"]:
        raise st.GateBlocked("G03-18-MATCHED", "UNMATCHED_A1_A2_A3", json.dumps(matched["unmatched"][:5]))

    row_by_id = {row["record_id"]: row for row in expanded}
    comparable = 0
    ineligible = 0
    for item in matched["matched"]:
        members = [row_by_id.get(rid) for rid in item.get("member_ids", {}).values()]
        members = [row for row in members if row is not None]
        bad = [row for row in members if row.get("terminal_status") != "SUCCESS"]
        if bad:
            ineligible += 1
            item["comparability_status"] = "INELIGIBLE"
            item["terminal_status"] = "INELIGIBLE"
            item["failure_codes"] = sorted({str(row.get("failure_code") or "NON_SUCCESS_TERMINAL") for row in bad})
        else:
            comparable += 1
            item["comparability_status"] = "COMPARABLE"
            item["terminal_status"] = "SUCCESS"
            item["failure_codes"] = []
        item["implementation_amendment_id"] = AMENDMENT_ID

    matched["structural_match_count"] = len(matched["matched"])
    matched["comparable_match_count"] = comparable
    matched["ineligible_match_count"] = ineligible
    matched["implementation_amendment_id"] = AMENDMENT_ID
    st.write_json(out / "matched_operating_points.json", matched)
    st.write_jsonl(out / "matched_operating_point_rows.jsonl", expanded)
    return {
        "status": "PASS",
        "products": ["P03-PROD-032"],
        "matched_set_count": len(matched["matched"]),
        "comparable_set_count": comparable,
        "ineligible_set_count": ineligible,
        "unmatched_count": len(matched["unmatched"]),
        "matched_operating_points": "matched_operating_points.json",
        "implementation_amendment_id": AMENDMENT_ID,
    }


def stage_20(ctx, out: Path, progress):
    attempts = st._read_jsonl(st._stage_dir(ctx, "11") / "calibration_attempt_ledger.jsonl")
    conditional = st._read_jsonl(st._stage_dir(ctx, "13") / "conditional_uncertainty_attempts.jsonl")
    sparse = st._read_jsonl(st._stage_dir(ctx, "19") / "sparse_support_warnings.jsonl")
    leakage = st._read_jsonl(st._stage_dir(ctx, "08") / "leakage_warning_records.jsonl")
    a2_candidates = st._read_jsonl(st._stage_dir(ctx, "14") / "a2_rule_candidates.jsonl")
    a2_applications = st._read_jsonl(st._stage_dir(ctx, "15") / "a2_application_results.jsonl")
    a3_candidates = st._read_jsonl(st._stage_dir(ctx, "16") / "a3_rule_candidates.jsonl")
    intake = json.loads((st._stage_dir(ctx, "04") / "p03_intake_ledger.json").read_text(encoding="utf-8"))
    negative = []

    for row in attempts:
        if row["terminal_status"] != "SUCCESS":
            negative.append({
                "source": row["attempt_id"],
                "failure_class": "failed calibration" if row["terminal_status"] == "FAILED" else "conditional skip",
                "terminal_status": row["terminal_status"],
                "reason": row.get("reason"),
            })
    negative.extend({
        "source": row["group_id"] + ":" + row["feature_id"],
        "failure_class": "conditional skip",
        "terminal_status": row.get("status"),
        "reason": row.get("reason"),
    } for row in conditional if row.get("status") != "ELIGIBLE")
    negative.extend({
        "source": row["group_source_id"],
        "failure_class": "sparse group",
        "terminal_status": "DIAGNOSTIC_ONLY",
        "reason": "SPARSE_GROUP_SUPPORT",
    } for row in sparse)
    negative.extend({
        "source": row["warning_id"],
        "failure_class": "invalid split",
        "terminal_status": "BLOCKED",
        "reason": row["illegal_use_code"],
    } for row in leakage)

    # Explicit A2/A3 no-rule and other terminal outcomes.
    for row in a2_candidates:
        if row.get("terminal_status") != "SUCCESS":
            negative.append({
                "source": f"{row.get('group_id')}:A2:confidence",
                "failure_class": "no threshold" if row.get("failure_code") == FAILURE_CODE_NO_RULE else "selective ineligible",
                "terminal_status": row.get("terminal_status"),
                "reason": row.get("failure_code") or row.get("reason"),
                "ablation_id": "A2",
                "feature_id": "confidence",
                "minimum_nonempty_selection": row.get("minimum_nonempty_selection"),
                "implementation_amendment_id": AMENDMENT_ID,
            })
    for row in a3_candidates:
        if row.get("terminal_status") != "SUCCESS":
            negative.append({
                "source": f"{row.get('group_id')}:A3:{row.get('feature_id')}",
                "failure_class": "no threshold" if row.get("failure_code") == FAILURE_CODE_NO_RULE else "selective ineligible",
                "terminal_status": row.get("terminal_status"),
                "reason": row.get("failure_code") or row.get("reason"),
                "ablation_id": "A3",
                "feature_id": row.get("feature_id"),
                "minimum_nonempty_selection": row.get("minimum_nonempty_selection"),
                "implementation_amendment_id": AMENDMENT_ID,
            })

    # Preserve every actual failed stage attempt, including the original Stage14
    # implementation failure that triggered this amendment.
    stage_failure_rows = []
    failure_root = ctx.run_root / "artifacts" / "negative_and_failed_results" / "phase_03" / "stage_failures"
    for path in sorted(failure_root.glob("stage_*_attempt_*.json")):
        receipt = json.loads(path.read_text(encoding="utf-8"))
        failure = receipt.get("failure") or {}
        row = {
            "source": path.relative_to(ctx.run_root).as_posix(),
            "failure_class": "stage execution failure",
            "terminal_status": receipt.get("status", "FAILED"),
            "reason": failure.get("reason_code") or failure.get("message"),
            "stage_id": receipt.get("stage_id"),
            "attempt": receipt.get("attempt"),
            "preserved_failed_attempt": True,
        }
        stage_failure_rows.append(row)
        negative.append(row)

    inherited_negative = []
    inherited_receipt = {
        "authoring_fixture": ctx.authoring_fixture,
        "source_run_id": intake["source_run_id"],
        "source_config_sha256": intake["source_config_sha256"],
        "objects": [],
    }
    if not ctx.authoring_fixture:
        config = st._config(ctx)
        locator = config["inputs"]["p02"]
        root = Path(st._stage_result(ctx, "03")["resolved_external_root"])
        diagnostic_rows = st._read_jsonl(root / locator["diagnostic_only_path"])
        failure_rows = st._read_jsonl(root / locator["failure_case_path"])
        for row in diagnostic_rows:
            inherited_negative.append({
                "source": row["record_id"], "source_phase": "P02", "source_ids": row.get("source_ids", []),
                "failure_class": "upstream diagnostic-only evidence", "terminal_status": "DIAGNOSTIC_ONLY",
                "reason": row.get("reason_code"), "allowed_consumers": row.get("allowed_consumers", []),
            })
        for row in failure_rows:
            inherited_negative.append({
                "source": row["record_id"], "source_phase": "P02", "source_ids": row.get("source_ids", []),
                "failure_class": str(row.get("failure_class", "upstream failure")), "terminal_status": "INHERITED_FAILURE",
                "reason": row.get("failure_code"), "evidence_consequence": row.get("evidence_consequence"),
            })
        for limitation in intake["limitations"]:
            inherited_negative.append({
                "source": limitation["limitation_id"], "source_phase": "P02", "source_ids": [],
                "failure_class": "persistent upstream limitation", "terminal_status": str(limitation["status_after_P02"]),
                "reason": limitation["tag"], "evidence_consequence": limitation["downstream_claim_impact"],
            })
        local_control_keys = {"downstream_readiness_contract_path", "persistent_limitations_path"}
        for key in (
            "a0_completion_path", "a4_completion_path", "baseline_metric_path", "diagnostic_only_path", "failure_case_path",
            "downstream_readiness_contract_path", "persistent_limitations_path",
        ):
            source_root = ctx.package_root if key in local_control_keys else root
            path = source_root / locator[key]
            inherited_receipt["objects"].append({
                "role": key, "path": locator[key], "bytes": path.stat().st_size, "sha256": st.sha256_file(path),
                "source": "BUNDLED_CUMULATIVE_P02_HANDOFF_AUTHORITY" if key in local_control_keys else "HF_FROZEN_P02_EXECUTION_SNAPSHOT",
            })
        inherited_receipt["ensemble_control_record_count"] = len(list((root / locator["ensemble_control_record_prefix"]).rglob("*.jsonl")))
        inherited_receipt["ensemble_control_manifest_count"] = len(list((root / locator["ensemble_control_manifest_prefix"]).rglob("*.json")))
    else:
        inherited_negative.extend({
            "source": row["limitation_id"], "source_phase": "P02", "source_ids": [],
            "failure_class": "fixture limitation", "terminal_status": row["status_after_P02"], "reason": row["tag"],
        } for row in intake["limitations"])
    negative.extend(inherited_negative)

    disposition_complete = bool(st._stage_result(ctx, "07")["disposition_complete"])
    upstream_counts = intake["upstream_record_counts"]
    inherited_count_complete = ctx.authoring_fixture or (
        sum(row["failure_class"] == "upstream diagnostic-only evidence" for row in inherited_negative) == int(upstream_counts["diagnostic_only_records"])
        and sum(row["terminal_status"] == "INHERITED_FAILURE" for row in inherited_negative) == int(upstream_counts["failure_case_records"])
        and sum(row["failure_class"] == "persistent upstream limitation" for row in inherited_negative) == len(intake["limitations"])
    )
    group_count = int(st._stage_result(ctx, "07")["group_count"])
    a2_terminal_complete = len(a2_candidates) == group_count and len(a2_applications) == group_count
    expected_a3 = group_count * len(st._protocol(ctx)["scientific"]["a3"]["feature_profiles"])
    a3_terminal_complete = len(a3_candidates) == expected_a3
    threshold_expected = (
        sum(row.get("terminal_status") == "SUCCESS" for row in a2_candidates)
        + sum(row.get("terminal_status") == "SUCCESS" for row in a3_candidates)
    )
    threshold_complete = int(st._stage_result(ctx, "17")["threshold_record_count"]) == threshold_expected
    denominator_complete = bool(
        disposition_complete
        and inherited_count_complete
        and len(attempts) == st._stage_result(ctx, "11")["attempt_count"]
        and a2_terminal_complete
        and a3_terminal_complete
        and threshold_complete
    )
    if not denominator_complete:
        raise st.GateBlocked(
            "G03-20-NEGATIVE",
            "NEGATIVE_EVIDENCE_DENOMINATOR_INCOMPLETE",
            json.dumps({
                "disposition": disposition_complete,
                "inherited": inherited_count_complete,
                "a2_terminal": a2_terminal_complete,
                "a3_terminal": a3_terminal_complete,
                "threshold_complete": threshold_complete,
            }, sort_keys=True),
        )

    st.write_jsonl(out / "negative_result_notes.jsonl", negative)
    st.write_jsonl(out / "inherited_p02_negative_and_limitation_records.jsonl", inherited_negative)
    st.write_json(out / "p02_inherited_contract_receipt.json", inherited_receipt)
    st.write_json(out / "failure_taxonomy_summary.json", {
        "planned_calibration_attempts": len(attempts),
        "terminal_calibration_attempts": len(attempts),
        "negative_count": len(negative),
        "inherited_p02_negative_count": len(inherited_negative),
        "preserved_stage_failure_count": len(stage_failure_rows),
        "a2_no_rule_count": sum(row.get("failure_code") == FAILURE_CODE_NO_RULE for row in a2_candidates),
        "a3_no_rule_count": sum(row.get("failure_code") == FAILURE_CODE_NO_RULE for row in a3_candidates),
        "terminal_counts": dict(Counter(row["terminal_status"] for row in negative)),
        "denominator_complete": denominator_complete,
        "upstream_prediction_disposition_complete": disposition_complete,
        "inherited_record_counts_complete": inherited_count_complete,
        "a2_terminal_denominator_complete": a2_terminal_complete,
        "a3_terminal_denominator_complete": a3_terminal_complete,
        "threshold_registration_denominator_complete": threshold_complete,
        "failed_attempts_deleted": 0,
        "implementation_amendment_id": AMENDMENT_ID,
    })
    progress(1, 1, "negative/failure closure", 0, "COMPLETE")
    return {
        "status": "PASS",
        "products": ["P03-PROD-035", "P03-PROD-036", "P03-PROD-037"],
        "negative_result_count": len(negative),
        "inherited_p02_negative_count": len(inherited_negative),
        "preserved_stage_failure_count": len(stage_failure_rows),
        "a2_no_rule_count": sum(row.get("failure_code") == FAILURE_CODE_NO_RULE for row in a2_candidates),
        "a3_no_rule_count": sum(row.get("failure_code") == FAILURE_CODE_NO_RULE for row in a3_candidates),
        "denominator_complete": denominator_complete,
        "negative_result_notes": "negative_result_notes.jsonl",
        "p02_inherited_contract_receipt": "p02_inherited_contract_receipt.json",
        "implementation_amendment_id": AMENDMENT_ID,
    }


def stage_23(ctx, out: Path, progress):
    progress(0, 6, "stage/gate ledger", 0, "IN_PROGRESS")
    checkpoints = st._checkpoint_rows(ctx)
    expected_complete = {f"{i:02d}" for i in range(23)}
    complete = {row["stage_id"] for row in checkpoints if row["status"] == "COMPLETE"}
    if complete != expected_complete:
        raise st.GateBlocked("G03-23-SUFFICIENCY", "PRIOR_STAGE_TERMINALITY_INCOMPLETE", f"missing={sorted(expected_complete-complete)}")
    st.write_json(out / "stage_ledger.json", {"run_id": ctx.run_id, "stages": checkpoints, "complete_count": len(complete)})
    gate_rows = [{"gate_id": row["gate_id"], "stage_id": row["stage_id"], "decision": "PASS", "receipt_sha256": st.sha256_json(row)} for row in checkpoints]
    st.write_jsonl(out / "gate_decision_report.jsonl", gate_rows)
    progress(1, 6, "product completeness", 0, "IN_PROGRESS")
    traceability = st._artifact_traceability(ctx, 22)
    realized = {row["product_id"] for row in traceability}
    required_before_24 = {f"P03-PROD-{i:03d}" for i in range(1, 58)} | {"P03-PROD-062", "P03-PROD-063"}
    realized.update({"P03-PROD-051", "P03-PROD-052", "P03-PROD-053", "P03-PROD-054", "P03-PROD-055", "P03-PROD-056", "P03-PROD-057"})
    missing = sorted(required_before_24 - realized)
    if missing:
        raise st.GateBlocked("G03-23-SUFFICIENCY", "EXPECTED_PRODUCT_WRITER_MISSING", ",".join(missing))

    progress(2, 6, "ablation closure", 0, "IN_PROGRESS")
    a1 = st._stage_result(ctx, "11")["selection_count"] > 0
    a2 = bool(st._stage_result(ctx, "15").get("a2_denominator_complete"))
    a3 = bool(st._stage_result(ctx, "16").get("a3_denominator_complete"))
    intake = st._stage_result(ctx, "04")
    a0 = bool(intake["a0_validated"])
    a4 = bool(intake["a4_validated"])
    if not (a0 and a1 and a2 and a3 and a4):
        raise st.GateBlocked("G03-23-SUFFICIENCY", "ABLATION_CLOSURE_INCOMPLETE", f"A0={a0},A1={a1},A2={a2},A3={a3},A4={a4}")

    progress(3, 6, "handoff closure", 0, "IN_PROGRESS")
    p04_path = st._stage_dir(ctx, "22") / "p03_to_p04_handoff_manifest.json"
    if not p04_path.is_file() or not st._stage_result(ctx, "22")["consumer_handoff_count"]:
        raise st.GateBlocked("G03-23-SUFFICIENCY", "DOWNSTREAM_HANDOFF_INCOMPLETE", "P04/later handoffs missing")
    required_outputs = [
        st._stage_dir(ctx, "04") / "p03_intake_ledger.json",
        st._stage_dir(ctx, "07") / "upstream_prediction_disposition.jsonl",
        st._stage_dir(ctx, "08") / "split_integrity_reports.jsonl",
        st._stage_dir(ctx, "09") / "calibration_eligibility_table.jsonl",
        st._stage_dir(ctx, "10") / "identity_calibration_records.jsonl",
        st._stage_dir(ctx, "11") / "calibration_attempt_ledger.jsonl",
        st._stage_dir(ctx, "12") / "reliability_audit_reports.jsonl",
        st._stage_dir(ctx, "13") / "uncertainty_records.jsonl",
        st._stage_dir(ctx, "15") / "a2_selective_prediction_records.jsonl",
        st._stage_dir(ctx, "16") / "a3_selective_prediction_records.jsonl",
        st._stage_dir(ctx, "17") / "threshold_registry_records.jsonl",
        st._stage_dir(ctx, "18") / "matched_operating_points.json",
        st._stage_dir(ctx, "19") / "group_budget_audit.jsonl",
        st._stage_dir(ctx, "20") / "negative_result_notes.jsonl",
        st._stage_dir(ctx, "21") / "artifact_traceability.csv",
        st._stage_dir(ctx, "22") / "p03_to_p04_handoff_manifest.json",
    ]
    missing_outputs = [path.relative_to(ctx.run_root).as_posix() for path in required_outputs if not path.is_file()]
    disagreement = st._stage_result(ctx, "13")
    disagreement_accounted = int(disagreement["member_disagreement_accounted_group_count"]) == int(st._stage_result(ctx, "07")["group_count"])
    score_semantics_complete = int(st._stage_result(ctx, "09")["eligibility_count"]) == int(st._stage_result(ctx, "07")["group_count"])
    failure_denominator_complete = bool(st._stage_result(ctx, "20")["denominator_complete"])
    handoff_complete = bool(st._stage_result(ctx, "22")["consumer_handoff_count"])
    artifacts_complete = not missing_outputs and failure_denominator_complete and disagreement_accounted
    if not artifacts_complete:
        raise st.GateBlocked(
            "G03-23-SUFFICIENCY",
            "REQUIRED_ARTIFACT_OR_CONDITIONAL_TERMINAL_MISSING",
            json.dumps({"missing": missing_outputs, "failure_denominator": failure_denominator_complete, "disagreement_accounted": disagreement_accounted}, sort_keys=True),
        )
    resource = {
        "status": "PASS", "scientific_worker_processes": 1, "numerical_threads": 1,
        "heartbeat_seconds": st._config(ctx)["execution"]["heartbeat_seconds"],
        "resource_reduction_applied": False, "authoring_fixture": ctx.authoring_fixture,
    }
    readiness = {
        "status": "READY" if not ctx.authoring_fixture else "NON_SCIENTIFIC_AUTHORING_VALIDATION_COMPLETE",
        "P02_contract_validated": bool(intake["p02_contract_complete"]),
        "score_semantics_complete": score_semantics_complete,
        "class_order_complete": score_semantics_complete,
        "leakage_guards_pass": st._stage_result(ctx, "08")["leakage_warning_count"] == 0,
        "A1_complete": a1, "A2_complete": a2, "A3_complete": a3, "A2_A3_distinct": True,
        "A2_successful_rule_groups": st._stage_result(ctx, "14").get("a2_success_count"),
        "A2_explicit_no_rule_groups": st._stage_result(ctx, "14").get("a2_no_rule_count"),
        "A3_successful_rule_children": st._stage_result(ctx, "16").get("a3_record_count"),
        "A3_explicit_no_rule_children": st._stage_result(ctx, "16").get("a3_no_rule_count"),
        "A0_inherited": a0, "A4_inherited": a4,
        "A4_disagreement_eligible_groups": disagreement["member_disagreement_eligible_count"],
        "A4_disagreement_ineligible_groups": disagreement["member_disagreement_ineligible_count"],
        "A4_disagreement_all_groups_accounted": disagreement_accounted,
        "A14_absent": True, "products_expected": 65, "products_pre_export_realized": len(realized), "literal_secrets": 0,
        "implementation_amendment_id": AMENDMENT_ID,
    }
    sufficiency = {
        "status": "PASS",
        "all_prior_stages_terminal": complete == expected_complete,
        "every_required_artifact_produced_or_lawfully_terminal": artifacts_complete,
        "every_required_ablation_ran": all((a0, a1, a2, a3, a4)),
        "failures_persisted": failure_denominator_complete,
        "downstream_handoffs_created": handoff_complete,
        "manifests_complete": not missing,
        "required_output_missing": missing_outputs,
        "checksums_pending_stage_24": True,
        "secret_scan_pending_stage_24": True,
        "authoring_fixture": ctx.authoring_fixture,
        "implementation_amendment_id": AMENDMENT_ID,
    }
    execution_manifest = {
        "run_id": ctx.run_id,
        "immutable_fingerprint": ctx.immutable_fingerprint,
        "runtime_implementation_amendment_id": AMENDMENT_ID,
        "stage_count_before_export": len(checkpoints),
        "product_ids_before_export": sorted(realized),
        "readiness": readiness,
        "evidence_sufficiency": sufficiency,
    }
    st.write_json(out / "execution_manifest.json", execution_manifest)
    st.write_json(out / "readiness_report.json", readiness)
    st.write_json(out / "evidence_sufficiency_decision.json", sufficiency)
    st.write_json(out / "resource_qualification_report.json", resource)
    progress(6, 6, "evidence sufficiency PASS", 0, "COMPLETE")
    return {
        "status": "PASS",
        "products": ["P03-PROD-051", "P03-PROD-052", "P03-PROD-053", "P03-PROD-054", "P03-PROD-055", "P03-PROD-056", "P03-PROD-057"],
        "prior_stage_count": len(checkpoints),
        "pre_export_product_count": len(realized),
        "readiness_report": "readiness_report.json",
        "evidence_sufficiency_decision": "evidence_sufficiency_decision.json",
        "implementation_amendment_id": AMENDMENT_ID,
    }
