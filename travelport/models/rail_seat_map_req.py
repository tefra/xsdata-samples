from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_1 import BaseReq1
from travelport.models.rail_info import RailInfo

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass(kw_only=True)
class RailSeatMapReq(BaseReq1):
    """
    Request a rail seat map/coach map.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    rail_info: RailInfo = field(
        metadata={
            "name": "RailInfo",
            "type": "Element",
            "required": True,
        }
    )
