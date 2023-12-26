from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class AlertCDirectionEnum(Enum):
    """The direction of traffic flow concerned by a situation or traffic data.

    In ALERT-C the positive (resp. negative) direction corresponds to
    the positive offset direction within the RDS location table.

    :cvar BOTH: Indicates that both directions of traffic flow are
        affected by the situation or relate to the traffic data.
    :cvar NEGATIVE: The direction of traffic flow concerned by a
        situation or traffic data. In ALERT-C the negative direction
        corresponds to the negative offset direction within the RDS
        location table.
    :cvar POSITIVE: The direction of traffic flow concerned by a
        situation or traffic data. In ALERT-C the positive direction
        corresponds to the positive offset direction within the RDS
        location table.
    :cvar UNKNOWN: Unknown direction.
    """

    BOTH = "both"
    NEGATIVE = "negative"
    POSITIVE = "positive"
    UNKNOWN = "unknown"
