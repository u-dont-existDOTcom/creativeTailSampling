# Exa + Parallel Retrieval Ensemble Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and retrospectively test an independent Exa + Parallel retrieval ensemble that catches false novelty before Creative Tail Sampling promotes a candidate, while reserving Parallel deep research for stubborn survivors.

**Architecture:** Candidate generation remains retrieval-free. A benchmark fixture set is drawn from the repo's labeled historical record; each candidate is searched independently through Exa and Parallel Search using frozen query families, then provider results are normalized and adjudicated without cross-feeding until both initial passes finish. Parallel Task/CLI is an escalation lane for unresolved routine survivors. Authentication is runtime-only via environment variables/OAuth and no secret is committed.

**Tech Stack:** Python 3 standard library, pytest, JSON/JSONL, Codex remote MCP configuration, Exa MCP, Parallel Search MCP, Parallel Task MCP, optional Parallel CLI.

## Global Constraints

- Never expose Exa/Parallel retrieval results to the candidate-generation stage.
- Run the active-project corpus collision gate before external retrieval.
- Initial Exa and Parallel searches must be independent: neither provider sees the other's hits or generated search terms.
- A credible collision from either provider is sufficient to kill or narrow a candidate; provider consensus is not required.
- Parallel Task/CLI deep research is escalation only, never the default lane for every candidate.
- No API key, bearer token, OAuth token, `.env` secret, or literal credential may be committed.
- A search miss means `no collision found`, never `original`.
- Current strict survivors are stress-test cases, not presumed true negatives.

---

### Task 1: Freeze benchmark schema and labeled fixtures

**Files:**
- Create: `analysis/retrieval_ensemble/schema.json`
- Create: `analysis/retrieval_ensemble/benchmark_cases.json`
- Create: `tests/test_retrieval_benchmark_fixtures.py`

**Interfaces:**
- Consumes: historical candidate labels and narrowing/rejection reasons from `FINDINGS.md`, `STATE.md`, and `runs/`.
- Produces: `benchmark_cases.json`, an array of records with `case_id`, `candidate_text`, `historical_label`, `expected_action`, `known_collision_family`, `source_run`, and `notes`.

- [ ] **Step 1: Write the failing fixture-validation test**

```python
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_benchmark_cases_are_stratified_and_secret_free():
    cases = json.loads((ROOT / "analysis/retrieval_ensemble/benchmark_cases.json").read_text())
    assert len(cases) >= 12
    labels = {case["historical_label"] for case in cases}
    assert {"rejected", "narrowed", "survivor", "cross_domain"} <= labels
    for case in cases:
        assert case["case_id"]
        assert case["candidate_text"].strip()
        assert case["expected_action"] in {"reject", "narrow", "adjudicate"}
        serialized = json.dumps(case).lower()
        assert "api_key" not in serialized
        assert "bearer " not in serialized
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `pytest tests/test_retrieval_benchmark_fixtures.py -v`
Expected: FAIL because the benchmark fixture file does not yet exist.

- [ ] **Step 3: Create the schema and at least 12 stratified cases**

Use historical cases with explicit provenance. Include at minimum examples from: familiar/rejected branches, `C003`, `C011`, `C013`, `C015`, `C018`, current strict survivors, and at least two cross-domain transfers. Do not infer a historical rejection reason that is not recorded in the repo.

- [ ] **Step 4: Run fixture validation**

Run: `pytest tests/test_retrieval_benchmark_fixtures.py -v`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add analysis/retrieval_ensemble/schema.json analysis/retrieval_ensemble/benchmark_cases.json tests/test_retrieval_benchmark_fixtures.py
git commit -m "test: add retrieval ensemble benchmark fixtures"
```

---

### Task 2: Add deterministic query-family generation

**Files:**
- Create: `analysis/retrieval_ensemble/query_families.py`
- Create: `tests/test_query_families.py`

