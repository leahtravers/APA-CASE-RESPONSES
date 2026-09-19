/* CASE 1 V16 CANDIDATE MIGRATION 002 — DO NOT EXECUTE. */
DO $candidate_guard$
BEGIN
  RAISE EXCEPTION 'CANDIDATE_ONLY_NOT_AUTHORIZED_FOR_EXECUTION:CASE1_V16_002';
END
$candidate_guard$;

BEGIN;

CREATE TABLE apa_licensing.reservation_v16_candidate (
  reservation_key uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  reservation_ref text NOT NULL UNIQUE,
  manifest_ref text NOT NULL,
  manifest_sha256 text NOT NULL CHECK (manifest_sha256 ~ '^[0-9a-f]{64}$'),
  policy_ref text NOT NULL,
  policy_sha256 text NOT NULL CHECK (policy_sha256 ~ '^[0-9a-f]{64}$'),
  endpoint_ref text NOT NULL,
  capacity_bound integer NOT NULL CHECK (capacity_bound > 0),
  state text NOT NULL CHECK (state IN ('REQUESTED','RESERVED','CONSUMED','EXPIRED','SUSPENDED','REVOKED','NOT_ISSUED')),
  reserved_at timestamptz,
  expires_at timestamptz,
  predecessor_reservation_ref text,
  created_at timestamptz NOT NULL DEFAULT clock_timestamp()
);

CREATE TABLE apa_licensing.execution_license_v16_candidate (
  license_key uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  license_ref text NOT NULL UNIQUE,
  job_ref text NOT NULL,
  attempt_ref text NOT NULL,
  manifest_ref text NOT NULL,
  reservation_ref text NOT NULL,
  policy_ref text NOT NULL,
  policy_sha256 text NOT NULL CHECK (policy_sha256 ~ '^[0-9a-f]{64}$'),
  worker_ref text NOT NULL,
  endpoint_ref text NOT NULL,
  destination_contract_ref text NOT NULL,
  audit_requirement_ref text NOT NULL,
  state text NOT NULL CHECK (state IN ('REQUESTED','POLICY_BOUND','RESERVED','ACTIVE','CONSUMED','EXPIRED','SUSPENDED','REVOKED','NOT_ISSUED')),
  activated_at timestamptz,
  closed_at timestamptz,
  predecessor_license_ref text,
  created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
  UNIQUE (job_ref, attempt_ref)
);

CREATE TABLE apa_licensing.action_permit_v16_candidate (
  permit_key uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  permit_ref text NOT NULL UNIQUE,
  license_ref text NOT NULL,
  tool_candidate_ref text NOT NULL,
  tool_candidate_sha256 text NOT NULL CHECK (tool_candidate_sha256 ~ '^[0-9a-f]{64}$'),
  action_ref text NOT NULL,
  state text NOT NULL CHECK (state IN ('INACTIVE','ACTIVE','SUSPENDED','REVOKED','RETIRED')),
  effective_at timestamptz,
  expires_at timestamptz,
  predecessor_permit_ref text,
  created_at timestamptz NOT NULL DEFAULT clock_timestamp()
);

CREATE TABLE apa_processing.queue_entry_v16_candidate (
  queue_entry_key uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  queue_entry_ref text NOT NULL UNIQUE,
  job_ref text NOT NULL,
  attempt_ref text NOT NULL,
  manifest_ref text NOT NULL,
  reservation_ref text NOT NULL,
  policy_ref text NOT NULL,
  license_ref text NOT NULL,
  packet_ref text NOT NULL,
  destination_contract_ref text NOT NULL,
  audit_requirement_ref text NOT NULL,
  endpoint_ref text NOT NULL,
  capacity_bound integer NOT NULL CHECK (capacity_bound > 0),
  source_versions_json jsonb NOT NULL,
  state text NOT NULL CHECK (state IN ('NOT_READY','QUEUED','DEPENDENCY_WAIT','CAPACITY_WAIT','DECISION_WAIT','RESERVED','DISPATCHED','START_UNCONFIRMED','RUNNING','OUTCOME_RECONCILING','SUCCEEDED','PARTIAL_SUCCESS','FAILED','NOT_DEPLOYED','UNCERTAIN')),
  enqueued_at timestamptz NOT NULL DEFAULT clock_timestamp(),
  predecessor_queue_entry_ref text,
  UNIQUE (job_ref, attempt_ref)
);

