from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SanitaryFacilityEnumeration(Enum):
    NONE = "none"
    TOILET = "toilet"
    WHEEL_CHAIR_ACCESS_TOILET = "wheelChairAccessToilet"
    SHOWER = "shower"
    WASHING_AND_CHANGE_FACILITIES = "washingAndChangeFacilities"
    BABY_CHANGE = "babyChange"
    WHEELCHAIR_BABY_CHANGE = "wheelchairBabyChange"
    SHOE_SHINER = "shoeShiner"
    OTHER = "other"
