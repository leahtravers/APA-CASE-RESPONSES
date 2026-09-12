"""Run repeatability fixtures against the dedicated Researcher Inventory saved agent.

This runner does not write to Supabase. It tests behavior first.
"""
from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

API = "https://api.openai.com/v1"
AGENT_ID_FILE = Path("researcher_inventory/runtime/agent_id.txt")
FIXTURES = Path("researcher_inventory/tests/fixtures.json")
RESULTS = Path("researcher_inventory/runtime/test_results.json")


def request(path: str, method: str = "GET", body=None):
    key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not key:
        raise RuntimeError("OPENAI_API_KEY is required")
    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "OpenAI-Beta": "agents=v1",
    }
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(API + path, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=120) as response:
            raw = response.read()
            return json.loads(raw) if raw.strip() else None
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f"OpenAI request failed with HTTP {exc.code}") from None


def wait_for_terminal(session_id: str, timeout_seconds: int = 240):
    deadline = time.time() + timeout_seconds
    while time.time() < deadline:
        state = request(f"/agents/sessions/{session_id}")
        status = state.get("status")
        if status == "idle":
            return
        if status in ("failed", "requires_action"):
            raise RuntimeError(f"Session terminal status: {status}")
        time.sleep(2)
    raise RuntimeError("Session did not return to idle before timeout")


def final_answer(session_id: str) -> str:
    query = urllib.parse.urlencode({"order": "asc", "limit": 100})
    page = request(f"/agents/sessions/{session_id}/items?{query}")
    answers = []
    for item in page.get("data", []):
        if item.get("type") != "message" or item.get("role") != "assistant":
            continue
        if item.get("status") != "completed" or item.get("phase") != "final_answer":
            continue
        for part in item.get("content", []):
            if part.get("type") == "output_text":
                answers.append(part.get("text", ""))
    if not answers:
        raise RuntimeError("No completed assistant final answer found")
    return "\n".join(answers).strip()


def validate_structure(payload: dict, fixture: dict):
    failures = []
    expected_classes = {"PLACE", "TIME", "PERSON", "OBJECT", "LABEL", "VERB", "LOCATOR"}
    unit_classes = {u.get("unit_class") for u in payload.get("units", [])}
    if not unit_classes.issubset(expected_classes):
        failures.append("invented unit class")

    refs = {u.get("unit_ref") for u in payload.get("units", [])}
    for compound in payload.get("compounds", []):
        for ref in compound.get("referenced_unit_refs", []):
            if ref != "Q" and ref not in refs:
                failures.append(f"compound references unknown unit: {ref}")

    searchable = json.dumps(payload, ensure_ascii=False).lower()
    for phrase in fixture.get("must_preserve", []):
        if phrase.lower() not in searchable:
            failures.append(f"missing preserved source phrase: {phrase}")
    for phrase in fixture.get("must_not_introduce", []):
        if phrase.lower() in searchable:
            failures.append(f"introduced forbidden normalization: {phrase}")

    counts = {}
    for u in payload.get("units", []):
        counts[u.get("unit_class")] = counts.get(u.get("unit_class"), 0) + 1
    max_units = fixture.get("max_units")
    if max_units is not None and len(payload.get("units", [])) > max_units:
        failures.append(f"over-granular: {len(payload.get('units', []))} units > {max_units}")
    min_units = fixture.get("min_units")
    if min_units is not None and len(payload.get("units", [])) < min_units:
        failures.append(f"under-inventory: {len(payload.get('units', []))} units < {min_units}")

    validation = payload.get("validation", {})
    for key in (
        "source_language_preserved",
        "lightweight_resolution_preserved",
        "all_compound_refs_registered",
        "forbidden_work_avoided",
    ):
        if validation.get(key) is not True:
            failures.append(f"self-validation failed: {key}")
    return failures, counts


def run_fixture(agent_id: str, fixture: dict, iteration: int):
    prompt = (
        "Prepare researcher inventory. Return ONLY the JSON object required by your contract.\n\n"
        f"Candidate ref: {fixture['candidate_ref']}-R{iteration}\n"
        f"Researcher interest: {fixture.get('researcher_interest') or 'none supplied'}\n\n"
        "CASE TEXT:\n" + fixture["case_text"]
    )
    session = request(
        "/agents/sessions",
        method="POST",
        body={
            "agent_id": agent_id,
            "environment": {"type": "none"},
            "input": prompt,
            "metadata": {
                "apa_session_type": "researcher_inventory_test",
                "fixture": fixture["name"],
                "iteration": str(iteration),
            },
        },
    )
    session_id = session["id"]
    wait_for_terminal(session_id)
    raw = final_answer(session_id)
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError:
        return {
            "fixture": fixture["name"],
            "iteration": iteration,
            "session_id": session_id,
            "pass": False,
            "failures": ["final answer was not bare valid JSON"],
        }
    failures, counts = validate_structure(payload, fixture)
    return {
        "fixture": fixture["name"],
        "iteration": iteration,
        "session_id": session_id,
        "pass": not failures,
        "failures": failures,
        "unit_counts": counts,
        "unit_total": len(payload.get("units", [])),
        "compound_total": len(payload.get("compounds", [])),
    }


def main():
    agent_id = AGENT_ID_FILE.read_text(encoding="utf-8").strip()
    fixtures = json.loads(FIXTURES.read_text(encoding="utf-8"))
    repetitions = int(os.environ.get("TEST_REPETITIONS", "2"))
    results = []
    for fixture in fixtures:
        for iteration in range(1, repetitions + 1):
            result = run_fixture(agent_id, fixture, iteration)
            results.append(result)
            print(json.dumps(result, ensure_ascii=False))
    RESULTS.parent.mkdir(parents=True, exist_ok=True)
    RESULTS.write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    if not all(r["pass"] for r in results):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
