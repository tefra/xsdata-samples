from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/uprofileCommon_v30_0"


@dataclass(kw_only=True)
class TicketNumber2:
    """
    The identifying number for the actual ticket.
    """

    class Meta:
        name = "TicketNumber"
        namespace = "http://www.travelport.com/schema/uprofileCommon_v30_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "max_length": 13,
        },
    )
