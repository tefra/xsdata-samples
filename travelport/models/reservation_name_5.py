from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.booking_traveler_ref_5 import BookingTravelerRef5
from travelport.models.name_override_5 import NameOverride5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass(kw_only=True)
class ReservationName5:
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
        namespace = "http://www.travelport.com/schema/common_v34_0"

    booking_traveler_ref: None | BookingTravelerRef5 = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
        },
    )
    name_override: None | NameOverride5 = field(
        default=None,
        metadata={
            "name": "NameOverride",
            "type": "Element",
        },
    )
