from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


class TypeServiceFeeType1(Enum):
    """
    A code for categorizing service fees or charges.
    """

    CANCELLATION = "Cancellation"
    CHANGE = "Change"
    EXCHANGE = "Exchange"
    FLAT = "Flat"
    MANUAL_BOOKING = "Manual Booking"
    MISCELLANEOUS = "Miscellaneous"
    NEW_BOOKING = "New Booking"
    PER_PERSON = "Per Person"
    PHONE_BOOKING = "Phone Booking"
    PROCESSING = "Processing"
    REFUND = "Refund"
    FEE_CAP = "Fee Cap"
