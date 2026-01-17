from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


class TypeNetTransCommission(Enum):
    """
    Type to support net trans commission indicator.

    Supported for 1G and 1V provider. A stands for Excellent. B stands for
    Good. C stands for Poor. P stands for Payment Bureau X stands for
    Unknown. To support any other value than A,B,C and P.
    """

    A = "A"
    B = "B"
    C = "C"
    P = "P"
    X = "X"
