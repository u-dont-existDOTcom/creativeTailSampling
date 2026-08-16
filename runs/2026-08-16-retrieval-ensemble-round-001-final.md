# Retrieval Ensemble Round 001 — Final Synthesis

Date: 2026-08-16
Branch: `agent/exa-parallel-retrieval-ensemble`
Routine manifest SHA-256: `6bdbe5e0b75c9f1f0779f0084513d901372d084b9131e3ab6a567636c2fec40c`
Status: COMPLETE

## Question

Does Creative Tail Sampling improve its false-novelty control by adding Exa Search, Parallel Search, and Parallel Task as independent retrieval adversaries?

## Design

The benchmark froze 14 historical cases and four provider-independent query families before retrieval. Historical labels, known collision families, notes, and expected dispositions were hidden from providers.

Routine conditions:

1. Exa Search MCP — independent first pass.
2. Parallel Search MCP — independent first pass.
3. Ensemble — union/adjudication of those independent passes.

Deep condition:

4. Parallel Task `pro` — only for five surviving/boundary cases after routine adjudication: C001, C005, C006, C015, C025.

Raw routine evidence is under `analysis/retrieval_ensemble/results/round-001/raw/`. Deep outputs are under `analysis/retrieval_ensemble/results/round-001/deep/`.

## Historical false-novelty / narrowing benchmark

The positive set contained eight cases with pre-benchmark expected action `reject` or `narrow`.

Conservative routine scoring:

| Condition | Correct catches | Catch rate |
|---|---:|---:|
| Exa Search | 8 / 8 | 100% |
| Parallel Search | 2 / 8 | 25% |
| Exa + Parallel routine union | 8 / 8 | 100% |

Sensitivity scoring credits one borderline Parallel N018 result:

- Parallel Search: 3 / 8 = 37.5%.

Routine ensemble incremental recall over Exa: **0 / 8**.

### Routine provider character

**Exa Search:** repeatedly converted unusual candidate wording into the correct conceptual neighborhood. It found direct or root-plus-residual precedents across community resilience, organizational replication, substantive exit, institutional evolution, governance experimentation, matching markets, deprecation/tombstones, and adult exit/consent.

**Parallel Search:** useful as an independent corroborator in a few cases, but short keyword queries frequently locked onto lexical/polysemous neighbors rather than structural neighbors. Recurrent examples included `variant` → genetics/investment-brand noise, `commitment` → behavioral commitment-contract literature, and `adult transition` → generic adulthood-transition material.

Conclusion from routine benchmark: **mandatory Exa is justified; mandatory routine Parallel Search is not.**

## Current-survivor stress tests after routine retrieval

### C016 — Verifiably unpredictable federation audit sampling

**Demote from strict originality ledger.**

RFC 3797 already contains essentially the full mechanism: publish/freeze the eligible pool, prepublish the deterministic algorithm, use future public randomness unknown when the algorithm is fixed, use randomness outside administrator control, keep the published pool immutable, and make the realized selection publicly replayable. Parallel also found public-randomness-beacon material explicitly applying the same architecture to audit sampling.

Preserve as a practical design rule; it is not a Creative Tail Sampling originality finding.

### C015 — Governance rights-liveness verification

**Narrow strongly.**

Routine Exa already found voting/social-choice work explicitly using safety/liveness, formal voting verification, DAO/governance execution constraints, and real recusal/quorum/deadline rules. Deep Parallel Task then found even closer target-domain administrative-law work: multimember commissions whose legally granted authority becomes unusable because vacancies destroy quorum, plus ex-ante vacancy-continuity mechanisms, delegation, and procedural dead states.

Surviving residual:

> A unified adversarial reachable-state verification procedure for a whole governance-rights architecture, testing safety, liveness, and bounded liveness across interacting recusal, vacancy, quorum, deadline, delegation, jurisdiction, and noncooperation states.

The root proposition `a right may exist in text but be dead in practice` is not novel.

### C001 — Active normative edge-case search

**Root collision + narrow residual.**

Parallel Task found the component architecture distributed across established methods:

- reflective equilibrium and thought experiments use deliberately diagnostic cases to pressure-test principles;
- case-based legal reasoning uses strategically selected cases to discriminate interpretations;
- deliberative polling and Delphi preserve independent/pre-deliberative judgments before group interaction;
- constitutional-design experiments independently evaluate multiple concrete constitutional profiles;
- precedent and democratic experimentalism preserve prior resolutions/evidence for future institutional learning.

No single retrieved precedent contained the complete pipeline.

Surviving residual:

> Explicitly select discriminating/high-information normative cases, collect independent answers before deliberation, and preserve resolved cases as a durable regression-test suite for future constitutional/value interpretations.

Do not claim novelty for case-based moral reasoning, independent elicitation, deliberation sequencing, or precedent individually.

### C005 — Reproductive-variance / superstar-reproduction trap

**Root collision + narrow residual.**

Routine Exa found the exact source-domain distribution-not-mean literature. Parallel Task added closer target-domain evidence:

- Hutterite colony fission demography with parent/daughter structure;
- Amish church-district fission producing repeated daughter districts;
- organizational genealogy with explicit parent-progeny transfer;
- church multiplication and social-innovation scaling frameworks with parent/daughter reproduction.

