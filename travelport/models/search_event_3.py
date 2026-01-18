from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_event_type_3 import TypeEventType3
from travelport.models.type_time_range_3 import TypeTimeRange3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass(kw_only=True)
class SearchEvent3(TypeTimeRange3):
    """
    Search for various reservation events.
    """

    class Meta:
        name = "SearchEvent"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    type_value: None | TypeEventType3 = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
