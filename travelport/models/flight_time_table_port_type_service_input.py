from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.flight_time_table_req import FlightTimeTableReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class FlightTimeTablePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | FlightTimeTablePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        flight_time_table_req: None | FlightTimeTableReq = field(
            default=None,
            metadata={
                "name": "FlightTimeTableReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v52_0",
            },
        )
