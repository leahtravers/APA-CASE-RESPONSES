#!/usr/bin/env python3
"""V147A whole-source scaffold-first / bounded-relation harness.

RI-CONTRACT-V147 remains the sole durable semantic authority. This successor retains
V146A's single-turn whole-source topology while changing only the operation selector so
it follows V147's scaffold-first hybrid order. No gold/evaluator/holdout material is
included.
"""
from __future__ import annotations

from typing import Any

from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory import v146a_relation_first_harness as v146a
from researcher_inventory.v126a_task_rules import V126A_BASE_RULES
from researcher_inventory.v147a_task_rules import V147A_INTEGRATED_RULE


class V147AHybridInventoryApparatus(v146a.V146ARelationFirstHarnessInventoryApparatus):
    """Execute V147 semantics in one coherent whole-source model turn."""

    def _extract_integrated(self, source: str) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
        payload = {
            "task": "researcher_inventory_build_scaffold_bounded_inventory",
            "rules": V126A_BASE_RULES + "\n" + V147A_INTEGRATED_RULE,
            "source": source,
            "response_schema": {
                "classes": {cls: [v146a._UNIT_SCHEMA] for cls in apparatus.CLASSES},
                "compounds": [{
                    "members": [{
                        "class": "one of PLACE, TIME, PERSON, OBJECT, LABEL, VERB, LOCATOR",
                        "canonical_key": "canonical_key from the returned primitive in that class",
                    }],
                    "researcher_bundle": "concise source-near bundle or null",
                    "qualities_available": "boolean only",
                }],
            },
        }
        last: Exception | None = None
        for _ in range(self.retries + 1):
            try:
                response = self.adapter.ask(payload)
                if not isinstance(response, dict):
                    raise apparatus.ApparatusError("integrated extraction must return an object")
                classes = response.get("classes")
                if not isinstance(classes, dict):
                    raise apparatus.ApparatusError("integrated extraction requires classes object")
                by_class: dict[str, list[apparatus.Candidate]] = {}
                unknown_classes = set(classes) - set(apparatus.CLASSES)
                if unknown_classes:
                    raise apparatus.ApparatusError(f"integrated extraction returned unknown classes: {sorted(unknown_classes)}")
                for cls in apparatus.CLASSES:
                    if cls not in classes:
                        raise apparatus.ApparatusError(f"integrated extraction omitted class {cls}")
                    by_class[cls] = self._normalize_integrated_class(source, cls, classes[cls])
                units, refmap = self._assign_refs(by_class)
                keymap = self._key_to_ref(by_class, refmap)
                compounds = self._normalize_integrated_compounds(response.get("compounds"), keymap, refmap)
                return units, compounds
            except Exception as exc:
                last = exc
                payload["correction"] = str(exc)
        raise apparatus.ApparatusError(f"integrated V147A extraction failed after retries: {last}")

    def run(self, source: str, source_case_ref: str | None = None, researcher_interest: str | None = None, created_by_ref: str = "RI-WORKER") -> dict[str, Any]:
        result = super().run(source, source_case_ref, researcher_interest, created_by_ref)
        result["validation"]["notes"] = ["V147A one-turn whole-source scaffold-first / bounded-relation semantic pass plus mechanical validation passed"]
        return result
