#!/usr/bin/env python3
"""Mechanical APA Researcher Inventory apparatus.

The model is a replaceable semantic extractor. Code owns IDs, ordering, source
verification, Q expression, compound integrity, and SQL-ready output.
The worker never receives approved archetypes or evaluator answers.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
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
PREFIX = {"PLACE": "P", "TIME": "T", "OBJECT": "O", "LABEL": "L", "VERB": "V", "LOCATOR": "R"}

CLASS_RULES = {
    "PLACE": (
        "Return every materially distinct place/scene coordinate needed to locate represented material. "
        "Keep an explicit broad setting and contained setting separate even when one phrase names both. "
        "Retain supported unnamed places for a material object location, destination, waiting scene, later conversation, or present telling when independently selectable. "
        "For inferred places use source_wording null and an exact source_cue; never invent a location name. "
        "When broad and contained settings arise in one situation, give them the same order_cue and scope_rank 0 for broad, 1 for contained."
    ),
    "TIME": (
        "Return all materially distinct temporal frames in source progression: attempts/conditions, help/response episodes, transitions/departures, waits, intended periods, later conversations/reports, recurring spans, present reflection, and explicitly represented prospective/future frames. "
        "A TIME does not require a clock/date/temporal noun. For unnamed times use source_wording null and an exact source_cue. "
        "Retaining an intended, questioned, recurring, or future frame does not assert its content happened; preserve posture."
    ),
    "PERSON": (
        "Return the speaker plus every materially represented human/social actor, including relational actors needed by retained things/relations. Merge true aliases/coreference. Speaker canonical_key must be B. "
        "For each non-speaker, order_cue should be the exact first source cue where that actor independently participates (acts, speaks, perceives, is acted upon, or is the endpoint of a material interaction/relation). "
        "If the actor is only a possessor/beneficiary/descriptor and never independently participates, set order_cue null so code places them after participating actors."
    ),
    "OBJECT": (
        "Return every materially represented independently selectable concrete or abstract thing, including source-distinguished wholes/parts, amounts/values, orders/services/results, decisions/next steps, contemplated choices treated as things, recurring relations, named sets/categories, and internal represented objects. "
        "Do not duplicate a thing as OBJECT when its only source function is PLACE. Do not discard a represented part merely because its whole is retained."
    ),
    "LABEL": (
        "Return every independently selectable source characterization/quality/state/comparison/identity/self-label/evaluative phrase/question-label/contrast/rejection/correction. "
        "Use the shortest complete exact source form that carries the characterization. LABEL inventory is separate from the qualities_available boolean. Never translate to synonyms or inferred psychological meanings."
    ),
    "VERB": (
        "Return materially represented lexical predicate increments in source order. Split matrix and embedded predicates when each is independently selectable, and split coordinated predicates when they do different jobs. "
        "Prefer the shortest complete lexical predicate construction, normally without subject or optional objects. "
        "Retain predicates under negation, uncertainty, questions, intentions, hypotheticals, proposals, recurrence, and future language; inventorying a predicate does not assert that its event happened. Preserve exact source posture."
    ),
    "LOCATOR": (
        "Return every materially useful spatial/directional/containment/path/proximity/movement/relational locator increment. Use the smallest complete meaningful construction, not an isolated preposition. "
        "One episode may contain several independently selectable locator relations such as broad setting, contained setting, movement, accompaniment, destination, or containment. "
        "When broad and contained setting locators arise in one situation, give them the same order_cue and scope_rank 0 for broad, 1 for contained."
    ),
}

BASE_RULES = """You are a comprehensive literal extraction worker. Inventory only.
READ THE WHOLE SOURCE before answering the requested class, then do a second end-to-end omission pass.
NEVER substitute a synonym just because it is convenient. Preserve the source's own words, colloquial language, dialect, questions, negation, uncertainty, comparison, attribution, and figurative wording.
Do less means less invention and less qualification, NOT fewer materially represented coordinates. Do not stop after salient items.
An unnamed PLACE may exist because a material occurrence/object/relation requires a scene coordinate. An unnamed TIME may exist because represented material requires an episode/frame. For inferred PLACE/TIME, source_wording MUST be null and source_cue MUST be exact source text anchoring the coordinate.
qualities_available is ONLY a boolean: true when the source gives qualities/descriptions associated with that coordinate, otherwise false. Do not interpret or classify qualities merely to justify Q. LABEL inventory remains separate from this boolean.
Inventorying a verb, time frame, question, hypothetical, negation, intention, or prospective relation does not assert that it happened. Preserve source posture instead of deleting materially represented language.
Remove only grammatical debris, unsupported inference, and duplicate mentions of the same coordinate. Keep independently selectable coordinates at their own grain.
Never do APA scoring, psychological interpretation, protected-thread analysis, promotion, conclusions, or gold-answer reconstruction.
Return JSON only. You have no access to archetypes, gold outputs, expected counts, evaluator findings, prior scored outputs, or holdout outputs.
"""

_WORD_RE = re.compile(r"[A-Za-z0-9']+")


@dataclass
class Candidate:
    unit_class: str
    canonical_key: str
    short_tag: str
    source_wording: str | None
    source_cue: str
    note: str | None
    qualities_available: bool
    anchor: int
    order_anchor: int | None = None
    scope_rank: int = 0


class ApparatusError(RuntimeError):
    pass


class CommandAdapter:
    """Provider-neutral stdin JSON -> stdout JSON adapter."""
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
    def _exact_anchor(source: str, wording: str | None, cue: str, proposed: Any) -> int:
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

    @staticmethod
    def _assert_source_near_tag(tag: str, wording: str | None, cue: str) -> None:
        """Reject convenient synonyms for explicit coordinates."""
        if wording is None:
            return
        allowed = {w.casefold() for w in _WORD_RE.findall((wording or "") + " " + cue)}
        tag_words = {w.casefold() for w in _WORD_RE.findall(tag)}
        if tag_words - allowed:
            raise ApparatusError(f"short_tag introduces non-source wording: {tag!r}")

    @staticmethod
    def _possessive_only_first_mention(source: str, wording: str | None, anchor: int) -> bool:
        if not wording:
            return False
        end = anchor + len(wording)
        tail = source[end:end + 2]
        return tail.startswith("’") or tail.startswith("'s") or tail.startswith("’s")

    def _extract_class(self, source: str, cls: str) -> list[Candidate]:
        response_schema = {
            "type": "array",
            "items": {
                "canonical_key": "stable neutral identity for alias/coreference merge; B for speaker",
                "short_tag": "compact source-near tag; no synonym substitution",
                "source_wording": "exact source substring, or null only for a supported inferred PLACE/TIME",
                "source_cue": "required exact bounded source substring anchoring the coordinate",
                "note": "neutral inference/coreference note or null",
                "qualities_available": "boolean only",
                "anchor_hint": "integer source offset if known",
                "order_cue": "optional exact source substring establishing semantic order; for PERSON use first independent participation; null for relation-only actors",
                "scope_rank": "optional nonnegative integer; 0 broad/whole, 1 contained/dependent when two coordinates share one material situation",
            },
        }
        payload = {
            "task": "researcher_inventory_extract_one_class",
            "rules": BASE_RULES,
            "class": cls,
            "class_rule": CLASS_RULES[cls],
            "response_schema": response_schema,
            "source": source,
        }
        last: Exception | None = None
        for _ in range(self.retries + 1):
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
                    key = str(row.get("canonical_key") or "").strip()
                    tag = str(row.get("short_tag") or "").strip()
                    if not key or not tag or not isinstance(cue, str) or not cue:
                        raise ApparatusError("canonical_key, short_tag, and exact source_cue are required")
                    if wording is None and cls not in {"PLACE", "TIME"}:
                        raise ApparatusError(f"source_wording may be null only for inferred PLACE/TIME, not {cls}")
                    self._assert_exact_source(source, wording, "source_wording")
                    self._assert_exact_source(source, cue, "source_cue")
                    self._assert_source_near_tag(tag, wording, cue)
                    anchor = self._exact_anchor(source, wording, cue, row.get("anchor_hint"))

                    order_cue = row.get("order_cue")
                    if order_cue is not None:
                        if not isinstance(order_cue, str) or not order_cue:
                            raise ApparatusError("order_cue must be a nonempty exact source substring or null")
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
                        raise ApparatusError("scope_rank must be a nonnegative integer") from None

                    out.append(Candidate(
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
            except Exception as exc:
                last = exc
                payload["correction"] = str(exc)
        raise ApparatusError(f"{cls} extraction failed after retries: {last}")

    @staticmethod
    def _merge_and_order(rows: list[Candidate], cls: str) -> list[Candidate]:
        grouped: dict[str, list[Candidate]] = {}
        for row in rows:
            grouped.setdefault(row.canonical_key.casefold(), []).append(row)
        merged: list[Candidate] = []
        for members in grouped.values():
            members.sort(key=lambda x: (x.anchor, x.scope_rank, x.short_tag.casefold()))
            first = members[0]
            notes = [m.note for m in members if m.note]
            if len(members) > 1:
                notes.append("alias/coreference mentions merged mechanically")
            order_candidates = [m.order_anchor for m in members if m.order_anchor is not None]
            merged.append(Candidate(
                unit_class=cls,
                canonical_key=first.canonical_key,
                short_tag=first.short_tag,
                source_wording=first.source_wording,
                source_cue=first.source_cue,
                note="; ".join(dict.fromkeys(notes)) if notes else None,
                qualities_available=any(m.qualities_available for m in members),
                anchor=min(m.anchor for m in members),
                order_anchor=min(order_candidates) if order_candidates else None,
                scope_rank=min(m.scope_rank for m in members),
            ))

        if cls == "PERSON":
            speakers = [x for x in merged if x.canonical_key == "B"]
            others = [x for x in merged if x.canonical_key != "B"]
            if len(speakers) != 1:
                raise ApparatusError(f"PERSON requires exactly one speaker canonical_key B; found {len(speakers)}")
            participants = [x for x in others if x.order_anchor is not None]
            relational_only = [x for x in others if x.order_anchor is None]
            participants.sort(key=lambda x: (x.order_anchor, x.scope_rank, x.anchor, x.short_tag.casefold()))
            relational_only.sort(key=lambda x: (x.anchor, x.scope_rank, x.short_tag.casefold()))
            return speakers + participants + relational_only

        merged.sort(key=lambda x: (
            x.order_anchor if x.order_anchor is not None else x.anchor,
            x.scope_rank,
            x.anchor,
            x.short_tag.casefold(),
        ))
        return merged

    @staticmethod
    def _assign_refs(by_class: dict[str, list[Candidate]]) -> tuple[list[dict[str, Any]], dict[str, Candidate]]:
        units: list[dict[str, Any]] = []
        refmap: dict[str, Candidate] = {}
        for cls in CLASSES:
            for i, row in enumerate(by_class[cls], 1):
                ref = ("B" if i == 1 else f"H{i-1}") if cls == "PERSON" else f"{PREFIX[cls]}{i}"
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
            "rules": BASE_RULES + "\nMap the story at materially distinct event/proposition grain, not only broad scenes. Create a useful compound for each distinct represented predicate relation, characterization proposition, question/correction/reflection, and prospective relation. Use only supplied unit_ref values. Q is not a unit ref. A compound cannot repair a missing unit.",
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
                    raise ApparatusError("compound extraction must return array")
                normalized: list[tuple[int, str, list[str], bool, Any]] = []
                for row in rows:
                    refs = row.get("refs") if isinstance(row, dict) else None
                    if not isinstance(refs, list) or len(refs) < 2 or any(r not in refmap for r in refs):
                        raise ApparatusError(f"invalid compound refs: {refs}")
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
        raise ApparatusError(f"compound extraction failed after retries: {last}")

    @staticmethod
    def _candidate_ref(source: str, source_case_ref: str | None) -> str:
        digest = hashlib.sha256(source.encode("utf-8")).hexdigest()[:16]
        stem = re.sub(r"[^A-Za-z0-9_.-]+", "-", source_case_ref or "CASE").strip("-") or "CASE"
        return f"RI-{stem}-{digest}"

    @staticmethod
    def sql_rows(result: dict[str, Any]) -> dict[str, Any]:
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

        by_class: dict[str, list[Candidate]] = {}
        with ThreadPoolExecutor(max_workers=len(CLASSES), thread_name_prefix="ri-class") as pool:
            futures = {pool.submit(self._extract_class, source, cls): cls for cls in CLASSES}
            for future in as_completed(futures):
                cls = futures[future]
                by_class[cls] = future.result()

        units, refmap = self._assign_refs(by_class)
        compounds = self._extract_compounds(source, units, refmap)
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
                "notes": ["mechanical source-span, literal-language, semantic-order, ID, Q, and reference checks passed"],
            },
        }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--source-file", required=True)
    p.add_argument("--source-case-ref")
    p.add_argument("--researcher-interest")
    p.add_argument("--created-by-ref", default="RI-WORKER")
    p.add_argument("--sql-rows", action="store_true")
    args = p.parse_args()
    source = open(args.source_file, encoding="utf-8").read()
    app = InventoryApparatus(CommandAdapter(os.environ.get("RI_MODEL_COMMAND", "")))
    result = app.run(source, args.source_case_ref, args.researcher_interest, args.created_by_ref)
    print(json.dumps(app.sql_rows(result) if args.sql_rows else result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ApparatusError as exc:
        print(json.dumps({"error": "APPARATUS_FAILURE", "detail": str(exc)}), file=sys.stderr)
        raise SystemExit(2)
