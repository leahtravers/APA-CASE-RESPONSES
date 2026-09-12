# APA Case Responses — Researcher Inventory Agent

Current mission: one job only.

When asked to prepare a **researcher inventory**, compile a lightweight, provisional researcher map of the supplied case and write it to the isolated candidate desk. Do not perform APA interpretation, protected-thread scoring, promotion, or Oval Office writes.

The governing files are:

- `researcher_inventory/AGENT_CONTRACT.md` — exact behavioral contract.
- `researcher_inventory/output_schema.json` — machine output contract.
- `researcher_inventory/session_bootstrap.py` — creates/boots the dedicated managed-agent session.
- `researcher_inventory/candidate_writer.py` — writes validated inventory output to the candidate tables only.
- `researcher_inventory/tests/` — repeatability fixtures and expected structural invariants.

Candidate database destination: `apa_cases_candidate` in APA Database V2 clean sandbox.

Promotion into Oval Office is deliberately out of scope and requires separate presidential authority.
