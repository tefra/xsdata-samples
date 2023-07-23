from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.rating_range import RatingRange

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class HotelRating:
    """
    Hotel rating information.

    Parameters
    ----------
    rating
        Hotel rating value
    rating_range
        Search for a range of ratings
    rating_provider
        Rating providers, ie AAA, NTM
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    rating: list[int] = field(
        default_factory=list,
        metadata={
            "name": "Rating",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    rating_range: None | RatingRange = field(
        default=None,
        metadata={
            "name": "RatingRange",
            "type": "Element",
        }
    )
    rating_provider: None | str = field(
        default=None,
        metadata={
            "name": "RatingProvider",
            "type": "Attribute",
            "required": True,
        }
    )
