from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class VisualObstacleEnumeration(StrEnum):
    NONE = "none"
    CAR_PARKING = "carParking"
    VEGETATION = "vegetation"
    BUILDING = "building"
    STREET_FURNITURE = "streetFurniture"
    OTHER = "other"
