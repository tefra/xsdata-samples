from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.hotel_property import HotelProperty

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class HotelAlternateProperties:
    """
    Alternate Properties returned by some Vendors if the requested property is not
    available.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    hotel_property: list[HotelProperty] = field(
        default_factory=list,
        metadata={
            "name": "HotelProperty",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
