from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class TypeTimeRange2:
    """
    Specify a range of times.
    """
    class Meta:
        name = "typeTimeRange"

    earliest_time: None | str = field(
        default=None,
        metadata={
            "name": "EarliestTime",
            "type": "Attribute",
            "required": True,
        }
    )
    latest_time: None | str = field(
        default=None,
        metadata={
            "name": "LatestTime",
            "type": "Attribute",
            "required": True,
        }
    )
