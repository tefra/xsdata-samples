from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_event_type_1 import TypeEventType1
from travelport.models.type_time_range_1 import TypeTimeRange1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class SearchEvent1(TypeTimeRange1):
    """
    Search for various reservation events.
    """

    class Meta:
        name = "SearchEvent"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    type_value: None | TypeEventType1 = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
