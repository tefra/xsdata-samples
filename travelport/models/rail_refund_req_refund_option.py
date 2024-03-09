from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


class RailRefundReqRefundOption(Enum):
    RETAIN = "Retain"
    REFUND = "Refund"
