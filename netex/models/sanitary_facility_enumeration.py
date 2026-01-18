from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SanitaryFacilityEnumeration(Enum):
    NONE = "none"
    TOILET = "toilet"
    WHEELCHAIR_ACCESS_TOILET = "wheelchairAccessToilet"
    SHOWER = "shower"
    WASHING_AND_CHANGE_FACILITIES = "washingAndChangeFacilities"
    BABY_CHANGE = "babyChange"
    WHEELCHAIR_BABY_CHANGE = "wheelchairBabyChange"
    SHOE_SHINER = "shoeShiner"
    OTHER = "other"
