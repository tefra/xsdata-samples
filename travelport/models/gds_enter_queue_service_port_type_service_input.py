from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.gds_enter_queue_req import GdsEnterQueueReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class GdsEnterQueueServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: GdsEnterQueueServicePortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        gds_enter_queue_req: GdsEnterQueueReq = field(
            metadata={
                "name": "GdsEnterQueueReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/gdsQueue_v52_0",
            }
        )
