# RESEARCHER INVENTORY V31 CALIBRATION CORRECTION RECORD

Status: ACTIVE CALIBRATION SUCCESSOR EVIDENCE — NOT CERTIFICATION
Date: 2026-09-14
Authority: Leah’s standing Researcher Inventory calibration directive
Predecessor contract: `researcher_inventory/AGENT_CONTRACT_V30.md`
Successor contract: `researcher_inventory/AGENT_CONTRACT_V31.md`
Evidence run: GitHub Actions `34877095967`
Promotion authority: NONE

## Immutable archetype gate

Run `34877095967` verified both Leah-approved workbook copies by SHA-256 before calibration, with no repair:

- `Case_2_Lightweight_Researcher_Inventory.xlsx` = `d47915552fdbdd23adc8c3f66ab06f94e022ab0bfd93faa5faabb53fdf9c9193`
- `Case_6_Lightweight_Researcher_Inventory_v2_with_Verbs_and_Locators.xlsx` = `50d646aad08b33051b93c1f3b3538d59ff78386558473b71a906a94213635070`

The deterministic apparatus unit suite also passed 9/9 tests before semantic calibration.

## Failure classification

V30 failed the diagnostic archetype batch. No current evidence demonstrates a workbook, canonical-extract, or deterministic-harness defect.

Two worker-behavior patterns are generalizable:

1. **Uniform-grain drift.** V30’s global rule to retain the smallest complete source-distinguished semantic coordinate is too uniform across classes. It pushes TIME toward lexical event/action granularity and encourages other class-grain drift. The approved lightweight architecture instead uses different semantic resolution by class: PLACE scene-position, TIME episode/frame, PERSON resolved actor, OBJECT source-treated referent, LABEL characterization increment, VERB lexical relation edge, LOCATOR orienting relation.
2. **Literal span failure.** The oil-change attempt exhausted retries because a returned VERB `source_wording` was not an exact contiguous source substring. The validator behaved as designed. The worker needs an explicit pre-return exact-substring self-check rather than looser paraphrase/repair behavior.

## Corrective principle

V31 therefore:

- replaces V30’s universal minimum-grain rule with class-specific grain rules;
- states explicitly that TIME is coarser than VERB and that consecutive actions inside one stable episode normally share a TIME;
- preserves provisionally distinct source-progressed PLACE scene-position roles even when physical overlap is possible;
- clarifies source-treated choice/relation content for OBJECT without allowing analyst proposition nominalization;
- permits LABEL characterization regardless of grammatical form when the source actually characterizes;
- keeps VERB at exact lexical relation-edge grain with a bounded exception for one source-selected coordinated action package;
- expands LOCATOR clarification for materially orienting accompaniment and recurring/context relations;
- requires exact character-for-character substring verification of every explicit wording/cue/order span before return.

No archetype row, evaluator finding, expected count, prior scored output, case-specific correction example, or sealed holdout content is included in worker-visible V31 instructions.

## Preserved controls

Unchanged:

- immutable workbook hash gate and canonical extracts;
- deterministic evaluator/pass criteria;
- candidate-only/no-promotion state;
- no APA IDs or database admission;
- worker isolation from gold/evaluator/holdout information;
- failure/history preservation;
- repeated Case 2/Case 6 pass requirement under one finalized contract and one calibration lineage;
- exactly-once calibrated-lineage Case 5 holdout gate;
- retirement of that lineage and fresh-agent clean-room Case 5 verification after a first holdout pass.

## Holdout state

At V31 creation, sealed Case 5 remains `NOT DEPLOYED`. No holdout source or output was used to derive V31.

## Historical effect

`PARTIALLY SUPERSEDED — 2026-09-14`

V30 remains historical calibration evidence. V31 controls forward calibration behavior only for the class-resolution and literal-span self-check rules expressly changed in `AGENT_CONTRACT_V31.md`.
