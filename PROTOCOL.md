# Creative Tail Sampling Protocol

Status: canonical working protocol, recovered 2026-08-15 and tightened after repeated false-positive novelty failures. Claim-integrity rules added 2026-09-28.

## Purpose

Use deliberate tail sampling to search for propositions or **cross-domain transfers** that are genuinely non-obvious, useful, coherent, and consequential. The goal is not unusual wording or random novelty. It is to find ideas that remain interesting after being stated plainly **and after comparison with existing project findings and intellectual traditions**.

The method is designed to resist the model's tendency to collapse back toward familiar, high-probability ideas and then mistake elaboration for discovery.

## Core procedure

### 1. Define the concept / search domain

Start from the concept or problem under investigation. Do not prematurely narrow the search to conventional framings.

### 2. Sample the tail rather than the mode

Generate multiple distinct candidate propositions from the low-probability tail of the idea distribution.

- tail-sample **at least 12 plain propositions** before selecting;
- optimize for unusual *propositions*, not unusual language;
- reject incoherent randomness: low probability is necessary but not sufficient;
- do not average candidates together toward consensus.

### 3. Strip style before judging novelty

Rewrite each candidate as a plain modal proposition: what, exactly, is being claimed about the world?

Remove metaphors, new labels, rhetorical intensity, unusual vocabulary, and examples that are more interesting than the proposition they illustrate.

A candidate only counts as novel if it remains interesting in boring language.

### 4. Common-sense compression adversary

Try aggressively to compress the proposition into:

- common sense;
- a familiar aphorism;
- a standard textbook idea;
- a trivial consequence of something already accepted;
- an ordinary mechanism with new terminology.

If this succeeds, reject the candidate.

### 5. Active-project corpus collision gate — MANDATORY BEFORE EXTERNAL NOVELTY SEARCH

When Creative Tail Sampling is being used to extend an existing research project, **the project's own authoritative findings must be checked before any candidate can be promoted**.

For `u-dont-existDOTcom/communities`, the authoritative read order is:

1. `recovered/COMMUNITIES-FINAL-SYNTHESIS-REPORT.md` — horizontal synthesis of all promoted findings;
2. `recovered/COMMUNITIES-SYNTHESIS-CROSSWALK.csv` — finding-to-theme/synthesis mapping;
3. `recovered/COMMUNITIES-EVIDENCE-LEDGER.csv` — source-level factual authority, limits, alternatives, outcomes and verification needs;
4. `recovered/COMMUNITIES-RESEARCH-STATE.md` — completed scope, boundaries and current evidence picture;
5. `COMMUNITY-DEVELOPMENT-LESSONS.md` plus later tail supplements — practical ideas already preserved even where originality failed.

Before promotion ask:

> Is this candidate already explicitly present, substantially implied, or already operationalized anywhere in the project's completed evidence/synthesis/lessons?

Disposition rules:

- **Direct collision:** demote immediately. It is not a new tail finding.
- **Root collision + narrower additive mechanism:** preserve only the narrower residual and state exactly what the corpus already owned.
- **Corroboration only:** record as corroboration; do not create a new finding number.
- **New practical operationalization but no new empirical finding:** add to the project's lessons layer, not the originality ledger.
- **Materially additive candidate:** only then proceed to external literature novelty screening.

For community-related work, **a candidate may not be promoted merely because no external paper was found if the 198-finding corpus already contains it under different wording**.

This gate must be re-run against the latest branch/head because parallel research can advance while tail sampling continues.

**Absence claims cover only what was searched.** A materially additive disposition, or any statement that a corpus, article, or conversation does not contain something, is a claim about absence. Before making it, search all of that material for counterexamples, including other wording for the same mechanism. The claim covers only what was searched: record the version searched (branch/head or source fingerprint) and the files or rows checked, and say so when the search covered less than all of it. Saying the user never raised, accepted, or rejected something is also an absence claim; search the whole conversation and the saved records first, and say so if part of either was unavailable.

### 6. Historical / literature compression gate — MANDATORY BEFORE PROMOTION

