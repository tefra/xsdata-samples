from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class FlexibleRouteTypeEnumeration(Enum):
    FLEXIBLE_AREAS_ONLY = "flexibleAreasOnly"
    HAIL_AND_RIDE_SECTIONS = "hailAndRideSections"
    MIXED = "mixed"
    FIXED = "fixed"
    OTHER = "other"
