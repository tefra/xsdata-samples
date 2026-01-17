from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_5 import BaseRsp5
from travelport.models.bridge_branch import BridgeBranch

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileRetrieveBridgeBranchesRsp(BaseRsp5):
    """
    Response to retreive an Agent's Bridge Branch Assignments.

    Returns the list of bridge branches that the agent is currently
    assigned to.

    Parameters
    ----------
    bridge_branch
    agent_id
        The system-assigned, unique profile ID of the agent.
    user_name
        The login name of the agent.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    bridge_branch: list[BridgeBranch] = field(
        default_factory=list,
        metadata={
            "name": "BridgeBranch",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    agent_id: None | int = field(
        default=None,
        metadata={
            "name": "AgentID",
            "type": "Attribute",
            "required": True,
        },
    )
    user_name: None | str = field(
        default=None,
        metadata={
            "name": "UserName",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        },
    )
