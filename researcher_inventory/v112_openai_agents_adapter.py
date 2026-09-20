#!/usr/bin/env python3
"""V112 runtime adapter retaining bounded same-session transport recovery.

Semantic authority is the saved agent bootstrapped from AGENT_CONTRACT_V112.
This wrapper changes only current contract identity and recovery evidence location.
"""
from __future__ import annotations

import os
from pathlib import Path

import v111_openai_agents_adapter as v111

CONTRACT_VERSION = os.environ.get("CONTRACT_VERSION", "RI-CONTRACT-V112").strip() or "RI-CONTRACT-V112"
V112_RECOVERY_DIR = Path("researcher_inventory/runtime/v112_session_recovery")

v111.v110.v109.v108.v107.v100.v99.v98.v97.v96.v95.v94.v93.v92.v90.prior.base.CONTRACT_VERSION = CONTRACT_VERSION
v111.v110.v109.v108.v107.v100.v99.v98.v97.v96.v95.v94.v93.v92.RECOVERY_DIR = V112_RECOVERY_DIR
v111.v110.v109.v108.v107.v100.v99.v98.v97.v96.v95.v94.v93.v92.recovery.RECOVERY_DIR = V112_RECOVERY_DIR
v111.v110.v109.v108.v107.v100.v99.v98.v97.v96.v95.v94.v93.v92.v90.prior.base.recovery.RECOVERY_DIR = V112_RECOVERY_DIR

if __name__ == "__main__":
    raise SystemExit(v111.v110.v109.v108.v107.v100.v99.v98.v97.v96.v95.v94.v93.v92.v90.prior.base.main())
