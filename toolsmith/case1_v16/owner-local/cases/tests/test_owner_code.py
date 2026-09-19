import unittest
from owner_code import CardinalOutcome, CardinalResult, ContractError, DestinationResult, direct_write, terminal_state


class CasesTests(unittest.TestCase):
    def test_partial_and_uncertain_states(self):
        partial=DestinationResult("P","A",(CardinalResult(1,CardinalOutcome.WRITTEN,"ID","PROOF"),CardinalResult(2,CardinalOutcome.REJECTED_BEFORE_WRITE,error_class="DENIED")))
        partial.validate(packet_ref="P",attempt_ref="A",cardinal_count=2)
        self.assertEqual(terminal_state(partial),"PARTIAL")
        uncertain=DestinationResult("P","A",(CardinalResult(1,CardinalOutcome.UNCERTAIN,destination_proof_ref="READBACK"),))
        self.assertEqual(terminal_state(uncertain),"UNCERTAIN")

    def test_unwritten_identity_mismatch_and_direct_write_denied(self):
        with self.assertRaisesRegex(ContractError,"UNWRITTEN_CARDINAL"):
            CardinalResult(1,CardinalOutcome.REJECTED_BEFORE_WRITE,"ID")
        with self.assertRaisesRegex(ContractError,"DIRECT_DESTINATION_WRITE"):
            direct_write()


if __name__ == "__main__": unittest.main()
