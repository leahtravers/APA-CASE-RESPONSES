from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from .contracts import CandidatePacket, ContractError, DestinationResult, VersionBinding


class DestinationGateway(Protocol):
    """Owner-implemented interface. This candidate package never invokes it."""

    contract: VersionBinding

    def submit(self, packet: CandidatePacket) -> DestinationResult:
        ...


@dataclass(frozen=True)
class DestinationResultValidator:
    contract: VersionBinding

    def validate(self, packet: CandidatePacket, result: DestinationResult) -> None:
        if packet.destination_contract != self.contract:
            raise ContractError("DESTINATION_CONTRACT_BINDING_MISMATCH")
        result.validate_against(packet)


def direct_write(*_args: object, **_kwargs: object) -> None:
    raise ContractError("DIRECT_DESTINATION_WRITE_PROHIBITED_USE_OWNER_GATEWAY")

