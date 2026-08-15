# Creative Tail Sampling — Canonical Findings Index

Updated: 2026-08-15

This is intentionally a **compact current index**. Full candidate audits, literature collisions, demotions, empirical reconstructions, and method history are preserved under `runs/`; reproducible calculations are under `analysis/` and `data/`.

A user familiarity veto or strong nearest-neighbor literature collision overrides promotion. Practical usefulness is tracked separately in the communities repo even when originality fails.

## Current survivors

### C001 — Active normative edge-case search
**Status:** SURVIVING / provisional cross-domain transfer

Use active-learning logic to choose concrete governance/value cases most likely to distinguish members' plausible interpretations. Collect independent answers before deliberation and preserve resolved high-information cases as a versioned constitutional regression suite.

### C003 — Asset-gated cultural mutation
**Status:** NARROW SURVIVOR / provisional

Collective branch inheritance can pre-filter which institutional variants receive enough land, tools, treasury, reputation, or other capital to become viable competitors. Apparent superiority of a canonical form can therefore partly reflect pre-selection capitalization rather than downstream institutional selection.

### C005 — Reproductive-variance / superstar-reproduction trap
**Status:** SURVIVING / empirically strengthened

Do not infer reproducibility from total spread or mean daughter output alone. Measure the full parent-offspring distribution: `P(K=0)`, median, variance/mean, top-decile daughter share, generation interval, granddaughter reproduction, and subsidy/propagule structure.

Mature-parent Hutterite results currently preserved:

- Manitoba Schmiedeleut: `P(K=0)=4.08%`, median `K=2`, top-10% daughter share ~22.3%.
- Lehrerleut 1918–1953: `P(K=0)=3.45%`, median `K=1`, top-10% share 24.53%.
- Dariusleut 1918–1953: `P(K=0)=0%`, median `K=2`, top-10% share 20.0%.

Operational shorthand: **make reproduction boring** — daughter formation should be an ordinary lifecycle event for the median competent community rather than a rare founder feat.

Data/scripts:
- `data/hutterite_manitoba_mature_lineage_reconstruction.csv`
- `analysis/hutterite_reproduction_metrics.py`
- `data/hutterite_manitoba_period_growth_1918_1975.csv`
- `analysis/hutterite_period_growth_log_check.py`
- `data/hutterite_feefhs_1973_mature_cohorts.csv`
- `analysis/hutterite_feefhs_reproduction_metrics.py`

### C006 — Descendant inflation / lineage-size sampling bias
**Status:** SURVIVING / research-control

Prolific lineages mechanically contribute more extant observations even under perfect enumeration. State whether the estimand is a random founding attempt/root, lineage, extant community, current resident, or future movement contribution.

### C009 — Cohort-composition admission
**Status:** SURVIVING / provisional; market-thickness bounded

Applicant value can be non-separable: individually strong applicants can compose badly, while individually mediocre candidates can form a strong cohort together. Use cohort/set analysis only when several plausible applicants and openings genuinely overlap—especially founding, daughter formation, new sites and expansion waves. Do not manufacture batches in sparse mature-community markets.

### C011 — Shadow governance
**Status:** SURVIVING / provisional cross-domain transfer

Before transferring real authority to a substantially new governance process, run it nonbinding in parallel on the same admissible cases while the incumbent remains authoritative. Analyze divergence before live pilot/adoption.

### C012 — Standing constitutional-relation testing
**Status:** SURVIVING / provisional, narrowed

Maintain versioned tests for relations a community claims should hold even without one uniquely correct answer: irrelevance/invariance, symmetry, monotonicity, jurisdiction invariance, etc. Identity-swapped paired testing itself is old; the surviving transfer is the standing multi-relation constitutional suite.

### C013 — Federated reciprocal applicant clearing after exploration
**Status:** SURVIVING / provisional, narrow target transfer

After seekers and autonomous communities discover reciprocal preferences through visits/trials, coordinate commitments movement-wide so compatible seeker–vacancy pairs are not lost to isolated timing/search decisions, while preserving opt-out and local admission authority.

### C015 — Governance rights-liveness verification
**Status:** SURVIVING / provisional cross-domain transfer from formal methods

A right can exist syntactically yet be dead in a reachable governance state. Verify that important communal rights/remedies retain a permitted path to review/remedy/closure under realistic combinations of recusal, vacancy, quorum, jurisdiction, deadlines, delegation, escalation, strategic noncooperation and practical capacity limits.

