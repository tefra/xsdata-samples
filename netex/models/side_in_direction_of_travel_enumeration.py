from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SideInDirectionOfTravelEnumeration(StrEnum):
    LEFT = "left"
    RIGHT = "right"
    BOTH = "both"
    UNKNOWN = "unknown"
