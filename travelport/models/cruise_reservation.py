from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_reservation_1 import BaseReservation1
from travelport.models.booking_traveler_ref_1 import BookingTravelerRef1
from travelport.models.cruise_itinerary import CruiseItinerary
from travelport.models.cruise_pricing_info import CruisePricingInfo
from travelport.models.cruise_segment import CruiseSegment
from travelport.models.optional_service_2 import OptionalService2
from travelport.models.payment_1 import Payment1
from travelport.models.provider_reservation_info_ref_1 import (
    ProviderReservationInfoRef1,
)

__NAMESPACE__ = "http://www.travelport.com/schema/cruise_v52_0"


@dataclass(kw_only=True)
class CruiseReservation(BaseReservation1):
    """
    The parent container for all cruise booking data.

    Parameters
    ----------
    cruise_segment
    cruise_itinerary
    cruise_pricing_info
        Cruise pricing Information. Contains all        related pricing data
        for travelers.
    optional_service
    booking_traveler_ref
    provider_reservation_info_ref
    payment
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/cruise_v52_0"

    cruise_segment: None | CruiseSegment = field(
        default=None,
        metadata={
            "name": "CruiseSegment",
            "type": "Element",
        },
    )
    cruise_itinerary: list[CruiseItinerary] = field(
        default_factory=list,
        metadata={
            "name": "CruiseItinerary",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    cruise_pricing_info: None | CruisePricingInfo = field(
        default=None,
        metadata={
            "name": "CruisePricingInfo",
            "type": "Element",
        },
    )
    optional_service: list[OptionalService2] = field(
        default_factory=list,
        metadata={
            "name": "OptionalService",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    booking_traveler_ref: list[BookingTravelerRef1] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    provider_reservation_info_ref: None | ProviderReservationInfoRef1 = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    payment: list[Payment1] = field(
        default_factory=list,
        metadata={
            "name": "Payment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
