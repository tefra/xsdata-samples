from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class TypeAnchorFlightData:
    """
    To support Anchor flight search contain the anchor flight details.

    Supported providers 1P.

    Parameters
    ----------
    airline_code
        Indicates Anchor flight carrier code
    flight_number
        Indicates Anchor flight number
    connection_indicator
        Indicates that the Anchor flight has any connecting flight or not
    """

    class Meta:
        name = "typeAnchorFlightData"

    airline_code: str = field(
        metadata={
            "name": "AirlineCode",
            "type": "Attribute",
            "required": True,
            "length": 2,
        }
    )
    flight_number: str = field(
        metadata={
            "name": "FlightNumber",
            "type": "Attribute",
            "required": True,
            "max_length": 5,
        }
    )
    connection_indicator: None | bool = field(
        default=None,
        metadata={
            "name": "ConnectionIndicator",
            "type": "Attribute",
        },
    )
