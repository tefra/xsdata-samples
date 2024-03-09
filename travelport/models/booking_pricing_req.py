from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.add_pricing import AddPricing
from travelport.models.booking_base_req import BookingBaseReq
from travelport.models.delete_pricing import DeletePricing

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class BookingPricingReq(BookingBaseReq):
    """
    Stores/Modifies pricing.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    add_pricing: None | AddPricing = field(
        default=None,
        metadata={
            "name": "AddPricing",
            "type": "Element",
        },
    )
    delete_pricing: None | DeletePricing = field(
        default=None,
        metadata={
            "name": "DeletePricing",
            "type": "Element",
        },
    )
