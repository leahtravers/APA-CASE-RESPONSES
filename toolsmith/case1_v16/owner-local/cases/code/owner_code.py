from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

OWNER = "APA_CASES"
INTERFACE_VERSION = "CASE1-V16-OWNER-BOUNDARY-0001"


class ContractError(ValueError):
    pass


class CardinalOutcome(str, Enum):
    WRITTEN = "WRITTEN"
    REJECTED_BEFORE_WRITE = "REJECTED_BEFORE_WRITE"
    UNCERTAIN = "UNCERTAIN"


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
            if not self.written_identity_ref or not self.destination_proof_ref:
                raise ContractError("WRITTEN_REQUIRES_IDENTITY_AND_DESTINATION_PROOF")
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
        expected = tuple(range(1, len(self.results) + 1))
        if tuple(item.cardinal for item in self.results) != expected:
            raise ContractError("RESULT_CARDINALS_MUST_BE_CONTIGUOUS_1_TO_N")

    def validate(self, *, packet_ref: str, attempt_ref: str, cardinal_count: int) -> None:
        if self.packet_ref != packet_ref or self.attempt_ref != attempt_ref:
            raise ContractError("RESULT_PACKET_OR_ATTEMPT_MISMATCH")
        if len(self.results) != cardinal_count:
            raise ContractError("RESULT_CARDINALITY_MISMATCH")


def terminal_state(result: DestinationResult) -> str:
    outcomes = {item.outcome for item in result.results}
    if CardinalOutcome.UNCERTAIN in outcomes:
        return "UNCERTAIN"
    if outcomes == {CardinalOutcome.WRITTEN}:
        return "COMPLETED"
    if CardinalOutcome.WRITTEN in outcomes:
        return "PARTIAL"
    return "REJECTED_BEFORE_WRITE"


def direct_write(*_args: object, **_kwargs: object) -> None:
    raise ContractError("DIRECT_DESTINATION_WRITE_PROHIBITED_USE_OWNER_GATEWAY")
