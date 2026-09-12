#!/usr/bin/env python3
"""Verify immutable Leah-approved Researcher Inventory workbooks.

The XLSX files are the gold-standard archetypes. Calibration must not run unless
both exact SHA-256 hashes match. If a repository copy is wrong, attempt a local
repair from the checked-in authoritative base64 package. A repaired workbook is
accepted only if its SHA-256 equals Leah's immutable hash.
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


def _zip_members(raw: bytes) -> dict[str, bytes] | None:
    try:
        with zipfile.ZipFile(io.BytesIO(raw)) as zf:
            return {Path(name).name: zf.read(name) for name in zf.namelist() if not name.endswith("/")}
    except zipfile.BadZipFile:
        return None


def _recover_local_entries(raw: bytes) -> dict[str, bytes]:
    """Recover complete local-file entries when the outer ZIP central directory is missing."""
    out: dict[str, bytes] = {}
    pos = 0
    sig = b"PK\x03\x04"
    while True:
        start = raw.find(sig, pos)
        if start < 0 or start + 30 > len(raw):
            break
        try:
            (
                signature,
                version,
                flags,
                method,
                mtime,
                mdate,
                crc32,
                comp_size,
                uncomp_size,
                name_len,
                extra_len,
            ) = struct.unpack_from("<IHHHHHIIIHH", raw, start)
        except struct.error:
            break
        name_start = start + 30
        data_start = name_start + name_len + extra_len
        if data_start > len(raw):
            break
        name = raw[name_start:name_start + name_len].decode("utf-8", errors="replace")

        data: bytes | None = None
        end: int | None = None
        if comp_size and data_start + comp_size <= len(raw):
            compressed = raw[data_start:data_start + comp_size]
            if method == 0:
                data = compressed
            elif method == 8:
                try:
                    data = zlib.decompress(compressed, -15)
                except zlib.error:
                    data = None
            end = data_start + comp_size
        elif method == 8:
            # Data-descriptor form: deflate stream itself tells us where it ends.
            d = zlib.decompressobj(-15)
            try:
                data = d.decompress(raw[data_start:]) + d.flush()
                consumed = len(raw[data_start:]) - len(d.unused_data)
                if d.eof and consumed > 0:
                    end = data_start + consumed
                else:
                    data = None
            except zlib.error:
                data = None
        elif method == 0:
            # Stored entry with descriptor: next local header bounds the data.
            nxt = raw.find(sig, data_start)
            if nxt > data_start:
                data = raw[data_start:nxt]
                end = nxt

        if data is not None:
            if uncomp_size and len(data) != uncomp_size:
                data = None
            elif crc32 and (zlib.crc32(data) & 0xFFFFFFFF) != crc32:
                data = None

        if data is not None and name and not name.endswith("/"):
            out[Path(name).name] = data

        if end is None or end <= start:
            pos = start + 4
        else:
            # Skip optional data descriptor if present; otherwise next scan is safe.
            pos = end
    return out


def package_members() -> tuple[dict[str, bytes], str]:
    chunks = sorted(PACKAGE.glob("chunk_*.txt"))
    if not chunks:
        return {}, "none"
    encoded_chunks = ["".join(p.read_text(encoding="utf-8").split()) for p in chunks]

    candidates: list[tuple[str, bytes]] = []
    try:
        candidates.append(("concatenated_base64", base64.b64decode("".join(encoded_chunks), validate=True)))
    except Exception:
        pass
    try:
        candidates.append(("chunkwise_base64", b"".join(base64.b64decode(chunk, validate=True) for chunk in encoded_chunks)))
    except Exception:
        pass

    diagnostics = []
    for mode, raw in candidates:
        diagnostics.append({"mode": mode, "bytes": len(raw), "prefix_hex": raw[:8].hex(), "suffix_hex": raw[-8:].hex()})
        members = _zip_members(raw)
        if members is not None:
            return members, mode
        recovered = _recover_local_entries(raw)
        if recovered:
            diagnostics[-1]["recovered_names"] = sorted(recovered)
            return recovered, mode + ":local-entry-recovery"

    raise RuntimeError(f"authoritative package could not be decoded as ZIP; diagnostics={diagnostics}")


def write_status(report: dict) -> None:
    STATUS.parent.mkdir(parents=True, exist_ok=True)
    STATUS.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")


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
    package_mode = None
    try:
        if mismatched:
            members, package_mode = package_members()
            for name in mismatched:
                expected = EXPECTED[name]
                data = members.get(name)
                if data is None:
                    raise RuntimeError(f"immutable archetype mismatch and authoritative package lacks {name}; package contains {sorted(members)}")
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
            "package_mode": package_mode,
            "package_hashes": package_hashes,
        }
        write_status(report)
        print(json.dumps(report, sort_keys=True))
        if wrong:
            raise RuntimeError(f"archetype integrity failed: {wrong}")
        return 0
    except Exception as exc:
        write_status({
            "status": "FAILED",
            "expected": EXPECTED,
            "before": before,
            "mismatched": mismatched,
            "repaired": repaired,
            "package_mode": package_mode,
            "package_hashes": package_hashes,
            "error": f"{type(exc).__name__}: {exc}",
        })
        raise


if __name__ == "__main__":
    raise SystemExit(main())
