# Orthogonal Tail Batch 31 — Fission, Merge, and Accidental Political Incentives

Date: 2026-08-15

## Outcome

One narrow provisional cross-domain survivor:

- **C020 — Fission/merge representation-effect audit**

The source mathematics is established: weighted-voting theory explicitly studies player splitting, merging, annexation, false-name manipulation, and the resulting change in Banzhaf/Shapley power. Dynamic federation research also studies fair representation as child communities form and federation structure evolves.

The surviving target transfer is narrower and tied to this project's reproduction criterion:

> **When community formation/fission/merger is a legitimate movement lifecycle process, explicitly measure and choose the political representation effect of that structural change instead of letting the voting rule create an accidental subsidy or penalty to reproduction.**

This is not an anti-splitting/Sybil rule. Legitimate daughter communities may deserve separate political voice. The new design question is whether the resulting gain/loss of aggregate lineage/member influence is intentional.

---

# A. Why this matters for communal reproduction

The project treats successful daughter-community formation as a major success criterion. C005 already says reproduction should become ordinary rather than jackpot-like.

Federation governance can quietly change the incentive to reproduce:

- **one-community/one-vote** generally gives organizational separation more representation units;
- **population-linear weights** preserve total nominal weight after a population-preserving split but can still change actual pivotal power because the player/coalition geometry changes;
- **concave weights such as square roots** mechanically increase the sum of nominal weights when one population is split (`sqrt(n1)+sqrt(n2) > sqrt(n1+n2)`), but actual pivotal power can still rise, fall, or remain unchanged depending on the quota and other members;
- **merger** creates the reverse possibility: two communities may lose or gain aggregate power when they become one legal member.

Therefore a federation can unintentionally:

- politically reward fission;
- politically punish fission;
- reward merger/consolidation;
- punish merger;
- create strategic pressure to remain institutionally fragmented or consolidated for representation rather than community-development reasons.

---

# B. Source-domain collision boundary

## Weighted-voting split/merge manipulation

Aziz & Paterson and subsequent weighted-voting work explicitly analyze how splitting one weighted voter into multiple identities, or merging players, changes Banzhaf/Shapley-Shubik power. This fully owns the mathematical fact that player boundaries can alter power.

**Not novel.**

## Dynamic child-community representation

Shapiro & Talmon's 2025 Grassroots Democratic Federation work explicitly models federations whose child communities form and evolve dynamically and imposes fairness conditions on representation of child communities.

This is a strong near-collision with the broad proposition `representation should remain fair as child communities form`.

**Therefore that broad claim is rejected.**

## Cooperative target reality

Cooperative law in several jurisdictions recognizes both:

- division of one cooperative into multiple new cooperatives; and
- cooperative federations whose member cooperatives can receive one vote each or multiple votes based on membership/business formulas.

Thus the representation/fission interaction is a real cooperative institutional issue, not a metaphor.

The target search did **not** locate a cooperative/intentional-community federation procedure that routinely performs an explicit before/after voting-power audit of legitimate member-community division/merger and classifies the change as an intended or unintended reproduction incentive.

**C020 survives only at this narrow operational layer.**

---

# C. C020 — operational architecture

## 1. Declare the structural event

Before admitting daughters created from a parent member, or recognizing a merger, classify the change:

- genuine fission into operationally autonomous communities;
- administrative/legal split with continued unified governance;
- merger with substantial continuing internal autonomy;
- temporary multi-site structure;
- spinout/new independent community with partial parent lineage;
- unrelated new community.

Do not equate every new legal entity with a genuinely new political community.

## 2. Define the representation objective

Choose explicitly whether federation representation is trying to track:

- autonomous communities as political units;
- individual members/residents;
- both, through a hybrid rule;
- movement lineages/founding units;
- another stated objective.

Different objectives imply different desired fission effects.

## 3. Compute before/after power

For the actual federation rule, calculate before and after:

- nominal weights/seats;
- Penrose-Banzhaf or other appropriate pivotal-power measure;
- veto/dummy status;
- minimum winning coalitions;
- aggregate power of the parent lineage/daughters when they vote identically;
- daughter powers when they vote independently;
- sensitivity to quota and abstention.

C019's warning applies: nominal weight preservation is not power preservation.

## 4. Run an aligned-preference counterfactual

A useful constitutional regression test is:

> **If the daughters contained the same total people and voted identically to the unsplit parent, how much would aggregate federation power change solely because one institutional boundary became two?**

Call this a **split/merge representation effect**, not automatically a defect.

If the federation wants organizational sovereignty to matter independently of population, a non-zero effect may be deliberate.

## 5. Publish the political reproduction effect

Before finalizing representation after fission/merge, state plainly:

- aggregate power before;
- aggregate aligned-daughter power after;
- independent-daughter power range after;
- whether the difference is an intended autonomy premium, population correction, or accidental artifact;
- whether the rule creates a plausible strategic incentive for/against structural splitting.

## 6. Avoid automatic anti-fission fixes

Do not punish daughters merely because false-name manipulation exists mathematically.

A real daughter community may acquire:

- distinct land/site;
- separate budget and risk;
- separate membership;
- independent internal governance;
- genuinely different interests.

Separate political voice can therefore be substantively justified.

The design principle is **explicitness**, not compulsory invariance.

---

# D. Conditional numerical illustrations

These examples reuse the Batch 30 toy populations `[100, 64, 9]` only to demonstrate structural effects. They are **not claims about the live 2026 FEC voting rule**.

