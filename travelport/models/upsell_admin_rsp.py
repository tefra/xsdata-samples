from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_upsell_rule import AirUpsellRule
from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.hotel_upsell_rule import HotelUpsellRule
from travelport.models.vehicle_upsell_rule import VehicleUpsellRule

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class UpsellAdminRsp(BaseRsp1):
    """
    Response to add/delete/update of offer/qualify.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    air_upsell_rule: list[AirUpsellRule] = field(
        default_factory=list,
        metadata={
            "name": "AirUpsellRule",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    vehicle_upsell_rule: list[VehicleUpsellRule] = field(
        default_factory=list,
        metadata={
            "name": "VehicleUpsellRule",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    hotel_upsell_rule: list[HotelUpsellRule] = field(
        default_factory=list,
        metadata={
            "name": "HotelUpsellRule",
            "type": "Element",
            "max_occurs": 999,
        },
    )
