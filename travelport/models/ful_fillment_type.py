from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass(kw_only=True)
class FulFillmentType:
    """
    Fulfillment options for this segment. the options will be one of
    "Ticket on Departure", "Ticketless", "Ticket By Email", "Travel
    Agency".
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    value: str = field(
        default="",
        metadata={
            "min_length": 0,
            "max_length": 255,
        },
    )
