"""Create the replaceable semantic extractor used by inventory_apparatus.py."""
from __future__ import annotations
import json, os, urllib.error, urllib.request
from pathlib import Path

API = "https://api.openai.com/v1"
MODEL = os.environ.get("OPENAI_MODEL", "gpt-5.6-sol")
CONTRACT_VERSION = os.environ.get("CONTRACT_VERSION", "RI-CONTRACT-V9")
AGENT_ID_FILE = Path("researcher_inventory/runtime/extractor_agent_id.txt")

INSTRUCTIONS = """You are a bounded Researcher Inventory extraction subroutine.
Return only the JSON value requested. Do not explain.
Read the whole source.
Use exact source wording. Never substitute synonyms, clean up wording, or interpret figurative language.
A place may exist even when unnamed if an actual event occurred there. In that case source_wording must be null and the tag must be neutral, such as place of meeting or place B is waiting.
A time may exist even when no date or clock time is given if an actual event occurred. In that case source_wording may be null and the tag must be a neutral episode label.
qualities_available is only a boolean indicating whether source qualities/descriptions are available. Do not unpack or classify those qualities.
Prefer actual represented people, actual happenings, actual objects, labels, relations, places, and times. Do not multiply rhetorical, generic, speculative, or hypothetical coordinates unless the request specifically requires them.
When uncertain, return fewer coordinates rather than inventing or over-qualifying.
You never see or use archetypes, gold outputs, expected counts, evaluator findings, or prior scored outputs.
You do not assign final IDs, write databases, score APA material, interpret psychology, or promote records.
"""

def request(path: str, method: str = "GET", body=None):
    key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not key:
        raise RuntimeError("OPENAI_API_KEY is required")
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json", "Accept": "application/json", "OpenAI-Beta": "agents=v1"}
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
            detail += " " + json.dumps({"type": err.get("type"), "code": err.get("code"), "param": err.get("param"), "message": (err.get("message") or "")[:500]}, ensure_ascii=False)
        except Exception:
            pass
        raise RuntimeError(f"OpenAI request failed: {detail}") from None

def main():
    agent = request("/agents", method="POST", body={
        "name": f"APA Researcher Inventory Semantic Extractor {CONTRACT_VERSION}",
        "model": MODEL,
        "instructions": INSTRUCTIONS,
        "metadata": {"apa_role": "researcher_inventory_semantic_extractor", "contract_version": CONTRACT_VERSION, "promotion_authority": "none", "archetype_access": "forbidden"},
    })
    AGENT_ID_FILE.parent.mkdir(parents=True, exist_ok=True)
    AGENT_ID_FILE.write_text(agent["id"] + "\n", encoding="utf-8")
    print(f"extractor_agent_id={agent['id']}")
    print(f"model={MODEL}")
    print(f"contract_version={CONTRACT_VERSION}")

if __name__ == "__main__":
    main()
