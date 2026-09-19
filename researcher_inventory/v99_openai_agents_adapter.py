#!/usr/bin/env python3
"""V99 runtime adapter retaining bounded same-session transport recovery.

Semantic authority is the saved agent bootstrapped from AGENT_CONTRACT_V99.
This wrapper changes only current contract identity and recovery evidence location.
"""
from __future__ import annotations

import os
from pathlib import Path

import v98_openai_agents_adapter as v98

CONTRACT_VERSION = os.environ.get("CONTRACT_VERSION", "RI-CONTRACT-V99").strip() or "RI-CONTRACT-V99"
V99_RECOVERY_DIR = Path("researcher_inventory/runtime/v99_session_recovery")

v98.v97.v96.v95.v94.v93.v92.v90.prior.base.CONTRACT_VERSION = CONTRACT_VERSION
v98.v97.v96.v95.v94.v93.v92.RECOVERY_DIR = V99_RECOVERY_DIR
v98.v97.v96.v95.v94.v93.v92.recovery.RECOVERY_DIR = V99_RECOVERY_DIR
v98.v97.v96.v95.v94.v93.v92.v90.prior.base.recovery.RECOVERY_DIR = V99_RECOVERY_DIR

if __name__ == "__main__":
    raise SystemExit(v98.v97.v96.v95.v94.v93.v92.v90.prior.base.main())
