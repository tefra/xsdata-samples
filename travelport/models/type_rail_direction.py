from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


class TypeRailDirection(Enum):
    """
    The direction of travel.
    """

    INBOUND = "Inbound"
    OUTBOUND = "Outbound"
    BOTH = "Both"
