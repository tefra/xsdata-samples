from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SafetyEdgeEnumeration(Enum):
    NONE = "none"
    ONE_SIDE = "oneSide"
    BOTH_SIDES = "bothSides"
