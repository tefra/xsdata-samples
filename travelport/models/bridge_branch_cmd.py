from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.bridge_branch_add import BridgeBranchAdd
from travelport.models.bridge_branch_delete import BridgeBranchDelete

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class BridgeBranchCmd:
    """
    Command to add or remove a Bridge Branch assignment.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    bridge_branch_add: None | BridgeBranchAdd = field(
        default=None,
        metadata={
            "name": "BridgeBranchAdd",
            "type": "Element",
        },
    )
    bridge_branch_delete: None | BridgeBranchDelete = field(
        default=None,
        metadata={
            "name": "BridgeBranchDelete",
            "type": "Element",
        },
    )
