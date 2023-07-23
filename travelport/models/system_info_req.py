from __future__ import annotations
from dataclasses import dataclass
from travelport.models.base_req_3 import BaseReq3

__NAMESPACE__ = "http://www.travelport.com/schema/system_v32_0"


@dataclass
class SystemInfoReq(BaseReq3):
    """
    Requests system information.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/system_v32_0"
