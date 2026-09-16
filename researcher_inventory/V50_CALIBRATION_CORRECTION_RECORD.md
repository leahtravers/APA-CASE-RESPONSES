# V50 CALIBRATION CORRECTION RECORD

Status: `PROSPECTIVE SUCCESSOR CORRECTION`
Date: 2026-09-15
Predecessor: `RI-CONTRACT-V49`
Successor: `RI-CONTRACT-V50`
Authority: Leah's standing Researcher Inventory calibration directive
Registrar record: `APA-EXEC-CASES-RI-CAL-V50-20260915-2343`

## Evidence basis

Latest preserved V49 calibration evidence: workflow run `35052099982`, stored under `calibration_history/researcher_inventory/35052099982/` and preserved by commit `310f7799d55827263accf0dc1857f0fc5da4066c`.

The immutable-workbook gate verified the repository copies of Leah-approved Case 2 and Case 6 workbooks against the required SHA-256 values:

- `Case_2_Lightweight_Researcher_Inventory.xlsx` = `d47915552fdbdd23adc8c3f66ab06f94e022ab0bfd93faa5faabb53fdf9c9193`
- `Case_6_Lightweight_Researcher_Inventory_v2_with_Verbs_and_Locators.xlsx` = `50d646aad08b33051b93c1f3b3538d59ff78386558473b71a906a94213635070`

`archetype_integrity.json` records `status: VERIFIED` and `repaired: []`. The deterministic source/literal/reference checks passed. Hidden semantic calibration failed on both archetypes. The sealed holdout was not attempted and remains unavailable to calibration.

## Defect classification

`AGENT-BEHAVIOR / GENERALIZABLE DURABLE RESOLUTION DEFECT`

The evidence does not show a corrupted workbook, harness translation defect, source-span validator defect, or holdout leak. V49's semantic correction over-expanded the selection grain. Across both archetypes it admitted many physical/location words, temporal cues, concrete/discourse nouns, clause-sized predicate spans, and orientation phrases as independent units while still omitting supported scene/episode and relation coordinates. Those unit-layer mismatches cascaded into compound mismatches.

The cross-case failure demonstrates a generalizable rule error: **coverage cannot be obtained by atomizing every source-presented semantic component.** A child span is entitled to a unit only when it independently satisfies the class-native research-coordinate gate; a larger and smaller span may both survive only when they perform genuinely distinct research roles.

## V50 correction

V50 therefore:

- restores the class-native research-coordinate admission gate and excess controls from the V48 line;
- keeps the whole-source coverage map only as an omission/duplicate detector, never as an entitlement list;
- adds an explicit `coverage without atomization` two-gate rule;
- prefers represented scenes/occurrence positions over literal locative words for PLACE;
- keeps TIME at independently selectable episode/period grain rather than action/cue grain;
- keeps OBJECT referent-based and rejects proposition/discourse/noun-census inflation;
- keeps LABEL characterization-value based and rejects predicate/modifier duplication;
- restores the shortest complete lexical predicate kernel for VERB while retaining required particles/reflexives/complements needed for relation identity;
- keeps LOCATOR only for independently selectable orientation relations;
- removes parent/child duplicate grains and cross-class duplication without a second independent function;
- constructs compounds only after the corrected unit layer is frozen.

No archetype row, expected count, evaluator finding, case-specific gold correction, or holdout content is placed into worker instructions.

## Retained controls

Unchanged:

- immutable archetype SHA-256 gate;
- exact-source literal lock;
- hidden evaluator and worker/gold isolation;
- candidate-only status;
- every attempt/failure preserved;
- sealed Case 5 prohibited during calibration;
- repeated Case 2/Case 6 passes required under one finalized contract before holdout;
- calibrated-lineage Case 5 may run exactly once only after that gate;
- successful calibrated lineage must be retired before fresh-agent clean-room Case 5 verification;
- no Oval Office promotion, APA IDs, or APA database/fabric writes.

## Forward effect

V50 prospectively supersedes V49 for new calibration/certification runs only. V49 and all predecessor contracts/runs remain immutable training history. No prior run is relabeled or deleted.
