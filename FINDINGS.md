# Creative Tail Sampling — Canonical Findings Index

Updated: 2026-08-15

This file distinguishes **actual survivors** from useful-but-familiar material. A user familiarity veto or strong historical/literature compression overrides earlier promotion.

## Current result

### No accepted grand social-theory finding yet

The multiplex/relational-unbundling branch failed the novelty gate. It remains historical/applied material only.

## Current surviving cross-domain connections

### C001 — Active normative edge-case search

**Status:** SURVIVING CROSS-DOMAIN CONNECTION; not claimed as academically unprecedented.

Transfer active learning / preference elicitation + software regression testing into intentional-community values/governance.

Instead of maximizing agreement on abstract values, adaptively select concrete cases where members' plausible interpretations are most likely to diverge. Collect baseline responses independently, separate measurement from deliberation, and preserve resolved high-information cases as a versioned **constitutional regression suite**. Re-run after membership/rule changes to expose semantic drift.

Important caveat: moral preferences may be unstable, sequence-sensitive, noisy, or poorly represented by the elicitation model, so replicate/randomize some cases and do not assume one fixed latent utility function.

Demote if a target-domain precedent is found using substantially the same adaptive case-selection + regression-suite architecture.

### C003 — Asset-gated cultural mutation — NARROW SURVIVOR

**Status:** SURVIVING CROSS-DOMAIN CONNECTION, narrowed after Batch 07.

Broad claims that property affects exit or innovation are **not novel**. Religious-exit research already treats property loss/renunciation as an exit cost; church-property law extensively addresses assets after schism; property-rights research shows ownership allocation can affect innovation.

The remaining candidate is specifically about **collective branch inheritance as a pre-selection filter**:

> An incumbent reproduction architecture can alter which institutional variants are ever exposed to selection by determining which organizational branches inherit enough accumulated capital to become viable competitors.

This creates possible **selection blindness**. A canonical community form can appear superior to alternatives when alternatives were systematically prevented from starting with comparable land, tools, treasury, reputation, or other inherited resources.

The relevant distinctions are:

- individual exit rights;
- collective fork/branch inheritance rights;
- parent-approved daughter inheritance;
- process-triggered seed rights independent of doctrinal approval.

High demographic daughter production can therefore coexist with low institutional experimentation.

Demote if existing scholarship is found explicitly modeling collective branch asset portability as a filter on institutional variation/evolution rather than merely documenting exit costs or property disputes.

Audit: `runs/2026-08-15-orthogonal-tail-batch-06.md` and `runs/2026-08-15-adversarial-tail-batch-07.md`.

### C005 — Reproductive-variance trap / superstar reproduction trap

**Status:** SURVIVED CROSS-DOMAIN CONNECTION; current strongest reproduction-specific result; **empirically strengthened in Batch 09**.

**Source:** branching-process theory.

A movement's mean number of viable daughter communities per parent can be high while the underlying community design remains **poorly reproducible**.

The missing object is the full offspring distribution `P(K=k)`, where `K` is the number of viable daughters produced by a sufficiently mature community.

#### Sharp example

Two hypothetical designs both have mean daughter count = 2.

- **A:** every parent produces exactly 2 viable daughters.
- **B:** 90% produce 0; 10% produce 20.

Same arithmetic mean. Under a simple Galton-Watson model, B has eventual extinction probability given by the smallest solution to `q = 0.9 + 0.1q^20`, approximately **91.8%** from one founding community.

Therefore distinguish:

1. **historical spread** — many communities exist;
2. **mean reproduction** — average daughter count;
3. **typical reproducibility** — an ordinary daughter has a high chance of becoming reproductive itself;
4. **lineage robustness** — low extinction risk without dependence on rare jackpot parents.

A movement can score high on 1 and 2 while scoring badly on 3 and 4.

#### Empirical anchor — older Manitoba Hutterite lineage

A manual reconstruction from the Manitoba Historical Society colony genealogy was saved at:

- `data/hutterite_manitoba_mature_lineage_reconstruction.csv`

Reproducible metrics:

- `analysis/hutterite_reproduction_metrics.py`

Important scope limitation: the historical table explicitly lists **Manitoba Daughter(s)**, so offspring outside Manitoba are omitted. The values below are therefore Manitoba-lineage counts, not complete North-American lifetime offspring counts.

For the **49 Manitoba colonies founded by 1970**:

- total recorded Manitoba daughters = **103**;
- mean `K = 2.102`;
- median `K = 2`;
- population variance `Var(K) = 1.724`;
- variance / mean = **0.820**;
- recorded-Manitoba `P(K=0) = 2/49 = 4.08%`;
- top 10% of parent colonies account for only about **22.3%** of recorded daughters.

One of the two zero-daughter colonies, Roseisle, closed in 1936 only seven years after founding. Because out-of-province daughters are omitted, the true total-daughter zero rate could be lower than 4.08%.