A proposition that survives the project's own corpus and the model's familiarity test can still be an old idea the model has merely failed to retrieve.

Before labeling anything a finding, deliberately ask:

> Is this substantially contained in an existing intellectual tradition, named theory, research program, or classic thinker, even if the vocabulary differs?

For social/community questions, the default collision set includes at minimum:

- Marx: alienation, commodity relations/fetishism, division of labor/class relations;
- Durkheim: mechanical/organic solidarity and division of labor;
- Tönnies: Gemeinschaft/Gesellschaft;
- Weber: rationalization/bureaucracy;
- Polanyi: embedded/disembedded economies;
- Simmel: metropolitan life, money, social differentiation;
- Granovetter/social-network traditions: embeddedness, weak ties, network structure;
- Bourdieu/social-capital traditions;
- Goffman/role and presentation traditions;
- Ostrom/collective-action and institutional-design traditions;
- organizational ecology, institutional economics, game theory, network science, cultural evolution, and diffusion-of-innovation literatures where relevant.

This is not an exhaustive canon. Search broader when the candidate points elsewhere.

**Same-domain rediscovery rule:** if a competent reader of the *target-domain* literature could reasonably say "this is basically X," the candidate is **not a creative-tail finding**. At most, preserve a distinctive operationalization as derivative material.

**Cross-domain transfer exception:** Creative Tail Sampling is partly a search for surprising connections between knowledge domains. A mechanism may be well known in a source domain and still survive if:

1. the transfer into the target domain is not already standard;
2. the mapping is structural rather than metaphorical decoration;
3. it generates a distinctive prediction, measurement, or design rule that the target-domain framing would not obviously supply;
4. targeted search does not reveal that substantially the same transfer is already established;
5. the active project's own corpus/lessons do not already contain substantially the same transfer.

Label such results **CROSS-DOMAIN CONNECTION**, not "new theory."

When novelty matters, perform a targeted literature/web search for candidate survivors before promotion. Failure to find a precedent is not proof of originality; it merely clears one rejection gate.

**Collision claims are factual claims.** Saying that a tradition, theory, field, standard, or classification contains, includes, or excludes a mechanism (`this is basically X`) is a factual claim about X. Check it against a source, or record that it comes from memory. A from-memory collision can still reject or narrow a candidate; the label shows later readers which collisions were checked against a source. When the user has stated expertise in the area, find a source before contradicting the user's usage.

#### Retrieval ensemble architecture — benchmark-validated 2026-08-16

Round 001 retrospectively tested Exa Search, Parallel Search, and Parallel Task against frozen historical false-novelty/narrowing cases. The validated external retrieval sequence is now:

1. **Do not retrieve during tail generation.** Keep creative recall low; web/literature retrieval begins only after a candidate survives the common-sense and active-project gates.
2. **Exa semantic collision attack — mandatory routine lane.** Search independently across at least these query families before strict promotion:
   - closest target-domain neighbor;
   - alternate terminology / older vocabulary;
   - source-domain mechanism plus evidence of transfer into the target domain;
   - explicit falsification / strongest predecessor attack.
3. **Adjudicate evidence rather than search snippets.** Fetch/read primary or full sources when the collision judgment depends on them. A retrieved URL is not itself a collision.
4. **Parallel Search — optional corroboration/disagreement lane.** It may be used for cheap independent retrieval, but Round 001 did not justify making shallow Parallel Search mandatory: Exa caught all 8/8 historical positive cases while Parallel Search caught 2/8 conservatively (3/8 under sensitivity scoring), and the routine union added no recall over Exa.
5. **Parallel Task deep research — mandatory survivor escalation before strict originality promotion.** If a candidate would still enter the strict originality ledger after routine Exa adjudication, run an independent deep nearest-neighbor/falsification attack. Do not feed it Exa's discovered precedents or evaluator labels; preserve retrieval independence. Do not spend deep research on candidates already rejected or narrowed below promotion threshold.
6. **Promote only the surviving residual.** If retrieval finds a familiar root but not the whole mechanism, rewrite the candidate to the narrow residual actually left. If no residual remains, demote it. A provider returning nothing is `no collision found`, never proof of originality.

