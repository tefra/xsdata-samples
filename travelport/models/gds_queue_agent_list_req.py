from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_1 import BaseReq1

__NAMESPACE__ = "http://www.travelport.com/schema/gdsQueue_v52_0"


@dataclass
class GdsQueueAgentListReq(BaseReq1):
    """
    Use this request to list items stuck on the Queue.

    Parameters
    ----------
    agent_id
        The Agent ID for the applicable supplier/vendor
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/gdsQueue_v52_0"

    agent_id: None | str = field(
        default=None,
        metadata={
            "name": "AgentID",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 32,
        }
    )
