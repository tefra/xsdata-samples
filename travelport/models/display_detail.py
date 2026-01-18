from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_display_detail_name import TypeDisplayDetailName

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass(kw_only=True)
class DisplayDetail:
    """
    Display the contents for requested MCO,Cruise etc. details.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    name: TypeDisplayDetailName = field(
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
        }
    )
    value: str = field(
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        }
    )
