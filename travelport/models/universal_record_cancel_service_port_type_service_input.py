from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.universal_record_cancel_req import UniversalRecordCancelReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class UniversalRecordCancelServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | UniversalRecordCancelServicePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        universal_record_cancel_req: None | UniversalRecordCancelReq = field(
            default=None,
            metadata={
                "name": "UniversalRecordCancelReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/universal_v52_0",
            }
        )
