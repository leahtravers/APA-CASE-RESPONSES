import hashlib
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from case1_v16.authority import DispatchAuthority  # noqa: E402
from case1_v16.contracts import (  # noqa: E402
    AuditRequirementPackage,
    CandidateCardinal,
    CandidatePacket,
    CardinalOutcome,
    CardinalResult,
    ContractError,
    DestinationResult,
    LicenseState,
    PolicyState,
    VersionBinding,
)
from case1_v16.destination import DestinationResultValidator, direct_write  # noqa: E402
from case1_v16.evidence import EvidenceEmitter  # noqa: E402
from case1_v16.processing import (  # noqa: E402
    EndpointCustody,
    QueueEntry,
    assert_no_replay,
    open_uncertainty,
)
from case1_v16.vault import CandidatePackageManifest, FileDigest  # noqa: E402


HASH = "a" * 64
NOW = datetime(2026, 9, 19, 2, 0, tzinfo=timezone.utc)


def binding(ref):
    return VersionBinding(ref, HASH)


def packet():
    return CandidatePacket(
        "PACKET-1", "ATTEMPT-1", "JOB-1", binding("MANIFEST-1"),
        binding("RESERVATION-1"), binding("POLICY-1"), binding("LICENSE-1"),
        binding("DESTINATION-1"), binding("ARP-1"), binding("COMPILER-1"),
        (CandidateCardinal(1, "candidate"),),
    )


def authority(**changes):
    p = packet()
    values = dict(
        manifest=p.manifest,
        reservation=p.reservation,
        reservation_manifest=p.manifest,
        policy=p.policy,
        policy_state=PolicyState.EFFECTIVE,
        policy_expires_at=NOW + timedelta(hours=2),
        license=p.license,
        license_state=LicenseState.ACTIVE,
        license_policy=p.policy,
        license_manifest=p.manifest,
        license_expires_at=NOW + timedelta(hours=1),
        audit_requirements=p.audit_requirements,
        destination_contract=p.destination_contract,
        queue_position=1,
        capacity_bound=1,
    )
    values.update(changes)
    return DispatchAuthority(**values)


def queue_entry(**changes):
    p = packet()
    values = dict(
        job_ref=p.job_ref,
        attempt_ref=p.attempt_ref,
        endpoint_ref="CASE-GATEWAY",
        manifest=p.manifest,
        reservation=p.reservation,
        policy=p.policy,
        license=p.license,
        packet=binding(p.packet_ref),
        destination_contract=p.destination_contract,
        audit_requirements=p.audit_requirements,
        source_versions_sha256=HASH,
        queue_position=1,
        capacity_bound=1,
    )
    values.update(changes)
    return QueueEntry(**values)


class AuthorityProcessingVaultTests(unittest.TestCase):
    def test_exact_authority_bindings_pass_without_activation(self):
        authority().validate(packet(), at=NOW)

    def test_mismatched_or_inactive_authority_fails_closed(self):
        with self.assertRaisesRegex(ContractError, "AUTHORITY_BINDING_MISMATCH"):
            authority(license_policy=binding("OTHER-POLICY")).validate(packet(), at=NOW)
        with self.assertRaisesRegex(ContractError, "POLICY_NOT_EFFECTIVE"):
            authority(policy_state=PolicyState.SUSPENDED).validate(packet(), at=NOW)

    def test_expired_and_policy_outliving_license_rules(self):
        with self.assertRaisesRegex(ContractError, "POLICY_EXPIRED"):
            authority(policy_expires_at=NOW).validate(packet(), at=NOW)
        with self.assertRaisesRegex(ContractError, "OUTLIVES_POLICY"):
            authority(
                policy_expires_at=NOW + timedelta(minutes=30),
                license_expires_at=NOW + timedelta(hours=1),
            ).validate(packet(), at=NOW)

    def test_queue_requires_numeric_bounds(self):
        with self.assertRaisesRegex(ContractError, "POSITIVE_NUMERIC_BOUNDS"):
            queue_entry(capacity_bound=0)

    def test_only_one_endpoint_holder_and_exact_release(self):
        custody = EndpointCustody()
        lease = custody.acquire(queue_entry())
        with self.assertRaisesRegex(ContractError, "ENDPOINT_ALREADY_HELD"):
            custody.acquire(queue_entry(attempt_ref="ATTEMPT-2"))
        self.assertEqual(custody.release(lease).state, "RELEASED")

    def test_uncertainty_uses_shorter_deadline_and_forbids_replay(self):
        window = open_uncertainty(
            job_ref="JOB-1",
            attempt_ref="ATTEMPT-1",
            opened_at=NOW,
            contract_deadline=NOW + timedelta(minutes=7),
        )
        self.assertEqual(window.deadline, NOW + timedelta(minutes=7))
        self.assertTrue(window.requires_escalation(at=NOW + timedelta(minutes=7)))
        with self.assertRaisesRegex(ContractError, "CANNOT_BE_REPLAYED"):
            assert_no_replay(uncertain_attempt_ref="ATTEMPT-1", proposed_attempt_ref="ATTEMPT-1")

    def test_destination_validator_checks_exact_contract_without_invocation(self):
        p = packet()
        DestinationResultValidator(p.destination_contract).validate(
            p,
            DestinationResult(
                p.packet_ref,
                p.attempt_ref,
                (CardinalResult(1, CardinalOutcome.REJECTED_BEFORE_WRITE, error_class="DENIED"),),
            ),
        )
        with self.assertRaisesRegex(ContractError, "DIRECT_DESTINATION_WRITE_PROHIBITED"):
            direct_write("anything")

    def test_evidence_emitter_rejects_unprescribed_fields(self):
        arp = AuditRequirementPackage(
            "ARP-1", "JOB-1", binding("CONTRACT"), ("job_ref", "terminal_state"), (), ()
        )
        emitter = EvidenceEmitter(arp)
        submission = emitter.emit(
            submission_ref="SUBMISSION-1",
            job_ref="JOB-1",
            evidence={"job_ref": "JOB-1", "terminal_state": "NOT_DEPLOYED"},
        )
        self.assertEqual(len(submission.payload_sha256), 64)
        with self.assertRaisesRegex(ContractError, "UNPRESCRIBED"):
            emitter.emit(
                submission_ref="SUBMISSION-2",
                job_ref="JOB-1",
                evidence={"job_ref": "JOB-1", "terminal_state": "FAILED", "invented": True},
            )

    def test_vault_manifest_verifies_exact_file_set_and_hashes(self):
        material = {"src/module.py": b"content"}
        digest = hashlib.sha256(material["src/module.py"]).hexdigest()
        manifest = CandidatePackageManifest("PKG-1", None, HASH, (FileDigest("src/module.py", digest),))
        manifest.verify(material)
        with self.assertRaisesRegex(ContractError, "HASH_MISMATCH"):
            manifest.verify({"src/module.py": b"changed"})

    def test_toolsmith_cannot_package_quality_or_mint_outputs(self):
        with self.assertRaisesRegex(ContractError, "PROTECTED_VAULT_RESULT"):
            FileDigest("artifacts/quality-result.json", HASH)


if __name__ == "__main__":
    unittest.main()
