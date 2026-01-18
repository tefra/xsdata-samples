from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class VoidFailureInfo:
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    ticket_number: str = field(
        metadata={
            "name": "TicketNumber",
            "type": "Attribute",
            "required": True,
        }
    )
    code: None | int = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
        },
    )
