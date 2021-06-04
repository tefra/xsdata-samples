from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class QueueManagementEnumeration(Enum):
    NONE_VALUE = "none"
    MAZE = "maze"
    SEPARATE_LINES = "separateLines"
    TICKETED = "ticketed"
    OTHER = "other"
