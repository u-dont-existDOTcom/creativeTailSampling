# Parallel Task MCP fresh-chat execution smoke test

Date: 2026-08-16
Mode: research/state maintenance only; no article editing
Branch: `agent/federation-ecology-gap-continuation-20260816`

## Purpose

Verify actual Parallel Task/deep-research execution in a fresh ChatGPT conversation created after the user added the Task MCP. The prior conversation could not see a Task namespace, so schema visibility alone was not sufficient evidence.

This smoke test does **not** reopen the completed federation/experimental-ecology lane and does **not** backfill Batches 65–68. Those batches made zero strict Creative-Tail originality promotions, and Batch 68 reached the lane stopping rule.

## Branch resolution before execution

Live heads were resolved before the tool call:

- `u-dont-existDOTcom/creativeTailSampling:agent/federation-ecology-gap-continuation-20260816` = `c35bfb64b078bdd53e3e49fef7526156a29d9f2a`
- `u-dont-existDOTcom/communities:agent/federation-ecology-gap-continuation-20260816` = `f344d979f7b8f1c2991408b969240d3ed482d4a3`

The fresh handoff, Task addendum, `PROTOCOL.md`, `STATE.md`, `FINDINGS.md`, retrieval runbook/final synthesis, Batches 65–68, Communities workflow architecture, research state, final synthesis, and canonical current gap-bank manifest were reconciled before any substantive continuation.

## Actual Task execution

### `createDeepResearch`: PASS

A real Task deep-research call was executed with a deliberately small, read-only, already-settled empirical query about historical FEC LEX/LETS exchange and the later move away from parity/debt-style transactional accounting.

The connector accepted the request and returned:

- run ID: `trun_201682d6febd4300b1742888d33c1c53`
- interaction ID: `trun_201682d6febd4300b1742888d33c1c53`
- status at creation: `queued`
- processor: `pro`
- platform URL: `https://platform.parallel.ai/view/task-run/trun_201682d6febd4300b1742888d33c1c53`
- created at: `2026-08-16T13:45:16.637213Z`

This is sufficient to establish that **actual Task creation/execution is exposed in this fresh chat**. It is not merely schema visibility.

### Follow-up status/result control: connector-dispatch problem

After the user explicitly said `continue`, the conversation attempted the exposed lightweight `getStatus` action for the same run ID.

The dispatch failed with:

> `Resource not found: Parallels_Task_MCP.getStatus.`

The harness then instructed the conversation to rediscover the tools. Rediscovery again showed the Task namespace and four exposed functions (`createDeepResearch`, `createTaskGroup`, `getResultMarkdown`, `getStatus`), but a subsequent filtered discovery became inconsistent and listed only the ordinary installed connectors.

Disposition:

- **Task creation capability: PASS.**
- **Task result-poll/retrieval capability in this exact chat: unresolved connector-dispatch issue.**
- Do not reinterpret the follow-up dispatch failure as evidence that `createDeepResearch` did not run.
- Before a future strict originality promotion depends on a Task report, verify that the created run can also be retrieved/adjudicated through `getStatus`/`getResultMarkdown` or another supported Task-result path.
- Do not launch duplicate deep tasks merely because result polling is temporarily unavailable; preserve and reuse the existing `trun_...` ID.

## Production-gate consequence

The benchmark-validated architecture remains unchanged:

1. retrieval-free generation;
2. hostile common-sense/user-familiarity veto;
3. latest Communities-corpus collision;
4. mandatory Exa routine semantic collision search;
5. Parallel Search optional corroboration/disagreement;
6. mandatory Parallel Task deep research **only before strict Creative-Tail originality promotion**;
7. consequence/coherence/testability gate;
8. promote only the residual.

A Task run being creatable does **not** convert article gaps into strict findings. The deep report must be retrievable and adjudicated before a strict promotion can occur.

## No federation backfill

Do not reopen G-026–G-028 merely because Task creation now works.

- Batches 65–68: zero strict promotions.
- G-026–G-028 remain article-facing gaps/applications, not strict Creative-Tail survivors.
- Batch 68: no G-029; federation/experimental-ecology lane closed under the stopping rule.
- Canonical Communities article-gap manifest remains `recovered/COMMUNITIES-ARTICLE-GAP-BANK-CURRENT.md`, G-001–G-028, 14 B / 10 C / 4 D.

## Next move

Research-only mode remains in force until the user explicitly authorizes article editing.

Routine work should now be limited to:

- resolving the Task result-retrieval control when a strict candidate actually needs the deep gate;
- source/state maintenance; or
- a genuinely new empirical dependency that meets the lane-reopening condition.

Do not manufacture another federation gap simply to exercise the newly available Task connector.
