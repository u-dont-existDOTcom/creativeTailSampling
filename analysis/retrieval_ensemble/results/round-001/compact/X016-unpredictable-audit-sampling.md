# X016-unpredictable-audit-sampling

**Candidate:** For federation audits, freeze the eligible universe before future randomness is knowable, precommit deterministic selection, use uncontrollable future randomness, and make the realized draw replayable afterward.

## Exa

### 1. Commit-Reveal for Scheduled Draws — Provable.io Docs
- URL: https://provable.io/docs/commit-reveal-scheduled-draws
- Published: 2026-05-25T00:00:00.000Z
- Query families: alternate_terminology, falsification, source_domain, target_neighbor
- Excerpt: A regular`/api/ints` draw is verifiable after the fact, but the server picked the seed in the same moment you sent the request — a sufficiently motivated server operator could in principle pick a seed favorable to them. Commit-reveal eliminates that worry by splitting the draw into two HTTP calls separated by time: ... 1. Commit. The server picks a fresh`serverSeed`, publishes its`serverHash`, and locks the seed away. You publish that hash somewhere durable (a pinned post, a tweet, a blockchain transaction) before entries close. 2. Reveal. Later, when it's time to run the draw, you submit your`clientSeed` and parameters. The server runs the generator against the committed seed and returns the outcome plus the seed itself, so anyone can check the math. ... Because the hash was published before anyone knew the clientSeed or the entry list, the server couldn't have picked a seed designed to

### 2. RFC 3797:  Publicly Verifiable Nominations Committee (NomCom) Random Selection
- URL: https://www.rfc-editor.org/rfc/rfc3797
- Published: N/A
- Query families: alternate_terminology, falsification, source_domain, target_neighbor
- Excerpt: 2.2. Publication of the Algorithm The exact algorithm to be used, including the public future sources of randomness, is made public. For example, the members of the final list of eligible volunteers are ordered by publicly numbering them, some public future sources of randomness such as government run lotteries are specified, and an exact algorithm is specified whereby eligible volunteers are selected based on a strong hash function [RFC 1750] of these future sources of randomness. ... 3. Randomness The crux of the unbiased nature of the selection is that it is based in an exact, predetermined fashion on random information which will be revealed in the future and thus can not be known to the person specifying the algorithm. That random information will be used to control the selection. The random information must be such that it will be publicly and unambiguously revealed in a timely fas

### 3. Verifiable randomness | ICP Developer Docs
- URL: https://docs.internetcomputer.org/concepts/verifiable-randomness/
- Published: N/A
- Query families: alternate_terminology, falsification, source_domain, target_neighbor
- Excerpt: unpredictable random numbers ... : lotteries, ... node must agree ... Consensus-based protocols execute every transaction deterministically. Each node replays the same operations and must arrive at the same state. This means randomness sources available to normal programs (such as OS entropy (`/dev/urandom`), hardware timers, or per-process seeds) cannot be used directly: they would produce different values on each replica, breaking consensus. ... - Next steps - Block hashes as seeds. Miners or validators can selectively publish or withhold blocks to influence outcomes. Any actor who produces blocks can bias the result. - Commit-reveal schemes. Participants can abort after seeing others’ commitments, biasing the outcome in their favor if abstaining is cheaper than losing. - Trusted oracles. External randomness sources reintroduce centralization and single points of failure: contradicting

### 4. N/A
- URL: https://www.rfc-editor.org/rfc/rfc3797.html
- Published: N/A
- Query families: alternate_terminology, falsification, target_neighbor
- Excerpt: 2.2. Publication of the Algorithm The exact algorithm to be used, including the public future sources of randomness, is made public. For example, the members of the final list of eligible volunteers are ordered by publicly numbering them, some public future sources of randomness such as government run lotteries are specified, and an exact algorithm is specified whereby eligible volunteers are selected based on a strong hash function [RFC 1750] of these future sources of randomness. ... 3. Randomness The crux of the unbiased nature of the selection is that it is based in an exact, predetermined fashion on random information which will be revealed in the future and thus can not be known to the person specifying the algorithm. That random information will be used to control the selection. The random information must be such that it will be publicly and unambiguously revealed in a timely fas

