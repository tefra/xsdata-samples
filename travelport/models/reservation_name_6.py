from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.booking_traveler_ref_6 import BookingTravelerRef6
from travelport.models.name_override_6 import NameOverride6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class ReservationName6:
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
        namespace = "http://www.travelport.com/schema/common_v38_0"

    booking_traveler_ref: None | BookingTravelerRef6 = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
        },
    )
    name_override: None | NameOverride6 = field(
        default=None,
        metadata={
            "name": "NameOverride",
            "type": "Element",
        },
    )
