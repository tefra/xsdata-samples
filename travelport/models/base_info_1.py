from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.agency_base_info_1 import AgencyBaseInfo1
from travelport.models.branch_base_info_1 import BranchBaseInfo1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class BaseInfo1:
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
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    agency_base_info: None | AgencyBaseInfo1 = field(
        default=None,
        metadata={
            "name": "AgencyBaseInfo",
            "type": "Element",
        },
    )
    branch_base_info: None | BranchBaseInfo1 = field(
        default=None,
        metadata={
            "name": "BranchBaseInfo",
            "type": "Element",
        },
    )
