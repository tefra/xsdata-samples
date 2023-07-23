from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.flight_information_req import FlightInformationReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class FlightInfoPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | FlightInfoPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        flight_information_req: None | FlightInformationReq = field(
            default=None,
            metadata={
                "name": "FlightInformationReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v52_0",
            }
        )
