from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class FlexibleLineTypeEnumeration(Enum):
    CORRIDOR_SERVICE = "corridorService"
    MAIN_ROUTE_WITH_FLEXIBLE_ENDS = "mainRouteWithFlexibleEnds"
    FLEXIBLE_AREAS_ONLY = "flexibleAreasOnly"
    HAIL_AND_RIDE_SECTIONS = "hailAndRideSections"
    FIXED_STOP_AREA_WIDE = "fixedStopAreaWide"
    FREE_AREA_AREA_WIDE = "freeAreaAreaWide"
    MIXED_FLEXIBLE = "mixedFlexible"
    MIXED_FLEXIBLE_AND_FIXED = "mixedFlexibleAndFixed"
    FIXED = "fixed"
    OTHER = "other"
