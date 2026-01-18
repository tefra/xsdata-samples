from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_upsell_offer_search_criteria import (
    AirUpsellOfferSearchCriteria,
)
from travelport.models.air_upsell_qualify_search_criteria import (
    AirUpsellQualifySearchCriteria,
)

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass(kw_only=True)
class AirUpsellSearchCriteria:
    """
    Search criteria for AirUpsell.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    air_upsell_offer_search_criteria: None | AirUpsellOfferSearchCriteria = (
        field(
            default=None,
            metadata={
                "name": "AirUpsellOfferSearchCriteria",
                "type": "Element",
            },
        )
    )
    air_upsell_qualify_search_criteria: AirUpsellQualifySearchCriteria = field(
        metadata={
            "name": "AirUpsellQualifySearchCriteria",
            "type": "Element",
            "required": True,
        }
    )
