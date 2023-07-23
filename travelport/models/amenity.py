from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class Amenity:
    """
    Parameters
    ----------
    code
    amenity_type
        Amenity type code. “HA” (Hotel Property Amenity) or “RA” (Room
        Amenity). Defaults to “HA” if no value is sent.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    code: None | int = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999,
        }
    )
    amenity_type: None | str = field(
        default=None,
        metadata={
            "name": "AmenityType",
            "type": "Attribute",
            "length": 2,
        }
    )
