from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.coach import Coach

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass(kw_only=True)
class RailSeatMapRsp(BaseRsp1):
    """
    Returns rail seat map/coach map.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    coach: list[Coach] = field(
        default_factory=list,
        metadata={
            "name": "Coach",
            "type": "Element",
            "max_occurs": 999,
        },
    )
