from __future__ import annotations

from dataclasses import dataclass

from travelport.models.base_rsp_5 import BaseRsp5

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileDeleteTagRsp2(BaseRsp5):
    """
    Successful Response that the tag has been deleted.
    """

    class Meta:
        name = "ProfileDeleteTagRsp"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"
