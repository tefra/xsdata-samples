from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.vehicle_upsell_offer_search_criteria import VehicleUpsellOfferSearchCriteria
from travelport.models.vehicle_upsell_qualify_search_criteria import VehicleUpsellQualifySearchCriteria

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class VehicleUpsellSearchCriteria:
    """
    Search criteria for VehicleUpsell.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    vehicle_upsell_offer_search_criteria: None | VehicleUpsellOfferSearchCriteria = field(
        default=None,
        metadata={
            "name": "VehicleUpsellOfferSearchCriteria",
            "type": "Element",
        }
    )
    vehicle_upsell_qualify_search_criteria: None | VehicleUpsellQualifySearchCriteria = field(
        default=None,
        metadata={
            "name": "VehicleUpsellQualifySearchCriteria",
            "type": "Element",
            "required": True,
        }
    )
