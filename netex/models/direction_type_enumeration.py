from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DirectionTypeEnumeration(StrEnum):
    INBOUND = "inbound"
    OUTBOUND = "outbound"
    CLOCKWISE = "clockwise"
    ANTICLOCKWISE = "anticlockwise"