### 5. RFC 2777: Publicly Verifiable Nomcom Random Selection | RFC Editor
- URL: https://www.rfc-editor.org/info/rfc2777/
- Published: 2000-02-01T00:00:00.000Z
- Query families: alternate_terminology, falsification, target_neighbor
- Excerpt: 1. Introduction Under the IETF rules, each year 10 persons are randomly selected from among the eligible persons who volunteer to be the voting members of the nominations committee (NomCom) to nominate members of the Internet Engineering Steering Group (IESG) and the Internet Architecture Board (IAB) [RFC 2727]. The number of eligible volunteers in recent years has varied in the approximate range of 40 to 60. It is highly desireable that the random selection of the voting NomCom be done in a unimpeachable fashion so that no reasonable charges of bias or favoritism can be brought. This is for the protection of the IETF from bias and protection of the administrator of the selection (currently, the appointed non-voting NomCom chair) from suspicion of bias. A method such that public information will enable any person to verify the randomness of the selection meets this criterion. This docume

### 6. A Fair, Traceable, Auditable and Participatory Randomization Tool for Legal Systems
- URL: https://doi.org/10.48550/arxiv.2006.02956
- Published: 2020-06-04T00:00:00.000Z
- Query families: alternate_terminology, source_domain
- Excerpt: jurors [6] and judges [7], in which the main goal is to guarantee that each candidate has a pre-defined (not necessarily uniform) probability of being picked. In this scenario, though, randomization comes with two additional requirements: auditability by design and active social engagement. More precisely, auditability by design improves the trust in the system. Hence, it can avoid suspicions commonly raised when statistical deviations are observed in a non-auditable random procedure [19], even if such biases are not the result of ill-intent. Meanwhile, an active, self-reflective and well-coordinated participation by pertinent members of a community can result in more engagement and inclusiveness, relevant aspects of social practices that also apply to the legal system [36, 40]. Combined, such requirements can help legal systems to achieve an important goal: to ensure that its norms (exp

### 7. draft-hoffman-random-candidate-selection-02
- URL: https://datatracker.ietf.org/doc/html/draft-hoffman-random-candidate-selection
- Published: N/A
- Query families: falsification, target_neighbor
- Excerpt: This document describes a process to randomly select a subset of named candidates from a larger set of candidates. The process uses an unpredictable value that can be trusted by all candidates.¶ ... It is common to need to pick a subset of people from a larger group using a random selection method. This is often done on an ad hoc basis, but for some selections, a more formal process is needed, particularly if the people in the larger group don't all trust the administrator of the selection process to be unbiased.¶ ... This document gives a simple, understandable process that can be done for groups and subsets of arbitrary size. The process is purposely transparent and reproducible. It works with any group of entities that have names: people, companies, locations, and so on.¶ ... As a simple example, a future leadership committee will have a fixed size. The members of the committee will b

### 8. draft-thomson-elegy-vrs-00
- URL: https://datatracker.ietf.org/doc/html/draft-thomson-elegy-vrs-00
- Published: N/A
- Query families: falsification, source_domain
- Excerpt: On occasion, a group of people might agree that it is necessary to select from a set of options, but cannot agree on a selection. In such cases, a random selection might be acceptable, but any potential for bias might not be.¶ ... A process for selection in way that is verifiable and not subject to bias or influence by any party can be useful in such situations. This document describes one such process.¶ ... IETF Nominating Committee [NOMCOM] is an example of where a random selection is necessary. Ten people are drawn from ... larger pool of eligible volunteers ... selected group is entrusted with considerable responsibility, there is a need to avoid any risk of bias in the outcome.¶ ... This document describes a process that is an alternative to RFC 3797 [RFC3797].¶ ... A random selection process might be invoked to select a subset of one or more items from a longer list of options. The

### 9. Interoperable Randomness Beacons | CSRC
- URL: https://csrc.nist.gov/Projects/interoperable-randomness-beacons/apps
- Published: N/A
- Query families: alternate_terminology, source_domain
- Excerpt: A generic application (app, for short) of beacon randomness is enabling public-verifiability of randomized procedures. For example, when randomly sampling for audits, auditors are prevented from biasing the selections (or being accused of it), and auditees are prevented from knowing the selections in advance (or being accused of it). ... An interesting randomness/determinism duality: although beacon applications relate to the use of randomness, their public auditability requires a well specified deterministic operation (which then uses as input the needed random values). ... 1. Commit upfront: publish a statement \(S\) that explains the deterministic operation that will use the Beacon randomness (the output value randOut) from future time \(t\); 2. Derive a seed: Get \(R={\tt randOut}[t]\) (from the pulse with timestamp \(t\)), and set the seed as \(Z=Hash(S||R)\) 3. Perform the operatio

### 10. Interoperable Randomness Beacons | CSRC
- URL: https://csrc.nist.gov/projects/interoperable-randomness-beacons/apps
- Published: N/A
- Query families: falsification, target_neighbor
- Excerpt: A generic application (app, for short) of beacon randomness is enabling public-verifiability of randomized procedures. For example, when randomly sampling for audits, auditors are prevented from biasing the selections (or being accused of it), and auditees are prevented from knowing the selections in advance (or being accused of it). ... An interesting randomness/determinism duality: although beacon applications relate to the use of randomness, their public auditability requires a well specified deterministic operation (which then uses as input the needed random values). ... 1. Perform the operation: Do what the statement \(S\) promised, using \(Z\) as the seed for all needed pseudo-randomness. 2. Derive a seed: Get \(R={\tt randOut}[t]\) (from the pulse with timestamp \(t\)), and set the seed as \(Z=Hash(S||R)\) 3. Commit upfront: publish a statement \(S\) that explains the deterministi

## Parallel

### 1. (PDF) The Importance of Randomness in the Universe: Superdeterminism and Free Will
- URL: https://www.researchgate.net/publication/341397134_The_Importance_of_Randomness_in_the_Universe_Superdeterminism_and_Free_Will
- Published: 2021-08-01
- Query families: alternate_terminology, falsification, source_domain, target_neighbor
- Excerpt: With randomness in Nature, the universe could not have been predetermined completely in the sense that it should be impossible in principle to compute from the big bang or at any later moment whether live and conscious observers might or might not appear there.

### 2. Commit-Reveal²: Securing Randomness Beacons with Randomized Reveal Order in Smart Contracts
- URL: https://arxiv.org/html/2504.03936v2
- Query families: alternate_terminology, falsification, source_domain, target_neighbor
- Excerpt: To address this, we propose an in-protocol, low-overhead mechanism that restores liveness without external governance while preserving accountability and slashing as a future work. The design remains compatible with existing Commit-Reveal2 verification paths (e.g., EIP-712 signatures and Merkle-based checks) and uses a simple, deterministic selection rule. After the system enters HALTED and a fixed election delay elapses, any compliant operator may start an election round. The remaining active operators execute a lightweight, on-chain commit–reveal mini-round to derive election randomness

### 3. Exploring the NIST Randomness Beacon: A Deep Dive into Verif
- URL: https://umatechnology.org/exploring-the-nist-randomness-beacon-a-deep-dive-into-verifiable-randomness
- Published: 2026-05-19
- Query families: alternate_terminology, falsification, source_domain, target_neighbor
- Excerpt: tag=umatechnology09-20&linkCode=osi&th=1&psc=1&keywords=quantum+computers "Buy on Amazon") | Understanding the beacon means looking beyond the random number itself. Its architecture, signatures, hash chaining, access methods, and validation process all shape what guarantees it provides—and what guarantees it does not. Developers and researchers can use it effectively when they treat it as a public, verifiable randomness source rather than a universal substitute for local cryptographic random number generation. ## What the NIST Randomness Beacon Is The NIST Randomness Beacon is a public service operated by the National Institute of Standards and Technology that periodically publishes random values along with metadata that lets anyone identify, retrieve, and verify each publication. Its purpose is not to give a private secret to one user, as a cryptographic random number generator inside a

