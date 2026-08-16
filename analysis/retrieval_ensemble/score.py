def _is_correct_catch(expected: str, observed: str) -> bool:
    return expected in {"reject", "narrow"} and observed == expected


def score_cases(labels: dict, outcomes: dict) -> dict:
    benchmark_ids = [
        case_id
        for case_id, metadata in labels.items()
        if metadata["expected_action"] in {"reject", "narrow"}
    ]

    metrics = {}
    for condition, condition_outcomes in outcomes.items():
        caught = [
            case_id
            for case_id in benchmark_ids
            if _is_correct_catch(
                labels[case_id]["expected_action"],
                condition_outcomes.get(case_id, "missing"),
            )
        ]
        denominator = len(benchmark_ids)
        metrics[condition] = {
            "caught": caught,
            "count": len(caught),
            "denominator": denominator,
            "catch_rate": (len(caught) / denominator) if denominator else 0.0,
        }

    exa_caught = set(metrics.get("exa", {}).get("caught", []))
    parallel_caught = set(metrics.get("parallel", {}).get("caught", []))
    metrics["unique_catches"] = {
        "exa": sorted(exa_caught - parallel_caught),
        "parallel": sorted(parallel_caught - exa_caught),
    }

    best_single = max(
        metrics.get("exa", {}).get("catch_rate", 0.0),
        metrics.get("parallel", {}).get("catch_rate", 0.0),
    )
    ensemble_rate = metrics.get("ensemble", {}).get("catch_rate", 0.0)
    metrics["ensemble_incremental_recall"] = ensemble_rate - best_single

    new_survivor_collisions = {}
    for case_id, metadata in labels.items():
        if metadata["expected_action"] != "adjudicate":
            continue
        collision_conditions = [
            condition
            for condition, condition_outcomes in outcomes.items()
            if condition_outcomes.get(case_id) in {"reject", "narrow"}
        ]
        if collision_conditions:
            new_survivor_collisions[case_id] = collision_conditions
    metrics["new_survivor_collisions"] = new_survivor_collisions

    return metrics
