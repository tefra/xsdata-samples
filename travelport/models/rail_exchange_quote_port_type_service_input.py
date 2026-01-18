from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.rail_exchange_quote_req import RailExchangeQuoteReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class RailExchangeQuotePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: RailExchangeQuotePortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        rail_exchange_quote_req: RailExchangeQuoteReq = field(
            metadata={
                "name": "RailExchangeQuoteReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/rail_v52_0",
            }
        )
