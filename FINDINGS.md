# Creative Tail Sampling — Canonical Findings Index

Updated: 2026-08-15

Compact canonical index. Detailed derivations, literature collisions, empirical reconstructions, and rejected candidates are under `runs/`; reproducible data/calculations are under `data/` and `analysis/`.

A user familiarity veto or strong literature compression overrides earlier promotion.

## Current status

No accepted grand social-theory finding yet. The earlier multiplex/relational-unbundling branch failed the novelty gate and is historical/applied material only.

## Current surviving cross-domain connections

### C001 — Active normative edge-case search

**Status:** SURVIVING / provisional.

Transfer active learning + preference elicitation + regression testing into community governance.

Instead of maximizing abstract-values agreement, adaptively choose concrete cases most likely to distinguish members' plausible interpretations. Collect baseline responses independently, separate measurement from deliberation/socialization, and preserve resolved high-information cases as a versioned **constitutional regression suite**.

Caveat: moral judgments can be sequence-sensitive/unstable; replicate/randomize some cases and do not assume one fixed latent utility function.

### C003 — Asset-gated cultural mutation

**Status:** NARROW SURVIVOR / provisional.

Broad claims that property affects exit or innovation are old. Remaining candidate:

> **Collective branch inheritance can pre-filter which institutional variants receive enough inherited capital to become viable competitors.**

This can create **selection blindness**: a canonical form may appear superior when alternatives were systematically denied comparable land, tools, treasury, reputation, or other inherited resources before selection could test them.

A final targeted precedent attack in Batch 16 found adjacent work on group fission, institutional legacies, cultural group selection, social-protocell inheritance, and religious/organizational schism, but no close precedent explicitly modeling collective branch asset portability as a pre-selection filter on institutional variants.

Keep narrow. Demote on a close target precedent.

### C005 — Reproductive-variance / superstar-reproduction trap

**Status:** SURVIVING; strongest reproduction-specific result; empirically strengthened across three Hutterite samples/branches.

Mean viable-daughter output can substantially overstate how reproducible a community design is. The full parent-offspring distribution matters.

Distinguish:

1. historical spread;
2. mean reproduction;
3. typical reproducibility;
4. lineage robustness.

#### Manitoba Schmiedeleut anchor

For 49 reconstructed Manitoba colonies founded by 1970:

- recorded Manitoba daughters = 103;
- mean `K = 2.102`;
- median `K = 2`;
- population variance `1.724`;
- variance/mean `0.820`;
- recorded-Manitoba `P(K=0) = 4.08%`;
- top 10% of parents account for ~22.3% of daughters.

Historical period data also show stable Manitoba colony reproduction through 1918–1975: reported compound annual colony growth ~4.25%–5.75%, mean division interval ~13.6–15.2 years.

Scope warning: the genealogy field is Manitoba daughters only; cross-border daughters are omitted.

#### Batch 17 cross-branch replication — FEEFHS 1973 tables

To standardize censoring, Batch 17 reconstructed colonies founded **1918–1953 inclusive**, giving at least 20 years of possible daughter production before the 1973 table cutoff.

**Lehrerleut** (`n=29` mature parents):

- listed daughters = 53;
- mean `K = 1.828`;
- median `K = 1`;
- population variance `1.453`;
- variance/mean `0.795`;
- `P(K=0) = 3.45%`;
- top 10% share = `24.53%`;
- maximum `K = 5`.

**Dariusleut** (`n=33` mature parents):

- listed daughters = 60;
- mean `K = 1.818`;
- median `K = 2`;
- population variance `0.694`;
- variance/mean `0.382`;
- `P(K=0) = 0%`;
- top 10% share = `20.0%`;
- maximum `K = 3`.

The same qualitative result now appears across distinct Hutterite branches: mature-parent reproduction is broadly distributed, not jackpot-dominated. Subject to historical table/node-identity caveats, the Dariusleut cohort is especially striking because every mature cohort node reproduced at least once by the cutoff.

Operational shorthand: **make reproduction boring**. A strongly replicable community system should make daughter formation an ordinary lifecycle event for the median competent community rather than an exceptional achievement by a few charismatic or unusually capable founders.

Data / analysis:

- `data/hutterite_manitoba_mature_lineage_reconstruction.csv`
- `analysis/hutterite_reproduction_metrics.py`
- `data/hutterite_manitoba_period_growth_1918_1975.csv`
- `analysis/hutterite_period_growth_log_check.py`
- `data/hutterite_feefhs_1973_mature_cohorts.csv`
- `analysis/hutterite_feefhs_reproduction_metrics.py`

Full Batch 17 caveats and source normalization are in `runs/2026-08-15-orthogonal-tail-batch-17.md`.

### C006 — Descendant inflation / lineage-size sampling bias

**Status:** SURVIVING; audited against the user's real community-research corpus.

When daughter communities inherit parent culture, prolific lineages mechanically contribute more observations to present-day community samples. This is distinct from ordinary survivorship bias: even perfect enumeration gives descendant-rich lineages more sampling weight.

The correct weighting depends on the estimand:

- random founding attempt/root;
- random lineage;
- random extant community;
- random current resident;
- future movement culture/reproductive contribution.

Applied to `u-dont-existDOTcom/communities`, C006 does **not** invalidate the current mechanism-bounded P0 synthesis. Do not retrofit lineage weights there; carry genealogy/estimand controls into future comparative/prevalence analyses.

### C009 — Cohort-composition admission

**Status:** SURVIVING / provisional cross-domain operational transfer; narrowed in Batch 17.

Applicant utility may be **non-separable**: a candidate who looks poor against today's membership may belong to the best reachable future cohort, while individually acceptable applicants may compose into a poor cohort.

Batch 17 confirms a major scope condition: this matters only when the candidate market is sufficiently **thick**. Mature communes may often receive applicants too sparsely for batching to be useful; founding, daughter formation, new-site openings, expansion waves, and multiple simultaneous vacancies are stronger use cases.

Operational consequence when several plausible candidates genuinely overlap:

- retain a provisional candidate pool rather than finalize every acceptable applicant immediately;
- evaluate plausible candidate sets and interaction effects, not only individual fit;
- use joint trial periods where feasible;
- preserve voluntary exit and applicant autonomy;
- explicitly compare expected composition gain with vacancy, delay, and applicant-attrition costs.

Ottawa Cohousing's forming-stage matchmaking/affinity-group process is a near precedent and supports the founding-stage scope correction; no close established-community cohort-admission precedent based explicitly on applicant interaction effects has yet been found.

Demote if a close target precedent is found or if empirical interaction effects are trivial relative to individual fit.

### C010 — Governance fault injection

**Status:** SURVIVING / provisional cross-domain operational transfer from chaos engineering and continuity exercises.

Having backups and succession plans is not equivalent to testing whether they work.

Proposed transfer:

> Under bounded conditions, deliberately simulate or safely induce temporary loss of a key person, permission, account, service, or infrastructure component and observe the community's actual ability to preserve essential functions.

Examples include founder absence for one governance cycle, treasurer unavailability, loss of normal internet/phone access, facilitator absence, vehicle/supplier loss, or inaccessible records.

The distinctive element is **testing dependency loss**, not merely documenting a contingency plan. Generic continuity practice already uses key-person-unavailable scenarios, but target searches did not find systematic intentional-community use of recurring governance/dependency fault injection.

Safety boundary: never inject a live failure when plausible downside to health, children, medication, housing security, legal rights, or other necessities is material. Use tabletop/sandbox simulations for high-stakes functions.

Prediction: communities that test actual dependency loss will discover more hidden single points of failure than equally documented communities that only discuss backups.

### C011 — Shadow governance

**Status:** SURVIVING / provisional cross-domain operational transfer from shadow-mode / parallel-run deployment.

Intentional communities sometimes **live-pilot** a new governance system. The proposed intermediate step is different:

> Before transferring authority to a substantially new governance process, run it nonbinding in parallel on the same admissible cases and compare what it would have decided with the incumbent process.

Minimal architecture:

1. incumbent process remains authoritative;
2. shadow process receives the same admissible inputs;
3. shadow decision/reasoning/time/dissent/recusal/evidence requirements are logged;
4. analyze the **divergence cases**, not merely overall agreement;
5. only then decide whether to revise, live-pilot, adopt, or reject the new process.

Cambridge Cohousing reports a six-month live Dynamic Governance trial, demonstrating that governance pilots occur in the target domain; target searches have not yet found the same **parallel nonbinding decision comparison** structure.

