# Creative Tail Sampling — Canonical Findings Index

Updated: 2026-08-15

Compact canonical index. Detailed derivations, literature collisions, empirical reconstructions, and rejected candidates are under `runs/`; reproducible data/calculations are under `data/` and `analysis/`.

A user familiarity veto or strong literature compression overrides earlier promotion.

## Current status

No accepted grand social-theory finding yet. The earlier multiplex/relational-unbundling branch failed the novelty gate and is historical/applied material only.

Batch 20 produced no new survivor. Batch 21 produced one narrow provisional transfer, C015.

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

Keep narrow. Demote on a close target precedent.

### C005 — Reproductive-variance / superstar-reproduction trap

**Status:** SURVIVING; strongest reproduction-specific result; empirically strengthened across three Hutterite samples/branches.

Mean viable-daughter output can substantially overstate how reproducible a community design is. Distinguish historical spread, mean reproduction, typical reproducibility, and lineage robustness.

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

#### Cross-branch replication — FEEFHS 1973 tables

Standardized mature cohort: colonies founded **1918–1953 inclusive**, giving at least 20 years of possible daughter production before the 1973 cutoff.

**Lehrerleut** (`n=29`): daughters 53; mean `K=1.828`; median 1; population variance `1.453`; variance/mean `0.795`; `P(K=0)=3.45%`; top-10% share `24.53%`; max `K=5`.

**Dariusleut** (`n=33`): daughters 60; mean `K=1.818`; median 2; population variance `0.694`; variance/mean `0.382`; `P(K=0)=0%`; top-10% share `20.0%`; max `K=3`.

The same qualitative result appears across distinct Hutterite branches: mature-parent reproduction is broadly distributed, not jackpot-dominated.

Operational shorthand: **make reproduction boring**. A strongly replicable community system should make daughter formation an ordinary lifecycle event for the median competent community rather than an exceptional achievement by a few unusually capable founders.

A public row-level non-Hutterite genealogy sufficient for a comparable `K` distribution has not yet been found. Aggregate church-planting evidence remains qualitative context only.

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

### C011 — Shadow governance

**Status:** SURVIVING / provisional cross-domain operational transfer.

Before transferring authority to a substantially new governance process, run it nonbinding in parallel on the same admissible cases and compare what it would have decided with the incumbent process. Analyze divergence cases before live pilot/adoption.

### C012 — Standing constitutional-relation testing

**Status:** SURVIVING / provisional, narrowed.

Identity-swapped paired testing itself is old. The remaining proposed transfer is a **versioned constitutional relation suite** testing multiple relations a community already claims should hold—irrelevance/invariance, symmetry, monotonicity, jurisdiction invariance, and other predeclared relational properties—even where there is no agreed uniquely correct answer.

### C013 — Federated reciprocal applicant clearing after exploration

**Status:** SURVIVING / provisional cross-domain operational transfer; narrowed in Batch 20.

Matching-market design is known. Historical kibbutz practice also included movement-level centralized applicant screening, so neither centralized recruitment nor centralized screening is novel communal practice.

The remaining target-domain transfer is narrower:

> **After seekers and autonomous communities learn reciprocal preferences through visits/trials, coordinate commitments movement-wide so compatible seeker–vacancy pairs are not lost to isolated timing/search decisions.**

Current Kibbutz Movement infrastructure helps seekers discover accepting communities but retains community-specific admissions. No close intentional-community/ecovillage precedent has yet been found for coordinated reciprocal preference clearing across autonomous communities after exploration.

Recommended architecture remains dynamic and non-coercive: hard constraints first; several mutual exploration matches; visits/trials before final rankings; reciprocal acceptability; coordinated commitment suggestions; opt-out and local admission authority preserved; C009 cohort logic only where several openings/candidates genuinely coexist.

Demote if a close target implementation is found.

### C015 — Governance rights-liveness verification

**Status:** SURVIVING / provisional cross-domain operational transfer from formal methods.

Formal bylaw modeling, workflow model checking, safety/liveness verification, and legal-remedy doctrine are all established. The surviving target application is narrower:

> **For an important communal right or remedy, verify that from every realistic state in which it is validly invoked, the governance process still has a permitted path to the promised review/remedy/closure despite adverse combinations of recusal, vacancy, quorum, jurisdiction, deadlines, delegation and escalation.**

A right can therefore exist syntactically in a constitution while being **dead** in a reachable governance state.

Example: an independent five-person appeal panel exists; two members must recuse; one seat is vacant; the remaining two lack quorum; only the implicated local board may fill vacancies; conflict rules bar that board from acting. The appeal clause exists, but no valid transition reaches review.

Verification targets should distinguish:

- **safety:** prohibited acts/states never occur;
- **liveness:** a promised review/remedy remains reachable under explicit assumptions;
- **bounded liveness:** the remedy can complete within a defined procedural/time bound rather than merely “eventually.”

Candidate first-use procedures:

- complaint intake and bypass;
- expulsion/sanction appeal;
- child/safeguarding escalation;
- records access/correction;
- exit valuation/payment;
- emergency safety/medical bypass;
- leadership removal/succession;
- replacement of conflicted adjudicators;
- federation-level review of a captured local body.

