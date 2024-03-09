from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class HotelSpecialRequest:
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 250,
        },
    )
