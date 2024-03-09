from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_refund_req import AirRefundReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class AirRefundTicketPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | AirRefundTicketPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        air_refund_req: None | AirRefundReq = field(
            default=None,
            metadata={
                "name": "AirRefundReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v52_0",
            },
        )
