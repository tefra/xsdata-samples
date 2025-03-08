from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class SeatStatusSimType:
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )
    command: None | str = field(
        default=None,
        metadata={
            "name": "Command",
            "type": "Attribute",
        },
    )
