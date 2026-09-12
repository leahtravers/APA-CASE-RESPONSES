"""Revise the Researcher Inventory behavioral contract from failed archetype tests.

This trainer never sees the sealed holdout. It may revise only AGENT_CONTRACT.md.
The approved archetypes and exact output schema remain fixed external authorities.
"""
from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request
from pathlib import Path

API = "https://api.openai.com/v1"
MODEL = os.environ.get("OPENAI_MODEL", "gpt-5.6-sol")
CONTRACT = Path("researcher_inventory/AGENT_CONTRACT.md")
SCHEMA = Path("researcher_inventory/output_schema.json")
SPEC = Path("researcher_inventory/tests/archetype_spec.json")
RESULTS = Path("researcher_inventory/runtime/test_results.json")
HISTORY = Path("researcher_inventory/training_contracts")


def request(body):
    key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not key:
        raise RuntimeError("OPENAI_API_KEY is required")
    req = urllib.request.Request(
        API + "/responses",
        data=json.dumps(body).encode(),
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=240) as response:
            return json.loads(response.read())
    except urllib.error.HTTPError as exc:
        detail = exc.read(4096).decode("utf-8", "replace")
        raise RuntimeError(f"contract revision request failed HTTP {exc.code}: {detail[:500]}") from None


def output_text(response: dict) -> str:
    if isinstance(response.get("output_text"), str):
        return response["output_text"].strip()
    parts = []
    for item in response.get("output", []):
        for content in item.get("content", []) if isinstance(item, dict) else []:
            if content.get("type") == "output_text":
                parts.append(content.get("text", ""))
    text = "\n".join(parts).strip()
    if not text:
        raise RuntimeError("trainer returned no output text")
    return text


def bounded_failures(results):
    out = []
    for run in results:
        if run.get("pass"):
            continue
        out.append({
            "fixture": run.get("fixture"),
            "findings": [
                {
                    "class": f.get("finding_class"),
                    "observed": f.get("observed_behavior"),
                }
                for f in run.get("findings", [])[:80]
            ],
        })
    return out


def main():
    current = CONTRACT.read_text(encoding="utf-8")
    schema = SCHEMA.read_text(encoding="utf-8")
    spec = SPEC.read_text(encoding="utf-8")
    results = json.loads(RESULTS.read_text(encoding="utf-8"))
    failures = bounded_failures(results)
    if not failures:
        print("no contract revision needed")
        return

    prompt = f"""You are the contract trainer for one narrowly scoped APA Researcher Inventory agent.

Revise the behavioral contract so a fresh GPT-5.6 Sol agent generalizes the APPROVED ARCHETYPE BEHAVIOR more reliably. Return the COMPLETE replacement Markdown contract only. No code fences and no commentary.

HARD RULES:
- The exact JSON schema is immutable. Never rename fields or weaken validation.
- The approved archetypes are authorities for resolution, source fidelity, coordinate classes and lightweight compound behavior.
- Infer GENERAL PROCEDURAL RULES from failures. Do not memorize coupon/oil-change case-specific IDs, row text or answers into the contract.
- Never mention, infer, request or use any sealed holdout case.
- Preserve the seven classes PLACE/TIME/PERSON/OBJECT/LABEL/VERB/LOCATOR.
- Preserve Q/qualities_available semantics.
- Preserve uncertainty, questions, negation, hypotheticals and source idiom exactly enough to remain selectable later.
- Do not introduce APA parsing, protected-thread analysis, psychological interpretation, scoring, promotion, APA IDs or Oval Office writes.
- Prefer a short deterministic procedure with a mandatory whole-case first pass, class-by-class inventory pass, compound pass, and source-fidelity audit.
- A candidate researcher inventory may be wrong; it must remain provisional.
- Do not weaken the contract merely to make tests pass.

CURRENT CONTRACT:
{current}

IMMUTABLE OUTPUT SCHEMA:
{schema}

ARCHETYPE SPECIFICATION:
{spec}

CURRENT FAILED TEST FINDINGS:
{json.dumps(failures, ensure_ascii=False, indent=2)}
"""
    response = request({"model": MODEL, "input": prompt})
    revised = output_text(response)
    if revised.startswith("```"):
        revised = revised.strip("`").strip()
        if revised.lower().startswith("markdown"):
            revised = revised[8:].lstrip()
    if len(revised) < 2500:
        raise RuntimeError("trainer revision suspiciously short; refusing replacement")
    required_tokens = ["PLACE", "TIME", "PERSON", "OBJECT", "LABEL", "VERB", "LOCATOR", "qualities_available", "candidate", "units", "compounds", "validation"]
    missing = [x for x in required_tokens if x not in revised]
    if missing:
        raise RuntimeError(f"trainer revision omitted required concepts: {missing}")

    HISTORY.mkdir(parents=True, exist_ok=True)
    stamp = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    (HISTORY / f"predecessor_{stamp}.md").write_text(current, encoding="utf-8")
    CONTRACT.write_text(revised.rstrip() + "\n", encoding="utf-8")
    print(f"contract revised; predecessor archived at {stamp}")


if __name__ == "__main__":
    main()
