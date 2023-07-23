from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class TypeDateRange6:
    """
    Specify a range of dates.
    """
    class Meta:
        name = "typeDateRange"

    start_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Attribute",
            "required": True,
        }
    )
    end_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Attribute",
            "required": True,
        }
    )
