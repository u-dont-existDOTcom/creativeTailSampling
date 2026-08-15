# Orthogonal Tail Batch 53 — Non-Custodial Federation Research via Privacy-Preserving Computation

Date: 2026-08-15

## Outcome

One provisional target-domain survivor:

- **C024 — Non-custodial federation research**

The cryptographic/statistical source mechanisms are established: secure aggregation, secure multiparty computation (MPC), federated analytics, differential privacy, secret sharing and privacy-preserving computation.

The surviving communal transfer is the **trust architecture**:

> **For suitable federation-wide sensitive analyses, design the computation so neither local community leadership nor the federation research center needs to possess members' raw answers in readable form.**

This does not eliminate output disclosure risk. C024 must be paired with C023 cumulative disclosure control.

---

# Source-domain collision boundary

Secure MPC permits multiple parties to compute functions of private inputs while revealing only the intended output, not the individual inputs.

Federated analytics similarly computes aggregate analytics across distributed clients/institutions without centralizing raw data.

Secure aggregation protects individual contributions from the aggregator, but the final aggregate can still leak individual information when the group is small or auxiliary information is strong.

Differential privacy or other disclosure control can protect outputs, at a utility cost.

Therefore no cryptographic primitive here is new.

Target searches did not locate a close intentional-community/ecovillage research system using secure aggregation/MPC/federated analytics to gather sensitive communal wellbeing/safety/governance evidence without central raw-data custody.

---

# C024 — Non-custodial federation research

## Plain proposition

Batch 43 says members may distrust the survey if they believe either their local leaders or federation analysts can identify their unfavorable answers.

The ordinary fix is organizational:
- promise confidentiality;
- appoint an independent custodian.

C024 adds a technical option for suitable aggregate questions:

> **Make raw-answer access unnecessary by architecture.**

Examples:
- federation-wide prevalence of a sensitive experience;
- direct-vs-indirect reporting-bias diagnostic totals;
- overall satisfaction distribution;
- pooled rate of people privately considering transfer;
- measurement-canary classification distributions;
- aggregate outcomes among current vs former members.

The research center receives only the permitted aggregate/statistical result.

---

# Two-layer privacy architecture

## Layer A — input confidentiality

Goal: no single research administrator sees raw individual answers.

Possible techniques:
- secure aggregation;
- MPC / secret sharing between independent servers/organizations;
- federated analytics;
- encrypted local aggregation;
- split-key / threshold decryption.

## Layer B — output disclosure control

Goal: permitted aggregate itself does not expose an individual.

Use C023 controls:
- minimum safe aggregation scope;
- pooling;
- suppression;
- query/release ledger;
- differencing checks;
- formal differential privacy when justified;
- access tiers.

**Layer A without Layer B is insufficient.**

---

# Operational architecture

## C024-01 — Start with aggregate questions, not full raw-data replacement

High-value early use cases are simple statistics:
- count;
- sum;
- mean;
- histogram/category frequencies;
- simple contingency tables;
- selected reporting-pressure diagnostics.

Do not adopt heavy cryptography simply to replicate a spreadsheet workflow no one needs.

## C024-02 — Member submissions should bypass local community custody

Sensitive answers should go from the participant's private client/channel into the privacy-preserving protocol.

Local leadership should not receive plaintext copies.

## C024-03 — Split trust across institutions where feasible

One practical MPC architecture can use two or more non-colluding trustees, for example:
- federation research office;
- independent ombuds/research nonprofit;
- elected privacy trustee.

Each holds only a share needed for computation; no one alone can reconstruct individual responses.

The exact threat model must be explicit.

## C024-04 — Do not hide the threat model behind `encrypted`

State:
- who could collude;
- what servers/keys exist;
- whether malicious inputs are detectable;
- what metadata remains visible;
- what happens on dropout;
- who can authorize a query;
- what output is released.

## C024-05 — Participant verification should be possible without exposing answers

Need to prevent:
- duplicate submissions;
- outsiders flooding a commune's results;
- leaders submitting on behalf of members.

Possible design:
- anonymous/one-time eligibility tokens separated from response contents.

Eligibility verification and answer custody should be separate functions.

## C024-06 — Output query authorization must be governed

