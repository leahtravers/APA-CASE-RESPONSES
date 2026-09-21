#!/usr/bin/env python3
"""V131 runtime adapter retaining the established V126A contract-subordinate harness."""
from __future__ import annotations

import os
from pathlib import Path

import v126_openai_agents_adapter as v126

CONTRACT_VERSION = os.environ.get("CONTRACT_VERSION", "RI-CONTRACT-V131").strip() or "RI-CONTRACT-V131"
V131_RECOVERY_DIR = Path("researcher_inventory/runtime/v131_session_recovery")

base = v126.base
base.CONTRACT_VERSION = CONTRACT_VERSION
v126.V126_RECOVERY_DIR = V131_RECOVERY_DIR
v126.v125.V125_RECOVERY_DIR = V131_RECOVERY_DIR
v126.v125.v124.v123.v122.v121.v120.v119.v118.v117.v116.v115.v114.v113.v112.v111.v110.v109.v108.v107.v100.v99.v98.v97.v96.v95.v94.v93.v92.RECOVERY_DIR = V131_RECOVERY_DIR
v126.v125.v124.v123.v122.v121.v120.v119.v118.v117.v116.v115.v114.v113.v112.v111.v110.v109.v108.v107.v100.v99.v98.v97.v96.v95.v94.v93.v92.recovery.RECOVERY_DIR = V131_RECOVERY_DIR
base.recovery.RECOVERY_DIR = V131_RECOVERY_DIR

if __name__ == "__main__":
    raise SystemExit(base.main())
