# RESEARCHER INVENTORY V20 CALIBRATION CORRECTION RECORD

Status: CALIBRATION HISTORY / FORWARD CORRECTION RECORD
Date: 2026-09-13
Authority: Leah's standing Researcher Inventory calibration directive
Predecessor calibration contract: `AGENT_CONTRACT_V19.md` / `RI-CONTRACT-V19`
Successor calibration contract: `AGENT_CONTRACT_V20.md` / `RI-CONTRACT-V20`
Primary predecessor failed run: `34787385058`

## Immutable gold gate

Before this correction, run `34787385058` verified both repository archetype workbooks before and after the integrity gate with no repair:

- `Case_2_Lightweight_Researcher_Inventory.xlsx` = `d47915552fdbdd23adc8c3f66ab06f94e022ab0bfd93faa5faabb53fdf9c9193`
- `Case_6_Lightweight_Researcher_Inventory_v2_with_Verbs_and_Locators.xlsx` = `50d646aad08b33051b93c1f3b3538d59ff78386558473b71a906a94213635070`

No gold workbook, canonical extract, evaluator expected count, or sealed holdout object is changed by V20.

## Preserved predecessor evidence

The complete V19 attempt remains preserved at:

`calibration_history/researcher_inventory/34787385058/`

Its status remains failed. The holdout stages were skipped. No sealed Case 5 source or output was used for this correction.

## Defect separation

V20 separates two defects demonstrated by the V19 run.

### A. Evaluator alignment defect — harness only

The V19 output included already-correct semantic coordinates whose source-near wording differed from editor shorthand or inflection in the hidden canonical extract. The evaluator then reported the same semantic coordinate as both missing and extra. Examples include an actual waiting-position coordinate and an attendant-walk-away temporal coordinate.

That is a harness-alignment defect, not evidence that the worker must learn hidden editor wording.

V20 therefore adds an **evaluator-only** alignment repair in `v20_calibration_runner.py`:

- normalize common `-ing` inflection for comparison;
- permit strong content-token overlap between source-near tags and editor shorthand;
- permit bounded evidence-token alignment for unnamed PLACE descriptions when both sides are explicitly unnamed;
- preserve the existing ambiguity margin so weak collisions remain unmatched.

This repair is never imported into worker instructions and does not alter gold rows, expected counts, or pass criteria.

### B. Worker over-resolution defect — durable instruction

The V19 worker contract made the represented-situation spine too generative. The worker repeatedly created rows because a situation could be described spatially, temporally, propositionally, verbally, or figuratively, even when the row did not perform an independent class job.

The repeated excess pattern is generalizable:

- PLACE expanded into hypothetical, recurring, mental, or predicate-derived positions;
- TIME could be minted from represented hypothetical actions rather than distinct frames;
- LABEL often retained full question/clause scaffolding instead of the characterization itself;
- VERB split or retained copular/state scaffolding whose only job was carrying a LABEL;
- LOCATOR treated state metaphors as locating relations;
- compounds inherited broad scene/frame coordinates merely because they were globally true.

V20 replaces the generative situation-spine pressure with one positive-job gate:

> A row exists only because it performs one positive job for its own class. Do less. If a marginal row has no clear independent class job, omit it.

The class rules then define the positive job mechanically:

- PLACE = where job for actual represented occurrence/entity/destination, including unnamed actual occurrence-position;
- TIME = episode/span/frame job without requiring clock/date;
- PERSON = human actor/group job;
- OBJECT = independently selectable referent job;
- LABEL = characterization itself, stripped of irrelevant clause/question/copular scaffolding;
- VERB = shortest complete material lexical action/relation, excluding state scaffolding whose only job is LABEL;
- LOCATOR = independent locating/context relation, excluding quality-only spatial metaphors.

Compounds now prohibit automatic inheritance of every broad scene/place/time/locator and include only units that materially participate in the proposition.

These are domain-general rules. No case-specific phrase, gold row, expected count, evaluator finding, or sealed holdout content is placed in worker-visible instructions.

## Holdout boundary

Case 5 remains sealed. V20 must pass the immutable Case 2 and Case 6 archetypes repeatedly under the same finalized V20 contract and saved-agent lineage before the calibrated-lineage holdout is allowed to run exactly once.

If that holdout passes, the calibrated lineage must be retired and a brand-new saved agent created from finalized V20 durable instructions only for a new-session clean-room Case 5 verification.

## Candidate-only boundary

All calibration outputs remain candidate/test material. V20 creates no APA identity, grants no promotion authority, and authorizes no Oval Office research write.

## Forward state

`RI-CONTRACT-V20` is authorized for calibration only. Certification remains contingent on repeated archetype passes, one calibrated-lineage sealed holdout pass, retirement, and fresh-agent clean-room holdout success.
