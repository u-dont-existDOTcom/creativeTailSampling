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

#### Cross-branch replication — FEEFHS 1973 tables

Standardized mature cohort: colonies founded **1918–1953 inclusive**, giving at least 20 years of possible daughter production before the 1973 cutoff.

**Lehrerleut** (`n=29` mature parents): daughters 53; mean `K=1.828`; median 1; population variance `1.453`; variance/mean `0.795`; `P(K=0)=3.45%`; top-10% share `24.53%`; max `K=5`.

**Dariusleut** (`n=33` mature parents): daughters 60; mean `K=1.818`; median 2; population variance `0.694`; variance/mean `0.382`; `P(K=0)=0%`; top-10% share `20.0%`; max `K=3`.

The same qualitative result appears across distinct Hutterite branches: mature-parent reproduction is broadly distributed, not jackpot-dominated.

Operational shorthand: **make reproduction boring**. A strongly replicable community system should make daughter formation an ordinary lifecycle event for the median competent community rather than an exceptional achievement by a few unusually capable founders.

#### Non-Hutterite screen

A public row-level church-planting genealogy sufficient for a comparable `K` distribution has not yet been found. Aggregate church-planting evidence suggests reproduction is much less routine, but follow-up, unit definitions, subsidy, and mechanisms differ too much for a numerical Hutterite-vs-church effect size. Use only as qualitative context.

Data / analysis:

- `data/hutterite_manitoba_mature_lineage_reconstruction.csv`
- `analysis/hutterite_reproduction_metrics.py`
- `data/hutterite_manitoba_period_growth_1918_1975.csv`
- `analysis/hutterite_period_growth_log_check.py`
- `data/hutterite_feefhs_1973_mature_cohorts.csv`
- `analysis/hutterite_feefhs_reproduction_metrics.py`

### C006 — Descendant inflation / lineage-size sampling bias

**Status:** SURVIVING; audited against the user's real community-research corpus.

When daughter communities inherit parent culture, prolific lineages mechanically contribute more observations to present-day community samples. This is distinct from ordinary survivorship bias: even perfect enumeration gives descendant-rich lineages more sampling weight.

The correct weighting depends on the estimand: random founding attempt/root, random lineage, random extant community, random current resident, or future movement culture/reproductive contribution.

Applied to `u-dont-existDOTcom/communities`, C006 does **not** invalidate the current mechanism-bounded P0 synthesis. Carry genealogy/estimand controls into future comparative/prevalence analyses.

### C009 — Cohort-composition admission

**Status:** SURVIVING / provisional cross-domain operational transfer; market-thickness bounded.

Applicant utility may be **non-separable**: a candidate who looks poor against today's membership may belong to the best reachable future cohort, while individually acceptable applicants may compose into a poor cohort.

This matters only when the candidate market is sufficiently thick. Mature communes may receive applicants too sparsely for batching to be useful; founding, daughter formation, new-site openings, expansion waves, and multiple simultaneous vacancies are stronger use cases.

When several plausible candidates genuinely overlap: retain a provisional pool, evaluate candidate sets/interaction effects, use joint trials where feasible, preserve voluntary exit/autonomy, and compare composition gains with vacancy/delay/attrition costs.

Ottawa Cohousing's forming-stage matchmaking/affinity-group process is a near precedent. No close established-community cohort-admission precedent based explicitly on interaction effects has yet been found.

### C011 — Shadow governance

**Status:** SURVIVING / provisional cross-domain operational transfer from shadow-mode / parallel-run deployment.

Before transferring authority to a substantially new governance process, run it nonbinding in parallel on the same admissible cases and compare what it would have decided with the incumbent process.

Minimal architecture: incumbent remains authoritative; shadow process receives the same admissible inputs; log its decision/reasoning/time/dissent/recusal/evidence requirements; analyze **divergence cases**; only then revise, live-pilot, adopt, or reject.

Target searches found live governance trials and adjacent “shadow government” projects, but not the same-case nonbinding parallel decision-comparison architecture in intentional communities.

Limits: shadow behavior can differ from live behavior, duplication costs time, sensitive cases may be inappropriate, and agreement does not prove legitimacy.

### C012 — Standing constitutional-relation testing

