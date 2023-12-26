from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.gds_queue_count_req import GdsQueueCountReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class GdsQueueCountServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | GdsQueueCountServicePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        gds_queue_count_req: None | GdsQueueCountReq = field(
            default=None,
            metadata={
                "name": "GdsQueueCountReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/gdsQueue_v52_0",
            },
        )
