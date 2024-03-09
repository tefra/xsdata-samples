from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

from travelport.models.type_date_range_1 import TypeDateRange1

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class TypeDateSpec:
    """
    Specifies dates as either specific date or a date range.
    """

    class Meta:
        name = "typeDateSpec"

    date_range: None | TypeDateRange1 = field(
        default=None,
        metadata={
            "name": "DateRange",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/universal_v52_0",
        },
    )
    specific_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "SpecificDate",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/universal_v52_0",
        },
    )
