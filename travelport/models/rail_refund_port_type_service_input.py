from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.rail_refund_req import RailRefundReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class RailRefundPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: RailRefundPortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        rail_refund_req: RailRefundReq = field(
            metadata={
                "name": "RailRefundReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/rail_v52_0",
            }
        )
