from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class EntranceTurningSpacePositionEnumeration(Enum):
    NONE = "none"
    OUTSIDE = "outside"
    INSIDE = "inside"
    INSIDE_AND_OUTSIDE = "insideAndOutside"
