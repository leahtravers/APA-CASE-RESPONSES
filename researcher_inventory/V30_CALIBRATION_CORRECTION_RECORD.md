# RESEARCHER INVENTORY V30 CALIBRATION CORRECTION RECORD

Status: ACTIVE CALIBRATION SUCCESSOR EVIDENCE — NOT CERTIFICATION
Date: 2026-09-14
Authority: Leah’s standing Researcher Inventory calibration directive
Predecessor contract: `researcher_inventory/AGENT_CONTRACT_V29.md`
Successor contract: `researcher_inventory/AGENT_CONTRACT_V30.md`
Evidence run: GitHub Actions `34873681060`
Promotion authority: NONE

## Immutable archetype gate

Run `34873681060` verified the repository copies of both Leah-approved gold-standard workbooks by direct SHA-256 over workbook bytes before semantic calibration:

- `Case_2_Lightweight_Researcher_Inventory.xlsx` = `d47915552fdbdd23adc8c3f66ab06f94e022ab0bfd93faa5faabb53fdf9c9193`
- `Case_6_Lightweight_Researcher_Inventory_v2_with_Verbs_and_Locators.xlsx` = `50d646aad08b33051b93c1f3b3538d59ff78386558473b71a906a94213635070`

`repaired` was empty. The gold inputs therefore did not require repair in that run.

## Failure classification

The V29 workflow completed with `failure` during archetype calibration. The deterministic evaluator remained hash-gated and compared worker output to the unchanged canonical extracts. No current evidence demonstrates a harness/gold defect.

The V29 outputs show a generalizable grain error in both directions:

- legitimate small source-distinguished coordinates are omitted when they are nested inside larger story propositions;
- broader proposition-sized OBJECT/TIME/LABEL substitutes are introduced;
- distinct lexical relation edges are collapsed into broad predicate families while other grammar-derived rows are still over-produced;
- compounds then inherit the wrong unit grain and diverge extensively.

This pattern appears across both calibration archetypes and therefore supports a durable contract correction rather than a case-specific instruction.

## Corrective principle

V30 replaces V29’s whole-story independent-role test with the rule:

> Retain the smallest complete source-distinguished semantic coordinate that performs a real positive function of the requested class; exclude only material that exists as grammatical debris, unsupported reification, inference, alias duplication, or a fragment with no separate semantic job.

For VERB specifically, V30 restores **minimal relation-edge** resolution instead of broad predicate-family resolution, while still prohibiting bare auxiliary/support fragments.

V30 also tightens OBJECT against proposition nominalization and clarifies source-established unnamed PLACE/TIME, source-applied LABEL, and orienting LOCATOR functions.

## Preserved controls

Unchanged:

- immutable Case 2/Case 6 workbooks and hash gate;
- evaluator/canonical extracts and pass criteria;
- exact lexical/source-posture preservation requirement;
- calibration worker isolation from archetypes, evaluator findings, expected counts, prior scored outputs, and holdout content;
- candidate-only/no-promotion state;
- no APA ID creation;
- failure/history preservation;
- repeated Case 2/Case 6 pass requirement under one finalized contract;
- exactly-once calibrated-lineage Case 5 holdout gate;
- retirement and fresh-agent clean-room Case 5 verification after a first holdout pass.

## Holdout state

At V30 creation, sealed Case 5 remains `NOT DEPLOYED`. No holdout source or output was used to derive V30.

## Historical effect

`PARTIALLY SUPERSEDED — 2026-09-14`

V29 remains historical calibration evidence. V30 controls forward calibration behavior only for the semantic-coordinate/grain rules expressly changed in `AGENT_CONTRACT_V30.md`.
