import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from analysis.retrieval_ensemble.direct_mcp import (
    EXA_URL,
    PARALLEL_SEARCH_URL,
    PARALLEL_TASK_URL,
    build_parallel_search_args,
    parallel_headers,
)


def test_direct_endpoints_do_not_depend_on_codex():
    assert EXA_URL == "https://mcp.exa.ai/mcp?tools=web_search_exa,web_fetch_exa,web_search_advanced_exa"
    assert PARALLEL_SEARCH_URL == "https://search.parallel.ai/mcp"
    assert PARALLEL_TASK_URL == "https://task-mcp.parallel.ai/mcp"


def test_parallel_headers_use_key_when_available_and_allow_anonymous_fallback(monkeypatch):
    monkeypatch.setenv("PARALLEL_API_KEY", "secret-value")
    assert parallel_headers() == {"Authorization": "Bearer secret-value"}
    assert parallel_headers(required=False) == {"Authorization": "Bearer secret-value"}
    monkeypatch.delenv("PARALLEL_API_KEY")
    assert parallel_headers(required=False) == {}


def test_parallel_search_args_are_deterministic_and_three_queries():
    candidate = "Governance rights should remain live under recusal vacancy quorum and deadline states."
    objective = "Find the closest established theory or practice containing this claim."
    first = build_parallel_search_args(candidate, objective)
    second = build_parallel_search_args(candidate, objective)
    assert first == second
    assert first["objective"] == objective
    assert len(first["search_queries"]) == 3
    assert all(3 <= len(q.split()) <= 6 for q in first["search_queries"])
