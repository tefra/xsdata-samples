from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeVarianceIndicator(Enum):
    """
    Type code for Variance.
    """

    EARLY = "Early"
    LATE = "Late"
