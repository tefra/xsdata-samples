from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


class RailRefundReqRefundOption(StrEnum):
    RETAIN = "Retain"
    REFUND = "Refund"
