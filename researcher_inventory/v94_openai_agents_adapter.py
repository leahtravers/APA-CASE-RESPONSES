#!/usr/bin/env python3
"""V94 runtime adapter retaining V93/V92 bounded same-session transport recovery.

Semantic authority is the saved agent bootstrapped from AGENT_CONTRACT_V94.
This wrapper changes contract/version identity and evidence location only. The proven
V93/V92 same-session transient recovery implementation remains unchanged.
"""
from __future__ import annotations

import os
from pathlib import Path

import v93_openai_agents_adapter as v93

CONTRACT_VERSION = os.environ.get("CONTRACT_VERSION", "RI-CONTRACT-V94").strip() or "RI-CONTRACT-V94"
V94_RECOVERY_DIR = Path("researcher_inventory/runtime/v94_session_recovery")

# Rebind only current contract identity and evidence home; retain the proven adapter path.
v93.v92.v90.prior.base.CONTRACT_VERSION = CONTRACT_VERSION
v93.v92.RECOVERY_DIR = V94_RECOVERY_DIR
v93.v92.recovery.RECOVERY_DIR = V94_RECOVERY_DIR
v93.v92.v90.prior.base.recovery.RECOVERY_DIR = V94_RECOVERY_DIR

if __name__ == "__main__":
    raise SystemExit(v93.v92.v90.prior.base.main())
