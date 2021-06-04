from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CappingPeriodEnumeration(Enum):
    DAY = "day"
    WEEK = "week"
    MONTH = "month"
    NONE_VALUE = "none"
