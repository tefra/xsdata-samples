from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class MinimumStayTypeEnumeration(Enum):
    NONE_VALUE = "none"
    SPECIFIED_NIGHTS_AWAY = "specifiedNightsAway"
    COUNT_NIGHTS_AWAY = "countNightsAway"
    BOTH = "both"
    EITHER = "either"
