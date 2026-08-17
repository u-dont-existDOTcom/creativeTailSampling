# Inner Signal Graph — inner-child therapy protocol merge plan

Date: 2026-08-17
Target repo: `u-dont-existDOTcom/innerSignalGraph`
Source repo: `u-dont-existDOTcom/creativeTailSampling`
Therapy semantic source checkpoint: `db591713a3feb0a1576943408ae356685c0034ec`
Source branch: `agent/inner-child-therapy-protocol-mermaid-20260817`

## Objective

Merge the current research-stage inner-child/reparenting therapy protocol into the existing executable Inner Signal Graph architecture. Do not create a parallel therapy engine. Reconcile the new Mermaid control surface with the existing `guide-graph-v1` JSON graph, planner, case variables, source maps, routing, guide packets, hypnosis gates, tests, and durable state.

The current owner request explicitly authorizes this therapy-policy merge and supersedes the older `state/CODEX-CURRENT-STATE.md` line saying not to copy r03 therapy changes. It does **not** authorize promotion to `stable` or a release.

## Mandatory authority recovery

Before changing anything:

1. Resolve the live `innerSignalGraph/main` head. At plan creation it was `a22f2e611fab778bf26b8e7215afbf85aba4ba5e`, but do not assume it is still current.
2. Read, in order: `AGENTS.md`, `.github/codex-repository.json`, `state/CODEX-CURRENT-STATE.md`, `README.md`, `AUTOPILOT.md`, `docs/INDEX.md`, `docs/ARCHITECTURE.md`.
3. Inspect the current runtime graph stack: `src/guide-graph/{contract,planner,validate,compiler,regressions,source-map}.mjs`, `guide-graphs/candidates/inner-child.graph.json`, `guide-graphs/source-maps/inner-child-guide.json`, `guide-graphs/source-maps/owner-amendments.json`, `guides/owner-amendments.json`, `tests/guide-graph.test.mjs`, `tests/therapy-routing.test.mjs`, the guide-packet tests, and A001/H001 difficult cases.
4. Resolve/fetch the live Creative Tail source branch. The source used for this plan must contain semantic checkpoint `db591713a3feb0a1576943408ae356685c0034ec` or a later descendant. If later commits are documentation/merge-plan only, keep `db591713…` recorded as the therapy semantic checkpoint.
5. Read the source protocol in this order:
   - `analysis/inner_child_protocol/STATE.md`
   - `analysis/inner_child_protocol/THERAPY-PROTOCOL-OVERVIEW.md`
   - all `analysis/inner_child_protocol/maps/*.md`
   - `analysis/inner_child_protocol/OWNER-CLARIFICATION-ONE-INNER-PARENT-20260817.md`
   - `analysis/inner_child_protocol/OPERATION-PERMISSION-AND-REQUIRED-FIELDS.md`
   - `analysis/inner_child_protocol/BOT-SAFETY-VALIDATION-PLAN.md`
   - `analysis/inner_child_protocol/PROTOCOL-GAP-LEDGER.md`
   - `analysis/inner_child_protocol/CANDIDATE-STATUS-LEDGER.md`
   - `analysis/inner_child_protocol/EVIDENCE-LEDGER.md`
   - `analysis/inner_child_protocol/ARTICLE-PROTOCOL-CROSSWALK.md`
   - relevant retrieval/run/verification records when a rule needs provenance.
6. Read current universal lessons from `u-dont-existDOTcom/universal-dev-architecture`, especially living Mermaid/control-surface guidance and current Codex/Git workflow lessons.

## Worktree / branch

Use an isolated worktree/task branch from the freshly resolved `origin/main`. Do not work directly on `main`, `stable`, or `runtime-diagnostics`.

Suggested branch: `agent/merge-inner-child-protocol-20260817`.

Use the protected PR path back to `main`. Never merge `runtime-diagnostics` into source. Do not advance `stable` in this task.

## Non-negotiable protocol semantics

### One inner parent, three qualities

There is **one inner parent / integrated adult**. `Nurturer`, `Protector`, and `Guide` are three distinguishable qualities/functions of that one parent, not three inner parents or three independent internal people.

The analytic split exists because the qualities can be uneven, context-specific, temporarily unavailable, confused with maladaptive substitutes, and borrowed/developed one at a time. The developmental target is integration into **one coherent parental presence**.

This must be represented in the executable graph, prompts, source maps, tests, and owner amendments as an anti-reification invariant.

### Other mandatory semantics

