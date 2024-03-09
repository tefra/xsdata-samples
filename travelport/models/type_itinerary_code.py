from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


class TypeItineraryCode(Enum):
    """
    Properties
    ----------
    INTERNATIONAL
        Indicates the itinerary is International
    DOMESTIC
        Indicates the itinerary is domestic
    """

    INTERNATIONAL = "International"
    DOMESTIC = "Domestic"
