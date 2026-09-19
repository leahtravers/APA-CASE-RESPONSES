#!/usr/bin/env python3
"""V98 runtime adapter retaining bounded same-session transport recovery.

Semantic authority is the saved agent bootstrapped from AGENT_CONTRACT_V98.
This wrapper changes only current contract identity and recovery evidence location.
"""
from __future__ import annotations

import os
from pathlib import Path

import v97_openai_agents_adapter as v97

CONTRACT_VERSION = os.environ.get("CONTRACT_VERSION", "RI-CONTRACT-V98").strip() or "RI-CONTRACT-V98"
V98_RECOVERY_DIR = Path("researcher_inventory/runtime/v98_session_recovery")

v97.v96.v95.v94.v93.v92.v90.prior.base.CONTRACT_VERSION = CONTRACT_VERSION
v97.v96.v95.v94.v93.v92.RECOVERY_DIR = V98_RECOVERY_DIR
v97.v96.v95.v94.v93.v92.recovery.RECOVERY_DIR = V98_RECOVERY_DIR
v97.v96.v95.v94.v93.v92.v90.prior.base.recovery.RECOVERY_DIR = V98_RECOVERY_DIR

if __name__ == "__main__":
    raise SystemExit(v97.v96.v95.v94.v93.v92.v90.prior.base.main())
