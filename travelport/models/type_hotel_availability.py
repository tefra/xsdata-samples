from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


class TypeHotelAvailability(Enum):
    """
    Availability status of hotel Hotel is Available NotAvailable Available, but not
    for the rates requested On request Unknown.
    """

    AVAILABLE = "Available"
    NOT_AVAILABLE = "NotAvailable"
    AVAILABLE_FOR_OTHER_RATES = "AvailableForOtherRates"
    ON_REQUEST = "OnRequest"
    UNKNOWN = "Unknown"
