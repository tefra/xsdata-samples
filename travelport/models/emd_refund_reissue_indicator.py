from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class EmdRefundReissueIndicator(Enum):
    REFUNDABLE = "Refundable"
    NON_REFUNDABLE = "NonRefundable"
    REUSE = "Reuse"
