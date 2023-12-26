from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_search_rsp_1 import BaseSearchRsp1
from travelport.models.currency_rate_conversion import CurrencyRateConversion
from travelport.models.hotel_super_shopper_results import (
    HotelSuperShopperResults,
)
from travelport.models.quick_response import QuickResponse
from travelport.models.vendor_location_1 import VendorLocation1

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class HotelSuperShopperRsp(BaseSearchRsp1):
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    vendor_location: list[VendorLocation1] = field(
        default_factory=list,
        metadata={
            "name": "VendorLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    currency_rate_conversion: list[CurrencyRateConversion] = field(
        default_factory=list,
        metadata={
            "name": "CurrencyRateConversion",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    hotel_super_shopper_results: list[HotelSuperShopperResults] = field(
        default_factory=list,
        metadata={
            "name": "HotelSuperShopperResults",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    quick_response: None | QuickResponse = field(
        default=None,
        metadata={
            "name": "QuickResponse",
            "type": "Element",
        },
    )
