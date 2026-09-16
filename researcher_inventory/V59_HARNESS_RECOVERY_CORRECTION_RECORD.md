# V59 HARNESS RECOVERY CORRECTION RECORD

Status: ACTIVE ADDITIVE HARNESS SUCCESSOR
Date: 2026-09-16
Semantic contract: `RI-CONTRACT-V59`
Preserved triggering run: `35137987643`
Executive filing: `APA-EXEC-2026-09-16-CASES-RI-V59-CAL-0001`

## Defect classification

`HARNESS / TRANSPORT RECOVERY DEFECT — UNCERTAIN STATE`

During V58 calibration run `35137987643`, the oil-change calibration path had an existing saved-agent session identity but a subsequent Agents API access returned `HTTP 500: An internal error occurred.` The failure occurred in session-state/result transport, before a complete semantic adjudication could be obtained.

This event is not agent-behavior evidence and is not used to justify semantic contract changes.

## Predecessor behavior

The shared V32/V55 recovery implementation treats runtime errors other than the literal string `session timeout` as terminal. The V55 adapter then deletes local recovery state for generic exceptions. For a transient HTTP 5xx or connection/status-read failure, this can lose the durable pointer to an execution that may still exist and later cause a fresh backend session to be created for the same semantic request.

That conflicts with the uncertain-state rule: reconcile/recover the existing attempt before starting another.

## Additive V59 repair

V59 does not rewrite V32, V55, or V58 historical adapters. Instead, `v59_openai_agents_adapter.py` installs a successor session-recovery wrapper for V59 only.

The wrapper:

1. preserves the existing session ID and local recovery state when an Agents API status/result read returns a transient HTTP 5xx, connection-reset/refusal, gateway/service-unavailable, or equivalent temporary transport error;
2. records the uncertain transport event in the recovery trace;
3. raises the existing `SessionUncertain` state rather than classifying the semantic execution as failed;
4. allows the apparatus retry path to resume/reconcile the same backend session;
5. retains confirmed terminal-state behavior for actual terminal session states and non-transient errors;
6. does not alter semantic prompts, evaluator behavior, archetype access, or holdout gates.

## Boundary

This is a harness recovery correction only. It does not change what constitutes a Researcher Inventory coordinate or compound, does not consume semantic evaluator findings, and does not authorize a research rerun when the predecessor execution remains uncertain.

## Historical integrity

All V32/V55/V58 adapters, traces, and failed attempts remain unchanged. The V59 recovery namespace is separate and preserves successor lineage.
