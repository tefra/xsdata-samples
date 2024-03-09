from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class TypeSpecificFlightNumber:
    """
    Specify exact flight number.
    """

    class Meta:
        name = "typeSpecificFlightNumber"

    flight_number: None | str = field(
        default=None,
        metadata={
            "name": "FlightNumber",
            "type": "Attribute",
            "required": True,
            "max_length": 5,
        },
    )
