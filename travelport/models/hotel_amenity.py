from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_amenity_level import TypeAmenityLevel

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class HotelAmenity:
    """
    Parameters
    ----------
    level
        Property or Room amenity
    amenity_code
        OTA amenity code
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    level: None | TypeAmenityLevel = field(
        default=None,
        metadata={
            "name": "Level",
            "type": "Attribute",
            "required": True,
        },
    )
    amenity_code: None | int = field(
        default=None,
        metadata={
            "name": "AmenityCode",
            "type": "Attribute",
            "required": True,
            "total_digits": 3,
        },
    )
