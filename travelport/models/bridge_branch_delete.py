from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_bridge_branch_cmd import TypeBridgeBranchCmd

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class BridgeBranchDelete(TypeBridgeBranchCmd):
    """
    Command to delete a bridge branch assoication of an agent.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"
