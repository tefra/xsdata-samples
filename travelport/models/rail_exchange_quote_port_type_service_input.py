from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.rail_exchange_quote_req import RailExchangeQuoteReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class RailExchangeQuotePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | RailExchangeQuotePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        rail_exchange_quote_req: None | RailExchangeQuoteReq = field(
            default=None,
            metadata={
                "name": "RailExchangeQuoteReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/rail_v52_0",
            },
        )
