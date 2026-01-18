from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.rail_refund_quote_req import RailRefundQuoteReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class RailRefundQuotePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: RailRefundQuotePortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        rail_refund_quote_req: RailRefundQuoteReq = field(
            metadata={
                "name": "RailRefundQuoteReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/rail_v52_0",
            }
        )
