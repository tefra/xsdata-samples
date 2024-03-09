from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class ValueDetails:
    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
        },
    )
    value: None | str = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        },
    )
