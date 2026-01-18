from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_1 import BaseReq1
from travelport.models.hotel_property import HotelProperty
from travelport.models.hotel_rate_detail import HotelRateDetail

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass(kw_only=True)
class HotelUpsellDetailsReq(BaseReq1):
    """
    Upsell Request to retrieve the details of a hotel property.

    Parameters
    ----------
    hotel_property
    hotel_rate_detail
        Only returned if number of adults and   checkin/checkout given on
        request
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    hotel_property: HotelProperty = field(
        metadata={
            "name": "HotelProperty",
            "type": "Element",
            "required": True,
        }
    )
    hotel_rate_detail: None | HotelRateDetail = field(
        default=None,
        metadata={
            "name": "HotelRateDetail",
            "type": "Element",
        },
    )
