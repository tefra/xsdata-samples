from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_exchange_multi_quote_req import AirExchangeMultiQuoteReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class AirExchangeMultiQuotePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | AirExchangeMultiQuotePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_exchange_multi_quote_req: None | AirExchangeMultiQuoteReq = field(
            default=None,
            metadata={
                "name": "AirExchangeMultiQuoteReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v52_0",
            }
        )
