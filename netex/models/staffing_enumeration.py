from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class StaffingEnumeration(StrEnum):
    FULL_TIME = "fullTime"
    PART_TIME = "partTime"
    UNMANNED = "unmanned"
