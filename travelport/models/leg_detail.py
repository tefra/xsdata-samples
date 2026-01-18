from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class LegDetail:
    """
    Information about the journey Leg, Shared by Leg and LegPrice Elements.

    Parameters
    ----------
    key
    origin_airport
        Returns the origin airport code for the Leg Detail.
    destination_airport
        Returns the destination airport code for the Leg Detail.
    carrier
        Carrier for the Search Leg Detail.
    travel_date
        The Departure date and time for this Leg Detail.
    flight_number
        Flight Number for the Search Leg Detail.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    key: str = field(
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    origin_airport: str = field(
        metadata={
            "name": "OriginAirport",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    destination_airport: str = field(
        metadata={
            "name": "DestinationAirport",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    carrier: str = field(
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "required": True,
            "length": 2,
        }
    )
    travel_date: None | str = field(
        default=None,
        metadata={
            "name": "TravelDate",
            "type": "Attribute",
        },
    )
    flight_number: None | str = field(
        default=None,
        metadata={
            "name": "FlightNumber",
            "type": "Attribute",
            "max_length": 5,
        },
    )
