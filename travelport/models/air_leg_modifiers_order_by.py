from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class AirLegModifiersOrderBy(StrEnum):
    JOURNEY_TIME = "JourneyTime"
    DEPARTURE_TIME = "DepartureTime"
    ARRIVAL_TIME = "ArrivalTime"
