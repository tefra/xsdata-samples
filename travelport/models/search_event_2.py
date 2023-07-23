from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_event_type_2 import TypeEventType2
from travelport.models.type_time_range_2 import TypeTimeRange2

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class SearchEvent2(TypeTimeRange2):
    """
    Search for various reservation events.
    """
    class Meta:
        name = "SearchEvent"
        namespace = "http://www.travelport.com/schema/common_v32_0"

    type_value: None | TypeEventType2 = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
