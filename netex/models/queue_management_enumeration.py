from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class QueueManagementEnumeration(Enum):
    NONE = "none"
    MAZE = "maze"
    SEPARATE_LINES = "separateLines"
    TICKETED = "ticketed"
    OTHER = "other"
