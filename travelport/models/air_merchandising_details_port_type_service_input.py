from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_merchandising_details_req import (
    AirMerchandisingDetailsReq,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class AirMerchandisingDetailsPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | AirMerchandisingDetailsPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        air_merchandising_details_req: None | AirMerchandisingDetailsReq = (
            field(
                default=None,
                metadata={
                    "name": "AirMerchandisingDetailsReq",
                    "type": "Element",
                    "namespace": "http://www.travelport.com/schema/air_v52_0",
                },
            )
        )
