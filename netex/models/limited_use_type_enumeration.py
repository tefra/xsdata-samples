from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LimitedUseTypeEnumeration(StrEnum):
    INTERCHANGE_ONLY = "interchangeOnly"
    NO_DIRECT_ROAD_ACCESS = "noDirectRoadAccess"
    LONG_WALK_TO_ACCESS = "longWalkToAccess"
    ISOLATED = "isolated"
    LIMITED_SERVICE = "limitedService"
    OTHER = "other"
