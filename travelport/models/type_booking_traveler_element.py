from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


class TypeBookingTravelerElement(Enum):
    """
    Defines the list of available data types for modifications.
    """

    BOOKING_TRAVELER = "BookingTraveler"
    PHONE_NUMBER = "PhoneNumber"
    EMAIL = "Email"
    NAME_REMARK = "NameRemark"
    DELIVERY_INFO = "DeliveryInfo"
    ADDRESS = "Address"
    APPLIED_PROFILE = "AppliedProfile"
    CUSTOMIZED_NAME_DATA = "CustomizedNameData"
