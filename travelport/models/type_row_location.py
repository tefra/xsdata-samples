from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeRowLocation(Enum):
    """Facility Position with respect to a Row.

    Possible values are Rear, Front
    """

    REAR = "Rear"
    FRONT = "Front"
