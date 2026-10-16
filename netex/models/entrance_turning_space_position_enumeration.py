from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class EntranceTurningSpacePositionEnumeration(StrEnum):
    NONE = "none"
    OUTSIDE = "outside"
    INSIDE = "inside"
    INSIDE_AND_OUTSIDE = "insideAndOutside"
