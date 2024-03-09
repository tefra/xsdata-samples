from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_exchange_req import AirExchangeReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class AirExchangeProcessPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | AirExchangeProcessPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        air_exchange_req: None | AirExchangeReq = field(
            default=None,
            metadata={
                "name": "AirExchangeReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v52_0",
            },
        )
