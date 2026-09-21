#!/usr/bin/env python3
"""V126A harness-only correction for worker-facing prompt composition.

This module changes request semantics only enough to remove contradictory legacy
prompt text. AGENT_CONTRACT_V126 remains the sole durable semantic authority.
It contains no archetype rows, expected counts, evaluator findings, or holdout text.
"""
from __future__ import annotations

from typing import Any

from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v66_harness_correction import V66HarnessInventoryApparatus
from researcher_inventory.v126a_task_rules import V126A_COMPOUND_RULE


class V126AHarnessInventoryApparatus(V66HarnessInventoryApparatus):
    """Preserve V66 mechanical/evaluator behavior with contract-subordinate compounds."""

    def _extract_compounds(self, source: str, units: list[dict[str, Any]], refmap):
        payload = {
            "task": "researcher_inventory_build_lightweight_compounds",
            "rules": apparatus.BASE_RULES + "\n" + V126A_COMPOUND_RULE,
            "source": source,
            "units": units,
            "response_schema": [{
                "refs": "array of at least two existing unit_ref strings in semantic/source order",
                "researcher_bundle": "concise source-near bundle or null",
                "qualities_available": "boolean only",
            }],
        }
        last: Exception | None = None
        for _ in range(self.retries + 1):
            try:
                rows = self.adapter.ask(payload)
                if not isinstance(rows, list):
                    raise apparatus.ApparatusError("compound extraction must return array")
                normalized: list[tuple[int, str, list[str], bool, Any]] = []
                for row in rows:
                    refs = row.get("refs") if isinstance(row, dict) else None
                    if not isinstance(refs, list) or len(refs) < 2 or any(r not in refmap for r in refs):
                        raise apparatus.ApparatusError(f"invalid compound refs: {refs}")
                    refs = list(dict.fromkeys(refs))
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
                    "compound_expression": expr,
                    "researcher_bundle": bundle,
                    "referenced_unit_refs": refs,
                    "qualities_available": q,
                } for i, (_, expr, refs, q, bundle) in enumerate(ordered, 1)]
            except Exception as exc:
                last = exc
                payload["correction"] = str(exc)
        raise apparatus.ApparatusError(f"compound extraction failed after retries: {last}")
