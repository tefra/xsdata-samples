from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.mco_void_req import McoVoidReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class McoVoidPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | McoVoidPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        mco_void_req: None | McoVoidReq = field(
            default=None,
            metadata={
                "name": "McoVoidReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/util_v52_0",
            }
        )
