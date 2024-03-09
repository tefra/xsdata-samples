from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeInventoryRequest(Enum):
    """The valid inventory types are Seamless - A, DirectAccess - B, Basic - C"""

    SEAMLESS = "Seamless"
    DIRECT_ACCESS = "DirectAccess"
    BASIC = "Basic"
