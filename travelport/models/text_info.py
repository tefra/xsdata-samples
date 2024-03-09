from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class TextInfo:
    """
    Information on baggage as published by carrier.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    text: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "max_occurs": 999,
            "max_length": 250,
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Attribute",
        },
    )
