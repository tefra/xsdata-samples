from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class Urlinfo:
    """
    Contains the text and URL of baggage as published by carrier.
    """

    class Meta:
        name = "URLInfo"
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
    url: list[str] = field(
        default_factory=list,
        metadata={
            "name": "URL",
            "type": "Element",
            "max_occurs": 999,
        },
    )
