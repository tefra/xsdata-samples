from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.location_6 import Location6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class CoordinateLocation6(Location6):
    """
    Specific lat/long location, usually associated with a Distance.
    """

    class Meta:
        name = "CoordinateLocation"
        namespace = "http://www.travelport.com/schema/common_v38_0"

    latitude: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    longitude: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
