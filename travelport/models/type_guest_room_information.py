from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.booking_traveler_ref_1 import BookingTravelerRef1
from travelport.models.type_guest_child_information import TypeGuestChildInformation

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class TypeGuestRoomInformation:
    """
    Information about guest to book.

    Parameters
    ----------
    adults
        The number of adult guests per room. Maximum number of adults may
        vary by supplier or aggregator.
    booking_traveler_ref
        Reference for the Booking Traveler. Used for Hotel Booking only. The
        value is arbitrary.
    child
        Information about a child guest.
    """
    class Meta:
        name = "typeGuestRoomInformation"

    adults: None | int = field(
        default=None,
        metadata={
            "name": "Adults",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "required": True,
        }
    )
    booking_traveler_ref: list[BookingTravelerRef1] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 9,
        }
    )
    child: list[TypeGuestRoomInformation.Child] = field(
        default_factory=list,
        metadata={
            "name": "Child",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "max_occurs": 6,
        }
    )

    @dataclass
    class Child(TypeGuestChildInformation):
        """
        Parameters
        ----------
        booking_traveler_ref
            Reference for the Booking Traveler. Used for Hotel Booking only.
            The value is arbitrary.
        """
        booking_traveler_ref: None | BookingTravelerRef1 = field(
            default=None,
            metadata={
                "name": "BookingTravelerRef",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
            }
        )
