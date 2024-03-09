from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.vehicle_upsell_offer import VehicleUpsellOffer
from travelport.models.vehicle_upsell_qualify import VehicleUpsellQualify

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class VehicleUpsellUpdate:
    """
    Update command for updating VehicleUpsellQualify,VehicleUpsellOffer.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    vehicle_upsell_qualify: None | VehicleUpsellQualify = field(
        default=None,
        metadata={
            "name": "VehicleUpsellQualify",
            "type": "Element",
        },
    )
    vehicle_upsell_offer: None | VehicleUpsellOffer = field(
        default=None,
        metadata={
            "name": "VehicleUpsellOffer",
            "type": "Element",
        },
    )
