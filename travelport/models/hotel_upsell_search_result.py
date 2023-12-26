from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.hotel_upsell_offer import HotelUpsellOffer
from travelport.models.hotel_upsell_qualify import HotelUpsellQualify

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class HotelUpsellSearchResult:
    """
    Hotel upsell search criteria result having matching offer and qualifies.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    hotel_upsell_qualify: list[HotelUpsellQualify] = field(
        default_factory=list,
        metadata={
            "name": "HotelUpsellQualify",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    hotel_upsell_offer: None | HotelUpsellOffer = field(
        default=None,
        metadata={
            "name": "HotelUpsellOffer",
            "type": "Element",
            "required": True,
        },
    )
