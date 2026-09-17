import unittest

from researcher_inventory.v64_compound_order_calibration_runner import (
    canonical_semantic_compound,
    filter_order_only_compound_findings,
)


class V64CompoundOrderHarnessTests(unittest.TestCase):
    def test_canonicalization_preserves_membership_and_q(self):
        self.assertEqual(
            canonical_semantic_compound("P1_B_V1_Q"),
            (("B", "P1", "V1"), True),
        )
        self.assertEqual(
            canonical_semantic_compound("B_V1_P1"),
            (("B", "P1", "V1"), False),
        )

    def test_order_only_missing_extra_pair_is_removed(self):
        findings = [
            ("BAD_COMPOUND", "missing semantic compound B_V1_P1"),
            ("BAD_COMPOUND", "extra semantic compound P1_B_V1"),
            ("MISSING_UNIT", "missing T1 [TIME] example"),
            ("BAD_COMPOUND", "compound C3 uses unmatched unit refs ['X1']"),
        ]
        self.assertEqual(
            filter_order_only_compound_findings(findings),
            [
                ("MISSING_UNIT", "missing T1 [TIME] example"),
                ("BAD_COMPOUND", "compound C3 uses unmatched unit refs ['X1']"),
            ],
        )

    def test_q_difference_is_not_removed(self):
        findings = [
            ("BAD_COMPOUND", "missing semantic compound B_V1_P1_Q"),
            ("BAD_COMPOUND", "extra semantic compound P1_B_V1"),
        ]
        self.assertEqual(filter_order_only_compound_findings(findings), findings)

    def test_true_membership_difference_is_not_removed(self):
        findings = [
            ("BAD_COMPOUND", "missing semantic compound B_V1_P1"),
            ("BAD_COMPOUND", "extra semantic compound B_V1_P2"),
        ]
        self.assertEqual(filter_order_only_compound_findings(findings), findings)

    def test_pairing_is_count_preserving(self):
        findings = [
            ("BAD_COMPOUND", "missing semantic compound B_V1_P1"),
            ("BAD_COMPOUND", "missing semantic compound P1_V1_B"),
            ("BAD_COMPOUND", "extra semantic compound P1_B_V1"),
        ]
        filtered = filter_order_only_compound_findings(findings)
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0][0], "BAD_COMPOUND")
        self.assertTrue(filtered[0][1].startswith("missing semantic compound"))


if __name__ == "__main__":
    unittest.main()
