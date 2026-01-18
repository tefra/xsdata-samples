from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass(kw_only=True)
class TypeSegmentRef1:
    class Meta:
        name = "typeSegmentRef"

    key: str = field(
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
