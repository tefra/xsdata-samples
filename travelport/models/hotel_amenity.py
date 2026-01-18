from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_amenity_level import TypeAmenityLevel

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass(kw_only=True)
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

    level: TypeAmenityLevel = field(
        metadata={
            "name": "Level",
            "type": "Attribute",
            "required": True,
        }
    )
    amenity_code: int = field(
        metadata={
            "name": "AmenityCode",
            "type": "Attribute",
            "required": True,
            "total_digits": 3,
        }
    )
