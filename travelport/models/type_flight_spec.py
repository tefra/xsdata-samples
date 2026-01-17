from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_flight_number_range import TypeFlightNumberRange
from travelport.models.type_specific_flight_number import (
    TypeSpecificFlightNumber,
)

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class TypeFlightSpec:
    """
    Specifies flight number as either specific flight number or a flight
    number range.
    """

    class Meta:
        name = "typeFlightSpec"

    flight_number_range: None | TypeFlightNumberRange = field(
        default=None,
        metadata={
            "name": "FlightNumberRange",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/util_v52_0",
        },
    )
    specific_flight_number: None | TypeSpecificFlightNumber = field(
        default=None,
        metadata={
            "name": "SpecificFlightNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/util_v52_0",
        },
    )
