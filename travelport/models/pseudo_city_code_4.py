from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass(kw_only=True)
class PseudoCityCode4:
    class Meta:
        name = "PseudoCityCode"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 2,
            "max_length": 10,
        },
    )
