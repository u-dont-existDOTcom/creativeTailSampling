from analysis.retrieval_ensemble.adjudication import adjudicate
from analysis.retrieval_ensemble.normalize import normalize_result


def test_direct_collision_from_one_provider_is_enough_to_reject():
    records = [
        {"provider": "exa", "collision_strength": "direct", "source_quality": "primary"},
        {"provider": "parallel", "collision_strength": "no_collision", "source_quality": "none"},
    ]
    assert adjudicate(records)["action"] == "reject"


def test_root_plus_residual_narrows():
    records = [
        {"provider": "exa", "collision_strength": "root_plus_residual", "source_quality": "scholarly"},
        {"provider": "parallel", "collision_strength": "no_collision", "source_quality": "none"},
    ]
    assert adjudicate(records)["action"] == "narrow"


def test_ambiguous_provider_disagreement_escalates():
    records = [
        {"provider": "exa", "collision_strength": "ambiguous", "source_quality": "scholarly"},
        {"provider": "parallel", "collision_strength": "no_collision", "source_quality": "none"},
    ]
    assert adjudicate(records)["action"] == "escalate"


def test_normalize_result_preserves_provider_and_allowed_strength():
    raw = {
        "provider": "exa",
        "query_family": "falsification",
        "title": "Prior work",
        "url": "https://example.org/prior",
        "date": "2020-01-01",
        "precedent_claim": "same mechanism",
        "collision_strength": "direct",
        "source_quality": "scholarly",
        "rationale": "substantially contains the candidate",
    }
    result = normalize_result(raw)
    assert result["provider"] == "exa"
    assert result["collision_strength"] == "direct"
    assert result["unique_to_provider"] is False
