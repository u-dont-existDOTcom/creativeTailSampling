#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PY="$ROOT/.venv-retrieval/bin/python"
EXPECTED_BRANCH="agent/exa-parallel-retrieval-ensemble"
RESULTS="analysis/retrieval_ensemble/results/round-001"

cd "$ROOT"

if [[ ! -x "$PY" ]]; then
  echo 'Direct retrieval environment: missing'
  echo 'Run: bash scripts/setup_direct_retrieval_runner.sh'
  exit 2
fi

branch="$(git branch --show-current)"
if [[ "$branch" != "$EXPECTED_BRANCH" ]]; then
  echo "Refusing benchmark write on branch '$branch'."
  echo "Switch to $EXPECTED_BRANCH first."
  exit 2
fi

if [[ -z "${PARALLEL_API_KEY:-}" ]]; then
  echo 'PARALLEL_API_KEY: missing'
  exit 2
fi

# Verify deterministic/unit invariants and live provider connectivity before
# spending retrieval calls.
"$PY" -m pytest -q
"$PY" -m scripts.check_direct_retrieval_capabilities

set +e
"$PY" -m scripts.run_retrieval_benchmark --round round-001 "$@"
rc=$?
set -e

if [[ "$rc" -ne 0 ]]; then
  "$PY" -m scripts.report_retrieval_benchmark_errors --round round-001 || true
fi

# Preserve every completed checkpoint even if a provider rate-limits or fails.
# Use a runner-local identity so a fresh clone does not require personal Git
# identity configuration and we never mutate the user's global git config.
git add "$RESULTS"
if ! git diff --cached --quiet; then
  if [[ "$rc" -eq 0 ]]; then
    message='benchmark: collect round-001 routine retrieval'
  else
    message='benchmark: checkpoint partial round-001 retrieval'
  fi
  git -c user.name="Creative Tail Sampling Runner" \
      -c user.email="creative-tail-sampling@localhost" \
      commit -m "$message"
  git push origin HEAD
fi

exit "$rc"
