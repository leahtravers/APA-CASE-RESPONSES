#!/usr/bin/env python3
"""V58 contract-version-correct isolated agent adapter.

Reuses the V55 transport/session implementation only; V58 durable contract remains the semantic authority. Gold/evaluator/holdout material is never sent to the worker.
"""
import os
from pathlib import Path
import v55_openai_agents_adapter as base

base.CONTRACT_VERSION = os.environ.get("CONTRACT_VERSION", "RI-CONTRACT-V58").strip() or "RI-CONTRACT-V58"
base.recovery.RECOVERY_DIR = Path("researcher_inventory/runtime/v58_session_recovery")

if __name__ == "__main__":
    raise SystemExit(base.main())
