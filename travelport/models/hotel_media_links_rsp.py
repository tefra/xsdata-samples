from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.hotel_property_with_media_items import HotelPropertyWithMediaItems

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class HotelMediaLinksRsp(BaseRsp1):
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    hotel_property_with_media_items: list[HotelPropertyWithMediaItems] = field(
        default_factory=list,
        metadata={
            "name": "HotelPropertyWithMediaItems",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 20,
        }
    )
