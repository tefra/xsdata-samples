from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class DateRangeType:
    """
    Attributes:
        outbound_date: Outbound date
        date_range: Number of date range
    """

    outbound_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "OutboundDate",
            "type": "Attribute",
        },
    )
    date_range: None | int = field(
        default=None,
        metadata={
            "name": "DateRange",
            "type": "Attribute",
        },
    )
