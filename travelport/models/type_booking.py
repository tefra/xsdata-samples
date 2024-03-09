from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeBooking(Enum):
    """
    Type of booking.
    """

    SSR = "SSR"
    AUXILLARY_SEGMENT = "Auxillary Segment"
    AVAILABLE_FOR_DISPLAY_PRICING = "Available for Display/Pricing"
    CONTACT_CARRIER_FOR_BOOKING = "Contact Carrier for Booking"
    NO_BOOKING_REQUIRED = "No Booking Required"
    APPLY_BOOKING_PER_SERVICE = "Apply booking per service"
