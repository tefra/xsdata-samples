from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CrossingTypeEnumeration(Enum):
    LEVEL_CROSSING = "levelCrossing"
    BARROW_CROSSING = "barrowCrossing"
    ROAD_CROSSING = "roadCrossing"
    ROAD_CROSSING_WITH_ISLAND = "roadCrossingWithIsland"
    OTHER = "other"
