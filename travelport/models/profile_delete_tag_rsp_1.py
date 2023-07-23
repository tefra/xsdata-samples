from __future__ import annotations
from dataclasses import dataclass
from travelport.models.base_rsp_2 import BaseRsp2

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class ProfileDeleteTagRsp1(BaseRsp2):
    """
    Successful Response that the tag has been deleted.
    """
    class Meta:
        name = "ProfileDeleteTagRsp"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"
