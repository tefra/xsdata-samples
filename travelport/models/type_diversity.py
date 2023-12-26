from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeDiversity(Enum):
    """
    Used in Low Fare Search to better promote unique results.
    """

    BLEND = "Blend"
    AIRPORTS = "Airports"
    CARRIER = "Carrier"
    ORIGIN = "Origin"
    DESTINATION = "Destination"
    DATE_COMBINATION = "DateCombination"
    FIRST_ODDATE = "FirstODDate"
    SECOND_ODDATE = "SecondODDate"
    FIRST_OD = "FirstOD"
    SECOND_OD = "SecondOD"
