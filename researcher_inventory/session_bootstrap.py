"""Create or refresh the dedicated Researcher Inventory saved agent and session.

Requires OPENAI_API_KEY scoped to the APA Case Responses project.
Prints only stable IDs; never prints the API key.
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
SESSION_ID_FILE = Path("researcher_inventory/runtime/session_id.txt")
CONTRACT = Path("researcher_inventory/AGENT_CONTRACT.md")


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
        # Do not emit remote bodies because they can include sensitive request context.
        raise RuntimeError(f"OpenAI request failed with HTTP {exc.code}") from None


def main():
    instructions = CONTRACT.read_text(encoding="utf-8")

    agent = request(
        "/agents",
        method="POST",
        body={
            "name": "APA Researcher Inventory",
            "model": MODEL,
            "instructions": instructions,
            "reasoning": {"effort": "high"},
            "multi_agent": {"enabled": False, "max_concurrent_subagents": 1},
            "metadata": {
                "apa_role": "researcher_inventory",
                "contract_version": "v1",
                "promotion_authority": "none",
            },
        },
    )
    agent_id = agent["id"]

    session = request(
        "/agents/sessions",
        method="POST",
        body={
            "agent_id": agent_id,
            "environment": {"type": "none"},
            "metadata": {
                "apa_session_type": "researcher_inventory",
                "contract_version": "v1",
                "candidate_desk_only": "true",
            },
        },
    )
    session_id = session["id"]

    AGENT_ID_FILE.parent.mkdir(parents=True, exist_ok=True)
    AGENT_ID_FILE.write_text(agent_id + "\n", encoding="utf-8")
    SESSION_ID_FILE.write_text(session_id + "\n", encoding="utf-8")

    print(f"agent_id={agent_id}")
    print(f"session_id={session_id}")
    print(f"model={MODEL}")


if __name__ == "__main__":
    main()
