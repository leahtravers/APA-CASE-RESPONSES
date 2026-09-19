from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import hmac
from typing import Any, Mapping

from .contracts import (
    AuditRequirementPackage,
    CandidatePacket,
    CardinalOutcome,
    ContractError,
    DestinationResult,
)


@dataclass(frozen=True)
class DispositionTombstone:
    disposition_ref: str
    job_ref: str
    attempt_ref: str
    packet_ref: str
    package_sha256: str
    hmac_key_ref: str
    hmac_sha256: str
    planned_cardinals: tuple[int, ...]
    written_cardinals: tuple[int, ...]
    unwritten_cardinals: tuple[int, ...]
    outcome: str
    reason: str
    destruction_attestation_ref: str
    audit_requirement_ref: str
    created_at: str
    predecessor_ref: str | None = None

    def as_evidence(self) -> dict[str, Any]:
        return self.__dict__.copy()


def reconcile_destination(packet: CandidatePacket, result: DestinationResult) -> dict[str, Any]:
    result.validate_against(packet)
    if any(item.outcome is CardinalOutcome.UNCERTAIN for item in result.results):
        next_action = "READBACK_RECONCILIATION_REQUIRED_NO_REPLAY"
    else:
        next_action = "DESTROY_UNWRITTEN_AND_FILE_TOMBSTONE"
    return {
        "packet_ref": packet.packet_ref,
        "attempt_ref": packet.attempt_ref,
        "package_sha256": packet.package_sha256,
        "planned_cardinals": tuple(item.cardinal for item in packet.cardinals),
        "written_cardinals": result.written,
        "unwritten_cardinals": result.unwritten,
        "terminal_state": result.terminal_state.value,
        "next_action": next_action,
    }


def build_tombstone(
    *,
    packet: CandidatePacket,
    result: DestinationResult,
    disposition_ref: str,
    hmac_key_ref: str,
    hmac_key: bytes,
    destruction_attestation_ref: str,
    reason: str,
    predecessor_ref: str | None = None,
) -> DispositionTombstone:
    reconciliation = reconcile_destination(packet, result)
    if reconciliation["next_action"].startswith("READBACK"):
        raise ContractError("UNCERTAIN_MUST_BE_RECONCILED_BEFORE_DESTRUCTION")
    unwritten = set(result.unwritten)
    digest_input = b"\x1f".join(
        item.candidate_material.encode("utf-8")
        for item in packet.cardinals
        if item.cardinal in unwritten
    )
    digest = hmac.new(hmac_key, digest_input, hashlib.sha256).hexdigest()
    return DispositionTombstone(
        disposition_ref=disposition_ref,
        job_ref=packet.job_ref,
        attempt_ref=packet.attempt_ref,
        packet_ref=packet.packet_ref,
        package_sha256=packet.package_sha256,
        hmac_key_ref=hmac_key_ref,
        hmac_sha256=digest,
        planned_cardinals=reconciliation["planned_cardinals"],
        written_cardinals=reconciliation["written_cardinals"],
        unwritten_cardinals=reconciliation["unwritten_cardinals"],
        outcome=reconciliation["terminal_state"],
        reason=reason,
        destruction_attestation_ref=destruction_attestation_ref,
        audit_requirement_ref=packet.audit_requirements.ref,
        created_at=datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        predecessor_ref=predecessor_ref,
    )


def compile_audit_evidence(
    requirements: AuditRequirementPackage,
    evidence: Mapping[str, Any],
) -> dict[str, Any]:
    requirements.validate_evidence(evidence)
    material = dict(evidence)
    material["audit_requirement_ref"] = requirements.requirement_ref
    return material


def logging_projection(
    *,
    audit_evidence: Mapping[str, Any],
    allowed_fields: tuple[str, ...],
    requisition_ref: str,
    criterion_ref: str,
) -> dict[str, Any]:
    if not requisition_ref or not criterion_ref:
        raise ContractError("LOGGING_REQUIRES_OPEN_REQUISITION_AND_CRITERION")
    return {
        "requisition_ref": requisition_ref,
        "criterion_ref": criterion_ref,
        "surfaced": {name: audit_evidence[name] for name in allowed_fields if name in audit_evidence},
    }

