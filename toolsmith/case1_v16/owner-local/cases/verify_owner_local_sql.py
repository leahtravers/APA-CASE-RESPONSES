from __future__ import annotations

import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SQL = ROOT / "004_cases_candidate.sql"
EXPECTED_SHA256 = "b3f3205373c69d0d73ddde1f492eb044f6d86b531a7c7c06f2a7f990f9490a13"
EXPECTED_TABLES = ["apa_cases_candidate.research_inventory_rehearsal_attempt_v16_candidate","apa_cases_candidate.research_inventory_cardinal_result_v16_candidate"]
EXPECTED_SCHEMA = "apa_cases_candidate"

text = SQL.read_text(encoding="utf-8")
actual_sha256 = hashlib.sha256(SQL.read_bytes()).hexdigest()
assert actual_sha256 == EXPECTED_SHA256, (actual_sha256, EXPECTED_SHA256)
assert "CANDIDATE_ONLY_NOT_AUTHORIZED_FOR_EXECUTION:" in text
assert text.index("RAISE EXCEPTION 'CANDIDATE_ONLY_NOT_AUTHORIZED_FOR_EXECUTION:") < text.index("CREATE TABLE")
assert not re.search(r"^\s*(DROP|DELETE|TRUNCATE|INSERT|UPDATE)\b", text, re.I | re.M)
created = re.findall(r"^CREATE TABLE\s+([a-z_]+\.[a-z0-9_]+)\s*\(", text, re.I | re.M)
altered = re.findall(r"^ALTER TABLE\s+([a-z_]+\.[a-z0-9_]+)\s+ENABLE ROW LEVEL SECURITY;", text, re.I | re.M)
revoked = re.findall(r"^REVOKE ALL ON TABLE\s+([a-z_]+\.[a-z0-9_]+)\s+FROM PUBLIC, anon, authenticated;", text, re.I | re.M)
assert created == EXPECTED_TABLES, (created, EXPECTED_TABLES)
assert set(created) == set(altered) == set(revoked)
assert all(name.startswith(EXPECTED_SCHEMA + ".") for name in created)
print("APA Cases: 2 tables / owner-local hash and safety checks / PASS")

