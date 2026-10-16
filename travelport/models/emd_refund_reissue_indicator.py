from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class EmdRefundReissueIndicator(StrEnum):
    REFUNDABLE = "Refundable"
    NON_REFUNDABLE = "NonRefundable"
    REUSE = "Reuse"
