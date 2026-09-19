from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
import hashlib
import json
from typing import Any, Iterable, Mapping


class ContractError(ValueError):
    """Fail-closed contract validation error."""


class CardinalOutcome(str, Enum):
    WRITTEN = "WRITTEN"
    REJECTED_BEFORE_WRITE = "REJECTED_BEFORE_WRITE"
    UNCERTAIN = "UNCERTAIN"


class JobState(str, Enum):
    DRAFT = "DRAFT"
    CONTRACTED = "CONTRACTED"
    MANIFESTED = "MANIFESTED"
    AUDIT_REQUIREMENTS_ASSIGNED = "AUDIT_REQUIREMENTS_ASSIGNED"
    RESERVED = "RESERVED"
    POLICY_BOUND = "POLICY_BOUND"
    LICENSED = "LICENSED"
    QUEUED = "QUEUED"
    ENDPOINT_HELD = "ENDPOINT_HELD"
    EXECUTING = "EXECUTING"
    OUTCOME_RECONCILING = "OUTCOME_RECONCILING"
    COMPLETED = "COMPLETED"
    PARTIAL = "PARTIAL"
    FAILED_AFTER_WRITE = "FAILED_AFTER_WRITE"
    REJECTED_BEFORE_WRITE = "REJECTED_BEFORE_WRITE"
    NOT_DEPLOYED = "NOT_DEPLOYED"
    UNCERTAIN = "UNCERTAIN"


class PolicyState(str, Enum):
    DRAFT = "DRAFT"
    SECURITY_ACCEPTED = "SECURITY_ACCEPTED"
    EFFECTIVE = "EFFECTIVE"
    SUSPENDED = "SUSPENDED"
    WITHDRAWN = "WITHDRAWN"
    SUPERSEDED = "SUPERSEDED"
    EXPIRED = "EXPIRED"


class LicenseState(str, Enum):
    REQUESTED = "REQUESTED"
    POLICY_BOUND = "POLICY_BOUND"
    RESERVED = "RESERVED"
    ACTIVE = "ACTIVE"
    CONSUMED = "CONSUMED"
    EXPIRED = "EXPIRED"
    SUSPENDED = "SUSPENDED"
    REVOKED = "REVOKED"
    NOT_ISSUED = "NOT_ISSUED"


TERMINAL_JOB_STATES = {
    JobState.COMPLETED,
    JobState.PARTIAL,
    JobState.FAILED_AFTER_WRITE,
    JobState.REJECTED_BEFORE_WRITE,
    JobState.NOT_DEPLOYED,
    JobState.UNCERTAIN,
}


