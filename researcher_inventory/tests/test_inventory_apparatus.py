import unittest

from researcher_inventory.inventory_apparatus import InventoryApparatus, ApparatusError, Candidate


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
                    {"canonical_key":"B","short_tag":"I","source_wording":"I","source_cue":"I met Gary","note":None,"qualities_available":False,"anchor_hint":0},
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
                    {"canonical_key":"call-risky","short_tag":"called risky","source_wording":"called","source_cue":"Gary called the plan risky","note":None,"qualities_available":True,"anchor_hint":41},
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
                {"refs":["B","V1","H1","P1","T1"],"researcher_bundle":"I met Gary at the office yesterday","qualities_available":False},
                {"refs":["H1","V2","O1","L1"],"researcher_bundle":"Gary called the plan risky","qualities_available":True},
                {"refs":["H1","V3","R2","P2"],"researcher_bundle":"walked out of the room","qualities_available":False},
            ]
        raise AssertionError(task)


class BadSourceAdapter(FakeAdapter):
    def ask(self, payload):
        if payload["task"] == "researcher_inventory_extract_one_class" and payload["class"] == "LABEL":
            return [{"canonical_key":"bad","short_tag":"dangerous","source_wording":"dangerous","source_cue":"dangerous","note":None,"qualities_available":False,"anchor_hint":0}]
        return super().ask(payload)


class SynonymAdapter(FakeAdapter):
    def ask(self, payload):
        if payload["task"] == "researcher_inventory_extract_one_class" and payload["class"] == "LABEL":
            return [{"canonical_key":"risky-plan","short_tag":"dangerous","source_wording":"risky","source_cue":"called the plan risky","note":None,"qualities_available":False,"anchor_hint":57}]
        return super().ask(payload)


class InferredSceneAdapter(FakeAdapter):
    def ask(self, payload):
        if payload["task"] == "researcher_inventory_extract_one_class" and payload["class"] == "PLACE":
            return [{"canonical_key":"meeting-scene","short_tag":"place of meeting","source_wording":None,"source_cue":"I met Gary","note":"unnamed place inferred from represented occurrence","qualities_available":False,"anchor_hint":0}]
        if payload["task"] == "researcher_inventory_extract_one_class" and payload["class"] == "TIME":
            return [{"canonical_key":"meeting-episode","short_tag":"meeting episode","source_wording":None,"source_cue":"I met Gary","note":"unnamed time inferred from represented occurrence","qualities_available":False,"anchor_hint":0}]
        if payload["task"] == "researcher_inventory_build_lightweight_compounds":
            return [{"refs":["B","V1","H1","P1","T1"],"researcher_bundle":"I met Gary","qualities_available":False}]
        return super().ask(payload)


class InventoryApparatusTests(unittest.TestCase):
    def test_same_semantic_rows_produce_same_mechanical_output(self):
        app = InventoryApparatus(FakeAdapter())
        self.assertEqual(app.run(SOURCE, "TEST-1"), app.run(SOURCE, "TEST-1"))

    def test_code_owns_canonical_ids_and_alias_merge(self):
        result = InventoryApparatus(FakeAdapter()).run(SOURCE, "TEST-1")
        self.assertEqual(
            [u["unit_ref"] for u in result["units"]],
            ["P1","P2","T1","B","H1","O1","L1","V1","V2","V3","R1","R2"],
        )
        self.assertEqual(len([u for u in result["units"] if u["unit_class"] == "PERSON"]), 2)

    def test_person_order_uses_participation_before_possessive_only_actor(self):
        rows = [
            Candidate("PERSON", "B", "I", "I", "I bought", "speaker", False, 0, 0, 0),
            Candidate("PERSON", "kids", "my kids", "my kids", "my kids’ cereal", None, False, 9, None, 0),
            Candidate("PERSON", "attendant", "attendant", "attendant", "The attendant helped me", None, False, 30, 30, 0),
            Candidate("PERSON", "partner", "partner", "partner", "I called my partner", None, False, 55, 55, 0),
        ]
        ordered = InventoryApparatus._merge_and_order(rows, "PERSON")
        self.assertEqual([r.canonical_key for r in ordered], ["B", "attendant", "partner", "kids"])

    def test_shared_order_anchor_uses_broad_before_contained_scope(self):
        rows = [
            Candidate("PLACE", "self-check", "self-check", "self-check", "at the self-check at the store", None, False, 10, 3, 1),
            Candidate("PLACE", "store", "store", "store", "at the self-check at the store", None, False, 28, 3, 0),
        ]
        ordered = InventoryApparatus._merge_and_order(rows, "PLACE")
        self.assertEqual([r.canonical_key for r in ordered], ["store", "self-check"])

    def test_q_is_constructed_mechanically(self):
        result = InventoryApparatus(FakeAdapter()).run(SOURCE, "TEST-1")
        expressions = [c["compound_expression"] for c in result["compounds"]]
        self.assertIn("H1_V2_O1_L1_Q", expressions)
        for compound in result["compounds"]:
            self.assertEqual(compound["compound_expression"].endswith("_Q"), compound["qualities_available"])

    def test_invented_source_wording_is_rejected(self):
        with self.assertRaises(ApparatusError):
            InventoryApparatus(BadSourceAdapter(), retries=0).run(SOURCE, "TEST-1")

    def test_synonym_short_tag_is_rejected(self):
        with self.assertRaises(ApparatusError):
            InventoryApparatus(SynonymAdapter(), retries=0).run(SOURCE, "TEST-1")

    def test_unnamed_place_and_time_are_allowed_when_anchored_to_occurrence(self):
        result = InventoryApparatus(InferredSceneAdapter()).run(SOURCE, "TEST-1")
        p1 = next(u for u in result["units"] if u["unit_ref"] == "P1")
        t1 = next(u for u in result["units"] if u["unit_ref"] == "T1")
        self.assertIsNone(p1["source_wording"])
        self.assertIsNone(t1["source_wording"])
        self.assertEqual(p1["source_cue"], "I met Gary")
        self.assertEqual(t1["source_cue"], "I met Gary")

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
