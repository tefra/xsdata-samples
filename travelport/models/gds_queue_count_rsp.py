from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.queue_info import QueueInfo

__NAMESPACE__ = "http://www.travelport.com/schema/gdsQueue_v52_0"


@dataclass
class GdsQueueCountRsp(BaseRsp1):
    """
    The response from the host for a queue count.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/gdsQueue_v52_0"

    queue_info: list[QueueInfo] = field(
        default_factory=list,
        metadata={
            "name": "QueueInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
