from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/gdsQueue_v52_0"


@dataclass
class DateRangeInfo:
    """
    The information related to date range .

    Parameters
    ----------
    date_range
        Date range number where the PNR should be queued. Possible values
        are 1,2,1-4 etc.
    title
        Title of a date range.
    count
        The PNR count of date range.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/gdsQueue_v52_0"

    date_range: None | str = field(
        default=None,
        metadata={
            "name": "DateRange",
            "type": "Attribute",
            "required": True,
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Attribute",
        },
    )
    count: None | int = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Attribute",
            "required": True,
        },
    )
