import json
from pathlib import Path

from analysis.retrieval_ensemble.live_runner import (
    build_manifest,
    manifest_digest,
    result_path,
    should_skip,
)


def _cases():
    return [
        {
            "case_id": "C1",
            "candidate_text": "A plain candidate proposition.",
            "historical_label": "rejected",
            "expected_action": "reject",
            "known_collision_family": "SECRET GROUND TRUTH",
            "notes": "SECRET NOTES",
        }
    ]


def test_manifest_exposes_only_candidate_and_frozen_queries():
    manifest = build_manifest(_cases())
    encoded = json.dumps(manifest, sort_keys=True)
    assert "SECRET GROUND TRUTH" not in encoded
    assert "SECRET NOTES" not in encoded
    assert "historical_label" not in encoded
    case = manifest["cases"][0]
    assert set(case) == {"case_id", "candidate_text", "queries"}
    assert set(case["queries"]) == {
        "target_neighbor",
        "alternate_terminology",
        "source_domain",
        "falsification",
    }


def test_manifest_digest_is_stable_for_same_content():
    first = build_manifest(_cases())
    second = build_manifest(_cases())
    assert manifest_digest(first) == manifest_digest(second)


def test_successful_checkpoint_is_skipped_but_error_is_retriable(tmp_path: Path):
    ok = result_path(tmp_path, "exa", "C1", "target_neighbor")
    ok.parent.mkdir(parents=True)
    ok.write_text(json.dumps({"status": "ok"}))
    assert should_skip(ok) is True

    failed = result_path(tmp_path, "parallel", "C1", "target_neighbor")
    failed.parent.mkdir(parents=True)
    failed.write_text(json.dumps({"status": "error"}))
    assert should_skip(failed) is False
