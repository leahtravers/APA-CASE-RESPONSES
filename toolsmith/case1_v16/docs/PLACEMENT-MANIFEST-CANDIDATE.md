# Case 1 V16 Placement Manifest Candidate

Status: `CANDIDATE — PRESIDENTIAL PLACEMENT APPROVAL AND OWNER ACCEPTANCE REQUIRED BEFORE DDL`  
Target: APA Database V2 clean sandbox `uvzkiajzzlujxtywhubx`  
Construction authority: repository-only; no database access or execution

## Purpose

Provide additive V16 structures for policy, licensing, Processing, per-cardinal destination outcomes, evidence, Monitoring, Logging, transport, unwritten-candidate disposition, and Tool Vault custody without modifying or deleting predecessor objects.

## Placement

| Migration | Schemas | Substantive owners |
|---|---|---|
| `001_identity_security_candidate.sql` | `apa_identity`, `apa_security` | CIA Identity; Security |
| `002_licensing_processing_candidate.sql` | `apa_licensing`, `apa_processing` | Licensing; Processing |
| `003_evidence_monitoring_transport_candidate.sql` | `apa_audit`, `apa_monitoring`, `apa_logging`, `apa_post_office` | Audit; Monitoring; Logging; Post Office |
| `004_cases_graveyard_vault_candidate.sql` | `apa_cases_candidate`, `apa_graveyard`, `apa_oval_office` | APA Cases; Graveyard; Tool Vault/Oval Office |

## Readers and writers

No executable grants are proposed in this candidate. Every table enables RLS and revokes access from `PUBLIC`, `anon`, and `authenticated`. Security must issue exact policy semantics; Licensing must bind the permitted subject/action/resource/condition set; Facilities must translate accepted policy into separately reviewed policies and grants.

## One-way doors

- Candidate identity material may flow to one authorized destination operation only.
- Only destination-confirmed written cardinals may produce active identity bindings.
- Unwritten material flows to destruction plus a Graveyard tombstone containing digest references, not plaintext.
- Audit evidence and home commentary remain separate payload classes.
- Logging receives only a Monitoring-matched, requisition-authorized projection from Audit.
- Minting does not issue an action copy.

## Prohibited connections

- no assembler read from destination tables;
- no cross-department broad browsing;
- no direct ordinary-agent table writes;
- no policy authored inside Licensing or Facilities implementation;
- no producer-to-Logging bypass;
- no plaintext candidate storage in ordinary Graveyard, Audit, Monitoring, or Logging;
- no Toolsmith write to quality or mint results;
- no blind replay after uncertainty.

## Functions and views

No privileged function or view is included in the first placement candidate. Those require owner-accepted signatures, exact caller roles, fixed search paths, and function-specific negative tests before Facilities prepares a successor migration.

## Succession and removal

Every object is additive and suffixed or uniquely named. No predecessor is renamed, dropped, repurposed, or rewritten. Before any operational write, accepted candidate objects become forward successors through owner-specific authority records. If rejected before use, removal still requires separate Facilities authority and a preserved construction disposition.

## Required acceptance

CIA Identity, Security, Licensing, Processing, APA Cases, Audit, Monitoring, Logging, Post Office, Graveyard, Facilities, Tool Vault governance, and applicable HR separation evidence must each accept only their own remit. Audit must issue job-specific requirement packages. Presidential placement approval is separate from repository construction authorization.

