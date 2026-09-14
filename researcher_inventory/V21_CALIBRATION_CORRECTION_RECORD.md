# RESEARCHER INVENTORY V21 CALIBRATION CORRECTION RECORD

Status: CALIBRATION HISTORY / FORWARD CORRECTION RECORD
Date: 2026-09-13
Authority: Leah's standing Researcher Inventory calibration directive
Predecessor calibration contract: `AGENT_CONTRACT_V20.md` / `RI-CONTRACT-V20`
Successor calibration contract: `AGENT_CONTRACT_V21.md` / `RI-CONTRACT-V21`
Primary predecessor failed run: `34791080786`

## Immutable gold gate

Run `34791080786` verified both repository archetype workbooks before calibration with no repair:

- `Case_2_Lightweight_Researcher_Inventory.xlsx` = `d47915552fdbdd23adc8c3f66ab06f94e022ab0bfd93faa5faabb53fdf9c9193`
- `Case_6_Lightweight_Researcher_Inventory_v2_with_Verbs_and_Locators.xlsx` = `50d646aad08b33051b93c1f3b3538d59ff78386558473b71a906a94213635070`

No gold workbook, canonical extract, evaluator expected count, or sealed holdout object is changed by V21.

## Preserved predecessor evidence

The complete V20 attempt remains preserved at:

`calibration_history/researcher_inventory/34791080786/`

Its status remains failed. The holdout stages were skipped. No sealed Case 5 source or output was used for this correction.

## Defect separation

### Harness state

The V20 workflow passed:

- immutable workbook SHA verification;
- deterministic apparatus tests;
- source-copy/mechanical validation;
- durable failure-history preservation.

V20's evaluator-only alignment repair remains useful: it prevents source-near inflection/editor-shorthand differences from being misreported as semantic absence while retaining class-bounded matching and ambiguity margins. The latest run did not demonstrate a new reason to weaken gold criteria or expose hidden editor wording to the worker.

Therefore V21 does **not** change the hidden archetypes, canonical extracts, expected counts, or scoring criteria. Its calibration runner reuses the V20 evaluator-alignment layer unchanged.

### Worker-behavior defect

V20 corrected V19 over-resolution by introducing a global positive-job/minimality pressure. The latest run shows that this pressure overshot. The worker repeatedly omitted materially represented local coordinates because they looked marginal, overlapped another class, or were already represented by a broader frame.

The recurrent under-resolution is generalizable across the seven-class architecture:

- PLACE lost unnamed positions of distinct waits, movements/destinations, later conversations, and other materially distinct situations;
- TIME collapsed distinct subepisodes and omitted intended, recurring, or prospective frames;
- OBJECT lost choices, decisions, internal objects, and recurring relations treated as independently selectable referents;
- LABEL omitted material source-applied characterizations when similar wording also functioned as action, location, or state;
- VERB over-merged nested/embedded relations because it optimized for one lexical chunk rather than distinct material relation edges;
- LOCATOR omitted movement, destination, recurring-context, and other locating relations when related semantics were already carried elsewhere;
- compound construction then inherited the unit omissions and also became too reluctant to carry the local PLACE/TIME/LOCATOR frame governing nearby propositions.

The failure is not a request for exhaustive grammar extraction. V19 demonstrated the opposite risk: a broad represented-situation spine could create rows merely because a situation was describable from another angle. V21 therefore restores coverage without restoring generative over-resolution.

## V21 correction

V21 replaces the scalar minimality pressure with **class-local coordinate closure**.

Controlling rule:

> Discover the complete set of materially represented coordinates for the requested class first. Then prune only same-class aliases, true duplicates, grammar debris, and invented rows. Do not prune a coordinate merely because another class carries related meaning or because the coordinate is local to only one episode/proposition.

Class-local consequences:

- PLACE admits explicit and unnamed situation positions, origins/destinations, later-report/conversation positions, and present telling when materially distinct, while rejecting hypothetical-only, generic-recurrence, and state-metaphor pseudo-places;
- TIME admits distinct episodes/subepisodes, spans, transitions, intended periods, recurrences, reflections, and prospective frames without minting a row per verb or clause;
- PERSON remains actor/participant based with alias/coreference resolution;
- OBJECT explicitly includes choices, decisions, recurring relations, and internal/figurative referents when independently selectable, while still rejecting noun-phrase/proposition exhaustiveness;
- LABEL preserves the complete source characterization including polarity/negation when semantically material and allows legitimate overlap with other classes;
- VERB uses material **relation-edge** grain: nested or embedded relations are separate only when each connects materially represented coordinates; bare grammatical support remains excluded;
- LOCATOR permits legitimate overlap with VERB/LABEL when the same phrase independently performs a locating/context job;
- compounds inherit the specific local frame that is materially in force for the proposition, but frame inheritance stops at real discourse/frame transitions and never becomes global propagation.

These are domain-general rules. No case-specific phrase, hidden gold row, expected count, evaluator finding, scored output, or sealed holdout content appears in worker-visible V21 instructions.

## Holdout boundary

Case 5 remains sealed. V21 must pass the immutable Case 2 and Case 6 archetypes repeatedly under the same finalized V21 contract and saved-agent lineage before the calibrated-lineage holdout is allowed to run exactly once.

If that holdout passes, the calibrated lineage must be retired and a brand-new saved agent created from finalized V21 durable instructions only for a new-session clean-room Case 5 verification.

## Candidate-only boundary

All calibration outputs remain candidate/test material. V21 creates no APA identity, grants no promotion authority, and authorizes no Oval Office research write.

## Forward state

`RI-CONTRACT-V21` is authorized for calibration only. Certification remains contingent on repeated archetype passes, one calibrated-lineage sealed holdout pass, retirement, and fresh-agent clean-room holdout success.
