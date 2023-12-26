from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_rsp_2 import BaseRsp2
from travelport.models.profile_child_summary_1 import ProfileChildSummary1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class ProfileChildSearchRsp1(BaseRsp2):
    """
    Response to allow a user to retrieve the immediate children of a given profile.

    Parameters
    ----------
    profile_child_summary
        Summary of each Profile Child
    more_results
        Indicates whether more results are available that match the search
        parameters.
    number_of_children
        Total number of children that the profile searched under has,
    """

    class Meta:
        name = "ProfileChildSearchRsp"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    profile_child_summary: list[ProfileChildSummary1] = field(
        default_factory=list,
        metadata={
            "name": "ProfileChildSummary",
            "type": "Element",
        },
    )
    more_results: None | bool = field(
        default=None,
        metadata={
            "name": "MoreResults",
            "type": "Attribute",
            "required": True,
        },
    )
    number_of_children: None | int = field(
        default=None,
        metadata={
            "name": "NumberOfChildren",
            "type": "Attribute",
        },
    )
