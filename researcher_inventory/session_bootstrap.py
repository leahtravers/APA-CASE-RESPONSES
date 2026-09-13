"""Create the replaceable semantic extractor used by inventory_apparatus.py."""
from __future__ import annotations

import hashlib
import json
import os
import urllib.error
import urllib.request
from pathlib import Path

API = "https://api.openai.com/v1"
MODEL = os.environ.get("OPENAI_MODEL", "gpt-5.6-sol")
CONTRACT_VERSION = os.environ.get("CONTRACT_VERSION", "RI-CONTRACT-V18")
AGENT_ID_FILE = Path("researcher_inventory/runtime/extractor_agent_id.txt")
CONTRACT_FILE = Path(os.environ.get("RI_CONTRACT_FILE", "researcher_inventory/AGENT_CONTRACT_V18.md"))

BOOT_PREFIX = """You are the APA Researcher Inventory semantic extraction subroutine.
The durable contract below is your complete behavioral authority.
You receive one bounded JSON request at a time and return only the JSON value required by that request's response_schema.
Return JSON only. Do not explain. Do not add fields that were not requested.
The worker never receives archetypes, gold outputs, evaluator findings, expected counts, prior scored outputs, or holdout outputs.

DURABLE CONTRACT:
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
    data = json.dumps(body, ensure_ascii=False).encode("utf-8") if body is not None else None
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
    if not CONTRACT_FILE.exists():
        raise RuntimeError(f"durable contract file is missing: {CONTRACT_FILE}")
    contract = CONTRACT_FILE.read_text(encoding="utf-8")
    contract_sha = hashlib.sha256(contract.encode("utf-8")).hexdigest()
    instructions = BOOT_PREFIX + contract
    agent = request(
        "/agents",
        method="POST",
        body={
            "name": f"APA Researcher Inventory Semantic Extractor {CONTRACT_VERSION}",
            "model": MODEL,
            "instructions": instructions,
            "metadata": {
                "apa_role": "researcher_inventory_semantic_extractor",
                "contract_version": CONTRACT_VERSION,
                "contract_sha256": contract_sha,
                "contract_file": str(CONTRACT_FILE),
                "promotion_authority": "none",
                "archetype_access": "forbidden",
                "holdout_access": "forbidden",
            },
        },
    )
    AGENT_ID_FILE.parent.mkdir(parents=True, exist_ok=True)
    AGENT_ID_FILE.write_text(agent["id"] + "\n", encoding="utf-8")
    print(f"extractor_agent_id={agent['id']}")
    print(f"model={MODEL}")
    print(f"contract_version={CONTRACT_VERSION}")
    print(f"contract_file={CONTRACT_FILE}")
    print(f"contract_sha256={contract_sha}")


if __name__ == "__main__":
    main()
