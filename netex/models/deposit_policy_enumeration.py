from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DepositPolicyEnumeration(StrEnum):
    NONE = "none"
    DEPOSIT_TAKEN = "depositTaken"
    DEPOSIT_BLOCKED = "depositBlocked"
    OTHER = "other"
