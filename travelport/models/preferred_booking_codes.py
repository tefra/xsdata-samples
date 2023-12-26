from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.booking_code import BookingCode

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class PreferredBookingCodes:
    """
    This is the container to specify all preferred booking codes.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    booking_code: list[BookingCode] = field(
        default_factory=list,
        metadata={
            "name": "BookingCode",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
