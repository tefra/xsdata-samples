from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class TrafficStatusEnum(Enum):
    """
    List of terms used to describe traffic conditions.

    :cvar IMPOSSIBLE: Traffic in the specified direction is completely
        congested, effectively at a standstill, making driving
        impossible.
    :cvar CONGESTED: Traffic in the specified direction is congested
        making driving very slow and difficult.
    :cvar HEAVY: Traffic in the specified direction is heavier than
        usual making driving conditions more difficult than normal.
    :cvar FREE_FLOW: Traffic in the specified direction is free flowing.
    :cvar UNKNOWN: Traffic conditions are unknown.
    """
    IMPOSSIBLE = "impossible"
    CONGESTED = "congested"
    HEAVY = "heavy"
    FREE_FLOW = "freeFlow"
    UNKNOWN = "unknown"
