from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_upsell_offer import AirUpsellOffer
from travelport.models.air_upsell_qualify import AirUpsellQualify

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class AirUpsellAdd:
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    air_upsell_qualify: None | AirUpsellQualify = field(
        default=None,
        metadata={
            "name": "AirUpsellQualify",
            "type": "Element",
            "required": True,
        },
    )
    air_upsell_offer: None | AirUpsellOffer = field(
        default=None,
        metadata={
            "name": "AirUpsellOffer",
            "type": "Element",
        },
    )
