from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/gdsQueue_v52_0"


@dataclass
class PseudoCityCode2:
    class Meta:
        name = "PseudoCityCode"
        namespace = "http://www.travelport.com/schema/gdsQueue_v52_0"

    value: None | str = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 10,
        },
    )
