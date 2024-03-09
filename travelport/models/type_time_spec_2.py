from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_specific_time_2 import TypeSpecificTime2
from travelport.models.type_time_range_2 import TypeTimeRange2

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class TypeTimeSpec2:
    """
    Specifies times as either specific times, or a time range.

    Parameters
    ----------
    time_range
    specific_time
    preferred_time
        Specifies a time that would be preferred within the time range
        specified.
    """

    class Meta:
        name = "typeTimeSpec"

    time_range: None | TypeTimeRange2 = field(
        default=None,
        metadata={
            "name": "TimeRange",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v32_0",
        },
    )
    specific_time: None | TypeSpecificTime2 = field(
        default=None,
        metadata={
            "name": "SpecificTime",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v32_0",
        },
    )
    preferred_time: None | str = field(
        default=None,
        metadata={
            "name": "PreferredTime",
            "type": "Attribute",
        },
    )
