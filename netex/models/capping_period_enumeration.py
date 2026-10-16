from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CappingPeriodEnumeration(StrEnum):
    DAY = "day"
    WEEK = "week"
    MONTH = "month"
    NONE = "none"
