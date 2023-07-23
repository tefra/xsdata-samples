from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.mct_lookup_req import MctLookupReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class MctLookupPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | MctLookupPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        mct_lookup_req: None | MctLookupReq = field(
            default=None,
            metadata={
                "name": "MctLookupReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/util_v52_0",
            }
        )
