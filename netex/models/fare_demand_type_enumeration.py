from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class FareDemandTypeEnumeration(StrEnum):
    PEAK = "peak"
    MIDDLE = "middle"
    OFF_PEAK = "offPeak"
    SUPER_OFF_PEAK = "superOffPeak"
    NIGHT = "night"
    SPECIAL_EVENT = "specialEvent"
