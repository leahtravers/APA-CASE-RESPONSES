#!/usr/bin/env python3
"""V21 bounded adapter with class-local closure verification.

The worker sees only its installed durable V21 contract, neutral apparatus rules, the
bounded source/request, and one unscored provisional output from another stateless
pass under the same contract. No archetype, evaluator finding, expected count,
scored output, or sealed holdout material is supplied.
"""
from __future__ import annotations

import json
import sys

from openai_agents_adapter import AGENT_ID_FILE, final_answer, request, wait


CLASS_ATTENTION = {
    "PLACE": (
        "Complete the WHERE coordinate set first. Preserve explicit settings/positions plus materially distinct unnamed situation positions and represented movement destinations. Physical overlap does not force situation positions to merge. Then prune only aliases, identical where-jobs, hypothetical-only pseudo-places, state metaphors, or direction wording that is only LOCATOR."
    ),
    "TIME": (
        "Complete the EPISODE/FRAME set first. Preserve materially distinct subepisodes, standing spans, intentions, recurrences, later reports, present reflection and prospective frames when the discourse establishes them separately. Then prune only duplicate frames and verb/clause-derived pseudo-times."
    ),
    "PERSON": (
        "Complete the represented human actor/participant set, including material human relation endpoints. Resolve aliases, pronouns, kinship, and stable groups before pruning duplicates."
    ),
    "OBJECT": (
        "Complete independently selectable referents first, including concrete/abstract/internal/figurative referents plus material choices, decisions, next-step alternatives, and standing/recurring relations treated as things. Cross-class overlap is allowed. Then prune proposition wrappers, pronoun repeats, metadiscourse, and nominalization with no independent referent."
    ),
    "LABEL": (
        "Complete source-applied characterizations first. Preserve the shortest COMPLETE phrase including material polarity/negation/qualification. A phrase may also be a VERB/LOCATOR/PLACE if it independently characterizes. Then strip only non-characterizing scaffolding and duplicates."
    ),
    "VERB": (
        "Complete MATERIAL RELATION EDGES first. Preserve distinct nested/embedded/modal/locative/reporting/perception/thought/state/purpose relations when each connects represented coordinates. Do not merge material edges just because one syntax contains another. Then prune bare auxiliaries/support/markers with no relation job. Cross-class overlap is allowed."
    ),
    "LOCATOR": (
        "Complete independent locating/context relations first: setting, position, path, direction, origin/destination, movement, containment, proximity, recurring context, and genuine figurative/mental location. A phrase may also be a VERB or LABEL. Then prune isolated prepositions, routine argument marking, temporal-only wording, and characterization-only wording."
    ),
}

COMPOUND_ATTENTION = (
    "Build compounds only after units are final. Identify each materially distinct proposition first. Include every retained unit that materially participates and include the specific local PLACE/TIME/LOCATOR frame that governs the proposition even when established earlier in nearby discourse. Local frame inheritance can continue while the same episode/frame remains in force, but stop it at real frame/discourse transitions. Never propagate a broad/global frame through the whole story merely because it is generally true. Keep one proposition together; do not make arbitrary subsets or quality-only fragments."
)


def _bounded_request(payload: dict) -> dict:
    keep = {
        "task", "rules", "class", "class_rule", "response_schema", "source",
        "units", "candidate", "researcher_interest", "created_by_ref", "correction",
    }
    return {k: v for k, v in payload.items() if k in keep}


def _attention_for(bounded: dict) -> str:
    task = bounded.get("task")
    if task == "researcher_inventory_extract_one_class":
        cls = bounded.get("class")
        return (
            "Read the complete source. Use COVERAGE FIRST, PRUNING SECOND. First enumerate silently every materially represented coordinate with a real job for this class, including local coordinates that appear in only one episode/proposition and coordinates whose source span also performs another class's job. Then prune only same-class aliases/coreferential duplicates, identical class jobs at the same semantic coordinate, bare grammatical debris, and invented rows. Do NOT optimize for fewest rows and do NOT delete a coordinate merely because another class carries related meaning. "
            "ORDER BY EARLIEST MATERIAL SEMANTIC ANCHOR after alias/coreference resolution. "
            "COPY SOURCE FIELDS EXACTLY: explicit source_wording and source_cue must be contiguous character-for-character source substrings with original punctuation, apostrophes, hyphens, capitalization, spelling, and dialect. For a materially required unnamed PLACE/TIME only, source_wording may be null. "
            + CLASS_ATTENTION.get(cls, "")
        )
    if task == "researcher_inventory_build_lightweight_compounds":
        return COMPOUND_ATTENTION
    return "Apply the installed V21 durable contract and supplied neutral apparatus rules exactly to this bounded task."


def _session(agent_id: str, prompt: str, session_type: str):
    session = request(
        "/agents/sessions",
        method="POST",
        body={
            "agent_id": agent_id,
            "environment": {"type": "none"},
            "input": prompt,
            "metadata": {"apa_session_type": session_type},
        },
    )
    session_id = session["id"]
    wait(session_id)
    raw = final_answer(session_id)
    if raw.startswith("```"):
        lines = raw.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        raw = "\n".join(lines).strip()
    return json.loads(raw)


def main() -> int:
    payload = json.load(sys.stdin)
    agent_id = AGENT_ID_FILE.read_text(encoding="utf-8").strip()
    bounded = _bounded_request(payload)
    attention = _attention_for(bounded)

    initial_prompt = (
        "Execute only this bounded request under your installed durable V21 contract and supplied neutral apparatus rules. Return ONLY the JSON value required by response_schema. Do not infer or reconstruct any archetype, expected answer, expected count, evaluator preference, prior scored output, sealed holdout source, or holdout output.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
    )
    provisional = _session(agent_id, initial_prompt, "researcher_inventory_v21_initial")

    verify_prompt = (
        "Perform a separate stateless V21 verification. The provisional output is unscored and non-authoritative. Re-read the complete source and rebuild the requested result from the durable contract. COVERAGE FIRST: identify every missing class-local coordinate with a real job, even if it overlaps another class or is local to one episode/proposition, and add it. PRUNING SECOND: remove only same-class aliases, true duplicate class jobs, bare grammar debris, or invented coordinates. Preserve legitimate cross-class overlap. Resolve aliases/coreference, exact source copying, and earliest semantic ordering. Return ONLY the complete replacement JSON required by response_schema.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False) + "\n\n"
        "PROVISIONAL_UNSCORED_OUTPUT:\n" + json.dumps(provisional, ensure_ascii=False)
    )
    verified = _session(agent_id, verify_prompt, "researcher_inventory_v21_verification")
    sys.stdout.write(json.dumps(verified, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
