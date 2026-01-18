from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_3 import BaseRsp3
from travelport.models.system_info import SystemInfo
from travelport.models.system_time import SystemTime

__NAMESPACE__ = "http://www.travelport.com/schema/system_v32_0"


@dataclass(kw_only=True)
class SystemInfoRsp(BaseRsp3):
    class Meta:
        namespace = "http://www.travelport.com/schema/system_v32_0"

    system_info: SystemInfo = field(
        metadata={
            "name": "SystemInfo",
            "type": "Element",
            "required": True,
        }
    )
    system_time: SystemTime = field(
        metadata={
            "name": "SystemTime",
            "type": "Element",
            "required": True,
        }
    )
