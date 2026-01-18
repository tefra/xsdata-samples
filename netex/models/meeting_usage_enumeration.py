from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class MeetingUsageEnumeration(Enum):
    PICK_UP = "pickUp"
    SET_DOWN = "setDown"
    ALL = "all"
