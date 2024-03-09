from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.mco_search_req import McoSearchReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class McoSearchPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | McoSearchPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        mco_search_req: None | McoSearchReq = field(
            default=None,
            metadata={
                "name": "McoSearchReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/util_v52_0",
            },
        )
