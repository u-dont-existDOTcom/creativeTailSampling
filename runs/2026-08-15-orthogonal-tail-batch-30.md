# Orthogonal Tail Batch 30 — Federation Voting Weight vs Actual Voting Power

Date: 2026-08-15

## Outcome

One provisional cross-domain survivor:

- **C019 — Power-targeted federation voting design**

The source theory is established voting-power/game theory. The surviving transfer is not the Penrose square-root rule itself; it is the operational requirement that an intentional-community federation **define the representation objective, model both tiers, compute actual pivotal power under the real quota/rule, and solve weights/quota toward the intended power distribution rather than treating nominal population weights as equivalent to influence.**

No close intentional-community/cooperative-federation implementation using Penrose-Banzhaf/Shapley-style power auditing was found in the target search.

---

# A. C019 — Power-targeted federation voting design

## Target problem

Community federations can face a representation tradeoff:

- one-community/one-vote protects community sovereignty but gives a member of a tiny community more indirect representation per person than a member of a huge community;
- population-proportional weights look individually egalitarian but can create very different **pivotal power** from the nominal weight;
- supermajority thresholds and small numbers of communities can make some members effectively veto players, dummies, or coalition gatekeepers;
- the local community's internal decision process is a second tier that changes an individual member's final influence.

## Source-domain result

Voting-power theory distinguishes **voting weight** from **voting power**.

Penrose's classic two-tier model asks how to equalize the indirect influence of individuals whose local constituencies first choose a position and then act through a weighted upper-tier body. Under the classic independent, equiprobable binary-vote assumptions, an individual's chance of being pivotal within a constituency falls roughly with the square root of its population. This motivates an upper-tier power target proportional to the square root of population.

But several important qualifications are established:

1. the square-root rule is assumption-dependent;
2. correlated voter preferences can change the optimal weights substantially;
3. **weights are not the same as power**, so assigning square-root *weights* does not generally guarantee square-root *power*;
4. the decision quota can materially change the power distribution even when weights are unchanged;
5. small federations are especially poorly described by asymptotic rules.

Therefore C019 is explicitly **not** `use square-root weights`.

## Operational transfer

Before adopting or revising a weighted fallback rule, a community federation should:

### 1. Define the fairness objective

Examples:

- equal sovereignty of member communities;
- equal a-priori indirect influence of individual adult members;
- a hybrid floor for small communities plus population responsiveness;
- protection against one large community dominating;
- high action capacity while retaining meaningful blocking rights for minorities.

There is no mathematically neutral answer until the objective is named.

### 2. Specify the actual two-tier process

Record:

- how each community determines its position: consensus, direct vote, delegate discretion, mandate, multiple delegates, etc.;
- whether delegates from one community must vote together;
- how many delegates each community has;
- what population counts for representation;
- top-tier weights;
- decision quota(s);
- quorum;
- proxy/absence rules;
- whether some decisions use different thresholds.

### 3. Compute power, not just weight

For the top-tier weighted game, calculate at least one appropriate pivotal-power measure such as:

- Penrose-Banzhaf;
- Shapley-Shubik;
- empirical pivotality under a model fitted to actual voting/coalition behavior.

For a two-tier individual-equality objective, combine top-tier pivotality with the probability/influence of an individual in the local process.

### 4. Stress assumptions

Run several models rather than one ceremonial calculation:

- independent local votes;
- correlated local preferences;
- communities voting as cohesive blocs;
- delegate discretion;
- historical coalition patterns;
- abstention/absence;
- population changes;
- admission/removal of a community.

If the fairness conclusion flips across plausible models, publish that uncertainty instead of claiming mathematical equality.

### 5. Solve the inverse problem

If the federation has a desired power distribution, search over **weights and quota together** for rules that approximate it while satisfying political constraints. Do not set nominal weights equal to desired power shares and assume the job is done.

### 6. Re-audit after structural change

Recompute when:

- population distribution changes materially;
- a large/small community joins or leaves;
- the number of communities becomes very small;
- local decision rules change;
- the quota changes;
- actual voting correlations shift.

---

# B. FEC illustration — explicitly conditional, not a claim about the current rule

The current official FEC website says the old `thefec.org` site is out of date and that the federation is rebuilding. The current official site lists three full-member communities with approximate populations:

- Twin Oaks: about 100 adults and children;
- East Wind: about 60 adults and 4 children;
- Alpha Farm: 9 people.

Historical/outdated FEC materials describe a fallback vote based on population and a 3/5 threshold for some major decisions, but the current public policy page could not be inspected deeply enough in this pass to confirm the exact live weighting formula. **Do not describe the following as the current FEC voting system.**

### Conditional toy calculation

Assume for illustration only:

- community weights are linearly proportional to populations `[100, 64, 9]`;
- winning quota is 60% of total weight.

Then total weight is 173 and quota is 103.8.

Winning minimal pairs are:

- Twin Oaks + East Wind;
- Twin Oaks + Alpha Farm.

East Wind + Alpha Farm cannot win.

Raw Banzhaf swing counts are:

- Twin Oaks: 3;
- East Wind: 1;
- Alpha Farm: 1.

Normalized top-tier power:

- Twin Oaks: **60%**;
- East Wind: **20%**;
- Alpha Farm: **20%**.

Yet their nominal linear population weights are roughly:

- 57.8%;
- 37.0%;
- 5.2%.

