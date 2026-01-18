from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.flight_details import FlightDetails

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class FlightDetailsList:
    """
    The shared object list of FlightDetails.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    flight_details: list[FlightDetails] = field(
        default_factory=list,
        metadata={
            "name": "FlightDetails",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
