from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass(kw_only=True)
class ExpirationDate:
    """
    Expiration Date range.

    For specific date usage set both limits to same value.

    Parameters
    ----------
    earliest_date
        Earliest date of the Expiration date
    latest_date
        Latest date of the Expiration date
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    earliest_date: str = field(
        metadata={
            "name": "EarliestDate",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^:Z].*",
        }
    )
    latest_date: str = field(
        default="9999-12-31",
        metadata={
            "name": "LatestDate",
            "type": "Attribute",
            "pattern": r"[^:Z].*",
        },
    )
