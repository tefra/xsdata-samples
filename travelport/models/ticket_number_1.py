from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass(kw_only=True)
class TicketNumber1:
    """
    The identifying number for the actual ticket.
    """

    class Meta:
        name = "TicketNumber"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "max_length": 13,
        },
    )
