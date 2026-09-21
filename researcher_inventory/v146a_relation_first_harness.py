#!/usr/bin/env python3
"""V146A harness correction: enforce one whole-source relation-first semantic pass.

This is a harness/runtime correction only. RI-CONTRACT-V146 remains the sole durable
semantic authority. No archetype rows, expected counts, evaluator findings, scored
outputs, case-specific corrections, or holdout material appear here.
"""
from __future__ import annotations

from typing import Any

from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v126a_harness_prompt_correction import V126AHarnessInventoryApparatus
from researcher_inventory.v126a_task_rules import V126A_BASE_RULES
from researcher_inventory.v146a_task_rules import V146A_INTEGRATED_RULE


_UNIT_SCHEMA = {
    "canonical_key": "stable neutral identity for same-class alias/coreference merge; B for speaker",
    "short_tag": "compact source-near tag; no synonym substitution",
    "source_wording": "exact source substring, or null only for a supported unnamed PLACE/TIME",
    "source_cue": "required exact bounded source substring anchoring the coordinate",
    "note": "neutral inference/coreference note or null",
    "qualities_available": "boolean only",
    "anchor_hint": "integer source offset if known",
    "order_cue": "optional exact source substring establishing semantic order; for PERSON use first independent participation; null for relation-only actors",
    "scope_rank": "optional nonnegative integer; 0 broad/whole, 1 contained/dependent when two coordinates share one material situation",
}


