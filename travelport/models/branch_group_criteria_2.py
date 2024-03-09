from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_profile_search_criteria_2 import (
    TypeProfileSearchCriteria2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class BranchGroupCriteria2(TypeProfileSearchCriteria2):
    """
    Branch Group search modifiers.

    Parameters
    ----------
    name
        Branch Group name wild card
    branch_group_code
        Zircon site ID
    """

    class Meta:
        name = "BranchGroupCriteria"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        },
    )
    branch_group_code: None | str = field(
        default=None,
        metadata={
            "name": "BranchGroupCode",
            "type": "Attribute",
        },
    )
