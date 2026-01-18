from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_search_req_1 import BaseSearchReq1
from travelport.models.hotel_search_location import HotelSearchLocation
from travelport.models.hotel_search_modifiers import HotelSearchModifiers
from travelport.models.hotel_stay import HotelStay
from travelport.models.quick_response import QuickResponse

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass(kw_only=True)
class HotelSuperShopperReq(BaseSearchReq1):
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    hotel_search_location: None | HotelSearchLocation = field(
        default=None,
        metadata={
            "name": "HotelSearchLocation",
            "type": "Element",
        },
    )
    hotel_search_modifiers: None | HotelSearchModifiers = field(
        default=None,
        metadata={
            "name": "HotelSearchModifiers",
            "type": "Element",
        },
    )
    hotel_stay: HotelStay = field(
        metadata={
            "name": "HotelStay",
            "type": "Element",
            "required": True,
        }
    )
    quick_response: None | QuickResponse = field(
        default=None,
        metadata={
            "name": "QuickResponse",
            "type": "Element",
        },
    )