Distinguish safety, liveness and bounded liveness. State every cooperation/fairness assumption explicitly.

### C016 — Verifiably unpredictable federation audit sampling
**Status:** SURVIVING / provisional cross-domain transfer

When random federation oversight is independently justified:

1. publish audit scope/rights;
2. freeze/commit the complete eligible universe before future randomness is knowable;
3. precommit deterministic sampling rules;
4. obtain future randomness not controlled by leadership/auditee;
5. derive the sample deterministically;
6. make selection replayable/verifiable afterward.

A random draw from a manipulable eligible universe is still manipulable.

### C017 — Intervention-aware evaluation of rescue-triggering community forecasts
**Status:** SURVIVING / provisional cross-domain transfer

> **Do not use the intervention-produced outcome as an unadjusted label for the forecast that triggered the intervention.**

If a community forecasts high failure risk without new aid, that warning triggers effective rescue, and failure is prevented, naive scoring can punish a truthful early warning. Define the intervention regime, freeze the forecast/evidence before rescue, evaluate forecast quality separately from intervention efficacy, and record rescue/subsidy exposure in survival/reproduction comparisons.

Full audit: `runs/2026-08-15-orthogonal-tail-batch-23.md`.

### C018 — Replicated-governance tombstones
**Status:** SURVIVING / provisional cross-domain transfer

When a high-consequence governance pattern is retired for a known failure, propagate a durable **semantic deprecation record** through the same daughter/template/fork replication channels that could otherwise reintroduce it.

The tombstone records the failed pattern's semantic scope, why it failed, evidence/counterexamples, replacement, context limits, and conditions/process for reconsideration. It is forced institutional memory, not an eternal prohibition.

Full audit: `runs/2026-08-15-orthogonal-tail-batch-25.md`.

### C019 — Power-targeted federation voting design
**Status:** SURVIVING / provisional cross-domain transfer from voting-power theory

Federations should design/audit the **power distribution they intend**, not treat nominal voting weights as equivalent to influence.

Operational loop:

1. define the representation objective—equal communities, equal indirect individual influence, or an explicit hybrid;
2. model how each community forms its position and how delegates act;
3. specify top-tier weights, quota, quorum, proxies and decision-specific rules;
4. compute actual pivotal power (e.g. Penrose-Banzhaf, Shapley-Shubik, or empirically modeled pivotality);
5. stress correlated preferences, bloc voting, delegate discretion, absence and historical coalitions;
6. solve weights **and quota together** toward the desired power distribution rather than assigning intuitive weights and assuming they produce it;
7. re-audit when communities/populations/rules change.

**Do not convert C019 into `use square-root weights`.** Penrose's classic square-root result is assumption-dependent; weights are not power; and small federations can be dominated by coalition geometry and quota effects.

A conditional three-community illustration in Batch 30 shows how nominal population shares around 58/37/5 can map to Banzhaf power 60/20/20 under a hypothetical linear-weight 60% rule. Switching those weights to square roots while retaining the same quota leaves the same coalition structure and the same 60/20/20 top-tier power. The point is the power audit, not the example rule.

Reusable tool:
- `analysis/weighted_voting_power.py` — exact Banzhaf + Shapley-Shubik indices for small weighted voting games.

Full audit: `runs/2026-08-15-orthogonal-tail-batch-30.md`.

### C020 — Fission/merge representation-effect audit
**Status:** SURVIVING / provisional cross-domain transfer linking voting-power theory to communal reproduction

Weighted-voting theory already shows that splitting/merging players can change Banzhaf/Shapley power, and dynamic-federation research already treats child-community representation as a fairness problem. The surviving target connection is narrower:

> **When daughter-community formation or merger is a legitimate lifecycle event, explicitly measure and choose the political representation effect of that structural change instead of letting the voting rule create an accidental subsidy or penalty to reproduction.**

A useful constitutional diagnostic is an **aligned-preference split/merge counterfactual**: if daughters contain the same total people and vote identically to the unsplit parent, how much does aggregate federation influence change solely because one organizational boundary became two? A non-zero result is not automatically unfair—separate autonomous communities may deserve a sovereignty premium—but it should be explicit.

