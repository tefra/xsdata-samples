from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.location_3 import Location3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class City3(Location3):
    """
    City identifier.
    """

    class Meta:
        name = "City"
        namespace = "http://www.travelport.com/schema/common_v33_0"

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
