# Exa + Parallel Retrieval Ensemble Design

Date: 2026-08-16
Status: approved architecture boundary (Option B)
Branch: `agent/exa-parallel-retrieval-ensemble`

## Goal

Reduce false novelty in Creative Tail Sampling without contaminating the creative-generation stage with retrieval priors.

The system should keep candidate generation retrieval-free, then make precedent search substantially more adversarial by using multiple partially independent retrieval systems.

## Architecture

### Stage 0 — Retrieval-free generation

Generate tail candidates exactly as the protocol already requires. Do not expose the generator to Exa, Parallel, or external search results before candidate generation and internal compression gates are complete.

Reason: retrieval before generation would pull the model back toward already-salient concepts and undermine the purpose of tail sampling.

### Stage 1 — Internal corpus collision

Run the existing active-project corpus collision gate first. Candidates already owned by the target project's authoritative corpus are rejected or narrowed before any external retrieval cost is incurred.

### Stage 2 — Independent routine retrieval adversaries

For each surviving candidate, run two independent external nearest-neighbor attacks:

1. **Exa MCP**
   - primary role: semantic nearest-neighbor / terminology-translation collision search;
   - use `web_search_exa`, `web_fetch_exa`, and when useful `web_search_advanced_exa`;
   - search both target-domain precedent and plausible source-domain precedent for cross-domain transfers.

2. **Parallel Search MCP**
   - primary role: independent broad web retrieval and content extraction;
   - use `web_search` and `web_fetch`;
   - formulate its queries without seeing Exa results.

Provider result sets remain separate until both searches complete. One provider's result set must not be used to generate the other provider's initial queries.

Official integration references:
- Exa MCP: https://exa.ai/docs/reference/exa-mcp
- Parallel Search MCP: https://docs.parallel.ai/integrations/mcp/search-mcp

### Stage 3 — Retrieval disagreement analysis

After both providers finish:

- normalize each retrieved item into the alleged prior concept, source/domain, date, and collision rationale;
- compare conceptual neighborhoods rather than simply pooling URLs;
- record which precedents were found by Exa only, Parallel only, both, or neither;
- treat provider disagreement as search evidence, not noise;
- when one provider surfaces a new intellectual neighborhood, run a bounded follow-up attack in that neighborhood.

A candidate is killed or narrowed if any credible source demonstrates a substantive collision. Provider consensus is not required.

### Stage 4 — Escalation for stubborn survivors

Use **Parallel Task MCP and/or Parallel CLI deep research only for candidates that survive the routine ensemble or for cases of unresolved provider disagreement**.

Escalation triggers:

- both routine providers fail to find a convincing precedent and the candidate would otherwise be promoted;
- one provider finds a plausible but ambiguous collision that requires deeper source tracing;
- providers return materially different intellectual neighborhoods and the novelty judgment depends on resolving them;
- the proposed finding is unusually consequential and therefore merits a stronger promotion burden.

Parallel references:
- Task MCP: https://docs.parallel.ai/integrations/mcp/task-mcp
- CLI: https://docs.parallel.ai/integrations/cli

Do not run deep research automatically on every generated candidate.

## Query independence

Each provider receives the same canonical plain-language candidate plus provider-specific search instructions, but not the other provider's hits.

Minimum query families per provider:

1. exact mechanism / target-domain nearest neighbor;
2. same mechanism using alternate terminology;
3. source-domain search if the candidate is a cross-domain transfer;
4. falsification-oriented query asking for the strongest established equivalent or predecessor.

Only after these independent passes may results be cross-fed for bounded follow-up searches.

## Evidence record

Each candidate audit should preserve:

- canonical candidate proposition;
- provider;
- exact search objective/query;
- retrieved source URL/title/date where available;
- normalized precedent claim;
- collision strength: direct / root-plus-residual / corroboration / no collision / ambiguous;
- whether the result was unique to that provider;
- final adjudication and rationale;
- whether Parallel deep-research escalation was required.

Secrets and API keys must never be committed. Authentication should use OAuth, environment variables, or host-level MCP credentials.

## Retrospective benchmark

Before making the ensemble mandatory for future promotions, test it against the repository's historical labeled record.

### Benchmark set

Construct a stratified sample from prior batches containing:

- candidates later rejected as familiar or already established;
- candidates that survived only after substantial narrowing;
- strict current survivors;
- cross-domain candidates where terminology mismatch made precedent search difficult.

The benchmark's primary positive class is **known historical false-novelty or narrowing cases**. Current survivors are not assumed to be genuinely novel; they are a stress-test set whose newly discovered collisions require adjudication rather than being automatically counted as false positives.

### Conditions

Run at least these retrieval conditions on the same canonical candidate text:

1. Exa alone;
2. Parallel Search alone;
3. Exa + Parallel union after independent passes;
4. ensemble + Parallel deep-research escalation for routine survivors.

Where a reproducible baseline from prior run logs exists, compare against the historical retrieval/adjudication outcome as well.

### Metrics

Primary metrics:

- **false-novelty catch rate**: fraction of known rejected/narrowed cases where the provider finds a collision sufficient to trigger correct rejection or narrowing;
- **unique collision yield**: credible collisions found by only one provider;
- **ensemble incremental recall** over the stronger single provider;
- **time-to-kill / search effort**: number of retrieval stages needed before a historical false novelty is correctly rejected or narrowed.

Secondary metrics:

- source quality distribution;
- rate of ambiguous apparent collisions requiring human/model adjudication;
- deep-research escalation rate;
- newly discovered credible collisions against current survivors.

Do not score a current survivor as a false rejection merely because a provider returns a superficially similar result. Collision adjudication remains substantive.

## Acceptance criteria

Adopt the routine Exa + Parallel ensemble as a mandatory protocol gate if testing shows at least one of the following without an unacceptable adjudication burden:

- materially higher false-novelty catch rate than either provider alone / the historical search process;
- meaningful unique collision yield from both providers, demonstrating genuine retrieval complementarity;
- materially earlier detection of known collisions, reducing wasted elaboration and deep-research cost.

If one provider contributes almost no unique useful collisions, simplify rather than preserving redundant complexity.

Parallel deep research remains an escalation layer only if it resolves a meaningful fraction of routine-survivor ambiguities or catches precedents missed by both routine providers.

## Failure handling

- Provider unavailable: record the failed lane; do not silently treat absence of results as evidence of novelty.
- Rate limit/auth failure: retry only within bounded policy, then mark the novelty gate incomplete.
- Search returns no results: record `no collision found`, never `original`.
- Conflicting adjudications: preserve both rationales and escalate only if the novelty decision depends on the conflict.

## Repository changes after benchmark validation

If the benchmark supports the ensemble:

1. update `PROTOCOL.md` to make the independent Exa + Parallel collision pass the default external novelty gate;
2. add a reusable retrieval/adjudication schema and runner documentation;
3. add benchmark fixtures and results under `analysis/` and/or `runs/`;
4. update `STATE.md` with provider availability and exact resume behavior;
5. preserve future provider-specific outputs in each substantive batch audit.

If the benchmark does not support both providers, retain only the components that demonstrably add retrieval recall or reduce search effort.
