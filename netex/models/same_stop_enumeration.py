from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SameStopEnumeration(Enum):
    ANY = "any"
    SAME_AS_ORIGIN = "sameAsOrigin"
    SAME_AS_DESTINATION = "sameAsDestination"
    SAME_AS_ORIGIN_OR_DESTINATION = "sameAsOriginOrDestination"
    ANY_STOP_ON_ROUTE = "anyStopOnRoute"
    ANY_STOP_IN_ZONE = "anyStopInZone"
    DIFFERENT = "different"