class V146ARelationFirstHarnessInventoryApparatus(V126AHarnessInventoryApparatus):
    """Execute V146 primitive + compound semantics in one whole-source model turn."""

    def _normalize_integrated_class(self, source: str, cls: str, rows: Any) -> list[apparatus.Candidate]:
        if not isinstance(rows, list):
            raise apparatus.ApparatusError(f"{cls} integrated extraction must return an array")
        out: list[apparatus.Candidate] = []
        for row in rows:
            if not isinstance(row, dict):
                raise apparatus.ApparatusError(f"{cls} integrated candidate must be object")
            wording = row.get("source_wording")
            cue = row.get("source_cue")
            key = str(row.get("canonical_key") or "").strip()
            tag = str(row.get("short_tag") or "").strip()
            if not key or not tag or not isinstance(cue, str) or not cue:
                raise apparatus.ApparatusError(f"{cls} canonical_key, short_tag, and exact source_cue are required")
            if wording is None and cls not in {"PLACE", "TIME"}:
                raise apparatus.ApparatusError(f"source_wording may be null only for inferred PLACE/TIME, not {cls}")
            self._assert_exact_source(source, wording, "source_wording")
            self._assert_exact_source(source, cue, "source_cue")
            self._assert_source_near_tag(tag, wording, cue)
            anchor = self._exact_anchor(source, wording, cue, row.get("anchor_hint"))
            order_cue = row.get("order_cue")
            if order_cue is not None:
                if not isinstance(order_cue, str) or not order_cue:
                    raise apparatus.ApparatusError("order_cue must be a nonempty exact source substring or null")
                self._assert_exact_source(source, order_cue, "order_cue")
                order_anchor: int | None = source.find(order_cue)
            elif cls == "PERSON" and key != "B" and self._possessive_only_first_mention(source, wording, anchor):
                order_anchor = None
            else:
                order_anchor = anchor
            scope_rank_raw = row.get("scope_rank", 0)
            try:
                scope_rank = max(0, int(scope_rank_raw))
            except (TypeError, ValueError):
                raise apparatus.ApparatusError("scope_rank must be a nonnegative integer") from None
            out.append(apparatus.Candidate(
                unit_class=cls,
                canonical_key=key,
                short_tag=tag,
                source_wording=wording,
                source_cue=cue,
                note=row.get("note"),
                qualities_available=bool(row.get("qualities_available")),
                anchor=anchor,
                order_anchor=order_anchor,
                scope_rank=scope_rank,
            ))
        return self._merge_and_order(out, cls)

    @staticmethod
    def _key_to_ref(by_class: dict[str, list[apparatus.Candidate]], refmap: dict[str, apparatus.Candidate]) -> dict[tuple[str, str], str]:
        keymap: dict[tuple[str, str], str] = {}
        for ref, candidate in refmap.items():
            k = (candidate.unit_class, candidate.canonical_key.casefold())
            if k in keymap:
                raise apparatus.ApparatusError(f"ambiguous integrated canonical key after merge: {k}")
            keymap[k] = ref
        expected = sum(len(rows) for rows in by_class.values())
        if len(keymap) != expected:
            raise apparatus.ApparatusError("integrated key/ref map is incomplete")
        return keymap

    def _normalize_integrated_compounds(self, rows: Any, keymap: dict[tuple[str, str], str], refmap: dict[str, apparatus.Candidate]) -> list[dict[str, Any]]:
        if not isinstance(rows, list):
            raise apparatus.ApparatusError("integrated compounds must return an array")
        normalized: list[tuple[int, str, list[str], bool, Any]] = []
        for row in rows:
            if not isinstance(row, dict):
                raise apparatus.ApparatusError("integrated compound must be object")
            members = row.get("members")
            if not isinstance(members, list) or len(members) < 2:
                raise apparatus.ApparatusError(f"integrated compound requires at least two members: {members}")
            refs: list[str] = []
            for member in members:
                if not isinstance(member, dict):
                    raise apparatus.ApparatusError(f"integrated compound member must be object: {member}")
                cls = str(member.get("class") or "").strip().upper()
                key = str(member.get("canonical_key") or "").strip()
                if cls not in apparatus.CLASSES or not key:
                    raise apparatus.ApparatusError(f"invalid integrated compound member: {member}")
                ref = keymap.get((cls, key.casefold()))
                if not ref:
                    raise apparatus.ApparatusError(f"integrated compound references unknown member: {member}")
                if ref not in refs:
                    refs.append(ref)
            if len(refs) < 2:
                raise apparatus.ApparatusError(f"integrated compound collapses below two unique refs: {refs}")
            q = bool(row.get("qualities_available"))
            expression = "_".join(refs) + ("_Q" if q else "")
            anchor = min(refmap[r].anchor for r in refs)
            normalized.append((anchor, expression, refs, q, row.get("researcher_bundle")))
        dedup: dict[str, tuple[int, str, list[str], bool, Any]] = {}
        for item in normalized:
            dedup.setdefault(item[1], item)
        ordered = sorted(dedup.values(), key=lambda x: (x[0], x[1]))
        return [{
            "compound_ref": f"C{i}",
            "compound_expression": expression,
            "researcher_bundle": bundle,
            "referenced_unit_refs": refs,
            "qualities_available": q,
        } for i, (_, expression, refs, q, bundle) in enumerate(ordered, 1)]

    def _extract_integrated(self, source: str) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
        payload = {
            "task": "researcher_inventory_build_relation_first_inventory",
            "rules": V126A_BASE_RULES + "\n" + V146A_INTEGRATED_RULE,
            "source": source,
            "response_schema": {
                "classes": {cls: [_UNIT_SCHEMA] for cls in apparatus.CLASSES},
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
        raise apparatus.ApparatusError(f"integrated relation-first extraction failed after retries: {last}")

    def run(self, source: str, source_case_ref: str | None = None, researcher_interest: str | None = None, created_by_ref: str = "RI-WORKER") -> dict[str, Any]:
        if not source.strip():
            raise apparatus.ApparatusError("source is empty")
        units, compounds = self._extract_integrated(source)
        return {
            "candidate": {
                "candidate_ref": self._candidate_ref(source, source_case_ref),
                "source_case_ref": source_case_ref,
                "source_case_text": source,
                "researcher_interest": researcher_interest,
                "created_by_ref": created_by_ref,
            },
            "units": units,
            "compounds": compounds,
            "validation": {
                "source_language_preserved": True,
                "lightweight_resolution_preserved": True,
                "all_compound_refs_registered": True,
                "forbidden_work_avoided": True,
                "notes": ["V146A one-turn whole-source relation-first semantic pass plus mechanical source-span, semantic-order, ID, Q, and reference checks passed"],
            },
        }
