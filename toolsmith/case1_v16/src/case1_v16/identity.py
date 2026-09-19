from __future__ import annotations

from dataclasses import dataclass
import hashlib
import re
from typing import Mapping

from .contracts import ContractError


@dataclass(frozen=True)
class GrammarContract:
    """Owner-supplied grammar. The Toolsmith does not choose its semantics."""

    contract_ref: str
    contract_sha256: str
    literal_prefix: str
    delimiter: str
    ordered_fields: tuple[str, ...]
    component_pattern: str
    maximum_length: int

    def __post_init__(self) -> None:
        if not self.contract_ref or len(self.contract_sha256) != 64:
            raise ContractError("INVALID_GRAMMAR_CONTRACT_BINDING")
        if not self.literal_prefix or not self.delimiter or not self.ordered_fields:
            raise ContractError("INCOMPLETE_GRAMMAR_CONTRACT")
        if "cardinal" not in self.ordered_fields:
            raise ContractError("GRAMMAR_MUST_INCLUDE_CARDINAL")
        if self.maximum_length < 1:
            raise ContractError("INVALID_GRAMMAR_MAXIMUM_LENGTH")
        re.compile(self.component_pattern)


@dataclass(frozen=True)
class CompiledCandidate:
    candidate_class: str
    grammar_contract_ref: str
    grammar_contract_sha256: str
    cardinal: int
    candidate_material: str

    @property
    def candidate_sha256(self) -> str:
        return hashlib.sha256(self.candidate_material.encode("utf-8")).hexdigest()


class CandidateIdentityCompiler:
    """Pure pre-entry compiler. It has no destination client or write method."""

    def __init__(self, grammar: GrammarContract) -> None:
        self.grammar = grammar
        self._component = re.compile(grammar.component_pattern)

    def compile(self, values: Mapping[str, str | int]) -> CompiledCandidate:
        if set(values) != set(self.grammar.ordered_fields):
            missing = sorted(set(self.grammar.ordered_fields) - set(values))
            extra = sorted(set(values) - set(self.grammar.ordered_fields))
            raise ContractError(f"GRAMMAR_FIELD_MISMATCH:missing={missing}:extra={extra}")
        cardinal = values["cardinal"]
        if not isinstance(cardinal, int) or cardinal < 1:
            raise ContractError("CARDINAL_MUST_BEGIN_AT_ONE")
        components = []
        for name in self.grammar.ordered_fields:
            component = str(values[name])
            if not self._component.fullmatch(component):
                raise ContractError(f"INVALID_GRAMMAR_COMPONENT:{name}")
            components.append(component)
        candidate = self.grammar.delimiter.join((self.grammar.literal_prefix, *components))
        if len(candidate.encode("utf-8")) > self.grammar.maximum_length:
            raise ContractError("CANDIDATE_IDENTITY_TOO_LONG")
        return CompiledCandidate(
            candidate_class="CANDIDATE_IDENTITY_MATERIAL",
            grammar_contract_ref=self.grammar.contract_ref,
            grammar_contract_sha256=self.grammar.contract_sha256,
            cardinal=cardinal,
            candidate_material=candidate,
        )


class HistoricalIdentityDecoder:
    def __init__(self, contracts: Mapping[str, GrammarContract]) -> None:
        self.contracts = dict(contracts)

    def decode(self, identity: str, contract_ref: str) -> dict[str, str]:
        try:
            grammar = self.contracts[contract_ref]
        except KeyError as exc:
            raise ContractError("UNKNOWN_HISTORICAL_GRAMMAR") from exc
        parts = identity.split(grammar.delimiter)
        if len(parts) != len(grammar.ordered_fields) + 1 or parts[0] != grammar.literal_prefix:
            raise ContractError("IDENTITY_DOES_NOT_MATCH_BOUND_GRAMMAR")
        return {
            "contract_ref": grammar.contract_ref,
            "contract_sha256": grammar.contract_sha256,
            **dict(zip(grammar.ordered_fields, parts[1:], strict=True)),
        }

