#!/usr/bin/env python3
"""Verify/repair immutable Leah-approved Researcher Inventory workbooks.

Calibration may not run unless both repository XLSX files match Leah's exact
SHA-256 values. Repair material is checked in as text-only base64 packaging and
is never exposed to the semantic extractor.
"""
from __future__ import annotations

import base64
import hashlib
import io
import json
from pathlib import Path
import struct
import zipfile
import zlib

ROOT = Path(__file__).resolve().parent
ARCHETYPES = ROOT / "tests" / "archetypes"
PACKAGE = ARCHETYPES / "package"
STATUS = ROOT / "runtime" / "archetype_integrity.json"

CASE2 = "Case_2_Lightweight_Researcher_Inventory.xlsx"
CASE6 = "Case_6_Lightweight_Researcher_Inventory_v2_with_Verbs_and_Locators.xlsx"
EXPECTED = {
    CASE2: "d47915552fdbdd23adc8c3f66ab06f94e022ab0bfd93faa5faabb53fdf9c9193",
    CASE6: "50d646aad08b33051b93c1f3b3538d59ff78386558473b71a906a94213635070",
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _recover_local_entries(raw: bytes) -> dict[str, bytes]:
    """Recover complete local-file entries from an outer ZIP missing its directory."""
    out: dict[str, bytes] = {}
    sig = b"PK\x03\x04"
    pos = 0
    while True:
        start = raw.find(sig, pos)
        if start < 0 or start + 30 > len(raw):
            break
        try:
            _, _, _, method, _, _, crc32, comp_size, uncomp_size, name_len, extra_len = struct.unpack_from(
                "<IHHHHHIIIHH", raw, start
            )
        except struct.error:
            break
        name_start = start + 30
        data_start = name_start + name_len + extra_len
        if data_start > len(raw):
            break
        name = raw[name_start:name_start + name_len].decode("utf-8", errors="replace")
        data = None
        end = None
        if comp_size and data_start + comp_size <= len(raw):
            compressed = raw[data_start:data_start + comp_size]
            try:
                data = compressed if method == 0 else zlib.decompress(compressed, -15) if method == 8 else None
            except zlib.error:
                data = None
            end = data_start + comp_size
        elif method == 8:
            d = zlib.decompressobj(-15)
            try:
                data = d.decompress(raw[data_start:]) + d.flush()
                consumed = len(raw[data_start:]) - len(d.unused_data)
                end = data_start + consumed if d.eof and consumed > 0 else None
                if end is None:
                    data = None
            except zlib.error:
                data = None
        if data is not None:
            if uncomp_size and len(data) != uncomp_size:
                data = None
            elif crc32 and (zlib.crc32(data) & 0xFFFFFFFF) != crc32:
                data = None
        if data is not None and name and not name.endswith("/"):
            out[Path(name).name] = data
        pos = end if end and end > start else start + 4
    return out


def case2_source() -> tuple[bytes, str]:
    chunks = sorted(PACKAGE.glob("chunk_*.txt"))
    if not chunks:
        raise RuntimeError("Case 2 authoritative package chunks are missing")
    encoded = "".join("".join(p.read_text(encoding="utf-8").split()) for p in chunks)
    raw = base64.b64decode(encoded, validate=True)
    try:
        with zipfile.ZipFile(io.BytesIO(raw)) as zf:
            members = {Path(n).name: zf.read(n) for n in zf.namelist() if not n.endswith("/")}
            mode = "outer-zip"
    except zipfile.BadZipFile:
        members = _recover_local_entries(raw)
        mode = "outer-zip-local-entry-recovery"
    data = members.get(CASE2)
    if data is None:
        raise RuntimeError(f"Case 2 authoritative package lacks {CASE2}; contains {sorted(members)}")
    return data, mode


def case6_source() -> tuple[bytes, str]:
    chunks = sorted(PACKAGE.glob("case6_[0-9][0-9][0-9].b64"))
    if not chunks:
        raise RuntimeError("Case 6 authoritative package chunks are missing")
    encoded = "".join("".join(p.read_text(encoding="utf-8").split()) for p in chunks)
    data = base64.b64decode(encoded, validate=True)
    return data, f"case6-chunked-base64:{len(chunks)}"


def write_status(report: dict) -> None:
    STATUS.parent.mkdir(parents=True, exist_ok=True)
    STATUS.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    STATUS.parent.mkdir(parents=True, exist_ok=True)
    before = {name: sha256(ARCHETYPES / name) if (ARCHETYPES / name).exists() else None for name in EXPECTED}
    mismatched = [name for name, expected in EXPECTED.items() if before[name] != expected]
    repaired: list[str] = []
    source_modes: dict[str, str] = {}
    source_hashes: dict[str, str] = {}
    try:
        for name in mismatched:
            if name == CASE2:
                data, mode = case2_source()
            elif name == CASE6:
                data, mode = case6_source()
            else:
                raise RuntimeError(f"no authoritative source registered for {name}")
            digest = hashlib.sha256(data).hexdigest()
            source_modes[name] = mode
            source_hashes[name] = digest
            if digest != EXPECTED[name]:
                raise RuntimeError(
                    f"authoritative source hash for {name} is {digest}, required {EXPECTED[name]}"
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
            "source_modes": source_modes,
            "source_hashes": source_hashes,
        }
        write_status(report)
        print(json.dumps(report, sort_keys=True))
        if wrong:
            raise RuntimeError(f"archetype integrity failed after repair: {wrong}")
        return 0
    except Exception as exc:
        write_status({
            "status": "FAILED",
            "expected": EXPECTED,
            "before": before,
            "mismatched": mismatched,
            "repaired": repaired,
            "source_modes": source_modes,
            "source_hashes": source_hashes,
            "error": f"{type(exc).__name__}: {exc}",
        })
        raise


if __name__ == "__main__":
    raise SystemExit(main())
