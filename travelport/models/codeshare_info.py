from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class CodeshareInfo:
    """
    Describes the codeshare disclosure (simple text string) or the specific
    operating flight information (as attributes).

    Parameters
    ----------
    value
    operating_carrier
        The actual carrier that is operating the flight.
    operating_flight_number
        The actual flight number of the carrier that is operating the
        flight.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    operating_carrier: None | str = field(
        default=None,
        metadata={
            "name": "OperatingCarrier",
            "type": "Attribute",
            "length": 2,
        },
    )
    operating_flight_number: None | str = field(
        default=None,
        metadata={
            "name": "OperatingFlightNumber",
            "type": "Attribute",
            "max_length": 5,
        },
    )
