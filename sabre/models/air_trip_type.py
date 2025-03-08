from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


class AirTripType(Enum):
    """Identifies the trip type - one way, return, circle trip, open jaw."""

    ONE_WAY = "OneWay"
    RETURN = "Return"
    CIRCLE = "Circle"
    OPEN_JAW = "OpenJaw"
    OTHER = "Other"
