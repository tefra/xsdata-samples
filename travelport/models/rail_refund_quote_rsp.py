from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.rail_refund_info import RailRefundInfo

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass(kw_only=True)
class RailRefundQuoteRsp(BaseRsp1):
    """
    Returns rail refund information.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    rail_refund_info: list[RailRefundInfo] = field(
        default_factory=list,
        metadata={
            "name": "RailRefundInfo",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
