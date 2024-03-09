from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class TravelInfo5:
    """
    Traveler information details like Travel Purpose and Trip Name.

    Parameters
    ----------
    trip_name
        Trip Name
    travel_purpose
        Purpose of the trip
    """

    class Meta:
        name = "TravelInfo"
        namespace = "http://www.travelport.com/schema/common_v34_0"

    trip_name: None | str = field(
        default=None,
        metadata={
            "name": "TripName",
            "type": "Attribute",
            "max_length": 50,
        },
    )
    travel_purpose: None | str = field(
        default=None,
        metadata={
            "name": "TravelPurpose",
            "type": "Attribute",
            "max_length": 50,
        },
    )
