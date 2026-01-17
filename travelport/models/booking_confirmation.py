from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class BookingConfirmation:
    """
    Hotel Booking Confirmation Number for hotel segment.

    Supported Providers:1P.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    value: str = field(
        default="",
        metadata={
            "max_length": 32,
        },
    )
