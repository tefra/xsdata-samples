from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


class TypeMcostatus(Enum):
    """
    The available status codes for an MCO.
    """

    OPEN = "Open"
    USED = "Used"
    REFUNDED = "Refunded"
    VOIDED = "Voided"
    EXPIRED = "Expired"
