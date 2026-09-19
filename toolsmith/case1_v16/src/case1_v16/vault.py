from __future__ import annotations

from dataclasses import dataclass
import hashlib
from typing import Mapping

from .contracts import ContractError, canonical_sha256


PROTECTED_VAULT_OUTPUTS = (
    "quality-result",
    "quality_result",
    "mint-record",
    "mint_record",
    "action-copy",
    "action_copy",
)


@dataclass(frozen=True)
class FileDigest:
    path: str
    sha256: str

    def __post_init__(self) -> None:
        if not self.path or self.path.startswith("/") or ".." in self.path.split("/"):
            raise ContractError("INVALID_PACKAGE_PATH")
        if len(self.sha256) != 64 or any(c not in "0123456789abcdef" for c in self.sha256):
            raise ContractError("INVALID_PACKAGE_FILE_SHA256")
        lowered = self.path.lower()
        if any(name in lowered for name in PROTECTED_VAULT_OUTPUTS):
            raise ContractError("TOOLSMITH_CANNOT_PACKAGE_PROTECTED_VAULT_RESULT")


@dataclass(frozen=True)
class CandidatePackageManifest:
    package_ref: str
    predecessor_ref: str | None
    dependency_lock_sha256: str
    files: tuple[FileDigest, ...]

    def __post_init__(self) -> None:
        if not self.package_ref or not self.files:
            raise ContractError("INCOMPLETE_CANDIDATE_PACKAGE_MANIFEST")
        if len({item.path for item in self.files}) != len(self.files):
            raise ContractError("DUPLICATE_CANDIDATE_PACKAGE_PATH")
        if len(self.dependency_lock_sha256) != 64 or any(
            c not in "0123456789abcdef" for c in self.dependency_lock_sha256
        ):
            raise ContractError("INVALID_DEPENDENCY_LOCK_SHA256")

    @property
    def manifest_sha256(self) -> str:
        return canonical_sha256(
            {
                "package_ref": self.package_ref,
                "predecessor_ref": self.predecessor_ref,
                "dependency_lock_sha256": self.dependency_lock_sha256,
                "files": [item.__dict__ for item in sorted(self.files, key=lambda item: item.path)],
            }
        )

    def verify(self, material: Mapping[str, bytes]) -> None:
        expected = {item.path: item.sha256 for item in self.files}
        if set(material) != set(expected):
            raise ContractError("CANDIDATE_PACKAGE_FILE_SET_MISMATCH")
        mismatched = [
            path
            for path, content in material.items()
            if hashlib.sha256(content).hexdigest() != expected[path]
        ]
        if mismatched:
            raise ContractError("CANDIDATE_PACKAGE_HASH_MISMATCH:" + ",".join(sorted(mismatched)))

