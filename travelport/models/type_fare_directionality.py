from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeFareDirectionality(Enum):
    """
    A fare's directionality (e.g. one-way, return )
    """

    OUTBOUND = "Outbound"
    RETURN = "Return"
    ALL = "All"
