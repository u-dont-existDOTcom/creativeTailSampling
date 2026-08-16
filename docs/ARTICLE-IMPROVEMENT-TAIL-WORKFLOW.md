# Article-Improvement Creative Tail Workflow

Status: reusable architecture for applying Creative Tail Sampling to an existing article.

## Purpose

Use Creative Tail Sampling to improve an existing article without confusing three different outputs:

1. a genuinely original proposition;
2. a known but missing practical improvement;
3. a correction to an internal contradiction, overclaim, category mistake, or safety gap.

An article can improve substantially even when the strict originality ledger remains empty.

## One-run architecture

### 1. Freeze the source

Record the source filename, SHA-256, line/word/byte counts, and whether editing is authorized. Never silently edit while the discovery audit is still running.

### 2. Build the active-article corpus map

Extract the article's existing claims, rules, warnings, examples, distinctions, and unresolved tensions. Treat this map as the first collision corpus. A candidate already present or substantially implied is not a new addition.

### 3. Generate at least 12 plain candidates without retrieval

Generate propositions from orthogonal source families. Strip rhetoric before evaluation. Include candidates that could challenge the article's own organizing assumptions.

### 4. Run separate gates

- **Internal collision:** already present or implied?
- **Common-sense / named-theory compression:** familiar root?
- **Argument-integrity check:** does it contradict, qualify, or expose an unsupported generalization?
- **Category check:** are experiential depth, intensity, access, integration, efficacy, and durability being kept distinct rather than substituted for one another?
- **Safety / epistemic check:** could the current wording encourage coercion, false certainty, dependency, or functional deterioration?
- **External collision:** mandatory Exa semantic search for serious candidates.
- **Independent falsification:** mandatory Parallel Task attack before strict promotion.

### 5. Smoke-test retrieval execution, not schema visibility

At the start of a fresh run where Exa or Parallel Task availability is uncertain:

1. actually invoke `exa_mcp_search.web_search_exa` on a small real query and verify a substantive result is returned;
2. actually invoke `Parallels_Task_MCP.createDeepResearch` on a narrow falsification query and verify a task/run identifier or result is returned;
3. if the user has instructed continuation, use `getStatus` / `getResultMarkdown` as needed rather than assuming task creation equals task completion;
4. do not substitute ordinary web search for a failed mandatory provider and do not promote a strict survivor while either mandatory lane is unexecuted.

Visible MCP schemas are not proof that the provider actually executes.

### 6. Maintain two ledgers

- **Strict novelty ledger:** only candidates that pass the repo's full Exa and Parallel Task gates.
- **Practical improvement ledger:** useful known mechanisms, operationalizations, corrections, and safeguards.

Never promote practical value into originality merely to produce a survivor.

### 7. For each retained improvement, specify

- exact placement in the article;
- what the article already owns;
- the additive residual;
- whether it strengthens, qualifies, or directly challenges the current argument;
- evidence status;
- an insertion architecture, not a silent rewrite.

### 8. Outcome tracking without premature model rejection

For therapeutic/self-help frameworks, measure prospective outcomes and adverse signals, but do not collapse `no improvement yet` into `the underlying therapeutic target is wrong for this person`.

When results are absent or poor, distinguish at least:

1. misunderstanding or incorrect use;
2. insufficient dose, duration, sequencing, or repetition;
3. missing prerequisite support/regulation;
4. a particular technique or delivery format that does not fit;
5. a protocol that needs additional nuance or updating;
6. an adjunct or different modality needed for a current obstacle;
7. evidence that challenges the broader mechanism or target itself.

These are different hypotheses and should be discriminated rather than treated as one stop/switch rule.

### 9. Keep experiential depth separate from integration

Do not redefine `depth of experience` as integration or therapeutic outcome. In the inner-child article, experiential depth refers to how deeply/richly the experience reaches the material and may involve access and/or intensity, commonly both. Integration is a separate downstream dimension: what becomes incorporated into ordinary functioning, understanding, behavior, and choice.

A deep experience can be poorly integrated. A less intense experience can still integrate well. Neither distinction by itself determines clinical efficacy.

### 10. Keep internalization separate from self-sufficiency

In reparenting work, `receive care → observe care → participate → initiate → internalize` is a developmental sequence for acquiring the internal caregiving function. The fact that healthy adults may continue to rely on chosen relationships, therapy, community, or practical support does not remove the requirement to internalize the reparenting capacity itself.

Therefore distinguish:

- **internalization of the adult/reparenting function**, which is central to the method;
- **ongoing external interdependence**, which can remain compatible with adulthood;
- **authority dependency**, which is a separate risk and should not be confused with either.

### 11. Preserve modal claims accurately

Do not silently weaken `may` claims into claims about present experience only. If an article says a felt sense **may** know something the conditioned self was trained to forget, preserve that epistemic possibility unless evidence directly falsifies it. Historical-certainty safeguards can coexist with the modal claim; they are not substitutes for it.

### 12. Preserve source integrity

Do not edit the article until the ledger is reviewed or the user explicitly asks to proceed. When editing begins, preserve the author's arguments; any disagreement must remain visible as an argument, not a silent softening.

## Persistence outputs

Every run should produce:

- `analysis/<target>/source-fingerprint-batch-NNN.txt`;
- `analysis/<target>/candidate-ledger-batch-NNN.csv`;
- `analysis/<target>/IMPROVEMENT-LEDGER-BATCH-NNN.md`;
- `runs/YYYY-MM-DD-<target>-tail-batch-NNN.md`;
- a lane-specific fresh-conversation handoff when the run establishes reusable corrections or tool constraints;
- `STATE.md` checkpoint where the global project state materially changes;
- `FINDINGS.md` only for strict survivors or important explicit non-promotion records.
