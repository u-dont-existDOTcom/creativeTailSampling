from analysis.retrieval_ensemble.query_families import build_query_families


def test_query_families_are_complete_and_do_not_cross_feed_provider_names():
    case = {
        "candidate_text": "A neutral lottery assigns viable split groups to mother and daughter settlements.",
        "known_collision_family": "organizational fission / random allocation",
        "notes": "cross-domain source may include experimental allocation procedures",
    }
    q = build_query_families(case)
    assert set(q) == {"target_neighbor", "alternate_terminology", "source_domain", "falsification"}
    flat = " ".join(x for xs in q.values() for x in xs).lower()
    assert "exa" not in flat
    assert "parallel" not in flat
    assert case["candidate_text"].lower() in flat


def test_query_families_do_not_leak_historical_collision_ground_truth():
    base = {
        "candidate_text": "A neutral lottery assigns viable split groups to mother and daughter settlements.",
        "known_collision_family": "SECRET_GROUND_TRUTH_ONE",
        "notes": "historical notes one",
    }
    changed = {
        **base,
        "known_collision_family": "SECRET_GROUND_TRUTH_TWO",
        "notes": "completely different historical notes",
    }
    assert build_query_families(base) == build_query_families(changed)
