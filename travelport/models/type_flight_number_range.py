from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class TypeFlightNumberRange:
    """
    Specify a range of flight numbers.
    """

    class Meta:
        name = "typeFlightNumberRange"

    flight_number_range_start: None | str = field(
        default=None,
        metadata={
            "name": "FlightNumberRangeStart",
            "type": "Attribute",
            "required": True,
            "max_length": 5,
        },
    )
    flight_number_range_end: None | str = field(
        default=None,
        metadata={
            "name": "FlightNumberRangeEnd",
            "type": "Attribute",
            "required": True,
            "max_length": 5,
        },
    )
