from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_3 import BaseRsp3
from travelport.models.system_time import SystemTime

__NAMESPACE__ = "http://www.travelport.com/schema/system_v32_0"


@dataclass(kw_only=True)
class TimeRsp(BaseRsp3):
    """
    Returns the time of the system.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/system_v32_0"

    system_time: None | SystemTime = field(
        default=None,
        metadata={
            "name": "SystemTime",
            "type": "Element",
        },
    )
