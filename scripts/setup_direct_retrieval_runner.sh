#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV="$ROOT/.venv-retrieval"

python3 -m venv "$VENV"
"$VENV/bin/python" -m pip install --upgrade pip
"$VENV/bin/python" -m pip install --upgrade mcp pytest

cat <<EOF
Direct retrieval runner ready.

Activate with:
  source "$VENV/bin/activate"

Then verify direct MCP connectivity with:
  python scripts/check_direct_retrieval_capabilities.py

No Codex process is required.
EOF
