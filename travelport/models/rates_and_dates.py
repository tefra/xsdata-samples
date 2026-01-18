from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass(kw_only=True)
class RatesAndDates:
    """
    Contains the rates that apply over a date range, all with the same
    status.

    May represent multiple rooms.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    status: str = field(
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
        }
    )
    start: str = field(
        metadata={
            "name": "Start",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^:Z].*",
        }
    )
    end: str = field(
        metadata={
            "name": "End",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^:Z].*",
        }
    )
    low: str = field(
        metadata={
            "name": "Low",
            "type": "Attribute",
            "required": True,
        }
    )
    high: str = field(
        metadata={
            "name": "High",
            "type": "Attribute",
            "required": True,
        }
    )