The benchmark's canonical report is `runs/2026-08-16-retrieval-ensemble-round-001-final.md`; raw evidence and deep reports are under `analysis/retrieval_ensemble/results/round-001/`.

#### Claims about sources, quotations, and figures

These rules cover every source the method handles: retrieved literature, the project corpus, an article under review, and the user's own words.

- **Anchor each claim about a source.** Every sentence that says what a source, author, corpus file, or the user says, writes, describes, presents, defines, or did must rest on a specific passage that can be cited. That includes words of scope, frequency, persistence, or consent, such as everyone, never, always, kept, stopped, many, willing, and forced. A source read earlier in the session still has to be checked when the sentence is written. If no passage supports the sentence, label it as an interpretation ("I read this as ...") or cut it. Never phrase an inference as the source's content, and never add backstory, motives, or history that a person did not state.
- **Quotation marks mean exact words.** Put only a source's exact words inside quotation marks. Mark translations as translations. Do not join words from separate sentences inside one quotation, and do not put a paraphrase in quotation marks.
- **Trace figures to the primary source.** Before a number, percentage, or superlative goes into a finding, a verdict, or text someone will publish, open the source cited for it. For a figure computed in this repository, that source is the data file and the script that produced it. If a secondary figure does not match its own citation, use the primary figure. Two figures that trace to one source are one finding, not two. Say when the only available source is weak.

### 7. User familiarity veto

If the user immediately recognizes the proposition as common sense or a familiar theory, demote it regardless of whether the formulation appears technically sharper.

Do not defend a failed novelty claim by explaining why the restatement is more precise. Precision can make an old idea useful; it does not make it new.

Record the failure as a stronger boundary for subsequent sampling.

**Recheck before conceding, as before defending.** When the user disputes a factual claim, such as what a source says or what a figure is, check the source before agreeing, just as before defending the claim. Agreement is not verification. Do not swing to the opposite claim; say what the source supports, which may be both readings. The familiarity veto above needs no source check, because non-obviousness to the user is itself a promotion condition; when a veto names a specific theory or precedent, record that as the user's identification unless it has been checked. When the user corrects how a reply or record restates the user's own argument, go back to the user's words; do not defend the earlier restatement, and do not adopt a new one the user did not state.

### 8. Coherence / realism gate

Reject candidates that only work because of unrealistic forced choices, artificial institutional constraints, or scenarios that real people can trivially escape.

Preserve realistic options such as rejecting all proposals, retaining the status quo, abstaining/refusing agreement, or leaving where exit is genuinely available.

Do not manufacture a paradox by deleting ordinary options.

### 9. Consequence expansion

For every promising proposition, derive consequences at least **three inferential steps** beyond the initial observation.

Ask:

- If this is true, what else must tend to be true?
- What variable does it change that conventional models treat as independent?
- What apparently separate phenomena could it unify?
- What design rule follows?
- What counterintuitive prediction follows?
- What observation would distinguish it from the familiar alternative?

A proposition that produces no non-obvious downstream consequences is weak even if superficially novel.

**Important:** several non-obvious-looking consequences of an old root theory do not automatically constitute a new root finding. Apply both the project-corpus and literature compression gates again to the derived mechanism.

### 10. Evaluation dimensions

Evaluate candidates on at least:

- **project novelty** — materially additive to the authoritative active-project corpus;
- **originality** — survives plain restatement and target-domain literature compression;
- **connection novelty** — for transfers, the cross-domain mapping is not already standard;
- **insight** — reveals structure not captured by the familiar target framing;
- **coherence** — no hidden contradictions or contrived assumptions;
- **fitness** — relevant to the problem being explored;
- **consequence** — generates downstream predictions/design implications;
- **testability** — evidence could discriminate it from alternatives;
- **distance from the rejection frontier** — not merely one inferential step beyond something already rejected.

### 11. Selection rule

Do not blend mediocre candidates into a safe synthesis. Select the strongest candidate that survives all gates and develop it deeply.

