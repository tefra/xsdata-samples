from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeConnectionIndicator(Enum):
    """
    Types of connection indicator : AvailabilityAndPricing : Specified
    availability and pricing connection; TurnAround : Specified turn
    around; Stopover : Specified stopover;.
    """

    AVAILABILITY_AND_PRICING = "AvailabilityAndPricing"
    TURN_AROUND = "TurnAround"
    STOPOVER = "Stopover"
