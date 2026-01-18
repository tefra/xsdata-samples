from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_2 import BaseRsp2
from travelport.models.profile_history_1 import ProfileHistory1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass(kw_only=True)
class ProfileRetrieveHistoryRsp1(BaseRsp2):
    """
    Response with the profile history filtered as specified in the request.

    Parameters
    ----------
    profile_history
    more_results
        Indicates whether more results are available that match the search
        parameters.
    """

    class Meta:
        name = "ProfileRetrieveHistoryRsp"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    profile_history: ProfileHistory1 = field(
        metadata={
            "name": "ProfileHistory",
            "type": "Element",
            "required": True,
        }
    )
    more_results: bool = field(
        metadata={
            "name": "MoreResults",
            "type": "Attribute",
            "required": True,
        }
    )
