from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass(kw_only=True)
class TypeDateRange3:
    """
    Specify a range of dates.
    """

    class Meta:
        name = "typeDateRange"

    start_date: XmlDate = field(
        metadata={
            "name": "StartDate",
            "type": "Attribute",
            "required": True,
        }
    )
    end_date: XmlDate = field(
        metadata={
            "name": "EndDate",
            "type": "Attribute",
            "required": True,
        }
    )
