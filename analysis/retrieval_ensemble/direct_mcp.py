import os
import re

EXA_URL = "https://mcp.exa.ai/mcp?tools=web_search_exa,web_fetch_exa,web_search_advanced_exa"
PARALLEL_SEARCH_URL = "https://search.parallel.ai/mcp"
PARALLEL_TASK_URL = "https://task-mcp.parallel.ai/mcp"

_STOPWORDS = {
    "the", "a", "an", "and", "or", "of", "to", "in", "on", "for", "with", "by",
    "is", "are", "be", "when", "so", "that", "this", "under", "before", "after",
    "should", "can", "could", "would", "from", "into", "rather", "than", "their",
    "its", "as", "if", "while", "through", "enough", "same", "new", "real",
}


def parallel_headers(*, required: bool = True) -> dict[str, str]:
    """Return Task auth headers; routine Search stays anonymous when not required."""
    if not required:
        return {}
    key = os.environ.get("PARALLEL_API_KEY", "").strip()
    if not key:
        raise RuntimeError("PARALLEL_API_KEY is required for Parallel Task MCP")
    return {"Authorization": f"Bearer {key}"}


def _keywords(text: str) -> list[str]:
    words = re.findall(r"[A-Za-z0-9][A-Za-z0-9_-]*", text.lower())
    out: list[str] = []
    for word in words:
        if word in _STOPWORDS or len(word) < 3 or word in out:
            continue
        out.append(word)
    return out


def _query(words: list[str], fallback: list[str]) -> str:
    chosen = words[:6]
    if len(chosen) < 3:
        chosen = (chosen + fallback)[:3]
    return " ".join(chosen)


def build_parallel_search_args(candidate_text: str, objective: str) -> dict[str, object]:
    """Build Parallel's objective + three short keyword queries without evaluator metadata."""
    words = _keywords(candidate_text)
    q1 = _query(words[:6], ["prior", "theory", "mechanism"])
    q2 = _query(words[3:9], ["established", "practice", "precedent"])
    q3 = _query(words[::2][:5] + ["precedent"], ["novelty", "prior", "art"])

    queries: list[str] = []
    for query in (q1, q2, q3):
        if query not in queries:
            queries.append(query)
    while len(queries) < 3:
        base = _query(words[:4], ["prior", "theory", "mechanism"])
        queries.append(f"{base} prior{len(queries) + 1}")

    return {"objective": objective, "search_queries": queries[:3]}
