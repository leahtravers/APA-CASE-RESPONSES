"""Create the replaceable semantic extractor used by inventory_apparatus.py.

The extractor does not own IDs, ordering, schema normalization, compounds, SQL rows,
or access to archetypes. It answers bounded JSON extraction requests only.
"""
from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from pathlib import Path

API = "https://api.openai.com/v1"
MODEL = os.environ.get("OPENAI_MODEL", "gpt-5.6-sol")
CONTRACT_VERSION = os.environ.get("CONTRACT_VERSION", "RI-CONTRACT-V8")
AGENT_ID_FILE = Path("researcher_inventory/runtime/extractor_agent_id.txt")

INSTRUCTIONS = """You are the APA Researcher Inventory semantic extraction subroutine.
You receive one bounded JSON request at a time and return only the JSON value required by that request's response_schema.
You never see or use approved archetypes, gold outputs, expected answers, expected counts, evaluator findings, or prior scored outputs.
You do not assign final canonical IDs, decide database writes, promote records, score APA material, interpret psychology, or perform protected-thread analysis.
Preserve exact source wording and source posture. Read the complete supplied source before extracting the requested class.
Follow the supplied class rule and retention rule literally. Return JSON only, with no Markdown or explanation.
"""


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
            detail += " " + json.dumps({
                "type": err.get("type"),
                "code": err.get("code"),
                "param": err.get("param"),
                "message": (err.get("message") or "")[:500],
            }, ensure_ascii=False)
        except Exception:
            pass
        raise RuntimeError(f"OpenAI request failed: {detail}") from None


def main():
    agent = request(
        "/agents",
        method="POST",
        body={
            "name": f"APA Researcher Inventory Semantic Extractor {CONTRACT_VERSION}",
            "model": MODEL,
            "instructions": INSTRUCTIONS,
            "metadata": {
                "apa_role": "researcher_inventory_semantic_extractor",
                "contract_version": CONTRACT_VERSION,
                "promotion_authority": "none",
                "archetype_access": "forbidden",
            },
        },
    )
    AGENT_ID_FILE.parent.mkdir(parents=True, exist_ok=True)
    AGENT_ID_FILE.write_text(agent["id"] + "\n", encoding="utf-8")
    print(f"extractor_agent_id={agent['id']}")
    print(f"model={MODEL}")
    print(f"contract_version={CONTRACT_VERSION}")


if __name__ == "__main__":
    main()
