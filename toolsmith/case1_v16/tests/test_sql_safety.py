from pathlib import Path
import re
import unittest


ROOT = Path(__file__).parents[1]


class SqlSafetyTests(unittest.TestCase):
    def test_every_migration_is_fail_closed_candidate(self):
        migrations = sorted((ROOT / "migrations").glob("*.sql"))
        self.assertTrue(migrations)
        for migration in migrations:
            text = migration.read_text(encoding="utf-8")
            self.assertIn("CANDIDATE_ONLY_NOT_AUTHORIZED_FOR_EXECUTION", text, migration.name)
            self.assertLess(text.index("CANDIDATE_ONLY_NOT_AUTHORIZED_FOR_EXECUTION"), text.index("CREATE TABLE"))

    def test_no_destructive_sql(self):
        destructive = re.compile(r"\b(DROP|TRUNCATE|DELETE\s+FROM|ALTER\s+TABLE\s+\S+\s+DROP)\b", re.I)
        for migration in (ROOT / "migrations").glob("*.sql"):
            text = re.sub(r"/\*.*?\*/", "", migration.read_text(encoding="utf-8"), flags=re.S)
            self.assertIsNone(destructive.search(text), migration.name)

    def test_candidate_tables_enable_rls_and_revoke_public(self):
        for migration in (ROOT / "migrations").glob("*.sql"):
            text = migration.read_text(encoding="utf-8")
            created = re.findall(r"CREATE TABLE\s+([a-z_]+\.[a-z0-9_]+)", text, flags=re.I)
            for table in created:
                self.assertRegex(text, rf"ALTER TABLE\s+{re.escape(table)}\s+ENABLE ROW LEVEL SECURITY", table)
            self.assertIn("REVOKE ALL", text, migration.name)

    def test_no_plaintext_candidate_column_in_graveyard(self):
        text = (ROOT / "migrations" / "004_cases_graveyard_vault_candidate.sql").read_text(encoding="utf-8")
        block = text.split("CREATE TABLE apa_graveyard.unwritten_identity_candidate_disposition", 1)[1]
        block = block.split(");", 1)[0]
        self.assertNotRegex(block, r"candidate_(string|plaintext|material)\s")
        self.assertIn("hmac_sha256", block)
        self.assertIn("hmac_key_ref", block)


if __name__ == "__main__":
    unittest.main()

