# Retrieval Ensemble Benchmark Runbook

## Purpose

Measure whether independent Exa and Parallel retrieval materially improve the Creative Tail Sampling novelty gate. This is a retrieval benchmark, not a test of whether historical survivor labels were correct.

## Inputs

- `benchmark_cases.json` — frozen historical labels and ground-truth collision families.
- `query_families.py` — provider-independent query templates.
- `normalize.py` / `adjudication.py` — common result format and novelty disposition.
- `score.py` — benchmark scoring.

The fields `known_collision_family`, `expected_action`, `historical_label`, `notes`, and `source_run` are evaluator metadata. **Do not expose them to Exa or Parallel.** Provider prompts may consume only `case_id`, `candidate_text`, and the frozen query strings generated from `candidate_text`.

## Canonical execution command

The benchmark is Codex-independent. From the feature branch with the direct retrieval environment installed:

```bash
bash scripts/run_retrieval_benchmark.sh
```

The wrapper:

1. runs the repository test suite;
2. verifies direct Exa, Parallel Search, and Parallel Task connectivity;
3. freezes and hashes the `round-001` query manifest before retrieval;
4. collects the Exa and Parallel Search lanes independently and sequentially;
5. checkpoints each individual call atomically;
6. stops a provider lane after its first tool failure rather than hammering a rate-limited or schema-changed service;
7. commits and pushes all completed checkpoints even when the round is incomplete;
8. resumes by skipping only checkpoints whose status is `ok`.

Parallel Search may run anonymously for ad-hoc use, but the benchmark uses `PARALLEL_API_KEY` whenever it is available so a large frozen round is not truncated by the anonymous free-tier rate limit. The helper's optional-auth mode means **use the key if present, fall back anonymously only if absent**. Parallel Task/deep research always requires authentication.

## Conditions

Run the same cases under four conditions:

1. `exa` — Exa MCP initial independent pass.
2. `parallel` — Parallel Search MCP initial independent pass.
3. `ensemble` — union/adjudication after both independent passes are finished.
4. `ensemble_deep` — Parallel Task/CLI escalation only for cases still ambiguous or with no collision after the routine ensemble.

Do not cross-feed Exa results into Parallel's initial queries or vice versa.

## Freeze queries before retrieval

For each case, generate all four query families before invoking either provider:

- `target_neighbor`
- `alternate_terminology`
- `source_domain`
- `falsification`

Save the generated query manifest under the immutable round directory and hash it before the first provider call. Do not edit the manifest after seeing retrieval results; if a query defect requires a change, create a new benchmark round and preserve the old round.

## Initial provider passes

### Exa

Use `web_search_exa` for each frozen query. Use `web_fetch_exa` on plausible collision sources during the adjudication pass. Use `web_search_advanced_exa` only when ordinary Exa search leaves a concrete unresolved terminology/domain/date question; record that it was an advanced follow-up.

### Parallel Search

Use `web_search` for each frozen query and `web_fetch` on plausible collision sources during adjudication. Do not add terms learned from Exa until the first Parallel pass is complete.

The routine collector stores raw search responses before any novelty judgment. This keeps retrieval measurement distinct from adjudication.

## Evidence standard

A search result is not itself a collision. For each plausible source, record:

- exact source/title/URL and date if available;
- what the source actually claims;
- whether the relevant mechanism is in the same target domain or only a source domain;
- `collision_strength`: `direct`, `root_plus_residual`, `corroboration`, `ambiguous`, or `no_collision`;
- `source_quality`: prefer primary literature, original technical documentation, or direct historical sources over snippets and secondary summaries;
- a short rationale that distinguishes structural equivalence from superficial vocabulary overlap.

For a cross-domain candidate, source-domain familiarity alone does **not** kill the transfer. A direct kill requires evidence that substantially the same structural transfer to the target domain was already established, or that the target claim adds nothing distinctive beyond the source mechanism.

## Output layout

Routine retrieval is stored as:

```text
analysis/retrieval_ensemble/results/
  round-001/
    query_manifest.json
    query_manifest.sha256
    schemas/
      exa.json
      parallel.json
    raw/
      exa/<case_id>/<query_family>.json
      parallel/<case_id>/<query_family>.json
```

Later adjudication/deep-search artifacts must remain downstream of these frozen raw responses rather than rewriting them.

## Ensemble adjudication

Only after both first-pass provider lanes are complete:

1. mark substantially equivalent precedents that both found;
2. mark credible precedents unique to Exa or Parallel;
3. fetch primary/full sources where snippets are insufficient;
4. run `adjudicate` over the normalized evidence;
5. allow one credible direct collision to reject even if the other provider missed it;
6. preserve `root_plus_residual` as a narrowing event rather than flattening it into rejection;
7. escalate unresolved `ambiguous` cases.

A provider returning nothing is `no_collision_found`, never evidence of originality.

## Parallel deep-research escalation

Use Parallel Task/CLI only when:

- the routine ensemble finds no convincing precedent and the candidate would otherwise be promoted;
- a plausible collision cannot be resolved from retrieved primary sources;
- Exa and Parallel expose materially different conceptual neighborhoods and novelty depends on resolving them.

Do not pay for deep research on cases already correctly rejected or narrowed by routine retrieval.

Round 001's frozen escalation set is `C015`, `C001`, `C005`, `C006`, and `C025`. `C016` is excluded because routine retrieval already produced a decisive direct collision.

Canonical escalation command:

```bash
bash scripts/run_parallel_deep_benchmark.sh
```

The wrapper:

1. runs the full test suite before any paid task is created;
2. verifies Parallel CLI authentication;
3. launches at most one `pro` research run per frozen escalation case using `--no-wait`;
4. commits/pushes every created `trun_...` ID before polling;
5. polls those same IDs and stores the final JSON results;
6. never relaunches an existing task on resume.

The processor is intentionally frozen to `pro` for this benchmark so cost/quality are comparable across cases. Do not silently upgrade processors or add cases within the same benchmark round.

## Scoring

Primary positive set: historical cases whose `expected_action` is `reject` or `narrow`.

Report:

- Exa false-novelty catch rate;
- Parallel false-novelty catch rate;
- ensemble catch rate;
- ensemble incremental recall over the stronger single provider;
- Exa-only and Parallel-only correct catches;
- search stage/time-to-kill where observable;
- deep escalation count and resolution yield;
- newly discovered `reject`/`narrow` evidence against historical current survivors, listed separately for manual adjudication.

Do not count an over-rejection as a correct narrowing. If history says `narrow`, the benchmark only counts `narrow` as the correct catch.

## Adoption decision

Make routine Exa + Parallel mandatory only if the benchmark shows meaningful complementary retrieval or earlier correct collision detection without excessive adjudication burden. If one provider adds negligible unique value, simplify the stack. Retain Parallel deep research only if it resolves a meaningful share of routine residual cases.
