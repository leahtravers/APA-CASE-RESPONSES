# APA Cases — Renewed V16 Data-Contract Return

Date: 2026-09-18  
Authority event: `APA-EVENT-2026-09-18-V16-CLARIFIED-INTENT-0001` / blob `48d05727460f19185335c0827b0571cd99acde39`  
Registrar: `APA-EXEC-CASE1-V16-CLARIFIED-INTENT-RECONCILIATION-20260918-0001`  
Mode: `SIMULATED EXECUTIVE SEAT — REPRESENTED BY PRESIDENTIAL EXECUTIVE ASSISTANT`  
Independence: `PROCEDURAL / ATTRIBUTED — NOT TECHNICALLY ISOLATED`  
Scope: documentary decision only; no execution authority.

Seat: APA Cases General and Secretary — bounded case-domain pass  
Result: `ACCEPTED WITH EXACT DATA-CONTRACT CONDITIONS`

## Destination contract decisions

1. A destination accepts one sealed, manifest-matched candidate packet and returns an immutable per-cardinal outcome.
2. Identity activation is derived only from actual committed row admission. Unwritten candidates never appear as active identities.
3. A partial outcome preserves every written row and reports the unwritten subset; no rollback, deletion, renumbering, or candidate reuse occurs.
4. Lost response enters uncertain-state reconciliation. Readback uses exact permitted keys/proofs and may establish the written subset; it may not replay blindly.
5. A retry is a new attempt with newly compiled candidate material.
6. Direct writes outside the authorized gateway are denied and evidenced.
7. Security supplies the policy version and semantics. Licensing supplies a bounded active authority derived from that policy. The destination enforces both without authoring either.
8. The job carries its Audit Requirement Package and emits the exact per-cardinal and transaction evidence it specifies.
9. Monitoring receives bounded condition references; Logging receives nothing directly from the destination absent an expressly authorized non-audit diagnostic contract.

## Required outputs

- attempt and job references;
- admitted manifest/reservation/policy/license versions;
- per-cardinal `WRITTEN`, `REJECTED_BEFORE_WRITE`, or `UNCERTAIN` result;
- written-row identity references;
- destination integrity/readback proof;
- exact error class without payload leakage;
- Audit package reference;
- home-commentary reference, if any, held separately.

## Prohibited inferences

A license is not a policy; a receipt is not substantive success; a compiled candidate is not an identity; a later successful attempt does not erase a prior partial/failed attempt; a complete log is not an Audit finding.

## Holds preserved

No case data, schema, function, or policy was read or changed.
