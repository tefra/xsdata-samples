from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/terminal_v33_0"


@dataclass
class TypeTextBlock2:
    class Meta:
        name = "typeTextBlock"

    text: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/terminal_v33_0",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
