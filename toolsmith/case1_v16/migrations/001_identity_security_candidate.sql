/*
CASE 1 V16 CANDIDATE MIGRATION 001
STATUS: DO NOT EXECUTE. REPOSITORY-ONLY PLACEMENT CANDIDATE.
Owners: CIA Identity (identity semantics); Security (policy); Facilities (placement).
No approval, installation, or database authority is conveyed by this file.
*/

DO $candidate_guard$
BEGIN
  RAISE EXCEPTION 'CANDIDATE_ONLY_NOT_AUTHORIZED_FOR_EXECUTION:CASE1_V16_001';
END
$candidate_guard$;

BEGIN;

CREATE TABLE apa_security.access_policy_v16_candidate (
  policy_key uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  policy_ref text NOT NULL UNIQUE,
  policy_version text NOT NULL,
  policy_sha256 text NOT NULL CHECK (policy_sha256 ~ '^[0-9a-f]{64}$'),
  security_owner_ref text NOT NULL,
  protected_resource_ref text NOT NULL,
  subject_classes_json jsonb NOT NULL,
  permitted_actions_json jsonb NOT NULL,
  denied_actions_json jsonb NOT NULL,
  conditions_json jsonb NOT NULL,
  exceptions_json jsonb NOT NULL DEFAULT '[]'::jsonb,
  test_vectors_json jsonb NOT NULL,
  required_evidence_json jsonb NOT NULL,
  state text NOT NULL CHECK (state IN ('DRAFT','SECURITY_ACCEPTED','EFFECTIVE','SUSPENDED','WITHDRAWN','SUPERSEDED','EXPIRED')),
  effective_at timestamptz,
  expires_at timestamptz,
  predecessor_policy_ref text,
  successor_policy_ref text,
  created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
  CHECK (predecessor_policy_ref IS DISTINCT FROM policy_ref),
  CHECK (successor_policy_ref IS DISTINCT FROM policy_ref)
);

CREATE TABLE apa_security.access_policy_test_v16_candidate (
  policy_test_key uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  policy_test_ref text NOT NULL UNIQUE,
  policy_ref text NOT NULL,
  test_class text NOT NULL CHECK (test_class IN ('POSITIVE','NEGATIVE','STALE','MISMATCH','EXPIRED','WITHDRAWN','PRIVILEGE','SEARCH_PATH','SECRET')),
  input_sha256 text NOT NULL CHECK (input_sha256 ~ '^[0-9a-f]{64}$'),
  expected_decision text NOT NULL CHECK (expected_decision IN ('ALLOW','DENY','FAIL_CLOSED')),
  evidence_requirement_ref text NOT NULL,
  created_at timestamptz NOT NULL DEFAULT clock_timestamp()
);

CREATE TABLE apa_identity.identity_rule_binding_v16_candidate (
  binding_key uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  binding_ref text NOT NULL UNIQUE,
  written_identity_ref text NOT NULL UNIQUE,
  identity_rule_ref text NOT NULL,
  identity_rule_sha256 text NOT NULL CHECK (identity_rule_sha256 ~ '^[0-9a-f]{64}$'),
  destination_write_proof_ref text NOT NULL,
  bound_at timestamptz NOT NULL DEFAULT clock_timestamp(),
  predecessor_binding_ref text,
  successor_binding_ref text
);

CREATE TABLE apa_identity.identity_event_binding_v16_candidate (
  event_binding_key uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  event_binding_ref text NOT NULL UNIQUE,
  written_identity_ref text NOT NULL,
  owner_domain_ref text NOT NULL,
  owner_event_ref text NOT NULL,
  event_reference_type text NOT NULL,
  binding_role text NOT NULL,
  disclosure_state text NOT NULL,
  authority_ref text NOT NULL,
  bound_at timestamptz NOT NULL DEFAULT clock_timestamp(),
  UNIQUE (written_identity_ref, owner_domain_ref, owner_event_ref, binding_role)
);

CREATE TABLE apa_identity.identity_relation_v16_candidate (
  relation_key uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  relation_ref text NOT NULL UNIQUE,
  subject_written_identity_ref text NOT NULL,
  relation_type_ref text NOT NULL,
  object_written_identity_ref text NOT NULL,
  governing_rule_ref text NOT NULL,
  governing_rule_sha256 text NOT NULL CHECK (governing_rule_sha256 ~ '^[0-9a-f]{64}$'),
  authority_event_ref text NOT NULL,
  created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
  predecessor_relation_ref text,
  successor_relation_ref text,
  CHECK (subject_written_identity_ref <> object_written_identity_ref),
  UNIQUE (subject_written_identity_ref, relation_type_ref, object_written_identity_ref)
);

CREATE TABLE apa_identity.decoder_contract_v16_candidate (
  decoder_contract_key uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  decoder_contract_ref text NOT NULL UNIQUE,
  grammar_version_ref text NOT NULL,
  source_sha256 text NOT NULL CHECK (source_sha256 ~ '^[0-9a-f]{64}$'),
  supported_written_version_refs_json jsonb NOT NULL,
  prohibited_projection_fields_json jsonb NOT NULL,
  state text NOT NULL CHECK (state IN ('CANDIDATE','OWNER_ACCEPTED','SUPERSEDED','WITHDRAWN')),
  predecessor_decoder_contract_ref text,
  created_at timestamptz NOT NULL DEFAULT clock_timestamp()
);

ALTER TABLE apa_security.access_policy_v16_candidate ENABLE ROW LEVEL SECURITY;
ALTER TABLE apa_security.access_policy_test_v16_candidate ENABLE ROW LEVEL SECURITY;
ALTER TABLE apa_identity.identity_rule_binding_v16_candidate ENABLE ROW LEVEL SECURITY;
ALTER TABLE apa_identity.identity_event_binding_v16_candidate ENABLE ROW LEVEL SECURITY;
ALTER TABLE apa_identity.identity_relation_v16_candidate ENABLE ROW LEVEL SECURITY;
ALTER TABLE apa_identity.decoder_contract_v16_candidate ENABLE ROW LEVEL SECURITY;

REVOKE ALL ON TABLE apa_security.access_policy_v16_candidate FROM PUBLIC, anon, authenticated;
REVOKE ALL ON TABLE apa_security.access_policy_test_v16_candidate FROM PUBLIC, anon, authenticated;
REVOKE ALL ON TABLE apa_identity.identity_rule_binding_v16_candidate FROM PUBLIC, anon, authenticated;
REVOKE ALL ON TABLE apa_identity.identity_event_binding_v16_candidate FROM PUBLIC, anon, authenticated;
REVOKE ALL ON TABLE apa_identity.identity_relation_v16_candidate FROM PUBLIC, anon, authenticated;
REVOKE ALL ON TABLE apa_identity.decoder_contract_v16_candidate FROM PUBLIC, anon, authenticated;

COMMIT;