This older cohort is strikingly **non-jackpot-like**: reproduction is broadly distributed across mature colonies, the median is close to the mean, and the distribution is mildly underdispersed rather than dominated by a small number of hyper-reproductive parents.

A historical consistency check supports the underlying list's completeness through 1975: the reconstruction contains 62 colonies ever founded by then, while a 1977 Manitoba monograph reports 60 operating colonies; the genealogy explicitly contains two pre-1975 closures, giving exactly 60 surviving operations.

#### Non-stationarity warning

Later Manitoba cohorts show many more recorded zero-Manitoba-daughter colonies, but this cannot be interpreted as simple reproductive collapse because:

- later colonies are more right-censored;
- the source omits daughters outside Manitoba;
- Hutterite colonies increasingly added industrial operations to create jobs and delay branching;
- the 1990s Schmiedeleut schism temporarily accelerated branching;
- land prices/location constraints changed.

Therefore Batch 09 treats the pre-1970 cohort as the cleaner descriptive test of whether the mature historical reproduction process was superstar-driven.

#### Current inference

C005 is **empirically strengthened, not proven**.

The Hutterite case supplies a real example in which a famously persistent, multi-generational communal lineage appears to reproduce broadly across parent units rather than through rare reproductive jackpots.

The next high-value test is a genuinely parent-resolved movement with strong overdispersion, so we can ask whether equal/similar mean reproduction but different offspring variance predicts different lineage depth and extinction risk.

#### Measurement implication

For mature communities, collect at minimum:

- `K` = viable daughters founded;
- `P(K=0)` = zero-daughter fraction;
- median K;
- variance/dispersion of K;
- fraction of all daughters produced by top 10% of parents;
- daughter survival criterion;
- daughter-to-granddaughter reproduction;
- reproductive timing;
- propagule burden and federation/parent subsidy.

Mean K alone is inadequate.

Demote if target-domain scholarship is found already using offspring-distribution/branching extinction metrics to make substantially this distinction between movement growth and community-level reproducibility.

Audits: `runs/2026-08-15-adversarial-tail-batch-07.md`, `runs/2026-08-15-empirical-reproduction-batch-08.md`, and `runs/2026-08-15-hutterite-lineage-batch-09.md`.

### C006 — Descendant inflation / lineage-size sampling bias

**Status:** SURVIVED CROSS-DOMAIN CONNECTION; current strongest research-method result.

**Source:** ancestral reproductive bias in branching processes + phylogenetic/clade sampling bias.

If some community lineages produce many daughters and others produce few, a contemporary survey that samples **communities** uniformly is mechanically weighted toward the cultures of prolific lineages. Each daughter creates another observation descended from the same historical experiment.

This is not ordinary survivorship bias. Even if every extant community were perfectly enumerated, a lineage with 20 daughters contributes up to 21 related observations while a non-reproducing lineage contributes one.

#### Consequence

A trait can become common in a current-community dataset because it increases **reproduction**, even if it does not improve—and could even worsen—a separate outcome such as:

- child happiness;
- member welfare;
- freedom;
- conflict quality;
- local stability;
- environmental performance.

If descendants inherit the trait, reproductive success itself determines how heavily that trait is represented in the sample.

Treating daughters as independent replications can then create a second problem: genealogical pseudoreplication inflates apparent evidence around inherited traits.

#### Estimand rule

There is no universal correction because different research questions require different probability measures.

- **Random founding attempt:** weight independent founding attempts/roots appropriately rather than letting descendants multiply the root's weight automatically.
- **Random current community:** uniform extant-community weighting is legitimate, but the estimand is intentionally reproduction-weighted.
- **Random current resident:** weight by community population.
- **Future movement culture:** reproductive-value weighting may be exactly appropriate.

Therefore community research should state which estimand it is answering before deciding what a 'representative' sample means.

#### Target-domain screen

Commune/intentional-community methodology already recognizes major sampling problems, including undercounting short-lived or nameless communes, overrepresentation of institutionalized groups, availability/convenience bias, directory bias, and living-community survivor bias.

The targeted search did **not** locate an intentional-community method explicitly correcting for **daughter-community proliferation as a genealogical size-bias mechanism** or defining separate estimands for founding attempts versus extant descendant communities.

#### Operational implication

Where feasible, community datasets should add:

- parent/founding lineage;
- daughter relationships;
- independent founding versus organizational offspring;
- common federation/parent support;
- lineage depth.

Then use genealogy-aware/hierarchical models, clustered uncertainty, and explicit sensitivity to lineage weighting where relevant. Do not blindly inverse-weight lineages; that merely changes the estimand.

Demote C006 if target-domain work is found already making substantially this genealogical reproductive-size-bias distinction.

Audit: `runs/2026-08-15-orthogonal-tail-batch-10.md`.

## Derived measurement rules — useful but below novelty threshold

### D004 — Governance commutativity

