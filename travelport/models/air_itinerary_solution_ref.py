from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class AirItinerarySolutionRef:
    """
    Reference to a complete AirItinerarySolution from a shared list.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    key: str = field(
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
