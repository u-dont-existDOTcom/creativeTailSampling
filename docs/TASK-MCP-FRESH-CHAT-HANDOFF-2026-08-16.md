# Task MCP fresh-chat handoff addendum

Updated: 2026-08-16 ~14:00 UTC
Mode: research state handoff; no article editing authorization implied

## Why this addendum exists

The user added the Task MCP after an older ChatGPT conversation had already been created. That older conversation could not see a Task namespace, so it could not distinguish `new MCP not visible to this conversation` from `MCP itself broken`.

A new post-registration conversation has now executed a real Parallel Task request. This file therefore **supersedes older `Parallel Task: BLOCKED / not exposed` status statements wherever they still appear in the earlier handoff/state prose**. Those older statements remain historically accurate for the old conversation but are no longer the current capability result.

Full audit:

- `runs/2026-08-16-task-mcp-fresh-chat-smoke-test.md`

## Fresh-chat actual execution result

### Task creation / deep-research execution: PASS

The fresh conversation resolved the live heads first:

- `u-dont-existDOTcom/creativeTailSampling:agent/federation-ecology-gap-continuation-20260816` = `c35bfb64b078bdd53e3e49fef7526156a29d9f2a` before the smoke-test persistence commits;
- `u-dont-existDOTcom/communities:agent/federation-ecology-gap-continuation-20260816` = `f344d979f7b8f1c2991408b969240d3ed482d4a3`.

It then executed a real `createDeepResearch` call using a deliberately small, read-only, already-settled empirical FEC exchange question.

The connector accepted the call and returned:

- run / interaction ID: `trun_201682d6febd4300b1742888d33c1c53`;
- processor: `pro`;
- creation status: `queued`;
- platform URL: `https://platform.parallel.ai/view/task-run/trun_201682d6febd4300b1742888d33c1c53`;
- created at: `2026-08-16T13:45:16.637213Z`.

This establishes **actual Task creation/execution capability**, not merely schema visibility.

### Follow-up status/result retrieval: unresolved connector-dispatch issue

After the user explicitly instructed the fresh conversation to continue, it attempted the exposed lightweight `getStatus` action against the same `trun_...` ID.

The harness returned:

> `Resource not found: Parallels_Task_MCP.getStatus.`

Tool rediscovery was inconsistent afterward: one discovery exposed the four Task functions (`createDeepResearch`, `createTaskGroup`, `getResultMarkdown`, `getStatus`), while a later filtered discovery listed only ordinary installed connectors.

Current disposition:

- **Task creation: PASS.**
- **Task report polling/retrieval in this exact conversation: unresolved connector-dispatch problem.**
- Do not reinterpret the polling failure as evidence that the Task run was not created.
- Do not relaunch a duplicate paid/deep task merely because polling is unavailable; preserve/reuse the existing `trun_...` identifier.
- Before any future strict originality promotion depends on a Parallel Task report, verify that the report itself can be retrieved and adjudicated through `getStatus`/`getResultMarkdown` or another supported Task-result path.

## Production gate remains unchanged

The validated production rule remains:

1. retrieval-free generation;
2. hostile common-sense/user-familiarity veto;
3. latest Communities-corpus collision;
4. mandatory Exa routine semantic collision search;
5. Parallel Search optional corroboration/disagreement;
6. mandatory Parallel Task deep research **before strict Creative-Tail originality promotion**;
7. consequence/coherence/testability gate;
8. promote only the residual.

Task creation being available does not itself clear step 6. A strict promotion requires the deep report to be retrieved and adjudicated.

## Important: there is no mandatory Task backlog from Batches 65–68

Batches 65–68 made **zero strict originality promotions**. Their outputs were article gaps, empirical findings, and practical lessons. They therefore did not violate the strict-promotion gate when Task was unavailable in the older conversation.

The federation/experimental-ecology gap-discovery lane reached its stopping rule in Batch 68 and remains closed. Do **not** reopen G-026–G-028 merely because Task creation now works.

Task is required only when:

- a future candidate is being considered for the strict `FINDINGS.md` originality ledger; or
- the user explicitly asks to deep-adjudicate an existing article-gap residual for originality.

## Current research checkpoint

Canonical fresh handoff:
- `docs/FRESH-CONVERSATION-HANDOFF.md`

This Task capability addendum:
- `docs/TASK-MCP-FRESH-CHAT-HANDOFF-2026-08-16.md`

Task execution audit:
- `runs/2026-08-16-task-mcp-fresh-chat-smoke-test.md`

Canonical Creative Tail state:
- `STATE.md`
- `FINDINGS.md`

Current Communities article-gap manifest:
- `u-dont-existDOTcom/communities/recovered/COMMUNITIES-ARTICLE-GAP-BANK-CURRENT.md`

Current article-gap bank:
- G-001 through G-028;
- 14 B / 10 C / 4 D.

Federation lane:
- Batches 65–68 complete;
- G-026 mobility interface;
- G-027 purpose-specific intercommunity accounting / liability;
- G-028 federation constitutional casebook;
- no G-029;
- lane closed after Batch 68 yielded no defensible new gap.

## Next substantive step

Research mode remains in force until the user explicitly authorizes article editing.

If article harmonization is authorized, use `COMMUNITIES-ARTICLE-GAP-BANK-CURRENT.md` as the change specification, verify publication-facing load-bearing evidence selected for insertion, preserve the user's thesis/arguments, and only afterward proceed to humanization.

If article editing is not authorized, do not manufacture more federation gaps. Restrict work to concrete source verification/state maintenance, resolving the Task-result retrieval path when it is actually needed, or a genuinely new empirical dependency that satisfies the federation-lane reopening condition.

## Starter for a later fresh conversation

> Continue my intentional-community Creative Tail / article-gap project from `u-dont-existDOTcom/creativeTailSampling` and `u-dont-existDOTcom/communities`. Read `creativeTailSampling/docs/FRESH-CONVERSATION-HANDOFF.md` and then `creativeTailSampling/docs/TASK-MCP-FRESH-CHAT-HANDOFF-2026-08-16.md`; the latter supersedes older statements that Parallel Task was unavailable. Resolve the live heads of both `agent/federation-ecology-gap-continuation-20260816` branches before work. Preserve the production gate: retrieval-free generation, hostile common-sense veto, latest Communities-corpus collision, mandatory Exa routine search, and mandatory Task deep research only before strict Creative-Tail originality promotion. Do not reopen G-026–G-028 merely because Task creation works: Batches 65–68 made zero strict promotions and the federation/experimental-ecology gap lane is closed after Batch 68 reached the stopping rule. The canonical article-gap manifest is `communities/recovered/COMMUNITIES-ARTICLE-GAP-BANK-CURRENT.md` with G-001–G-028. Research only unless I explicitly authorize article editing. Save durable results back to GitHub and continue automatically through routine next steps.
