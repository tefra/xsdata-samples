from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.emdissuance_req import EmdissuanceReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class EmdissuancePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: EmdissuancePortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        emdissuance_req: EmdissuanceReq = field(
            metadata={
                "name": "EMDIssuanceReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v52_0",
            }
        )
