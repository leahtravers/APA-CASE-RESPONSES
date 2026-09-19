# Audit Requirement Package Candidate

Package: `ARP-CASE1-V16-REPOSITORY-CONSTRUCTION-CANDIDATE`  
Status: `CANDIDATE FOR AUDIT OWNER ASSIGNMENT — NOT AN AUDIT-ISSUED PACKAGE`  
Producer: Presidential Toolsmith  
Subject: Case 1 V16 repository-only construction campaign

This file proposes the minimally sufficient evidence fields for Audit. It does not assign requirements to Audit, constitute Audit acceptance, or authorize execution.

## Required common evidence

1. job, attempt, contract, manifest, authority, owner, environment, and intended-output references;
2. admitted and prohibited inputs;
3. source paths, blob identities, SHA-256 values, and predecessor/successor references;
4. start and end timestamps;
5. exact repository, branch, commit, file, and artifact hashes;
6. positive, negative, failure, partial, rejection, nondeployment, uncertainty, and recovery test outcomes where applicable;
7. policy, identity, license, Processing, Post Office, Facilities, Graveyard, and Tool Vault references where applicable;
8. prohibited-event assertions;
9. redaction and restricted-reference markers;
10. duplicate-correlation and retention rules.

## Job packages requested from Audit

| Job | Required outcome coverage |
|---|---|
| Shared contracts | deterministic validation; stale/missing/mismatched version denial |
| Identity compiler/decoder | zero/full/partial write; no destination read; historical decode; retry regeneration |
| Security/Licensing | allow/deny/stale/expired/withdrawn/mismatched policy; privilege denial |
| Processing/Cases | queue, endpoint exclusivity, every cardinal boundary, lost response, readback, no replay |
| Evidence/Monitoring/Logging/Post Office | all terminal evidence; dual payload; requisition projection; duplicate safety |
| Graveyard | no plaintext; HMAC/key separation; destruction; sealed-expiry; non-reuse |
| Tool Vault | reproducible build; locked dependencies; source/artifact hashes; separation of builder/quality/mint |

## Prohibited evidence content

- plaintext unwritten identity candidates;
- secrets or HMAC keys;
- unrestricted destination payloads;
- unrestricted home commentary;
- hidden calibration archetypes or sealed holdout content;
- invented Audit findings or owner acceptances.

