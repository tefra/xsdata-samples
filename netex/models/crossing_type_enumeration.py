from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CrossingTypeEnumeration(StrEnum):
    LEVEL_CROSSING = "levelCrossing"
    BARROW_CROSSING = "barrowCrossing"
    ROAD_CROSSING = "roadCrossing"
    ROAD_CROSSING_WITH_ISLAND = "roadCrossingWithIsland"
    OTHER = "other"
