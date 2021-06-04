from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PreassignedFareProductEnumeration(Enum):
    SINGLE_TRIP = "singleTrip"
    SHORT_TRIP = "shortTrip"
    TIME_LIMITED_SINGLE_TRIP = "timeLimitedSingleTrip"
    DAY_RETURN_TRIP = "dayReturnTrip"
    PERIOD_RETURN_TRIP = "periodReturnTrip"
    MULTISTEP_TRIP = "multistepTrip"
    DAY_PASS = "dayPass"
    PERIOD_PASS = "periodPass"
    SUPPLEMENT = "supplement"
    OTHER = "other"
