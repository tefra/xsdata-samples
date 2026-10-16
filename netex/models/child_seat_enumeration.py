from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ChildSeatEnumeration(StrEnum):
    BABY = "baby"
    SMALL_CHILD = "smallChild"
    OLDER_CHILD = "olderChild"
    NONE = "none"
    OTHER = "other"
