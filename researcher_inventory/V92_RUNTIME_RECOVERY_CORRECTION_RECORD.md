# V92 Researcher Inventory Runtime Recovery Correction Record

Status: `ACTIVE APPARATUS CORRECTION`  
Date: 2026-09-19  
Authority: Leah's standing Researcher Inventory calibration instruction  
Semantic contract: `RI-CONTRACT-V92`  
Evidence run: `35428079437-A1`  
Executive Registrar record: `APA-EXEC-2026-09-19-CASES-RI-V92-CAL-0001`

## Defect classification

`TEST-HARNESS / RUNTIME TRANSPORT DEFECT — SAME-SESSION WAIT RECOVERY`

During the V91 run's Case 6 calibration attempt, the saved agent session was created and the apparatus entered the bounded wait path. A transient connection reset surfaced as `urllib.error.URLError` from the session wait request. The inherited V90 recovery wrapper handles `RuntimeError("session timeout")` and contains a transient-transport branch inside that `RuntimeError` handler, but a transport exception that is not a `RuntimeError` bypasses that branch and escapes the adapter.

This failure occurred before semantic adjudication and therefore does not support a worker-contract change.

## Correction

V92 runtime recovery prospectively changes only transport handling:

1. preserve and reuse the exact existing session ID;
2. catch transient transport exceptions from `wait()` regardless of their Python exception class;
3. reconcile the current remote session status when possible;
4. if the same session remains nonterminal and the bounded total continuation window remains open, continue polling that same session;
5. if status retrieval itself encounters a transient transport failure, retry status/wait reconciliation within the same bounded window rather than creating a second session;
6. retry transient final-answer retrieval against the same completed session within the same bounded window;
7. preserve the recovery trace and state after every uncertain/transient event;
8. if the bounded window is exhausted or state cannot be reconciled, return `SessionUncertain` with the preserved session ID rather than manufacturing a semantic failure or starting a duplicate execution.

## Non-effects

This apparatus correction does not:

- change Researcher Inventory semantic rules;
- create a new session merely because transport failed;
- treat a lost response as proof of agent failure;
- alter evaluator/gold alignment;
- open or consume sealed Case 5;
- authorize promotion, APA IDs, or database writes.

## Historical integrity

The V90/V91 recovery implementations and run `35428079437-A1` remain unchanged historical evidence. V92 adds a successor runtime path only for new executions.