Limits: shadow behavior may differ from live behavior, duplication costs time, sensitive personal cases may be inappropriate, and agreement does not prove legitimacy.

Prediction: shadow runs will expose high-impact decision divergences that abstract constitutional debate misses, especially around agenda control, evidence, vetoes, recusal, timing, and jurisdiction.

## Demoted / useful but not novel

### D001 — Flagship founder trap
Demoted after spinout/social-movement literature attack. Employee-spinout research already studies parent loss of key human capital/routines versus knowledge diffusion and offspring/ecosystem benefits.

### D002 — Multi-parent daughter recombination
Too close to cross-pollination/cultural recombination.

### D003 — Developmental-sequence replication
Too close to tacit knowledge/path dependence/lifecycle.

### D004 — Governance commutativity
Useful diagnostic; near-decomposability/interdependence/modularity owns the structural principle.

### D005 — Reproductive timing
Useful classic-demography measurement rule.

### D006 — Propagule burden / independent seedability
Useful distinction between reliable fission and de-novo seedability; propagule-size/fidelity literature already contains the mechanism.

### D007 — Effective number of reproducing communities
Potential tool derived from reproductive skew; not independent novelty.

### D008 — Low-base-rate evidence-lifecycle safeguard
Former C007. Demoted after safeguarding/personnel-vetting precedent attack. Useful applied safety architecture, not a tail discovery.

### D009 — Arithmetic-growth mirage under shared environmental variation
Former C008. Mathematically valid, but historical Manitoba Hutterite reproduction is too stable for the correction to matter materially in the best current exemplar.

### D010 — Failure-history inheritance
Useful practice but not novel: organizational-learning literature explicitly studies negative knowledge / knowing what not to do.

### D011 — Spatial-vs-temporal replication attention tradeoff
Rejected as novel after direct 2026 organizational-replication precedent: scaling new units and maintaining adherence in existing units compete for scarce attention.

### D012 — Evidence-lineage counting
Useful: many endorsers repeating one originating source do not create independent evidence. Too close to source-independence/provenance/pseudoreplication traditions for promotion.

### D013 — Governance feedback-lag / reform oscillation
Useful warning but too close to policy feedback, control-system delay, institutional repetition, and change-fatigue literatures.

## Hard rejection frontier

Do not repromote technical restatements of:

- commodification/alienation/specialization of social relations;
- thick-vs-thin ties, embeddedness, social capital, multiplex exchange;
- planned fission/propagule reproduction;
- cultural fidelity/complexity thresholds;
- source/sink dynamics;
- modularity/near-decomposability/interdependence;
- ordinary founder/lifecycle/path-dependence effects;
- generic schism/forkability;
- generic property/exit/liquidity effects;
- cooperative withdrawal/redemption bank-run logic;
- organizational forgetting;
- self-selection/endogeneity;
- survivorship/external-validity corrections;
- ordinary critical-slowing-down applications;
- newcomer-integration overload;
- generic common-cause risk/diversification;
- checks-and-balances/least privilege;
- policy experimentation/laboratories of democracy;
- generic matching/compatibility without non-separable cohort effects;
- generic business continuity / succession planning without a distinct transfer;
- generic pilots without the parallel nonbinding structure of C011.

## Method findings

- **M001:** formalization is not novelty.
- **M002:** user familiarity veto dominates model confidence.
- **M003:** nearest-neighbor literature attack is mandatory before promotion.
- **M004:** nonstandard structural cross-domain transfer can count; same-domain rediscovery cannot.
- **M005:** empty batches are successful; prefer no result to weak promotion.
- **M006:** terminology differences do not save a candidate when the target domain already implements the same structure.
- **M007:** a mathematically surprising transfer that does not materially affect the best available target case should be demoted until a real consequential case is found.

## Provenance

Latest detailed runs:

- `runs/2026-08-15-c007-adversarial-screen-13.md`
- `runs/2026-08-15-orthogonal-tail-batch-14.md`
- `runs/2026-08-15-c008-hutterite-empirical-test-15.md`
- `runs/2026-08-15-orthogonal-tail-batch-16.md`
- `runs/2026-08-15-orthogonal-tail-batch-17.md`

Earlier batches and the recovered pre-deletion snapshot remain under `runs/`.