**Interfaces:**
- Consumes: one benchmark case record.
- Produces: `build_query_families(case: dict) -> dict[str, list[str]]` with provider-independent canonical families: `target_neighbor`, `alternate_terminology`, `source_domain`, and `falsification`.

- [ ] **Step 1: Write failing tests for stable, provider-independent queries**

```python
from analysis.retrieval_ensemble.query_families import build_query_families


def test_query_families_are_complete_and_do_not_cross_feed_provider_names():
    case = {
        "candidate_text": "A neutral lottery assigns viable split groups to mother and daughter settlements.",
        "known_collision_family": "organizational fission / random allocation",
        "notes": "cross-domain source may include experimental allocation procedures",
    }
    q = build_query_families(case)
    assert set(q) == {"target_neighbor", "alternate_terminology", "source_domain", "falsification"}
    flat = " ".join(x for xs in q.values() for x in xs).lower()
    assert "exa" not in flat
    assert "parallel" not in flat
    assert case["candidate_text"].lower() in flat
```

- [ ] **Step 2: Run the tests to verify failure**

Run: `pytest tests/test_query_families.py -v`
Expected: FAIL because the module does not exist.

- [ ] **Step 3: Implement `build_query_families` with fixed templates**

The function must generate at least one query in each family and must not consume provider output. Use the canonical candidate text verbatim in every family, adding only role-specific instructions such as “find an established equivalent using different terminology” or “find the strongest prior mechanism that would make this claim non-novel.”

- [ ] **Step 4: Run tests**

Run: `pytest tests/test_query_families.py -v`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add analysis/retrieval_ensemble/query_families.py tests/test_query_families.py
git commit -m "feat: add independent novelty attack query families"
```

---

### Task 3: Add provider-result normalization and collision adjudication schema

**Files:**
- Create: `analysis/retrieval_ensemble/normalize.py`
- Create: `analysis/retrieval_ensemble/adjudication.py`
- Create: `tests/test_retrieval_normalization.py`

**Interfaces:**
- Consumes: provider-tagged raw result records produced by MCP/CLI runs.
- Produces: normalized records with `provider`, `query_family`, `title`, `url`, `date`, `precedent_claim`, `collision_strength`, `source_quality`, `unique_to_provider`, and `rationale`.
- Produces: `adjudicate(records: list[dict]) -> dict` with action `reject`, `narrow`, `escalate`, or `no_collision_found`.

- [ ] **Step 1: Write failing normalization/adjudication tests**

```python
from analysis.retrieval_ensemble.adjudication import adjudicate


def test_direct_collision_from_one_provider_is_enough_to_reject():
    records = [
        {"provider": "exa", "collision_strength": "direct", "source_quality": "primary"},
        {"provider": "parallel", "collision_strength": "no_collision", "source_quality": "none"},
    ]
    assert adjudicate(records)["action"] == "reject"


def test_ambiguous_provider_disagreement_escalates():
    records = [
        {"provider": "exa", "collision_strength": "ambiguous", "source_quality": "scholarly"},
        {"provider": "parallel", "collision_strength": "no_collision", "source_quality": "none"},
    ]
    assert adjudicate(records)["action"] == "escalate"
```

- [ ] **Step 2: Run tests to verify failure**

Run: `pytest tests/test_retrieval_normalization.py -v`
Expected: FAIL because the modules do not exist.

- [ ] **Step 3: Implement normalization and adjudication**

Allowed collision strengths: `direct`, `root_plus_residual`, `corroboration`, `ambiguous`, `no_collision`. `direct` yields reject; `root_plus_residual` yields narrow; unresolved `ambiguous` yields escalate; only absence of substantive collisions yields `no_collision_found`.

- [ ] **Step 4: Run tests**

Run: `pytest tests/test_retrieval_normalization.py -v`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add analysis/retrieval_ensemble/normalize.py analysis/retrieval_ensemble/adjudication.py tests/test_retrieval_normalization.py
git commit -m "feat: normalize and adjudicate provider collisions"
```

