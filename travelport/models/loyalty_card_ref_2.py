from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass(kw_only=True)
class LoyaltyCardRef2:
    class Meta:
        name = "LoyaltyCardRef"
        namespace = "http://www.travelport.com/schema/common_v32_0"

    key: str = field(
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
