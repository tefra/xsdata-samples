from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class SellMessage3:
    """Sell Message from Vendor.

    This is applicable in response messages only, any input in request
    message will be ignored.
    """

    class Meta:
        name = "SellMessage"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
