# N018-replicated-governance-tombstones

**Candidate:** When a high-consequence governance pattern is retired for a known failure, propagate a semantic deprecation record through the same daughter, template, and fork channels that could otherwise resurrect it.

## Exa

### 1. Deprecation discipline: canonical definition | Gautier Dorval
- URL: https://gautierdorval.com/en/definitions/deprecation-discipline/
- Published: 2026-05-09T00:00:00.000Z
- Query families: alternate_terminology, falsification, source_domain, target_neighbor
- Excerpt: Deprecation discipline: the controlled process that declares when a term, route, version, example, source or artifact should no longer govern interpretation while preserving enough trace to explain the change. ... Deprecation discipline matters because silent deletion rarely removes interpretive influence. Old pages can remain indexed, external links can keep circulating, models can retain prior summaries and users can cite archived language. Deprecation declares the status change instead of pretending that removal equals correction. It gives systems and readers a route from the old surface to the current canonical source. ... Phase 12 exists because a corpus does not remain authoritative merely by accumulating pages. It remains authoritative when its canon, links, artifacts, exclusions, definitions, source hierarchy, version states and correction states are maintained as a coherent syst

### 2. Tombstone Pattern · Agents Playbook
- URL: https://playbook.agentskit.io/docs/pillars/governance/tombstone-pattern
- Published: N/A
- Query families: alternate_terminology, falsification, source_domain, target_neighbor
- Excerpt: Retired content keeps its file but gets a 🪦 status block prepended. Back-references are updated to mark it retired without removing the link. The historical record stays intact; the agent reading the file knows immediately it is no longer active. ... 1. The decision trail. Future agents need to know that something was the answer, why it was, and why it changed. The file is the evidence. 2. Back-references. Other docs / ADRs / commit messages link to it. Hard links break; agents follow broken links and waste a turn. 3. Audit history. Compliance / governance / security reviews need to see what existed and when. ... Prepend to the top of the file, above the ... ``` > 🪦 **TOMBSTONED YYYY-MM-DD** — <one-line reason: what replaced it, or why retired>. > Kept for trail; do not treat as active. # <original title kept> <original body kept verbatim> ... - `🪦` emoji — visual signal. - `TOMBSTONED` 

### 3. structural-explainability/spec-gb
- URL: https://github.com/structural-explainability/spec-gb
- Published: 2025-12-31T00:00:00.000Z
- Query families: falsification, source_domain, target_neighbor
- Excerpt: defines what structural artifacts ... The purpose of GB is to specify what governance-level structures may be represented so that coordination, traceability, and accountability are possible without altering the neutral substrate. ... GB defines constraints on: ... - governance artifacts (e.g., specifications, adapters, profiles, appendices) - governance actions over artifacts (e.g., recorded publication, recorded approval, recorded deprecation, or recorded supersession) - versioning, dependency, and provenance structures ... GB does not define meaning, enforcement, or correctness of governance actions. ... GB protects the neutral substrate and downstream structural artifacts from a specific failure mode: ... - Unvalidated or unauthorized ... the system. ... - preserve conformance with Structural Explain ... - introduce explicit structural definitions and constraints via new identifiers -

### 4. When to Retire an ADR — Deprecation, Supersession, and the Never-Delete Rule — WhyChose
- URL: https://whychose.com/seo/when-to-retire-an-adr
- Published: 2026-05-31T00:00:00.000Z
- Query families: alternate_terminology, falsification, source_domain
- Excerpt: Unlike supersession, deprecation touches exactly one file. There is no second ADR to write and no bidirectional pointer to maintain. The three changes are: ... 1. Status: Deprecated — this is the canonical value. Do not use Obsolete, Retired, Archived, or Inactive. These non-canonical variants cause the ADR GitHub Action auto-index job to treat the file as having an unrecognized status, which produces a broken row in the generated index table. The five canonical values the tooling knows are Proposed, Accepted, Superseded, Deprecated, and Rejected. ... 2. A Notes entry in the format `Deprecated YYYY-MM-DD: [one-sentence reason].` Written at the top of the Notes section in reverse-chronological order, consistent with how all Notes entries are written. ... 3. Optionally: Deprecated-by: [pointer] — a PR URL, Jira ticket, migration guide URL, or commit SHA that explains why the decision becam

### 5. Chapter 23. Retirement, Replacement, and End-of-Life Discipline - Secure AI Agent Architecture
- URL: https://agent-axiom.github.io/agent-arch/en/book/part-viii/chapter-23/
- Published: N/A
- Query families: source_domain, target_neighbor
- Excerpt: If support-triage v2 replaces the old path that once created duplicate tickets, retirement must prove that the old`create_support_ticket` path can no longer act. Removing the prompt route is not enough: the team must close the tool principal, revoke gateway exposure, expire paused approvals, stop background retries, and preserve the audit trail so a future duplicate cannot be blamed on an “unknown” old agent. ... Retirement case-spine note: each canonical case retires a different kind of right to act. Support triage retires deprecated write paths and paused approvals; Internal knowledge assistant retires stale corpora, obsolete embeddings, and memory-write rules; Incident coordination retires emergency-only capabilities, escalation routes, and notification channels once the response path is no longer valid. A retirement plan that only deletes a runtime leaves old authority behind. ... re

### 6. Deprecations — CASRAI
- URL: https://casrai.org/standards/deprecations
- Published: N/A
- Query families: alternate_terminology, source_domain
- Excerpt: Every URI we have ever published continues to resolve, and every deprecated URI carries a forward pointer to its successor — for the lifetime of the vocabulary. ... When a CASRAI term, picklist entry, object template, or domain identifier is superseded, the change is recorded as a chain: the deprecated URI points forward to its replacement via a typed relationship, and the replacement carries a reciprocal back-pointer to the term it replaced. The chain can extend: if a replacement is itself later replaced, the original URI is updated to point at the most recent successor while preserving the intermediate chain in the chain's history. Implementers traversing the chain reach the current canonical successor; implementers checking the history can see how the concept evolved. ... - `movedTo`— the deprecated entry has been transferred to a different steward's vocabulary (typically a federation

### 7. Obsolescence control: canonical definition | Gautier Dorval
- URL: https://gautierdorval.com/en/definitions/obsolescence-control/
- Published: 2026-05-09T00:00:00.000Z
- Query families: falsification, target_neighbor
- Excerpt: Obsolescence control: the governance of outdated, superseded, stale or context-expired pages, sources, examples, artifacts and memory states before they continue to influence new interpretation. ... Obsolescence control matters because old material often remains technically available and semantically active. A page can be outdated without being false, an example can be historical without being governing, and a source can remain accessible while losing authority. If obsolescence is not controlled, systems may treat availability as relevance and persistence as current authority. ... a coherent system. ... - historical examples are cited as current policy. - a superseded artifact remains easier to retrieve than the current one. - old blog posts outrank current definitions internally. - memory states reuse expired assumptions. - deprecation notices are missing from obsolete routes. ... At mi

### 8. seps/2596-spec-feature-lifecycle-and-deprecation.md
- URL: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/seps/2596-spec-feature-lifecycle-and-deprecation.md
- Published: N/A
- Query families: alternate_terminology, target_neighbor
- Excerpt: A Deprecated feature MAY be restored to Active by a SEP that supersedes the deprecation SEP and documents the changed circumstances. Restoration follows the same approval path as deprecation. If the feature is later deprecated again, the minimum deprecation window in [Deprecating a feature](#deprecating-a-feature) is measured afresh from the revision in which the new deprecation takes effect. ... When the deprecation SEP reaches Final the deprecation is scheduled: the following changes land in the draft specification (`schema/draft/` and `docs/specification/draft/`). The feature becomes Deprecated when the revision carrying these changes is released as Current under the [versioning guide][versioning], and the minimum deprecation window is counted from that release. Anchoring the clock to the revision release means every feature deprecated in the same revision shares one earliest removal 

### 9. specs/03-OMEGA-04_EXTENSION_GOVERNANCE.md
- URL: https://github.com/SymbolGroundingFramework/SGF-manifest/blob/main/specs/03-OMEGA-04_EXTENSION_GOVERNANCE.md
- Published: N/A
- Query families: falsification, target_neighbor
- Excerpt: What has been missing is ... governance envelope around the public exercise of `META_DEFINITION_RULE`. The mechanism is in the spec. The procedure for using it on shared canonical vocabulary is what this ... specifies. The honest declaration is that the ... voluntarily binds itself: it grants extension authority, but it ... it through a named procedure, with ... limits, and named recovery paths. ... Standing to propose an extension is open. Any party may draft a `META_DEFINITION_RULE` invocation and circulate it. Standing to ratify an extension into the canonical vocabulary is not open. Ratification requires: ... 1. **A rationale record.** A structured artifact answering: what gap does this extension fill, what alternatives were considered, why this design. The rationale record becomes part of the canonical lineage. A ratified extension without a rationale record is malformed. ... 2. **P

### 10. A.6.6 Base Declaration Discipline - Kind-explicit, scoped, witnessed base declaration discipline (with base-change lexicon) - FPF Reference
- URL: https://fpf.sh/generated/patterns/A.6.6
- Published: N/A
- Query families: source_domain
- Excerpt: These names denote semantic change classes. In decision/publication lanes, implementations MUST represent these changes by minting a new SWBD (new id/edition) and linking it to the prior one via explicit continuity/withdrawal (WF‑BD‑5 / CC‑BD‑10), rather than mutating the prior record. ... 1. declareBase — create a new base declaration with explicit`dependent`,`base`,`baseRelation`,`scope`, and, when applicable,`Γ_time`, plus witnesses when decision-relevant. 2. withdrawBaseDecl — retire a declaration (or render it inapplicable by scope narrowing or time restriction, depending on baseRelation declaration). 3. rebase — change`base` while keeping the same`dependent` and`baseRelation`(legality depends on the baseRelation declaration; often requires witness refresh). 4. repointDependent — change`dependent` while keeping the same`base` and`baseRelation`. ... 5. rescope — change`scope`(widen/n

## Parallel

### 1. GitHub - briancurtin/deprecation: A library to handle automated deprecations · GitHub
- URL: https://github.com/briancurtin/deprecation
- Query families: alternate_terminology, falsification, source_domain, target_neighbor
- Excerpt: # briancurtin/deprecation - Page: GitHub repository - URL: https://github.com/briancurtin/deprecation - Description: A library to handle automated deprecations - Stars: 95 - Forks: 33 - License: Apache-2.0 license - Default branch: master - Created: 2017-01-12T17:51:51.000Z - Commits: 60 ## Top-level files - docs/ - tests/ - .coveragerc - .gitignore - .travis.yml - LICENSE - MANIFEST.in - README.rst - deprecation.py - docs-requirements.txt - example.py - setup.cfg - setup.py - test-requirements.txt - tox.ini ## README.rst ## deprecation [Documentation Status](http://deprecation.readthedocs.io/en/latest/) [https://travis-ci.org/briancurtin/deprecation.svg?branch=master](https://travis-ci.org/briancurtin/deprecation) The `deprecation` library provides a `deprecated` decorator and a `fail_if_not_removed` decorator for your tests. Together, the two enable the automation of several things: 1.

### 2. kevin-biot/governance-failure-patterns - GitHub
- URL: https://github.com/kevin-biot/governance-failure-patterns
- Published: 2026-04-23
- Query families: alternate_terminology, falsification, source_domain, target_neighbor
- Excerpt: # kevin-biot/governance-failure-patterns - Page: GitHub repository - URL: https://github.com/kevin-biot/governance-failure-patterns - Description: Public incubation repo for governance failure patterns and remediation taxonomy - kevin-biot/governance-failure-patterns - Stars: 0 - Forks: 0 - License: CC-BY-4.0 license - Default branch: main - Created: 2026-04-23T09:27:47.000Z - Commits: 25 ## Top-level files - .github/ISSUE_TEMPLATE/ - anti-patterns/ - case-studies/ - docs/ - evidence/notes/ - patterns/ - reports/templates/ - spec/ - taxonomy/ - templates/ - .gitignore - CHANGELOG.md - CONTRIBUTING.md - LICENSE - PUBLICATION-STANDARD.md - README.md - editorial-policy.md - framework.md ## README.md # Governance Failure Patterns _A public-interest taxonomy and conformance method for recurring governance failures in AI-assisted decision systems, policy tooling, and agentic infrastructure._ T

### 3. Model deprecation is the new continuity risk – Andreas Timm
- URL: https://andreastimm.com/model-deprecation-is-new-continuity-risk/
- Query families: alternate_terminology, falsification, source_domain, target_neighbor
- Excerpt: None of this is hard. It is just unglamorous work that does not get done unless someone owns it. ## The strategic consequence is renewed buy-versus-build math Continuity risk changes the calculus of where to deploy AI capability. For workflows where the cost of unplanned migration is high — regulated workflows, mission-critical operations, customer-facing experiences with high switching costs — the case for either fine-tuning a frontier model into a controlled deployment, partnering with a vendor offering enterprise-grade continuity commitments, or building on open-weight models the enterprise can host indefinitely is stronger than it was in 2024. The case for relying on whichever model is best on a benchmark this quarter is weaker. The math is not simple. Open-weight models lag the frontier, sometimes meaningfully. Self-hosting carries operational cost that the proprietary providers abs

### 4. lifecycle | Semprini/md-ddl Agent Skill | SkillsMP
- URL: https://skillsmp.com/creators/semprini/md-ddl/agents-agent-ontology-skills-lifecycle
- Query families: alternate_terminology, source_domain, target_neighbor
- Excerpt: --- description: Promote domains through lifecycle stages (Draft → Review → Active → Deprecated → Retired) and manage semantic version bumps. Use when the user wants to... title: lifecycle | Semprini/md-ddl Agent Skill | SkillsMP image: https://skillsmp.com/skills/semprini-md-ddl-agents-agent-ontology-skills-lifecycle-skill-md/opengraph-image --- [Skip to main content](#main-content) # lifecycle Promote domains through lifecycle stages (Draft → Review → Active → Deprecated → Retired) and manage semantic version bumps. Use when the user wants to promote a domain, bump its version, deprecate or retire a domain, or generate/update lifecycle history. [Jump to install](#install-skill) ## Source facts Repository Semprini/md-ddl Last source activity July 25, 2026 at 01:49 Detected SKILL.md language English Stars 1 Forks 0 ## Install options The review-first prompt is selected by default. You ca

### 5. 
	Deprecation of old Excel and CSV import experience... - Microsoft Fabric Community

- URL: https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Deprecation-of-old-Excel-and-CSV-import-experience-in-Power-BI/ba-p/5173941
- Published: 2026-02-10
- Query families: falsification, target_neighbor
- Excerpt: * Deprecation of old Excel and CSV import experience... * Back to Blog * Newer Article * Older Article msgracegong Microsoft Employee [msgracegong](https://community.fabric.microsoft.com/t5/user/viewprofilepage/user-id/920949) ‎02-10-2026 08:00 AM ## Deprecation of old Excel and CSV import experience in Power BI Service * [Subscribe to RSS Feed](https://community.fabric.microsoft.com/oxcrx34285/rss/message?board.id=fbc_pbiupdatesblog&message.id=40) * * Mark as New * Mark as Read * * Bookmark * Subscribe * * Printer Friendly Page * Report Inappropriate Content Excel and CSV files remain a valid data source for Power BI semantic models and reports. You can use them to create reports in the Power BI service from the **Create** page or in Power BI Desktop. This blog post is for users who created reports using the old experience to import an Excel or CSV file from the **Create** page in the s

### 6. AI Governance Taxonomy & Reference Glossary
- URL: https://chrishood.com/ai-governance-taxonomy-reference-glossary
- Published: 2026-02-24
- Query families: alternate_terminology, source_domain
- Excerpt: ### The 14 Governance Dimensions _(Nomotic architecture)_ The specific set of dimensions evaluated simultaneously for every consequential action in a Nomotic governance architecture: 1. **Scope Compliance** — Is the action within the agent’s authorized scope? 2. **Authority Verification** — Does the agent have explicit authority for this specific action? 3. **Resource Boundaries** — Are resource limits (rate, concurrency, cost) respected? 4. **Behavioral Consistency** — Does this action match the agent’s established behavioral patterns? 5. **Cascading Impact** — What are the downstream consequences if this action proceeds? 6. **Stakeholder Impact** — Who is affected and how? 7. **Incident Detection** — Does this action match known failure or attack patterns? 8. **Isolation Integrity** — Are containment boundaries between agents or systems maintained? 9. **Temporal Compliance** — Is the t

### 7. AI Lifecycle Ownership Checklist For Governance
- URL: https://aicompetence.org/ai-lifecycle-ownership-checklist-for-governance
- Published: 2026-05-15
- Query families: alternate_terminology, source_domain
- Excerpt: One person may hold more than one role in a smaller organization. That is not the problem. The problem is when the roles are blurred, assumed, or left unenforceable. |Lifecycle Stage |Business/Product Owner |Technical Owner |Risk/Control Owner |Operational Owner |Highest-Risk Failure if Weak |Primary Escalation Trigger | | --- | --- | --- | --- | --- | --- | --- | |Problem framing |High |Medium |High |Low |Use case approved without real boundary control |Rights, safety, compliance, or external-user impact | |Sourcing |Medium |High |High |Low |Vendor or data dependencies accepted without review |Vendor change, provenance gap, contractual constraint | |Design and control definition |Medium |High |High |Medium |Controls exist conceptually but not operationally |Missing safeguards, undefined thresholds, weak evidence | |Pre-deployment sign-off |High |High |High |Medium |Launch approved witho

### 8. Governance Failure and Governance Under Failure: Reviewing ...
- URL: https://journals.sagepub.com/doi/10.1177/01492063231225420
- Published: 2024-07-01
- Query families: falsification, target_neighbor
- Excerpt: Our review of the 112 articles published in management, marketing, operations management, supply chain, public relations, accounting, and finance on the topic (using criteria specified in the appendix ) revealed a range of different theories, concepts, and mechanisms (see Table 1 ) as well as different effects and outcomes for individuals, committees, boards, and firms. In reviewing this literature, we aim to develop a comprehensive and integrated framework that can highlight what is currently known from the work to date, identify gaps that deserve further attention, and provide a road map for future research. We do this in two steps. First, to organize our review, we classify studies focusing on the influences of governance on misconduct (i.e., the board and director antecedents of misconduct) to be studies of _governance failures_ . In contrast, we consider studies on the influences of

### 9. Semantic Diff for Prompts: Why Git Diff Lies About What Your Prompt Change Will Do
- URL: https://tianpan.co/blog/2026-04-23-semantic-diff-prompts-behavioral-impact
- Published: 2026-04-23
- Query families: alternate_terminology, target_neighbor
- Excerpt: A well-known study on prompt perturbations showed that adding a single trailing space to a prompt caused over 500 prediction changes across a benchmark; appending "Thank you" changed hundreds more; requesting a specific output format flipped at least 10% of predictions on every task the authors tested. Rephrasing a question as a statement — a transformation with near-zero semantic content for a human reader — produced over 900 prediction changes. None of these edits look meaningful in a git diff. All of them are meaningful to the model. The reverse failure mode is just as common and less discussed. Large, visually dramatic prompt refactors often do almost nothing to behavior. You split one giant instruction into five bullet points; you move the tool list from the bottom to the top; you rewrite the system prompt in a different voice. The diff is enormous. The eval deltas are within noise.

### 10. Structural Leadership Failure in High-Consequence Systems
- URL: https://www.academia.edu/167936815/Structural_Leadership_Failure_in_High_Consequence_Systems
- Query families: falsification, source_domain
- Excerpt: Through analysis of four Australian case studies — the Optus telecommunications outage, pressures within the childcare sector, the Robodebt administrative failure, and the Qantas governance crisis — the paper demonstrates how structural misalignment frequently precedes visible institutional failure.
