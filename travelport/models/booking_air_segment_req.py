from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.add_air_segment import AddAirSegment
from travelport.models.booking_base_req import BookingBaseReq
from travelport.models.delete_air_segment import DeleteAirSegment
from travelport.models.update_air_segment import UpdateAirSegment

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class BookingAirSegmentReq(BookingBaseReq):
    """
    Used for Air Segment Sell and modification.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    add_air_segment: None | AddAirSegment = field(
        default=None,
        metadata={
            "name": "AddAirSegment",
            "type": "Element",
        },
    )
    update_air_segment: None | UpdateAirSegment = field(
        default=None,
        metadata={
            "name": "UpdateAirSegment",
            "type": "Element",
        },
    )
    delete_air_segment: None | DeleteAirSegment = field(
        default=None,
        metadata={
            "name": "DeleteAirSegment",
            "type": "Element",
        },
    )
