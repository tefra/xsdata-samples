from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.guarantee_1 import Guarantee1
from travelport.models.guest_information import GuestInformation
from travelport.models.hotel_bedding import HotelBedding
from travelport.models.hotel_property import HotelProperty
from travelport.models.hotel_rate_detail import HotelRateDetail
from travelport.models.hotel_stay import HotelStay
from travelport.models.promotion_code import PromotionCode

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass(kw_only=True)
class AddHotelSegment:
    """
    Container for Hotel Segment to be added.

    Parameters
    ----------
    hotel_rate_detail
    hotel_property
    hotel_stay
    hotel_bedding
    guest_information
    promotion_code
        Used to specify promotional code include in the booking
    guarantee
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    hotel_rate_detail: HotelRateDetail = field(
        metadata={
            "name": "HotelRateDetail",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "required": True,
        }
    )
    hotel_property: HotelProperty = field(
        metadata={
            "name": "HotelProperty",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "required": True,
        }
    )
    hotel_stay: HotelStay = field(
        metadata={
            "name": "HotelStay",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "required": True,
        }
    )
    hotel_bedding: list[HotelBedding] = field(
        default_factory=list,
        metadata={
            "name": "HotelBedding",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "max_occurs": 4,
        },
    )
    guest_information: None | GuestInformation = field(
        default=None,
        metadata={
            "name": "GuestInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
        },
    )
    promotion_code: None | PromotionCode = field(
        default=None,
        metadata={
            "name": "PromotionCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
        },
    )
    guarantee: None | Guarantee1 = field(
        default=None,
        metadata={
            "name": "Guarantee",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
