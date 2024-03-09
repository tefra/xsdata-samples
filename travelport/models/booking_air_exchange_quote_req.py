from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_pricing_solution import AirPricingSolution
from travelport.models.booking_base_req import BookingBaseReq
from travelport.models.original_itinerary_details import (
    OriginalItineraryDetails,
)
from travelport.models.repricing_modifiers import RepricingModifiers
from travelport.models.ticket_number_1 import TicketNumber1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class BookingAirExchangeQuoteReq(BookingBaseReq):
    """
    Quotes the new exchange based on the new segments.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    ticket_number: list[TicketNumber1] = field(
        default_factory=list,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        },
    )
    air_pricing_solution: list[AirPricingSolution] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingSolution",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "min_occurs": 1,
            "max_occurs": 5,
        },
    )
    repricing_modifiers: list[RepricingModifiers] = field(
        default_factory=list,
        metadata={
            "name": "RepricingModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "min_occurs": 1,
            "max_occurs": 5,
        },
    )
    original_itinerary_details: None | OriginalItineraryDetails = field(
        default=None,
        metadata={
            "name": "OriginalItineraryDetails",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "required": True,
        },
    )
