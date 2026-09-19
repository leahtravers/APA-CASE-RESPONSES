from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

from .contracts import ContractError, VersionBinding


def _aware_utc(value: datetime, name: str) -> datetime:
    if value.tzinfo is None or value.utcoffset() is None:
        raise ContractError(f"{name}_MUST_BE_TIMEZONE_AWARE")
    return value.astimezone(timezone.utc)


@dataclass(frozen=True)
class QueueEntry:
    job_ref: str
    attempt_ref: str
    endpoint_ref: str
    manifest: VersionBinding
    reservation: VersionBinding
    policy: VersionBinding
    license: VersionBinding
    packet: VersionBinding
    destination_contract: VersionBinding
    audit_requirements: VersionBinding
    source_versions_sha256: str
    queue_position: int
    capacity_bound: int

    def __post_init__(self) -> None:
        if not all((self.job_ref, self.attempt_ref, self.endpoint_ref)):
            raise ContractError("QUEUE_ENTRY_REQUIRES_JOB_ATTEMPT_ENDPOINT")
        if self.queue_position < 1 or self.capacity_bound < 1:
            raise ContractError("QUEUE_AND_CAPACITY_REQUIRE_POSITIVE_NUMERIC_BOUNDS")
        if len(self.source_versions_sha256) != 64 or any(
            c not in "0123456789abcdef" for c in self.source_versions_sha256
        ):
            raise ContractError("INVALID_SOURCE_VERSIONS_SHA256")


@dataclass(frozen=True)
class EndpointLease:
    endpoint_ref: str
    job_ref: str
    attempt_ref: str
    state: str = "HELD"


class EndpointCustody:
    """Pure in-memory contract model; it contains no dispatcher or gateway client."""

    def __init__(self) -> None:
        self._holders: dict[str, EndpointLease] = {}

    def acquire(self, entry: QueueEntry) -> EndpointLease:
        if entry.endpoint_ref in self._holders:
            raise ContractError("ENDPOINT_ALREADY_HELD")
        lease = EndpointLease(entry.endpoint_ref, entry.job_ref, entry.attempt_ref)
        self._holders[entry.endpoint_ref] = lease
        return lease

    def release(self, lease: EndpointLease) -> EndpointLease:
        current = self._holders.get(lease.endpoint_ref)
        if current != lease:
            raise ContractError("ENDPOINT_RELEASE_HOLDER_MISMATCH")
        del self._holders[lease.endpoint_ref]
        return EndpointLease(lease.endpoint_ref, lease.job_ref, lease.attempt_ref, "RELEASED")


@dataclass(frozen=True)
class UncertaintyWindow:
    job_ref: str
    attempt_ref: str
    opened_at: datetime
    deadline: datetime
    action: str = "READBACK_RECONCILIATION_REQUIRED_NO_REPLAY"

    def requires_escalation(self, *, at: datetime) -> bool:
        return _aware_utc(at, "CHECK_TIME") >= self.deadline


def open_uncertainty(
    *,
    job_ref: str,
    attempt_ref: str,
    opened_at: datetime,
    contract_deadline: datetime | None = None,
) -> UncertaintyWindow:
    opened = _aware_utc(opened_at, "UNCERTAINTY_OPENED_AT")
    maximum = opened + timedelta(minutes=15)
    deadline = maximum
    if contract_deadline is not None:
        bounded = _aware_utc(contract_deadline, "CONTRACT_DEADLINE")
        if bounded <= opened:
            raise ContractError("UNCERTAINTY_DEADLINE_MUST_FOLLOW_OPENING")
        deadline = min(maximum, bounded)
    return UncertaintyWindow(job_ref, attempt_ref, opened, deadline)


def assert_no_replay(*, uncertain_attempt_ref: str, proposed_attempt_ref: str) -> None:
    if uncertain_attempt_ref == proposed_attempt_ref:
        raise ContractError("UNCERTAIN_ATTEMPT_CANNOT_BE_REPLAYED")

