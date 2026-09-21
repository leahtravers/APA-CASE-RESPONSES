import unittest

from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v126a_harness_prompt_correction import V126AHarnessInventoryApparatus
from researcher_inventory.v126a_task_rules import V126A_BASE_RULES, V126A_CLASS_RULES


FORBIDDEN_LEGACY_DIRECTIVES = (
    "comprehensive literal extraction worker",
    "Do less means less invention and less qualification, NOT fewer materially represented coordinates",
    "Return every independently selectable source characterization",
    "Return materially represented lexical predicate increments",
    "Map the story at materially distinct event/proposition grain",
    "Create a useful compound for each distinct represented predicate relation",
)


class CaptureAdapter:
    def __init__(self):
        self.payloads = []

    def ask(self, payload):
        self.payloads.append(payload)
        return []


class V126APromptHarnessTests(unittest.TestCase):
    def setUp(self):
        self.old_base = apparatus.BASE_RULES
        self.old_classes = apparatus.CLASS_RULES
        apparatus.BASE_RULES = V126A_BASE_RULES
        apparatus.CLASS_RULES = V126A_CLASS_RULES

    def tearDown(self):
        apparatus.BASE_RULES = self.old_base
        apparatus.CLASS_RULES = self.old_classes

    def assert_contract_subordinate(self, text):
        self.assertIn("durable contract", text.lower())
        self.assertIn("controlling semantic authority", text.lower())
        for phrase in FORBIDDEN_LEGACY_DIRECTIVES:
            self.assertNotIn(phrase, text)

    def test_class_request_uses_only_contract_subordinate_envelope(self):
        adapter = CaptureAdapter()
        app = apparatus.InventoryApparatus(adapter)
        self.assertEqual(app._extract_class("source", "PLACE"), [])
        payload = adapter.payloads[-1]
        self.assert_contract_subordinate(payload["rules"])
        self.assertIn("apply the durable contract's PLACE rule exactly", payload["class_rule"])
        for phrase in FORBIDDEN_LEGACY_DIRECTIVES:
            self.assertNotIn(phrase, payload["class_rule"])

    def test_compound_request_does_not_reintroduce_legacy_expansion_rule(self):
        adapter = CaptureAdapter()
        app = V126AHarnessInventoryApparatus(adapter)
        self.assertEqual(app._extract_compounds("source", [], {}), [])
        payload = adapter.payloads[-1]
        self.assert_contract_subordinate(payload["rules"])
        self.assertIn("apply the durable contract's compound-construction rule exactly", payload["rules"])
        self.assertIn("cannot repair a missing primitive", payload["rules"])

    def test_request_layer_restates_isolation_without_answer_content(self):
        combined = V126A_BASE_RULES + "\n" + "\n".join(V126A_CLASS_RULES.values())
        self.assertIn("never infer permission", combined.lower())
        self.assertIn("sealed holdout source", combined.lower())
        self.assertIn("evaluator findings", combined.lower())
        self.assertNotIn("d47915552fdbdd23adc8c3f66ab06f94e022ab0bfd93faa5faabb53fdf9c9193", combined)
        self.assertNotIn("50d646aad08b33051b93c1f3b3538d59ff78386558473b71a906a94213635070", combined)


if __name__ == "__main__":
    unittest.main()
