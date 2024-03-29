from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_3 import BaseReq3
from travelport.models.payload import Payload

__NAMESPACE__ = "http://www.travelport.com/schema/system_v32_0"


@dataclass
class PingReq(BaseReq3):
    """
    A simple request to test connectivity to the system without imposing any
    actions.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/system_v32_0"

    payload: None | Payload = field(
        default=None,
        metadata={
            "name": "Payload",
            "type": "Element",
        },
    )
