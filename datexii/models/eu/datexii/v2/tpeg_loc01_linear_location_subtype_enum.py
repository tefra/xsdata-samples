from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class TpegLoc01LinearLocationSubtypeEnum(Enum):
    """
    Types of linear location.

    :cvar SEGMENT: A segment (or link) of the road network corresponding
        to the way in which the road operator has segmented the network.
    """
    SEGMENT = "segment"
