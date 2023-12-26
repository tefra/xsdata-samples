from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_reprice_req import AirRepriceReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class AirRepriceSearchPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | AirRepriceSearchPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        air_reprice_req: None | AirRepriceReq = field(
            default=None,
            metadata={
                "name": "AirRepriceReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v52_0",
            },
        )
