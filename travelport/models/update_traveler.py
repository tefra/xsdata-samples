from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.booking_traveler_1 import BookingTraveler1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class UpdateTraveler:
    """
    Container for Travelers or its contents to be updated.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    booking_traveler: list[BookingTraveler1] = field(
        default_factory=list,
        metadata={
            "name": "BookingTraveler",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "min_occurs": 1,
            "max_occurs": 18,
        },
    )
