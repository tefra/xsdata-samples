from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeVarianceType(Enum):
    """
    Type code for Variance.
    """

    ACTUAL = "Actual"
    ESTIMATED = "Estimated"
    CANCELED = "Canceled"
    DIVERSION = "Diversion"
