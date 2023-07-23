from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.hotel_upsell_offer import HotelUpsellOffer
from travelport.models.hotel_upsell_qualify import HotelUpsellQualify

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class HotelUpsellRule:
    """
    Binds an HotelUpsellQualify and HotelUpsellOffer.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    hotel_upsell_qualify: None | HotelUpsellQualify = field(
        default=None,
        metadata={
            "name": "HotelUpsellQualify",
            "type": "Element",
        }
    )
    hotel_upsell_offer: None | HotelUpsellOffer = field(
        default=None,
        metadata={
            "name": "HotelUpsellOffer",
            "type": "Element",
        }
    )
