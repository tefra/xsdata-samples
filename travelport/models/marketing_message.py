from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class MarketingMessage:
    """
    Marketing information provided by the supplier.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    text: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "max_occurs": 99,
        },
    )