If none survive, say **none survived** and generate another tail batch. Never lower the novelty standard in order to have a result.

### 12. Stop condition for a local discovery

A candidate becomes a serious finding only when it is:

1. genuinely non-obvious to the user;
2. materially additive to the active project's authoritative corpus;
3. not substantially contained in an existing target-domain named theory/tradition;
4. if cross-domain, a nonstandard structural transfer with distinctive consequences;
5. consequential;
6. coherent;
7. testable or at least discriminable in principle;
8. sufficiently far from the established rejection frontier that it is not merely an ornate restatement.

Then treat it as the new search seed and tail-sample its implications.

## Anti-elaboration rule

Once a root branch is identified as familiar **or already owned by the active project corpus**, stop elaborating that branch for novelty. Do not generate increasingly technical mechanisms around it and promote them as discoveries simply because the wording becomes less familiar.

Either:

- preserve a genuinely useful operationalization in the practical lessons layer;
- use the known result explicitly as background for a genuinely orthogonal jump; or
- leave the branch entirely and sample a new region.

This rule was originally added after the multiplex/relational-unbundling branch kept producing increasingly formal versions of ideas already adjacent to Marx, Durkheim, Tönnies, Polanyi, social-capital theory, and multiplex-network research. It now also covers rediscovery of the project's own evidence base.

## Interaction rules learned from the session

- Do not stop after finding something merely correct.
- Do not present rediscovered influencers, bargaining power, specialization, commodification, alienation, embeddedness, social capital, or other familiar concepts as major discoveries.
- Do not re-discover a project's own completed findings and award them new tail IDs.
- User objections are search information. Record *why* a candidate failed and move the frontier beyond it.
- Apparent paradoxes are suspect; first check whether an option, variable, or degree of freedom was silently removed.
- Continue automatically onto the next inferential step unless a genuinely human-only ambiguity blocks progress.

## Persistence rule

Every substantive session should update:

1. `FINDINGS.md` with genuine survivors and important rejections;
2. `STATE.md` with the current frontier and exact next move;
3. a detailed `runs/` audit for each tail batch;
4. the target project's practical lessons layer for useful community-development ideas even when novelty fails.

The repository, not chat history, is the durable source of truth.

When writing these records, and in replies:

- **Say exactly what was checked.** A record or reply that says a candidate passed a gate, or that something was verified, checks out, or matches, must name what was compared against which source or version, such as the corpus branch/head searched or the query families actually run. If only part was checked, name the part. Before calling a quotation right or wrong, find the version the author used. Describe edits to records, articles, or this protocol exactly: text that was deleted or replaced was not "fixed".
- **Keep claims consistent and label estimates.** Before sending a reply or writing a record, compare it with what was already said on the same candidate or topic, in the conversation, in `FINDINGS.md` and `STATE.md`, and in any lane state or handoff file for the same work. If they conflict, correct one and say so. Label estimates as estimates, and report a derived number at the resolution of its inputs; for example, a time computed from minute-level timestamps is a range.

**Experimental: key-condition check on written verdicts.** For a written verdict (a gate disposition, a promotion or demotion, a `FINDINGS.md` entry, or an evidence summary), a separate checker, such as another agent or a fresh context, reads only the verdict text and names the key conditions it answers: the sources it rests on, including the corpus version; the disposition axis (strict originality or practical usefulness, which this protocol keeps separate); the target domain, or for an empirical finding the population and outcome measure; and the scope, meaning which residual was judged and how far the search went. If the checker cannot name them, or names different ones from those the verdict was meant to answer, the verdict is vague or blends conditions; revise it. This adapts ProCo (Wu et al., EMNLP 2024, https://aclanthology.org/2024.emnlp-main.714/). That paper tested open-domain question-answering, arithmetic, and commonsense reasoning problems that were generally short, averaging 52.3 words, with answers that were typically numbers or entities; it leaves longer problems and other answer types to future research. Long written verdicts are outside what it tested, so this check never blocks promotion, demotion, or delivery; record its hits and misses in the run audit. Never apply it to conversational or therapeutic replies.
