from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.amenity import Amenity

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class Amenities:
    """
    Amenity information.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    amenity: list[Amenity] = field(
        default_factory=list,
        metadata={
            "name": "Amenity",
            "type": "Element",
            "max_occurs": 999,
        },
    )
