from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class TpegLoc03JunctionPointDescriptorSubtypeEnum(Enum):
    """
    Descriptors for describing a point at a road junction.

    :cvar JUNCTION_NAME: Name of a road network junction where two or
        more roads join.
    """

    JUNCTION_NAME = "junctionName"