---

### Task 4: Add secret-safe Codex/MCP bootstrap and capability check

**Files:**
- Create: `scripts/setup_retrieval_mcp_codex.sh`
- Create: `scripts/check_retrieval_capabilities.sh`
- Create: `docs/RETRIEVAL-MCP-SETUP.md`
- Create: `tests/test_secret_hygiene.py`

**Interfaces:**
- Consumes: optional runtime `PARALLEL_API_KEY`; no Exa key required for the benchmark baseline.
- Produces: Codex MCP entries `exa`, `parallel-search`, `parallel-task`; optional `parallel-cli`; capability report that never prints secret values.

- [ ] **Step 1: Write a failing secret-hygiene test**

```python
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_setup_files_never_embed_literal_credentials():
    paths = [
        ROOT / "scripts/setup_retrieval_mcp_codex.sh",
        ROOT / "scripts/check_retrieval_capabilities.sh",
        ROOT / "docs/RETRIEVAL-MCP-SETUP.md",
    ]
    text = "\n".join(path.read_text() for path in paths).lower()
    assert "your-parallel-api-key" not in text
    assert "authorization: bearer sk-" not in text
    assert "parallel_api_key=" not in text
```

- [ ] **Step 2: Run test to verify failure**

Run: `pytest tests/test_secret_hygiene.py -v`
Expected: FAIL because setup files do not exist.

- [ ] **Step 3: Implement idempotent Codex bootstrap**

The script must:

```bash
codex mcp add exa --url 'https://mcp.exa.ai/mcp?tools=web_search_exa,web_fetch_exa,web_search_advanced_exa'
codex mcp add parallel-search --url https://search.parallel.ai/mcp --bearer-token-env-var PARALLEL_API_KEY
codex mcp add parallel-task --url https://task-mcp.parallel.ai/mcp --bearer-token-env-var PARALLEL_API_KEY
```

Before adding authenticated Parallel entries, test only whether `PARALLEL_API_KEY` is set/non-empty; never echo it. Make repeated runs safe by detecting/removing/replacing existing entries using supported `codex mcp` commands rather than appending duplicate config blocks.

Document that Search can run anonymously if desired, while Task always requires auth. Document Parallel CLI installation with `pipx install "parallel-web-tools[cli]" && pipx ensurepath`, and `parallel-cli auth` as the verification command.

- [ ] **Step 4: Implement capability checks**

Verify presence of `codex`, list configured MCP servers, verify `parallel-cli` if installed, and report only `PARALLEL_API_KEY: set` or `PARALLEL_API_KEY: missing`.

- [ ] **Step 5: Run tests**

Run: `pytest tests/test_secret_hygiene.py -v`
Expected: PASS.

- [ ] **Step 6: Commit**

```bash
git add scripts/setup_retrieval_mcp_codex.sh scripts/check_retrieval_capabilities.sh docs/RETRIEVAL-MCP-SETUP.md tests/test_secret_hygiene.py
git commit -m "feat: add secret-safe Exa Parallel MCP bootstrap"
```

---

### Task 5: Add benchmark run contract and scoring

**Files:**
- Create: `analysis/retrieval_ensemble/score.py`
- Create: `analysis/retrieval_ensemble/RUNBOOK.md`
- Create: `tests/test_retrieval_scoring.py`

**Interfaces:**
- Consumes: normalized JSONL result files named `<case_id>.<condition>.jsonl` where condition is `exa`, `parallel`, `ensemble`, or `ensemble_deep`.
- Produces: aggregate metrics including false-novelty catch rate, unique collision yield, ensemble incremental recall, escalation rate, and newly discovered survivor collisions.

- [ ] **Step 1: Write failing scoring tests with a miniature synthetic fixture**

