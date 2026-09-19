# Candidate Test Results

Date: 2026-09-19  
Command: `python -m unittest discover -s toolsmith/case1_v16/tests -v`  
Result: `PASS — 29 tests`

Covered controls:

- cardinal sequence is exactly `1..N`;
- unwritten cardinals cannot receive active identity references;
- partial outcomes preserve written subsets;
- uncertain outcomes require readback and block destruction/replay;
- Graveyard tombstones contain HMAC digest references but no plaintext candidate material;
- retries require new attempts, packets, and candidate material;
- Audit evidence and Logging projections remain separated;
- every migration is guarded against execution;
- migrations contain no destructive SQL;
- candidate tables enable RLS and revoke ordinary/public access;
- the Graveyard candidate object separates HMAC key references from digests.
- the assembler obeys only an exact owner-supplied grammar contract;
- historical decoding requires the exact grammar version;
- job transitions are forward-only;
- the Monitoring registry contains exactly `MON-V16-01..14`;
- Post Office keeps evidence and home commentary separate and validates receipt correlation.
- no migration may use a schema-wide grant or revoke against predecessor tables;
- endpoint exclusivity uses a partial unique index limited to the active `HELD` state.
- exact manifest, reservation, policy, license, Audit-package, and destination bindings fail closed on drift;
- inactive, expired, or policy-outliving license authority is rejected;
- queue and capacity bounds must be positive numeric values;
- repository-only endpoint custody permits one exact holder and exact-holder release;
- uncertainty uses the shorter of the contract deadline or 15 minutes and forbids same-attempt replay;
- destination results require the exact owner contract while direct writes remain prohibited;
- Audit evidence emitters reject fields not prespecified by the requirement package;
- reproducible vault manifests verify the exact file set and hashes;
- Toolsmith packages cannot contain Quality, mint, or action-copy result artifacts.

This is Toolsmith test evidence, not an Audit finding, owner acceptance, Facilities verification, Security approval, or Tool Vault quality result.
