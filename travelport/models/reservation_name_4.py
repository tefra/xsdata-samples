from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.booking_traveler_ref_4 import BookingTravelerRef4
from travelport.models.name_override_4 import NameOverride4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass(kw_only=True)
class ReservationName4:
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
        namespace = "http://www.travelport.com/schema/common_v37_0"

    booking_traveler_ref: None | BookingTravelerRef4 = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
        },
    )
    name_override: None | NameOverride4 = field(
        default=None,
        metadata={
            "name": "NameOverride",
            "type": "Element",
        },
    )
