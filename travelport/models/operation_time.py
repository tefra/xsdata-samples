from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class OperationTime:
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
