from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SameZoneEnumeration(Enum):
    ANY = "any"
    SAME = "same"
    SAME_AS_ORIGIN = "sameAsOrigin"
    SAME_AS_DESTINATION = "sameAsDestination"
    SAME_AS_ORIGIN_OR_DESTINATION = "sameAsOriginOrDestination"
    WITHIN = "within"
    CONTAINING = "containing"
    EQUIVALENT = "equivalent"
    DIFFERENT = "different"
