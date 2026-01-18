from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_event_type_6 import TypeEventType6
from travelport.models.type_time_range_6 import TypeTimeRange6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass(kw_only=True)
class SearchEvent6(TypeTimeRange6):
    """
    Search for various reservation events.
    """

    class Meta:
        name = "SearchEvent"
        namespace = "http://www.travelport.com/schema/common_v38_0"

    type_value: None | TypeEventType6 = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
