from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_5 import BaseRsp5
from travelport.models.profile_2 import Profile2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class ProfileRetrieveRsp2(BaseRsp5):
    """
    Response with the profile.
    """

    class Meta:
        name = "ProfileRetrieveRsp"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile: Profile2 = field(
        metadata={
            "name": "Profile",
            "type": "Element",
            "required": True,
        }
    )
