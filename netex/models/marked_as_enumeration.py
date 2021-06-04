from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class MarkedAsEnumeration(Enum):
    UNUSED = "unused"
    ACTIVATED = "activated"
    MARKED = "marked"
    USED = "used"
    EXPIRED = "expired"
