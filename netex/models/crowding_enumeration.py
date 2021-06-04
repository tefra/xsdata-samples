from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CrowdingEnumeration(Enum):
    VERY_QUIET = "veryQuiet"
    QUIET = "quiet"
    NORMAL = "normal"
    BUSY = "busy"
    VERY_BUSY = "veryBusy"
