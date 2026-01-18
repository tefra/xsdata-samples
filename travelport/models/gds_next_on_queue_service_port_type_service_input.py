from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.gds_next_on_queue_req import GdsNextOnQueueReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class GdsNextOnQueueServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: GdsNextOnQueueServicePortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        gds_next_on_queue_req: GdsNextOnQueueReq = field(
            metadata={
                "name": "GdsNextOnQueueReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/gdsQueue_v52_0",
            }
        )
