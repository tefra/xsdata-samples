from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.emdissuance_req import EmdissuanceReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class EmdissuancePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | EmdissuancePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        emdissuance_req: None | EmdissuanceReq = field(
            default=None,
            metadata={
                "name": "EMDIssuanceReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v52_0",
            }
        )
