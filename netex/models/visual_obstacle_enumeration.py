from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class VisualObstacleEnumeration(Enum):
    NONE = "none"
    CAR_PARKING = "carParking"
    VEGETATION = "vegetation"
    BUILDING = "building"
    STREET_FURNITURE = "streetFurniture"
    OTHER = "other"
