from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.hotel_detail_item import HotelDetailItem
from travelport.models.hotel_property import HotelProperty
from travelport.models.hotel_rate_detail import HotelRateDetail
from travelport.models.type_result_message_1 import TypeResultMessage1

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class HotelSuperShopperResults:
    """
    Parameters
    ----------
    hotel_property
    hotel_detail_item
    hotel_rate_detail
        Returns hotel rate details during the stay if rates are available
        for requested property
    hotel_results_error
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    hotel_property: None | HotelProperty = field(
        default=None,
        metadata={
            "name": "HotelProperty",
            "type": "Element",
            "required": True,
        },
    )
    hotel_detail_item: list[HotelDetailItem] = field(
        default_factory=list,
        metadata={
            "name": "HotelDetailItem",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    hotel_rate_detail: list[HotelRateDetail] = field(
        default_factory=list,
        metadata={
            "name": "HotelRateDetail",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    hotel_results_error: list[TypeResultMessage1] = field(
        default_factory=list,
        metadata={
            "name": "HotelResultsError",
            "type": "Element",
            "max_occurs": 999,
        },
    )
