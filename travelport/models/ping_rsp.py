from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_rsp_3 import BaseRsp3

__NAMESPACE__ = "http://www.travelport.com/schema/system_v32_0"


@dataclass
class PingRsp(BaseRsp3):
    """Response to the PingReq.

    Will contain the exact payload (if any) that was sent in
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/system_v32_0"

    payload: None | str = field(
        default=None,
        metadata={
            "name": "Payload",
            "type": "Element",
            "max_length": 32768,
        }
    )
