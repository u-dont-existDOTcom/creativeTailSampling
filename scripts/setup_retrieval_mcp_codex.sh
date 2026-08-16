#!/usr/bin/env bash
set -euo pipefail

EXA_URL='https://mcp.exa.ai/mcp?tools=web_search_exa,web_fetch_exa,web_search_advanced_exa'
PARALLEL_SEARCH_URL='https://search.parallel.ai/mcp'
PARALLEL_TASK_URL='https://task-mcp.parallel.ai/mcp'

if ! command -v codex >/dev/null 2>&1; then
  echo 'ERROR: codex is not on PATH.' >&2
  exit 1
fi

replace_server() {
  local name=$1
  shift
  codex mcp remove "$name" >/dev/null 2>&1 || true
  codex mcp add "$name" "$@"
}

replace_server exa --url "$EXA_URL"

if [[ -n "${PARALLEL_API_KEY:-}" ]]; then
  replace_server parallel-search --url "$PARALLEL_SEARCH_URL" --bearer-token-env-var PARALLEL_API_KEY
  replace_server parallel-task --url "$PARALLEL_TASK_URL" --bearer-token-env-var PARALLEL_API_KEY
  echo 'Parallel Search configured with authenticated higher-rate access.'
  echo 'Parallel Task configured with PARALLEL_API_KEY bearer authentication.'
else
  replace_server parallel-search --url "$PARALLEL_SEARCH_URL"
  codex mcp remove parallel-task >/dev/null 2>&1 || true
  echo 'Parallel Search configured anonymously.'
  echo 'Parallel Task not configured: PARALLEL_API_KEY is missing.'
fi

echo 'Exa configured with web_search_exa, web_fetch_exa, and web_search_advanced_exa.'
echo 'Restart Codex so the new MCP configuration and environment are loaded.'
