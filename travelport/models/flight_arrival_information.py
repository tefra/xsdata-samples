from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass(kw_only=True)
class FlightArrivalInformation:
    """
    The flight arrival information (airline code and flight number) for the
    airport/city at which the rental car will be picked up.

    Parameters
    ----------
    carrier
        The carrier that is marketing this segment
    flight_number
        The flight number under which the marketing carrier is marketing
        this flight
    key
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    carrier: str = field(
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "required": True,
            "length": 2,
        }
    )
    flight_number: None | str = field(
        default=None,
        metadata={
            "name": "FlightNumber",
            "type": "Attribute",
            "max_length": 30,
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
