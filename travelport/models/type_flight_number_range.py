from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass(kw_only=True)
class TypeFlightNumberRange:
    """
    Specify a range of flight numbers.
    """

    class Meta:
        name = "typeFlightNumberRange"

    flight_number_range_start: str = field(
        metadata={
            "name": "FlightNumberRangeStart",
            "type": "Attribute",
            "required": True,
            "max_length": 5,
        }
    )
    flight_number_range_end: str = field(
        metadata={
            "name": "FlightNumberRangeEnd",
            "type": "Attribute",
            "required": True,
            "max_length": 5,
        }
    )
