from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.gds_enter_queue_req import GdsEnterQueueReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class GdsEnterQueueServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | GdsEnterQueueServicePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        gds_enter_queue_req: None | GdsEnterQueueReq = field(
            default=None,
            metadata={
                "name": "GdsEnterQueueReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/gdsQueue_v52_0",
            }
        )
