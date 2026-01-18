from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class SeatStatusSimType:
    type_value: str = field(
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    command: None | str = field(
        default=None,
        metadata={
            "name": "Command",
            "type": "Attribute",
        },
    )
