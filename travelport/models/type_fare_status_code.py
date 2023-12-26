from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeFareStatusCode(Enum):
    """
    Properties
    ----------
    READY_TO_TICKET
        Fare is enabled and available for ticketing
    UNABLE_TO_TICKET
        Fare could not be ticketed
    REPRICE
        Fare needs to be repriced
    TICKETED
        Fare is ticketed
    UNABLE
        Fare is not enabled
    UNKNOWN
        To handle new enumerations added by provider but currently not
        recognized by API
    """

    READY_TO_TICKET = "ReadyToTicket"
    UNABLE_TO_TICKET = "UnableToTicket"
    REPRICE = "Reprice"
    TICKETED = "Ticketed"
    UNABLE = "Unable"
    UNKNOWN = "Unknown"
