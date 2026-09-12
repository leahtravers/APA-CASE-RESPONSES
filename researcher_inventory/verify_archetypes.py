#!/usr/bin/env python3
"""Verify immutable Leah-approved Researcher Inventory workbooks.

The XLSX files are the gold-standard archetypes.  Calibration must not run unless
both exact SHA-256 hashes match.  If a repository copy is wrong, attempt a local
repair from the checked-in authoritative base64 package.  A repaired workbook is
accepted only if its SHA-256 equals Leah's immutable hash.
"""
from __future__ import annotations

import base64
import hashlib
import io
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parent
ARCHETYPES = ROOT / "tests" / "archetypes"
PACKAGE = ARCHETYPES / "package"
STATUS = ROOT / "runtime" / "archetype_integrity.json"

EXPECTED = {
    "Case_2_Lightweight_Researcher_Inventory.xlsx": "d47915552fdbdd23adc8c3f66ab06f94e022ab0bfd93faa5faabb53fdf9c9193",
    "Case_6_Lightweight_Researcher_Inventory_v2_with_Verbs_and_Locators.xlsx": "50d646aad08b33051b93c1f3b3538d59ff78386558473b71a906a94213635070",
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def package_members() -> dict[str, bytes]:
    chunks = sorted(PACKAGE.glob("chunk_*.txt"))
    if not chunks:
        return {}
    encoded = "".join("".join(p.read_text(encoding="utf-8").split()) for p in chunks)
    try:
        raw = base64.b64decode(encoded, validate=True)
    except Exception as exc:
        raise RuntimeError(f"authoritative package is not valid base64: {exc}") from exc
    try:
        with zipfile.ZipFile(io.BytesIO(raw)) as zf:
            return {Path(name).name: zf.read(name) for name in zf.namelist() if not name.endswith("/")}
    except Exception as exc:
        raise RuntimeError(f"authoritative package is not a readable ZIP: {exc}") from exc


def main() -> int:
    STATUS.parent.mkdir(parents=True, exist_ok=True)
    before = {}
    mismatched = []
    for name, expected in EXPECTED.items():
        path = ARCHETYPES / name
        actual = sha256(path) if path.exists() else None
        before[name] = actual
        if actual != expected:
            mismatched.append(name)

    repaired = []
    package_hashes = {}
    if mismatched:
        members = package_members()
        for name in mismatched:
            expected = EXPECTED[name]
            data = members.get(name)
            if data is None:
                raise RuntimeError(f"immutable archetype mismatch and authoritative package lacks {name}")
            digest = hashlib.sha256(data).hexdigest()
            package_hashes[name] = digest
            if digest != expected:
                raise RuntimeError(
                    f"immutable archetype mismatch for {name}; package hash {digest} also does not equal required {expected}"
                )
            (ARCHETYPES / name).write_bytes(data)
            repaired.append(name)

    after = {name: sha256(ARCHETYPES / name) for name in EXPECTED}
    wrong = {name: {"actual": after[name], "expected": expected} for name, expected in EXPECTED.items() if after[name] != expected}
    report = {
        "status": "VERIFIED" if not wrong else "FAILED",
        "expected": EXPECTED,
        "before": before,
        "after": after,
        "repaired": repaired,
        "package_hashes": package_hashes,
    }
    STATUS.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, sort_keys=True))
    if wrong:
        raise RuntimeError(f"archetype integrity failed: {wrong}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
