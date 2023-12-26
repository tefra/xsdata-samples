from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class TypeTextBlock1:
    class Meta:
        name = "typeTextBlock"

    text: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 100,
        },
    )
