/*
CASE 1 V16 OWNER-LOCAL CUSTODY CORRECTION
Owner: APA Cases
Status: CANDIDATE — REPOSITORY ONLY — DO NOT EXECUTE
Authorizing instruction: Presidential authorization in chat, 2026-09-19
Predecessor integrated candidate: leahtravers/APA-CASE-RESPONSES@9c2fd6d2bf4f782d8e03f64a2dd5b750741d3730
Source migration(s):
- 004_cases_graveyard_vault_candidate.sql; SHA-256 f526f97f5f41a7b76f30eb1ea516f3f0697795fdb03abb5c242a2f17d5aea502; Git blob ceb70a3857a0b8530679e6c552da0613bc6ee08b
Custody effect: additive owner-local successor for departmental validation.
No owner acceptance, Facilities approval, Security approval, installation, execution, or database authority is conveyed.
*/

DO $candidate_guard$
BEGIN
  RAISE EXCEPTION 'CANDIDATE_ONLY_NOT_AUTHORIZED_FOR_EXECUTION:CASE1_V16_OWNER_LOCAL_CASES';
END
$candidate_guard$;

BEGIN;

CREATE TABLE apa_cases_candidate.research_inventory_rehearsal_attempt_v16_candidate (
  attempt_key uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  attempt_ref text NOT NULL UNIQUE,
  job_ref text NOT NULL,
  packet_ref text NOT NULL UNIQUE,
  manifest_ref text NOT NULL,
  reservation_ref text NOT NULL,
  policy_ref text NOT NULL,
  license_ref text NOT NULL,
  destination_contract_ref text NOT NULL,
  audit_requirement_ref text NOT NULL,
  packet_sha256 text NOT NULL CHECK (packet_sha256 ~ '^[0-9a-f]{64}$'),
  planned_cardinal_count integer NOT NULL CHECK (planned_cardinal_count > 0),
  state text NOT NULL CHECK (state IN ('SEALED','PRESENTED','OUTCOME_RECONCILING','COMPLETED','PARTIAL','REJECTED_BEFORE_WRITE','UNCERTAIN')),
  presented_at timestamptz,
  reconciled_at timestamptz,
  predecessor_attempt_ref text,
  created_at timestamptz NOT NULL DEFAULT clock_timestamp()
);

CREATE TABLE apa_cases_candidate.research_inventory_cardinal_result_v16_candidate (
  cardinal_result_key uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  cardinal_result_ref text NOT NULL UNIQUE,
  attempt_ref text NOT NULL,
  cardinal integer NOT NULL CHECK (cardinal > 0),
  outcome text NOT NULL CHECK (outcome IN ('WRITTEN','REJECTED_BEFORE_WRITE','UNCERTAIN')),
  written_row_ref text,
  written_identity_ref text,
  destination_proof_ref text,
  error_class text,
  recorded_at timestamptz NOT NULL DEFAULT clock_timestamp(),
  CHECK ((outcome = 'WRITTEN' AND written_row_ref IS NOT NULL AND written_identity_ref IS NOT NULL AND destination_proof_ref IS NOT NULL)
      OR (outcome <> 'WRITTEN' AND written_row_ref IS NULL AND written_identity_ref IS NULL)),
  CHECK (outcome <> 'UNCERTAIN' OR destination_proof_ref IS NOT NULL),
  UNIQUE (attempt_ref, cardinal)
);

ALTER TABLE apa_cases_candidate.research_inventory_rehearsal_attempt_v16_candidate ENABLE ROW LEVEL SECURITY;
ALTER TABLE apa_cases_candidate.research_inventory_cardinal_result_v16_candidate ENABLE ROW LEVEL SECURITY;

REVOKE ALL ON TABLE apa_cases_candidate.research_inventory_rehearsal_attempt_v16_candidate FROM PUBLIC, anon, authenticated;
REVOKE ALL ON TABLE apa_cases_candidate.research_inventory_cardinal_result_v16_candidate FROM PUBLIC, anon, authenticated;

COMMIT;
