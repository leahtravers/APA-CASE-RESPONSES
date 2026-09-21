import unittest

from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v148a_class_complete_harness import V148AClassCompleteInventoryApparatus
from researcher_inventory.v148a_task_rules import V148A_INTEGRATED_RULE


class CaptureAdapter:
    def __init__(self, response):
        self.response = response
        self.payloads = []
    def ask(self, payload):
        self.payloads.append(dict(payload))
        return self.response


def minimal_response():
    return {
        "classes": {
            "PLACE": [{"canonical_key":"store","short_tag":"store","source_wording":"store","source_cue":"at the store","note":None,"qualities_available":False,"anchor_hint":12,"order_cue":"at the store","scope_rank":0}],
            "TIME": [],
            "PERSON": [{"canonical_key":"B","short_tag":"I","source_wording":"I","source_cue":"I waited","note":None,"qualities_available":False,"anchor_hint":0,"order_cue":"I waited","scope_rank":0}],
            "OBJECT": [],
            "LABEL": [],
            "VERB": [{"canonical_key":"waited","short_tag":"waited","source_wording":"waited","source_cue":"waited","note":None,"qualities_available":False,"anchor_hint":2,"order_cue":"waited","scope_rank":0}],
            "LOCATOR": [{"canonical_key":"at_store","short_tag":"at the store","source_wording":"at the store","source_cue":"at the store","note":None,"qualities_available":False,"anchor_hint":9,"order_cue":"at the store","scope_rank":0}],
        },
        "compounds": [{"members":[{"class":"PERSON","canonical_key":"B"},{"class":"VERB","canonical_key":"waited"},{"class":"PLACE","canonical_key":"store"},{"class":"LOCATOR","canonical_key":"at_store"}],"researcher_bundle":"I waited at the store","qualities_available":False}],
    }


class V148AClassCompleteHarnessTests(unittest.TestCase):
    def test_whole_source_class_complete_uses_one_request(self):
        adapter = CaptureAdapter(minimal_response())
        result = V148AClassCompleteInventoryApparatus(adapter).run("I waited at the store.", "test-case", "lightweight researcher inventory only")
        self.assertEqual(len(adapter.payloads), 1)
        payload = adapter.payloads[0]
        self.assertEqual(payload["task"], "researcher_inventory_build_class_complete_source_role_inventory")
        lower = payload["rules"].lower()
        self.assertIn("primitive completeness is class-local", lower)
        self.assertIn("class-local exclusions", lower)
        self.assertEqual(set(payload["response_schema"]["classes"]), set(apparatus.CLASSES))
        self.assertEqual({u["unit_ref"] for u in result["units"]}, {"P1","B","V1","R1"})

    def test_unknown_compound_member_fails(self):
        response = minimal_response()
        response["compounds"][0]["members"].append({"class":"OBJECT","canonical_key":"missing"})
        with self.assertRaises(apparatus.ApparatusError):
            V148AClassCompleteInventoryApparatus(CaptureAdapter(response), retries=0).run("I waited at the store.")

    def test_runtime_rule_is_gold_blind_and_contract_subordinate(self):
        lower = V148A_INTEGRATED_RULE.lower()
        self.assertIn("durable contract", lower)
        self.assertIn("primitive completeness is class-local", lower)
        self.assertIn("sealed-holdout material", lower)
        self.assertNotIn("d47915552fdbdd23adc8c3f66ab06f94e022ab0bfd93faa5faabb53fdf9c9193", V148A_INTEGRATED_RULE)
        self.assertNotIn("50d646aad08b33051b93c1f3b3538d59ff78386558473b71a906a94213635070", V148A_INTEGRATED_RULE)


if __name__ == "__main__":
    unittest.main()
