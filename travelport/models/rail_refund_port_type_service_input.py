from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.rail_refund_req import RailRefundReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class RailRefundPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | RailRefundPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        rail_refund_req: None | RailRefundReq = field(
            default=None,
            metadata={
                "name": "RailRefundReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/rail_v52_0",
            },
        )
