#!/usr/bin/env python3
"""V100 runtime adapter retaining bounded same-session transport recovery.

Semantic authority is the saved agent bootstrapped from AGENT_CONTRACT_V100.
This wrapper changes only current contract identity and recovery evidence location.
"""
from __future__ import annotations

import os
from pathlib import Path

import v99_openai_agents_adapter as v99

CONTRACT_VERSION = os.environ.get("CONTRACT_VERSION", "RI-CONTRACT-V100").strip() or "RI-CONTRACT-V100"
V100_RECOVERY_DIR = Path("researcher_inventory/runtime/v100_session_recovery")

v99.v98.v97.v96.v95.v94.v93.v92.v90.prior.base.CONTRACT_VERSION = CONTRACT_VERSION
v99.v98.v97.v96.v95.v94.v93.v92.RECOVERY_DIR = V100_RECOVERY_DIR
v99.v98.v97.v96.v95.v94.v93.v92.recovery.RECOVERY_DIR = V100_RECOVERY_DIR
v99.v98.v97.v96.v95.v94.v93.v92.v90.prior.base.recovery.RECOVERY_DIR = V100_RECOVERY_DIR

if __name__ == "__main__":
    raise SystemExit(v99.v98.v97.v96.v95.v94.v93.v92.v90.prior.base.main())
