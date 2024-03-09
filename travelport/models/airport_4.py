from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.location_4 import Location4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass
class Airport4(Location4):
    """
    Airport identifier.
    """

    class Meta:
        name = "Airport"
        namespace = "http://www.travelport.com/schema/common_v37_0"

    code: None | str = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        },
    )