**Status:** DEMOTED from C004 after Batch 07.

The order-independence test from distributed systems remains a useful way to diagnose whether two governance actions truly conflict, but near-decomposability, modularity, task interdependence, and interface governance already contain the structural principle. Do not repromote as a discovery.

### D005 — Reproductive timing / generation interval

Population growth depends on amount **and timing** of reproduction. This is classic demography, not a tail discovery, but it changes what a spreading-community project should measure:

- time to first viable daughter;
- daughter-founding age distribution;
- time to granddaughter reproduction.

Lifetime daughter count alone is insufficient.

### D006 — Propagule burden / independent seedability

**Status:** USEFUL MEASUREMENT DISTINCTION; not novel.

Reliable fission reproduction does not imply that a community architecture can be recreated de novo by a small founder team.

Measure how much mature structure each daughter inherits:

- number/fraction of experienced members transferred;
- land/capital/tools;
- continuing parent/federation support;
- whether daughters later reproduce without equivalent extraordinary subsidy.

The underlying point is covered by propagule-size and cultural-transmission literatures, so do not repromote it as a discovery.

### D007 — Effective number of reproducing communities

**Status:** DERIVED QUANTITATIVE TOOL; not an independent discovery.

When daughter production is highly skewed, census community count can greatly exceed the effective number of lineages contributing to future movement culture. Population-genetic effective-size concepts may be useful once multi-movement genealogies exist, but this follows directly from reproductive skew/C005.

## Other demoted applied hypotheses

### D001 — Flagship founder trap / founder-export externality

Demoted after spinout/social-movement literature attack.

### D002 — Multi-parent daughter recombination

Too close to cross-pollination/cultural recombination/diverse founder experience.

### D003 — Developmental-sequence replication

Too close to tacit knowledge, organizational lifecycle, sequencing, and path dependence.

## Known / derivative community material — DO NOT REPROMOTE AS NOVEL

- specialization/commodification/alienation of social relations;
- thick-vs-thin ties, embeddedness, social capital, multiplex exchange;
- planned fission/propagule reproduction;
- packet reproduction through experienced member splits;
- propagule size/fidelity tradeoffs;
- cultural-transmission complexity/fidelity thresholds;
- germline/reproductive specialization;
- source/sink institutional dynamics;
- network modularity/near-decomposability/interdependence;
- cultural compression through repeated transmission;
- recruitment-composition effects;
- generic schism/forkability;
- ordinary individual religious exit costs;
- generic property disputes after schism;
- generic property-rights → innovation claims;
- organizational lifecycle/path dependence;
- policy experimentation/laboratories-of-democracy;
- checks and balances/threshold approval;
- institutionalized dissent/red teams;
- Tiebout-style mobility/exit;
- stress tests/redundancy without a stronger consequence;
- mean reproduction number by itself;
- shorter generation time spreads faster, by itself;
- rare-task organizational forgetting;
- founder-stage versus mature-stage governance by itself;
- self-selection/endogeneity of community membership;
- ordinary current-directory/survivor sampling bias.

## Earlier provisional branches

### E001 — Epistemic firebreaks

Too close to wisdom-of-crowds / information-cascade theory.

### E002 — Whole-package ratification

Too close to known social-choice problems.

## Protocol lessons

### M001 — Formalization is not novelty

A familiar root idea does not become a tail discovery because downstream mechanisms receive technical names.

### M002 — User familiarity veto dominates model confidence

If the intended expert user immediately compresses the candidate to common sense or known theory, record the collision and move outward.

### M003 — Nearest-neighbor literature attack before promotion

Candidate survivors require explicit search for conceptual ancestors. This prevents obvious retrieval failures; it does not prove originality.

### M004 — Cross-domain transfer can count, same-domain rediscovery cannot

A known source-domain mechanism can survive if its target transfer is nonstandard and yields distinctive predictions/design rules.

### M005 — Empty batches are successful

Prefer 'nothing survived' over weak promotion.

## Provenance

- recovered pre-deletion state: `runs/2026-08-15-recovered-pre-deletion-findings.md`
- multiplex batches 01–03: historical exploration, later vetoed
- user veto: `runs/2026-08-15-user-veto-multiplex-branch.md`
- orthogonal batch 04: `runs/2026-08-15-orthogonal-tail-batch-04.md`
- reproduction batch 05: `runs/2026-08-15-reproduction-tail-batch-05.md`
- orthogonal batch 06: `runs/2026-08-15-orthogonal-tail-batch-06.md`
- adversarial batch 07: `runs/2026-08-15-adversarial-tail-batch-07.md`
- empirical batch 08: `runs/2026-08-15-empirical-reproduction-batch-08.md`
- Hutterite lineage batch 09: `runs/2026-08-15-hutterite-lineage-batch-09.md`
- orthogonal batch 10: `runs/2026-08-15-orthogonal-tail-batch-10.md`
