from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class PromotionCode:
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 30,
        }
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
