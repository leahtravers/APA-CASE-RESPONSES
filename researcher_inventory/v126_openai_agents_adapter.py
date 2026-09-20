#!/usr/bin/env python3
"""V126 runtime adapter retaining bounded same-session transport recovery.

Semantic authority is the saved agent bootstrapped from AGENT_CONTRACT_V126.
This wrapper changes only current contract identity and recovery evidence location.
"""
from __future__ import annotations

import os
from pathlib import Path

import v125_openai_agents_adapter as v125

CONTRACT_VERSION = os.environ.get("CONTRACT_VERSION", "RI-CONTRACT-V126").strip() or "RI-CONTRACT-V126"
V126_RECOVERY_DIR = Path("researcher_inventory/runtime/v126_session_recovery")

base = v125.base
base.CONTRACT_VERSION = CONTRACT_VERSION
v125.V125_RECOVERY_DIR = V126_RECOVERY_DIR
v125.v124.v123.v122.v121.v120.v119.v118.v117.v116.v115.v114.v113.v112.v111.v110.v109.v108.v107.v100.v99.v98.v97.v96.v95.v94.v93.v92.RECOVERY_DIR = V126_RECOVERY_DIR
v125.v124.v123.v122.v121.v120.v119.v118.v117.v116.v115.v114.v113.v112.v111.v110.v109.v108.v107.v100.v99.v98.v97.v96.v95.v94.v93.v92.recovery.RECOVERY_DIR = V126_RECOVERY_DIR
base.recovery.RECOVERY_DIR = V126_RECOVERY_DIR

if __name__ == "__main__":
    raise SystemExit(base.main())
