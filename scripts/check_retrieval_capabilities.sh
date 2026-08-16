#!/usr/bin/env bash
set -u

status=0

if command -v codex >/dev/null 2>&1; then
  echo "Codex: $(codex --version 2>/dev/null || echo installed)"
  for server in exa parallel-search parallel-task; do
    if codex mcp get "$server" >/dev/null 2>&1; then
      echo "$server: configured"
    else
      echo "$server: missing"
      [[ "$server" == parallel-task && -z "${PARALLEL_API_KEY:-}" ]] || status=1
    fi
  done
else
  echo 'Codex: missing'
  status=1
fi

if [[ -n "${PARALLEL_API_KEY:-}" ]]; then
  echo 'PARALLEL_API_KEY: set'
else
  echo 'PARALLEL_API_KEY: missing'
fi

if command -v parallel-cli >/dev/null 2>&1; then
  echo "Parallel CLI: $(parallel-cli --version 2>/dev/null || echo installed)"
  parallel-cli auth >/dev/null 2>&1 && echo 'Parallel CLI auth: valid' || echo 'Parallel CLI auth: not verified'
else
  echo 'Parallel CLI: optional / not installed'
fi

exit "$status"
