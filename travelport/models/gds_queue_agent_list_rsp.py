from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.queue_agent_record import QueueAgentRecord

__NAMESPACE__ = "http://www.travelport.com/schema/gdsQueue_v52_0"


@dataclass
class GdsQueueAgentListRsp(BaseRsp1):
    """
    Use this request to list items stuck on the Queue.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/gdsQueue_v52_0"

    queue_agent_record: list[QueueAgentRecord] = field(
        default_factory=list,
        metadata={
            "name": "QueueAgentRecord",
            "type": "Element",
            "max_occurs": 999,
        }
    )
