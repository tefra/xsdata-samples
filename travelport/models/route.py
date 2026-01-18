from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.leg import Leg

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class Route:
    """
    Information about this Route component.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    leg: list[Leg] = field(
        default_factory=list,
        metadata={
            "name": "Leg",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    key: str = field(
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
