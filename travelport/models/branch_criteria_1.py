from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_filter_control_and_workspace_1 import (
    TypeFilterControlAndWorkspace1,
)
from travelport.models.type_profile_search_criteria_1 import (
    TypeProfileSearchCriteria1,
)

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass(kw_only=True)
class BranchCriteria1(TypeProfileSearchCriteria1):
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
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

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
    branch_type: TypeFilterControlAndWorkspace1 = field(
        default=TypeFilterControlAndWorkspace1.WORKSPACE_ONLY,
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
