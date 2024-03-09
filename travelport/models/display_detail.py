from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_display_detail_name import TypeDisplayDetailName

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class DisplayDetail:
    """Display the contents for requested MCO,Cruise etc.

    details
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    name: None | TypeDisplayDetailName = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
        },
    )
    value: None | str = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        },
    )
