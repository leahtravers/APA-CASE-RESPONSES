#!/usr/bin/env python3
"""V57 contract-version-correct isolated agent adapter.

Reuses the V55 transport/session implementation only; V57 durable contract remains the semantic authority. Gold/evaluator/holdout material is never sent to the worker.
"""
import os
from pathlib import Path
import v55_openai_agents_adapter as base

base.CONTRACT_VERSION = os.environ.get("CONTRACT_VERSION", "RI-CONTRACT-V57").strip() or "RI-CONTRACT-V57"
base.recovery.RECOVERY_DIR = Path("researcher_inventory/runtime/v57_session_recovery")

if __name__ == "__main__":
    raise SystemExit(base.main())