Minimum protocol: model only relevant states/roles/transitions; predeclare safety/liveness properties; include realistic fault/adversarial states; run state-space/model checking or bounded exhaustive search; inspect counterexample traces; repair the actual procedure; rerun after material amendments; preserve counterexamples as regression tests.

Important limits: verification proves only the model; omitted states and unrealistic fairness assumptions can create false confidence; discretion is hard to formalize; a procedure can be perfectly live and still unjust. C015 supplements rather than replaces substantive rights, human judgment, and outcome evaluation.

Demote if a close target-domain implementation already routinely verifies human rights/remedies as liveness properties under adverse governance states, or if ordinary tabletop review catches the same material failures more cheaply.

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

### D022 — Hidden-harm capture–recapture / Multiple Systems Estimation
Former C014, demoted in Batch 20. Family-violence and child-abuse research already directly applies capture–recapture across multiple organizations. Keep only as a federation/research-center option with strong assumptions/privacy caveats.

### D023 — Lineage-aware comparative correction
Cultural phylogenetic methods already address non-independence from shared ancestry (`Galton's problem`). Highly relevant to daughter-community genealogies, but not a tail discovery.

### D024 — Sister-daughter matched comparisons
Established sibling/matched-comparison logic. Useful only with explicit attention to nonrandom self-sorting at fission.

### D025 — Cultural hitchhiking in successful packages
Directly modeled in cultural-evolution research: neutral or detrimental traits can hitchhike when transmitted with functional traits. Important practical warning, not novel.

### D026 — Constitutional holdout testing / legal overfitting
A 2026 legal scholarship precedent explicitly proposes holdout/test cases and regularization to reduce overfitting in precedential reasoning. Useful community-governance transfer, not novel.

### D027 — Neutral institutional variation for evolvability
Organization Science already models organizational evolvability on neutral landscapes. Useful caution against unnecessary standardization, not novel.

### D028 — Privacy-preserving federation overlap analytics
PSI/PPRL/secure multiparty computation is established cross-organizational infrastructure. No demonstrated community bottleneck yet justifies promotion; retain only as a future technical option.

### D029 — Expiring authority / revocation latency
Time-limited privilege, just-in-time access and access reviews are established security practice. Useful community lesson, not novelty.

### D030 — Cascading authority revocation
Delegation/revocation research explicitly models downstream revocation chains and propagation. Useful community lesson, not novelty.

### D031 — Governance conformance checking
Process-mining research already compares event logs with normative/reference process models for compliance. Useful if communal record burden is reasonable, not novelty.

### D032 — Compensating transitions for non-atomic communal changes
Distributed Saga/compensating-transaction design owns the mechanism; legal escrow/conditions provide adjacent human forms. Useful for complex transitions, not novelty.

### D033 — Procedural fail-open/fail-closed defaults
Established safety/security/default-rule logic. Useful companion to C015, not novelty.

## Hard rejection frontier

Do not repromote technical restatements of commodification/alienation; thick-vs-thin ties/social capital; planned fission/propagule reproduction; cultural fidelity thresholds; cultural phylogenetic non-independence; cultural linkage/hitchhiking; source/sink dynamics; modularity/interdependence; founder/lifecycle effects; generic schism/forkability; property/exit/liquidity; organizational forgetting; self-selection/endogeneity; survivorship/external validity; generic monitoring; newcomer overload; common-cause diversification; checks-and-balances/least privilege; laboratories of democracy; generic matching; continuity/succession exercises; generic governance pilots; ordinary paired discrimination testing; legal holdout/cross-validation; generic organizational evolvability/neutral drift; generic privacy-preserving record linkage; random juries/reviewer assignment; threshold access; blind review; comparative controls; staff rotation; generic access-control leases/revocation; process conformance; and compensating transactions.

## Method findings

- **M001:** formalization is not novelty.
- **M002:** user familiarity veto dominates model confidence.
- **M003:** nearest-neighbor literature attack is mandatory before promotion.
- **M004:** nonstandard structural cross-domain transfer can count; same-domain rediscovery cannot.
- **M005:** empty batches are successful; prefer no result to weak promotion.
- **M006:** terminology differences do not save a candidate when the target domain already implements the same structure.
- **M007:** a mathematically surprising transfer that does not materially affect the best available target case should be demoted until a consequential case is found.
- **M008:** practical usefulness and originality require separate dispositions; novelty demotion must not erase useful community-development knowledge.
- **M009:** when a candidate's source mechanism is known, target novelty must lie in a genuinely different operational structure—not merely in applying the same method to another kind of organization.
- **M010:** if a broad analogy collides, narrow the object being transferred until it either yields a distinct operational failure/test or dies; C015 survived only after “model-check bylaws” was rejected and the target became right-exercisability under adverse states.

## Provenance

Latest detailed runs:

- `runs/2026-08-15-orthogonal-tail-batch-18.md`
- `runs/2026-08-15-orthogonal-tail-batch-19.md`
- `runs/2026-08-15-orthogonal-tail-batch-20.md`
- `runs/2026-08-15-orthogonal-tail-batch-21.md`

Earlier batches and the recovered pre-deletion snapshot remain under `runs/`.
