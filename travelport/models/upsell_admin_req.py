from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_upsell_criteria import AirUpsellCriteria
from travelport.models.base_req_1 import BaseReq1
from travelport.models.hotel_upsell_criteria import HotelUpsellCriteria
from travelport.models.vehicle_upsell_criteria import VehicleUpsellCriteria

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass(kw_only=True)
class UpsellAdminReq(BaseReq1):
    """
    Request to add/delete/update qualify/offer.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    air_upsell_criteria: None | AirUpsellCriteria = field(
        default=None,
        metadata={
            "name": "AirUpsellCriteria",
            "type": "Element",
        },
    )
    vehicle_upsell_criteria: None | VehicleUpsellCriteria = field(
        default=None,
        metadata={
            "name": "VehicleUpsellCriteria",
            "type": "Element",
        },
    )
    hotel_upsell_criteria: None | HotelUpsellCriteria = field(
        default=None,
        metadata={
            "name": "HotelUpsellCriteria",
            "type": "Element",
        },
    )