Even if raw data are hidden, an analyst who can ask unlimited aggregates can reconstruct individuals.

Therefore combine with C023:
- query approval;
- release ledger;
- cumulative disclosure budget;
- minimum cohort/aggregation conditions.

## C024-07 — Explain privacy in member-comprehensible terms

The method only improves Batch 43 reporting validity if participants understand the protection enough to trust it.

Provide a plain-language statement such as:

`No community leader and no federation researcher receives your individual answer. Your response is mathematically combined with many others before anyone can read a result.`

Do not promise more than the protocol actually guarantees.

## C024-08 — Verify the software/protocol independently

A privacy claim dependent on software should have:
- open specification/code where possible;
- independent security review;
- reproducible deployment/configuration;
- public threat model;
- incident/update process.

## C024-09 — Keep opt-out and alternative participation routes

Do not force all research into a cryptographic system that some members cannot use.

Provide accessible alternatives with equivalent confidentiality protections where possible.

## C024-10 — Secure aggregation does not make dishonest answers truthful

It reduces custody/reprisal risk.

It does not eliminate:
- identity-protective beliefs;
- social desirability unrelated to actual disclosure risk;
- coordinated lying;
- misunderstanding;
- bad question design.

Combine with Batches 43–44.

## C024-11 — Secure computation can also reduce federation capture risk

Even benevolent analysts cannot later misuse raw data they never possessed.

This matters if:
- federation leadership changes;
- records are subpoenaed/stolen;
- research center becomes politicized;
- one faction captures governance.

## C024-12 — Some research still legitimately requires controlled raw data

Qualitative interviews, case reconstruction, safeguarding investigations and complex validation may need identifiable/contextual information under consent/legal rules.

C024 is not a universal replacement.

## C024-13 — Community-specific statistics may be impossible under strong privacy

If a commune has eight members, secure aggregation cannot make an exact eight-person sensitive mean non-identifying.

The answer may need to remain:
- private to participants;
- federation-pooled;
- noisy/coarsened;
- unpublished.

## C024-14 — Use federation scale to make indirect survey methods practical

B44 list/randomized-response techniques are too noisy for single communes.

Non-custodial federation aggregation can pool them across many compatible communities without centralizing raw answers.

## C024-15 — Distinguish local vs central DP

Local differential privacy perturbs answers before they leave the participant but can require much more noise.

Secure aggregation can allow more accurate central/statistical DP because no central analyst sees plaintext individual responses during aggregation.

Choose based on threat model and sample size rather than ideology.

## C024-16 — Privacy architecture can become part of methodological validation

Batch 44 can randomize ordinary confidentiality vs stronger non-custodial mode (where ethically feasible) to measure whether improved technical privacy changes sensitive reporting.

If it does, that is evidence that custody fear was affecting the measurement channel.

---

# Distinctive target predictions

If C024 is valuable:

1. stronger non-custodial privacy should increase trust/confidence among at least some members relative to organizational confidentiality promises;
2. some sensitive response distributions may shift under the stronger architecture, revealing custody-sensitive reporting;
3. federation-wide aggregate analysis can remain possible even when communities refuse to transfer raw sensitive microdata;
4. later federation political capture/data breach creates less harm because raw historical responses do not exist centrally;
5. output privacy, not input encryption, becomes the limiting factor for very small community-specific statistics.

---

# Falsifiers / demotion conditions

Demote C024 if:
- members do not understand/trust the architecture and reporting behavior does not improve;
- operational complexity causes low participation/data loss greater than privacy gains;
- the research questions require contextual microdata so frequently that secure aggregate use is marginal;
- existing intentional-community research already implements a substantially equivalent non-custodial architecture;
- simple independent custody + strong access controls delivers essentially the same practical trust/validity at much lower cost for the movement's scale.

---

## Disposition

**SURVIVES provisionally as C024 — Non-custodial federation research.**

Claim only the intentional-community federation research architecture. MPC, secure aggregation, federated analytics, secret sharing and differential privacy are established source technologies.

Core rule:

> **For sensitive aggregate questions, minimize not only who is allowed to read raw data, but whether readable centralized raw data ever needs to exist. Then separately control what can be inferred from the aggregate outputs.**
