from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.rail_segment import RailSegment

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass
class RailSegmentList:
    """
    List of Rail Segments.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    rail_segment: list[RailSegment] = field(
        default_factory=list,
        metadata={
            "name": "RailSegment",
            "type": "Element",
            "max_occurs": 999,
        }
    )
