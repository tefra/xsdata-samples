from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_refund_quote_req import AirRefundQuoteReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class AirRefundQuotePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: AirRefundQuotePortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        air_refund_quote_req: AirRefundQuoteReq = field(
            metadata={
                "name": "AirRefundQuoteReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v52_0",
            }
        )
