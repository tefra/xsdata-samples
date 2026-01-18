from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class TicketDesignator:
    """
    Ticket Designator used to further qualify a Fare Basis Code.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    value: str = field(
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
            "min_length": 0,
            "max_length": 20,
        }
    )
