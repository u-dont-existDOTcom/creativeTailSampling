#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PY="$ROOT/.venv-retrieval/bin/python"

if [[ ! -x "$PY" ]]; then
  echo 'Direct retrieval environment: missing'
  echo 'Run: bash scripts/setup_direct_retrieval_runner.sh'
  exit 2
fi

cd "$ROOT"
exec "$PY" -m scripts.check_direct_retrieval_capabilities