- Permission/risk routing precedes operation selection.
- Safety is longitudinal/multi-turn, not only single-turn.
- Capacity/readiness is operation-specific; do not use one global `ready/not ready` identity as the primary gate.
- Loss of orientation/meaningful choice/function outranks depth; distress alone is not a universal stop signal.
- Optional introspection requires present consent. A clear `not now` stops/changes that optional exercise. A later attempt is not owed and requires renewed consent. Do not encode a scheduled/precommitted retry loop.
- Thin interface, not inner constitution: internal states report; Protector alarms trigger review rather than truth/permanent veto; Guide proposes; Nurturer cares; the present adult integrates facts/values/obligations/expertise and owns external behavior/consequences.
- Nurturer warmth/non-cruelty is not payment for obedience, success, gratitude, or agreement. Limits can still exist.
- Adult capacity is function × context, not one scalar.
- Parentification: preserve genuine competence. Separate developmental evidence of parentification from current costly overfunctioning/function imbalance. If history is unknown, describe the imbalance and do not invent the etiology.
- Prediction-based, domain-specific trust repair.
- Broken-promise loop: `miss → acknowledgment → impact → repair → diagnosis → resize/renegotiate → return`, not shame → larger vow.
- No-arrears: abolish punitive accumulation of missed internal-care practice, **not** external accountability/restitution or dose-sensitive therapy requirements.
- Pain is not the admission ticket to care: ordinary positive inner-parent/child contact includes play, curiosity, beauty, companionship, celebration, silliness, exploration, and trying things badly.
- Provenance is a runtime epistemic gate. Direct memory, testimony, inference, imagery/rescripting, felt sense, dream, hypnosis, altered state, metaphor/symbolic material, and uncertainty remain distinguishable. Salience/confidence cannot silently rewrite source class.
- Preserve the owner's modal claim that felt sense **may** know something conditioning obscured while never treating felt sense as historical proof.
- Depth and integration are independent axes. Do not redefine depth as integration.
- Internalization is not self-sufficiency. Preserve `receive → observe → participate → initiate → internalize` for the reparenting function while allowing healthy continuing therapy/friendship/community/co-regulation/practical support.
- Outcome failure uses a differential: misunderstanding, implementation, repetition/dose/duration, sequencing, prerequisites/support, delivery mismatch, protocol nuance/gap, adjunct need, evidence against a narrower mechanism, and only after stronger evidence challenge to the broad owner thesis. Adverse deterioration overrides `just keep practicing`.
- The composite protocol is research-stage. Do not make the runtime or UI claim that the unified treatment itself is clinically validated.

## Integration strategy

### 1. Preserve research provenance locally

Add a compact imported-protocol provenance area in `innerSignalGraph` (choose a repo-consistent path, e.g. `docs/therapy-protocol/`) containing:

- source repo + source branch + semantic source SHA;
- canonical overview and/or a lossless snapshot/reference of the Mermaid maps needed to review the runtime translation;
- owner clarification(s);
- operation-permission contract;
- bot-safety validation plan or a lossless local reference/snapshot;
- a crosswalk showing Creative Tail protocol nodes → executable `guide-graph-v1` nodes/variables/tests.

Do **not** make runtime behavior depend on network access to Creative Tail. The pin is provenance, not a runtime fetch.

Do not copy the explanatory article prose into runtime as part of this task. The Creative Tail work explicitly kept article editing separate from protocol hardening.

### 2. Extend owner amendments/source maps

Update `guides/owner-amendments.json` and the graph/source-map ownership layer with explicit owner-approved rules for the new semantics. At minimum cover:

- one inner parent / three qualities;
- function × context;
- optional-introspection consent/no automatic retry;
- thin role interface;
- non-withdrawable Nurturer care;
- broken-promise repair;
- no-arrears boundary;
- positive contact outside crisis;
- parentification competence/etiology distinction;
- global provenance handling;
- depth ≠ integration;
- internalization ≠ self-sufficiency;
- felt-sense modal claim + historical-proof safeguard;
- differential outcome failure;
- operation-specific permissions and longitudinal bot safety.

Use stable amendment IDs and source refs. Do not convert research/provisional items into settled clinical facts.

### 3. Migrate case variables and permissions

The existing contract currently has global summaries such as `inner_adult_access`, `deep_work_readiness`, and `basic_reparenting_capacity`. Do not let these remain the primary decision architecture.

Translate `OPERATION-PERMISSION-AND-REQUIRED-FIELDS.md` into the existing contract/planner with the smallest coherent change. Requirements:

