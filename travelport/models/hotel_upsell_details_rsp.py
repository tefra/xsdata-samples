from __future__ import annotations
from dataclasses import dataclass
from travelport.models.base_hotel_details_rsp import BaseHotelDetailsRsp

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class HotelUpsellDetailsRsp(BaseHotelDetailsRsp):
    """
    Upsell Response showing details of a given hotel property.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"
