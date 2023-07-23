from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_refund_quote_req import AirRefundQuoteReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class AirRefundQuotePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | AirRefundQuotePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_refund_quote_req: None | AirRefundQuoteReq = field(
            default=None,
            metadata={
                "name": "AirRefundQuoteReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v52_0",
            }
        )
