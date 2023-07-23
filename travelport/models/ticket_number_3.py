from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class TicketNumber3:
    """
    The identifying number for the actual ticket.
    """
    class Meta:
        name = "TicketNumber"
        namespace = "http://www.travelport.com/schema/common_v32_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "max_length": 13,
        }
    )
