from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_upsell_search_criteria import (
    AirUpsellSearchCriteria,
)
from travelport.models.base_req_1 import BaseReq1
from travelport.models.hotel_upsell_search_criteria import (
    HotelUpsellSearchCriteria,
)
from travelport.models.upsell_search_modifier import UpsellSearchModifier
from travelport.models.vehicle_upsell_search_criteria import (
    VehicleUpsellSearchCriteria,
)

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class UpsellSearchReq(BaseReq1):
    """
    Request to retrieve all upsell qualify/offers based on search criteria for
    air,hotel and vehicle.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    air_upsell_search_criteria: None | AirUpsellSearchCriteria = field(
        default=None,
        metadata={
            "name": "AirUpsellSearchCriteria",
            "type": "Element",
        },
    )
    hotel_upsell_search_criteria: None | HotelUpsellSearchCriteria = field(
        default=None,
        metadata={
            "name": "HotelUpsellSearchCriteria",
            "type": "Element",
        },
    )
    vehicle_upsell_search_criteria: None | VehicleUpsellSearchCriteria = field(
        default=None,
        metadata={
            "name": "VehicleUpsellSearchCriteria",
            "type": "Element",
        },
    )
    upsell_search_modifier: None | UpsellSearchModifier = field(
        default=None,
        metadata={
            "name": "UpsellSearchModifier",
            "type": "Element",
            "required": True,
        },
    )
