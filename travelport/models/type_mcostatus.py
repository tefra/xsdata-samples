from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


class TypeMcostatus(StrEnum):
    """
    The available status codes for an MCO.
    """

    OPEN = "Open"
    USED = "Used"
    REFUNDED = "Refunded"
    VOIDED = "Voided"
    EXPIRED = "Expired"
