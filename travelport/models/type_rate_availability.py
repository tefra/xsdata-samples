from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


class TypeRateAvailability(Enum):
    AVAILABLE = "Available"
    CALL = "Call"
    CLOSED = "Closed"
