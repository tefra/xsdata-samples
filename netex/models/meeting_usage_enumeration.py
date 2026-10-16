from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class MeetingUsageEnumeration(StrEnum):
    PICK_UP = "pickUp"
    SET_DOWN = "setDown"
    ALL = "all"