**Status:** SURVIVING / provisional, **narrowed after Batch 19 nearest-neighbor attack**.

Identity-swapped paired testing itself is old: audit studies and matched-vignette experiments already vary race, sex, names, status, or other attributes while holding relevant facts constant.

The remaining proposed transfer is a **versioned constitutional relation suite** that tests several relations a community claims should hold even when no one knows the uniquely correct answer:

- irrelevance/invariance;
- symmetry between normatively equivalent parties;
- monotonicity when relevant evidence strengthens;
- jurisdiction invariance when proposer identity changes;
- other predeclared relational properties specific to the community's rules.

Workflow: state the expected relation first; create minimally transformed cases; blind/randomize where feasible; process independently; compare decisions and reasons; diagnose failures; preserve informative cases as regression tests.

C001 vs C012:
- **C001** discovers where members' values differ;
- **C012** tests whether the process follows relations already claimed.

Demote if target-domain governance already maintains substantially equivalent standing relational/property test suites.

### C013 — Federated applicant clearinghouse / pooled matching market

**Status:** SURVIVING / provisional cross-domain operational transfer; matching-market mechanism itself is known.

The user's C009 scarcity objection exposes a scale mismatch: an individual commune can have a thin applicant market even when the **movement-wide** market is thick.

Current intentional-community/ecovillage infrastructure is primarily directories, profiles, classifieds, compatibility search, and local admission. Kibbutz movement infrastructure aggregates accepting settlements and supports local absorption; Bruderhof centrally allocates committed members within one worldwide body. A strong adjacent precedent exists in Israel's Mechinot residential gap-year network, which has run a centralized matching market across dozens of programs and thousands of applicants with rich diversity constraints.

The proposed intentional-community transfer is therefore not “invent matching,” but:

> pool openings and seekers across autonomous communities, coordinate exploration and later commitments, while preserving reciprocal choice and local admission.

Recommended **dynamic/hybrid** architecture rather than forced one-shot assignment:

1. communities publish openings, hard constraints, trial windows, and relevant characteristics;
2. seekers/households publish needs, hard constraints, preferences, skills/interests, and mobility limits;
3. system proposes several plausible mutual exploration matches;
4. visits/trials let both sides discover preferences;
5. later, both sides mark/rank acceptable matches;
6. a coordinated round recommends commitments while preserving opt-out;
7. communities with multiple openings can optionally apply C009 cohort analysis;
8. unmatched participants return to later rounds without strategic waitlist rewards.

Prediction: if local thinness matters, pooling should reduce simultaneous `compatible seeker unmatched + suitable vacancy open` states and premature commitment caused by uncertainty about later opportunities.

Failure modes include standardized-screening pressure, strategic ranking/waiting, travel/learning cost, algorithmic authority, discrimination/legal constraints, household complementarities, and peer effects that violate simple matching assumptions.

Demote if a true intentional-community/ecovillage federation already operates substantially this two-sided coordinated preference/commitment structure.

### C014 — Federation-level hidden-harm under-ascertainment estimation

**Status:** SURVIVING / provisional **research-control** transfer from Multiple Systems Estimation (capture–recapture); source method is established.

A commune's formal complaint count can badly understate a harmful outcome. If several partially overlapping reporting/outcome channels exist, their overlap pattern can contain information about surveillance completeness.

The viable scale is **federation/research-center**, not one small commune. Possible channels for one narrowly defined outcome category include internal complaint records, independent/federation reports, confidential exit interviews, lawful safeguarding/care records, anonymous follow-up, and relevant external records.

Purpose:

> estimate how incomplete the surveillance system may be and which channels miss which cases — never infer a specific unseen individual or use a model estimate as evidence for sanction.

Required cautions from the source literature:

- source dependence/referrals can seriously bias estimates;
- capture probability varies across cases;
- periods and case definitions must align;
- linkage can be uncertain;
- small cells can produce unstable estimates;
- plausible models can yield very different totals;
- confidentiality/deductive disclosure can be severe.

Safer architecture: pool enough communities/years; preserve genuinely distinct capture mechanisms; model source dependence/heterogeneity; report sensitivity and wide uncertainty; use results only for surveillance design/hypothesis generation; externally validate where possible.

