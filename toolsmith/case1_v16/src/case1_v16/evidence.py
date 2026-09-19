from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping

from .contracts import AuditRequirementPackage, ContractError, canonical_sha256


@dataclass(frozen=True)
class EvidenceSubmission:
    submission_ref: str
    requirement_ref: str
    job_ref: str
    payload: Mapping[str, Any]
    payload_sha256: str


class EvidenceEmitter:
    """Emits only prespecified Audit fields; it does not adjudicate them."""

    def __init__(self, requirements: AuditRequirementPackage) -> None:
        self.requirements = requirements

    def emit(self, *, submission_ref: str, job_ref: str, evidence: Mapping[str, Any]) -> EvidenceSubmission:
        if not submission_ref:
            raise ContractError("EVIDENCE_SUBMISSION_REFERENCE_REQUIRED")
        if job_ref != self.requirements.job_ref:
            raise ContractError("EVIDENCE_JOB_REQUIREMENT_MISMATCH")
        self.requirements.validate_evidence(evidence)
        admitted = set(self.requirements.required_fields)
        unexpected = sorted(set(evidence) - admitted)
        if unexpected:
            raise ContractError("AUDIT_EVIDENCE_UNPRESCRIBED:" + ",".join(unexpected))
        payload = dict(evidence)
        digest = canonical_sha256(payload)
        return EvidenceSubmission(
            submission_ref=submission_ref,
            requirement_ref=self.requirements.requirement_ref,
            job_ref=job_ref,
            payload=payload,
            payload_sha256=digest,
        )


@dataclass(frozen=True)
class HomeCommentary:
    commentary_ref: str
    job_ref: str
    text: str

    def __post_init__(self) -> None:
        if not self.commentary_ref or not self.job_ref or not self.text:
            raise ContractError("HOME_COMMENTARY_REQUIRES_SEPARATE_REFERENCE_JOB_AND_TEXT")

