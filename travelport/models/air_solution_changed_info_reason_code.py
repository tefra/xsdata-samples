from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class AirSolutionChangedInfoReasonCode(Enum):
    PRICE = "Price"
    SCHEDULE = "Schedule"
    BOTH = "Both"
