from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.location_3 import Location3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class CoordinateLocation3(Location3):
    """
    Specific lat/long location, usually associated with a Distance.
    """
    class Meta:
        name = "CoordinateLocation"
        namespace = "http://www.travelport.com/schema/common_v33_0"

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