- operation-specific permission/required-field logic;
- explicit `unknown` behavior: unknown constrains operations that require the missing field rather than globally inventing readiness or blocking all support;
- state freshness where the source protocol requires it;
- separate availability of the inner parent's nurturing/protecting/guiding qualities in the current relevant context;
- preserve backward compatibility only where needed for existing fixtures/packets, and mark legacy global summaries as compatibility outputs rather than authoritative gates;
- no hidden boolean that collapses the whole person into `ready`.

If a structured context profile is necessary, revise the contract deliberately with validators/tests rather than hiding it in prompt prose.

### 4. Replace planner-wide global deferral with operation permissions

Refactor the current planner so the pre-operation safety/permission layer decides which classes of therapeutic operation are allowed before node selection.

Do not keep a hard-coded rule equivalent to `deep_work_readiness !== yes → defer all deep nodes` as the primary architecture. Preserve compatibility only while migrating old fixtures.

The planner must distinguish at least:

- grounded support/ordinary conversation;
- witness/borrowed-quality work;
- protector/guard work;
- identity/differentiation work;
- ordinary child contact/reparenting;
- trust/promise repair;
- deeper memory/dialogue work;
- hypnosis/altered-state/depth-amplifying work;
- integration/recovery;
- external support/escalation.

Use the exact O0–O10 operation definitions from the source document rather than inventing new ones if they already cover these classes.

### 5. Translate all nine Mermaid drill-downs into the executable graph

Update `guide-graphs/candidates/inner-child.graph.json` rather than creating a second runtime graph.

Every material behavior-changing node/edge from the canonical overview/drill-downs needs one of:

- an executable graph node/edge/effect;
- an explicit crosswalk entry showing it is already implemented elsewhere;
- a documented `PROVISIONAL / not runtime` disposition.

Do not copy rejected novelty candidates into the active path merely because they appear in research history.

The graph should encode the one-inner-parent ontology. It may expose separate nurturing/protecting/guiding functions for assessment/routing, but must not model them as three autonomous agents.

Regenerate compiled graphs/bundle through the repository's compiler; do not hand-edit compiled artifacts.

### 6. Reconcile somatic/hypnosis routing

Preserve existing useful cross-guide behavior, but update gates where the new protocol changes them:

- sober baseline and operation-specific capacity before deliberate depth amplification;
- provenance discipline for hypnosis/dream/altered-state material;
- depth/access/intensity separate from integration;
- unresolved integration/recovery can defer further deliberate depth without a fixed calendar delay;
- irreversible/high-stakes altered-state conclusions get sober/regulatory review unless immediate safety requires action;
- no forced introspection/exposure via hypnosis.

Keep the application's existing ownership of hypnosis consent, route isolation, and waking return.

### 7. Longitudinal bot safety

Translate `BOT-SAFETY-VALIDATION-PLAN.md` into deterministic/adversarial regression coverage and, where necessary, runtime trajectory state.

At minimum test the documented multi-turn failure families:

- avoidance ↔ reassurance;
- dependency ↔ chatbot authority;
- imagery/felt sense ↔ historical certainty;
- parts language ↔ reification;
- `growth` ↔ coercion;
- miss/failure ↔ punitive debt/overpromising;
- intensity ↔ intensity chasing;
- broad-model interpretation ↔ self-sealing.

A response being empathic on one turn does not make the trajectory safe.

### 8. Update extraction/prompts/orchestration only as required by the deterministic graph

If new case variables/permissions are required, update the structured case extraction, schemas/validators, context builder, operational diagnosis, realization constraints, and response contract so the deterministic planner receives the information it actually needs.

Do not make the LLM the hidden source of policy. The graph/permission layer should own policy; models may extract, formulate, critique, and realize within it.

### 9. Preserve historical fixtures; create a fresh candidate revision

Do not mutate r01/r02 historical guide-packet fixtures merely to make history look current. If the graph/packet must advance, create the next candidate revision (r03 if unused on live `main`, otherwise the next free revision) from current `main` + this source protocol.

Do **not** cherry-pick/resurrect an old unrelated `r03` therapy branch simply because the stale checkpoint mentions it. This task's source is the pinned Creative Tail protocol.

## TDD / required regression cases

Write failing tests before implementation for behavior that is changing. At minimum cover:

