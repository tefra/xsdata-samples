from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeFareRestrictionType(StrEnum):
    """
    The type of fare restriction.
    """

    DAY_OF_WEEK = "DayOfWeek"
    FLIGHT_TIME_OF_DAY = "FlightTimeOfDay"
    BOTH = "Both"
