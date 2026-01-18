from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass(kw_only=True)
class TypeTimeRange1:
    """
    Specify a range of times.
    """

    class Meta:
        name = "typeTimeRange"

    earliest_time: str = field(
        metadata={
            "name": "EarliestTime",
            "type": "Attribute",
            "required": True,
        }
    )
    latest_time: str = field(
        metadata={
            "name": "LatestTime",
            "type": "Attribute",
            "required": True,
        }
    )
