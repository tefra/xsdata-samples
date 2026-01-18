from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class StaffingEnumeration(Enum):
    FULL_TIME = "fullTime"
    PART_TIME = "partTime"
    UNMANNED = "unmanned"
