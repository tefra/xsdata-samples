from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DepositPolicyEnumeration(Enum):
    NONE = "none"
    DEPOSIT_TAKEN = "depositTaken"
    DEPOSIT_BLOCKED = "depositBlocked"
    OTHER = "other"
