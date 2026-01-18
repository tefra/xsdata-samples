from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.ssr_2 import Ssr2

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass(kw_only=True)
class Ssrinfo2:
    """
    Bundle SSR with BookingTraveler reference in order to add SSR post
    booking.

    Parameters
    ----------
    ssr
    booking_traveler_ref
        Reference to Booking Traveler.
    """

    class Meta:
        name = "SSRInfo"
        namespace = "http://www.travelport.com/schema/common_v32_0"

    ssr: Ssr2 = field(
        metadata={
            "name": "SSR",
            "type": "Element",
            "required": True,
        }
    )
    booking_traveler_ref: list[str] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "max_occurs": 999,
        },
    )
