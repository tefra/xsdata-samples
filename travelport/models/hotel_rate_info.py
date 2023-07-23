from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class HotelRateInfo:
    """
    This is a wrapper element for updating Rate Modifiers.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    rate_plan_type: None | str = field(
        default=None,
        metadata={
            "name": "RatePlanType",
            "type": "Attribute",
        }
    )
