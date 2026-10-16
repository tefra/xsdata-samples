from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TimeOfDayEnumeration(StrEnum):
    DAWN = "dawn"
    DUSK = "dusk"
    NOON = "noon"
    MIDNIGHT = "midnight"
    CURFEW_START = "curfewStart"
    CURFEW_END = "curfewEnd"
