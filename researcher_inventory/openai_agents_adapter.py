#!/usr/bin/env python3
"""OpenAI Agents adapter for the provider-neutral inventory apparatus."""
from __future__ import annotations
import json, os, sys, time, urllib.error, urllib.parse, urllib.request
from pathlib import Path

API = "https://api.openai.com/v1"
AGENT_ID_FILE = Path("researcher_inventory/runtime/extractor_agent_id.txt")

def request(path: str, method: str = "GET", body=None):
    key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not key:
        raise RuntimeError("OPENAI_API_KEY is required")
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json", "Accept": "application/json", "OpenAI-Beta": "agents=v1"}
    data = json.dumps(body, ensure_ascii=False).encode("utf-8") if body is not None else None
    req = urllib.request.Request(API + path, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=180) as response:
            raw = response.read()
            return json.loads(raw) if raw.strip() else None
    except urllib.error.HTTPError as exc:
        detail = f"HTTP {exc.code}"
        try:
            raw = exc.read(8192)
            payload = json.loads(raw) if raw else {}
            err = payload.get("error", {}) if isinstance(payload, dict) else {}
            detail += ": " + (err.get("message") or "")[:500]
        except Exception:
            pass
        raise RuntimeError(detail) from None

def wait(session_id: str, timeout: int = 360):
    deadline = time.time() + timeout
    while time.time() < deadline:
        state = request(f"/agents/sessions/{session_id}")
        status = state.get("status")
        if status == "idle":
            return
        if status in ("failed", "requires_action"):
            raise RuntimeError(f"session terminal status {status}")
        time.sleep(2)
    raise RuntimeError("session timeout")

def final_answer(session_id: str) -> str:
    query = urllib.parse.urlencode({"order":"asc", "limit":100})
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
        raise RuntimeError("no final answer")
    return "\n".join(answers).strip()

def main() -> int:
    payload = json.load(sys.stdin)
    agent_id = AGENT_ID_FILE.read_text(encoding="utf-8").strip()
    prompt = (
        "Execute only this bounded extraction. Return ONLY the requested JSON. "
        "Be literal and sparse: no synonyms, no polishing, no interpretation, no extra qualifications. "
        "Unnamed places and unnamed times are allowed when an actual represented event requires them, but never invent source wording. "
        "qualities_available is only yes/no availability. Prefer actual represented people and actual happenings. "
        "When uncertain, do less. You have no access to archetypes or expected answers.\n\nREQUEST JSON:\n"
        + json.dumps(payload, ensure_ascii=False)
    )
    session = request("/agents/sessions", method="POST", body={
        "agent_id": agent_id,
        "environment": {"type":"none"},
        "input": prompt,
        "metadata": {"apa_session_type":"researcher_inventory_semantic_subroutine"},
    })
    session_id = session["id"]
    wait(session_id)
    raw = final_answer(session_id)
    if raw.startswith("```"):
        lines = raw.splitlines()
        if lines and lines[0].startswith("```"): lines = lines[1:]
        if lines and lines[-1].strip() == "```": lines = lines[:-1]
        raw = "\n".join(lines).strip()
    value = json.loads(raw)
    sys.stdout.write(json.dumps(value, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
