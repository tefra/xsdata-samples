from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.airport_1 import Airport1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class SpecificTimeTable:
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    flight_origin: None | SpecificTimeTable.FlightOrigin = field(
        default=None,
        metadata={
            "name": "FlightOrigin",
            "type": "Element",
        },
    )
    flight_destination: None | SpecificTimeTable.FlightDestination = field(
        default=None,
        metadata={
            "name": "FlightDestination",
            "type": "Element",
        },
    )
    start_date: str = field(
        metadata={
            "name": "StartDate",
            "type": "Attribute",
            "required": True,
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
    flight_number: str = field(
        metadata={
            "name": "FlightNumber",
            "type": "Attribute",
            "required": True,
            "max_length": 5,
        }
    )

    @dataclass(kw_only=True)
    class FlightOrigin:
        airport: Airport1 = field(
            metadata={
                "name": "Airport",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class FlightDestination:
        airport: Airport1 = field(
            metadata={
                "name": "Airport",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
                "required": True,
            }
        )
