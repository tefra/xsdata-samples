from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.mct_count_req import MctCountReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class MctCountPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | MctCountPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        mct_count_req: None | MctCountReq = field(
            default=None,
            metadata={
                "name": "MctCountReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/util_v52_0",
            },
        )
