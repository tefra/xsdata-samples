from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class FlexibleRouteTypeEnumeration(StrEnum):
    FLEXIBLE_AREAS_ONLY = "flexibleAreasOnly"
    HAIL_AND_RIDE_SECTIONS = "hailAndRideSections"
    MIXED = "mixed"
    FIXED = "fixed"
    OTHER = "other"
