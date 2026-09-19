import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from case1_v16.contracts import ContractError, JobState  # noqa: E402
from case1_v16.identity import CandidateIdentityCompiler, GrammarContract, HistoricalIdentityDecoder  # noqa: E402
from case1_v16.monitoring import CRITERIA, record_match  # noqa: E402
from case1_v16.post_office import AuditEnvelope, correlate_receipt  # noqa: E402
from case1_v16.state_machine import JOB_MACHINE  # noqa: E402


class ExtendedContractTests(unittest.TestCase):
    def grammar(self):
        return GrammarContract(
            contract_ref="GRAMMAR-V16-OWNER-CANDIDATE",
            contract_sha256="b" * 64,
            literal_prefix="TEST",
            delimiter="::",
            ordered_fields=("origin", "job", "department", "minute", "cardinal"),
            component_pattern=r"[A-Z0-9_-]+",
            maximum_length=180,
        )

    def test_compiler_uses_only_bound_grammar_and_explicit_inputs(self):
        compiler = CandidateIdentityCompiler(self.grammar())
        candidate = compiler.compile(
            {"origin": "CASE1", "job": "JOB1", "department": "CASES", "minute": "20260919T0102Z", "cardinal": 1}
        )
        self.assertEqual(candidate.candidate_class, "CANDIDATE_IDENTITY_MATERIAL")
        self.assertEqual(candidate.candidate_material, "TEST::CASE1::JOB1::CASES::20260919T0102Z::1")

    def test_compiler_rejects_unbound_field_or_invalid_component(self):
        compiler = CandidateIdentityCompiler(self.grammar())
        with self.assertRaisesRegex(ContractError, "FIELD_MISMATCH"):
            compiler.compile({"cardinal": 1})
        with self.assertRaisesRegex(ContractError, "INVALID_GRAMMAR_COMPONENT"):
            compiler.compile(
                {"origin": "CASE 1", "job": "JOB1", "department": "CASES", "minute": "20260919T0102Z", "cardinal": 1}
            )

    def test_historical_decoder_requires_exact_contract(self):
        grammar = self.grammar()
        decoder = HistoricalIdentityDecoder({grammar.contract_ref: grammar})
        decoded = decoder.decode("TEST::CASE1::JOB1::CASES::20260919T0102Z::1", grammar.contract_ref)
        self.assertEqual(decoded["cardinal"], "1")
        with self.assertRaisesRegex(ContractError, "UNKNOWN_HISTORICAL_GRAMMAR"):
            decoder.decode("TEST::CASE1::JOB1::CASES::20260919T0102Z::1", "UNKNOWN")

    def test_job_machine_is_forward_only(self):
        transition = JOB_MACHINE.transition(
            JobState.DRAFT, JobState.CONTRACTED, authority_ref="AUTH-1", evidence_ref="EVIDENCE-1"
        )
        self.assertEqual(transition.successor, JobState.CONTRACTED)
        with self.assertRaisesRegex(ContractError, "INVALID_STATE_TRANSITION"):
            JOB_MACHINE.transition(
                JobState.EXECUTING, JobState.QUEUED, authority_ref="AUTH-1", evidence_ref="EVIDENCE-1"
            )

    def test_monitoring_registry_contains_exact_fourteen(self):
        self.assertEqual(set(CRITERIA), {f"MON-V16-{i:02d}" for i in range(1, 15)})
        match = record_match(
            criterion_ref="MON-V16-07", evidence_ref="E-1", owner_ref="PROCESSING", recipient_ref="SECURITY"
        )
        self.assertEqual(match["state"], "MATCHED")

    def test_post_office_keeps_payloads_separate_and_correlates(self):
        envelope = AuditEnvelope(
            envelope_ref="ENV-1",
            sender_ref="CASES",
            audit_destination_ref="AUDIT",
            evidence_submission_ref="EVIDENCE-1",
            evidence_sha256="c" * 64,
            home_commentary_ref="COMMENT-1",
            commentary_sha256="d" * 64,
        )
        self.assertEqual(correlate_receipt(envelope, envelope.correlation_sha256), "DELIVERED_CORRELATED")
        with self.assertRaisesRegex(ContractError, "CORRELATION_MISMATCH"):
            correlate_receipt(envelope, "e" * 64)


if __name__ == "__main__":
    unittest.main()

