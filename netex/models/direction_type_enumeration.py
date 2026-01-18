from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DirectionTypeEnumeration(Enum):
    INBOUND = "inbound"
    OUTBOUND = "outbound"
    CLOCKWISE = "clockwise"
    ANTICLOCKWISE = "anticlockwise"
