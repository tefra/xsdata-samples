from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/system_v32_0"


@dataclass(kw_only=True)
class BridgedBranch:
    """
    A branch, identified by a branch ID, that an agent, who belongs to
    another branch, is allowed to do work in.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/system_v32_0"

    branch_id: str = field(
        metadata={
            "name": "BranchId",
            "type": "Attribute",
            "required": True,
        }
    )
