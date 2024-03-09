from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_5 import BaseRsp5
from travelport.models.profile_history_2 import ProfileHistory2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileRetrieveHistoryRsp2(BaseRsp5):
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
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile_history: None | ProfileHistory2 = field(
        default=None,
        metadata={
            "name": "ProfileHistory",
            "type": "Element",
            "required": True,
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
