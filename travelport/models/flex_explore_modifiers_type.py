from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class FlexExploreModifiersType(StrEnum):
    ANY_WHERE = "AnyWhere"
    AREA = "Area"
    ZONE = "Zone"
    COUNTRY = "Country"
    STATE = "State"
    DISTANCE_IN_MILES = "DistanceInMiles"
    DISTANCE_IN_KILOMETERS = "DistanceInKilometers"
    DESTINATION = "Destination"
    GROUP = "Group"
