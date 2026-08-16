import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_benchmark_cases_are_stratified_and_secret_free():
    cases = json.loads((ROOT / "analysis/retrieval_ensemble/benchmark_cases.json").read_text())
    assert len(cases) >= 12
    labels = {case["historical_label"] for case in cases}
    assert {"rejected", "narrowed", "survivor", "cross_domain"} <= labels
    for case in cases:
        assert case["case_id"]
        assert case["candidate_text"].strip()
        assert case["expected_action"] in {"reject", "narrow", "adjudicate"}
        serialized = json.dumps(case).lower()
        assert "api_key" not in serialized
        assert "bearer " not in serialized
