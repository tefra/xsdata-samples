from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.vehicle_upsell_offer import VehicleUpsellOffer
from travelport.models.vehicle_upsell_qualify import VehicleUpsellQualify

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class VehicleUpsellSearchResult:
    """
    Vehicle upsell search criteria result having matching offer and
    qualifies.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    vehicle_upsell_qualify: list[VehicleUpsellQualify] = field(
        default_factory=list,
        metadata={
            "name": "VehicleUpsellQualify",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    vehicle_upsell_offer: None | VehicleUpsellOffer = field(
        default=None,
        metadata={
            "name": "VehicleUpsellOffer",
            "type": "Element",
            "required": True,
        },
    )
