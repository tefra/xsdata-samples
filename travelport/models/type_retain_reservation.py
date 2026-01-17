from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


class TypeRetainReservation(Enum):
    """
    Retain the Reservation (do not cancel) in the the event of a schedule
    or price change.
    """

    NONE = "None"
    SCHEDULE = "Schedule"
    PRICE = "Price"
    BOTH = "Both"
