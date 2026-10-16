from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TimingPointStatusEnumeration(StrEnum):
    TIMING_POINT = "timingPoint"
    SECONDARY_TIMING_POINT = "secondaryTimingPoint"
    NOT_TIMING_POINT = "notTimingPoint"
