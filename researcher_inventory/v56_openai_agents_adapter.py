#!/usr/bin/env python3
"""V56 contract-version-correct isolated agent adapter.

Reuses the V55 transport/session implementation only; V56 durable contract and task rules remain the semantic authority. Gold/evaluator/holdout material is never sent to the worker.
"""
import os
from pathlib import Path
import researcher_inventory.v55_openai_agents_adapter as base

base.CONTRACT_VERSION = os.environ.get("CONTRACT_VERSION", "RI-CONTRACT-V56").strip() or "RI-CONTRACT-V56"
base.recovery.RECOVERY_DIR = Path("researcher_inventory/runtime/v56_session_recovery")

if __name__ == "__main__":
    raise SystemExit(base.main())
