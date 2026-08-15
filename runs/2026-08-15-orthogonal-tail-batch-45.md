# Orthogonal Tail Batch 45 — Couples / Households in Federated Community Matching

Date: 2026-08-15

## Outcome

**No Creative Tail survivor.**

Matching-with-couples theory directly owns the root structure: when pairs have joint preferences over pairs of placements, stable matching can fail to exist; algorithms can fail to find an existing stable solution; near-feasible solutions can sometimes be obtained through small capacity perturbations.

The communal federation transfer is still practically important as an extension of C013 and C009.

---

# Core problem

A federation matching process that works tolerably for independent seekers can behave differently when applicants are linked:

- romantic couples;
- coparents and children;
- households;
- care dyads;
- close friends unwilling to separate;
- people willing to split only between nearby communities.

The relevant preference object is not `person A ranks communities` plus `person B ranks communities` independently. It can be a ranking over **pairs/configurations of placements**.

## Literature collision

Kojima/Pathak/Roth show that stable matching may not exist when couples are present. Klaus/Klijn/Massó show algorithmic problems can persist even with responsive preferences. Manlove et al. study almost-stable solutions when exact stability fails. Nguyen/Vohra show a nearby stable problem can sometimes be reached through small capacity perturbations.

**Disposition: no novelty claim.**

---

# Practical extensions to C013

## B45-L01 — Treat linked households as joint preference objects

Do not split a couple/household into nominally independent applicants and then hope to repair the result afterward.

Represent acceptable configurations explicitly:
- same community;
- specified nearby-community pairs;
- one community only if both admitted;
- temporary split allowed for N weeks;
- no split acceptable.

## B45-L02 — Do not promise that a stable matching always exists

A matching round can have no assignment where every seeker/household and community lacks a mutually preferable deviation.

If using coordinated clearing, label the objective honestly:
- stable if available;
- minimum-blocking / best feasible under declared constraints;
- or simple recommendations rather than binding assignments.

## B45-L03 — Preserve local admission authority and household opt-out

C013 already requires this. Couples constraints make coercive centralized assignment even less defensible.

## B45-L04 — Keep a small placement-slack reserve where feasible

Matching theory suggests tiny capacity changes can make an infeasible coupled market feasible.

Communal analogues:
- one flexible guest/trial room;
- temporary over-capacity housing with safeguards;
- a federation transition house;
- delayed finalization of one opening;
- nearby-community paired placement;
- temporary satellite housing.

Do not interpret this as `always overfill housing`; capacity, safety and consent remain hard constraints.

## B45-L05 — Market thickness matters even more with linked applicants

A thin federation may have no useful centralized-clearing advantage if there are only a few openings and linked household constraints consume most feasible combinations.

Pool across time/geography only where waiting/mobility costs are acceptable.

## B45-L06 — Couple/household constraints interact with C009 cohort composition

A household is already a mini-cohort. Its addition can interact with:
- childcare load;
- age distribution;
- work skills;
- faction/relationship topology;
- housing configuration;
- future births/care needs.

Set-level admission analysis becomes more relevant during expansion/founding waves.

## B45-L07 — Do not hide linked constraints until final ranking

Seekers and communities should disclose hard co-placement requirements before the clearing stage, while preserving privacy around irrelevant relationship details.

Hidden late constraints can invalidate the entire proposed assignment.

## B45-L08 — Distinguish hard constraints from preferences

Examples:
- `must live together` may be hard;
- `prefer same work area` may be soft;
- `need communities within 20 km due coparenting` may be hard;
- `prefer not to split temporarily` may be soft.

The algorithm/process should not infer this from rankings alone.

## B45-L09 — When exact stability fails, report blocking configurations

Instead of just returning `no solution`, identify:
- which household/community pairs generate conflicts;
- which capacity/resource constraint blocks feasibility;
- what small changes would create a feasible alternative.

This supports human negotiation rather than black-box rejection.

## B45-L10 — Capacity flexibility should be valued partly by option value

An empty flexible room/slot can look inefficient until it resolves a linked-household placement or crisis transfer.

This is ordinary slack/option-value reasoning; no novelty claim.

## B45-L11 — Nearby split placement creates federation-interface obligations

If members of one household live in different communities, clarify:
- childcare/care duties;
- transport;
- voting/membership status;
- labor obligations;
- benefits;
- privacy/records;
- conflict jurisdiction.

Otherwise the matching solution can create a governance problem.

## B45-L12 — Evaluate household outcomes, not only placement completion

A technically feasible match that later destabilizes the household/community is not success.

Follow:
- retention;
- household stability;
- childcare burden;
- satisfaction;
- transfer/exit;
- community effects.

---

## Disposition

No Creative Tail survivor.

Practical extension:

> **Federated applicant clearing should model couples/households as linked configurations, admit that exact stability can fail, and retain some bounded placement slack/nearby-placement flexibility rather than treating every vacancy as an independently filled slot.**
