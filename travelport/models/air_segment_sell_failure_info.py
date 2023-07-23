from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_segment_error import AirSegmentError

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirSegmentSellFailureInfo:
    """
    Container to return air segment sell failures.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_segment_error: list[AirSegmentError] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentError",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
