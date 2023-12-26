from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_event_type_5 import TypeEventType5
from travelport.models.type_time_range_5 import TypeTimeRange5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class SearchEvent5(TypeTimeRange5):
    """
    Search for various reservation events.
    """

    class Meta:
        name = "SearchEvent"
        namespace = "http://www.travelport.com/schema/common_v34_0"

    type_value: None | TypeEventType5 = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
