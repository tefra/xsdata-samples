from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.ssr_3 import Ssr3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class Ssrinfo3:
    """
    Bundle SSR with BookingTraveler reference in order to add SSR post booking.

    Parameters
    ----------
    ssr
    booking_traveler_ref
        Reference to Booking Traveler.
    """

    class Meta:
        name = "SSRInfo"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    ssr: None | Ssr3 = field(
        default=None,
        metadata={
            "name": "SSR",
            "type": "Element",
            "required": True,
        },
    )
    booking_traveler_ref: list[str] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "max_occurs": 999,
        },
    )
