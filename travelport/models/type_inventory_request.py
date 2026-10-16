from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeInventoryRequest(StrEnum):
    """
    The valid inventory types are Seamless - A, DirectAccess - B, Basic -
    C.
    """

    SEAMLESS = "Seamless"
    DIRECT_ACCESS = "DirectAccess"
    BASIC = "Basic"
