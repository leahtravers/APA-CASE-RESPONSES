#!/usr/bin/env python3
"""V53 harness-isolated adapter. Durable V53 contract is sole semantic authority."""
from pathlib import Path
import v52_openai_agents_adapter as base

base.recovery.RECOVERY_DIR = Path("researcher_inventory/runtime/v53_session_recovery")
_original_attention = base._attention_for


def _attention_for(bounded: dict) -> str:
    prior = _original_attention(bounded)
    task = bounded.get("task")
    if task == "researcher_inventory_extract_one_class":
        return prior + (
            "\nV53 RELATION-INTEGRITY CHECK: coverage is not syntactic census. After coverage, merge relation-internal fragments into the smallest COMPLETE semantic coordinate. "
            "Do not create new TIME for each predicate inside one episode; do not promote locator-only/figurative/object-position wording to PLACE without an independent physical scene; "
            "do not promote ordinary complements/arguments/question scaffolding into OBJECT/LABEL/LOCATOR. VERB relation identity outranks token minimalism: keep one source relation together even when it contains infinitival, particle, complement, modal, negation, serial, or coordinated material. Split only genuinely independently revisitable relations."
        )
    if task == "researcher_inventory_build_lightweight_compounds":
        return prior + "\nV53 RELATION-INTEGRITY CHECK: do not create nested subset alternatives or duplicate decompositions of one relation instance."
    return prior


base._attention_for = _attention_for

if __name__ == "__main__":
    raise SystemExit(base.main())
