from __future__ import annotations
from dataclasses import dataclass
from travelport.models.base_rsp_2 import BaseRsp2

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class UimetaDataDeleteRsp(BaseRsp2):
    """
    Service for Response to delete any settings by user in Profile Settings.
    """
    class Meta:
        name = "UIMetaDataDeleteRsp"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"
