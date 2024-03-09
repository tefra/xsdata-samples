from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_filter_control_and_workspace_2 import (
    TypeFilterControlAndWorkspace2,
)
from travelport.models.type_profile_search_criteria_2 import (
    TypeProfileSearchCriteria2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class BranchCriteria2(TypeProfileSearchCriteria2):
    """
    Branch search modifiers.

    Parameters
    ----------
    name
        Branch name wild card
    iata_number
        IATA Number wild card
    branch_type
        Specify the Branch type filter.  Defaults to WorkspaceOnly.
    pseudo_city_code
        PseudoCityCode wild card
    branch_code
        Zircon site ID
    """

    class Meta:
        name = "BranchCriteria"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        },
    )
    iata_number: None | str = field(
        default=None,
        metadata={
            "name": "IataNumber",
            "type": "Attribute",
        },
    )
    branch_type: TypeFilterControlAndWorkspace2 = field(
        default=TypeFilterControlAndWorkspace2.WORKSPACE_ONLY,
        metadata={
            "name": "BranchType",
            "type": "Attribute",
        },
    )
    pseudo_city_code: None | str = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
        },
    )
    branch_code: None | str = field(
        default=None,
        metadata={
            "name": "BranchCode",
            "type": "Attribute",
        },
    )
