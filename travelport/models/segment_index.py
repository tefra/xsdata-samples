from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class SegmentIndex:
    """
    Identifies the segment that is part of this group.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    value: None | int = field(
        default=None,
        metadata={
            "required": True,
        },
    )
