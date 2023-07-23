from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_rsp_2 import BaseRsp2
from travelport.models.profile_1 import Profile1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class ProfileRetrieveRsp1(BaseRsp2):
    """
    Response with the profile.
    """
    class Meta:
        name = "ProfileRetrieveRsp"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    profile: None | Profile1 = field(
        default=None,
        metadata={
            "name": "Profile",
            "type": "Element",
            "required": True,
        }
    )
