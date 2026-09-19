from __future__ import annotations

from dataclasses import dataclass
import hashlib

from .contracts import ContractError


@dataclass(frozen=True)
class AuditEnvelope:
    envelope_ref: str
    sender_ref: str
    audit_destination_ref: str
    evidence_submission_ref: str
    evidence_sha256: str
    home_commentary_ref: str | None
    commentary_sha256: str | None

    @property
    def correlation_sha256(self) -> str:
        material = "\x1f".join(
            (
                self.envelope_ref,
                self.sender_ref,
                self.audit_destination_ref,
                self.evidence_submission_ref,
                self.evidence_sha256,
                self.home_commentary_ref or "",
                self.commentary_sha256 or "",
            )
        )
        return hashlib.sha256(material.encode("utf-8")).hexdigest()

    def __post_init__(self) -> None:
        if bool(self.home_commentary_ref) != bool(self.commentary_sha256):
            raise ContractError("COMMENTARY_REFERENCE_AND_HASH_MUST_TRAVEL_TOGETHER")
        for digest in (self.evidence_sha256, self.commentary_sha256):
            if digest is not None and (len(digest) != 64 or any(c not in "0123456789abcdef" for c in digest)):
                raise ContractError("INVALID_PAYLOAD_SHA256")


def correlate_receipt(envelope: AuditEnvelope, returned_sha256: str) -> str:
    if returned_sha256 != envelope.correlation_sha256:
        raise ContractError("POST_OFFICE_RECEIPT_CORRELATION_MISMATCH")
    return "DELIVERED_CORRELATED"

