from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class LinearReferencingDirectionEnum(Enum):
    """
    Directions of traffic flow relative to the direction in which the linear
    element is defined.

    :cvar BOTH: Indicates that both directions of traffic flow are
        affected by the situation or relate to the traffic data.
    :cvar OPPOSITE: Indicates that the direction of traffic flow
        affected by the situation or related to the traffic data is in
        the opposite sense to the direction in which the linear element
        is defined.
    :cvar ALIGNED: Indicates that the direction of traffic flow affected
        by the situation or related to the traffic data is in the same
        sense as the direction in which the linear element is defined.
    :cvar UNKNOWN: Indicates that the direction of traffic flow affected
        by the situation or related to the traffic data is unknown.
    """

    BOTH = "both"
    OPPOSITE = "opposite"
    ALIGNED = "aligned"
    UNKNOWN = "unknown"
