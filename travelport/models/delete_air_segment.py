from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_segment_ref_1 import TypeSegmentRef1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class DeleteAirSegment:
    """
    Container for Air Segment to be deleted.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    air_segment_ref: list[TypeSegmentRef1] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentRef",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 8,
        },
    )
