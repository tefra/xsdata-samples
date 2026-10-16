from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class QueueManagementEnumeration(StrEnum):
    NONE = "none"
    MAZE = "maze"
    SEPARATE_LINES = "separateLines"
    TICKETED = "ticketed"
    OTHER = "other"
