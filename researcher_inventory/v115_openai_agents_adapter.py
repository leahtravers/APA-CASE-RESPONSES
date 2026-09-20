#!/usr/bin/env python3
"""V115 runtime adapter retaining bounded same-session transport recovery.

Semantic authority is the saved agent bootstrapped from AGENT_CONTRACT_V115.
This wrapper changes only current contract identity and recovery evidence location.
"""
from __future__ import annotations

import os
from pathlib import Path

import v114_openai_agents_adapter as v114

CONTRACT_VERSION = os.environ.get("CONTRACT_VERSION", "RI-CONTRACT-V115").strip() or "RI-CONTRACT-V115"
V115_RECOVERY_DIR = Path("researcher_inventory/runtime/v115_session_recovery")

base = v114.v113.v112.v111.v110.v109.v108.v107.v100.v99.v98.v97.v96.v95.v94.v93.v92.v90.prior.base
base.CONTRACT_VERSION = CONTRACT_VERSION
v114.v113.v112.v111.v110.v109.v108.v107.v100.v99.v98.v97.v96.v95.v94.v93.v92.RECOVERY_DIR = V115_RECOVERY_DIR
v114.v113.v112.v111.v110.v109.v108.v107.v100.v99.v98.v97.v96.v95.v94.v93.v92.recovery.RECOVERY_DIR = V115_RECOVERY_DIR
base.recovery.RECOVERY_DIR = V115_RECOVERY_DIR

if __name__ == "__main__":
    raise SystemExit(base.main())
