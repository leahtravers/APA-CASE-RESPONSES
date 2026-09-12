import unittest

from researcher_inventory.inventory_apparatus import InventoryApparatus, ApparatusError


SOURCE = "I met Gary at the office yesterday. Gary called the plan risky and walked out of the room."


class FakeAdapter:
    def ask(self, payload):
        task = payload["task"]
        if task == "researcher_inventory_extract_one_class":
            cls = payload["class"]
            rows = {
                "PLACE": [
                    {"canonical_key":"office","short_tag":"office","source_wording":"office","source_cue":"at the office","note":None,"qualities_available":False,"anchor_hint":18},
                    {"canonical_key":"room","short_tag":"room","source_wording":"room","source_cue":"out of the room","note":None,"qualities_available":False,"anchor_hint":84},
                ],
                "TIME": [
                    {"canonical_key":"yesterday","short_tag":"yesterday","source_wording":"yesterday","source_cue":"yesterday","note":None,"qualities_available":False,"anchor_hint":25},
                ],
                "PERSON": [
                    {"canonical_key":"B","short_tag":"speaker","source_wording":"I","source_cue":"I met Gary","note":None,"qualities_available":False,"anchor_hint":0},
                    {"canonical_key":"gary","short_tag":"Gary","source_wording":"Gary","source_cue":"met Gary","note":None,"qualities_available":False,"anchor_hint":6},
                    {"canonical_key":"gary","short_tag":"Gary","source_wording":"Gary","source_cue":"Gary called","note":"coreference","qualities_available":False,"anchor_hint":36},
                ],
                "OBJECT": [
                    {"canonical_key":"plan","short_tag":"plan","source_wording":"plan","source_cue":"the plan","note":None,"qualities_available":True,"anchor_hint":52},
                ],
                "LABEL": [
                    {"canonical_key":"risky-plan","short_tag":"risky","source_wording":"risky","source_cue":"called the plan risky","note":None,"qualities_available":False,"anchor_hint":57},
                ],
                "VERB": [
                    {"canonical_key":"meet","short_tag":"met","source_wording":"met","source_cue":"I met Gary","note":None,"qualities_available":False,"anchor_hint":2},
                    {"canonical_key":"call-risky","short_tag":"called ... risky","source_wording":"called","source_cue":"Gary called the plan risky","note":None,"qualities_available":True,"anchor_hint":41},
                    {"canonical_key":"walk-out","short_tag":"walked out","source_wording":"walked out","source_cue":"walked out of the room","note":None,"qualities_available":False,"anchor_hint":67},
                ],
                "LOCATOR": [
                    {"canonical_key":"at-office","short_tag":"at the office","source_wording":"at the office","source_cue":"at the office","note":None,"qualities_available":False,"anchor_hint":11},
                    {"canonical_key":"out-room","short_tag":"out of the room","source_wording":"out of the room","source_cue":"out of the room","note":None,"qualities_available":False,"anchor_hint":74},
                ],
            }
            return rows[cls]
        if task == "researcher_inventory_build_lightweight_compounds":
            return [
                {"refs":["B","V1","H1","P1","T1"],"researcher_bundle":"I met Gary at the office yesterday","qualities_available":False,"anchor_ref":"B"},
                {"refs":["H1","V2","O1","L1"],"researcher_bundle":"Gary called the plan risky","qualities_available":True,"anchor_ref":"H1"},
                {"refs":["H1","V3","R2","P2"],"researcher_bundle":"walked out of the room","qualities_available":False,"anchor_ref":"V3"},
            ]
        raise AssertionError(task)


class BadSourceAdapter(FakeAdapter):
    def ask(self, payload):
        if payload["task"] == "researcher_inventory_extract_one_class" and payload["class"] == "LABEL":
            return [{"canonical_key":"bad","short_tag":"dangerous","source_wording":"dangerous","source_cue":"dangerous","note":None,"qualities_available":False,"anchor_hint":0}]
        return super().ask(payload)


class InventoryApparatusTests(unittest.TestCase):
    def test_same_semantic_rows_produce_same_mechanical_output(self):
        app = InventoryApparatus(FakeAdapter())
        a = app.run(SOURCE, "TEST-1")
        b = app.run(SOURCE, "TEST-1")
        self.assertEqual(a, b)

    def test_code_owns_canonical_ids_and_alias_merge(self):
        result = InventoryApparatus(FakeAdapter()).run(SOURCE, "TEST-1")
        self.assertEqual(
            [u["unit_ref"] for u in result["units"]],
            ["P1","P2","T1","B","H1","O1","L1","V1","V2","V3","R1","R2"],
        )
        self.assertEqual(len([u for u in result["units"] if u["unit_class"] == "PERSON"]), 2)

    def test_q_is_constructed_mechanically(self):
        result = InventoryApparatus(FakeAdapter()).run(SOURCE, "TEST-1")
        expressions = [c["compound_expression"] for c in result["compounds"]]
        self.assertIn("H1_V2_O1_L1_Q", expressions)
        for compound in result["compounds"]:
            self.assertEqual(compound["compound_expression"].endswith("_Q"), compound["qualities_available"])

    def test_invented_source_wording_is_rejected(self):
        with self.assertRaises(ApparatusError):
            InventoryApparatus(BadSourceAdapter(), retries=0).run(SOURCE, "TEST-1")

    def test_sql_rows_stay_in_candidate_domain_shape(self):
        app = InventoryApparatus(FakeAdapter())
        result = app.run(SOURCE, "TEST-1")
        rows = app.sql_rows(result)
        self.assertEqual(set(rows), {
            "research_hypothesis_candidate",
            "research_inventory_unit_candidate",
            "research_inventory_compound_candidate",
        })
        self.assertTrue(all(r["candidate_ref"] == result["candidate"]["candidate_ref"] for r in rows["research_inventory_unit_candidate"]))
        self.assertEqual(rows["research_hypothesis_candidate"][0]["candidate_status"], "CANDIDATE")


if __name__ == "__main__":
    unittest.main()
