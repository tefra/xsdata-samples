from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.location_1 import Location1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class CoordinateLocation1(Location1):
    """
    Specific lat/long location, usually associated with a Distance.
    """
    class Meta:
        name = "CoordinateLocation"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    latitude: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    longitude: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
