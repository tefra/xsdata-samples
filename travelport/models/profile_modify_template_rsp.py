from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_5 import BaseRsp5
from travelport.models.profile_template import ProfileTemplate

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class ProfileModifyTemplateRsp(BaseRsp5):
    """
    Response with profile template data.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile_template: ProfileTemplate = field(
        metadata={
            "name": "ProfileTemplate",
            "type": "Element",
            "required": True,
        }
    )
