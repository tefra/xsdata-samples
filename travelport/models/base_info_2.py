from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.agency_base_info_2 import AgencyBaseInfo2
from travelport.models.branch_base_info_2 import BranchBaseInfo2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class BaseInfo2:
    """
    Parameters
    ----------
    agency_base_info
        Information relating to Agency.
    branch_base_info
        Information relating to Branch.
    """

    class Meta:
        name = "BaseInfo"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    agency_base_info: None | AgencyBaseInfo2 = field(
        default=None,
        metadata={
            "name": "AgencyBaseInfo",
            "type": "Element",
        },
    )
    branch_base_info: None | BranchBaseInfo2 = field(
        default=None,
        metadata={
            "name": "BranchBaseInfo",
            "type": "Element",
        },
    )
