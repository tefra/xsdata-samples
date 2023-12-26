from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class PassengerReceiptOverride:
    """
    It is required when a passenger receipt is required immediately ,GDS overrides
    the default value.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "white_space": "collapse",
        },
    )
