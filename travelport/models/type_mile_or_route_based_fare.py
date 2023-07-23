from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeMileOrRouteBasedFare(Enum):
    """
    Whether the fare is Mile or Route based.
    """
    MILE = "Mile"
    ROUTE = "Route"
    BOTH = "Both"
