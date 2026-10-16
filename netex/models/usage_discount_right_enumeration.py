from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class UsageDiscountRightEnumeration(StrEnum):
    MILEAGE_POINTS = "mileagePoints"
    USAGE_REBATE = "usageRebate"
    OTHER = "other"
