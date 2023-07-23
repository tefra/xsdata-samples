from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_pre_pay_req import AirPrePayReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class AirPrePayPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | AirPrePayPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_pre_pay_req: None | AirPrePayReq = field(
            default=None,
            metadata={
                "name": "AirPrePayReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v52_0",
            }
        )
