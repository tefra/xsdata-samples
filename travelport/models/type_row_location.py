from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeRowLocation(StrEnum):
    """
    Facility Position with respect to a Row.

    Possible values are Rear, Front.
    """

    REAR = "Rear"
    FRONT = "Front"
