from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.reference_data_update_req import ReferenceDataUpdateReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class ReferenceDataUpdatePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | ReferenceDataUpdatePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        reference_data_update_req: None | ReferenceDataUpdateReq = field(
            default=None,
            metadata={
                "name": "ReferenceDataUpdateReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/util_v52_0",
            },
        )
