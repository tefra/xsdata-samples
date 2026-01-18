from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class TpegLoc01SimplePointLocationSubtypeEnum(Enum):
    """
    Types of simple point.

    :cvar INTERSECTION: An point on the road network at which one or
        more roads intersect.
    :cvar NON_LINKED_POINT: A point on the road network which is not at
        a junction or intersection.
    """

    INTERSECTION = "intersection"
    NON_LINKED_POINT = "nonLinkedPoint"
