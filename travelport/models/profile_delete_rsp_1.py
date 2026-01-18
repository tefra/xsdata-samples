from __future__ import annotations

from dataclasses import dataclass

from travelport.models.base_rsp_2 import BaseRsp2

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass(kw_only=True)
class ProfileDeleteRsp1(BaseRsp2):
    """
    Response will only include warnings if they exist.
    """

    class Meta:
        name = "ProfileDeleteRsp"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"
