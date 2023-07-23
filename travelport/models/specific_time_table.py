from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.airport_1 import Airport1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class SpecificTimeTable:
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    flight_origin: None | SpecificTimeTable.FlightOrigin = field(
        default=None,
        metadata={
            "name": "FlightOrigin",
            "type": "Element",
        }
    )
    flight_destination: None | SpecificTimeTable.FlightDestination = field(
        default=None,
        metadata={
            "name": "FlightDestination",
            "type": "Element",
        }
    )
    start_date: None | str = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Attribute",
            "required": True,
        }
    )
    carrier: None | str = field(
        default=None,
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
            "required": True,
            "max_length": 5,
        }
    )

    @dataclass
    class FlightOrigin:
        airport: None | Airport1 = field(
            default=None,
            metadata={
                "name": "Airport",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
                "required": True,
            }
        )

    @dataclass
    class FlightDestination:
        airport: None | Airport1 = field(
            default=None,
            metadata={
                "name": "Airport",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
                "required": True,
            }
        )
