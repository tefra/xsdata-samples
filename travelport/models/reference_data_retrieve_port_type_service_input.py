from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.reference_data_retrieve_req import (
    ReferenceDataRetrieveReq,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class ReferenceDataRetrievePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | ReferenceDataRetrievePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        reference_data_retrieve_req: None | ReferenceDataRetrieveReq = field(
            default=None,
            metadata={
                "name": "ReferenceDataRetrieveReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/util_v52_0",
            },
        )
