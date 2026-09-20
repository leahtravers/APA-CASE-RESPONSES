# V118 RESEARCHER INVENTORY CALIBRATION CORRECTION RECORD

Status: `ACTIVE SUCCESSOR FOR CALIBRATION — NOT CERTIFIED`
Effective date: 2026-09-20
Authority: Leah's standing Researcher Inventory calibration instruction
Predecessor: `RI-CONTRACT-V117`
Successor: `RI-CONTRACT-V118`
Registrar: `APA-EXEC-2026-09-20-CASES-RI-V118-CAL-0001`

## Triggering evidence

Completed workflow run `35515875699` executed V117 against the required paired Case 2 and Case 6 calibration fixtures.

Before semantic execution it verified the repository archetype copies by SHA-256:

- `Case_2_Lightweight_Researcher_Inventory.xlsx` = `d47915552fdbdd23adc8c3f66ab06f94e022ab0bfd93faa5faabb53fdf9c9193`
- `Case_6_Lightweight_Researcher_Inventory_v2_with_Verbs_and_Locators.xlsx` = `50d646aad08b33051b93c1f3b3538d59ff78386558473b71a906a94213635070`

Repair required: none.

The deterministic apparatus/harness suite passed all 21 tests before semantic execution. Both semantic archetype comparisons then failed. The attempt and failure evidence were preserved in `calibration_history/researcher_inventory/35515875699-A1/` by apparatus commit `4fa06479f527ac62c1efc2ec1f253e220df0d911`.

A later scheduled V117 run `35517456325` was already in progress when V118 was prepared. V118 construction therefore does not manually rerun or dispatch calibration; the running predecessor attempt is allowed to finish under its own checked-out V117 authority and remains historical evidence.

## Defect classification

`WORKER-SEMANTIC DEFECT`

No new harness defect was demonstrated.

V117's `SOURCE-RECONNECTION COORDINATE CLOSURE` criterion allowed too many locally meaningful spans to qualify merely because they were useful for reconnecting source detail. This caused broad over-admission of surface fragments and incomplete natural-grain discrimination across classes. At the same time, some low-salience but genuinely source-individuated coordinates were still omitted.

The failure shows that **reconnection usefulness is necessary but not sufficient**. A coordinate must first be individuated by the source as a stable participant, referential handle, characterization, operative relation kernel, orientation, spatial support, or temporal support, and it must make a nonredundant contribution to at least one materially distinct binding.

## Prospective semantic correction

V118 introduces:

`MINIMAL SUFFICIENT BINDING BASIS AT SOURCE-INDIVIDUATED GRAIN`

The worker must:

1. identify materially distinct bindings before primitive extraction;
2. admit only source-individuated coordinates;
3. require each retained primitive to change at least one material binding;
4. restore local/one-use units when they are nonredundant binding coordinates rather than pruning them for low salience;
5. reject rhetorical color, discourse scaffolding, clause wrappers, modifier fragments, support wording, and semantically meaningful surface fragments that do not independently change binding structure;
6. preserve functional typing and literal source wording;
7. treat PLACE/TIME as distinct support only when needed to keep materially different bindings separate; and
8. construct compounds only as materially complete bindings among frozen primitives, without clause census, surface-proposition serialization, or graph closure.

No case-specific archetype rows, expected counts, evaluator findings, scored outputs, or sealed holdout material are included in the worker-facing contract or task rules.

## Harness disposition

Retained unchanged:

- immutable archetype verification;
- `V66` evaluator/harness correction;
- `V88A` editor-shorthand alignment;
- durable attempt-history preservation;
- same-session transient recovery;
- one-shot holdout isolation;
- clean-room certification gate.

Versioned V118 runner wrappers may point the existing proven evaluator to V118 task rules. This is routing, not a harness-semantic correction.

## Historical integrity

`RI-CONTRACT-V117` and all V117 runtime files, attempts, and findings remain preserved.

`RI-CONTRACT-V118` controls only new calibration executions after its activation. It does not retroactively alter or relabel V117 results.

## Holdout boundary

Case 5 remains `NOT_DEPLOYED` unless and until one finalized V118 contract and the same calibrated saved-agent lineage repeatedly pass Case 2 and Case 6 at approved archetypal resolution, lexical preservation, type assignment, and compound construction.

`researcher_inventory/tests/holdout/CASE_5.sealed.txt` must not be exposed to calibration, instructions, examples, or contract revision.
