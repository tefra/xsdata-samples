from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.flight_details_req import FlightDetailsReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class FlightDetailsPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | FlightDetailsPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        flight_details_req: None | FlightDetailsReq = field(
            default=None,
            metadata={
                "name": "FlightDetailsReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v52_0",
            },
        )
