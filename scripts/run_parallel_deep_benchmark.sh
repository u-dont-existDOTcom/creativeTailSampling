#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PY="$ROOT/.venv-retrieval/bin/python"
EXPECTED_BRANCH="agent/exa-parallel-retrieval-ensemble"
DEEP_RESULTS="analysis/retrieval_ensemble/results/round-001/deep"
BOT_NAME="creative-tail-sampling-bot"
BOT_EMAIL="creative-tail-sampling-bot@users.noreply.github.com"

cd "$ROOT"

if [[ ! -x "$PY" ]]; then
  echo 'Direct retrieval environment: missing'
  echo 'Run: bash scripts/setup_direct_retrieval_runner.sh'
  exit 2
fi

if ! command -v parallel-cli >/dev/null 2>&1; then
  echo 'Parallel CLI: missing'
  echo "Install with: pipx install 'parallel-web-tools[cli]'"
  exit 2
fi

branch="$(git branch --show-current)"
if [[ "$branch" != "$EXPECTED_BRANCH" ]]; then
  echo "Refusing benchmark write on branch '$branch'."
  echo "Switch to $EXPECTED_BRANCH first."
  exit 2
fi

if ! parallel-cli auth >/dev/null 2>&1; then
  echo 'Parallel CLI authentication is not valid.'
  exit 2
fi

commit_checkpoint() {
  local message="$1"
  git add "$DEEP_RESULTS"
  if git diff --cached --quiet; then
    return 0
  fi
  git -c user.name="$BOT_NAME" -c user.email="$BOT_EMAIL" commit -m "$message"
  git push origin HEAD
}

# Verify all deterministic invariants before creating paid runs.
"$PY" -m pytest -q

set +e
"$PY" -m scripts.run_parallel_deep_research --phase launch
launch_rc=$?
set -e
commit_checkpoint 'benchmark: launch Parallel deep escalation'

if [[ "$launch_rc" -ne 0 ]]; then
  echo 'Deep-research launch incomplete; launch checkpoints were preserved.'
  exit "$launch_rc"
fi

set +e
"$PY" -m scripts.run_parallel_deep_research --phase poll
poll_rc=$?
set -e
commit_checkpoint 'benchmark: collect Parallel deep escalation'

if [[ "$poll_rc" -ne 0 ]]; then
  echo 'One or more deep-research results are not complete. Re-run this same command; existing task IDs will be reused and never relaunched.'
fi

exit "$poll_rc"