CREATE TABLE apa_processing.endpoint_holder_v16_candidate (
  endpoint_holder_key uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  endpoint_holder_ref text NOT NULL UNIQUE,
  endpoint_ref text NOT NULL,
  job_ref text NOT NULL,
  attempt_ref text NOT NULL,
  license_ref text NOT NULL,
  state text NOT NULL CHECK (state IN ('HELD','RELEASED','EXPIRED','UNCERTAIN')),
  held_at timestamptz NOT NULL DEFAULT clock_timestamp(),
  released_at timestamptz
);

CREATE UNIQUE INDEX endpoint_holder_v16_one_active_holder
  ON apa_processing.endpoint_holder_v16_candidate (endpoint_ref)
  WHERE state = 'HELD';

CREATE TABLE apa_processing.cardinal_outcome_v16_candidate (
  cardinal_outcome_key uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  outcome_ref text NOT NULL UNIQUE,
  job_ref text NOT NULL,
  attempt_ref text NOT NULL,
  packet_ref text NOT NULL,
  cardinal integer NOT NULL CHECK (cardinal > 0),
  outcome text NOT NULL CHECK (outcome IN ('WRITTEN','REJECTED_BEFORE_WRITE','UNCERTAIN')),
  written_identity_ref text,
  destination_proof_ref text,
  error_class text,
  recorded_at timestamptz NOT NULL DEFAULT clock_timestamp(),
  CHECK ((outcome = 'WRITTEN' AND written_identity_ref IS NOT NULL AND destination_proof_ref IS NOT NULL)
      OR (outcome <> 'WRITTEN' AND written_identity_ref IS NULL)),
  CHECK (outcome <> 'UNCERTAIN' OR destination_proof_ref IS NOT NULL),
  UNIQUE (attempt_ref, cardinal)
);

CREATE TABLE apa_processing.uncertainty_v16_candidate (
  uncertainty_key uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  uncertainty_ref text NOT NULL UNIQUE,
  job_ref text NOT NULL,
  attempt_ref text NOT NULL,
  endpoint_ref text NOT NULL,
  last_confirmed_state text NOT NULL,
  readback_contract_ref text NOT NULL,
  state text NOT NULL CHECK (state IN ('OPEN','RECONCILING','RESOLVED_WRITTEN','RESOLVED_UNWRITTEN','ESCALATED')),
  opened_at timestamptz NOT NULL DEFAULT clock_timestamp(),
  must_escalate_at timestamptz NOT NULL,
  resolved_at timestamptz,
  successor_attempt_ref text
);

ALTER TABLE apa_licensing.reservation_v16_candidate ENABLE ROW LEVEL SECURITY;
ALTER TABLE apa_licensing.execution_license_v16_candidate ENABLE ROW LEVEL SECURITY;
ALTER TABLE apa_licensing.action_permit_v16_candidate ENABLE ROW LEVEL SECURITY;
ALTER TABLE apa_processing.queue_entry_v16_candidate ENABLE ROW LEVEL SECURITY;
ALTER TABLE apa_processing.endpoint_holder_v16_candidate ENABLE ROW LEVEL SECURITY;
ALTER TABLE apa_processing.cardinal_outcome_v16_candidate ENABLE ROW LEVEL SECURITY;
ALTER TABLE apa_processing.uncertainty_v16_candidate ENABLE ROW LEVEL SECURITY;

REVOKE ALL ON TABLE apa_licensing.reservation_v16_candidate FROM PUBLIC, anon, authenticated;
REVOKE ALL ON TABLE apa_licensing.execution_license_v16_candidate FROM PUBLIC, anon, authenticated;
REVOKE ALL ON TABLE apa_licensing.action_permit_v16_candidate FROM PUBLIC, anon, authenticated;
REVOKE ALL ON TABLE apa_processing.queue_entry_v16_candidate FROM PUBLIC, anon, authenticated;
REVOKE ALL ON TABLE apa_processing.endpoint_holder_v16_candidate FROM PUBLIC, anon, authenticated;
REVOKE ALL ON TABLE apa_processing.cardinal_outcome_v16_candidate FROM PUBLIC, anon, authenticated;
REVOKE ALL ON TABLE apa_processing.uncertainty_v16_candidate FROM PUBLIC, anon, authenticated;

COMMIT;
