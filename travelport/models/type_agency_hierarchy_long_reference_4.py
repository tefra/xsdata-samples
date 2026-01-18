from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_agency_hierarchy_reference_4 import (
    TypeAgencyHierarchyReference4,
)

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass(kw_only=True)
class TypeAgencyHierarchyLongReference4(TypeAgencyHierarchyReference4):
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

    profile_version: int = field(
        metadata={
            "name": "ProfileVersion",
            "type": "Attribute",
            "required": True,
        }
    )
    profile_name: str = field(
        metadata={
            "name": "ProfileName",
            "type": "Attribute",
            "required": True,
            "max_length": 102,
        }
    )
