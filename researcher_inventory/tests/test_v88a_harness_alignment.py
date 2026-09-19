from __future__ import annotations

import unittest

from researcher_inventory import apparatus_calibration_runner as evaluator
from researcher_inventory.v88a_harness_alignment_correction import (
    editor_shorthand_score,
    install_editor_shorthand_alignment,
)


class V88AEditorShorthandAlignmentTests(unittest.TestCase):
    def test_leading_article_and_minor_orthographic_difference_score_strongly(self):
        actual = {
            "unit_ref": "O1",
            "unit_class": "OBJECT",
            "researcher_short_tag": "a cargo trailor",
            "source_wording": "a cargo trailor",
            "source_cue": "source-preserved wording",
        }
        expected = {"c": "OBJECT", "g": "cargo trailer", "s": "editor shorthand"}
        self.assertGreaterEqual(editor_shorthand_score(evaluator, actual, expected), 930.0)

    def test_cross_class_near_match_is_never_created(self):
        actual = {
            "unit_ref": "L1",
            "unit_class": "LABEL",
            "researcher_short_tag": "a cargo trailor",
            "source_wording": "a cargo trailor",
        }
        expected = {"c": "OBJECT", "g": "cargo trailer", "s": "editor shorthand"}
        self.assertEqual(editor_shorthand_score(evaluator, actual, expected), 0.0)

    def test_vaguely_similar_phrase_does_not_receive_high_confidence_signal(self):
        actual = {
            "unit_ref": "O1",
            "unit_class": "OBJECT",
            "researcher_short_tag": "service counter",
            "source_wording": "service counter",
        }
        expected = {"c": "OBJECT", "g": "service center", "s": "editor shorthand"}
        self.assertEqual(editor_shorthand_score(evaluator, actual, expected), 0.0)

    def test_installed_alignment_breaks_generic_token_tie_toward_near_editor_shorthand(self):
        original = evaluator.alignment_score
        try:
            install_editor_shorthand_alignment(evaluator)
            actual_units = [{
                "unit_ref": "O1",
                "unit_class": "OBJECT",
                "researcher_short_tag": "a cargo trailor",
                "source_wording": "a cargo trailor",
                "source_cue": "cargo context",
                "researcher_note": None,
                "qualities_available": False,
            }]
            expected_units = {
                "O7": {"c": "OBJECT", "g": "cargo trailer", "s": "vehicle"},
                "O8": {"c": "OBJECT", "g": "cargo manifest", "s": "document"},
            }
            actual_to_expected, expected_to_actual, unmatched_actual, unmatched_expected = evaluator.align_units(
                actual_units, expected_units
            )
            self.assertEqual(actual_to_expected, {"O1": "O7"})
            self.assertEqual(expected_to_actual, {"O7": "O1"})
            self.assertEqual(unmatched_actual, set())
            self.assertEqual(unmatched_expected, {"O8"})
        finally:
            evaluator.alignment_score = original


if __name__ == "__main__":
    unittest.main()
