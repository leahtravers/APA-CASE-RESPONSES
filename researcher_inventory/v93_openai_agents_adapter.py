#!/usr/bin/env python3
"""V93 runtime adapter retaining V92 bounded same-session transport recovery.

Semantic authority is the saved agent bootstrapped from AGENT_CONTRACT_V93.
This wrapper changes contract/version identity and evidence location only. The proven
V92 same-session transient recovery implementation remains unchanged.
"""
from __future__ import annotations

import os
from pathlib import Path

import v92_openai_agents_adapter as v92

CONTRACT_VERSION = os.environ.get("CONTRACT_VERSION", "RI-CONTRACT-V93").strip() or "RI-CONTRACT-V93"
V93_RECOVERY_DIR = Path("researcher_inventory/runtime/v93_session_recovery")

# V92's adapter already installed the same-session recovery function into the
# underlying command path. Rebind only current contract identity and evidence home.
v92.v90.prior.base.CONTRACT_VERSION = CONTRACT_VERSION
v92.RECOVERY_DIR = V93_RECOVERY_DIR
v92.recovery.RECOVERY_DIR = V93_RECOVERY_DIR
v92.v90.prior.base.recovery.RECOVERY_DIR = V93_RECOVERY_DIR

if __name__ == "__main__":
    raise SystemExit(v92.v90.prior.base.main())
