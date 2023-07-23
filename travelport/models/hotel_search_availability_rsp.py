from __future__ import annotations
from dataclasses import dataclass
from travelport.models.base_hotel_search_rsp import BaseHotelSearchRsp

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class HotelSearchAvailabilityRsp(BaseHotelSearchRsp):
    """
    Hotel availablity search response.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"
