from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.gds_exit_queue_req import GdsExitQueueReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class GdsExitQueueServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: GdsExitQueueServicePortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        gds_exit_queue_req: GdsExitQueueReq = field(
            metadata={
                "name": "GdsExitQueueReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/gdsQueue_v52_0",
            }
        )
