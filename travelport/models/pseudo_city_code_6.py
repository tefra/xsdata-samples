from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class PseudoCityCode6:
    class Meta:
        name = "PseudoCityCode"
        namespace = "http://www.travelport.com/schema/common_v34_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 2,
            "max_length": 10,
        },
    )
