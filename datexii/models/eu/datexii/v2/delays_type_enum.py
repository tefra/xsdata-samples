from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class DelaysTypeEnum(Enum):
    """
    Course classifications of a delay.

    :cvar DELAYS: Delays on the road network as a result of any
        situation which causes hold-ups.
    :cvar DELAYS_OF_UNCERTAIN_DURATION: Delays on the road network whose
        predicted duration cannot be estimated.
    :cvar LONG_DELAYS: Delays on the road network of unusual severity.
    :cvar VERY_LONG_DELAYS: Delays on the road network of abnormally
        unusual severity.
    """

    DELAYS = "delays"
    DELAYS_OF_UNCERTAIN_DURATION = "delaysOfUncertainDuration"
    LONG_DELAYS = "longDelays"
    VERY_LONG_DELAYS = "veryLongDelays"
