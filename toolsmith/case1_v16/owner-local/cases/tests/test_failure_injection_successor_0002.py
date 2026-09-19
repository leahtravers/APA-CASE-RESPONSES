import unittest
from owner_code import CardinalOutcome, CardinalResult, ContractError, DestinationResult, terminal_state


class CasesFailureInjectionTests(unittest.TestCase):
    def test_written_requires_identity_and_proof(self):
        for identity, proof in ((None, "P"), ("ID", None), (None, None)):
            with self.subTest(identity=identity, proof=proof):
                with self.assertRaisesRegex(ContractError, "WRITTEN_REQUIRES"):
                    CardinalResult(1, CardinalOutcome.WRITTEN, identity, proof)

    def test_uncertain_requires_reconciliation_reference(self):
        with self.assertRaisesRegex(ContractError, "UNCERTAIN_REQUIRES"):
            CardinalResult(1, CardinalOutcome.UNCERTAIN)

    def test_result_cardinality_and_binding_fail_closed(self):
        with self.assertRaisesRegex(ContractError, "CONTIGUOUS"):
            DestinationResult("P", "A", (CardinalResult(2, CardinalOutcome.REJECTED_BEFORE_WRITE),))
        result = DestinationResult("P", "A", (CardinalResult(1, CardinalOutcome.REJECTED_BEFORE_WRITE),))
        with self.assertRaisesRegex(ContractError, "PACKET_OR_ATTEMPT"):
            result.validate(packet_ref="OTHER", attempt_ref="A", cardinal_count=1)
        with self.assertRaisesRegex(ContractError, "CARDINALITY"):
            result.validate(packet_ref="P", attempt_ref="A", cardinal_count=2)

    def test_complete_and_rejected_terminal_states(self):
        completed = DestinationResult("P", "A", (CardinalResult(1, CardinalOutcome.WRITTEN, "ID", "PROOF"),))
        rejected = DestinationResult("P", "A", (CardinalResult(1, CardinalOutcome.REJECTED_BEFORE_WRITE),))
        self.assertEqual(terminal_state(completed), "COMPLETED")
        self.assertEqual(terminal_state(rejected), "REJECTED_BEFORE_WRITE")

