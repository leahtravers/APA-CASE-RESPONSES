# Case 1 V16 Toolsmith Candidate Package

Status: `CANDIDATE — REPOSITORY CONSTRUCTION ONLY — DO NOT EXECUTE`

This package implements the deterministic shared contracts required by the Case 1 V16 Toolsmith BRD. It is deliberately separated from the active V15 dress-rehearsal workflow and the V87 calibration apparatus.

## Boundaries

- No database connection code.
- No SQL runner or deployment command.
- No gateway invocation.
- No APA identity activation outside a destination-confirmed `WRITTEN` result.
- No blind retry after an uncertain result.
- No Toolsmith-created Audit verdict, Security approval, Quality result, mint, or action copy.
- SQL files are additive placement candidates and begin with a fail-closed execution guard.

## Layout

- `src/case1_v16/contracts.py` — immutable contracts, state enumerations, and validation.
- `src/case1_v16/orchestrator.py` — deterministic repository-only orchestration and evidence generation.
- `src/case1_v16/authority.py` — exact manifest/reservation/policy/license binding validation.
- `src/case1_v16/processing.py` — queue bounds, endpoint custody, and uncertainty/no-replay contracts.
- `src/case1_v16/destination.py` — owner gateway protocol and result validator; no invocation implementation.
- `src/case1_v16/evidence.py` — prespecified-field Audit evidence emission with separate commentary type.
- `src/case1_v16/vault.py` — reproducible candidate-package validation without Quality or mint authority.
- `tests/test_contracts.py` — positive, negative, partial, uncertainty, retry, and custody tests.
- `migrations/` — candidate-only forward SQL. Facilities must inspect and separately authorize any execution.
- `audit-requirements/` — job-specific Audit Requirement Package candidates.
- `docs/` — placement, ownership, and owner-acceptance crosswalks.

## Authority

- Toolsmith Output BRD v2 blob: `a2a6e6712cb28a9716a4375f22b2f72e2e022163`
- Onboarding package blob: `1c34d762e3a41065a2505ef3c8d359866dd76170`
- Clarified-intent reconciliation blob: `b275167c89c13a984da3cf6ccbada8b9a6c5ff77`
- Compliance package: `APA-COMPLIANCE-V3`
- Construction Registrar: `APA-EXEC-CASE1-V16-TOOLSMITH-CONSTRUCTION-SUCCESSOR-20260919-0001`
