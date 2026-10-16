from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


class TypeRailDirection(StrEnum):
    """
    The direction of travel.
    """

    INBOUND = "Inbound"
    OUTBOUND = "Outbound"
    BOTH = "Both"
