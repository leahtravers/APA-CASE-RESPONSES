import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from case1_v16.contracts import (  # noqa: E402
    AuditRequirementPackage,
    CandidateCardinal,
    CandidatePacket,
    CardinalOutcome,
    CardinalResult,
    ContractError,
    DestinationResult,
    JobState,
    VersionBinding,
    assert_new_attempt,
)
from case1_v16.orchestrator import (  # noqa: E402
    build_tombstone,
    logging_projection,
    reconcile_destination,
)


HASH = "a" * 64


def binding(ref):
    return VersionBinding(ref, HASH)


def packet(packet_ref="PACKET-1", attempt_ref="ATTEMPT-1", values=("alpha", "beta")):
    return CandidatePacket(
        packet_ref=packet_ref,
        attempt_ref=attempt_ref,
        job_ref="JOB-1",
        manifest=binding("MANIFEST-1"),
        reservation=binding("RESERVATION-1"),
        policy=binding("POLICY-1"),
        license=binding("LICENSE-1"),
        destination_contract=binding("DESTINATION-1"),
        audit_requirements=binding("ARP-1"),
        compiler=binding("COMPILER-1"),
        cardinals=tuple(CandidateCardinal(i, value) for i, value in enumerate(values, 1)),
    )


class ContractTests(unittest.TestCase):
    def test_cardinals_must_be_contiguous(self):
        with self.assertRaisesRegex(ContractError, "CARDINALS_MUST_BE_CONTIGUOUS"):
            CandidatePacket(
                "P", "A", "J", binding("M"), binding("R"), binding("P"),
                binding("L"), binding("D"), binding("AR"), binding("C"),
                (CandidateCardinal(2, "x"),),
            )

    def test_unwritten_cannot_receive_active_identity(self):
        with self.assertRaisesRegex(ContractError, "UNWRITTEN_CARDINAL"):
            CardinalResult(1, CardinalOutcome.REJECTED_BEFORE_WRITE, "ACTIVE-ID")

    def test_partial_preserves_written_subset(self):
        p = packet()
        result = DestinationResult(
            p.packet_ref,
            p.attempt_ref,
            (
                CardinalResult(1, CardinalOutcome.WRITTEN, "ID-1", "PROOF-1"),
                CardinalResult(2, CardinalOutcome.REJECTED_BEFORE_WRITE, error_class="DENIED"),
            ),
        )
        reconciled = reconcile_destination(p, result)
        self.assertEqual(reconciled["terminal_state"], JobState.PARTIAL.value)
        self.assertEqual(reconciled["written_cardinals"], (1,))
        self.assertEqual(reconciled["unwritten_cardinals"], (2,))

    def test_uncertain_blocks_tombstone_and_replay(self):
        p = packet()
        result = DestinationResult(
            p.packet_ref,
            p.attempt_ref,
            (
                CardinalResult(1, CardinalOutcome.WRITTEN, "ID-1", "PROOF-1"),
                CardinalResult(2, CardinalOutcome.UNCERTAIN, destination_proof_ref="READBACK-1"),
            ),
        )
        self.assertEqual(
            reconcile_destination(p, result)["next_action"],
            "READBACK_RECONCILIATION_REQUIRED_NO_REPLAY",
        )
        with self.assertRaisesRegex(ContractError, "UNCERTAIN_MUST_BE_RECONCILED"):
            build_tombstone(
                packet=p,
                result=result,
                disposition_ref="D-1",
                hmac_key_ref="KEY-1",
                hmac_key=b"secret",
                destruction_attestation_ref="DESTROY-1",
                reason="unwritten",
            )

    def test_tombstone_contains_digest_not_plaintext(self):
        p = packet()
        result = DestinationResult(
            p.packet_ref,
            p.attempt_ref,
            (
                CardinalResult(1, CardinalOutcome.WRITTEN, "ID-1", "PROOF-1"),
                CardinalResult(2, CardinalOutcome.REJECTED_BEFORE_WRITE, error_class="DENIED"),
            ),
        )
        tombstone = build_tombstone(
            packet=p,
            result=result,
            disposition_ref="D-1",
            hmac_key_ref="KEY-1",
            hmac_key=b"secret",
            destruction_attestation_ref="DESTROY-1",
            reason="unwritten",
        ).as_evidence()
        self.assertNotIn("candidate_material", tombstone)
        self.assertNotIn("beta", repr(tombstone))
        self.assertEqual(tombstone["unwritten_cardinals"], (2,))

    def test_retry_requires_new_packet_attempt_and_material(self):
        predecessor = packet()
        with self.assertRaisesRegex(ContractError, "NEW_ATTEMPT"):
            assert_new_attempt(predecessor, packet(packet_ref="PACKET-2"))
        with self.assertRaisesRegex(ContractError, "NEW_PACKET"):
            assert_new_attempt(predecessor, packet(attempt_ref="ATTEMPT-2"))
        with self.assertRaisesRegex(ContractError, "REUSE_CANDIDATE"):
            assert_new_attempt(predecessor, packet("PACKET-2", "ATTEMPT-2"))
        assert_new_attempt(predecessor, packet("PACKET-2", "ATTEMPT-2", ("gamma", "delta")))

    def test_audit_and_logging_separation(self):
        arp = AuditRequirementPackage(
            "ARP-1", "JOB-1", binding("CONTRACT-1"),
            ("job_ref", "terminal_state"), ("candidate_plaintext",), ("no_secrets",),
        )
        evidence = {"job_ref": "JOB-1", "terminal_state": "PARTIAL", "private": "held"}
        arp.validate_evidence(evidence)
        projection = logging_projection(
            audit_evidence=evidence,
            allowed_fields=("job_ref", "terminal_state"),
            requisition_ref="REQ-1",
            criterion_ref="MON-V16-04",
        )
        self.assertNotIn("private", projection["surfaced"])


if __name__ == "__main__":
    unittest.main()

