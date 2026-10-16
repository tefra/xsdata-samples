from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class FlexibleLinkTypeEnumeration(StrEnum):
    HAIL_AND_RIDE = "hailAndRide"
    ON_DEMAND = "onDemand"
    FIXED = "fixed"
    OTHER = "other"
