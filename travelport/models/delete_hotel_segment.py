from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_non_air_reservation_ref_1 import (
    TypeNonAirReservationRef1,
)

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass(kw_only=True)
class DeleteHotelSegment:
    """
    Container for Hotel Segment to be deleted.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    hotel_reservation_ref: TypeNonAirReservationRef1 = field(
        metadata={
            "name": "HotelReservationRef",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
