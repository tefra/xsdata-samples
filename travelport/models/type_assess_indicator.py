from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeAssessIndicator(Enum):
    """
    The type of AssessIndicator.
    """

    MILEAGE_AND_CURRENCY = "MileageAndCurrency"
    MILEAGE_OR_CURRENCY = "MileageOrCurrency"
