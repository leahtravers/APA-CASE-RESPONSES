from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone

from .contracts import (
    CandidatePacket,
    ContractError,
    LicenseState,
    PolicyState,
    VersionBinding,
)


def _aware_utc(value: datetime, name: str) -> datetime:
    if value.tzinfo is None or value.utcoffset() is None:
        raise ContractError(f"{name}_MUST_BE_TIMEZONE_AWARE")
    return value.astimezone(timezone.utc)


@dataclass(frozen=True)
class DispatchAuthority:
    """Exact pre-dispatch bindings; validation never activates an authority."""

    manifest: VersionBinding
    reservation: VersionBinding
    reservation_manifest: VersionBinding
    policy: VersionBinding
    policy_state: PolicyState
    policy_expires_at: datetime
    license: VersionBinding
    license_state: LicenseState
    license_policy: VersionBinding
    license_manifest: VersionBinding
    license_expires_at: datetime
    audit_requirements: VersionBinding
    destination_contract: VersionBinding
    queue_position: int
    capacity_bound: int

    def validate(self, packet: CandidatePacket, *, at: datetime) -> None:
        now = _aware_utc(at, "VALIDATION_TIME")
        policy_expiry = _aware_utc(self.policy_expires_at, "POLICY_EXPIRY")
        license_expiry = _aware_utc(self.license_expires_at, "LICENSE_EXPIRY")

        exact = {
            "manifest": (self.manifest, packet.manifest),
            "reservation": (self.reservation, packet.reservation),
            "policy": (self.policy, packet.policy),
            "license": (self.license, packet.license),
            "audit_requirements": (self.audit_requirements, packet.audit_requirements),
            "destination_contract": (self.destination_contract, packet.destination_contract),
            "reservation_manifest": (self.reservation_manifest, self.manifest),
            "license_policy": (self.license_policy, self.policy),
            "license_manifest": (self.license_manifest, self.manifest),
        }
        mismatched = [name for name, (actual, expected) in exact.items() if actual != expected]
        if mismatched:
            raise ContractError("AUTHORITY_BINDING_MISMATCH:" + ",".join(sorted(mismatched)))
        if self.policy_state is not PolicyState.EFFECTIVE:
            raise ContractError(f"POLICY_NOT_EFFECTIVE:{self.policy_state.value}")
        if self.license_state is not LicenseState.ACTIVE:
            raise ContractError(f"LICENSE_NOT_ACTIVE:{self.license_state.value}")
        if now >= policy_expiry:
            raise ContractError("POLICY_EXPIRED_OR_STALE")
        if now >= license_expiry or license_expiry > policy_expiry:
            raise ContractError("LICENSE_EXPIRED_OR_OUTLIVES_POLICY")
        if self.queue_position < 1 or self.capacity_bound < 1:
            raise ContractError("QUEUE_AND_CAPACITY_REQUIRE_POSITIVE_NUMERIC_BOUNDS")

