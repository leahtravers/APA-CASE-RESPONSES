/* CASE 1 V16 CANDIDATE MIGRATION 003 — DO NOT EXECUTE. */
DO $candidate_guard$
BEGIN
  RAISE EXCEPTION 'CANDIDATE_ONLY_NOT_AUTHORIZED_FOR_EXECUTION:CASE1_V16_003';
END
$candidate_guard$;

BEGIN;

CREATE TABLE apa_audit.requirement_package_v16_candidate (
  requirement_package_key uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  requirement_package_ref text NOT NULL UNIQUE,
  job_type_ref text NOT NULL,
  contract_ref text NOT NULL,
  contract_sha256 text NOT NULL CHECK (contract_sha256 ~ '^[0-9a-f]{64}$'),
  admitted_inputs_json jsonb NOT NULL,
  prohibited_inputs_json jsonb NOT NULL,
  gate_states_json jsonb NOT NULL,
  required_evidence_fields_json jsonb NOT NULL,
  negative_assertions_json jsonb NOT NULL,
  redaction_rules_json jsonb NOT NULL,
  retention_rules_json jsonb NOT NULL,
  state text NOT NULL CHECK (state IN ('DRAFT','ASSIGNED','SUPERSEDED','WITHDRAWN')),
  issued_at timestamptz,
  predecessor_requirement_package_ref text
);

CREATE TABLE apa_audit.evidence_submission_v16_candidate (
  evidence_submission_key uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  evidence_submission_ref text NOT NULL UNIQUE,
  requirement_package_ref text NOT NULL,
  job_ref text NOT NULL,
  attempt_ref text NOT NULL,
  terminal_state text NOT NULL,
  evidence_json jsonb NOT NULL,
  evidence_sha256 text NOT NULL CHECK (evidence_sha256 ~ '^[0-9a-f]{64}$'),
  submitted_at timestamptz NOT NULL DEFAULT clock_timestamp(),
  predecessor_submission_ref text,
  UNIQUE (job_ref, attempt_ref, requirement_package_ref)
);

CREATE TABLE apa_audit.home_commentary_v16_candidate (
  home_commentary_key uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  home_commentary_ref text NOT NULL UNIQUE,
  evidence_submission_ref text NOT NULL,
  home_department_ref text NOT NULL,
  commentary_json jsonb NOT NULL,
  commentary_sha256 text NOT NULL CHECK (commentary_sha256 ~ '^[0-9a-f]{64}$'),
  signed_by_ref text NOT NULL,
  created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
  predecessor_commentary_ref text
);

CREATE TABLE apa_monitoring.criterion_v16_candidate (
  criterion_key uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  criterion_ref text NOT NULL UNIQUE CHECK (criterion_ref ~ '^MON-V16-(0[1-9]|1[0-4])$'),
  criterion_version text NOT NULL,
  trigger_contract_json jsonb NOT NULL,
  severity text NOT NULL CHECK (severity IN ('CRITICAL','HIGH','MEDIUM')),
  logging_rule text NOT NULL,
  closure_rule text NOT NULL,
  state text NOT NULL CHECK (state IN ('DRAFT','APPROVED','EFFECTIVE','SUPERSEDED','WITHDRAWN')),
  predecessor_criterion_ref text
);

CREATE TABLE apa_monitoring.match_v16_candidate (
  match_key uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  match_ref text NOT NULL UNIQUE,
  criterion_ref text NOT NULL,
  audit_evidence_ref text,
  explicit_missing_evidence_state text,
  bounded_trigger_reference_json jsonb NOT NULL,
  severity text NOT NULL CHECK (severity IN ('CRITICAL','HIGH','MEDIUM')),
  owner_ref text NOT NULL,
  recipient_ref text NOT NULL,
  state text NOT NULL CHECK (state IN ('MATCHED','ROUTED','ACKNOWLEDGED','RESOLVED','ESCALATED')),
  opened_at timestamptz NOT NULL DEFAULT clock_timestamp(),
  resolved_at timestamptz,
  CHECK (audit_evidence_ref IS NOT NULL OR explicit_missing_evidence_state IS NOT NULL)
);

CREATE TABLE apa_logging.requisition_v16_candidate (
  requisition_key uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  requisition_ref text NOT NULL UNIQUE,
  criterion_ref text NOT NULL,
  match_ref text NOT NULL,
  allowed_fields_json jsonb NOT NULL,
  recipients_json jsonb NOT NULL,
  retention_rule_json jsonb NOT NULL,
  redaction_rule_json jsonb NOT NULL,
  state text NOT NULL CHECK (state IN ('OPEN','SURFACED','ACKNOWLEDGED','CLOSED')),
  opened_by_ref text NOT NULL,
  opened_at timestamptz NOT NULL DEFAULT clock_timestamp(),
  closed_at timestamptz,
  predecessor_requisition_ref text
);

