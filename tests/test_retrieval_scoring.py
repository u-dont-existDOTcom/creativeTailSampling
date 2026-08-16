from analysis.retrieval_ensemble.score import score_cases


def test_ensemble_incremental_recall_counts_complementary_hits():
    labels = {
        "a": {"expected_action": "reject"},
        "b": {"expected_action": "narrow"},
    }
    outcomes = {
        "exa": {"a": "reject", "b": "no_collision_found"},
        "parallel": {"a": "no_collision_found", "b": "narrow"},
        "ensemble": {"a": "reject", "b": "narrow"},
    }
    metrics = score_cases(labels, outcomes)
    assert metrics["ensemble"]["catch_rate"] == 1.0
    assert metrics["ensemble_incremental_recall"] == 0.5
    assert metrics["unique_catches"]["exa"] == ["a"]
    assert metrics["unique_catches"]["parallel"] == ["b"]


def test_adjudicate_cases_are_excluded_from_false_novelty_denominator():
    labels = {
        "known": {"expected_action": "reject"},
        "survivor": {"expected_action": "adjudicate"},
    }
    outcomes = {
        "exa": {"known": "reject", "survivor": "reject"},
        "parallel": {"known": "no_collision_found", "survivor": "no_collision_found"},
        "ensemble": {"known": "reject", "survivor": "reject"},
    }
    metrics = score_cases(labels, outcomes)
    assert metrics["exa"]["denominator"] == 1
    assert metrics["exa"]["catch_rate"] == 1.0
    assert metrics["new_survivor_collisions"] == {"survivor": ["exa", "ensemble"]}
