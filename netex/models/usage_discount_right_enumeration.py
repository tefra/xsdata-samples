from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class UsageDiscountRightEnumeration(Enum):
    MILEAGE_POINTS = "mileagePoints"
    USAGE_REBATE = "usageRebate"
    OTHER = "other"