```python
from analysis.retrieval_ensemble.score import score_cases


def test_ensemble_incremental_recall_counts_complementary_hits():
    labels = {
        "a": {"expected_action": "reject"},
        "b": {"expected_action": "narrow"},
    }
    outcomes = {
        "exa": {"a": "reject", "b": "no_collision_found"},
        "parallel": {"a": "no_collision_found", "b": "narrow"},
        "ensemble": {"a": "reject", "b": "narrow"},
    }
    metrics = score_cases(labels, outcomes)
    assert metrics["ensemble"]["catch_rate"] == 1.0
    assert metrics["ensemble_incremental_recall"] == 0.5
```

- [ ] **Step 2: Run test to verify failure**

Run: `pytest tests/test_retrieval_scoring.py -v`
Expected: FAIL because the scoring module does not exist.

- [ ] **Step 3: Implement scoring and runbook**

The runbook must freeze query families before provider execution, require independent initial passes, specify where raw/normalized outputs are stored, and state that current-survivor collisions are manually adjudicated rather than counted as automatic errors.

- [ ] **Step 4: Run tests**

Run: `pytest tests/test_retrieval_scoring.py -v`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add analysis/retrieval_ensemble/score.py analysis/retrieval_ensemble/RUNBOOK.md tests/test_retrieval_scoring.py
git commit -m "feat: score retrieval ensemble benchmark"
```

---

### Task 6: Run the retrospective benchmark and decide whether B earns mandatory-gate status

**Files:**
- Create: `runs/2026-08-16-retrieval-ensemble-benchmark.md`
- Create: `analysis/retrieval_ensemble/results/` provider result files
- Modify only if benchmark passes acceptance criteria: `PROTOCOL.md`
- Modify: `STATE.md`

**Interfaces:**
- Consumes: configured Exa and Parallel MCPs, benchmark fixtures, frozen query families, normalization/adjudication/scoring tools.
- Produces: benchmark report plus a go/no-go decision for routine Exa + Parallel Search and a separate go/no-go decision for Parallel deep-research escalation.

- [ ] **Step 1: Verify capabilities before any paid deep-research call**

Run: `bash scripts/check_retrieval_capabilities.sh`
Expected: Exa and Parallel Search available; Parallel Task authenticated before escalation is attempted.

- [ ] **Step 2: Run independent Exa and Parallel Search passes**

For every benchmark case, execute all frozen query families against Exa first-pass and Parallel first-pass independently. Store provider outputs separately. Do not cross-feed results during initial passes.

- [ ] **Step 3: Normalize and adjudicate routine results**

Create per-case normalized records and compute provider-alone plus ensemble outcomes.

- [ ] **Step 4: Escalate only routine survivors/ambiguities through Parallel Task/CLI**

Record cost/processor choice where exposed by Parallel. Do not deep-research cases already correctly killed/narrowed by routine retrieval.

- [ ] **Step 5: Score and write the benchmark report**

The report must include per-provider catch rate, unique collision counts, ensemble incremental recall, escalation rate, qualitative source-quality notes, newly discovered survivor collisions, and any cases where retrieval was inconclusive.

- [ ] **Step 6: Apply the acceptance criteria**

If both providers materially contribute, update `PROTOCOL.md` to make the independent Exa + Parallel routine pass mandatory. If one is redundant, retain only the demonstrably useful component. Keep deep research escalation only if it resolves meaningful residual cases.

- [ ] **Step 7: Update durable state and commit**

```bash
git add analysis/retrieval_ensemble runs/2026-08-16-retrieval-ensemble-benchmark.md PROTOCOL.md STATE.md
git commit -m "bench: evaluate Exa Parallel novelty retrieval ensemble"
```

---

## Final verification

Run:

```bash
pytest -q
bash scripts/check_retrieval_capabilities.sh
```

Expected: all tests pass; capability output contains no credential values; benchmark report contains enough per-case evidence to reproduce every promotion/rejection/narrowing decision.
