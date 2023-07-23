from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.location_5 import Location5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class CoordinateLocation5(Location5):
    """
    Specific lat/long location, usually associated with a Distance.
    """
    class Meta:
        name = "CoordinateLocation"
        namespace = "http://www.travelport.com/schema/common_v34_0"

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