1. Nurturer/Protector/Guide are three qualities of one inner parent, not independent parents/agents.
2. One quality can be missing/borrowed without treating the entire inner adult as absent.
3. Function availability can differ by context.
4. Clear refusal stops an optional introspective operation now; it does not create an automatic retry obligation and does not erase external responsibility.
5. Nurturer care remains available during refusal/failure/limit-setting.
6. Protector alarm triggers review, not automatic factual danger/permanent veto.
7. Guide proposes; it cannot compel optional introspection.
8. Broken promise routes through acknowledgment/impact/repair/diagnosis/renegotiation/return rather than compensatory overpromise.
9. No-arrears does not erase external restitution or required therapeutic dose.
10. Provenance source class survives later confidence/salience changes.
11. Felt sense can remain meaningful without becoming historical proof.
12. Depth can rise while integration stays poor; mild depth can integrate well.
13. Internalized function can coexist with continuing healthy external support.
14. Parentification is not inferred from current competence when developmental evidence is unknown.
15. Positive ordinary child/inner-parent contact can be selected outside crisis.
16. Poor outcome routes through the differential failure tree before broad-model abandonment or endless identical retry.
17. Unknown/stale required fields constrain only the operations that need them.
18. Operation-specific readiness allows a lower-demand useful operation without requiring global stabilization.
19. Longitudinal VAIL-style failure trajectories are detected/repaired.
20. Existing A001 credibility case and H001 borrowed-adulthood/hypnosis behavior do not regress.
21. Existing somatic discrete-event exception remains valid where the new operation-specific gate says it is permitted.
22. Legacy packet/graph fixtures either continue to validate under compatibility rules or are intentionally versioned rather than silently rewritten.

Use the full adversarial set in `BOT-SAFETY-VALIDATION-PLAN.md`, not only these examples.

## Documentation/state changes

Create an accepted design + implementation plan under `docs/superpowers/specs/` and `docs/superpowers/plans/` before code changes.

Update at least:

- `docs/ARCHITECTURE.md` with the new permission layer and one-inner-parent semantics;
- `state/CODEX-CURRENT-STATE.md` to remove/supersede the stale `Do not copy r03 therapy changes` instruction and record this merge source/pin;
- `THERAPY-LESSONS` with durable lessons from the merge;
- graph/source-map/report artifacts as appropriate;
- `docs/INDEX.md` if adding canonical design/plan docs.

If you edit `README.md`, `AGENTS.md`, `docs/INDEX.md`, `SECURITY.md`, or `CONTRIBUTING.md`, update the reviewed SHA-256 bindings in `scripts/audit-repository.mjs` in the same change, per repository policy.

Do not falsely clear the unrelated installed-GitHub-App-permissions blocker/issue 4.

## Verification gates

Run fresh, on the final task-branch head:

```bash
npm ci --ignore-scripts
npm test
npm run graph:test
npm run therapy-lessons:verify
npm run audit:repository
npm run audit:publication
npm run verify
```

Run targeted graph/therapy/guide-packet tests repeatedly during implementation, not only at the end.

`npm run audit:publication:hosted` is only needed if this task changes hosted/publication controls or the current repository policy explicitly requires fresh hosted evidence; do not perform unrelated hosted mutations.

Inspect the final diff and generated/package artifacts. No success claim without the fresh outputs.

## PR / merge / release boundary

- Push the task branch and open a PR to protected `main`.
- Record in the PR: live target base SHA, Creative Tail semantic source SHA `db591713…` (or a later owner-approved semantic descendant), source branch, main graph changes, compatibility decisions, tests, and unresolved/provisional items.
- Wait for required checks: `deterministic-package`, `workflow-policy`, `codeql-javascript`, plus any newly required checks on live `main`.
- Resolve review conversations and merge through the protected path only after required checks pass.
- After merge, verify the resulting `main` SHA and required checks/readback; record the immutable receipt in the PR/comment/state pattern used by this repo.
- **Do not promote or merge to `stable`**. Stable/release authority remains owner-gated and was not granted by this task.

## Completion criteria

This task is complete only when:

- the executable Inner Signal graph/runtime embodies all active source-protocol rules that change bot behavior;
- every source protocol rule has a runtime/crosswalk/provisional disposition;
- the one-inner-parent/three-qualities ontology cannot be misread by the graph or prompts;
- operation permissions replace global-readiness gating as the authoritative routing model;
- bot-safety longitudinal regressions exist;
- source provenance is pinned and inspectable;
- historical artifacts are not silently rewritten;
- all target-repo tests/audits/package gates pass on the final branch head;
- the PR is merged to protected `main` with final evidence;
- `stable` remains unchanged.
