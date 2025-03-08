from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class SurchargesType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    ind: None | str = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Attribute",
        },
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
