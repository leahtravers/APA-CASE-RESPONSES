/* CASE 1 V16 CANDIDATE MIGRATION 004 — DO NOT EXECUTE. */
DO $candidate_guard$
BEGIN
  RAISE EXCEPTION 'CANDIDATE_ONLY_NOT_AUTHORIZED_FOR_EXECUTION:CASE1_V16_004';
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

CREATE TABLE apa_graveyard.unwritten_identity_candidate_disposition (
  disposition_key uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  disposition_ref text NOT NULL UNIQUE,
  job_ref text NOT NULL,
  attempt_ref text NOT NULL,
  manifest_ref text NOT NULL,
  reservation_ref text NOT NULL,
  contract_ref text NOT NULL,
  home_department_ref text NOT NULL,
  compiler_version_ref text NOT NULL,
  packet_sha256 text NOT NULL CHECK (packet_sha256 ~ '^[0-9a-f]{64}$'),
  hmac_key_ref text NOT NULL,
  hmac_sha256 text NOT NULL CHECK (hmac_sha256 ~ '^[0-9a-f]{64}$'),
  planned_cardinals_json jsonb NOT NULL,
  written_cardinals_json jsonb NOT NULL,
  unwritten_cardinals_json jsonb NOT NULL,
  outcome text NOT NULL CHECK (outcome IN ('NOT_DEPLOYED','PARTIAL','REJECTED_BEFORE_WRITE','FAILED_AFTER_WRITE')),
  reason text NOT NULL,
  destruction_attestation_ref text NOT NULL,
  audit_requirement_ref text NOT NULL,
  sealed_exception_ref text,
  sealed_exception_expires_at timestamptz,
  predecessor_disposition_ref text,
  successor_disposition_ref text,
  created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
  CHECK ((sealed_exception_ref IS NULL AND sealed_exception_expires_at IS NULL)
      OR (sealed_exception_ref IS NOT NULL AND sealed_exception_expires_at IS NOT NULL
          AND sealed_exception_expires_at <= created_at + interval '30 days'))
);

CREATE TABLE apa_oval_office.tool_candidate_v16_candidate (
  tool_candidate_key uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  tool_candidate_ref text NOT NULL UNIQUE,
  substantive_owner_ref text NOT NULL,
  source_repository_ref text NOT NULL,
  source_commit_sha1 text NOT NULL CHECK (source_commit_sha1 ~ '^[0-9a-f]{40}$'),
  source_manifest_sha256 text NOT NULL CHECK (source_manifest_sha256 ~ '^[0-9a-f]{64}$'),
  artifact_sha256 text NOT NULL CHECK (artifact_sha256 ~ '^[0-9a-f]{64}$'),
  dependency_lock_sha256 text NOT NULL CHECK (dependency_lock_sha256 ~ '^[0-9a-f]{64}$'),
  audit_requirement_ref text NOT NULL,
  state text NOT NULL CHECK (state IN ('CANDIDATE','OWNER_ACCEPTED','QUALITY_ELIGIBLE','REMAND','FAILED','SUPERSEDED','WITHDRAWN')),
  predecessor_tool_candidate_ref text,
  created_at timestamptz NOT NULL DEFAULT clock_timestamp()
);

CREATE TABLE apa_oval_office.tool_quality_result_v16_candidate (
  quality_result_key uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  quality_result_ref text NOT NULL UNIQUE,
  tool_candidate_ref text NOT NULL,
  quality_officer_ref text NOT NULL,
  qualification_contract_ref text NOT NULL,
  evidence_manifest_sha256 text NOT NULL CHECK (evidence_manifest_sha256 ~ '^[0-9a-f]{64}$'),
  result text NOT NULL CHECK (result IN ('QUALITY_PASSED','REMAND','UNCERTAIN','FAILED')),
  issued_at timestamptz NOT NULL DEFAULT clock_timestamp(),
  predecessor_quality_result_ref text
);

CREATE TABLE apa_oval_office.tool_mint_record_v16_candidate (
  mint_record_key uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  mint_record_ref text NOT NULL UNIQUE,
  tool_candidate_ref text NOT NULL,
  quality_result_ref text NOT NULL,
  security_acceptance_ref text NOT NULL,
  facilities_acceptance_ref text NOT NULL,
  processing_acceptance_ref text NOT NULL,
  licensing_completion_ref text NOT NULL,
  audit_package_ref text NOT NULL,
  oval_mint_authority_ref text NOT NULL,
  minting_officer_ref text NOT NULL,
  minted_at timestamptz NOT NULL DEFAULT clock_timestamp(),
  predecessor_mint_record_ref text
);

CREATE TABLE apa_oval_office.tool_action_copy_decision_v16_candidate (
  action_copy_decision_key uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  action_copy_decision_ref text NOT NULL UNIQUE,
  mint_record_ref text NOT NULL,
  processing_custodian_ref text NOT NULL,
  action_permit_ref text NOT NULL,
  state text NOT NULL CHECK (state IN ('NOT_ISSUED','ISSUED','SUSPENDED','REVOKED','RETIRED')),
  issued_at timestamptz,
  predecessor_action_copy_decision_ref text
);

ALTER TABLE apa_cases_candidate.research_inventory_rehearsal_attempt_v16_candidate ENABLE ROW LEVEL SECURITY;
ALTER TABLE apa_cases_candidate.research_inventory_cardinal_result_v16_candidate ENABLE ROW LEVEL SECURITY;
ALTER TABLE apa_graveyard.unwritten_identity_candidate_disposition ENABLE ROW LEVEL SECURITY;
ALTER TABLE apa_oval_office.tool_candidate_v16_candidate ENABLE ROW LEVEL SECURITY;
ALTER TABLE apa_oval_office.tool_quality_result_v16_candidate ENABLE ROW LEVEL SECURITY;
ALTER TABLE apa_oval_office.tool_mint_record_v16_candidate ENABLE ROW LEVEL SECURITY;
ALTER TABLE apa_oval_office.tool_action_copy_decision_v16_candidate ENABLE ROW LEVEL SECURITY;

REVOKE ALL ON TABLE apa_cases_candidate.research_inventory_rehearsal_attempt_v16_candidate FROM PUBLIC, anon, authenticated;
REVOKE ALL ON TABLE apa_cases_candidate.research_inventory_cardinal_result_v16_candidate FROM PUBLIC, anon, authenticated;
REVOKE ALL ON TABLE apa_graveyard.unwritten_identity_candidate_disposition FROM PUBLIC, anon, authenticated;
REVOKE ALL ON TABLE apa_oval_office.tool_candidate_v16_candidate FROM PUBLIC, anon, authenticated;
REVOKE ALL ON TABLE apa_oval_office.tool_quality_result_v16_candidate FROM PUBLIC, anon, authenticated;
REVOKE ALL ON TABLE apa_oval_office.tool_mint_record_v16_candidate FROM PUBLIC, anon, authenticated;
REVOKE ALL ON TABLE apa_oval_office.tool_action_copy_decision_v16_candidate FROM PUBLIC, anon, authenticated;

COMMIT;

