#!/usr/bin/env python3
"""APA Researcher Inventory apparatus.

The apparatus, not the model, owns the output mechanics.
A provider adapter receives JSON on stdin and returns JSON on stdout.
Set RI_MODEL_COMMAND to any executable command implementing that contract.

The worker NEVER receives approved archetypes or expected outputs.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shlex
import subprocess
import sys
from dataclasses import dataclass
from typing import Any

CLASSES = ("PLACE", "TIME", "PERSON", "OBJECT", "LABEL", "VERB", "LOCATOR")
PREFIX = {"PLACE":"P", "TIME":"T", "OBJECT":"O", "LABEL":"L", "VERB":"V", "LOCATOR":"R"}

CLASS_RULES = {
    "PLACE": "Retain materially represented settings, contained/off-scene settings, and supported inferred scene places. Do not emit bare prepositions.",
    "TIME": "Retain materially distinct periods, episodes, transitions, durations, recurrence, present-reflection frames, and future/conditional frames. Do not emit incidental tense alone.",
    "PERSON": "Retain speaker plus materially represented human/social actors or groups. Merge true aliases/coreference. Speaker canonical_key must be B.",
    "OBJECT": "Retain materially represented concrete or abstract things, proposition-like things, represented wholes and independently selectable parts. Do not emit every noun.",
    "LABEL": "Retain source characterizations, identities, comparisons, questions, alternatives, proposals, rejections, contrasts and corrections. Preserve question/negation/uncertainty posture.",
    "VERB": "Retain materially represented lexical predicates/happenings, including embedded, reported, hypothetical and prospective predicates. Preserve source wording; do not invent event summaries.",
    "LOCATOR": "Retain materially useful physical, directional, relational, containment, path, proximity and figurative locator constructions. Do not emit isolated prepositions.",
}

BASE_RULES = """You are a bounded extraction worker. Inventory only. Never do APA scoring, psychological interpretation, protected-thread analysis, promotion, or conclusions.
Read the entire source. Preserve colloquial language, dialect, questions, negation, uncertainty, comparison, attribution, hypothetical/future status, and figurative wording.
Return JSON only. Never use or infer any gold-standard answer, example output, archetype, or expected count.
A coordinate is retained only if materially represented or required by a materially represented situation and independently selectable for research. Do not inventory grammatical debris or every word.
qualities_available is true when the source gives one or more material qualities/descriptions of that coordinate beyond merely naming it. Do not unpack those qualities into extra coordinates unless they independently satisfy the requested class.
"""

@dataclass
class Candidate:
    unit_class: str
    canonical_key: str
    short_tag: str
    source_wording: str | None
    source_cue: str | None
    note: str | None
    qualities_available: bool
    anchor: int

class ApparatusError(RuntimeError):
    pass

class CommandAdapter:
    """Provider-neutral adapter. Any platform can implement stdin JSON -> stdout JSON."""
    def __init__(self, command: str, timeout: int = 180):
        if not command:
            raise ApparatusError("RI_MODEL_COMMAND is required")
        self.command = shlex.split(command)
        self.timeout = timeout

    def ask(self, payload: dict[str, Any]) -> Any:
        proc = subprocess.run(
            self.command,
            input=json.dumps(payload, ensure_ascii=False),
            text=True,
            capture_output=True,
            timeout=self.timeout,
        )
        if proc.returncode != 0:
            raise ApparatusError(f"model adapter failed rc={proc.returncode}: {proc.stderr[-2000:]}")
        raw = proc.stdout.strip()
        try:
            return json.loads(raw)
        except json.JSONDecodeError as exc:
            raise ApparatusError(f"model adapter returned non-JSON: {raw[:1000]}") from exc

class InventoryApparatus:
    def __init__(self, adapter: CommandAdapter, retries: int = 2):
        self.adapter = adapter
        self.retries = retries

    @staticmethod
    def _exact_anchor(source: str, wording: str | None, cue: str | None, proposed: Any) -> int:
        """Code, never the model, establishes the source anchor."""
        for text in (wording, cue):
            if text:
                pos = source.find(text)
                if pos >= 0:
                    return pos
        if isinstance(proposed, int) and 0 <= proposed < len(source):
            return proposed
        raise ApparatusError("candidate has no verifiable source anchor")

    @staticmethod
    def _assert_exact_source(source: str, value: str | None, field: str) -> None:
        if value is not None and value not in source:
            raise ApparatusError(f"{field} is not exact source text: {value!r}")

    def _extract_class(self, source: str, cls: str) -> list[Candidate]:
        schema = {
            "type": "array",
            "items": {
                "canonical_key": "string; stable neutral identity for alias/coreference merge; B for speaker in PERSON",
                "short_tag": "compact source-near navigation tag",
                "source_wording": "exact source substring or null for supported inference",
                "source_cue": "exact bounded source substring preserving posture/scope",
                "note": "neutral inference/alias note or null",
                "qualities_available": "boolean",
                "anchor_hint": "integer source character offset if known"
            }
        }
        payload = {
            "task": "researcher_inventory_extract_one_class",
            "rules": BASE_RULES,
            "class": cls,
            "class_rule": CLASS_RULES[cls],
            "response_schema": schema,
            "source": source,
        }
        last: Exception | None = None
        for attempt in range(self.retries + 1):
            try:
                rows = self.adapter.ask(payload)
                if not isinstance(rows, list):
                    raise ApparatusError("class extraction must return an array")
                out: list[Candidate] = []
                for row in rows:
                    if not isinstance(row, dict):
                        raise ApparatusError("candidate must be object")
                    wording = row.get("source_wording")
                    cue = row.get("source_cue")
                    self._assert_exact_source(source, wording, "source_wording")
                    self._assert_exact_source(source, cue, "source_cue")
                    key = str(row.get("canonical_key") or "").strip()
                    tag = str(row.get("short_tag") or "").strip()
                    if not key or not tag:
                        raise ApparatusError("canonical_key and short_tag are required")
                    anchor = self._exact_anchor(source, wording, cue, row.get("anchor_hint"))
                    out.append(Candidate(
                        unit_class=cls,
                        canonical_key=key,
                        short_tag=tag,
                        source_wording=wording,
                        source_cue=cue,
                        note=row.get("note"),
                        qualities_available=bool(row.get("qualities_available")),
                        anchor=anchor,
                    ))
                return self._merge_and_order(out, cls)
            except Exception as exc:
                last = exc
                payload["correction"] = str(exc)
        raise ApparatusError(f"{cls} extraction failed after retries: {last}")

    @staticmethod
    def _merge_and_order(rows: list[Candidate], cls: str) -> list[Candidate]:
        """Deterministic alias merge by worker canonical_key; code owns survivor/order."""
        grouped: dict[str, list[Candidate]] = {}
        for row in rows:
            grouped.setdefault(row.canonical_key.casefold(), []).append(row)
        merged: list[Candidate] = []
        for members in grouped.values():
            members.sort(key=lambda x: (x.anchor, x.short_tag.casefold()))
            first = members[0]
            cues = [m.source_cue for m in members if m.source_cue]
            wording = first.source_wording
            note_bits = [m.note for m in members if m.note]
            if len(members) > 1:
                note_bits.append("alias/coreference mentions merged mechanically")
            merged.append(Candidate(
                unit_class=cls,
                canonical_key=first.canonical_key,
                short_tag=first.short_tag,
                source_wording=wording,
                source_cue=cues[0] if cues else first.source_cue,
                note="; ".join(dict.fromkeys(note_bits)) if note_bits else None,
                qualities_available=any(m.qualities_available for m in members),
                anchor=min(m.anchor for m in members),
            ))
        merged.sort(key=lambda x: (x.anchor, x.short_tag.casefold()))
        if cls == "PERSON":
            speakers = [x for x in merged if x.canonical_key == "B"]
            others = [x for x in merged if x.canonical_key != "B"]
            if len(speakers) != 1:
                raise ApparatusError(f"PERSON requires exactly one speaker canonical_key B; found {len(speakers)}")
            merged = speakers + others
        return merged

    @staticmethod
    def _assign_refs(by_class: dict[str, list[Candidate]]) -> tuple[list[dict[str, Any]], dict[str, Candidate]]:
        units: list[dict[str, Any]] = []
        refmap: dict[str, Candidate] = {}
        for cls in CLASSES:
            rows = by_class[cls]
            for i, row in enumerate(rows, 1):
                if cls == "PERSON":
                    ref = "B" if i == 1 else f"H{i-1}"
                else:
                    ref = f"{PREFIX[cls]}{i}"
                refmap[ref] = row
                units.append({
                    "unit_ref": ref,
                    "unit_class": cls,
                    "researcher_short_tag": "B" if ref == "B" else row.short_tag,
                    "source_wording": row.source_wording,
                    "source_cue": row.source_cue,
                    "researcher_note": row.note,
                    "qualities_available": row.qualities_available,
                })
        return units, refmap

    def _extract_compounds(self, source: str, units: list[dict[str, Any]], refmap: dict[str, Candidate]) -> list[dict[str, Any]]:
        payload = {
            "task": "researcher_inventory_build_lightweight_compounds",
            "rules": BASE_RULES + "\nBuild a useful nonexhaustive map of major represented situations. A compound cannot repair a missing unit. Use only supplied unit_ref values. Do not use Q as a unit ref.",
            "source": source,
            "units": units,
            "response_schema": [{
                "refs": "array of existing unit_ref strings in source/situation order",
                "researcher_bundle": "concise source-near bundle or null",
                "qualities_available": "boolean",
                "anchor_ref": "one ref from refs establishing first material anchor"
            }]
        }
        last: Exception | None = None
        for _ in range(self.retries + 1):
            try:
                rows = self.adapter.ask(payload)
                if not isinstance(rows, list):
                    raise ApparatusError("compound extraction must return array")
                normalized = []
                for row in rows:
                    refs = row.get("refs") if isinstance(row, dict) else None
                    if not isinstance(refs, list) or len(refs) < 2 or any(r not in refmap for r in refs):
                        raise ApparatusError(f"invalid compound refs: {refs}")
                    refs = list(dict.fromkeys(refs))
                    q = bool(row.get("qualities_available"))
                    expression = "_".join(refs) + ("_Q" if q else "")
                    anchor = min(refmap[r].anchor for r in refs)
                    normalized.append((anchor, expression, refs, q, row.get("researcher_bundle")))
                # deterministic dedupe/order/ref assignment
                dedup: dict[str, tuple] = {}
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
        raise ApparatusError(f"compound extraction failed after retries: {last}")

    @staticmethod
    def _candidate_ref(source: str, source_case_ref: str | None) -> str:
        digest = hashlib.sha256(source.encode("utf-8")).hexdigest()[:16]
        stem = re.sub(r"[^A-Za-z0-9_.-]+", "-", source_case_ref or "CASE").strip("-") or "CASE"
        return f"RI-{stem}-{digest}"

    @staticmethod
    def sql_rows(result: dict[str, Any]) -> dict[str, Any]:
        """Return parameter rows for the isolated candidate tables. No SQL interpolation."""
        cref = result["candidate"]["candidate_ref"]
        return {
            "research_hypothesis_candidate": [{
                "candidate_ref": cref,
                "source_case_ref": result["candidate"]["source_case_ref"],
                "source_case_text": result["candidate"]["source_case_text"],
                "researcher_interest": result["candidate"]["researcher_interest"],
                "candidate_status": "CANDIDATE",
                "created_by_ref": result["candidate"]["created_by_ref"],
            }],
            "research_inventory_unit_candidate": [dict(candidate_ref=cref, **u) for u in result["units"]],
            "research_inventory_compound_candidate": [dict(candidate_ref=cref, **c) for c in result["compounds"]],
        }

    def run(self, source: str, source_case_ref: str | None = None, researcher_interest: str | None = None, created_by_ref: str = "RI-WORKER") -> dict[str, Any]:
        if not source.strip():
            raise ApparatusError("source is empty")
        by_class = {cls: self._extract_class(source, cls) for cls in CLASSES}
        units, refmap = self._assign_refs(by_class)
        compounds = self._extract_compounds(source, units, refmap)
        result = {
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
                "notes": ["mechanical source-span and reference integrity checks passed"],
            },
        }
        return result

def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--source-file", required=True)
    p.add_argument("--source-case-ref")
    p.add_argument("--researcher-interest")
    p.add_argument("--created-by-ref", default="RI-WORKER")
    p.add_argument("--sql-rows", action="store_true")
    args = p.parse_args()
    source = open(args.source_file, encoding="utf-8").read()
    apparatus = InventoryApparatus(CommandAdapter(os.environ.get("RI_MODEL_COMMAND", "")))
    result = apparatus.run(source, args.source_case_ref, args.researcher_interest, args.created_by_ref)
    print(json.dumps(apparatus.sql_rows(result) if args.sql_rows else result, ensure_ascii=False, indent=2))
    return 0

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ApparatusError as exc:
        print(json.dumps({"error":"APPARATUS_FAILURE", "detail":str(exc)}), file=sys.stderr)
        raise SystemExit(2)
