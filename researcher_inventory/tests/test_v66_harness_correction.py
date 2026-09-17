import re
import unittest
from types import SimpleNamespace

from researcher_inventory.v66_harness_correction import (
    V66HarnessInventoryApparatus,
    field_evidence_score,
)


class _SyntheticEvaluator:
    @staticmethod
    def norm(value):
        return re.sub(r"\s+", " ", str(value or "").lower()).strip()

    @staticmethod
    def tokens(value):
        weak = {"a", "an", "the", "is", "am", "are", "was", "were", "i", "to", "and", "during"}
        return {t for t in re.findall(r"[a-z0-9']+", _SyntheticEvaluator.norm(value)) if t not in weak and len(t) > 1}


class _CaptureAdapter:
    def __init__(self):
        self.payload = None

    def ask(self, payload):
        self.payload = payload
        return []


class V66HarnessCorrectionTests(unittest.TestCase):
    def test_field_score_uses_strong_source_cue_without_note_dilution(self):
        actual = {
            "unit_class": "TIME",
            "researcher_short_tag": "still waiting outside",
            "source_wording": None,
            "source_cue": "After the alarm, I am still waiting outside",
            "researcher_note": "A deliberately long neutral note with many unrelated navigation tokens that must not dilute source evidence.",
        }
        expected = {
            "c": "TIME",
            "g": "later waiting frame",
            "s": "speaker remains still waiting outside after the alarm",
        }
        self.assertGreaterEqual(field_evidence_score(_SyntheticEvaluator, actual, expected), 260.0)

    def test_field_score_does_not_boost_cross_class_match(self):
        actual = {
            "unit_class": "OBJECT",
            "researcher_short_tag": "still waiting outside",
            "source_wording": "waiting outside",
            "source_cue": "I am still waiting outside",
        }
        expected = {
            "c": "TIME",
            "g": "waiting frame",
            "s": "still waiting outside",
        }
        self.assertEqual(field_evidence_score(_SyntheticEvaluator, actual, expected), 0.0)

    def test_compound_task_is_selective_not_exhaustive(self):
        adapter = _CaptureAdapter()
        app = V66HarnessInventoryApparatus(adapter)
        refmap = {
            "B": SimpleNamespace(anchor=0),
            "V1": SimpleNamespace(anchor=10),
        }
        result = app._extract_compounds(
            "I waited.",
            [
                {"unit_ref": "B", "unit_class": "PERSON"},
                {"unit_ref": "V1", "unit_class": "VERB"},
            ],
            refmap,
        )
        self.assertEqual(result, [])
        rules = adapter.payload["rules"]
        self.assertIn("A primitive may remain unbundled", rules)
        self.assertIn("do not manufacture a compound merely because", rules)
        self.assertNotIn("Create a useful compound for each distinct represented predicate relation", rules)


if __name__ == "__main__":
    unittest.main()
