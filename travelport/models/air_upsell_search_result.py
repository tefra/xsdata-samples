from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_upsell_offer import AirUpsellOffer
from travelport.models.air_upsell_qualify import AirUpsellQualify

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass(kw_only=True)
class AirUpsellSearchResult:
    """
    Air upsell search criteria result having matching offer and qualifies.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    air_upsell_qualify: list[AirUpsellQualify] = field(
        default_factory=list,
        metadata={
            "name": "AirUpsellQualify",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    air_upsell_offer: AirUpsellOffer = field(
        metadata={
            "name": "AirUpsellOffer",
            "type": "Element",
            "required": True,
        }
    )
