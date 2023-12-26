from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.hotel_detail_item import HotelDetailItem
from travelport.models.hotel_property import HotelProperty
from travelport.models.hotel_rate_detail import HotelRateDetail

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class BaseHotelDetailsRsp(BaseRsp1):
    """
    Base response for all hotel details search response.

    Parameters
    ----------
    hotel_property
    hotel_detail_item
    hotel_rate_detail
        Only returned if number of adults and checkin/checkout given on
        request
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
    hotel_detail_item: list[HotelDetailItem] = field(
        default_factory=list,
        metadata={
            "name": "HotelDetailItem",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "max_occurs": 999,
        },
    )
    hotel_rate_detail: list[HotelRateDetail] = field(
        default_factory=list,
        metadata={
            "name": "HotelRateDetail",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "max_occurs": 999,
        },
    )
