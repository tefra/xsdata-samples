from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_exchange_quote_req import AirExchangeQuoteReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class AirExchangeQuotePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | AirExchangeQuotePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        air_exchange_quote_req: None | AirExchangeQuoteReq = field(
            default=None,
            metadata={
                "name": "AirExchangeQuoteReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v52_0",
            },
        )
