from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


class BookingSourceType3(Enum):
    """
    Properties
    ----------
    PSEUDO_CITY_CODE
    ARC_NUMBER
    IATA_NUMBER
    CUSTOMER_ID
    BOOKING_SOURCE_OVERRIDE
        The Booking Source Override is usually used when the car supplier
        has assigned a number (which can be alpha/numeric) to the
        agency/e-commerce to use in place of an IATA number. Supported
        provider(s) : 1P/1J
    """
    PSEUDO_CITY_CODE = "PseudoCityCode"
    ARC_NUMBER = "ArcNumber"
    IATA_NUMBER = "IataNumber"
    CUSTOMER_ID = "CustomerId"
    BOOKING_SOURCE_OVERRIDE = "BookingSourceOverride"
