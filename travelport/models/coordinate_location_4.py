from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.location_4 import Location4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass(kw_only=True)
class CoordinateLocation4(Location4):
    """
    Specific lat/long location, usually associated with a Distance.
    """

    class Meta:
        name = "CoordinateLocation"
        namespace = "http://www.travelport.com/schema/common_v37_0"

    latitude: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    longitude: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
