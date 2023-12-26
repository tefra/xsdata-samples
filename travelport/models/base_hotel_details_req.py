from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_1 import BaseReq1
from travelport.models.hotel_details_modifiers import HotelDetailsModifiers
from travelport.models.hotel_property import HotelProperty
from travelport.models.point_of_sale_1 import PointOfSale1

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class BaseHotelDetailsReq(BaseReq1):
    """
    Base request for all hotel details search request..
    """

    hotel_property: None | HotelProperty = field(
        default=None,
        metadata={
            "name": "HotelProperty",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "required": True,
        },
    )
    hotel_details_modifiers: None | HotelDetailsModifiers = field(
        default=None,
        metadata={
            "name": "HotelDetailsModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
        },
    )
    point_of_sale: None | PointOfSale1 = field(
        default=None,
        metadata={
            "name": "PointOfSale",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
