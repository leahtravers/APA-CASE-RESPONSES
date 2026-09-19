#!/usr/bin/env python3
"""V96 runtime adapter retaining bounded same-session transport recovery.

Semantic authority is the saved agent bootstrapped from AGENT_CONTRACT_V96.
This wrapper changes only current contract identity and recovery evidence location.
"""
from __future__ import annotations

import os
from pathlib import Path

import v95_openai_agents_adapter as v95

CONTRACT_VERSION = os.environ.get("CONTRACT_VERSION", "RI-CONTRACT-V96").strip() or "RI-CONTRACT-V96"
V96_RECOVERY_DIR = Path("researcher_inventory/runtime/v96_session_recovery")

v95.v94.v93.v92.v90.prior.base.CONTRACT_VERSION = CONTRACT_VERSION
v95.v94.v93.v92.RECOVERY_DIR = V96_RECOVERY_DIR
v95.v94.v93.v92.recovery.RECOVERY_DIR = V96_RECOVERY_DIR
v95.v94.v93.v92.v90.prior.base.recovery.RECOVERY_DIR = V96_RECOVERY_DIR

if __name__ == "__main__":
    raise SystemExit(v95.v94.v93.v92.v90.prior.base.main())
