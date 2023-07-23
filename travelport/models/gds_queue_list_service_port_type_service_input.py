from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.gds_queue_list_req import GdsQueueListReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class GdsQueueListServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | GdsQueueListServicePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        gds_queue_list_req: None | GdsQueueListReq = field(
            default=None,
            metadata={
                "name": "GdsQueueListReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/gdsQueue_v52_0",
            }
        )