A useful diagnostic does not require trusting one hidden-population point estimate: if distinct channels identify largely non-overlapping cases, a low formal-complaint count is weak evidence of low prevalence and may instead indicate under-ascertainment or incompatible channel definitions.

Demote if close communal/federation safety research already uses multi-list under-ascertainment estimation, or realistic data are too sparse/dependent for useful bounds.

## Demoted / useful but not novel

### D001 — Flagship founder trap
Demoted after spinout/social-movement literature attack; keep as practical movement design.

### D002 — Multi-parent daughter recombination
Too close to cross-pollination/cultural recombination.

### D003 — Developmental-sequence replication
Too close to tacit knowledge/path dependence/lifecycle.

### D004 — Governance commutativity
Near-decomposability/interdependence/modularity owns the structural principle.

### D005 — Reproductive timing
Classic demography measurement rule.

### D006 — Propagule burden / independent seedability
Propagule-size/fidelity literature already contains the mechanism.

### D007 — Effective number of reproducing communities
Tool derived from reproductive skew; not independent novelty.

### D008 — Low-base-rate evidence-lifecycle safeguard
Safeguarding/personnel-vetting precedent owns the architecture.

### D009 — Arithmetic-growth mirage under shared environments
Mathematically valid but materially negligible for the current Hutterite exemplar.

### D010 — Failure-history inheritance
Organizational-learning literature explicitly studies negative knowledge / knowing what not to do.

### D011 — Spatial-vs-temporal replication attention tradeoff
Direct organizational-replication precedent exists.

### D012 — Evidence-lineage counting
Useful but established source-independence/provenance/pseudoreplication logic.

### D013 — Governance feedback-lag / reform oscillation
Useful but close to policy feedback/control-system delay/change-fatigue traditions.

### D014 — Governance fault injection / dependency drills
Generic continuity practice already exercises loss of key people/functions. Keep as practical communal lesson.

### D015 — Seeded-fault review testing
Seeded-error audits, mutation testing, red teaming and integrity testing already own the mechanism.

### D016 — Randomized-response sensitive surveys
Established survey methodology; possible federation practice, not tail novelty.

### D017 — Random reviewer assignment
Established jury/audit/anti-corruption mechanism.

### D018 — Threshold/dual-control critical access
Established security and continuity practice.

### D019 — Blind content-before-source review
Established blind-review/structured-analysis practice.

### D020 — Cross-community control comparisons
Established comparative/causal inference practice.

### D021 — Experienced-member secondments
Established rotation/secondment/boundary-spanner practice.

## Hard rejection frontier

Do not repromote technical restatements of commodification/alienation; thick-vs-thin ties/social capital; planned fission/propagule reproduction; cultural fidelity thresholds; source/sink dynamics; modularity/interdependence; founder/lifecycle effects; generic schism/forkability; property/exit/liquidity; organizational forgetting; self-selection/endogeneity; survivorship/external validity; generic monitoring; newcomer overload; common-cause diversification; checks-and-balances/least privilege; laboratories of democracy; generic matching without non-separable cohort effects; continuity/succession exercises; generic governance pilots; ordinary paired discrimination testing; generic statistical monitoring/change-point detection; random juries/reviewer assignment; threshold access; blind review; comparative controls; and staff rotation.

## Method findings

- **M001:** formalization is not novelty.
- **M002:** user familiarity veto dominates model confidence.
- **M003:** nearest-neighbor literature attack is mandatory before promotion.
- **M004:** nonstandard structural cross-domain transfer can count; same-domain rediscovery cannot.
- **M005:** empty batches are successful; prefer no result to weak promotion.
- **M006:** terminology differences do not save a candidate when the target domain already implements the same structure.
- **M007:** a mathematically surprising transfer that does not materially affect the best available target case should be demoted until a consequential case is found.
- **M008:** practical usefulness and originality require separate dispositions; novelty demotion must not erase useful community-development knowledge.

## Provenance

Latest detailed runs:

- `runs/2026-08-15-orthogonal-tail-batch-16.md`
- `runs/2026-08-15-orthogonal-tail-batch-17.md`
- `runs/2026-08-15-orthogonal-tail-batch-18.md`
- `runs/2026-08-15-orthogonal-tail-batch-19.md`

Earlier batches and the recovered pre-deletion snapshot remain under `runs/`.
