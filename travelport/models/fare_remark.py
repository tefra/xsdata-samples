from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.url import Url

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class FareRemark:
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    text: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    url: list[Url] = field(
        default_factory=list,
        metadata={
            "name": "URL",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        },
    )
