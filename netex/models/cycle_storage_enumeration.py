from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CycleStorageEnumeration(Enum):
    RACKS = "racks"
    BARS = "bars"
    RAILINGS = "railings"
    CYCLE_SCHEME = "cycleScheme"
    OTHER = "other"
