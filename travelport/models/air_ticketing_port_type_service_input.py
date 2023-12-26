from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_ticketing_req import AirTicketingReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class AirTicketingPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | AirTicketingPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        air_ticketing_req: None | AirTicketingReq = field(
            default=None,
            metadata={
                "name": "AirTicketingReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v52_0",
            },
        )
