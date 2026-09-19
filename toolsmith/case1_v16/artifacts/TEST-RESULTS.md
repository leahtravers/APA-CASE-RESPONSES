# Candidate Test Results

Date: 2026-09-19  
Command: `python -m unittest discover -s toolsmith/case1_v16/tests -v`  
Result: `PASS — 11 tests`

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

This is Toolsmith test evidence, not an Audit finding, owner acceptance, Facilities verification, Security approval, or Tool Vault quality result.

