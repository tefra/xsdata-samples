from __future__ import annotations

from dataclasses import dataclass

from travelport.models.base_rsp_5 import BaseRsp5

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class ProfileDeleteRsp2(BaseRsp5):
    """
    Response will only include warnings if they exist.
    """

    class Meta:
        name = "ProfileDeleteRsp"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"
