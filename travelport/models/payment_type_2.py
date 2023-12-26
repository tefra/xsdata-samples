from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


class PaymentType2(Enum):
    """
    Properties
    ----------
    AIRLINE_FEE
        Payment for all airline based fees (paper ticket fee, SSR, etc.)
    DELIVERY_FEE
        Payment for agency ticket delivery fee
    ITINERARY
        Payment for all passengers
    PASSENGER
        Payment for a single passenger. The BookingTravelerRef attribute
        must be set.
    SERVICE_FEE
        Payment for a service fee other than an MCO
    OPTIONAL_SERVICE
        Payment for an optional service
    TICKET_FEE
        Deprecated
    """

    AIRLINE_FEE = "AirlineFee"
    DELIVERY_FEE = "DeliveryFee"
    ITINERARY = "Itinerary"
    PASSENGER = "Passenger"
    SERVICE_FEE = "ServiceFee"
    OPTIONAL_SERVICE = "OptionalService"
    TICKET_FEE = "TicketFee"