### 4. How to Achieve Randomness in a Smart Contract
- URL: https://www.flow.com/post/how-to-achieve-randomness-in-a-smart-contract
- Query families: alternate_terminology, falsification, source_domain, target_neighbor
- Excerpt: Revertible randomness is available instantly within the same transaction and is perfect for trusted transactions you call, such as distributing a prize to a random winner, generating raffle tickets for a later drawing, or anything else you call with a trusted user on your backend. In cases where the user might choose to revert the transaction (if they don’t like the outcome once the random result is revealed), you can double-down on security with a **Commit-Reveal scheme** . Using this technique, the user commits to randomness in one block and has it revealed in a future block. Users commit to using a future randomness without being able to predict it. Once committed, users cannot reverse their actions. **Check out the tutorial here** : [Native VRF with Commit-Reveal in Cadence](https://developers.flow.com/tutorials/native-vrf/commit-reveal-cadence) ‍ ## **Prefer EVM? Flow’s Got You Cove

### 5. Precommitment - Wikipedia
- URL: https://en.wikipedia.org/wiki/Precommitment
- Published: 2025-02-03
- Query families: alternate_terminology, falsification, source_domain, target_neighbor
- Excerpt: For the concept in cryptography, see commitment scheme . For the campaign to reduce self-harm by gamblers, see Andrew Wilkie . In psychology , **precommitment** is a strategy or a method of self-control that a person or organisation may use to restrict the number of choices available to them at a future time. [[ 1 ]](:2-1) Precommitment may also involve imposing obstacles or additional costs to certain courses of action in advance. Agents") may precommit themselves when they predict that their preferences will change but wish to ensure that their future actions will align with their current preferences. [[ 2 ]](:1-2) Precommitment has been studied as a bargaining strategy in which agents bind themselves to one course of action in order to enhance the credibility of present threats. Some scholars have proposed that collective political groups may also engage in precommitment by adopting c

### 6. Randomness | solidity-patterns
- URL: https://fravoll.github.io/solidity-patterns/randomness.html
- Query families: alternate_terminology, falsification, source_domain, target_neighbor
- Excerpt: Due to the commitment to a seed and the use of a future block hash, the generation of the random number comes with a little **delay** . In the fastest case a result can be expected after two blocks. When we compare these consequences with the ones of the Oracle pattern , we can work out their differences. The randomness provided by the Oracle can be true randomness, as we can query numbers from services providing true random numbers. While we only have to trust one party in our example, two parties have to be trusted when interacting with oracles: the data provider as well as the oracle service. Another difference is that the oracle service has to be paid for each request. The delay experienced with the oracle solution is comparable to the one proposed above. It can be concluded, that in simple contracts with no financial impact, a simple implication of block hash randomness without a se

### 7. The Knowable Future | Forecastability | Peter Catt
- URL: https://www.theknowablefuture.com/
- Query families: alternate_terminology, falsification, source_domain, target_neighbor
- Excerpt: top of page # The Knowable Future: Forecastability and the Limits of Prediction ## The limit on prediction is set by the information in the data, not the sophistication of the model. A research programme by Dr Peter Catt Auckland, Aotearoa New Zealand. ## The core research question: ## How far into the future does a time series contain usable information about its own evolution? Forecastability is the extent to which the past contains exploitable information about the future. It is a property of the series and the horizon, not of any model. The Knowable Future measures forecastability, maps how predictive information changes across forecast horizons, and identifies the limits of prediction in time series. It begins one step before model selection, with a prior question: how much of the future is actually knowable from the past? The answer varies across series and horizons. Some systems r

### 8. Upgrading Ethereum | 2.9.3 Randomness
- URL: https://eth2book.info/latest/part2/building_blocks/randomness/
- Query families: alternate_terminology, falsification, source_domain, target_neighbor
- Excerpt: For example, to selectively mount denial of service attacks against future proposers, or to bribe members of a particular committee, or to register especially advantageous validator numbers for themselves allowing them to take over a future committee, or simply to censor transactions.1 ... Intuitively, it is good for protocols to be unpredictable in the sense that miners do not learn that they are eligible to mine a block until shortly before it is due to be mined. Many attacks, such as double-spending, or selfish-mining, can become much more profitable if miners know in advance when they become eligible to mine. Unpredictability, arising from randomness, is an excellent first line of defence against many attacks.

### 9. GitHub - axiomzen/eth-random: commit-reveal RNG method in Ethereum · GitHub
- URL: https://github.com/axiomzen/eth-random
- Query families: alternate_terminology, source_domain, target_neighbor
- Excerpt: In addition to good quality of number generation, several concerns play when harvesting random numbers from blockchains, so let&#x27;s address the main points. Since the block hash in the future is unknown, it&#x27;s unpredictable at the time of commit. No user should be able to seed or tamper with the RNG input. As we discussed in item [1] above, counter measures must be in place to prevent &quot;re-rolls&quot;.

### 10. Truly Random Numbers — But Not by Chance | NIST
- URL: https://www.nist.gov/news-events/news/2012/10/truly-random-numbers-not-chance
- Query families: alternate_terminology, falsification, target_neighbor
- Excerpt: One is to <strong>generate a sequence of truly random numbers that is guaranteed by the laws of physics to be unknowable in advance of its generation, uncorrelated with anything in the universe</strong>.
