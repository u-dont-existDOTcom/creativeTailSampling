from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _text():
    paths = [
        ROOT / "scripts/setup_retrieval_mcp_codex.sh",
        ROOT / "scripts/check_retrieval_capabilities.sh",
        ROOT / "docs/RETRIEVAL-MCP-SETUP.md",
    ]
    return "\n".join(path.read_text() for path in paths)


def test_setup_files_never_embed_literal_credentials():
    text = _text().lower()
    assert "your-parallel-api-key" not in text
    assert "authorization: bearer sk-" not in text
    assert "parallel_api_key=" not in text


def test_setup_uses_environment_reference_and_expected_servers():
    text = _text()
    assert "PARALLEL_API_KEY" in text
    assert "https://mcp.exa.ai/mcp?tools=web_search_exa,web_fetch_exa,web_search_advanced_exa" in text
    assert "https://search.parallel.ai/mcp" in text
    assert "https://task-mcp.parallel.ai/mcp" in text
    assert "--bearer-token-env-var PARALLEL_API_KEY" in text