def canonical_sha256(value: Mapping[str, Any]) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def require_ref(name: str, value: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ContractError(f"MISSING_REQUIRED_REFERENCE:{name}")
    return value.strip()


@dataclass(frozen=True)
class VersionBinding:
    ref: str
    sha256: str

    def __post_init__(self) -> None:
        require_ref("version_ref", self.ref)
        if len(self.sha256) != 64 or any(c not in "0123456789abcdef" for c in self.sha256):
            raise ContractError("INVALID_SHA256")


@dataclass(frozen=True)
class CandidateCardinal:
    cardinal: int
    candidate_material: str = field(repr=False)

    def __post_init__(self) -> None:
        if self.cardinal < 1:
            raise ContractError("CARDINAL_MUST_BEGIN_AT_ONE")
        require_ref("candidate_material", self.candidate_material)

    @property
    def digest(self) -> str:
        return hashlib.sha256(self.candidate_material.encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class CandidatePacket:
    packet_ref: str
    attempt_ref: str
    job_ref: str
    manifest: VersionBinding
    reservation: VersionBinding
    policy: VersionBinding
    license: VersionBinding
    destination_contract: VersionBinding
    audit_requirements: VersionBinding
    compiler: VersionBinding
    cardinals: tuple[CandidateCardinal, ...]

    def __post_init__(self) -> None:
        for name in ("packet_ref", "attempt_ref", "job_ref"):
            require_ref(name, getattr(self, name))
        if not self.cardinals:
            raise ContractError("EMPTY_CANDIDATE_PACKET")
        actual = tuple(item.cardinal for item in self.cardinals)
        expected = tuple(range(1, len(self.cardinals) + 1))
        if actual != expected:
            raise ContractError("CARDINALS_MUST_BE_CONTIGUOUS_1_TO_N")

    @property
    def package_sha256(self) -> str:
        return canonical_sha256(
            {
                "packet_ref": self.packet_ref,
                "attempt_ref": self.attempt_ref,
                "job_ref": self.job_ref,
                "manifest": self.manifest.__dict__,
                "reservation": self.reservation.__dict__,
                "policy": self.policy.__dict__,
                "license": self.license.__dict__,
                "destination_contract": self.destination_contract.__dict__,
                "audit_requirements": self.audit_requirements.__dict__,
                "compiler": self.compiler.__dict__,
                "cardinals": [
                    {"cardinal": item.cardinal, "digest": item.digest}
                    for item in self.cardinals
                ],
            }
        )


@dataclass(frozen=True)
class CardinalResult:
    cardinal: int
    outcome: CardinalOutcome
    written_identity_ref: str | None = None
    destination_proof_ref: str | None = None
    error_class: str | None = None

    def __post_init__(self) -> None:
        if self.cardinal < 1:
            raise ContractError("INVALID_RESULT_CARDINAL")
        if self.outcome is CardinalOutcome.WRITTEN:
            require_ref("written_identity_ref", self.written_identity_ref or "")
            require_ref("destination_proof_ref", self.destination_proof_ref or "")
        elif self.written_identity_ref is not None:
            raise ContractError("UNWRITTEN_CARDINAL_CANNOT_HAVE_ACTIVE_IDENTITY")
        if self.outcome is CardinalOutcome.UNCERTAIN and not self.destination_proof_ref:
            raise ContractError("UNCERTAIN_REQUIRES_RECONCILIATION_REFERENCE")


@dataclass(frozen=True)
class DestinationResult:
    packet_ref: str
    attempt_ref: str
    results: tuple[CardinalResult, ...]

    def __post_init__(self) -> None:
        require_ref("packet_ref", self.packet_ref)
        require_ref("attempt_ref", self.attempt_ref)
        actual = tuple(item.cardinal for item in self.results)
        expected = tuple(range(1, len(self.results) + 1))
        if actual != expected:
            raise ContractError("RESULT_CARDINALS_MUST_BE_CONTIGUOUS_1_TO_N")

    def validate_against(self, packet: CandidatePacket) -> None:
        if self.packet_ref != packet.packet_ref or self.attempt_ref != packet.attempt_ref:
            raise ContractError("RESULT_PACKET_OR_ATTEMPT_MISMATCH")
        if len(self.results) != len(packet.cardinals):
            raise ContractError("RESULT_CARDINALITY_MISMATCH")

    @property
    def written(self) -> tuple[int, ...]:
        return tuple(r.cardinal for r in self.results if r.outcome is CardinalOutcome.WRITTEN)

    @property
    def unwritten(self) -> tuple[int, ...]:
        return tuple(r.cardinal for r in self.results if r.outcome is not CardinalOutcome.WRITTEN)

    @property
    def terminal_state(self) -> JobState:
        outcomes = {r.outcome for r in self.results}
        if CardinalOutcome.UNCERTAIN in outcomes:
            return JobState.UNCERTAIN
        if outcomes == {CardinalOutcome.WRITTEN}:
            return JobState.COMPLETED
        if CardinalOutcome.WRITTEN in outcomes:
            return JobState.PARTIAL
        return JobState.REJECTED_BEFORE_WRITE


@dataclass(frozen=True)
class AuditRequirementPackage:
    requirement_ref: str
    job_ref: str
    contract: VersionBinding
    required_fields: tuple[str, ...]
    prohibited_fields: tuple[str, ...]
    redaction_rules: tuple[str, ...]

    def __post_init__(self) -> None:
        require_ref("requirement_ref", self.requirement_ref)
        require_ref("job_ref", self.job_ref)
        if not self.required_fields:
            raise ContractError("AUDIT_REQUIREMENTS_EMPTY")
        overlap = set(self.required_fields).intersection(self.prohibited_fields)
        if overlap:
            raise ContractError("AUDIT_REQUIRED_PROHIBITED_OVERLAP:" + ",".join(sorted(overlap)))

    def validate_evidence(self, evidence: Mapping[str, Any]) -> None:
        missing = [field for field in self.required_fields if field not in evidence]
        prohibited = [field for field in self.prohibited_fields if field in evidence]
        if missing:
            raise ContractError("AUDIT_EVIDENCE_MISSING:" + ",".join(missing))
        if prohibited:
            raise ContractError("AUDIT_EVIDENCE_PROHIBITED:" + ",".join(prohibited))


def assert_new_attempt(predecessor: CandidatePacket, successor: CandidatePacket) -> None:
    if predecessor.attempt_ref == successor.attempt_ref:
        raise ContractError("RETRY_MUST_USE_NEW_ATTEMPT")
    if predecessor.packet_ref == successor.packet_ref:
        raise ContractError("RETRY_MUST_USE_NEW_PACKET")
    predecessor_digests = {item.digest for item in predecessor.cardinals}
    successor_digests = {item.digest for item in successor.cardinals}
    if predecessor_digests.intersection(successor_digests):
        raise ContractError("RETRY_CANNOT_REUSE_CANDIDATE_MATERIAL")


def cardinal_set(values: Iterable[int]) -> tuple[int, ...]:
    return tuple(sorted(set(values)))

