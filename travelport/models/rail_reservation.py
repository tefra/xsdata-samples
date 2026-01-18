from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_reservation_1 import BaseReservation1
from travelport.models.booking_traveler_ref_1 import BookingTravelerRef1
from travelport.models.payment_1 import Payment1
from travelport.models.rail_fare_note_list import RailFareNoteList
from travelport.models.rail_journey import RailJourney
from travelport.models.rail_pricing_info import RailPricingInfo
from travelport.models.rail_ticket_info import RailTicketInfo
from travelport.models.supplier_locator_1 import SupplierLocator1

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass(kw_only=True)
class RailReservation(BaseReservation1):
    """
    The parent container for all Rail booking data.

    Parameters
    ----------
    booking_traveler_ref
    rail_journey
    rail_pricing_info
    payment
    rail_ticket_info
    rail_fare_note_list
        List of RailFareNote(s) that is referenced by key in RailFare.
    supplier_locator
    booking_status
        The Current Status of the rail booking.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    booking_traveler_ref: list[BookingTravelerRef1] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "min_occurs": 1,
            "max_occurs": 9,
        },
    )
    rail_journey: list[RailJourney] = field(
        default_factory=list,
        metadata={
            "name": "RailJourney",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    rail_pricing_info: list[RailPricingInfo] = field(
        default_factory=list,
        metadata={
            "name": "RailPricingInfo",
            "type": "Element",
            "max_occurs": 999,
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
    rail_ticket_info: list[RailTicketInfo] = field(
        default_factory=list,
        metadata={
            "name": "RailTicketInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    rail_fare_note_list: None | RailFareNoteList = field(
        default=None,
        metadata={
            "name": "RailFareNoteList",
            "type": "Element",
        },
    )
    supplier_locator: list[SupplierLocator1] = field(
        default_factory=list,
        metadata={
            "name": "SupplierLocator",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    booking_status: str = field(
        metadata={
            "name": "BookingStatus",
            "type": "Attribute",
            "required": True,
        }
    )
