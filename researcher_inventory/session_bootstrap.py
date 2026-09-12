"""Create the reusable Researcher Inventory saved agent.

Requires OPENAI_API_KEY scoped to the APA Case Responses project.
Actual researcher-inventory sessions are created per case with initial input.
Prints only stable IDs and bounded API error metadata; never prints the API key.
"""
from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from pathlib import Path

API = "https://api.openai.com/v1"
MODEL = os.environ.get("OPENAI_MODEL", "gpt-5.6-sol")
AGENT_ID_FILE = Path("researcher_inventory/runtime/agent_id.txt")
CONTRACT = Path("researcher_inventory/AGENT_CONTRACT.md")
OUTPUT_SCHEMA = Path("researcher_inventory/output_schema.json")


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
        with urllib.request.urlopen(req, timeout=90) as response:
            raw = response.read()
            return json.loads(raw) if raw.strip() else None
    except urllib.error.HTTPError as exc:
        detail = f"HTTP {exc.code}"
        try:
            raw = exc.read(8192)
            payload = json.loads(raw) if raw else {}
            err = payload.get("error", {}) if isinstance(payload, dict) else {}
            safe = {
                "type": err.get("type"),
                "code": err.get("code"),
                "param": err.get("param"),
                "message": (err.get("message") or "")[:500],
            }
            detail += " " + json.dumps(safe, ensure_ascii=False)
        except Exception:
            pass
        raise RuntimeError(f"OpenAI request failed: {detail}") from None


def main():
    contract = CONTRACT.read_text(encoding="utf-8")
    schema = OUTPUT_SCHEMA.read_text(encoding="utf-8")
    instructions = (
        contract
        + "\n\n## EXACT OUTPUT SCHEMA\n"
        + "The final answer MUST use these exact top-level keys and field names. Do not invent aliases such as unit_rows, compound_rows, validation_report, candidate_metadata, ref, source_text, researcher_tag, composition, or member_refs.\n\n"
        + schema
    )
    agent = request(
        "/agents",
        method="POST",
        body={
            "name": "APA Researcher Inventory",
            "model": MODEL,
            "instructions": instructions,
            "metadata": {
                "apa_role": "researcher_inventory",
                "contract_version": os.environ.get("CONTRACT_VERSION", "RI-CONTRACT-V1"),
                "promotion_authority": "none",
            },
        },
    )
    agent_id = agent["id"]
    AGENT_ID_FILE.parent.mkdir(parents=True, exist_ok=True)
    AGENT_ID_FILE.write_text(agent_id + "\n", encoding="utf-8")
    print(f"agent_id={agent_id}")
    print(f"model={MODEL}")
    print("session_policy=per_case_with_initial_input")


if __name__ == "__main__":
    main()
