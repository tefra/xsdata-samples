from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_fare_directionality import TypeFareDirectionality
from travelport.models.type_fare_trip_type import TypeFareTripType

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class FareRestrictionDaysOfWeek:
    """
    Days of the week that the restriction applies too.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    direction: None | TypeFareDirectionality = field(
        default=None,
        metadata={
            "name": "Direction",
            "type": "Attribute",
        },
    )
    trip_type: None | TypeFareTripType = field(
        default=None,
        metadata={
            "name": "TripType",
            "type": "Attribute",
        },
    )
    monday: None | bool = field(
        default=None,
        metadata={
            "name": "Monday",
            "type": "Attribute",
        },
    )
    tuesday: None | bool = field(
        default=None,
        metadata={
            "name": "Tuesday",
            "type": "Attribute",
        },
    )
    wednesday: None | bool = field(
        default=None,
        metadata={
            "name": "Wednesday",
            "type": "Attribute",
        },
    )
    thursday: None | bool = field(
        default=None,
        metadata={
            "name": "Thursday",
            "type": "Attribute",
        },
    )
    friday: None | bool = field(
        default=None,
        metadata={
            "name": "Friday",
            "type": "Attribute",
        },
    )
    saturday: None | bool = field(
        default=None,
        metadata={
            "name": "Saturday",
            "type": "Attribute",
        },
    )
    sunday: None | bool = field(
        default=None,
        metadata={
            "name": "Sunday",
            "type": "Attribute",
        },
    )
