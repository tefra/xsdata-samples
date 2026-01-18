from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_hotel_location import TypeHotelLocation

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass(kw_only=True)
class HotelLocation:
    """
    Date and Location information for the Hotel.

    Location can be optional if a Reference Point is provided.

    Parameters
    ----------
    location
        IATA city/airport code
    location_type
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    location: None | str = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        },
    )
    location_type: TypeHotelLocation = field(
        default=TypeHotelLocation.AIRPORT,
        metadata={
            "name": "LocationType",
            "type": "Attribute",
        },
    )
