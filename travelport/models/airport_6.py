from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.location_6 import Location6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class Airport6(Location6):
    """
    Airport identifier.
    """

    class Meta:
        name = "Airport"
        namespace = "http://www.travelport.com/schema/common_v38_0"

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
