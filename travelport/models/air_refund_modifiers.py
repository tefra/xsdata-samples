from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirRefundModifiers:
    """
    Provides controls and switches for the Refund process.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    refund_date: None | str = field(
        default=None,
        metadata={
            "name": "RefundDate",
            "type": "Attribute",
        },
    )
    account_code: None | str = field(
        default=None,
        metadata={
            "name": "AccountCode",
            "type": "Attribute",
        },
    )
    ticket_designator: None | str = field(
        default=None,
        metadata={
            "name": "TicketDesignator",
            "type": "Attribute",
            "min_length": 0,
            "max_length": 20,
        },
    )
