from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.reference_data_search_req import ReferenceDataSearchReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class ReferenceDataLookupPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | ReferenceDataLookupPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        reference_data_search_req: None | ReferenceDataSearchReq = field(
            default=None,
            metadata={
                "name": "ReferenceDataSearchReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/util_v52_0",
            },
        )