These kill any broad claim that communal/organizational reproduction should be treated as parent→offspring rather than aggregate spread.

What remains:

> Use the **distribution of daughter units per parent community** as the actual communal reproducibility criterion — especially zero-daughter probability, median daughters, dispersion/variance, and concentration in prolific parent communities — rather than total descendant count or mean daughters alone.

No retrieved target-domain source used this full parent-indexed statistical bundle as the evaluative protocol.

### C006 — Descendant inflation / lineage-size sampling bias

**Root collision + narrow residual.**

Parallel Task found closer precedents than routine search:

- Hutterite fission datasets explicitly encode mother→daughter events;
- historical commune survival studies define sampling frames and sometimes aggregate all Hutterite colonies as a single commune;
- organizational genealogy and population ecology distinguish parent/progeny and founding/population units;
- cross-cultural sampling literature contains the broader dependence/unit-of-analysis problem.

Therefore `lineages differ in descendant counts` and `sampling units matter` are not novel.

Surviving residual:

> For communal replication research, explicitly declare the estimand and weighting rule — random founding attempt/root, lineage, extant community, current resident, or future movement contribution — and treat an extant-community sample as potentially descendant-size-biased rather than silently equating it with a sample of independent founding attempts.

### C025 — Community resolution / living-will architecture

**Root collision + narrow residual.**

Routine Exa found FEMA continuity/devolution planning for community-based organizations and nonprofits, including transfer of essential functions to another organization and separate reconstitution planning. Parallel Task added materially closer precedents:

- nursing-facility closure rules/practice where resident care becomes a transfer duty when the provider closes;
- Community Land Trust dissolution rules that transfer land/housing assets to successor nonprofit/governmental stewardship rather than preserve the original corporation;
- nonprofit dissolution/continuity doctrine;
- NIST/CISA multi-function community-resilience frameworks.

This defeats broad originality for `preserve essential functions even when an organization is disrupted or dissolved` and for housing stewardship surviving a legal entity.

Surviving residual:

> An integrated **permanent communal dissolution** protocol that preassigns successor/bridge responsibility across the complete member-critical bundle — housing, food/water, medication/care, childcare/education, cash/benefits, transport, records, family contact, and animal/land obligations — without making recovery/reconstitution of the commune itself the prerequisite for continuity.

## Parallel Task value

Unlike routine Parallel Search, Parallel Task materially changed the evidence picture.

It produced useful new target-domain or near-target precedents on all five escalated cases. The most consequential additions were:

1. **C005:** direct Hutterite/Amish parent→daughter fission and organizational genealogy, sharply isolating the residual to the statistical distributional rule.
2. **C006:** explicit commune sampling/aggregation choices and population/genealogy precedents, isolating the residual to descendant-size-biased estimand control.
3. **C025:** nursing-home closure transfer duties and CLT dissolution stewardship, shrinking the residual from generic `community living will` to an integrated multi-function permanent-dissolution protocol.
4. **C015:** direct administrative-law quorum/vacancy paralysis, strengthening the root collision and isolating the unified formal-verification residual.
5. **C001:** component-by-component target precedents, isolating novelty to the complete discriminating-case → independent-answer → deliberation → regression-suite pipeline.

Thus Parallel Task earns its place as a **survivor escalation lane**, even though Parallel Search does not earn mandatory routine status.

## Final architecture decision

Adopt the following external novelty gate:

1. **Generate without web retrieval.** Preserve creative independence; retrieval must not drag generation toward known material.
2. **Run active-project corpus collision first.** Internal rediscovery is demoted before external spend.
3. **Run Exa routine semantic collision attack — mandatory.** Use independent query families aimed at target neighbor, alternate terminology, source-domain transfer, and falsification.
4. **Adjudicate and fetch primary/full sources where needed.** A search hit is not itself a collision.
5. **Parallel Search — optional corroboration/disagreement lane, not mandatory.** Use when cheap independent retrieval is useful, but do not treat it as a required promotion gate based on Round 001.
6. **Parallel Task deep research — mandatory for a candidate that would otherwise enter the strict originality ledger after routine Exa.** Escalate only surviving/boundary candidates; do not spend on already-rejected candidates.
7. **Promote only the residual that survives both stages.** A provider returning nothing is never evidence of originality.

This keeps creative recall low during generation and precedent recall high during promotion.

## Method conclusions

- Semantic retrieval diversity matters more than simply adding another keyword engine.
- Provider disagreement is diagnostic: Exa repeatedly escaped literal-word traps that caught Parallel Search.
- Deep multi-source research can still add value even when the same vendor's shallow search did not.
- The strict originality ledger should be narrower after retrieval, not protected from retrieval.
- C016 is the benchmark's cleanest proof that the new gate prevents a plausible but false cross-domain novelty promotion.

## Final Round 001 verdict

**Adopt modified B:**

- **Exa routine: YES, mandatory.**
- **Parallel Search routine: NO, optional.**
- **Parallel Task survivor escalation: YES, mandatory before strict promotion.**

This replaces the original assumption that Exa and Parallel Search should both be routine mandatory adversaries.