CREATE TABLE apa_logging.surfaced_projection_v16_candidate (
  projection_key uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  projection_ref text NOT NULL UNIQUE,
  requisition_ref text NOT NULL,
  audit_evidence_ref text,
  explicit_missing_evidence_state text,
  bounded_projection_json jsonb NOT NULL,
  projection_sha256 text NOT NULL CHECK (projection_sha256 ~ '^[0-9a-f]{64}$'),
  redaction_marker text NOT NULL,
  surfaced_at timestamptz NOT NULL DEFAULT clock_timestamp()
);

CREATE TABLE apa_post_office.audit_envelope_v16_candidate (
  envelope_key uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  envelope_ref text NOT NULL UNIQUE,
  sender_ref text NOT NULL,
  audit_destination_ref text NOT NULL,
  evidence_submission_ref text NOT NULL,
  home_commentary_ref text,
  correlation_sha256 text NOT NULL CHECK (correlation_sha256 ~ '^[0-9a-f]{64}$'),
  state text NOT NULL CHECK (state IN ('SEALED','POSTED','DELIVERED','REJECTED','RETURNED','UNCERTAIN')),
  created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
  predecessor_envelope_ref text
);

CREATE TABLE apa_post_office.delivery_receipt_v16_candidate (
  delivery_receipt_key uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  delivery_receipt_ref text NOT NULL UNIQUE,
  envelope_ref text NOT NULL,
  attempt_no integer NOT NULL CHECK (attempt_no > 0),
  received_payload_classes_json jsonb NOT NULL,
  correlation_sha256 text NOT NULL CHECK (correlation_sha256 ~ '^[0-9a-f]{64}$'),
  result text NOT NULL CHECK (result IN ('DELIVERED','REJECTED','DUPLICATE_SAFE','UNCERTAIN')),
  received_at timestamptz NOT NULL DEFAULT clock_timestamp(),
  UNIQUE (envelope_ref, attempt_no)
);

ALTER TABLE apa_audit.requirement_package_v16_candidate ENABLE ROW LEVEL SECURITY;
ALTER TABLE apa_audit.evidence_submission_v16_candidate ENABLE ROW LEVEL SECURITY;
ALTER TABLE apa_audit.home_commentary_v16_candidate ENABLE ROW LEVEL SECURITY;
ALTER TABLE apa_monitoring.criterion_v16_candidate ENABLE ROW LEVEL SECURITY;
ALTER TABLE apa_monitoring.match_v16_candidate ENABLE ROW LEVEL SECURITY;
ALTER TABLE apa_logging.requisition_v16_candidate ENABLE ROW LEVEL SECURITY;
ALTER TABLE apa_logging.surfaced_projection_v16_candidate ENABLE ROW LEVEL SECURITY;
ALTER TABLE apa_post_office.audit_envelope_v16_candidate ENABLE ROW LEVEL SECURITY;
ALTER TABLE apa_post_office.delivery_receipt_v16_candidate ENABLE ROW LEVEL SECURITY;

REVOKE ALL ON TABLE apa_audit.requirement_package_v16_candidate FROM PUBLIC, anon, authenticated;
REVOKE ALL ON TABLE apa_audit.evidence_submission_v16_candidate FROM PUBLIC, anon, authenticated;
REVOKE ALL ON TABLE apa_audit.home_commentary_v16_candidate FROM PUBLIC, anon, authenticated;
REVOKE ALL ON TABLE apa_monitoring.criterion_v16_candidate FROM PUBLIC, anon, authenticated;
REVOKE ALL ON TABLE apa_monitoring.match_v16_candidate FROM PUBLIC, anon, authenticated;
REVOKE ALL ON TABLE apa_logging.requisition_v16_candidate FROM PUBLIC, anon, authenticated;
REVOKE ALL ON TABLE apa_logging.surfaced_projection_v16_candidate FROM PUBLIC, anon, authenticated;
REVOKE ALL ON TABLE apa_post_office.audit_envelope_v16_candidate FROM PUBLIC, anon, authenticated;
REVOKE ALL ON TABLE apa_post_office.delivery_receipt_v16_candidate FROM PUBLIC, anon, authenticated;

COMMIT;
