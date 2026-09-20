#!/usr/bin/env python3
"""V114 runtime adapter retaining bounded same-session transport recovery.

Semantic authority is the saved agent bootstrapped from AGENT_CONTRACT_V114.
This wrapper changes only current contract identity and recovery evidence location.
"""
from __future__ import annotations

import os
from pathlib import Path

import v113_openai_agents_adapter as v113

CONTRACT_VERSION = os.environ.get("CONTRACT_VERSION", "RI-CONTRACT-V114").strip() or "RI-CONTRACT-V114"
V114_RECOVERY_DIR = Path("researcher_inventory/runtime/v114_session_recovery")

base = v113.v112.v111.v110.v109.v108.v107.v100.v99.v98.v97.v96.v95.v94.v93.v92.v90.prior.base
base.CONTRACT_VERSION = CONTRACT_VERSION
v113.v112.v111.v110.v109.v108.v107.v100.v99.v98.v97.v96.v95.v94.v93.v92.RECOVERY_DIR = V114_RECOVERY_DIR
v113.v112.v111.v110.v109.v108.v107.v100.v99.v98.v97.v96.v95.v94.v93.v92.recovery.RECOVERY_DIR = V114_RECOVERY_DIR
base.recovery.RECOVERY_DIR = V114_RECOVERY_DIR

if __name__ == "__main__":
    raise SystemExit(base.main())
