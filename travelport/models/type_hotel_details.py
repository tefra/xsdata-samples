from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.hotel_detail_item import HotelDetailItem
from travelport.models.hotel_property import HotelProperty
from travelport.models.hotel_rate_detail import HotelRateDetail
from travelport.models.media_item_1 import MediaItem1

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class TypeHotelDetails:
    """
    Hotel Details Type.

    Parameters
    ----------
    hotel_property
    hotel_detail_item
    hotel_rate_detail
        Returns hotel rate details during the stay if rates are available
        for requested property
    media_item
    """

    class Meta:
        name = "typeHotelDetails"

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
    media_item: list[MediaItem1] = field(
        default_factory=list,
        metadata={
            "name": "MediaItem",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
