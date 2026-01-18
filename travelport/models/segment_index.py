from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class SegmentIndex:
    """
    Identifies the segment that is part of this group.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    value: int = field(
        metadata={
            "required": True,
        }
    )
