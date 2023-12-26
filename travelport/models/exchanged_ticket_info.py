from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class ExchangedTicketInfo:
    """
    Contains Exchanged/Reissued Ticket Information.

    Parameters
    ----------
    number
        Original Ticket that was Exchange/Reissued
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    number: None | str = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
            "required": True,
            "length": 13,
        },
    )
