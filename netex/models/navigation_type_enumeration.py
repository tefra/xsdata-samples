from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class NavigationTypeEnumeration(Enum):
    HALL_TO_QUAY = "hallToQuay"
    HALL_TO_STREET = "hallToStreet"
    QUAY_TO_HALL = "quayToHall"
    QUAY_TO_QUAY = "quayToQuay"
    QUAY_TO_STREET = "quayToStreet"
    STREET_TO_HALL = "streetToHall"
    STREET_TO_QUAY = "streetToQuay"
    STREET_TO_SPACE = "streetToSpace"
    SPACE_TO_STREET = "spaceToStreet"
    SPACE_TO_HALL = "spaceToHall"
    HALL_TO_SPACE = "hallToSpace"
    SPACE_TO_SPACE = "spaceToSpace"
    OTHER = "other"
