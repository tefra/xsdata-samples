from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class TravelTimeTypeEnum(Enum):
    """
    List of ways in which travel times are derived.

    :cvar BEST: Travel time is derived from the best out of a monitored
        sample.
    :cvar ESTIMATED: Travel time is an automated estimate.
    :cvar INSTANTANEOUS: Travel time is derived from instantaneous
        measurements.
    :cvar RECONSTITUTED: Travel time is reconstituted from other
        measurements.
    """
    BEST = "best"
    ESTIMATED = "estimated"
    INSTANTANEOUS = "instantaneous"
    RECONSTITUTED = "reconstituted"
