from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class RatesAndDates:
    """
    Contains the rates that apply over a date range, all with the same
    status.

    May represent multiple rooms.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    status: None | str = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
        },
    )
    start: None | str = field(
        default=None,
        metadata={
            "name": "Start",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^:Z].*",
        },
    )
    end: None | str = field(
        default=None,
        metadata={
            "name": "End",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^:Z].*",
        },
    )
    low: None | str = field(
        default=None,
        metadata={
            "name": "Low",
            "type": "Attribute",
            "required": True,
        },
    )
    high: None | str = field(
        default=None,
        metadata={
            "name": "High",
            "type": "Attribute",
            "required": True,
        },
    )
