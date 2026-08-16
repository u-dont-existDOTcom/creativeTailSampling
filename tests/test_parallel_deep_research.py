import json
from pathlib import Path

import pytest

from analysis.retrieval_ensemble.deep_research import (
    CASES,
    build_prompt,
    find_run_id,
    result_is_complete,
)


def test_escalation_set_is_exactly_five_cases():
    assert list(CASES) == ["C015", "C001", "C005", "C006", "C025"]


def test_prompts_do_not_leak_historical_ground_truth():
    for case_id, case in CASES.items():
        prompt = build_prompt(case_id, case)
        assert case["candidate"] in prompt
        assert "known_collision_family" not in prompt
        assert "expected_action" not in prompt
        assert "historical_label" not in prompt
        assert "find the strongest credible prior" in prompt.lower()
        assert "target domain" in prompt.lower()


def test_find_run_id_handles_nested_json():
    assert find_run_id({"run_id": "trun_123"}) == "trun_123"
    assert find_run_id({"data": {"id": "trun_456"}}) == "trun_456"
    with pytest.raises(ValueError):
        find_run_id({"status": "running"})


def test_result_complete_requires_nonempty_output(tmp_path: Path):
    path = tmp_path / "result.json"
    assert result_is_complete(path) is False
    path.write_text(json.dumps({"status": "completed", "output": "report"}))
    assert result_is_complete(path) is True
    path.write_text(json.dumps({"status": "completed"}))
    assert result_is_complete(path) is False
