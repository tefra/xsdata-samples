from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


class ActionStatusType5(Enum):
    """
    Properties
    ----------
    TAW
    TTL
    TLCXL
    ACTIVE
    CXL
    TAU
        Equivalent to TAX in Worldspan
    TRH
    """

    TAW = "TAW"
    TTL = "TTL"
    TLCXL = "TLCXL"
    ACTIVE = "ACTIVE"
    CXL = "CXL"
    TAU = "TAU"
    TRH = "TRH"
