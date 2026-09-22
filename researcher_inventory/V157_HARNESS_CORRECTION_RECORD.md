# Researcher Inventory V157 Harness Correction Record

Status: `HARNESS CORRECTION — SEMANTICALLY NEUTRAL`  
Date: 2026-09-22  
Authority: Leah's standing Researcher Inventory calibration instruction  
Related failed run: `35711775910` attempt 2  
Durable semantic contract retained: `researcher_inventory/AGENT_CONTRACT_V156.md` / `RI-CONTRACT-V156`  
Executive Registrar record: `APA-EXEC-2026-09-22-CASES-RI-V156-HARNESS-V157-1004-0001`

## 1. Evidence gate

Run `35711775910` attempt 2 recomputed and matched both immutable Leah-approved workbook SHA-256 values before semantic execution and repaired nothing:

- Case 2: `d47915552fdbdd23adc8c3f66ab06f94e022ab0bfd93faa5faabb53fdf9c9193`
- Case 6: `50d646aad08b33051b93c1f3b3538d59ff78386558473b71a906a94213635070`

All 51 deterministic apparatus/harness tests passed.

The attempt is preserved under `calibration_history/researcher_inventory/35711775910-A2/` by history commit `6d0f7ca0051067e11d639a8a8c4ea2fb0fe74419`.

The sealed Case 5 holdout was not opened or deployed.

## 2. Failure classification

Neither Case 2 nor Case 6 returned a semantic candidate. Both failed in managed Agents result reconciliation before evaluator adjudication.

V156 fixed the earlier replacement-session defect: each fixture kept one session identity and bounded recovery repeatedly reconciled that same session. The remaining failure was that the inherited V92/V156 path treated session status `idle` as terminal success and then searched session items for a `final_answer`. Both sessions remained `idle` while no final answer became visible until the bounded continuation window expired.

Current Agents lifecycle semantics distinguish **session state** from **turn state**. Session `idle` means the session is ready for input; it does not establish that the latest root turn completed successfully. The turn object independently exposes `status`, `completed_at`, and a customer-safe `error` for failed turns. Session items also carry `turn_id`, allowing output to be bound to the exact root turn.

Therefore this is a harness/runtime defect, not agent-behavior evidence. No semantic requirement is inferred from this failure and `RI-CONTRACT-V156` remains unchanged.

## 3. Semantically-neutral correction

V157 changes only result/session-turn reconciliation:

1. identify the latest root turn for the already-created session through `GET /agents/sessions/{session_id}/turns`;
2. bind recovery to that exact root turn identity;
3. while the turn is `queued`, `in_progress`, or `waiting`, continue bounded polling without creating a replacement session or turn;
4. if the turn is `failed`, surface the customer-safe turn error as runtime failure and do not infer semantic behavior;
5. if the turn is `cancelled`/`canceled`, surface runtime cancellation distinctly;
6. only when the exact root turn is `completed`, read the root session item history and accept `final_answer` output whose `turn_id` matches that turn;
7. paginate all item pages and reread the same completed turn for bounded result-visibility delay;
8. treat an unexpected root-turn identity change as uncertain state rather than silently switching executions.

V157 does not change the worker prompt, durable semantic contract, archetype evaluator, primitive normalization, compound normalization, immutable workbook gate, holdout gate, saved-agent instructions, or certification criteria.

## 4. Deterministic verification requirement

The successor harness must prove at minimum:

- a failed turn is surfaced immediately as runtime failure rather than being mistaken for an idle-session success;
- a completed turn can recover a final answer from a later paginated session-item page while filtering by exact `turn_id`;
- a nonterminal turn is polled until that same turn completes, regardless of session idleness; and
- a completed turn with initially delayed item visibility rereads the same turn rather than minting a new execution.

No gold rows, expected counts, evaluator findings, prior scored output, or holdout material may appear in these deterministic tests.

## 5. Historical integrity

V156 remains preserved as the harness that governed run `35711775910` attempt 2. V157 is an additive runtime successor only. It does not create `RI-CONTRACT-V157` and does not supersede V156 semantic instructions.

## 6. Holdout state

The sealed Case 5 holdout remains closed. A V157-routed execution must first achieve repeated Case 2 and Case 6 archetype passes under the unchanged finalized `RI-CONTRACT-V156` and the same saved-agent lineage before the one-shot holdout gate can open.
