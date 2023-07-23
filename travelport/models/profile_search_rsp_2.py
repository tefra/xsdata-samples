from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_rsp_5 import BaseRsp5
from travelport.models.profile_parent_search_summary_2 import ProfileParentSearchSummary2
from travelport.models.profile_summary_2 import ProfileSummary2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileSearchRsp2(BaseRsp5):
    """
    Response with the profile.

    Parameters
    ----------
    profile_summary
    profile_parent_search_summary
    search_token
        Search token generated after caching the results. Use this token in
        ProfileSearchReq to get the same result back in future profile
        search calls, if the cache still exists.
    more_results
        Indicates whether more results are available that match the search
        parameters.
    """
    class Meta:
        name = "ProfileSearchRsp"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile_summary: list[ProfileSummary2] = field(
        default_factory=list,
        metadata={
            "name": "ProfileSummary",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    profile_parent_search_summary: list[ProfileParentSearchSummary2] = field(
        default_factory=list,
        metadata={
            "name": "ProfileParentSearchSummary",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    search_token: None | str = field(
        default=None,
        metadata={
            "name": "SearchToken",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    more_results: None | bool = field(
        default=None,
        metadata={
            "name": "MoreResults",
            "type": "Attribute",
            "required": True,
        }
    )
