from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.gds_next_on_queue_req import GdsNextOnQueueReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class GdsNextOnQueueServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | GdsNextOnQueueServicePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        gds_next_on_queue_req: None | GdsNextOnQueueReq = field(
            default=None,
            metadata={
                "name": "GdsNextOnQueueReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/gdsQueue_v52_0",
            },
        )