## Illustration 1 — one-community/one-vote

Before a split, three equally weighted communities under simple majority have Banzhaf power `1/3` each.

If the 100-person community genuinely splits into two autonomous 50-person daughter communities and each organization receives one vote, there are now four equal organizational voters. Under strict majority, each has power `1/4`, so the two daughters' aligned aggregate top-tier power is `1/2`.

The lineage moves from `1/3` to `1/2` aggregate power solely because one organizational voter became two.

That may be a desired autonomy premium; if not, it is an accidental fission subsidy.

## Illustration 2 — linear population weights, 60% quota

Before split:

- weights `[100,64,9]`;
- quota = 60% of total;
- normalized Banzhaf powers = `[0.60, 0.20, 0.20]`.

Split the 100-person parent into two 50-person daughters while preserving total population:

- weights `[50,50,64,9]`;
- same absolute 60%-of-population quota;
- normalized Banzhaf powers = `[0.25, 0.25, 0.4167, 0.0833]`.

The aligned daughter lineage now has aggregate top-tier Banzhaf power `0.50`, **less** than the unsplit parent's `0.60`, despite total nominal population weight being unchanged.

So linear population weighting can create a fission **penalty** in actual pivotal power.

## Illustration 3 — square-root weights

Before split with square-root weights `[10,8,3]` at 60% quota, the top-tier Banzhaf distribution is `[0.60,0.20,0.20]`.

After splitting 100 into 50+50, the two daughter nominal weights sum to about `14.14`, exceeding the parent's old nominal weight `10` because square-root weighting is concave.

But after recalculating the full 60% game, all four players can have equal Banzhaf power `0.25`, giving the daughters aggregate `0.50`—again **less** than the parent's old `0.60`.

This is a useful warning:

> **Even when a weighting formula visibly rewards splitting at the nominal-weight level, the actual voting-power effect can point the other way.**

That is why C020 inherits C019's requirement to calculate power under the complete rule.

---

# E. Candidate audit

At least fourteen candidates were screened.

## T131-01 — Splitting can increase voting power
**Verdict:** REJECT AS NOVEL. Direct false-name/splitting-manipulation literature.

## T131-02 — Merging can change aggregate power
**Verdict:** REJECT AS NOVEL. Direct weighted-voting merge/annexation literature.

## T131-03 — Child-community representation should stay fair during growth
**Verdict:** REJECT AS NOVEL. Grassroots Democratic Federation directly models dynamic child-community representation fairness.

## T131-04 — One-community/one-vote rewards legal splitting
**Verdict:** REJECT AS NOVEL/OBVIOUS once stated; practical illustration only.

## T131-05 — Square-root weights mechanically reward split nominal weights
**Verdict:** REJECT AS MATHEMATICAL CONSEQUENCE. Concavity of square root.

## T131-06 — Linear population weights can still alter power after population-preserving split
**Verdict:** KNOWN weighted-voting consequence; important C020 operational input.

## T131-07 — Fission-neutrality as universal fairness axiom
**Verdict:** REJECT. Separate autonomous communities may legitimately deserve separate political voice; universal invariance would bake in one contested political philosophy.

## T131-08 — Aligned-preference split/merge regression test
**Verdict:** MERGE INTO C020. Useful diagnostic, not asserted universal axiom.

## T131-09 — Representation effect as reproduction subsidy/penalty
**Verdict:** SURVIVING TARGET CONNECTION. This ties community reproduction incentives to federation power architecture.

## T131-10 — Lineage-based permanent voting cap
**Verdict:** REJECT. Can entrench founder lineages and punish real autonomy.

## T131-11 — Temporary grace period before daughters receive separate representation
**Verdict:** REJECT AS GENERAL RULE. Could be appropriate locally but is arbitrary without objective/transition rationale.

## T131-12 — Separate voice floor + population component
**Verdict:** KNOWN HYBRID REPRESENTATION FAMILY; practical option, not discovery.

## T131-13 — Merger neutrality audit
**Verdict:** MERGE INTO C020. Same structural diagnostic in reverse.

## T131-14 — Recompute all players' power, not just parent/daughters
**Verdict:** KNOWN cooperative-game effect; essential practical step because fission can redistribute power among third-party communities.

---

# F. Practical lessons to mirror into communities

1. federation representation can create a political subsidy or penalty to community reproduction;
2. before/after any member-community fission or merger, recompute actual coalition power rather than only nominal weights;
3. run an aligned-preference split/merge counterfactual to isolate the effect of organizational boundaries;
4. explicitly decide whether separate autonomous communities deserve a political voice premium independent of population;
5. distinguish genuine autonomous fission from administrative/legal fragmentation;
6. analyze effects on **all** federation members, not only the parent/daughters;
7. do not use false-name/Sybil analogies to delegitimize real daughters—use that literature only for the power mathematics;
8. do not assume linear population weights are fission-neutral in power;
9. do not assume square-root weights have predictable split effects without recomputing quota/coalitions;
10. publish the representation effect as part of a planned-fission protocol so political incentives do not remain hidden.

## Method lesson

A known strategic-manipulation result can become a legitimate cross-domain finding only after removing the manipulative framing and asking what the same mathematics implies for a **desirable target process**. Community reproduction is not a false-name attack, but both change the player partition of the federation game. The novel target question is whether the political consequence of that legitimate partition change is intended.
