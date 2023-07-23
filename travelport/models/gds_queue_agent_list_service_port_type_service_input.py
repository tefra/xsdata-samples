from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.gds_queue_agent_list_req import GdsQueueAgentListReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class GdsQueueAgentListServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | GdsQueueAgentListServicePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        gds_queue_agent_list_req: None | GdsQueueAgentListReq = field(
            default=None,
            metadata={
                "name": "GdsQueueAgentListReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/gdsQueue_v52_0",
            }
        )
