from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


class ActionStatusType2(Enum):
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
