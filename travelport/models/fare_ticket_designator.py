from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class FareTicketDesignator:
    """
    Ticket Designator used to further qualify a Fare.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    value: None | str = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "min_length": 0,
            "max_length": 20,
        },
    )
