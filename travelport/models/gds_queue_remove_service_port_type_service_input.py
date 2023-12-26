from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.gds_queue_remove_req import GdsQueueRemoveReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class GdsQueueRemoveServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | GdsQueueRemoveServicePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        gds_queue_remove_req: None | GdsQueueRemoveReq = field(
            default=None,
            metadata={
                "name": "GdsQueueRemoveReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/gdsQueue_v52_0",
            },
        )
