from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_merchandising_details_req import (
    AirMerchandisingDetailsReq,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class AirMerchandisingDetailsPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: AirMerchandisingDetailsPortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        air_merchandising_details_req: AirMerchandisingDetailsReq = field(
            metadata={
                "name": "AirMerchandisingDetailsReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v52_0",
            }
        )
