import json
from pathlib import Path

from analysis.retrieval_ensemble.compact_results import extract_sources, compact_case


def test_extract_sources_parses_exa_and_parallel_formats():
    exa = {
        "status": "ok",
        "provider": "exa",
        "query_family": "target_neighbor",
        "response": {
            "content": [
                {
                    "text": (
                        "Title: Example Exa Source\n"
                        "URL: https://example.com/exa\n"
                        "Published: 2024-01-01\n"
                        "Highlights:\nStructural precedent text."
                    )
                }
            ]
        },
    }
    parallel = {
        "status": "ok",
        "provider": "parallel",
        "query_family": "falsification",
        "response": {
            "content": [
                {
                    "text": json.dumps(
                        {
                            "results": [
                                {
                                    "url": "https://example.com/parallel",
                                    "title": "Example Parallel Source",
                                    "publish_date": "2023-02-03",
                                    "excerpts": ["Parallel precedent text."],
                                }
                            ]
                        }
                    )
                }
            ]
        },
    }

    exa_sources = extract_sources(exa)
    parallel_sources = extract_sources(parallel)

    assert exa_sources[0]["url"] == "https://example.com/exa"
    assert exa_sources[0]["family"] == "target_neighbor"
    assert parallel_sources[0]["url"] == "https://example.com/parallel"
    assert parallel_sources[0]["family"] == "falsification"


def test_compact_case_deduplicates_urls_and_tracks_query_families(tmp_path: Path):
    raw = tmp_path / "raw"
    case_id = "C1"
    for family in ("target_neighbor", "falsification"):
        path = raw / "exa" / case_id / f"{family}.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(
                {
                    "status": "ok",
                    "provider": "exa",
                    "query_family": family,
                    "response": {
                        "content": [
                            {
                                "text": (
                                    "Title: Repeated Source\n"
                                    "URL: https://example.com/repeated\n"
                                    "Published: 2022-01-01\n"
                                    f"Highlights:\nEvidence from {family}."
                                )
                            }
                        ]
                    },
                }
            ),
            encoding="utf-8",
        )

    result = compact_case(raw, case_id, max_sources=10)
    assert len(result["exa"]) == 1
    assert result["exa"][0]["families"] == ["falsification", "target_neighbor"]
    assert result["exa"][0]["family_count"] == 2
