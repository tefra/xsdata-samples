from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_agency_hierarchy_reference_6 import (
    TypeAgencyHierarchyReference6,
)

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class TypeAgencyHierarchyLongReference6(TypeAgencyHierarchyReference6):
    """
    Parameters
    ----------
    profile_version
    profile_name
        Initially: Agent: Last, First, Branch: BranchCode, Agency: Name.
        After new profile  implementation: Agent: UserName, others levels:
        Name.
    """

    class Meta:
        name = "typeAgencyHierarchyLongReference"

    profile_version: None | int = field(
        default=None,
        metadata={
            "name": "ProfileVersion",
            "type": "Attribute",
            "required": True,
        },
    )
    profile_name: None | str = field(
        default=None,
        metadata={
            "name": "ProfileName",
            "type": "Attribute",
            "required": True,
            "max_length": 102,
        },
    )
