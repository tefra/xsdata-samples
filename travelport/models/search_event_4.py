from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_event_type_4 import TypeEventType4
from travelport.models.type_time_range_4 import TypeTimeRange4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass(kw_only=True)
class SearchEvent4(TypeTimeRange4):
    """
    Search for various reservation events.
    """

    class Meta:
        name = "SearchEvent"
        namespace = "http://www.travelport.com/schema/common_v37_0"

    type_value: None | TypeEventType4 = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