Thus the 64-person and 9-person communities have the same top-tier pivotal power in this simple game despite radically different nominal weights.

Now replace linear weights with square roots `[10, 8, 3]` but keep the 60% quota. The same winning coalitions remain, so the normalized Banzhaf powers remain **60/20/20**.

At a 50% quota with those square-root weights, every pair can win and the top-tier Banzhaf powers become **1/3 each**.

This illustrates the central point:

> **Changing weights without analyzing the quota and coalition geometry may not change power at all.**

It also illustrates why `square-root weights` is not a magic fairness formula in a three-community federation.

## Individual indirect power warning

Penrose-style equal-individual calculations additionally require a model of the local tier. The current population numbers include children differently across public descriptions, and actual internal decisions are not independent coin flips. Therefore no individual-level equality claim is made from this toy calculation.

---

# C. Target-domain precedent search

Searches included combinations of:

- intentional community + Banzhaf/Penrose/voting power;
- cooperative federation + Banzhaf/voting power;
- cooperative apex/federation weighted voting;
- FEC + Penrose/square-root/Banzhaf.

The search found:

- cooperative statutes and federations that allow organization-level weighted voting;
- FEC materials discussing consensus, delegates, and population-related fallback voting;
- digital-democratic-federation work with explicit fairness conditions;

but no close intentional-community/cooperative movement implementation in which the federation:

1. computes actual voting-power indices under its real weights/quota;
2. models the local-to-federation two-tier influence;
3. solves the inverse weights/quota problem toward an explicit individual/community fairness target.

**Disposition: C019 survives provisionally as a target-domain cross-transfer.**

Demote if such a close implementation is found.

---

# D. Candidate audit

At least sixteen candidates were screened.

## T130-01 — Population weight equals population power

Claim: use linear population weights for individual equality.

Verdict: **REJECT / FALSE IN GENERAL.** Weight and pivotal power differ.

## T130-02 — Use square-root weights

Verdict: **REJECT AS GENERAL RULE.** Penrose concerns power under assumptions; square-root weights alone can fail, especially in small games or different quotas.

## T130-03 — Compute top-tier Banzhaf power

Verdict: **KNOWN TOOL; MERGE INTO C019 target transfer.**

## T130-04 — Compute Shapley-Shubik as robustness check

Verdict: **KNOWN TOOL; MERGE.**

## T130-05 — Model internal local pivotality as second tier

Verdict: **KNOWN TWO-TIER THEORY; MERGE INTO C019.**

## T130-06 — Correlation-sensitive federation weights

Verdict: **KNOWN IN VOTING THEORY; important C019 caveat.** Correlated preferences break pure square-root prescriptions.

## T130-07 — Quota can matter more than weight changes

Verdict: **KNOWN VOTING-POWER RESULT; operationally important.**

## T130-08 — Tiny community can have same top-tier power as much larger community

Verdict: **NOT A GENERAL THEORY; illustrative consequence of coalition geometry.**

## T130-09 — Large community can become dictator under simple-majority linear weights

Verdict: **KNOWN WEIGHTED-VOTING PHENOMENON; practical stress case.**

## T130-10 — Delegate count is not delegate power

Verdict: **KNOWN; practical.** Multiple delegates from one mandated bloc are not independent checks.

## T130-11 — Population definition matters

Children, provisional members, supported members, absent members, etc. can change nominal representation without changing who participates internally.

Verdict: **KNOWN REPRESENTATION QUESTION; practical.**

## T130-12 — Supermajority creates de facto veto/dummy positions

Verdict: **KNOWN POWER-INDEX PHENOMENON; practical.**

## T130-13 — New-community admission can discontinuously change everyone else's power

Verdict: **KNOWN COALITION-GAME EFFECT; practical reason for re-audit.**

## T130-14 — Equal community sovereignty and equal individual influence are incompatible objectives in many unequal-size federations

Verdict: **KNOWN FEDERAL REPRESENTATION TRADEOFF; practical.**

## T130-15 — Solve weights to desired powers rather than choose intuitive weights

Verdict: **KNOWN INVERSE VOTING-POWER PROBLEM; key operational component of C019.**

## T130-16 — Historical coalition behavior can replace random-vote assumptions

Verdict: **KNOWN EMPIRICAL POWER MODEL; practical robustness analysis.**

---

# E. Practical lessons to mirror into communities

1. distinguish voting weight from voting power;
2. explicitly choose whether the federation is equalizing communities, individuals, or a hybrid objective;
3. model the actual local decision tier as well as federation voting;
4. compute pivotal-power indices rather than assuming nominal weights produce equivalent influence;
5. treat square-root rules as assumption-dependent models, not recipes;
6. analyze quota and weights jointly;
7. stress correlated preferences, bloc voting, delegate discretion, abstention and historical coalitions;
8. re-audit power when communities join/leave or population changes;
9. inspect whether supermajorities create unexpected veto/dummy players;
10. define whose population counts and why;
11. if an intended power distribution matters, solve the inverse voting-power problem rather than hand-tuning weights;
12. publish the model assumptions and uncertainty so mathematical language does not create false legitimacy.

## Method lesson

The valuable cross-domain transfer can be **a question the target domain is not currently asking**, even when every mathematical component is old. Here the question is not `what weights seem fair?` but:

> **What distribution of actual individual/community influence does this complete two-tier rule create, under plausible behavior models, and is that the distribution we intended?**
