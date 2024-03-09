from __future__ import annotations

from dataclasses import dataclass

from travelport.models.base_hotel_search_req import BaseHotelSearchReq

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class HotelSearchAvailabilityReq(BaseHotelSearchReq):
    """
    Request to search for hotel availability.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"
