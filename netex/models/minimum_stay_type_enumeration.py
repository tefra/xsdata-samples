from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class MinimumStayTypeEnumeration(StrEnum):
    NONE = "none"
    SPECIFIED_NIGHTS_AWAY = "specifiedNightsAway"
    COUNT_NIGHTS_AWAY = "countNightsAway"
    BOTH = "both"
    EITHER = "either"
