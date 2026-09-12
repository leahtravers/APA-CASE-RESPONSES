"""Run sealed Case 5 through the mechanical apparatus only after calibration passes.

The semantic extractor receives the story and general rules only. The hidden rubric
is loaded only after the apparatus has produced its result.
"""
from __future__ import annotations

import json
import os
import re
import time
import unicodedata
from pathlib import Path

from researcher_inventory.inventory_apparatus import InventoryApparatus, CommandAdapter

SEALED = Path("researcher_inventory/tests/holdout/CASE_5.sealed.txt")
RUBRIC = Path("researcher_inventory/tests/holdout/CASE_5.eval.json")
RESULT = Path("researcher_inventory/runtime/holdout_result.json")
CONTRACT_VERSION = os.environ.get("CONTRACT_VERSION", "RI-CONTRACT-V8")
MODEL_REF = os.environ.get("OPENAI_MODEL", "unknown")


def norm(v):
    s = unicodedata.normalize("NFKC", str(v or "")).lower()
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip()


def case_text():
    text = SEALED.read_text(encoding="utf-8")
    start = text.index("Ugh,")
    return text[start:].strip()


def evaluate(payload, rubric):
    failures = []
    counts = {}
    refs = set()
    for unit in payload["units"]:
        refs.add(unit["unit_ref"])
        counts[unit["unit_class"]] = counts.get(unit["unit_class"], 0) + 1
    for cls, minimum in rubric["minimum_class_counts"].items():
        if counts.get(cls, 0) < minimum:
            failures.append(("UNDER_GRANULARITY", f"{cls} count {counts.get(cls,0)} < {minimum}"))
    for compound in payload["compounds"]:
        for ref in compound["referenced_unit_refs"]:
            if ref not in refs:
                failures.append(("BAD_COMPOUND", f"unknown compound ref {ref}"))
    searchable = norm(json.dumps(payload, ensure_ascii=False))
    for phrase in rubric["must_preserve"]:
        if norm(phrase) not in searchable:
            failures.append(("SOURCE_FLATTENING", f"missing preserved phrase {phrase!r}"))
    for cue in rubric["required_uncertainty_cues"]:
        if norm(cue) not in searchable:
            failures.append(("SOURCE_FLATTENING", f"lost uncertainty/hypothetical cue {cue!r}"))
    for phrase in rubric["must_not_introduce"]:
        if norm(phrase) in searchable:
            failures.append(("OVER_NORMALIZATION", f"introduced forbidden assertion {phrase!r}"))
    return failures


def main():
    source = case_text()
    rubric = json.loads(RUBRIC.read_text(encoding="utf-8"))
    app = InventoryApparatus(CommandAdapter(os.environ.get("RI_MODEL_COMMAND", "python researcher_inventory/openai_agents_adapter.py")), retries=2)
    started = time.time()
    payload = None
    failures = []
    try:
        payload = app.run(source, "CASE-5-HOLDOUT", rubric.get("researcher_interest"), "RI-APPARATUS-HOLDOUT")
        failures = evaluate(payload, rubric)
    except Exception as exc:
        failures = [("OTHER", f"runtime failure: {type(exc).__name__}: {exc}")]
    result = {
        "training_run_ref": f"HOLDOUT-case5-{int(started)}",
        "contract_version_ref": CONTRACT_VERSION,
        "fixture": "case_5_holdout",
        "model_ref": MODEL_REF,
        "run_status": "COMPLETED" if not failures else "FAILED",
        "raw_output": payload,
        "findings": [{"finding_class": kind, "observed_behavior": msg} for kind, msg in failures],
        "pass": not failures,
        "started_unix": started,
        "finished_unix": time.time(),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({k:v for k,v in result.items() if k != "raw_output"}, ensure_ascii=False))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
