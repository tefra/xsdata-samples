from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_5 import BaseReq5

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileRetrieveBridgeBranchesReq(BaseReq5):
    """
    Request to retrieve an Agent's Bridge Branch Assignments.

    Parameters
    ----------
    agent_id
        The system-assigned, unique profile ID of the agent.
    user_name
        The login name of the agent.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    agent_id: None | int = field(
        default=None,
        metadata={
            "name": "AgentID",
            "type": "Element",
        }
    )
    user_name: None | str = field(
        default=None,
        metadata={
            "name": "UserName",
            "type": "Element",
            "min_length": 1,
            "max_length": 128,
        }
    )
