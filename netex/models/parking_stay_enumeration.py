from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ParkingStayEnumeration(Enum):
    SHORT_STAY = "shortStay"
    MID_TERM = "midTerm"
    LONG_TERM = "longTerm"
    DROPOFF = "dropoff"
    UNLIMITED = "unlimited"
    OTHER = "other"
    ALL = "all"
