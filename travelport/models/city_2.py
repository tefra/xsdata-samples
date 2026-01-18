from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.location_2 import Location2

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass(kw_only=True)
class City2(Location2):
    """
    City identifier.
    """

    class Meta:
        name = "City"
        namespace = "http://www.travelport.com/schema/common_v32_0"

    code: str = field(
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
