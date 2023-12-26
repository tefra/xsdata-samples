from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class RoadworksScaleEnum(Enum):
    """
    Coarse classifications of the scale of roadworks in terms of the traffic
    disruption they are likely to cause.

    :cvar MAJOR: The roadworks are likely to cause major traffic
        disruption.
    :cvar MEDIUM: The roadworks are likely to cause a medium level of
        traffic disruption.
    :cvar MINOR: The roadworks are likely to cause minor traffic
        disruption.
    """

    MAJOR = "major"
    MEDIUM = "medium"
    MINOR = "minor"