C020 inherits C019's core warning: nominal-weight preservation is not power preservation. Under a conditional Batch 31 toy rule, splitting a 100-person parent into 50+50 under population-linear weights preserved total nominal weight but reduced the lineage's normalized Banzhaf power from 0.60 to 0.50; under one-community/one-vote, a three-player parent with 1/3 power could become two of four equal voters with aligned aggregate power 1/2. These are illustrations, not recommended rules.

Planned-fission review should therefore include:
- before/after voting-power audit;
- effects on all third-party communities;
- distinction between genuine autonomy and administrative fragmentation;
- explicit decision on any community-unit/autonomy premium;
- merger effects as the reverse case.

Full audit: `runs/2026-08-15-orthogonal-tail-batch-31.md`.

## Recent empty novelty batches that produced practical lessons

- **Batch 26:** decision dependencies / truth maintenance — correction should propagate to dependent decisions; known in truth-maintenance, case-management and record-correction systems.
- **Batch 27:** request amplification, reporting counts, queueing — humanitarian bullwhip and safety-reporting literature already owns the mechanisms.
- **Batch 28:** communal labor ratchet — classic dynamic incentive theory plus direct Twin Oaks/Dandelion anti-ratchet precedents.
- **Batch 29:** hysteretic thresholds / anti-windup — control theory plus adjacent governance and administrative-law precedents.

All practical translations are mirrored in `u-dont-existDOTcom/communities` even though they are not Creative Tail discoveries.

## Hard rejection frontier

Do not repromote technical restatements of:

- commodification/alienation/division-of-labor effects;
- thick vs thin ties, social capital, generic multiplexity;
- generic fission/propagule reproduction and cultural fidelity;
- source/sink, modularity/interdependence, founder/lifecycle/path-dependence;
- ordinary property/exit/liquidity, organizational forgetting, survivorship/endogeneity;
- generic audits/monitoring/diversification/checks-and-balances;
- ordinary matching, pilots, continuity drills, blind review, privacy linkage;
- access-control revocation, process conformance, compensating transactions;
- anti-structuring, procedural DoS, common-control analysis;
- ordinary insurance/moral hazard/soft-budget logic;
- generic rescue forecasting/anticipatory action;
- ordinary polycentric coordination, version histories, change management;
- generic supply-chain bullwhip/queueing/reporting-culture effects;
- classic ratchet effects;
- generic hysteresis/chatter/anti-windup;
- voting-power mathematics, player splitting/merging, or Penrose formulas themselves (C019/C020 are only target-domain operational transfers).

## Method findings

- **M001:** formalization is not novelty.
- **M002:** user familiarity veto dominates model confidence.
- **M003:** nearest-neighbor literature attack is mandatory before promotion.
- **M004:** nonstandard structural cross-domain transfer can count; same-domain rediscovery cannot.
- **M005:** empty batches are successful; prefer no result to weak promotion.
- **M006:** terminology differences do not rescue an already-existing target structure.
- **M007:** mathematically surprising but materially irrelevant transfers should be demoted until a consequential target case appears.
- **M008:** originality and practical usefulness require separate dispositions.
- **M009:** known source mechanisms survive only when the target transfer changes an actual design/test/measurement decision.
- **M010:** when a broad analogy collides, narrow the transferred object until a distinct operational failure/test remains or the branch dies.
- **M011:** public accountability and adversarial unpredictability can coexist when the rules are public, the future random realization is unknowable, and the realized selection is replayable.
- **M012:** intervention-triggering predictions require intervention-aware evaluation.
- **M013:** negative institutional knowledge must propagate through replication channels, not merely survive in archives.
- **M014:** in weighted federations, the object to design is power under the complete rule, not the visible weight vector.
- **M015:** when reproduction changes the number/boundaries of federation players, representation can become an implicit subsidy or penalty to reproduction even without any explicit reward rule.

## Provenance

Latest runs:

- `runs/2026-08-15-orthogonal-tail-batch-26.md`
- `runs/2026-08-15-orthogonal-tail-batch-27.md`
- `runs/2026-08-15-orthogonal-tail-batch-28.md`
- `runs/2026-08-15-orthogonal-tail-batch-29.md`
- `runs/2026-08-15-orthogonal-tail-batch-30.md`
- `runs/2026-08-15-orthogonal-tail-batch-31.md`

Earlier batches and the recovered pre-deletion snapshot remain under `runs/`.
