# Case 1 V16 Owner-Local SQL Custody Correction

Status: `CANDIDATE — OWNER-LOCAL CUSTODY — NO ACCEPTANCE OR EXECUTION`  
Date: 2026-09-19  
Repository: `leahtravers/APA-CASE-RESPONSES`  
Branch: `toolsmith/case1-v16-candidate-20260919`  
Predecessor integrated candidate: `leahtravers/APA-CASE-RESPONSES@9c2fd6d2bf4f782d8e03f64a2dd5b750741d3730`

## Custody correction

The original integrated Toolsmith package remains preserved in APA-CASE-RESPONSES. That package is historical predecessor evidence and is not deleted, rewritten, or reclassified.

This additive successor places each SQL object inside the repository and departmental path of its substantive chain of command so that the responsible owner can validate, remand, or succeed its own candidate. Presence here does not constitute owner acceptance.

| Candidate object | Owner-local file | Owner |
|---|---|---|
| `apa_cases_candidate.research_inventory_rehearsal_attempt_v16_candidate` | `toolsmith/case1_v16/owner-local/cases/004_cases_candidate.sql` | `cases` |
| `apa_cases_candidate.research_inventory_cardinal_result_v16_candidate` | `toolsmith/case1_v16/owner-local/cases/004_cases_candidate.sql` | `cases` |

## Lineage and verification

- Every owner-local file identifies the exact source migration SHA-256 and Git blob.
- The split preserves the predecessor table definitions, constraints, RLS enablement, and table-scoped default-deny revocations.
- Each file begins with a fail-closed exception before DDL.
- Static verification found no `DROP`, `DELETE`, `TRUNCATE`, `INSERT`, or `UPDATE` statement.
- The complete cross-repository split contains exactly 29 candidate tables.
- No foreign-owner schema is included in any owner-local file.

## Non-effects

This correction does not merge a branch, approve placement, accept a candidate, execute SQL, access a database, activate RLS or policy, issue identity or licensing authority, dispatch work, create an Audit finding, pass Tool Vault Quality, mint a tool, or issue an action copy.

Successors and corrections must be additive. The responsible owner retains authority over its own candidate and may remand or issue a successor without altering the predecessor.
