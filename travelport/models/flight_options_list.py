from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.flight_option import FlightOption

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class FlightOptionsList:
    """
    List of Flight Options for the itinerary.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    flight_option: list[FlightOption] = field(
        default_factory=list,
        metadata={
            "name": "FlightOption",
            "type": "Element",
            "max_occurs": 999,
        },
    )
