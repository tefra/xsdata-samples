from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SameRouteEnumeration(Enum):
    ANY = "any"
    SAME = "same"
    OPPOSITE_DIRECTION = "oppositeDirection"
    DIFFERENT = "different"
