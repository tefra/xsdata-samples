from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_segment_error import AirSegmentError
from travelport.models.type_error_info_1 import TypeErrorInfo1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AvailabilityErrorInfo(TypeErrorInfo1):
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_segment_error: list[AirSegmentError] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentError",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
