from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_rsp_5 import BaseRsp5
from travelport.models.profile_2 import Profile2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileCreateRsp2(BaseRsp5):
    """
    Response with the newly created profile.
    """

    class Meta:
        name = "ProfileCreateRsp"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile: None | Profile2 = field(
        default=None,
        metadata={
            "name": "Profile",
            "type": "Element",
            "required": True,
        },
    )
