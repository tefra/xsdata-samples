from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_5 import BaseReq5
from travelport.models.bridge_branch_cmd import BridgeBranchCmd

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileModifyBridgeBranchesReq(BaseReq5):
    """
    Request to add or delete an Agent's Bridge Branch Assignments.

    The Default branch cannot be modified. That functionality will only be
    used in the Profile Create and Modify services.

    Parameters
    ----------
    agent_id
        The system-assigned, unique profile ID of the agent.
    user_name
        The login name of the agent.
    bridge_branch_cmd
        Command to add or remove a Bridge Branch assignment
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    agent_id: None | int = field(
        default=None,
        metadata={
            "name": "AgentID",
            "type": "Element",
        },
    )
    user_name: None | str = field(
        default=None,
        metadata={
            "name": "UserName",
            "type": "Element",
            "min_length": 1,
            "max_length": 128,
        },
    )
    bridge_branch_cmd: list[BridgeBranchCmd] = field(
        default_factory=list,
        metadata={
            "name": "BridgeBranchCmd",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
