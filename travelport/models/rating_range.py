from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class RatingRange:
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    minimum_rating: None | int = field(
        default=None,
        metadata={
            "name": "MinimumRating",
            "type": "Attribute",
        }
    )
    maximum_rating: None | int = field(
        default=None,
        metadata={
            "name": "MaximumRating",
            "type": "Attribute",
        }
    )
