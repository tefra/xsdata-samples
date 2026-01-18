from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class TicketNumberHistory2:
    """
    The identifying number for the actual ticket.
    """

    class Meta:
        name = "TicketNumberHistory"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 0,
            "max_length": 13,
        },
    )
