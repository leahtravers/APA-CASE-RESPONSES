#!/usr/bin/env python3
"""V122 runtime adapter retaining bounded same-session transport recovery.

Semantic authority is the saved agent bootstrapped from AGENT_CONTRACT_V122.
This wrapper changes only current contract identity and recovery evidence location.
"""
from __future__ import annotations

import os
from pathlib import Path

import v121_openai_agents_adapter as v121

CONTRACT_VERSION = os.environ.get("CONTRACT_VERSION", "RI-CONTRACT-V122").strip() or "RI-CONTRACT-V122"
V122_RECOVERY_DIR = Path("researcher_inventory/runtime/v122_session_recovery")

base = v121.base
base.CONTRACT_VERSION = CONTRACT_VERSION
v121.v120.v119.v118.v117.v116.v115.v114.v113.v112.v111.v110.v109.v108.v107.v100.v99.v98.v97.v96.v95.v94.v93.v92.RECOVERY_DIR = V122_RECOVERY_DIR
v121.v120.v119.v118.v117.v116.v115.v114.v113.v112.v111.v110.v109.v108.v107.v100.v99.v98.v97.v96.v95.v94.v93.v92.recovery.RECOVERY_DIR = V122_RECOVERY_DIR
base.recovery.RECOVERY_DIR = V122_RECOVERY_DIR

if __name__ == "__main__":
    raise SystemExit(base.main())
