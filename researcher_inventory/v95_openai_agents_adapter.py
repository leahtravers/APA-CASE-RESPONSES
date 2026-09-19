#!/usr/bin/env python3
"""V95 runtime adapter retaining V94/V93/V92 bounded same-session transport recovery.

Semantic authority is the saved agent bootstrapped from AGENT_CONTRACT_V95.
This wrapper changes contract/version identity and evidence location only. Proven
transport/session recovery remains unchanged.
"""
from __future__ import annotations

import os
from pathlib import Path

import v94_openai_agents_adapter as v94

CONTRACT_VERSION = os.environ.get("CONTRACT_VERSION", "RI-CONTRACT-V95").strip() or "RI-CONTRACT-V95"
V95_RECOVERY_DIR = Path("researcher_inventory/runtime/v95_session_recovery")

# Rebind only current contract identity and evidence home; retain the proven adapter path.
v94.v93.v92.v90.prior.base.CONTRACT_VERSION = CONTRACT_VERSION
v94.v93.v92.RECOVERY_DIR = V95_RECOVERY_DIR
v94.v93.v92.recovery.RECOVERY_DIR = V95_RECOVERY_DIR
v94.v93.v92.v90.prior.base.recovery.RECOVERY_DIR = V95_RECOVERY_DIR

if __name__ == "__main__":
    raise SystemExit(v94.v93.v92.v90.prior.base.main())
