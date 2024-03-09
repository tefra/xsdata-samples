from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class CarrierCode:
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "length": 2,
        },
    )
