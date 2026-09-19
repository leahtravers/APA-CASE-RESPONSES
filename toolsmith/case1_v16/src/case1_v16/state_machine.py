from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Generic, Mapping, TypeVar

from .contracts import ContractError, JobState, LicenseState, PolicyState, TERMINAL_JOB_STATES


StateT = TypeVar("StateT", bound=Enum)


@dataclass(frozen=True)
class Transition(Generic[StateT]):
    predecessor: StateT
    successor: StateT
    authority_ref: str
    evidence_ref: str


class StateMachine(Generic[StateT]):
    def __init__(self, allowed: Mapping[StateT, set[StateT]]) -> None:
        self.allowed = {key: frozenset(value) for key, value in allowed.items()}

    def transition(self, current: StateT, successor: StateT, *, authority_ref: str, evidence_ref: str) -> Transition[StateT]:
        if not authority_ref or not evidence_ref:
            raise ContractError("TRANSITION_REQUIRES_AUTHORITY_AND_EVIDENCE")
        if successor not in self.allowed.get(current, frozenset()):
            raise ContractError(f"INVALID_STATE_TRANSITION:{current.value}->{successor.value}")
        return Transition(current, successor, authority_ref, evidence_ref)


JOB_MACHINE = StateMachine(
    {
        JobState.DRAFT: {JobState.CONTRACTED},
        JobState.CONTRACTED: {JobState.MANIFESTED},
        JobState.MANIFESTED: {JobState.AUDIT_REQUIREMENTS_ASSIGNED},
        JobState.AUDIT_REQUIREMENTS_ASSIGNED: {JobState.RESERVED, JobState.NOT_DEPLOYED},
        JobState.RESERVED: {JobState.POLICY_BOUND, JobState.NOT_DEPLOYED},
        JobState.POLICY_BOUND: {JobState.LICENSED, JobState.NOT_DEPLOYED},
        JobState.LICENSED: {JobState.QUEUED, JobState.NOT_DEPLOYED},
        JobState.QUEUED: {JobState.ENDPOINT_HELD, JobState.NOT_DEPLOYED},
        JobState.ENDPOINT_HELD: {JobState.EXECUTING, JobState.NOT_DEPLOYED},
        JobState.EXECUTING: {JobState.OUTCOME_RECONCILING},
        JobState.OUTCOME_RECONCILING: set(TERMINAL_JOB_STATES - {JobState.NOT_DEPLOYED}),
    }
)

POLICY_MACHINE = StateMachine(
    {
        PolicyState.DRAFT: {PolicyState.SECURITY_ACCEPTED, PolicyState.WITHDRAWN},
        PolicyState.SECURITY_ACCEPTED: {PolicyState.EFFECTIVE, PolicyState.WITHDRAWN},
        PolicyState.EFFECTIVE: {PolicyState.SUSPENDED, PolicyState.WITHDRAWN, PolicyState.SUPERSEDED, PolicyState.EXPIRED},
        PolicyState.SUSPENDED: {PolicyState.EFFECTIVE, PolicyState.WITHDRAWN, PolicyState.SUPERSEDED, PolicyState.EXPIRED},
    }
)

LICENSE_MACHINE = StateMachine(
    {
        LicenseState.REQUESTED: {LicenseState.POLICY_BOUND, LicenseState.NOT_ISSUED},
        LicenseState.POLICY_BOUND: {LicenseState.RESERVED, LicenseState.NOT_ISSUED},
        LicenseState.RESERVED: {LicenseState.ACTIVE, LicenseState.EXPIRED, LicenseState.SUSPENDED, LicenseState.REVOKED},
        LicenseState.ACTIVE: {LicenseState.CONSUMED, LicenseState.EXPIRED, LicenseState.SUSPENDED, LicenseState.REVOKED},
        LicenseState.SUSPENDED: {LicenseState.ACTIVE, LicenseState.EXPIRED, LicenseState.REVOKED},
    }
)

