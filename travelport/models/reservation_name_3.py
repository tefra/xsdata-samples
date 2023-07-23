from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.booking_traveler_ref_3 import BookingTravelerRef3
from travelport.models.name_override_3 import NameOverride3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class ReservationName3:
    """
    Container to represent reservation name as appears in GDS booking.

    Parameters
    ----------
    booking_traveler_ref
    name_override
        To be used if the reservation name is other than booking travelers
        in the PNR
    """
    class Meta:
        name = "ReservationName"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    booking_traveler_ref: None | BookingTravelerRef3 = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
        }
    )
    name_override: None | NameOverride3 = field(
        default=None,
        metadata={
            "name": "NameOverride",
            "type": "Element",
        }
    )
