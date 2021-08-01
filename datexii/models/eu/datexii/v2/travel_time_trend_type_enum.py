from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class TravelTimeTrendTypeEnum(Enum):
    """
    List of terms used to describe the trend in travel times.

    :cvar DECREASING: Travel times are decreasing.
    :cvar INCREASING: Travel times are increasing.
    :cvar STABLE: Travel times are stable.
    """
    DECREASING = "decreasing"
    INCREASING = "increasing"
    STABLE = "stable"
