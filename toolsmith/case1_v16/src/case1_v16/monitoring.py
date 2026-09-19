from __future__ import annotations

from dataclasses import dataclass

from .contracts import ContractError


@dataclass(frozen=True)
class Criterion:
    ref: str
    name: str
    severity: str
    logging_rule: str


CRITERIA = {
    c.ref: c
    for c in (
        Criterion("MON-V16-01", "authority drift", "CRITICAL", "OPEN_IMMEDIATELY"),
        Criterion("MON-V16-02", "missing audit package", "CRITICAL", "OPEN_IMMEDIATELY"),
        Criterion("MON-V16-03", "evidence incompleteness", "HIGH", "AFTER_AUDIT_CONFIRMATION"),
        Criterion("MON-V16-04", "identity-state mismatch", "CRITICAL", "OPEN_RESTRICTED_FIELDS"),
        Criterion("MON-V16-05", "endpoint exclusivity breach", "CRITICAL", "OPEN_IMMEDIATELY"),
        Criterion("MON-V16-06", "policy-license mismatch", "CRITICAL", "OPEN_IMMEDIATELY"),
        Criterion("MON-V16-07", "retry or reuse breach", "CRITICAL", "OPEN_IMMEDIATELY"),
        Criterion("MON-V16-08", "queue or capacity degradation", "MEDIUM", "AFTER_THRESHOLD"),
        Criterion("MON-V16-09", "Post Office failure", "HIGH", "AFTER_SELF_RECOVERY_FAILS"),
        Criterion("MON-V16-10", "vault drift", "CRITICAL", "OPEN_IMMEDIATELY"),
        Criterion("MON-V16-11", "quality-gate bypass", "CRITICAL", "OPEN_IMMEDIATELY"),
        Criterion("MON-V16-12", "unresolved uncertainty", "HIGH", "AT_WINDOW_EXPIRY"),
        Criterion("MON-V16-13", "security incident", "CRITICAL", "OPEN_SECURITY_SAFE_FIELDS"),
        Criterion("MON-V16-14", "repeated nondeployment", "MEDIUM", "OPEN_AS_TREND"),
    )
}


def record_match(*, criterion_ref: str, evidence_ref: str, owner_ref: str, recipient_ref: str) -> dict[str, str]:
    try:
        criterion = CRITERIA[criterion_ref]
    except KeyError as exc:
        raise ContractError("UNKNOWN_MONITORING_CRITERION") from exc
    if not all((evidence_ref, owner_ref, recipient_ref)):
        raise ContractError("MONITORING_MATCH_REQUIRES_BOUNDED_REFERENCES")
    return {
        "criterion_ref": criterion.ref,
        "criterion_name": criterion.name,
        "severity": criterion.severity,
        "logging_rule": criterion.logging_rule,
        "evidence_ref": evidence_ref,
        "owner_ref": owner_ref,
        "recipient_ref": recipient_ref,
        "state": "MATCHED",
    }

