from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeFareRestrictionType(Enum):
    """
    The type of fare restriction.
    """

    DAY_OF_WEEK = "DayOfWeek"
    FLIGHT_TIME_OF_DAY = "FlightTimeOfDay"
    BOTH = "Both"
