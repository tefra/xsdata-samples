from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.hotel_upsell_offer_search_criteria import (
    HotelUpsellOfferSearchCriteria,
)
from travelport.models.hotel_upsell_qualify_search_criteria import (
    HotelUpsellQualifySearchCriteria,
)

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class HotelUpsellSearchCriteria:
    """
    Search criteria for HotelUpsell.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    hotel_upsell_offer_search_criteria: None | HotelUpsellOfferSearchCriteria = field(
        default=None,
        metadata={
            "name": "HotelUpsellOfferSearchCriteria",
            "type": "Element",
        },
    )
    hotel_upsell_qualify_search_criteria: None | HotelUpsellQualifySearchCriteria = field(
        default=None,
        metadata={
            "name": "HotelUpsellQualifySearchCriteria",
            "type": "Element",
            "required": True,
        },
    )
